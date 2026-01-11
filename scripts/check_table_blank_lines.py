#!/usr/bin/env python3

import argparse
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, List, Tuple


@dataclass
class Issue:
    path: Path
    line_no: int
    prev_line: str


_FRONTMATTER_DELIM = "---"
_CODE_FENCE_RE = re.compile(r"^\s*```")


def _split_frontmatter_lines(lines: List[str]) -> int:
    if not lines:
        return 0
    if lines[0].strip() != _FRONTMATTER_DELIM:
        return 0
    for i in range(1, len(lines)):
        if lines[i].strip() == _FRONTMATTER_DELIM:
            return i + 1
    return 0


def _is_table_separator_line(line: str) -> bool:
    s = line.strip()
    if not (s.startswith("|") and s.endswith("|")):
        return False
    if "-" not in s:
        return False
    # allow alignment colons/spaces/dashes/pipes
    return re.match(r"^\|[\s\-:|]+\|$", s) is not None


def _is_table_header_line(line: str) -> bool:
    s = line.strip()
    if not (s.startswith("|") and s.endswith("|")):
        return False
    return s.count("|") >= 3


def iter_section_files(content_dir: Path, languages: Iterable[str], sections: Iterable[str]) -> Iterable[Path]:
    for lang in languages:
        for section in sections:
            base = content_dir / lang / section
            if not base.exists():
                continue
            yield from sorted(base.rglob("*.md"))


def find_issues_in_text(text: str, path: Path) -> List[Issue]:
    lines = text.splitlines(keepends=False)
    body_start = _split_frontmatter_lines(lines)

    in_code_fence = False
    issues: List[Issue] = []

    for i in range(body_start, len(lines) - 1):
        line = lines[i]

        if _CODE_FENCE_RE.match(line):
            in_code_fence = not in_code_fence
            continue

        if in_code_fence:
            continue

        if _is_table_header_line(line) and _is_table_separator_line(lines[i + 1]):
            if i - 1 >= body_start:
                prev = lines[i - 1]
                if prev.strip() != "":
                    issues.append(
                        Issue(
                            path=path,
                            line_no=i + 1,
                            prev_line=prev.strip()[:200],
                        )
                    )

    return issues


def apply_fix(text: str) -> Tuple[str, int]:
    lines = text.splitlines(keepends=True)
    body_start = _split_frontmatter_lines([l.rstrip("\n") for l in lines])

    out: List[str] = []
    in_code_fence = False
    fixed = 0

    def _line_no_in_body(out_len: int) -> int:
        # out_len is 0-indexed; return corresponding original line number approx not used.
        return out_len + 1

    i = 0
    while i < len(lines):
        raw = lines[i]
        line = raw.rstrip("\n")

        if _CODE_FENCE_RE.match(line):
            in_code_fence = not in_code_fence
            out.append(raw)
            i += 1
            continue

        if not in_code_fence and i >= body_start and i + 1 < len(lines):
            nxt = lines[i + 1].rstrip("\n")
            if _is_table_header_line(line) and _is_table_separator_line(nxt):
                if out:
                    prev_out = out[-1].rstrip("\n")
                    if prev_out.strip() != "":
                        out.append("\n")
                        fixed += 1

        out.append(raw)
        i += 1

    return "".join(out), fixed


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--content-dir", default="content")
    parser.add_argument(
        "--languages",
        nargs="+",
        default=["en", "ja"],
        help="Languages to scan (default: en ja)",
    )
    parser.add_argument(
        "--sections",
        nargs="+",
        default=["glossary", "blog"],
        help="Sections to scan (default: glossary blog)",
    )
    parser.add_argument("--fix", action="store_true", help="Insert a blank line before table header when missing")
    parser.add_argument("--summary-only", action="store_true")
    parser.add_argument("--max-report", type=int, default=50)

    args = parser.parse_args()

    content_dir = Path(args.content_dir)
    files = list(iter_section_files(content_dir, args.languages, args.sections))

    total_issues = 0
    files_with_issues = 0
    reported: List[Issue] = []
    total_fixes = 0

    for p in files:
        text = p.read_text(encoding="utf-8")
        issues = find_issues_in_text(text, p)
        if issues:
            files_with_issues += 1
            total_issues += len(issues)
            if not args.summary_only and len(reported) < args.max_report:
                reported.extend(issues[: max(0, args.max_report - len(reported))])

        if args.fix:
            new_text, fixed = apply_fix(text)
            if fixed > 0:
                p.write_text(new_text, encoding="utf-8")
                total_fixes += fixed

    print(f"Scanned: {len(files)} files")
    print(f"Files with missing blank line before table: {files_with_issues}")
    print(f"Total table occurrences missing blank line: {total_issues}")

    if args.fix:
        print(f"Total fixes applied: {total_fixes}")
    else:
        print("DRY-RUN: no files modified (re-run with --fix to apply)")

    if reported and not args.summary_only:
        print("\nExamples:")
        for it in reported:
            rel = it.path.as_posix()
            print(f"- {rel}:{it.line_no} (prev: {it.prev_line})")
        if total_issues > len(reported):
            print(f"... and {total_issues - len(reported)} more")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
