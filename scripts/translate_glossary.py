#!/usr/bin/env python3
"""Create Japanese draft files from English glossary Markdown.

This is a lightweight helper that duplicates the English structure, applies
simple glossary-based term replacements (en→ja), and leaves TODO markers where
manual translation is still required.

Usage examples:

    python3 scripts/translate_glossary.py content-drafts/en/clean/ --output content-drafts/ja/clean/
    python3 scripts/translate_glossary.py content/en/glossary/bot-avatar.md --output content/ja/glossary/

The script intentionally does NOT call any external translation API. It simply
copies the file, swaps known terms using config/translation_glossary.csv, and
adds a header comment reminding editors to finish the translation.
"""

from __future__ import annotations

import argparse
import csv
import re
from pathlib import Path
from typing import Dict, Iterable, List, Tuple

FRONT_MATTER_PATTERN = re.compile(r"^---\s*\n(.*?)\n---\s*\n?", re.DOTALL)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", help="English Markdown file or directory")
    parser.add_argument(
        "--output",
        required=True,
        help="Output directory for Japanese drafts",
    )
    parser.add_argument(
        "--glossary",
        default="config/translation_glossary.csv",
        help="CSV mapping of en,ja terms (default: %(default)s)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would happen without writing",
    )
    return parser.parse_args()


def load_glossary(csv_path: Path) -> List[Tuple[str, str]]:
    glossary: List[Tuple[str, str]] = []
    with csv_path.open("r", encoding="utf-8") as fp:
        reader = csv.DictReader(fp)
        for row in reader:
            en = row.get("en", "").strip()
            ja = row.get("ja", "").strip()
            if en and ja:
                glossary.append((en, ja))
    # longer phrases first to avoid partial replacements breaking them
    glossary.sort(key=lambda pair: len(pair[0]), reverse=True)
    return glossary


def iter_markdown_files(path: Path) -> Iterable[Path]:
    if path.is_file() and path.suffix.lower() == ".md":
        yield path
    elif path.is_dir():
        for file in sorted(path.rglob("*.md")):
            if file.is_file():
                yield file
    else:
        raise FileNotFoundError(f"Input path not found: {path}")


def split_front_matter(text: str) -> Tuple[str, str]:
    match = FRONT_MATTER_PATTERN.match(text)
    if not match:
        raise ValueError("Markdown does not start with YAML front matter")
    front = match.group(1)
    body = text[match.end() :]
    return front, body


def apply_glossary(text: str, glossary: List[Tuple[str, str]]) -> str:
    result = text
    for en, ja in glossary:
        escaped = re.escape(en)
        pattern = re.compile(rf"(?<!\w){escaped}(?!\w)")
        result = pattern.sub(ja, result)
    return result


def create_translation_stub(front: str, body: str, glossary: List[Tuple[str, str]]) -> str:
    translated_front = apply_glossary(front, glossary)
    translated_body = apply_glossary(body, glossary)

    reminder = (
        "\n<!-- TODO: 翻訳を完了してください。英語原文を参考に、各セクションを自然な日本語に整えましょう。 -->\n\n"
    )
    return f"---\n{translated_front.strip()}\n---\n{reminder}{translated_body.lstrip()}"


def process_file(src: Path, dest: Path, glossary: List[Tuple[str, str]], dry_run: bool) -> None:
    original = src.read_text(encoding="utf-8")
    front, body = split_front_matter(original)
    stub = create_translation_stub(front, body, glossary)

    if dry_run:
        print(f"[DRY-RUN] Would create {dest}")
        return

    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(stub, encoding="utf-8")
    print(f"[OK] created draft: {dest}")


def main() -> None:
    args = parse_args()
    input_path = Path(args.input)
    output_dir = Path(args.output)
    glossary = load_glossary(Path(args.glossary))

    base = input_path if input_path.is_dir() else input_path.parent
    for file_path in iter_markdown_files(input_path):
        relative = file_path.relative_to(base)
        destination = output_dir / relative
        process_file(file_path, destination, glossary, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
