#!/usr/bin/env python3
"""Normalize glossary titles and translation keys.

Removes redundant suffixes such as "：用語集と包括的ガイド" or
": Glossary & Comprehensive Guide" from titles (including `e-title`),
and trims trailing `-glossary-...` segments from translation keys.

Usage examples:

    python scripts/title_sanitizer.py content/en/glossary/
    python scripts/title_sanitizer.py content/ja/glossary/Embed-Script.md

Pass one or more files/directories. Directories are scanned non-recursively
unless --recursive is specified.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path
from typing import Dict, Iterable, List, Tuple

import yaml


FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n(.*)$", re.DOTALL)
TITLE_SUFFIX_KEYWORDS_EN = (
    "glossary",
    "guide",
)
# Patterns to remove from end of titles (case-insensitive)
TITLE_SUFFIX_PATTERNS_EN = (
    " in AI Chatbot & Automation",
    " in AI Chatbots & Automation",
    " in AI Chatbots",
    " for AI Chatbot & Automation",
    " for AI Chatbots & Automation",
    " for AI Chatbots",
    " (AI Chatbot & Automation)",
    " (AI Chatbots & Automation)",
    " Glossary & Deep-Dive Resource",
    " Glossary & Deep Dive",
    " – Deep Glossary and Technical Overview",
    " Glossary",
)
TITLE_SUFFIX_PATTERNS_JA = (
    "用語集と詳細リソース",
    "用語集と詳細解説",
    " – 詳細用語集と技術概要",
    "用語集",
    "(AIチャットボット&自動化)",
    "(エーアイチャットボットアンドジドウカ)",
)
TITLE_SUFFIX_KEYWORDS_JA = (
    "用語集",
    "ようごしゅう",
    "ガイド",
    "決定版",
    "けっていばん",
    "実装",
    "じっそう",
    "完全",
    "かんぜん",
    "詳細",
    "しょうさい",
    "包括的",
    "ほうかつてき",
    "解説",
    "かいせつ",
    "リソース",
    "概要",
    "がいよう",
    "技術",
    "ぎじゅつ",
)
TRANSLATION_KEY_STOP_WORDS = {
    "glossary",
    "guide",
    "comprehensive",
    "complete",
    "deep",
    "dive",
    "practical",
    "definitive",
    "implementation",
    "usage",
    "example",
    "examples",
    "best",
    "practices",
    "types",
    "type",
    "design",
    "guidelines",
    "guideline",
    "use",
    "case",
    "cases",
    "strategic",
    "value",
    "values",
    "the",
    "for",
    "ai",
    "chatbot",
    "chatbots",
    "automation",
    "and",
    "in",
    "depth",
    "technical",
    "reference",
    "overview",
    "resource",
}


def slugify_filename_stem(stem: str) -> str:
    # Normalize stems like "Delay---Sleep-Node" -> "delay-sleep-node"
    s = stem.strip().lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    s = re.sub(r"-+", "-", s).strip("-")
    return s


def parse_markdown(path: Path) -> Tuple[Dict, str]:
    text = path.read_text(encoding="utf-8")
    match = FRONTMATTER_RE.match(text)
    if not match:
        return {}, text
    fm_raw, body = match.groups()
    fm = yaml.safe_load(fm_raw) or {}
    return fm, body


def dump_markdown(frontmatter: Dict, body: str) -> str:
    fm_yaml = yaml.safe_dump(frontmatter, allow_unicode=True, sort_keys=False).strip()
    return f"---\n{fm_yaml}\n---\n\n{body.lstrip()}"


def _needs_removal(segment: str) -> bool:
    segment_lower = segment.lower()
    return any(keyword in segment_lower for keyword in TITLE_SUFFIX_KEYWORDS_EN) or any(
        keyword in segment for keyword in TITLE_SUFFIX_KEYWORDS_JA
    )


def sanitize_title_text(title: str | None) -> str | None:
    if not title:
        return title
    
    # First, remove suffix patterns like "in AI Chatbots & Automation"
    title_lower = title.lower()
    for pattern in TITLE_SUFFIX_PATTERNS_EN:
        if title_lower.endswith(pattern.lower()):
            title = title[:-len(pattern)].strip()
            break
    
    # Remove Japanese suffix patterns
    for pattern in TITLE_SUFFIX_PATTERNS_JA:
        if title.endswith(pattern):
            title = title[:-len(pattern)].strip()
            break
    
    # Remove trailing Japanese keywords (for term field with hiragana)
    changed = True
    while changed:
        changed = False
        for keyword in TITLE_SUFFIX_KEYWORDS_JA:
            if title.endswith(keyword):
                title = title[:-len(keyword)].strip()
                # Also remove common delimiters
                title = title.rstrip(" 　–-:：と")
                changed = True
                break
    
    # Then check for colon-separated suffixes (always remove everything after colon)
    for delimiter in ("：", ":"):
        if delimiter in title:
            head, _tail = title.split(delimiter, 1)
            return head.strip()
    return title.strip()


def sanitize_translation_key(key: str | None, *, filename_slug: str | None = None) -> str | None:
    if not key:
        return key
    parts = [p for p in key.lower().split("-") if p]
    while parts and parts[-1] in TRANSLATION_KEY_STOP_WORDS:
        parts.pop()
    sanitized = "-".join(parts) if parts else key.lower()

    if filename_slug:
        filename_slug = filename_slug.lower()
        if sanitized.startswith(filename_slug) and sanitized != filename_slug:
            # If key is basically "<slug>-<boilerplate>" then collapse to the slug.
            # This keeps translationKey stable and concise, and matches EN/JA easily.
            suffix = sanitized[len(filename_slug):]
            if suffix.startswith("-"):
                suffix = suffix[1:]
            if suffix:
                return filename_slug

    return sanitized


def sanitize_front_matter(frontmatter: Dict) -> bool:
    changed = False

    for field in ("title", "e-title", "term", "reading"):
        if field in frontmatter:
            sanitized = sanitize_title_text(frontmatter[field])
            if sanitized and sanitized != frontmatter[field]:
                frontmatter[field] = sanitized
                changed = True

    if "translationKey" in frontmatter:
        sanitized_key = sanitize_translation_key(frontmatter["translationKey"])
        if sanitized_key and sanitized_key != frontmatter["translationKey"]:
            frontmatter["translationKey"] = sanitized_key
            changed = True

    return changed


def process_file(path: Path, dry_run: bool = False) -> bool:
    if not path.exists() or not path.is_file():
        return False

    frontmatter, body = parse_markdown(path)
    if not frontmatter:
        return False

    # translationKey may depend on filename slug
    filename_slug = slugify_filename_stem(path.stem)
    translation_key_changed = False
    if "translationKey" in frontmatter:
        sanitized_key = sanitize_translation_key(frontmatter.get("translationKey"), filename_slug=filename_slug)
        if sanitized_key and sanitized_key != frontmatter.get("translationKey"):
            frontmatter["translationKey"] = sanitized_key
            translation_key_changed = True

    front_matter_changed = sanitize_front_matter(frontmatter)
    if front_matter_changed or translation_key_changed:
        if dry_run:
            return True
        path.write_text(dump_markdown(frontmatter, body), encoding="utf-8")
        return True
    return False


def iter_markdown_files(paths: Iterable[Path], recursive: bool = False) -> Iterable[Path]:
    for path in paths:
        if path.is_dir():
            glob = "**/*.md" if recursive else "*.md"
            yield from path.glob(glob)
        elif path.suffix.lower() == ".md":
            yield path


def main() -> None:
    parser = argparse.ArgumentParser(description="Normalize glossary titles and translation keys")
    parser.add_argument("paths", nargs="+", help="Markdown files or directories to process")
    parser.add_argument("--recursive", action="store_true", help="Scan directories recursively")
    parser.add_argument("--dry-run", action="store_true", help="Show what would change without writing")
    args = parser.parse_args()

    targets = [Path(p).resolve() for p in args.paths]
    changed_files: List[Path] = []

    for md_file in iter_markdown_files(targets, recursive=args.recursive):
        if process_file(md_file, dry_run=args.dry_run):
            changed_files.append(md_file)

    if args.dry_run:
        for file in changed_files:
            print(f"[DRY-RUN] Would sanitize: {file}")
        print(f"[DRY-RUN] {len(changed_files)} file(s) would be updated.")
    else:
        for file in changed_files:
            print(f"Sanitized: {file}")
        print(f"Updated {len(changed_files)} file(s).")


if __name__ == "__main__":
    main()
