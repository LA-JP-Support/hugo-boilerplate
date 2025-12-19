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


REFERENCE_HEADING_KEYWORDS_EN = [
    "references",
    "reference",
    "further reading",
    "resources",
    "further reading and authoritative resources",
    "additional reading",
    "more reading",
]

REFERENCE_HEADING_KEYWORDS_JA = [
    "参考",
    "資料",
    "出典",
    "さらなる読み物",
    "権威あるリソース",
    "さらなるリソース",
]

ADDITIONAL_HEADING_KEYWORDS_EN = [
    "additional resources",
    "explore more",
    "additional resource",
    "extra resources",
]

ADDITIONAL_HEADING_KEYWORDS_JA = [
    "追加のリソース",
    "追加リソース",
    "さらに探索する",
    "さらなるリソース",
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
        # Pattern 5: Bullet form "- **Label:** [Link](url)"
        patterns.append(
            re.compile(
                rf"(?m)^\s*[-*]\s*\*\*{escaped}[:：]\*\*\s+\[[^\]]+\]\([^)]+\)"
                rf"(?:[,、]?\s*\[[^\]]+\]\([^)]+\))*[.,、]?[ \t]*\n"
            )
        )
        # Pattern 6: Bullet form "- Label: [Link](url)" without bold
        patterns.append(
            re.compile(
                rf"(?m)^\s*[-*]\s*(?:\*\*)?{escaped}(?:\*\*)?[:：]\s+\[[^\]]+\]\([^)]+\)"
                rf"(?:[,、]?\s*\[[^\]]+\]\([^)]+\))*[.,、]?[ \t]*\n"
            )
        )
        # Pattern 7: **Label:** [Link](url) on SAME LINE (inline style)
        # Matches: **Source:** [link](url), [link2](url2)
        # Also handles trailing punctuation like period, and Japanese comma (、)
        patterns.append(
            re.compile(
                rf"(?m)^\s*\*\*{escaped}[:：]\*\*[ \t]+\[[^\]]+\]\([^)]+\)"
                rf"(?:[,、]?[ \t]*\[[^\]]+\]\([^)]+\))*[.,、]?[ \t]*\n"
            )
        )
        # Pattern 8: Label: [Link](url) on SAME LINE (no bold)
        patterns.append(
            re.compile(
                rf"(?m)^\s*{escaped}[:：][ \t]+\[[^\]]+\]\([^)]+\)(?:[,、]?[ \t]*\[[^\]]+\]\([^)]+\))*[.,、]?[ \t]*\n"
            )
        )
    return patterns


INLINE_REFERENCE_PATTERNS = _build_patterns()


LINK_RE = re.compile(r"(?<!\!)\[([^\]]+)\]\((https?://[^)]+)\)")


def _split_frontmatter(text: str) -> tuple[str, str] | None:
    m = re.match(r"^---\n.*?\n---\n", text, flags=re.DOTALL)
    if not m:
        return None
    return text[: m.end()], text[m.end() :]


def _iter_lines_outside_fences(body: str):
    in_fence = False
    for line in body.splitlines(keepends=False):
        stripped = line.lstrip()
        if stripped.startswith("```"):
            in_fence = not in_fence
            yield line, False
            continue
        yield line, not in_fence


def _extract_external_links_from_line(line: str) -> list[tuple[str, str]]:
    return [(text.strip(), url.strip()) for text, url in LINK_RE.findall(line)]


def _is_external_link_list_item(line: str) -> bool:
    if re.match(r"^\s*(?:>\s*)?[-*]\s+", line) and LINK_RE.search(line):
        if re.search(r"\[\s*[^\]]+\s*\]\(/", line):
            return False
        return True
    return False


def _is_reference_label_line(line: str) -> bool:
    stripped = line.strip()
    if not stripped:
        return False
    for label in EN_LABELS + JA_LABELS:
        if re.match(rf"^(?:[-*]\s+)?(?:>\s*)?(?:\*\*)?{re.escape(label)}(?:\*\*)?\s*[:：]\s*$", stripped):
            return True
    for label in ("Key resources", "Key Resources", "For deeper reading", "For deeper reading", "For deeper reading", "Further reading", "Further Reading"):
        if re.match(rf"^(?:[-*]\s+)?(?:>\s*)?(?:\*\*)?{re.escape(label)}(?:\*\*)?\s*[:：]\s*$", stripped):
            return True
    for label in ("主要なリソース", "詳細はこちら", "詳細な情報", "さらに詳しく", "参考資料"):
        if re.match(rf"^(?:[-*]\s+)?(?:>\s*)?(?:\*\*)?{re.escape(label)}(?:\*\*)?\s*[:：]\s*$", stripped):
            return True
    return False


def _dedupe_links(links: list[tuple[str, str]]) -> list[tuple[str, str]]:
    seen: set[str] = set()
    out: list[tuple[str, str]] = []
    for text, url in links:
        if url in seen:
            continue
        seen.add(url)
        out.append((text, url))
    return out


def _references_heading(lang: str) -> str:
    return "## References" if lang == "en" else "## 参考資料"


def move_external_link_lists_to_references(text: str, *, lang: str) -> str:
    split = _split_frontmatter(text)
    if not split:
        return text
    fm, body = split

    lines = body.splitlines(keepends=False)
    ref_heading = _references_heading(lang)

    ref_heading_indices: list[int] = [
        i for i, line in enumerate(lines) if line.strip() == ref_heading
    ]
    last_ref_start = ref_heading_indices[-1] if ref_heading_indices else None

    def _find_section_end(start_idx: int) -> int:
        for j in range(start_idx + 1, len(lines)):
            if re.match(r"^##\s+", lines[j].strip()):
                return j
        return len(lines)

    last_ref_end = _find_section_end(last_ref_start) if last_ref_start is not None else None

    moved_links: list[tuple[str, str]] = []
    existing_ref_links: list[tuple[str, str]] = []
    last_ref_preface: list[str] = []

    # Collect links + preface from last existing References section (if any)
    if last_ref_start is not None and last_ref_end is not None:
        for k in range(last_ref_start + 1, last_ref_end):
            if _is_external_link_list_item(lines[k]):
                existing_ref_links.extend(_extract_external_links_from_line(lines[k]))
            elif lines[k].strip():
                last_ref_preface.append(lines[k])

    new_lines: list[str] = []
    i = 0
    in_fence = False
    while i < len(lines):
        line = lines[i]
        stripped = line.lstrip()

        if stripped.startswith("```"):
            in_fence = not in_fence
            new_lines.append(line)
            i += 1
            continue

        if in_fence:
            new_lines.append(line)
            i += 1
            continue

        # If this is an earlier References heading, drop the heading line but keep content.
        if line.strip() == ref_heading and i != last_ref_start:
            i += 1
            continue

        # If this is the last References heading, drop its entire content (we'll rebuild at end)
        if line.strip() == ref_heading and i == last_ref_start and last_ref_end is not None:
            i = last_ref_end
            continue

        # If we are inside an earlier References section, remove only external-link list items.
        in_earlier_ref_section = False
        for start_idx in ref_heading_indices[:-1] if ref_heading_indices else []:
            end_idx = _find_section_end(start_idx)
            if start_idx < i < end_idx:
                in_earlier_ref_section = True
                break

        if in_earlier_ref_section:
            if _is_external_link_list_item(line):
                moved_links.extend(_extract_external_links_from_line(line))
                i += 1
                continue
            new_lines.append(line)
            i += 1
            continue

        # Labeled blocks followed by link-list => move link list
        if _is_reference_label_line(line) and i + 1 < len(lines) and _is_external_link_list_item(lines[i + 1]):
            i += 1
            while i < len(lines) and _is_external_link_list_item(lines[i]):
                moved_links.extend(_extract_external_links_from_line(lines[i]))
                i += 1
            continue

        # Any external-link bullet/blockquote bullet => move
        if _is_external_link_list_item(line):
            moved_links.extend(_extract_external_links_from_line(line))
            i += 1
            continue

        new_lines.append(line)
        i += 1

    moved_links = _dedupe_links(moved_links)
    existing_ref_links = _dedupe_links(existing_ref_links)
    merged = _dedupe_links(existing_ref_links + moved_links)

    if not merged and not last_ref_preface:
        return fm + "\n".join(new_lines).rstrip() + "\n"

    bullets = [f"- [{t}]({u})" for t, u in merged]

    rebuilt = "\n".join(new_lines).rstrip()
    rebuilt = rebuilt.rstrip() + "\n\n" + ref_heading + "\n"
    if last_ref_preface:
        rebuilt += "\n" + "\n".join([l for l in last_ref_preface if l.strip()]) + "\n"
    if bullets:
        rebuilt += "\n" + "\n".join(bullets) + "\n"
    return fm + rebuilt.rstrip() + "\n"


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
    parser.add_argument(
        "--move-to-end",
        action="store_true",
        help="Move external link lists to a References section at the end",
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


def normalize_reference_headings(text: str) -> str:
    """Normalize reference/extra resource headings."""
    lines = text.splitlines()
    changed = False

    for idx, line in enumerate(lines):
        stripped = line.strip()
        if not stripped.startswith("##"):
            continue
        heading_text = stripped.lstrip("#").strip().lower()
        if any(keyword in heading_text for keyword in REFERENCE_HEADING_KEYWORDS_EN):
            if stripped != "## References":
                lines[idx] = "## References"
                changed = True
        elif any(keyword in heading_text for keyword in REFERENCE_HEADING_KEYWORDS_JA):
            if stripped != "## 参考資料":
                lines[idx] = "## 参考資料"
                changed = True
        elif any(keyword in heading_text for keyword in ADDITIONAL_HEADING_KEYWORDS_EN):
            if stripped != "## Additional Resources":
                lines[idx] = "## Additional Resources"
                changed = True
        elif any(keyword in heading_text for keyword in ADDITIONAL_HEADING_KEYWORDS_JA):
            if stripped != "## 追加リソース":
                lines[idx] = "## 追加リソース"
                changed = True

    if changed:
        return "\n".join(lines)
    return text


def process_file(file_path: Path, *, dry_run: bool = False, move_to_end: bool = False) -> bool:
    original = file_path.read_text(encoding="utf-8")
    updated = normalize_reference_headings(original)

    if move_to_end:
        lang = "en" if "/en/" in str(file_path) else "ja" if "/ja/" in str(file_path) else "en"
        updated = move_external_link_lists_to_references(updated, lang=lang)
    else:
        updated = remove_inline_references(updated)

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
        if process_file(md_file, dry_run=args.dry_run, move_to_end=args.move_to_end):
            changed += 1

    print(f"Processed {len(files)} file(s); updated {changed}")


if __name__ == "__main__":
    main()
