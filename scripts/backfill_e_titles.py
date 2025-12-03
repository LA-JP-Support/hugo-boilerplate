#!/usr/bin/env python3
"""Add missing e-title values to Japanese glossary files.

For each file under content/ja/glossary/:
  - If frontmatter already has `e-title`, skip.
  - Otherwise, copy the English title from the matching content/en/glossary/<slug>.md file.
  - If the English file doesn't exist or lacks a title, fall back to the translationKey
    (converted from kebab-case to Title Case).
"""

import argparse
import re
from pathlib import Path
from typing import Dict, Tuple

import yaml

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n(.*)$", re.DOTALL)


def parse_markdown(path: Path) -> Tuple[Dict, str]:
    text = path.read_text(encoding="utf-8")
    match = FRONTMATTER_RE.match(text)
    if not match:
        return {}, text
    fm_raw, body = match.groups()
    fm = yaml.safe_load(fm_raw) or {}
    return fm, body


def dump_markdown(fm: Dict, body: str) -> str:
    fm_yaml = yaml.safe_dump(fm, allow_unicode=True, sort_keys=False).strip()
    return f"---\n{fm_yaml}\n---\n\n{body.lstrip()}"


def humanize_slug(slug: str) -> str:
    words = slug.replace("_", "-").split("-")
    return " ".join(w.capitalize() for w in words if w)


def ensure_e_title(ja_path: Path, en_path: Path) -> bool:
    fm_ja, body = parse_markdown(ja_path)
    if not fm_ja:
        return False

    if "e-title" in fm_ja and fm_ja["e-title"]:
        return False

    title_en = None
    if en_path.exists():
        fm_en, _ = parse_markdown(en_path)
        title_en = fm_en.get("title")

    if not title_en:
        translation_key = fm_ja.get("translationKey") or ja_path.stem
        title_en = humanize_slug(str(translation_key))

    if not title_en:
        return False

    fm_ja["e-title"] = title_en
    ja_path.write_text(dump_markdown(fm_ja, body), encoding="utf-8")
    return True


def main() -> None:
    parser = argparse.ArgumentParser(description="Backfill e-title fields for Japanese glossary files")
    parser.add_argument(
        "--ja-dir",
        default="content/ja/glossary",
        help="Directory containing Japanese glossary Markdown files",
    )
    parser.add_argument(
        "--en-dir",
        default="content/en/glossary",
        help="Directory containing English glossary Markdown files",
    )
    args = parser.parse_args()

    ja_dir = Path(args.ja_dir)
    en_dir = Path(args.en_dir)

    updated = 0
    skipped = 0

    for ja_file in sorted(ja_dir.glob("*.md")):
        en_file = en_dir / ja_file.name
        if ensure_e_title(ja_file, en_file):
            updated += 1
            print(f"Added e-title to {ja_file.relative_to(ja_dir.parent.parent)}")
        else:
            skipped += 1

    print(f"Done. Updated {updated} file(s), skipped {skipped} file(s).")


if __name__ == "__main__":
    main()
