#!/usr/bin/env python3
"""Remove self-referencing internal links from glossary articles.

A self-referencing link is when an article links to itself, e.g.,
in Bot-Avatar.md: [bot avatar](/en/glossary/bot-avatar/)

Usage:
    python scripts/remove_self_links.py content/en/glossary/
    python scripts/remove_self_links.py content/ja/glossary/
    python scripts/remove_self_links.py content/en/glossary/Bot-Avatar.md --dry-run
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", help="File or directory to process")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show changes without writing files",
    )
    return parser.parse_args()


def remove_self_links(text: str, slug: str) -> str:
    """Remove links that point to the same article."""
    # Pattern matches [text](/lang/glossary/slug/) or [text](/glossary/slug/)
    # and replaces with just the text
    pattern = re.compile(
        rf'\[([^\]]+)\]\(/(?:en|ja)/glossary/{re.escape(slug)}/?\)',
        re.IGNORECASE
    )
    
    result = pattern.sub(r'\1', text)
    return result


def process_file(file_path: Path, dry_run: bool = False) -> int:
    """Process a single file. Returns count of removed links."""
    slug = file_path.stem.lower()
    
    original = file_path.read_text(encoding="utf-8")
    updated = remove_self_links(original, slug)
    
    if updated == original:
        return 0
    
    # Count removed links
    pattern = re.compile(
        rf'\[([^\]]+)\]\(/(?:en|ja)/glossary/{re.escape(slug)}/?\)',
        re.IGNORECASE
    )
    removed_count = len(pattern.findall(original))
    
    if dry_run:
        print(f"[DRY-RUN] {file_path}: would remove {removed_count} self-links")
        return removed_count
    
    file_path.write_text(updated, encoding="utf-8")
    print(f"[OK] {file_path}: removed {removed_count} self-links")
    return removed_count


def main():
    args = parse_args()
    target = Path(args.path)
    
    if target.is_file():
        files = [target]
    else:
        files = sorted(target.rglob("*.md"))
    
    total_removed = 0
    files_changed = 0
    
    for f in files:
        if f.name == "_index.md":
            continue
        removed = process_file(f, args.dry_run)
        if removed > 0:
            total_removed += removed
            files_changed += 1
    
    print(f"\nTotal: {files_changed} files, {total_removed} self-links removed")


if __name__ == "__main__":
    main()
