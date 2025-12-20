#!/usr/bin/env python3
"""
Enhanced Glossary & Blog Enrichment Script with Tooltip Conversion
Version 2.0 - with Smart Matching for plurals, case, and word order

This script:
1. Works with both glossary AND blog directories
2. Converts tooltips to internal links (for blog posts)
3. Adds internal links to glossary terms
4. Smart matching: handles plurals, case-insensitivity, and common variations
5. Adds title attributes with descriptions for hover tooltips

Usage:
    # Process glossary (English)
    python3 scripts/enrich_glossary_blog.py content/en/glossary/
    
    # Process blog (English) - converts tooltips
    python3 scripts/enrich_glossary_blog.py content/en/blog/ --convert-tooltips
    
    # Process both (dry run)
    python3 scripts/enrich_glossary_blog.py content/en/glossary/ --dry-run
    python3 scripts/enrich_glossary_blog.py content/en/blog/ --convert-tooltips --dry-run
    
    # Japanese
    python3 scripts/enrich_glossary_blog.py content/ja/glossary/
    python3 scripts/enrich_glossary_blog.py content/ja/blog/ --convert-tooltips
"""

import argparse
import ast
import json
import re
from pathlib import Path
from typing import Dict, List, Sequence, Set, Tuple, Optional

# Default dictionary paths
DEFAULT_DICT_EN = Path("config/keyword_dictionary_en.json")
DEFAULT_DICT_JA = Path("config/keyword_dictionary_ja.json")

# Patterns
FRONT_MATTER_PATTERN = re.compile(r"^---\s*\n(.*?)\n---\s*\n?", re.DOTALL)
TOOLTIP_PATTERN = re.compile(
    r'\{\{<\s*tooltip\s+text="([^"]*)"\s*>\}\}(.*?)\{\{<\s*/tooltip\s*>\}\}',
    re.DOTALL
)
INTERNAL_LINK_PATTERN = re.compile(r'\[([^\]]+)\]\((/[^)]+)\)')

# Project root
PROJECT_ROOT = Path(__file__).parent.parent


def normalize_keyword(keyword: str) -> str:
    """Normalize keyword for matching (lowercase, remove common variations)."""
    normalized = keyword.lower().strip()
    
    # Remove common punctuation
    normalized = normalized.replace('-', ' ').replace('_', ' ')
    
    # Normalize whitespace
    normalized = re.sub(r'\s+', ' ', normalized)
    
    return normalized


def get_keyword_variations(keyword: str) -> List[str]:
    """Generate common variations of a keyword for better matching."""
    variations = [keyword]
    normalized = normalize_keyword(keyword)
    
    # Add normalized version
    if normalized != keyword.lower():
        variations.append(normalized)
    
    # Handle plurals (simple English rules)
    if normalized.endswith('s'):
        # Remove trailing 's'
        singular = normalized[:-1]
        variations.append(singular)
        
        # Handle 'ies' -> 'y'
        if normalized.endswith('ies'):
            variations.append(normalized[:-3] + 'y')
    else:
        # Add plural forms
        variations.append(normalized + 's')
        
        # Handle 'y' -> 'ies'
        if normalized.endswith('y') and len(normalized) > 2:
            variations.append(normalized[:-1] + 'ies')
    
    # Handle common variations
    # "ticket system" <-> "ticketing system"
    if ' system' in normalized:
        base = normalized.replace(' system', '')
        variations.append(base + 'ing system')
    
    if 'ing system' in normalized:
        base = normalized.replace('ing system', '')
        variations.append(base + ' system')
    
    # Remove duplicates while preserving order
    seen = set()
    unique_variations = []
    for v in variations:
        if v not in seen:
            seen.add(v)
            unique_variations.append(v)
    
    return unique_variations


