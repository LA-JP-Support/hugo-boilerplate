#!/usr/bin/env python3
"""Strip "Definition:" / "定義:" prefixes from glossary headings."""

from __future__ import annotations

import re
from pathlib import Path

HEADING_DEF_PATTERN = re.compile(
    r"^(#{2,6}\s+)(?:Definition|Definitions|定義)\s*[：:]\s*(.+)$",
    re.MULTILINE,
)


def strip_definition_headings(text: str) -> str:
    def repl(match: re.Match[str]) -> str:
        heading_prefix = match.group(1)
        title = match.group(2).strip()
        return f"{heading_prefix}{title}"

    return HEADING_DEF_PATTERN.sub(repl, text)


def main() -> None:
    repo_root = Path(__file__).resolve().parent.parent
    targets = [
        repo_root / "content" / "en" / "glossary",
        repo_root / "content" / "ja" / "glossary",
    ]

    processed = 0

    for target_dir in targets:
        for md_file in sorted(target_dir.glob("*.md")):
            text = md_file.read_text(encoding="utf-8")
            new_text = strip_definition_headings(text)
            if new_text != text:
                md_file.write_text(new_text, encoding="utf-8")
                processed += 1
                print(f"Updated headings in: {md_file.relative_to(repo_root)}")

    if processed == 0:
        print("No files required heading updates.")
    else:
        print(f"\nTotal files updated: {processed}")


if __name__ == "__main__":
    main()
