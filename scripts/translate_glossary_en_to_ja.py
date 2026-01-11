#!/usr/bin/env python3
"""Translate English glossary markdown files to Japanese using Claude API.

AUTO-UPDATE CSV STATUS: After translation, automatically updates CSV with completion status.

Usage:
  python scripts/translate_glossary_en_to_ja.py --one-file File.md
  python scripts/translate_glossary_en_to_ja.py  # Translate all
"""

import argparse
import datetime
import os
import re
import textwrap
import csv
from pathlib import Path
from typing import Dict, Tuple, Optional, Iterable, List
from concurrent.futures import ThreadPoolExecutor, as_completed

import yaml

try:
    from dotenv import load_dotenv
    load_dotenv(dotenv_path=Path(__file__).resolve().parents[1] / ".env")
except ImportError:
    pass

try:
    import anthropic
except ImportError:
    anthropic = None


FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n(.*)$", re.DOTALL)
DEFAULT_STYLE_GUIDE = textwrap.dedent(
    """# FlowHunt Glossary Translation Guide
- Maintain a professional yet approachable tone suitable for enterprise readers.
- Prefer standard Japanese technical terms; keep product names in English if commonly used.
- Use Japanese punctuation (、。) and full-width brackets when appropriate.
- When translating bullet lists, keep indentation and marker style identical to the source.
- Keep measurements, code snippets, CLI commands, URLs, and file paths exactly as provided.
"""
).strip()


def parse_markdown_with_frontmatter(text: str) -> Tuple[Dict, str]:
    m = FRONTMATTER_RE.match(text)
    if not m:
        return {}, text
    fm_raw, body = m.groups()
    try:
        fm = yaml.safe_load(fm_raw) or {}
    except Exception:
        fm = {}
    return fm, body


def dump_markdown_with_frontmatter(frontmatter: Dict, body: str) -> str:
    fm_yaml = yaml.safe_dump(frontmatter, allow_unicode=True, sort_keys=False).strip()
    return f"---\n{fm_yaml}\n---\n\n{body.lstrip()}"


def build_claude_client() -> "anthropic.Anthropic":
    api_key = os.getenv("CLAUDE_API_KEY") or os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        raise RuntimeError(
            "CLAUDE_API_KEY (or fallback ANTHROPIC_API_KEY) is not set.\n"
            "Either export it or add to .env file in project root."
        )
    if anthropic is None:
        raise RuntimeError("anthropic package is not installed. Run: pip install anthropic")
    return anthropic.Anthropic(api_key=api_key)


def check_translation_complete(en_body: str, ja_body: str) -> Tuple[bool, str]:
    en_headings = re.findall(r"^(#{1,4})\s+(.+)$", en_body, re.MULTILINE)
    ja_headings = re.findall(r"^(#{1,4})\s+(.+)$", ja_body, re.MULTILINE)

    en_h2_count = sum(1 for h in en_headings if h[0] == "##")
    ja_h2_count = sum(1 for h in ja_headings if h[0] == "##")

    en_lines = len([l for l in en_body.strip().splitlines() if l.strip()])
    ja_lines = len([l for l in ja_body.strip().splitlines() if l.strip()])

    issues = []
    if ja_h2_count < en_h2_count:
        issues.append(f"見出し不足: EN={en_h2_count} vs JA={ja_h2_count}")
    if ja_lines < en_lines * 0.7:
        issues.append(f"行数不足: EN={en_lines} vs JA={ja_lines} (70%未満)")

    if issues:
        return False, "; ".join(issues)
    return True, "OK"


def chunked(seq: List[Path], size: int) -> Iterable[List[Path]]:
    for idx in range(0, len(seq), size):
        yield seq[idx : idx + size]


