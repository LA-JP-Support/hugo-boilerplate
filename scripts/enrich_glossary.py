#!/usr/bin/env python3
"""Enrich glossary Markdown files with keywords and internal links.

Usage examples:

    python3 scripts/enrich_glossary.py content/en/glossary/
    python3 scripts/enrich_glossary.py content/ja/glossary/ --dict config/keyword_dictionary_ja.json
    python3 scripts/enrich_glossary.py content/en/glossary/bot-avatar.md --dry-run

The script will:
- Load a keyword/link dictionary (default: config/keyword_dictionary.json)
- Automatically detect existing pages and only link to those that exist
- For each Markdown file, add missing keywords to the front matter
- Link matching terms in the body to existing glossary pages only
"""

from __future__ import annotations

import argparse
import ast
import json
import re
from pathlib import Path
from typing import Dict, List, Sequence

DEFAULT_DICT = Path("config/keyword_dictionary.json")
FRONT_MATTER_PATTERN = re.compile(r"^---\s*\n(.*?)\n---\s*\n?", re.DOTALL)
KEYWORDS_BLOCK_PATTERN = re.compile(
    r"(^keywords:\s*(?:\[[^\]]*\]|(?:\n(?:\s*-\s*[^\n]+\n?)+)))\n?",
    re.MULTILINE,
)

# Project root detection
PROJECT_ROOT = Path(__file__).parent.parent


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", help="Markdown file or directory to process")
    parser.add_argument(
        "--output",
        dest="output",
        help="Optional output directory. If omitted, files are updated in place.",
    )
    parser.add_argument(
        "--dict",
        dest="dictionary",
        default=str(DEFAULT_DICT),
        help="Path to keyword dictionary JSON (default: %(default)s)",
    )
    parser.add_argument(
        "--dry-run",
        dest="dry_run",
        action="store_true",
        help="Show planned changes without writing files",
    )
    return parser.parse_args()


def get_existing_pages(content_dir: Path) -> set:
    """Get set of existing glossary page slugs."""
    existing = set()
    if content_dir.exists():
        for md_file in content_dir.glob("*.md"):
            if md_file.name != "_index.md":
                # Convert filename to URL slug (lowercase)
                slug = md_file.stem.lower()
                existing.add(slug)
    return existing


def load_dictionary(
    path: Path, 
    existing_pages: set = None,
    lang: str = "en"
) -> List[Dict[str, Sequence[str]]]:
    """Load dictionary and filter to only include entries with existing pages."""
    with path.open("r", encoding="utf-8") as fp:
        data = json.load(fp)
    
    entries: List[Dict[str, Sequence[str]]] = []
    skipped = []
    
    for key, entry in data.items():
        if not {"keywords", "aliases", "link"} <= entry.keys():
            raise ValueError(f"Dictionary entry '{key}' must include keywords, aliases, link")
        
        # Check if the target page exists
        if existing_pages is not None:
            link = entry["link"]
            # Extract slug from link like /ja/glossary/copilot/ -> copilot
            parts = link.strip("/").split("/")
            if len(parts) >= 3:
                slug = parts[-1].lower()
                if slug not in existing_pages:
                    skipped.append((key, link))
                    continue
        
        entries.append(entry)
    
    if skipped:
        print(f"[INFO] Skipped {len(skipped)} entries (pages don't exist):")
        for key, link in skipped[:5]:
            print(f"       - {key} -> {link}")
        if len(skipped) > 5:
            print(f"       ... and {len(skipped) - 5} more")
    
    return entries


def split_front_matter(text: str) -> tuple[str, str]:
    match = FRONT_MATTER_PATTERN.match(text)
    if not match:
        raise ValueError("File does not start with YAML front matter")
    front = match.group(1)
    body = text[match.end() :]
    return front, body


def gather_keywords(front: str) -> List[str]:
    # inline list e.g. keywords: ["a", "b"]
    inline_match = re.search(r"^keywords:\s*\[(.*)\]\s*$", front, re.MULTILINE)
    if inline_match:
        inline_value = inline_match.group(1).strip()
        if inline_value:
            try:
                return list(ast.literal_eval(f"[{inline_value}]"))
            except (SyntaxError, ValueError):
                pass

    # multi-line list
    block_match = re.search(
        r"^keywords:\s*$\n((?:\s*-\s*[^\n]+\n?)+)",
        front,
        re.MULTILINE,
    )
    if block_match:
        items = []
        for line in block_match.group(1).splitlines():
            stripped = line.strip()
            if stripped.startswith("- "):
                items.append(stripped[2:].strip().strip('"'))
        return items

    return []


def format_keywords_block(keywords: Sequence[str]) -> str:
    unique = []
    seen = set()
    for kw in keywords:
        normalized = kw.strip()
        if not normalized:
            continue
        if normalized.lower() in seen:
            continue
        seen.add(normalized.lower())
        unique.append(normalized)
    quoted = ", ".join(f'"{kw}"' for kw in unique)
    return f"keywords: [{quoted}]"