class GlossaryDatabase:
    """Manages glossary entries and their metadata."""
    
    def __init__(self, glossary_dir: Path, lang: str = "en"):
        self.glossary_dir = glossary_dir
        self.lang = lang
        self.entries: Dict[str, Dict] = {}  # slug -> {title, url, description}
        # Index for fast lookup: normalized_keyword -> slug
        self.keyword_index: Dict[str, str] = {}
        self.load_entries()
    
    def load_entries(self):
        """Load all glossary entries."""
        if not self.glossary_dir.exists():
            print(f"⚠️  Glossary directory not found: {self.glossary_dir}")
            return
        
        for md_file in self.glossary_dir.glob("*.md"):
            if md_file.name == "_index.md":
                continue
            
            try:
                content = md_file.read_text(encoding='utf-8')
                
                # Extract frontmatter
                fm_match = FRONT_MATTER_PATTERN.match(content)
                if not fm_match:
                    continue
                
                frontmatter = fm_match.group(1)
                
                # Extract fields
                title = self._extract_field(frontmatter, 'title')
                description = self._extract_field(frontmatter, 'description')
                
                # Generate URL
                slug = md_file.stem
                url = f"/{self.lang}/glossary/{slug}/"
                
                if title:
                    self.entries[slug.lower()] = {
                        'title': title,
                        'url': url,
                        'description': description or title,
                        'slug': slug
                    }
                    
                    # Build keyword index with variations
                    for variation in get_keyword_variations(title):
                        if variation not in self.keyword_index:
                            self.keyword_index[variation] = slug.lower()
                    
            except Exception as e:
                print(f"⚠️  Error loading {md_file.name}: {e}")
        
        print(f"✅ Loaded {len(self.entries)} glossary entries for {self.lang}")
        print(f"   📑 Indexed {len(self.keyword_index)} keyword variations")
    
    def _extract_field(self, frontmatter: str, field: str) -> str:
        """Extract a field from frontmatter."""
        pattern = rf'^{field}:\s*["\']?(.+?)["\']?\s*$'
        match = re.search(pattern, frontmatter, re.MULTILINE)
        if match:
            return match.group(1).strip().strip('"').strip("'")
        return ""
    
    def find_by_keyword(self, keyword: str) -> Optional[Dict]:
        """Find glossary entry by keyword with smart matching."""
        # Try all variations
        for variation in get_keyword_variations(keyword):
            if variation in self.keyword_index:
                slug = self.keyword_index[variation]
                return self.entries.get(slug)
        
        return None


class TooltipConverter:
    """Converts tooltips to internal links."""
    
    def __init__(self, glossary_db: GlossaryDatabase):
        self.glossary_db = glossary_db
        self.converted_count = 0
        self.skipped_count = 0
        self.skipped_keywords: List[str] = []
    
    def convert_tooltip(self, match: re.Match) -> str:
        """Convert a single tooltip to internal link."""
        definition = match.group(1).strip()
        keyword_raw = match.group(2).strip()
        
        # Check if already has internal link
        link_match = INTERNAL_LINK_PATTERN.search(keyword_raw)
        if link_match:
            # Already has link - just remove tooltip wrapper
            self.converted_count += 1
            return keyword_raw
        
        # Clean keyword
        keyword = keyword_raw.strip().strip('*').strip('`')
        
        # Find matching glossary entry
        entry = self.glossary_db.find_by_keyword(keyword)
        
        if entry:
            # Create internal link with title attribute for hover
            link = f'[{keyword}]({entry["url"]} "{entry["description"]}")'
            self.converted_count += 1
            return link
        else:
            # No glossary entry - keep as plain text
            self.skipped_count += 1
            self.skipped_keywords.append(keyword)
            return keyword
    
    def convert_tooltips_in_text(self, text: str) -> str:
        """Convert all tooltips in text to internal links."""
        return TOOLTIP_PATTERN.sub(self.convert_tooltip, text)


class InternalLinkEnricher:
    """Adds internal links to glossary terms (for non-tooltip content)."""
    
    def __init__(self, glossary_db: GlossaryDatabase, current_slug: str = None):
        self.glossary_db = glossary_db
        self.current_slug = current_slug
        self.linked_slugs: Set[str] = set()  # Track which terms already linked
    
    def add_links(self, text: str) -> str:
        """Add internal links to glossary terms (first occurrence only)."""
        # Protect existing content
        protected: List[str] = []
        
        def protect_match(match: re.Match) -> str:
            """Protect a regex match."""
            idx = len(protected)
            protected.append(match.group(0))
            return f"__PROTECTED_{idx}__"
        
        def protect_str(text: str) -> str:
            """Protect a string directly."""
            idx = len(protected)
            protected.append(text)
            return f"__PROTECTED_{idx}__"
        
        result = text
        
        # Protect existing markdown links
        result = INTERNAL_LINK_PATTERN.sub(protect_match, result)
        
        # Protect code blocks
        result = re.sub(r'```[\s\S]*?```', protect_match, result)
        result = re.sub(r'`[^`]+`', protect_match, result)
        
        # Protect math
        result = re.sub(r'\$\$[\s\S]*?\$\$', protect_match, result)
        result = re.sub(r'\$[^$]+\$', protect_match, result)
        
        # Protect headings
        result = re.sub(r'^#{1,6}\s+.*$', protect_match, result, flags=re.MULTILINE)
        
        # Protect bold/italic
        result = re.sub(r'\*\*[^*]+\*\*', protect_match, result)
        
        # Build sorted list of glossary terms
        sorted_entries = []
        for slug, entry in self.glossary_db.entries.items():
            # Skip self-references
            if self.current_slug and slug == self.current_slug.lower():
                continue
            
            title = entry['title']
            # Only link terms with 4+ characters
            if len(title) >= 4:
                sorted_entries.append((title, entry, slug))
        
        # Sort by length (longer first)
        sorted_entries.sort(key=lambda x: -len(x[0]))
        
        # Add links (first occurrence only per target)
        for title, entry, slug in sorted_entries:
            if slug in self.linked_slugs:
                continue
            
            # Create pattern for this term
            escaped = re.escape(title)
            pattern = re.compile(
                rf"(?<![a-zA-Z0-9_\-])({escaped})(?![a-zA-Z0-9_\-])",
                re.IGNORECASE
            )
            
            match = pattern.search(result)
            if match:
                # Skip if inside protected content
                if "__PROTECTED_" in result[max(0, match.start()-20):match.start()]:
                    continue
                
                # Create link with title attribute
                new_link = f'[{match.group(1)}]({entry["url"]} "{entry["description"]}")'
                placeholder = protect_str(new_link)
                
                # Replace first occurrence
                result = result[:match.start()] + placeholder + result[match.end():]
                self.linked_slugs.add(slug)
        
        # Restore protected content (reverse order)
        for idx in range(len(protected) - 1, -1, -1):
            result = result.replace(f"__PROTECTED_{idx}__", protected[idx])
        
        return result


