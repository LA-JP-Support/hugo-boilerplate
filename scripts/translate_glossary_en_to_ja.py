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
from pathlib import Path
from typing import Dict, Tuple, Optional
from concurrent.futures import ThreadPoolExecutor, as_completed

import yaml

try:
    import anthropic
except ImportError:
    anthropic = None


FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n(.*)$", re.DOTALL)


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
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        raise RuntimeError("ANTHROPIC_API_KEY is not set in environment")
    if anthropic is None:
        raise RuntimeError("anthropic package is not installed. Run: pip install anthropic")
    return anthropic.Anthropic(api_key=api_key)


def translate_text(client, text: str, system_prompt: str) -> str:
    """Call Claude with a simple text-in / text-out interface."""
    resp = client.messages.create(
        model="claude-3-7-sonnet-latest",
        max_tokens=4000,
        temperature=0.2,
        system=system_prompt,
        messages=[{"role": "user", "content": text}],
    )
    chunks = []
    for block in resp.content:
        if getattr(block, "type", None) == "text":
            chunks.append(block.text)
    return "".join(chunks).strip()


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


def translate_markdown_file(client, src_path: Path, dst_path: Path, existing_ja_slugs: set) -> None:
    raw = src_path.read_text(encoding="utf-8")
    fm, body = parse_markdown_with_frontmatter(raw)

    title_en = fm.get("title", "")
    desc_en = fm.get("description", "")
    keywords_en = fm.get("keywords", []) or []

    # 1) 本文の Markdown だけを翻訳（JSON ではなくプレーンテキストとして受け取る）
    body_prompt = """You are translating a technical glossary entry body from English to natural, professional Japanese.

- Input is Markdown.
- Preserve Markdown structure (headings, lists, code blocks, links, emphasis) exactly.
- Translate all prose into Japanese.
- Do NOT translate code inside fenced code blocks or inline code (backticks). Keep code as-is.
- Translate link anchor text, but keep URLs unchanged.

Return ONLY the translated Markdown body, with no extra commentary.
"""

    body_ja = translate_text(client, body, system_prompt=body_prompt)

    # 2) title / description / keywords を小さな別リクエストで翻訳
    #    ここでタイトルの読み（かな）= TERM_JA も生成してもらう
    meta_prompt = """TITLE:
{title}

DESCRIPTION:
{description}

KEYWORDS (comma separated):
{keywords}

Please translate these into Japanese and respond ONLY in the following format:

TITLE_JA: <Japanese title>
TERM_JA: <reading of the title in Japanese kana. Start with hiragana/katakana, avoid kanji if possible>
DESCRIPTION_JA: <Japanese description>
KEYWORDS_JA: <keyword1>, <keyword2>, ...
""".format(
        title=title_en,
        description=desc_en,
        keywords=", ".join(map(str, keywords_en)),
    )

    meta_system = "You are translating glossary metadata (title, description, keywords) from English to Japanese. Follow the requested output format exactly."
    meta_text = translate_text(client, meta_prompt, system_prompt=meta_system)

    # パース: シンプルな prefix ベースで抽出
    title_ja = title_en
    desc_ja = desc_en
    term_ja: str | None = None
    keywords_ja: list[str] = []

    for line in meta_text.splitlines():
        line = line.strip()
        if line.startswith("TITLE_JA:"):
            title_ja = line[len("TITLE_JA:"):].strip()
        elif line.startswith("TERM_JA:"):
            term_ja = line[len("TERM_JA:"):].strip()
        elif line.startswith("DESCRIPTION_JA:"):
            desc_ja = line[len("DESCRIPTION_JA:"):].strip()
        elif line.startswith("KEYWORDS_JA:"):
            raw = line[len("KEYWORDS_JA:"):].strip()
            if raw:
                keywords_ja = [k.strip() for k in raw.split(",") if k.strip()]
    body_ja = rewrite_internal_links(body_ja, existing_ja_slugs)

    # Build JA frontmatter
    fm_ja = dict(fm)  # shallow copy
    fm_ja["title"] = title_ja
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
    print(f"Translated {src_path} -> {dst_path}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Translate English glossary Markdown files to Japanese using Claude API.")
    parser.add_argument("--source-dir", default="content/en/glossary", help="Source directory for English glossary .md files")
    parser.add_argument("--target-dir", default="content/ja/glossary", help="Target directory for Japanese glossary .md files")
    parser.add_argument("--one-file", help="Translate only this filename (e.g., autonomous-agents.md)")
    args = parser.parse_args()

    src_dir = Path(args.source_dir)
    dst_dir = Path(args.target_dir)

    client = build_claude_client()

    existing_ja_slugs = find_existing_ja_slugs(dst_dir)

    if args.one_file:
        src_path = src_dir / args.one_file
        if not src_path.exists():
            raise SystemExit(f"Source file not found: {src_path}")
        dst_path = dst_dir / src_path.name
        translate_markdown_file(client, src_path, dst_path, existing_ja_slugs)
        return

    # 一括翻訳時は、複数ファイルを並列処理して速度アップ
    src_files = sorted(src_dir.glob("*.md"))
    if not src_files:
        print(f"No markdown files found in {src_dir}")
        return

    # ネットワーク待ちが中心なので、3〜4スレッド程度の並列で十分
    max_workers = min(4, len(src_files))
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {
            executor.submit(translate_markdown_file, client, src_path, dst_dir / src_path.name, existing_ja_slugs): src_path
            for src_path in src_files
        }

        for fut in as_completed(futures):
            src = futures[fut]
            try:
                fut.result()
            except Exception as e:
                print(f"Error translating {src}: {e}")


if __name__ == "__main__":
    main()
