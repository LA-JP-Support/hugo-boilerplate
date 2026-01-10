#!/usr/bin/env python3

import argparse
import json
import os
import re
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Dict, List, Tuple


@dataclass
class FileReport:
    path: str
    changed: bool
    would_change: bool
    tags_replaced: int
    merges: int
    whitespace_fixes: int
    empty_bold_removed: int
    header_list_fixes: int
    unmatched_markers_before: bool
    unmatched_markers_after: bool
    skipped_due_to_unmatched_after: bool
    remaining_html_tags: int


CODE_FENCE_RE = re.compile(r"```[\s\S]*?```", re.MULTILINE)
INLINE_CODE_RE = re.compile(r"`[^`]*`")

STRONG_OPEN_RE = re.compile(r"<strong\b[^>]*>", re.IGNORECASE)
STRONG_CLOSE_RE = re.compile(r"</strong\s*>", re.IGNORECASE)
B_OPEN_RE = re.compile(r"<b\b[^>]*>", re.IGNORECASE)
B_CLOSE_RE = re.compile(r"</b\s*>", re.IGNORECASE)

HTML_TAG_RE = re.compile(r"<strong\b|</strong\b|<b\b|</b\b", re.IGNORECASE)

# Header: ###**Title** -> ### **Title**
HEADER_ADJ_RE = re.compile(r"^(#{1,6})\*\*", re.MULTILINE)

# List: -**Item** -> - **Item** (also +, *)
LIST_ADJ_RE = re.compile(r"^(\s*[-+*])\*\*", re.MULTILINE)

# Ordered list: 1.**Item** -> 1. **Item**
OLIST_ADJ_RE = re.compile(r"^(\s*\d+\.)\*\*", re.MULTILINE)

# Merge adjacent bold markers:
# **A****B** or **A** **B** becomes **AB** / **A B** by removing the middle ** **
ADJACENT_BOLD_RE = re.compile(r"\*\*([ \t]*)\*\*")

# Fix whitespace inside bold:
LEADING_WS_IN_BOLD_RE = re.compile(r"\*\*\s+((?:(?!\*\*).)+?)\*\*")
TRAILING_WS_IN_BOLD_RE = re.compile(r"\*\*((?:(?!\*\*).)+?)\s+\*\*")

# Empty bold created by <strong></strong> -> ****
EMPTY_BOLD_RE = re.compile(r"\*\*\*\*")

# Horizontal rule line like ****, ***, -----
HR_LINE_RE = re.compile(r"^\s*(\*{3,}|-{3,}|_{3,})\s*$", re.MULTILINE)


def mask_segments(text: str, pattern: re.Pattern, prefix: str) -> Tuple[str, Dict[str, str]]:
    mapping: Dict[str, str] = {}

    def _repl(m: re.Match) -> str:
        key = f"@@{prefix}{len(mapping)}@@"
        mapping[key] = m.group(0)
        return key

    return pattern.sub(_repl, text), mapping


def unmask_segments(text: str, mapping: Dict[str, str]) -> str:
    if not mapping:
        return text
    # Replace longer keys first just in case (not strictly needed here)
    for k in sorted(mapping.keys(), key=len, reverse=True):
        text = text.replace(k, mapping[k])
    return text


def count_bold_markers_ignoring_code(text: str) -> int:
    tmp = CODE_FENCE_RE.sub("", text)
    tmp = INLINE_CODE_RE.sub("", tmp)
    return len(re.findall(r"\*\*", tmp))


def convert_content(text: str) -> Tuple[str, int, int, int, int, int]:
    """Return (new_text, tags_replaced, merges, whitespace_fixes, empty_bold_removed, header_list_fixes)."""

    # Mask code and inline code first
    masked, code_map = mask_segments(text, CODE_FENCE_RE, "CODEFENCE")
    masked, inline_map = mask_segments(masked, INLINE_CODE_RE, "INLINE")

    # Mask horizontal rule lines to avoid turning '****' into ''
    masked, hr_map = mask_segments(masked, HR_LINE_RE, "HR")

    tags_replaced = 0
    merges = 0
    whitespace_fixes = 0
    empty_bold_removed = 0
    header_list_fixes = 0

    # Replace HTML strong/b tags
    masked, n = STRONG_OPEN_RE.subn("**", masked)
    tags_replaced += n
    masked, n = STRONG_CLOSE_RE.subn("**", masked)
    tags_replaced += n
    masked, n = B_OPEN_RE.subn("**", masked)
    tags_replaced += n
    masked, n = B_CLOSE_RE.subn("**", masked)
    tags_replaced += n

    # Fix headers/lists adjacency
    masked, n = HEADER_ADJ_RE.subn(r"\1 **", masked)
    header_list_fixes += n
    masked, n = LIST_ADJ_RE.subn(r"\1 **", masked)
    header_list_fixes += n
    masked, n = OLIST_ADJ_RE.subn(r"\1 **", masked)
    header_list_fixes += n

    # Merge adjacent bold markers (loop for chains)
    while True:
        masked, n = ADJACENT_BOLD_RE.subn(r"\1", masked)
        if n == 0:
            break
        merges += n

    # Remove empty bold occurrences that are not HR lines (HR lines are masked)
    masked, n = EMPTY_BOLD_RE.subn("", masked)
    empty_bold_removed += n

    # Fix whitespace inside bold
    masked, n = LEADING_WS_IN_BOLD_RE.subn(r"**\1**", masked)
    whitespace_fixes += n
    masked, n = TRAILING_WS_IN_BOLD_RE.subn(r"**\1**", masked)
    whitespace_fixes += n

    # Restore masked segments
    masked = unmask_segments(masked, hr_map)
    masked = unmask_segments(masked, inline_map)
    masked = unmask_segments(masked, code_map)

    return masked, tags_replaced, merges, whitespace_fixes, empty_bold_removed, header_list_fixes


