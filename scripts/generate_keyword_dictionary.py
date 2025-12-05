#!/usr/bin/env python3
"""Generate keyword dictionary from glossary articles.

This script scans glossary markdown files and generates a keyword dictionary
that can be used by enrich_glossary.py to add internal links.

Usage:
    python scripts/generate_keyword_dictionary.py
    python scripts/generate_keyword_dictionary.py --lang ja
    python scripts/generate_keyword_dictionary.py --lang en --output config/keyword_dictionary.json
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

PROJECT_ROOT = Path(__file__).parent.parent
FRONT_MATTER_PATTERN = re.compile(r"^---\s*\n(.*?)\n---\s*\n?", re.DOTALL)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--lang",
        choices=["en", "ja"],
        default="en",
        help="Language to process (default: en)",
    )
    parser.add_argument(
        "--output",
        help="Output file path (default: config/keyword_dictionary_{lang}.json)",
    )
    return parser.parse_args()


def extract_frontmatter(text: str) -> dict[str, Any]:
    """Extract frontmatter as a dictionary."""
    match = FRONT_MATTER_PATTERN.match(text)
    if not match:
        return {}
    
    fm_text = match.group(1)
    result = {}
    
    # Parse YAML-like frontmatter
    current_key = None
    current_list = []
    
    for line in fm_text.split("\n"):
        # Check for list item
        list_match = re.match(r"^\s*-\s*(.+)$", line)
        if list_match and current_key:
            current_list.append(list_match.group(1).strip().strip('"').strip("'"))
            continue
        
        # Check for key: value
        kv_match = re.match(r"^(\w+):\s*(.*)$", line)
        if kv_match:
            # Save previous list if any
            if current_key and current_list:
                result[current_key] = current_list
                current_list = []
            
            key = kv_match.group(1)
            value = kv_match.group(2).strip()
            
            # Check if value is inline list like [a, b, c]
            if value.startswith("[") and value.endswith("]"):
                items = value[1:-1].split(",")
                result[key] = [item.strip().strip('"').strip("'") for item in items if item.strip()]
                current_key = None
            elif value:
                result[key] = value.strip('"').strip("'")
                current_key = None
            else:
                # Value will be a list on following lines
                current_key = key
                current_list = []
    
    # Save last list if any
    if current_key and current_list:
        result[current_key] = current_list
    
    return result


# Common words that should not be linked even if they match a title
EXCLUDED_ALIASES = {
    "make", "api", "edge", "loop", "state", "code", "node", "nodes",
    "chat", "flow", "test", "data", "model", "query", "rich", "slot",
    "wake", "web", "bias", "load", "rate", "red", "rag",
}


def generate_aliases(title: str, keywords: list[str] = None) -> list[str]:
    """Generate aliases from title only (not keywords to avoid conflicts)."""
    aliases = set()
    
    # Add title variations
    aliases.add(title)
    aliases.add(title.lower())
    
    # Handle parenthetical abbreviations like "Natural Language Processing (NLP)"
    paren_match = re.match(r"(.+?)\s*\(([^)]+)\)\s*$", title)
    if paren_match:
        full_name = paren_match.group(1).strip()
        abbrev = paren_match.group(2).strip()
        aliases.add(full_name)
        aliases.add(full_name.lower())
        aliases.add(abbrev)
        aliases.add(abbrev.lower())
    
    # Handle hyphenated terms
    if "-" in title:
        # Add space-separated version
        aliases.add(title.replace("-", " "))
        aliases.add(title.replace("-", " ").lower())
    
    # Note: We intentionally don't add frontmatter keywords as aliases
    # because they often contain generic terms like "AI", "machine learning"
    # that would cause conflicts between multiple glossary entries
    
    # Remove empty strings and excluded common words
    aliases.discard("")
    aliases = {a for a in aliases if a.lower() not in EXCLUDED_ALIASES}
    
    return sorted(aliases, key=lambda x: (-len(x), x.lower()))


def process_glossary_file(file_path: Path, lang: str) -> dict[str, Any] | None:
    """Process a single glossary file and return dictionary entry."""
    text = file_path.read_text(encoding="utf-8")
    fm = extract_frontmatter(text)
    
    title = fm.get("title", "")
    if not title:
        return None
    
    # Get keywords from frontmatter
    keywords = fm.get("keywords", [])
    if isinstance(keywords, str):
        keywords = [keywords]
    
    # Generate slug from filename
    slug = file_path.stem.lower()
    link = f"/{lang}/glossary/{slug}/"
    
    # Generate aliases
    aliases = generate_aliases(title, keywords)
    
    # Filter aliases to reasonable length (avoid very short ones that cause false matches)
    aliases = [a for a in aliases if len(a) >= 2]
    
    return {
        "title": title,
        "keywords": keywords if keywords else [title],
        "link": link,
        "aliases": aliases,
    }


def main():
    args = parse_args()
    lang = args.lang
    
    glossary_dir = PROJECT_ROOT / "content" / lang / "glossary"
    if not glossary_dir.exists():
        print(f"[ERROR] Glossary directory not found: {glossary_dir}")
        return
    
    output_path = args.output
    if not output_path:
        output_path = PROJECT_ROOT / "config" / f"keyword_dictionary_{lang}.json"
    else:
        output_path = Path(output_path)
    
    dictionary = {}
    
    for md_file in sorted(glossary_dir.glob("*.md")):
        if md_file.name == "_index.md":
            continue
        
        entry = process_glossary_file(md_file, lang)
        if entry:
            # Use title as key
            key = entry["title"]
            dictionary[key] = {
                "keywords": entry["keywords"],
                "link": entry["link"],
                "aliases": entry["aliases"],
            }
    
    # Write output
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as f:
        json.dump(dictionary, f, ensure_ascii=False, indent=2)
    
    print(f"[OK] Generated {len(dictionary)} entries -> {output_path}")
    
    # Show sample entries
    print("\nSample entries:")
    for i, (key, entry) in enumerate(list(dictionary.items())[:3]):
        print(f"  {key}:")
        print(f"    link: {entry['link']}")
        print(f"    aliases: {entry['aliases'][:5]}...")


if __name__ == "__main__":
    main()
