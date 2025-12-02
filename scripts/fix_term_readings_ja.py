#!/usr/bin/env python3
"""Post-process Japanese glossary files to convert kanji-leading `term` values into kana.

- Targets: content/ja/glossary/*.md
- For each file:
  - Parse YAML frontmatter + body
  - If `term` exists and its first character is likely kanji, and translationKey exists
    - Ask Claude for a kana reading of the Japanese title suitable for sorting
    - Overwrite `term` with that reading

This script ONLY touches the `term` field; all other content is preserved.

Requirements:
- anthropic (pip install anthropic)
- pyyaml
- ANTHROPIC_API_KEY set in environment

Usage:

  python scripts/fix_term_readings_ja.py \
      --ja-dir content/ja/glossary
"""

import argparse
import os
import re
from pathlib import Path
from typing import Dict, Tuple

import yaml

try:
    import anthropic
except ImportError:
    anthropic = None

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n(.*)$", re.DOTALL)


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


def is_kanji(ch: str) -> bool:
    """Rudimentary kanji check based on Unicode ranges."""
    code = ord(ch)
    # CJK Unified Ideographs ranges
    return (
        0x4E00 <= code <= 0x9FFF
        or 0x3400 <= code <= 0x4DBF
        or 0xF900 <= code <= 0xFAFF
    )


def build_claude_client() -> "anthropic.Anthropic":
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        raise RuntimeError("ANTHROPIC_API_KEY is not set in environment")
    if anthropic is None:
        raise RuntimeError("anthropic package is not installed. Run: pip install anthropic")
    return anthropic.Anthropic(api_key=api_key)


def ask_reading(client, title_ja: str, term_current: str) -> str:
    """Ask Claude for a kana reading of the title.

    We supply both title and current term so the model can infer intent.
    """
    system = (
        "You generate Japanese readings (furigana) for glossary terms. "
        "Return a short reading suitable for alphabetical (gojuon) sorting. "
        "Start with hiragana or katakana (no leading kanji)."
    )
    prompt = f"""TITLE_JA:
{title_ja}

CURRENT_TERM:
{term_current}

Please respond with ONLY the reading in Japanese kana (hiragana and/or katakana),
without any quotes or extra text.
"""
    resp = client.messages.create(
        model="claude-3-7-sonnet-latest",
        max_tokens=128,
        temperature=0.1,
        system=system,
        messages=[{"role": "user", "content": prompt}],
    )
    text_parts = []
    for block in resp.content:
        if getattr(block, "type", None) == "text":
            text_parts.append(block.text)
    reading = "".join(text_parts).strip()
    # very small safety: strip surrounding quotes if present
    if (reading.startswith("\"") and reading.endswith("\"")) or (
        reading.startswith("'") and reading.endswith("'")
    ):
        reading = reading[1:-1].strip()
    return reading


def process_file(client, path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    fm, body = parse_markdown_with_frontmatter(text)

    term = str(fm.get("term") or "").strip()
    title = str(fm.get("title") or "").strip()

    if not term:
        # nothing to do
        return False
    first = term[0]
    if not is_kanji(first):
        return False

    # ask Claude for a kana reading
    new_reading = ask_reading(client, title or term, term)
    if not new_reading:
        print(f"[WARN] Empty reading for {path}, term stays as-is")
        return False

    fm["term"] = new_reading
    new_text = dump_markdown_with_frontmatter(fm, body)
    path.write_text(new_text, encoding="utf-8")
    print(f"Updated term in {path}: '{term}' -> '{new_reading}'")
    return True


def main() -> None:
    parser = argparse.ArgumentParser(description="Fix Japanese glossary term readings by converting kanji-leading term to kana using Claude.")
    parser.add_argument("--ja-dir", default="content/ja/glossary", help="Directory containing Japanese glossary .md files")
    args = parser.parse_args()

    ja_dir = Path(args.ja_dir)
    if not ja_dir.exists():
        raise SystemExit(f"Directory not found: {ja_dir}")

    client = build_claude_client()

    count = 0
    for path in sorted(ja_dir.glob("*.md")):
        if process_file(client, path):
            count += 1
    print(f"Done. Updated {count} files.")


if __name__ == "__main__":
    main()