def iter_md_files(root: Path) -> List[Path]:
    out: List[Path] = []
    for dirpath, _, filenames in os.walk(root):
        for fn in filenames:
            if fn.endswith(".md"):
                out.append(Path(dirpath) / fn)
    return out


def main() -> None:
    parser = argparse.ArgumentParser(description="Convert <strong>/<b> tags to Markdown ** in glossary content safely.")
    parser.add_argument(
        "--targets",
        nargs="*",
        default=[
            "content/en/glossary",
            "content/ja/glossary",
        ],
        help="Target directories to scan (default: content/en/glossary content/ja/glossary)",
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Actually write changes to files. Without this flag, runs in dry-run mode.",
    )
    parser.add_argument(
        "--report",
        default="strong_to_md_report.json",
        help="Report output path (json).",
    )
    parser.add_argument(
        "--max-print",
        type=int,
        default=30,
        help="Max file paths to print per category.",
    )

    args = parser.parse_args()

    repo_root = Path.cwd()
    targets = [repo_root / t for t in args.targets]

    md_files: List[Path] = []
    for t in targets:
        if not t.exists():
            raise SystemExit(f"Target directory not found: {t}")
        md_files.extend(iter_md_files(t))

    reports: List[FileReport] = []

    would_change_files: List[str] = []
    skipped_unmatched_files: List[str] = []

    total_tags = 0
    total_merges = 0
    total_ws = 0
    total_empty = 0
    total_hdr_list = 0

    for p in md_files:
        original = p.read_text(encoding="utf-8")

        unmatched_before = (count_bold_markers_ignoring_code(original) % 2) == 1

        new_text, tags_replaced, merges, ws_fixes, empty_removed, hdr_list_fixes = convert_content(original)

        unmatched_after = (count_bold_markers_ignoring_code(new_text) % 2) == 1

        remaining_html = len(HTML_TAG_RE.findall(new_text))

        changed = new_text != original
        would_change = changed

        skipped_due_to_unmatched_after = False

        # Safety: if conversion introduces unmatched **, don't apply changes.
        if (not unmatched_before) and unmatched_after and changed:
            skipped_due_to_unmatched_after = True

        if args.apply and changed and not skipped_due_to_unmatched_after:
            p.write_text(new_text, encoding="utf-8")

        if would_change and (tags_replaced > 0 or remaining_html > 0):
            would_change_files.append(str(p))

        if skipped_due_to_unmatched_after:
            skipped_unmatched_files.append(str(p))

        total_tags += tags_replaced
        total_merges += merges
        total_ws += ws_fixes
        total_empty += empty_removed
        total_hdr_list += hdr_list_fixes

        reports.append(
            FileReport(
                path=str(p),
                changed=bool(args.apply and changed and not skipped_due_to_unmatched_after),
                would_change=would_change,
                tags_replaced=tags_replaced,
                merges=merges,
                whitespace_fixes=ws_fixes,
                empty_bold_removed=empty_removed,
                header_list_fixes=hdr_list_fixes,
                unmatched_markers_before=unmatched_before,
                unmatched_markers_after=unmatched_after,
                skipped_due_to_unmatched_after=skipped_due_to_unmatched_after,
                remaining_html_tags=remaining_html,
            )
        )

    summary = {
        "apply": bool(args.apply),
        "targets": [str(t) for t in targets],
        "files_scanned": len(md_files),
        "total_tags_replaced": total_tags,
        "total_adjacent_merges": total_merges,
        "total_whitespace_fixes": total_ws,
        "total_empty_bold_removed": total_empty,
        "total_header_list_fixes": total_hdr_list,
        "files_would_change": len([r for r in reports if r.would_change]),
        "files_skipped_due_to_unmatched_after": len(skipped_unmatched_files),
        "files_with_remaining_html_tags": len([r for r in reports if r.remaining_html_tags > 0]),
    }

    out = {
        "summary": summary,
        "skipped_due_to_unmatched_after": skipped_unmatched_files,
        "reports": [asdict(r) for r in reports],
    }

    Path(args.report).write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")

    print("=== strong/b -> markdown ** conversion ===")
    print(json.dumps(summary, ensure_ascii=False, indent=2))

    if skipped_unmatched_files:
        print("\n[SKIPPED] Would become unmatched after conversion (showing first items):")
        for f in skipped_unmatched_files[: args.max_print]:
            print(f"- {f}")

    # Show a small sample of files that would be touched (for sanity)
    sample = [r.path for r in reports if r.would_change][: args.max_print]
    if sample:
        print("\n[Sample] Files that would change (first items):")
        for f in sample:
            print(f"- {f}")

    print(f"\nReport written to: {args.report}")


if __name__ == "__main__":
    main()