def split_front_matter(text: str) -> Tuple[str, str]:
    """Split frontmatter and body."""
    match = FRONT_MATTER_PATTERN.match(text)
    if not match:
        raise ValueError("File does not start with YAML front matter")
    front = match.group(1)
    body = text[match.end():]
    return front, body


def process_file(
    src: Path,
    dest: Path,
    glossary_db: GlossaryDatabase,
    convert_tooltips: bool = False,
    dry_run: bool = False
) -> None:
    """Process a single markdown file."""
    text = src.read_text(encoding='utf-8')
    front, body = split_front_matter(text)
    
    # Get current file's slug
    current_slug = src.stem
    
    # Step 1: Convert tooltips (if requested)
    if convert_tooltips:
        converter = TooltipConverter(glossary_db)
        body = converter.convert_tooltips_in_text(body)
        
        if converter.converted_count > 0:
            print(f"  🔄 Converted {converter.converted_count} tooltips")
        if converter.skipped_count > 0:
            print(f"  ⏭️  Skipped {converter.skipped_count} tooltips (no glossary match)")
            if converter.skipped_keywords:
                print(f"      Keywords: {', '.join(set(converter.skipped_keywords[:5]))}")
    
    # Step 2: Add internal links
    enricher = InternalLinkEnricher(glossary_db, current_slug=current_slug)
    body = enricher.add_links(body)
    
    if len(enricher.linked_slugs) > 0:
        print(f"  🔗 Added {len(enricher.linked_slugs)} internal links")
    
    # Reconstruct file
    new_content = f"---\n{front.strip()}\n---\n{body.lstrip()}"
    
    if dry_run:
        print(f"  [DRY-RUN] Would update {src} -> {dest}")
        return
    
    # Write file
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(new_content, encoding='utf-8')
    print(f"  ✅ Enriched: {dest.name}")


def iter_markdown_files(path: Path) -> List[Path]:
    """Get list of markdown files."""
    if path.is_file() and path.suffix.lower() == ".md":
        return [path]
    if path.is_dir():
        return sorted(p for p in path.rglob("*.md") if p.is_file() and p.name != "_index.md")
    raise FileNotFoundError(f"Input path not found: {path}")


def detect_language(input_path: Path) -> str:
    """Detect language from path."""
    path_str = str(input_path)
    if "/ja/" in path_str:
        return "ja"
    return "en"


def main():
    parser = argparse.ArgumentParser(description="Enrich glossary and blog with internal links")
    parser.add_argument('input', help='Markdown file or directory to process')
    parser.add_argument('--output', help='Optional output directory (default: update in place)')
    parser.add_argument('--convert-tooltips', action='store_true',
                       help='Convert tooltips to internal links (for blog posts)')
    parser.add_argument('--dry-run', action='store_true',
                       help='Show changes without writing files')
    
    args = parser.parse_args()
    
    input_path = Path(args.input)
    output_dir = Path(args.output) if args.output else None
    
    # Detect language
    lang = detect_language(input_path)
    print(f"📚 Language: {lang}")
    
    # Load glossary database
    glossary_dir = PROJECT_ROOT / "content" / lang / "glossary"
    glossary_db = GlossaryDatabase(glossary_dir, lang=lang)
    
    # Get files to process
    files = iter_markdown_files(input_path)
    base_dir = input_path if input_path.is_dir() else input_path.parent
    
    print(f"📝 Processing {len(files)} files...")
    if args.convert_tooltips:
        print(f"🔄 Tooltip conversion: ENABLED (with smart matching)")
    print()
    
    # Process each file
    for file_path in files:
        print(f"Processing: {file_path.name}")
        
        if output_dir:
            relative = file_path.relative_to(base_dir)
            destination = output_dir / relative
        else:
            destination = file_path
        
        try:
            process_file(
                file_path,
                destination,
                glossary_db,
                convert_tooltips=args.convert_tooltips,
                dry_run=args.dry_run
            )
        except Exception as e:
            print(f"  ❌ Error: {e}")
            import traceback
            traceback.print_exc()
        
        print()
    
    print(f"{'='*60}")
    print(f"✅ Completed processing {len(files)} files")
    print(f"{'='*60}")


if __name__ == '__main__':
    main()
