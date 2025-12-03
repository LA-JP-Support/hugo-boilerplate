#!/usr/bin/env python3
"""Remove horizontal rules (---) from Markdown body while keeping front matter.

Usage examples:

    # Remove body --- from all Markdown files under a directory
    python3 scripts/remove_inner_hrs.py content/ja/glossary
    
    # Single file
    python3 scripts/remove_inner_hrs.py content/ja/glossary/Bot-Avatar.md

Rules:
- The very first front matter block delimited by --- at the top of the file is preserved.
- Any later line whose content is exactly '---' (ignoring surrounding whitespace) is removed.
"""

import sys
from pathlib import Path
from typing import Iterable


def remove_inner_hrs_from_text(lines: Iterable[str]) -> str:
    """Return text with body-only '---' lines removed.

    - Preserves the first front matter block starting at line 0.
    - After front matter is closed, removes any line whose stripped content is exactly '---'.
    """

    out: list[str] = []
    in_front_matter = False
    front_done = False

    for idx, raw in enumerate(lines):
        line = raw.rstrip("\n")
        stripped = line.strip()

        # Detect start of front matter only at very top of file
        if idx == 0 and stripped == "---":
            in_front_matter = True
            out.append(line)
            continue

        # Detect end of front matter
        if in_front_matter and stripped == "---":
            in_front_matter = False
            front_done = True
            out.append(line)
            continue

        # After front matter, drop any standalone '---' line
        if front_done and not in_front_matter and stripped == "---":
            continue

        out.append(line)

    return "\n".join(out) + "\n"


def process_path(path: Path) -> None:
    """Process a single file or all .md files under a directory."""
    if path.is_dir():
        for md in path.rglob("*.md"):
            process_file(md)
    elif path.is_file():
        process_file(path)
    else:
        print(f"[WARN] Path not found: {path}")


def process_file(file_path: Path) -> None:
    if file_path.suffix.lower() != ".md":
        return

    text = file_path.read_text(encoding="utf-8")
    new_text = remove_inner_hrs_from_text(text.splitlines())

    if new_text != text:
        file_path.write_text(new_text, encoding="utf-8")
        print(f"[OK] cleaned: {file_path}")
    else:
        print(f"[SKIP] no changes: {file_path}")


def main(argv: list[str]) -> None:
    if len(argv) < 2:
        print("Usage: python3 scripts/remove_inner_hrs.py <file-or-directory>")
        raise SystemExit(1)

    target = Path(argv[1])
    process_path(target)


if __name__ == "__main__":  # pragma: no cover
    main(sys.argv)