class ClaudeTranslator:
    def __init__(
        self,
        client,
        *,
        model: str,
        style_guide: Optional[str],
        temperature: float = 0.2,
        max_tokens: int = 16000,
    ) -> None:
        self.client = client
        self.model = model
        self.style_guide = style_guide.strip() if style_guide else None
        self.temperature = temperature
        self.max_tokens = max_tokens

    def _run(self, *, user_text: str, system_prompt: str) -> str:
        system_full = system_prompt
        if self.style_guide:
            system_full = f"{self.style_guide}\n\n{system_prompt}".strip()

        resp = self.client.messages.create(
            model=self.model,
            max_tokens=self.max_tokens,
            temperature=self.temperature,
            system=system_full,
            messages=[{"role": "user", "content": [{"type": "text", "text": user_text}]}],
        )
        chunks: List[str] = []
        for block in resp.content:
            if getattr(block, "type", None) == "text":
                chunks.append(block.text)
        return "".join(chunks).strip()

    def translate_body(self, body_md: str) -> str:
        body_prompt = textwrap.dedent(
            """You are translating a technical glossary body from English to natural, professional Japanese.

- Input is Markdown.
- Preserve Markdown structure (headings, lists, code blocks, links, emphasis) exactly.
- Translate all prose into Japanese.
- Do NOT translate code inside fenced code blocks or inline code (backticks). Keep code as-is.
- Translate link anchor text, but keep URLs unchanged.

Return ONLY the translated Markdown body, with no extra commentary.
"""
        ).strip()
        return self._run(user_text=body_md, system_prompt=body_prompt)

    def translate_body_batch(self, docs: List[Dict[str, str]]) -> Dict[str, str]:
        batch_instructions = textwrap.dedent(
            """You are translating multiple glossary documents from English to Japanese.
Documents are delimited as follows:

<<DOC slug>>
<markdown body>
<<END DOC>>

Return the same delimiters and slugs, replacing the content with the translated Japanese Markdown. Do not add commentary.
"""
        ).strip()

        sections = []
        for doc in docs:
            sections.append(f"<<DOC {doc['slug']}>>\n{doc['body']}\n<<END DOC>>")
        user_payload = batch_instructions + "\n\n" + "\n\n".join(sections)
        output = self._run(user_text=user_payload, system_prompt="Batch translation for multiple Markdown documents.")

        pattern = re.compile(r"<<DOC (?P<slug>[^>]+)>>\s*(?P<body>.*?)\s*<<END DOC>>", re.DOTALL)
        results: Dict[str, str] = {}
        for match in pattern.finditer(output):
            results[match.group("slug")] = match.group("body").strip()
        if len(results) != len(docs):
            raise ValueError("Batch translation response missing documents or malformed delimiters")
        return results

    def translate_meta(self, title: str, description: str, keywords: List[str]) -> Tuple[str, str, List[str], str]:
        meta_prompt = f"""TITLE:
{title}

DESCRIPTION:
{description}

KEYWORDS (comma separated):
{', '.join(map(str, keywords))}

Please translate these into Japanese and respond ONLY in the following format:

TITLE_JA: <Japanese title>
TERM_JA: <reading of the title in Japanese kana. Start with hiragana/katakana, avoid kanji if possible>
DESCRIPTION_JA: <Japanese description>
KEYWORDS_JA: <keyword1>, <keyword2>, ...
"""
        meta_system = "You are translating glossary metadata (title, description, keywords) from English to Japanese. Follow the requested output format exactly."
        meta_text = self._run(user_text=meta_prompt, system_prompt=meta_system)

        title_ja = title
        desc_ja = description
        term_ja: str | None = None
        keywords_ja: List[str] = []
        for line in meta_text.splitlines():
            line = line.strip()
            if line.startswith("TITLE_JA:"):
                title_ja = line[len("TITLE_JA:") :].strip()
            elif line.startswith("TERM_JA:"):
                term_ja = line[len("TERM_JA:") :].strip()
            elif line.startswith("DESCRIPTION_JA:"):
                desc_ja = line[len("DESCRIPTION_JA:") :].strip()
            elif line.startswith("KEYWORDS_JA:"):
                raw = line[len("KEYWORDS_JA:") :].strip()
                if raw:
                    keywords_ja = [k.strip() for k in raw.split(",") if k.strip()]
        return title_ja, term_ja or title, keywords_ja or keywords, desc_ja


