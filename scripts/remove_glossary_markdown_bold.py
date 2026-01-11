#!/usr/bin/env python3

import argparse
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Tuple


@dataclass
class FileChange:
    path: Path
    bold_removed: int


_FRONTMATTER_DELIM = "---"
_CODE_FENCE_RE = re.compile(r"^\s*```")
_HEADING_RE = re.compile(r"^\s*#{1,6}\s+")

# Remove markdown bold markers, keeping the inner text.
# We intentionally only operate within a single line.
_BOLD_RE = re.compile(r"\*\*(.+?)\*\*")
_ASTERISK_RULE_RE = re.compile(r"^\s*\*{3,}\s*$")


def _split_frontmatter(text: str) -> Tuple[str, str]:
    """Return (frontmatter, body). frontmatter includes the delimiters if present."""
    if not text.startswith(_FRONTMATTER_DELIM + "\n"):
        return "", text

    lines = text.splitlines(keepends=True)
    if len(lines) < 2:
        return "", text

    # Find the second '---' line.
    fm_end_idx = None
    for i in range(1, len(lines)):
        if lines[i].strip() == _FRONTMATTER_DELIM:
            fm_end_idx = i
            break

    if fm_end_idx is None:
        return "", text

    frontmatter = "".join(lines[: fm_end_idx + 1])
    body = "".join(lines[fm_end_idx + 1 :])
    return frontmatter, body


def _process_body(body: str) -> Tuple[str, int]:
    out_lines = []
    removed = 0
    in_code_fence = False

    for line in body.splitlines(keepends=True):
        if _CODE_FENCE_RE.match(line):
            in_code_fence = not in_code_fence
            out_lines.append(line)
            continue

        if in_code_fence or _HEADING_RE.match(line):
            out_lines.append(line)
            continue

        def _sub(m: re.Match) -> str:
            nonlocal removed
            removed += 1
            return m.group(1)

        new_line = _BOLD_RE.sub(_sub, line)
        if not _ASTERISK_RULE_RE.match(new_line):
            if "**" in new_line:
                removed += new_line.count("**")
                new_line = new_line.replace("**", "")
        out_lines.append(new_line)

    return "".join(out_lines), removed


def iter_section_files(content_dir: Path, languages: Iterable[str], sections: Iterable[str]) -> Iterable[Path]:
    for lang in languages:
        for section in sections:
            base = content_dir / lang / section
            if not base.exists():
                continue
            yield from sorted(base.rglob("*.md"))


def process_file(path: Path) -> Tuple[str, int]:
    text = path.read_text(encoding="utf-8")
    frontmatter, body = _split_frontmatter(text)
    new_body, removed = _process_body(body)
    return frontmatter + new_body, removed


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Remove Markdown bold markers (**...**) from glossary body text. "
            "Frontmatter, headings, and fenced code blocks are preserved."
        )
    )
    parser.add_argument(
        "--content-dir",
        default="content",
        help="Content directory (default: content)",
    )
    parser.add_argument(
        "--languages",
        nargs="+",
        default=["en", "ja"],
        help="Languages to process (default: en ja)",
    )
    parser.add_argument(
        "--sections",
        nargs="+",
        default=["glossary"],
        help="Sections to process (default: glossary). Example: --sections glossary blog",
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Write changes to files (default: dry-run)",
    )
    parser.add_argument(
        "--include-headings",
        action="store_true",
        help="Also remove bold markers within Markdown heading lines (# ...) (default: false)",
    )
    parser.add_argument(
        "--summary-only",
        action="store_true",
        help="Only print totals (do not print per-file list)",
    )
    parser.add_argument(
        "--max-report",
        type=int,
        default=50,
        help="Max number of per-file entries to print (default: 50)",
    )

    args = parser.parse_args()

    content_dir = Path(args.content_dir)
    changes = []
    total_removed = 0
    scanned = 0

    for md in iter_section_files(content_dir, args.languages, args.sections):
        scanned += 1
        text = md.read_text(encoding="utf-8")
        frontmatter, body = _split_frontmatter(text)

        if args.include_headings:
            new_body, removed = _process_body(body)
        else:
            # Legacy behavior: preserve headings exactly.
            out_lines = []
            removed = 0
            in_code_fence = False
            for line in body.splitlines(keepends=True):
                if _CODE_FENCE_RE.match(line):
                    in_code_fence = not in_code_fence
                    out_lines.append(line)
                    continue
                if in_code_fence or _HEADING_RE.match(line):
                    out_lines.append(line)
                    continue

                def _sub(m: re.Match) -> str:
                    nonlocal removed
                    removed += 1
                    return m.group(1)

                new_line = _BOLD_RE.sub(_sub, line)
                if not _ASTERISK_RULE_RE.match(new_line):
                    if "**" in new_line:
                        removed += new_line.count("**")
                        new_line = new_line.replace("**", "")
                out_lines.append(new_line)
            new_body = "".join(out_lines)

        new_text = frontmatter + new_body
        if removed <= 0:
            continue

        total_removed += removed
        changes.append(FileChange(path=md, bold_removed=removed))

        if args.apply:
            md.write_text(new_text, encoding="utf-8")

    print(f"Scanned: {scanned} files")
    print(f"Files with changes: {len(changes)}")
    print(f"Total '**...**' removed: {total_removed}")

    if changes and not args.summary_only:
        print("\nPer-file changes:")
        report_n = min(len(changes), max(0, args.max_report))
        for ch in changes[:report_n]:
            rel = ch.path.as_posix()
            print(f"- {rel}: {ch.bold_removed}")
        if report_n < len(changes):
            print(f"... and {len(changes) - report_n} more")

    if args.apply:
        print("\nAPPLY MODE: changes written to disk")
    else:
        print("\nDRY-RUN: no files modified (re-run with --apply to write)")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
