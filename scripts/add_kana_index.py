#!/usr/bin/env python3
"""Add reading/kana_head metadata to Japanese glossary Markdown files.

Usage examples:

    python3 scripts/add_kana_index.py content/ja/glossary
    python3 scripts/add_kana_index.py content/ja/glossary/bot-avatar.md --dry-run

The script expects front matter with `title`. If `reading` (ひらがな) or
`kana_head` is missing, it prompts via romanized → kana conversion fallback
(naive) or simply copies the title as a placeholder. Editors can refine later.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

FRONT_MATTER_PATTERN = re.compile(r"^---\s*\n(.*?)\n---\s*\n?", re.DOTALL)

KANA_HEAD_MAP = [
    ("あ", "あいうえおぁぃぅぇぉアイウエオァィゥェォ"),
    ("か", "かきくけこがぎぐげござじずぜぞカキクケコガギグゲゴサシスセソ"),
    ("さ", "さしすせそサシスセソざじずぜぞザジズゼゾ"),
    ("た", "たちつてとだぢづでどタチツテトダヂヅデド"),
    ("な", "なにぬねのナニヌネノ"),
    ("は", "はひふへほばびぶべぼぱぴぷぺぽハヒフヘホバビブベボパピプペポ"),
    ("ま", "まみむめもマミムメモ"),
    ("や", "やゆよゃゅょヤユヨャュョ"),
    ("ら", "らりるれろラリルレロ"),
    ("わ", "わをんゎヲン"),
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", help="Japanese Markdown file or directory")
    parser.add_argument("--dry-run", action="store_true", help="No changes written")
    return parser.parse_args()


def iter_files(path: Path):
    if path.is_file() and path.suffix.lower() == ".md":
        yield path
    elif path.is_dir():
        for file in sorted(path.rglob("*.md")):
            yield file
    else:
        raise FileNotFoundError(f"Path not found: {path}")


def split_front_matter(text: str):
    match = FRONT_MATTER_PATTERN.match(text)
    if not match:
        raise ValueError("Missing YAML front matter")
    front = match.group(1)
    body = text[match.end() :]
    return front, body


def upsert_field(front: str, field: str, value: str) -> str:
    pattern = re.compile(rf"^{field}:.*$", re.MULTILINE)
    line = f"{field}: {value}"
    if pattern.search(front):
        return pattern.sub(line, front, count=1)
    return f"{front}\n{line}"


def infer_reading(title: str) -> str:
    # Extremely naive: assume title already in Japanese
    return title


def head_from_reading(reading: str) -> str:
    first = reading.strip()[0] if reading else ""
    for head, chars in KANA_HEAD_MAP:
        if first in chars:
            return head
    return "その他"


def process_file(path: Path, dry_run: bool) -> None:
    text = path.read_text(encoding="utf-8")
    front, body = split_front_matter(text)

    title_match = re.search(r"^title:\s*(.*)$", front, re.MULTILINE)
    title = title_match.group(1).strip().strip('"') if title_match else ""

    reading_match = re.search(r"^reading:\s*(.*)$", front, re.MULTILINE)
    reading = reading_match.group(1).strip() if reading_match else ""

    if not reading:
        reading = infer_reading(title)
        front = upsert_field(front, "reading", reading)

    kana_head_match = re.search(r"^kana_head:\s*(.*)$", front, re.MULTILINE)
    if not kana_head_match:
        head = head_from_reading(reading)
        front = upsert_field(front, "kana_head", head)

    output = f"---\n{front.strip()}\n---\n{body.lstrip()}"

    if dry_run:
        print(f"[DRY-RUN] Would update {path}")
        return

    path.write_text(output, encoding="utf-8")
    print(f"[OK] updated kana metadata: {path}")


def main() -> None:
    args = parse_args()
    for file_path in iter_files(Path(args.input)):
        process_file(file_path, args.dry_run)


if __name__ == "__main__":
    main()