def find_existing_ja_slugs(ja_dir: Path) -> set:
    return {p.stem for p in ja_dir.glob("*.md")}


def rewrite_internal_links(body_ja: str, existing_ja_slugs: set) -> str:
    def repl(match: re.Match) -> str:
        full = match.group(0)
        slug = match.group("slug")
        if slug in existing_ja_slugs:
            return full.replace("/en/", "/ja/")
        return full

    pattern = re.compile(r"/en/glossary/(?P<slug>[^/]+)/")
    return pattern.sub(repl, body_ja)


def _iter_markdown_lines_outside_fences(body: str):
    in_fence = False
    for line in body.splitlines(keepends=True):
        stripped = line.lstrip()
        if stripped.startswith("```"):
            in_fence = not in_fence
            yield line, True
            continue
        yield line, not in_fence


def _count_headings_by_level(body: str) -> Dict[int, int]:
    counts = {i: 0 for i in range(1, 7)}
    for line, enabled in _iter_markdown_lines_outside_fences(body):
        if not enabled:
            continue
        m = re.match(r"^(#{1,6})\s+", line)
        if m:
            counts[len(m.group(1))] += 1
    return counts


def normalize_body_headings(en_body: str, ja_body: str) -> str:
    en_counts = _count_headings_by_level(en_body)
    ja_counts = _count_headings_by_level(ja_body)

    if en_counts.get(1, 0) != 0:
        return ja_body
    if ja_counts.get(1, 0) == 0:
        return ja_body

    shift_all = ja_counts.get(1, 0) >= 2

    out_lines: List[str] = []
    for line, enabled in _iter_markdown_lines_outside_fences(ja_body):
        if not enabled:
            out_lines.append(line)
            continue
        m = re.match(r"^(#{1,6})(\s+)(.*)$", line)
        if not m:
            out_lines.append(line)
            continue
        hashes, ws, rest = m.groups()
        if shift_all:
            new_level = min(6, len(hashes) + 1)
            out_lines.append("#" * new_level + ws + rest)
            continue
        if len(hashes) == 1:
            out_lines.append("##" + ws + rest)
            continue
        out_lines.append(line)

    return "".join(out_lines)


def translate_markdown_file(
    translator: ClaudeTranslator,
    src_path: Path,
    dst_path: Path,
    existing_ja_slugs: set,
    *,
    body_override: Optional[str] = None,
    override_date: Optional[str] = None,
) -> None:
    raw = src_path.read_text(encoding="utf-8")
    fm, body = parse_markdown_with_frontmatter(raw)

    title_en = fm.get("title", "")
    e_title = fm.get("e-title", title_en)
    desc_en = fm.get("description", "")
    keywords_en = fm.get("keywords", []) or []

    body_ja = body_override or translator.translate_body(body)
    body_ja = normalize_body_headings(body, body_ja)

    title_ja, term_ja, keywords_ja, desc_ja = translator.translate_meta(title_en, desc_en, keywords_en)
    body_ja = rewrite_internal_links(body_ja, existing_ja_slugs)

    fm_ja = dict(fm)
    fm_ja["title"] = title_ja
    fm_ja["e-title"] = e_title or title_en
    
    filename_stem = src_path.stem
    fm_ja["url"] = f"/ja/glossary/{filename_stem.lower()}/"
    
    if "term" not in fm_ja or not fm_ja.get("term"):
        fm_ja["term"] = term_ja or title_ja

    if fm_ja.get("translationKey") == "autonomous-agents":
        fm_ja["term"] = "じりつがたエージェント"
    if desc_ja:
        fm_ja["description"] = desc_ja
    if keywords_ja:
        fm_ja["keywords"] = keywords_ja

    if override_date:
        fm_ja["date"] = override_date
        fm_ja["lastmod"] = override_date

    dst_path.parent.mkdir(parents=True, exist_ok=True)
    dst_text = dump_markdown_with_frontmatter(fm_ja, body_ja)
    dst_path.write_text(dst_text, encoding="utf-8")

    is_complete, check_msg = check_translation_complete(body, body_ja)
    if is_complete:
        print(f"✓ Translated {src_path.name} -> {dst_path.name}")
    else:
        print(f"⚠ Translated {src_path.name} -> {dst_path.name} [INCOMPLETE: {check_msg}]")


