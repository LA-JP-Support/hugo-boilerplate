#!/usr/bin/env python3
"""Translate English glossary markdown files to Japanese using Claude API.

- Reads from content/en/glossary/*.md
- Uses Anthropic Claude API (API key from ANTHROPIC_API_KEY env var)
- Writes translated files to content/ja/glossary/ with:
  - title/description/body translated to Japanese
  - translationKey copied as-is
  - keywords translated to Japanese
  - internal links /en/... -> /ja/... only when corresponding ja file exists

Usage (example):

  python scripts/translate_glossary_en_to_ja.py \
      --source-dir content/en/glossary \
      --target-dir content/ja/glossary \
      --one-file autonomous-agents.md

If --one-file is omitted, all .md files in source-dir are processed.
"""

import argparse
import os
import re
import textwrap
from pathlib import Path
from typing import Dict, Tuple, Optional, Iterable, List
from concurrent.futures import ThreadPoolExecutor, as_completed

import yaml

try:
    from dotenv import load_dotenv
    load_dotenv()  # .env ファイルから環境変数を自動読み込み
except ImportError:
    pass  # python-dotenv がなければスキップ

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
    """Parse simple YAML frontmatter and return (frontmatter, body).

    Falls back to empty frontmatter if no frontmatter block is found.
    """
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
    """Check if the Japanese translation covers all major sections of the English source.

    Returns (is_complete, message).
    """
    # 英語原文の見出しを抽出
    en_headings = re.findall(r"^(#{1,4})\s+(.+)$", en_body, re.MULTILINE)
    ja_headings = re.findall(r"^(#{1,4})\s+(.+)$", ja_body, re.MULTILINE)

    en_h2_count = sum(1 for h in en_headings if h[0] == "##")
    ja_h2_count = sum(1 for h in ja_headings if h[0] == "##")

    # 英語原文の行数と日本語訳の行数を比較
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
    """Rewrite /en/... links to /ja/... only when ja slug exists.

    - /en/glossary/slug/  -> /ja/glossary/slug/ if slug exists in ja_dir
    - Other /en/... are left as-is.
    """

    def repl(match: re.Match) -> str:
        full = match.group(0)
        slug = match.group("slug")
        if slug in existing_ja_slugs:
            return full.replace("/en/", "/ja/")
        return full

    pattern = re.compile(r"/en/glossary/(?P<slug>[^/]+)/")
    return pattern.sub(repl, body_ja)


def translate_markdown_file(
    translator: ClaudeTranslator,
    src_path: Path,
    dst_path: Path,
    existing_ja_slugs: set,
    *,
    body_override: Optional[str] = None,
) -> None:
    raw = src_path.read_text(encoding="utf-8")
    fm, body = parse_markdown_with_frontmatter(raw)

    title_en = fm.get("title", "")
    e_title = fm.get("e-title", title_en)
    desc_en = fm.get("description", "")
    keywords_en = fm.get("keywords", []) or []

    body_ja = body_override or translator.translate_body(body)

    title_ja, term_ja, keywords_ja, desc_ja = translator.translate_meta(title_en, desc_en, keywords_en)
    body_ja = rewrite_internal_links(body_ja, existing_ja_slugs)

    # Build JA frontmatter
    fm_ja = dict(fm)  # shallow copy
    fm_ja["title"] = title_ja
    fm_ja["e-title"] = e_title or title_en
    # 日本語側では term がない場合、少なくともタイトルを入れておく。
    # Claude が TERM_JA を返していればそれを優先し、なければタイトルをそのまま使用。
    if "term" not in fm_ja or not fm_ja.get("term"):
        fm_ja["term"] = term_ja or title_ja

    # 特定エントリの読みを固定: autonomous-agents -> じりつがたエージェント
    if fm_ja.get("translationKey") == "autonomous-agents":
        fm_ja["term"] = "じりつがたエージェント"
    if desc_ja:
        fm_ja["description"] = desc_ja
    if keywords_ja:
        fm_ja["keywords"] = keywords_ja

    # translationKey, type, date, category などはそのままコピー

    dst_path.parent.mkdir(parents=True, exist_ok=True)
    dst_text = dump_markdown_with_frontmatter(fm_ja, body_ja)
    dst_path.write_text(dst_text, encoding="utf-8")

    # 翻訳完了チェック
    is_complete, check_msg = check_translation_complete(body, body_ja)
    if is_complete:
        print(f"✓ Translated {src_path} -> {dst_path}")
    else:
        print(f"⚠ Translated {src_path} -> {dst_path} [INCOMPLETE: {check_msg}]")


def load_style_guide(path: Optional[str]) -> str:
    if not path:
        return DEFAULT_STYLE_GUIDE
    file_path = Path(path)
    if not file_path.exists():
        raise FileNotFoundError(f"Style guide file not found: {file_path}")
    return file_path.read_text(encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Translate English glossary Markdown files to Japanese using Claude API.")
    parser.add_argument("--source-dir", default="content/en/glossary", help="Source directory for English glossary .md files")
    parser.add_argument("--target-dir", default="content/ja/glossary", help="Target directory for Japanese glossary .md files")
    parser.add_argument("--one-file", help="Translate only this filename (e.g., autonomous-agents.md)")
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
    args = parser.parse_args()

    src_dir = Path(args.source_dir)
    dst_dir = Path(args.target_dir)

    client = build_claude_client()
    style_text = load_style_guide(args.style_guide)
    translator = ClaudeTranslator(client, model=args.model, style_guide=style_text)

    existing_ja_slugs = find_existing_ja_slugs(dst_dir)

    if args.one_file:
        src_path = src_dir / args.one_file
        if not src_path.exists():
            raise SystemExit(f"Source file not found: {src_path}")
        dst_path = dst_dir / src_path.name
        translate_markdown_file(translator, src_path, dst_path, existing_ja_slugs)
        return

    # 一括翻訳時は、複数ファイルを並列処理して速度アップ
    src_files = sorted(src_dir.glob("*.md"))
    if not src_files:
        print(f"No markdown files found in {src_dir}")
        return

    batch_size = max(1, args.batch_size)
    if batch_size == 1:
        # ネットワーク待ちが中心なので、3〜4スレッド程度の並列で十分
        max_workers = min(4, len(src_files))
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = {
                executor.submit(
                    translate_markdown_file,
                    translator,
                    src_path,
                    dst_dir / src_path.name,
                    existing_ja_slugs,
                ): src_path
                for src_path in src_files
            }

            for fut in as_completed(futures):
                src = futures[fut]
                try:
                    fut.result()
                except Exception as e:
                    print(f"Error translating {src}: {e}")
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
            continue

        for src_path in chunk_paths:
            body_override = translated_map.get(src_path.name)
            if not body_override:
                print(f"Missing batch result for {src_path}")
                continue
            translate_markdown_file(
                translator,
                src_path,
                dst_dir / src_path.name,
                existing_ja_slugs,
                body_override=body_override,
            )


if __name__ == "__main__":
    main()
