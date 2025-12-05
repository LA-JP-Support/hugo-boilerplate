#!/usr/bin/env python3
"""Remove inline "References:" blocks from Markdown files.

This script deletes reference lists that appear mid-article (e.g., under a section
without a heading), while preserving dedicated sections such as "## References" or
"## Further Reading".

Examples:
    python scripts/remove_inline_references.py content/en/glossary/
    python scripts/remove_inline_references.py content/en/glossary/HTTP-Request-Node.md
"""

from __future__ import annotations

import argparse
from pathlib import Path
import re
from typing import Iterable

EN_LABELS = [
    "Reference",
    "References",
    "Further Reading",
    "Further Reading and Resources",
    "References and URLs Used",
    "Source",
    "Sources",
    "See also",
    "See Also",
]

JA_LABELS = [
    "参考文献",
    "参考資料",
    "参考URL",
    "参考",
    "出典",
    "関連項目",
    "関連用語",
    "関連キーワード",
    "関連記事",
    "関連用語集",
    "関連情報",
    "関連リソース",
    "関連トピック",
    "関連YouTubeチュートリアル",
    "参考資料とツール",
    "リソース",
    "権威ある参考資料",
    "権威あるリソース",
    "追加リソース",
    "詳細リソース",
    "詳細な参考資料",
]


def _build_patterns() -> list[re.Pattern[str]]:
    """Build regex patterns for inline reference blocks.
    
    Matches patterns like:
    - **Reference:**  
      [Link](url)
    - References:
      - [Link](url)
    - **参考文献:**
      - [Link](url)
    - **Source:** [Link](url), [Link2](url2)  (same line)
    """
    patterns: list[re.Pattern[str]] = []
    for label in EN_LABELS + JA_LABELS:
        escaped = re.escape(label)
        # Pattern 1: **Label:** (colon inside bold) + bullet list on next lines
        patterns.append(
            re.compile(
                rf"(?m)^\s*\*\*{escaped}[:：]\*\*[ \t]*\n"
                rf"(?:\s*\n)?"
                rf"(?:\s*[-*]\s*\[[^\]]+\]\([^)]+\)\s*\n)+\n?"
            )
        )
        # Pattern 2: **Label:** (colon inside bold) + direct links on next lines (no bullet)
        patterns.append(
            re.compile(
                rf"(?m)^\s*\*\*{escaped}[:：]\*\*[ \t]*\n"
                rf"(?:\s*\n)?"
                rf"(?:\s*\[[^\]]+\]\([^)]+\)\s*\n)+\n?"
            )
        )
        # Pattern 3: **Label**: (colon outside bold) or Label: + bullet list on next lines
        patterns.append(
            re.compile(
                rf"(?m)^\s*(?:\*\*)?{escaped}(?:\*\*)?\s*[:：][ \t]*\n"
                rf"(?:\s*\n)?"
                rf"(?:\s*[-*]\s*\[[^\]]+\]\([^)]+\)\s*\n)+\n?"
            )
        )
        # Pattern 4: **Label**: (colon outside bold) or Label: + direct links on next lines
        patterns.append(
            re.compile(
                rf"(?m)^\s*(?:\*\*)?{escaped}(?:\*\*)?\s*[:：][ \t]*\n"
                rf"(?:\s*\n)?"
                rf"(?:\s*\[[^\]]+\]\([^)]+\)\s*\n)+\n?"
            )
        )
        # Pattern 5: **Label:** [Link](url) on SAME LINE (inline style)
        # Matches: **Source:** [link](url), [link2](url2)
        # Also handles trailing punctuation like period, and Japanese comma (、)
        patterns.append(
            re.compile(
                rf"(?m)^\s*\*\*{escaped}[:：]\*\*[ \t]+\[[^\]]+\]\([^)]+\)(?:[,、]?[ \t]*\[[^\]]+\]\([^)]+\))*[.,、]?[ \t]*\n"
            )
        )
        # Pattern 6: Label: [Link](url) on SAME LINE (no bold)
        patterns.append(
            re.compile(
                rf"(?m)^\s*{escaped}[:：][ \t]+\[[^\]]+\]\([^)]+\)(?:[,、]?[ \t]*\[[^\]]+\]\([^)]+\))*[.,、]?[ \t]*\n"
            )
        )
    return patterns


INLINE_REFERENCE_PATTERNS = _build_patterns()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "path",
        help="Markdown file or directory to process",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would change without writing files",
    )
    return parser.parse_args()


def iter_markdown_files(target: Path) -> Iterable[Path]:
    if target.is_file() and target.suffix.lower() == ".md":
        return [target]
    if target.is_dir():
        return sorted(p for p in target.rglob("*.md") if p.is_file())
    raise FileNotFoundError(f"Path not found: {target}")


def remove_inline_references(text: str) -> str:
    """Strip inline reference blocks, leaving formal sections intact."""
    updated = text
    for pattern in INLINE_REFERENCE_PATTERNS:
        updated = pattern.sub("", updated)
    return updated


def process_file(file_path: Path, dry_run: bool = False) -> bool:
    original = file_path.read_text(encoding="utf-8")
    updated = remove_inline_references(original)

    if updated == original:
        return False

    if dry_run:
        print(f"[DRY-RUN] Would update {file_path}")
        return True

    file_path.write_text(updated, encoding="utf-8")
    print(f"[OK] cleaned inline references: {file_path}")
    return True


def main() -> None:
    args = parse_args()
    target = Path(args.path)
    files = iter_markdown_files(target)

    changed = 0
    for md_file in files:
        if process_file(md_file, dry_run=args.dry_run):
            changed += 1

    print(f"Processed {len(files)} file(s); updated {changed}")


if __name__ == "__main__":
    main()