def load_style_guide(path: Optional[str]) -> str:
    if not path:
        return DEFAULT_STYLE_GUIDE
    file_path = Path(path)
    if not file_path.exists():
        raise FileNotFoundError(f"Style guide file not found: {file_path}")
    return file_path.read_text(encoding="utf-8")


def update_csv_status(csv_path: Path, en_dir: Path, ja_dir: Path) -> int:
    """CSVステータスを実ファイル存在状況に基づいて自動更新"""
    
    if not csv_path.exists():
        print(f"⚠️  CSV not found: {csv_path}")
        return 0
    
    # CSVを読み込み
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fieldnames = list(reader.fieldnames or [])
        rows = list(reader)
    
    # status列がない場合は追加
    if 'status_en' not in fieldnames:
        fieldnames.append('status_en')
    if 'status_ja' not in fieldnames:
        fieldnames.append('status_ja')
    
    # 各行のステータスを更新
    updated_count = 0
    for row in rows:
        filename = row.get('filename', '')
        if not filename:
            continue
        
        en_file = en_dir / filename
        ja_file = ja_dir / filename
        
        old_status_en = row.get('status_en', 'pending')
        old_status_ja = row.get('status_ja', 'pending')
        
        new_status_en = 'completed' if en_file.exists() else 'pending'
        new_status_ja = 'completed' if ja_file.exists() else 'pending'
        
        row['status_en'] = new_status_en
        row['status_ja'] = new_status_ja
        
        if old_status_en != new_status_en or old_status_ja != new_status_ja:
            updated_count += 1
    
    # CSVに書き戻し
    with open(csv_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    
    if updated_count > 0:
        print(f"📊 CSV updated: {updated_count} status changes")
    
    return updated_count


def main() -> None:
    parser = argparse.ArgumentParser(description="Translate English glossary Markdown files to Japanese using Claude API.")
    parser.add_argument("--source-dir", default="content/en/glossary", help="Source directory for English glossary .md files")
    parser.add_argument("--target-dir", default="content/ja/glossary", help="Target directory for Japanese glossary .md files")
    parser.add_argument("--one-file", help="Translate only this filename (e.g., autonomous-agents.md)")
    parser.add_argument(
        "--set-date-today",
        action="store_true",
        help="Overwrite frontmatter date/lastmod in generated Japanese files with today's date (YYYY-MM-DD)",
    )
    parser.add_argument(
        "--skip-existing",
        action="store_true",
        help="Skip translation if the target Japanese file already exists (do not overwrite)",
    )
    parser.add_argument("--model", default="claude-sonnet-4-5-20250929", help="Claude model name (default: %(default)s)")
    parser.add_argument(
        "--style-guide",
        help="Optional Markdown/Plaintext style guide injected via prompt caching",
    )
    parser.add_argument(
        "--batch-size",
        type=int,
        default=1,
        help="Number of files to bundle per body translation request (>=2 enables batch mode)",
    )
    parser.add_argument(
        "--max-workers",
        type=int,
        default=4,
        help="Max worker threads for parallel translation when --batch-size=1 (default: %(default)s)",
    )
    parser.add_argument(
        "--skip-csv-update",
        action="store_true",
        help="Skip automatic CSV status update after translation",
    )
    parser.add_argument(
        "--csv-path",
        default="docs/prioritized_keywords.csv",
        help="Path to CSV file for status tracking (default: %(default)s)",
    )
    args = parser.parse_args()

    src_dir = Path(args.source_dir)
    dst_dir = Path(args.target_dir)

    client = build_claude_client()
    style_text = load_style_guide(args.style_guide)
    translator = ClaudeTranslator(client, model=args.model, style_guide=style_text)

    existing_ja_slugs = find_existing_ja_slugs(dst_dir)

    override_date = datetime.date.today().isoformat() if args.set_date_today else None

    if args.one_file:
        src_path = src_dir / args.one_file
        if not src_path.exists():
            raise SystemExit(f"Source file not found: {src_path}")
        existing_ja_slugs.add(src_path.stem)
        dst_path = dst_dir / src_path.name
        if args.skip_existing and dst_path.exists():
            print(f"- Skipped (exists): {dst_path}")
            return
        translate_markdown_file(
            translator,
            src_path,
            dst_path,
            existing_ja_slugs,
            override_date=override_date,
        )
        
        # 翻訳完了後、CSV自動更新
        if not args.skip_csv_update:
            csv_path = Path(args.csv_path)
            if csv_path.exists():
                update_csv_status(csv_path, src_dir, dst_dir)
        
        return

    src_files = sorted(src_dir.glob("*.md"))
    if args.skip_existing:
        src_files = [p for p in src_files if not (dst_dir / p.name).exists()]
    if not src_files:
        print(f"No markdown files found in {src_dir}")
        return

    existing_ja_slugs |= {p.stem for p in src_files}

    batch_size = max(1, args.batch_size)
    if batch_size == 1:
        max_workers = min(max(1, args.max_workers), len(src_files))
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = {
                executor.submit(
                    translate_markdown_file,
                    translator,
                    src_path,
                    dst_dir / src_path.name,
                    existing_ja_slugs,
                    override_date=override_date,
                ): src_path
                for src_path in src_files
            }

            for fut in as_completed(futures):
                src = futures[fut]
                try:
                    fut.result()
                except Exception as e:
                    print(f"Error translating {src}: {e}")
        
        # 全翻訳完了後、CSV自動更新
        if not args.skip_csv_update:
            csv_path = Path(args.csv_path)
            if csv_path.exists():
                update_csv_status(csv_path, src_dir, dst_dir)
        
        return

    for chunk_paths in chunked(src_files, batch_size):
        docs = []
        for src_path in chunk_paths:
            raw = src_path.read_text(encoding="utf-8")
            _, body = parse_markdown_with_frontmatter(raw)
            docs.append({"slug": src_path.name, "body": body})
        try:
            translated_map = translator.translate_body_batch(docs)
        except Exception as exc:
            print(f"Batch translation failed for {[p.name for p in chunk_paths]}: {exc}")
            for src_path in chunk_paths:
                try:
                    translate_markdown_file(
                        translator,
                        src_path,
                        dst_dir / src_path.name,
                        existing_ja_slugs,
                        override_date=override_date,
                    )
                except Exception as e:
                    print(f"Error translating {src_path}: {e}")
            continue

        for src_path in chunk_paths:
            body_override = translated_map.get(src_path.name)
            if not body_override:
                print(f"Missing batch result for {src_path}")
                try:
                    translate_markdown_file(
                        translator,
                        src_path,
                        dst_dir / src_path.name,
                        existing_ja_slugs,
                        override_date=override_date,
                    )
                except Exception as e:
                    print(f"Error translating {src_path}: {e}")
                continue
            try:
                translate_markdown_file(
                    translator,
                    src_path,
                    dst_dir / src_path.name,
                    existing_ja_slugs,
                    body_override=body_override,
                    override_date=override_date,
                )
            except Exception as e:
                print(f"Error translating {src_path}: {e}")
    
    # 全翻訳完了後、CSV自動更新
    if not args.skip_csv_update:
        csv_path = Path(args.csv_path)
        if csv_path.exists():
            update_csv_status(csv_path, src_dir, dst_dir)


if __name__ == "__main__":
    main()
