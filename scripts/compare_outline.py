#!/usr/bin/env python3
"""Compare headings between English and Japanese glossary files.

Usage examples:

    python3 scripts/compare_outline.py content/en/glossary content/ja/glossary
    python3 scripts/compare_outline.py content/en/glossary/bot-avatar.md content/ja/glossary/bot-avatar.md

The script scans Markdown files, collects all headings (##, ###, ...), and
reports headings present in the first input but missing in the second. This
helps catch translation gaps or misplaced sections.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path
from typing import Iterable, List, Tuple

HEADING_PATTERN = re.compile(r"^(#{2,6})\s+(.*)$", re.MULTILINE)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", help="English file or directory")
    parser.add_argument("target", help="Japanese file or directory")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Fail with exit code 1 if differences are found",
    )
    return parser.parse_args()


def iter_markdown_files(path: Path) -> List[Path]:
    if path.is_file() and path.suffix.lower() == ".md":
        return [path]
    if path.is_dir():
        return sorted(p for p in path.rglob("*.md") if p.is_file())
    raise FileNotFoundError(f"Path not found: {path}")


def relative_key(base: Path, file_path: Path) -> Path:
    return file_path.relative_to(base)


def collect_headings(text: str) -> List[Tuple[str, str]]:
    results: List[Tuple[str, str]] = []
    for match in HEADING_PATTERN.finditer(text):
        level = match.group(1)
        title = match.group(2).strip()
        normalized = re.sub(r"\s+", " ", title).lower()
        results.append((level, normalized))
    return results


def compare_files(src: Path, dest: Path) -> List[str]:
    src_text = src.read_text(encoding="utf-8")
    dest_text = dest.read_text(encoding="utf-8")

    src_headings = collect_headings(src_text)
    dest_headings = collect_headings(dest_text)

    dest_set = {title for _, title in dest_headings}
    missing = [original for (_, original) in src_headings if original not in dest_set]

    if missing:
        return [f"  - Missing in {dest}: {src_heading}" for src_heading in missing]
    return []


def main() -> None:
    args = parse_args()
    src_path = Path(args.source)
    dest_path = Path(args.target)

    src_files = iter_markdown_files(src_path)
    base_src = src_path if src_path.is_dir() else src_path.parent
    base_dest = dest_path if dest_path.is_dir() else dest_path.parent

    differences: List[str] = []

    for src_file in src_files:
        rel = relative_key(base_src, src_file)
        target_file = dest_path / rel if dest_path.is_dir() else dest_path
        if not target_file.exists():
            differences.append(f"[WARN] Target file missing: {target_file}")
            continue
        diff = compare_files(src_file, target_file)
        if diff:
            differences.append(f"[FILE] {rel}")
            differences.extend(diff)

    if differences:
        print("\n".join(differences))
        if args.strict:
            raise SystemExit(1)
    else:
        print("No heading differences detected.")


if __name__ == "__main__":
    main()