def upsert_keywords(front: str, new_keywords: Sequence[str]) -> str:
    if not new_keywords:
        return front

    block = format_keywords_block(new_keywords)
    if KEYWORDS_BLOCK_PATTERN.search(front):
        return KEYWORDS_BLOCK_PATTERN.sub(block + "\n", front, count=1)

    insertion_point = re.search(r"^description:.*$", front, re.MULTILINE)
    if insertion_point:
        idx = insertion_point.end()
        return f"{front[:idx]}\n{block}\n{front[idx+1:]}"
    return f"{block}\n{front}"


def collect_new_keywords(body: str, dictionary: List[Dict[str, Sequence[str]]]) -> List[str]:
    found: List[str] = []
    body_lower = body.lower()
    for entry in dictionary:
        aliases = entry.get("aliases", [])
        if not aliases:
            continue
        if any(alias.lower() in body_lower for alias in aliases):
            found.extend(entry.get("keywords", []))
    return found


def link_terms(body: str, dictionary: List[Dict[str, Sequence[str]]]) -> str:
    """Add internal links to terms, avoiding existing markdown links."""
    # First, protect existing markdown links by replacing them with placeholders
    link_pattern = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')
    protected_links: List[str] = []
    
    def protect_link(match: re.Match[str]) -> str:
        idx = len(protected_links)
        protected_links.append(match.group(0))
        return f"__PROTECTED_LINK_{idx}__"
    
    result = link_pattern.sub(protect_link, body)
    
    # Now add links to terms
    for entry in dictionary:
        link = entry["link"]
        for alias in entry.get("aliases", []):
            escaped = re.escape(alias)
            pattern = re.compile(rf"(?<!\w)({escaped})(?!\w)", re.IGNORECASE)
            
            def _replacement(match: re.Match[str]) -> str:
                start = match.start()
                text = match.string
                
                # Skip if inside code spans/backticks
                if text[:start].count("`") % 2 == 1:
                    return match.group(0)
                
                # Skip if inside a protected placeholder
                before = text[:start]
                if "__PROTECTED_LINK_" in before:
                    last_placeholder = before.rfind("__PROTECTED_LINK_")
                    if "__" not in before[last_placeholder + 17:]:
                        # We're inside a placeholder, skip
                        return match.group(0)
                
                replacement = match.group(0)
                return f"[{replacement}]({link})"
            
            result = pattern.sub(_replacement, result)
    
    # Restore protected links
    for idx, original in enumerate(protected_links):
        result = result.replace(f"__PROTECTED_LINK_{idx}__", original)
    
    return result


def process_file(
    src: Path,
    dest: Path,
    dictionary: List[Dict[str, Sequence[str]]],
    dry_run: bool = False,
) -> None:
    text = src.read_text(encoding="utf-8")
    front, body = split_front_matter(text)

    current_keywords = gather_keywords(front)
    new_keywords = current_keywords + collect_new_keywords(body, dictionary)
    front_updated = upsert_keywords(front, new_keywords)
    body_updated = link_terms(body, dictionary)

    new_content = f"---\n{front_updated.strip()}\n---\n{body_updated.lstrip()}"

    if dry_run:
        print(f"[DRY-RUN] Would update {src} -> {dest}")
        return

    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(new_content, encoding="utf-8")
    print(f"[OK] enriched: {dest}")


def iter_markdown_files(path: Path) -> List[Path]:
    if path.is_file() and path.suffix.lower() == ".md":
        return [path]
    if path.is_dir():
        return sorted(p for p in path.rglob("*.md") if p.is_file())
    raise FileNotFoundError(f"Input path not found: {path}")


def detect_language(input_path: Path) -> str:
    """Detect language from path (en or ja)."""
    path_str = str(input_path)
    if "/ja/" in path_str:
        return "ja"
    return "en"


def main() -> None:
    args = parse_args()
    input_path = Path(args.input)
    output_dir = Path(args.output) if args.output else None
    
    # Detect language and get existing pages
    lang = detect_language(input_path)
    content_dir = PROJECT_ROOT / "content" / lang / "glossary"
    existing_pages = get_existing_pages(content_dir)
    
    print(f"[INFO] Language: {lang}")
    print(f"[INFO] Found {len(existing_pages)} existing glossary pages")
    
    # Load dictionary with filtering
    dictionary = load_dictionary(
        Path(args.dictionary), 
        existing_pages=existing_pages,
        lang=lang
    )
    print(f"[INFO] Using {len(dictionary)} dictionary entries with valid links")

    files = iter_markdown_files(input_path)
    base_dir = input_path if input_path.is_dir() else input_path.parent

    for file_path in files:
        if output_dir:
            relative = file_path.relative_to(base_dir)
            destination = output_dir / relative
        else:
            destination = file_path
        process_file(file_path, destination, dictionary, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
