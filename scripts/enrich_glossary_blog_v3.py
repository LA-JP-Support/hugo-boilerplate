#!/usr/bin/env python3
"""
Blog Enrichment Script V3
Converts tooltips to internal glossary links with parenthetical content matching
"""

import re
import argparse
from pathlib import Path
from typing import Dict, Set, Tuple

class GlossaryEnricher:
    def __init__(self, glossary_dir: Path, lang: str = "en"):
        self.glossary_dir = glossary_dir
        self.lang = lang
        self.glossary_index: Dict[str, Tuple[str, str]] = {}
        self.load_glossary()
    
    def load_glossary(self):
        """Load all glossary files and build keyword index"""
        print(f"Loading glossary from {self.glossary_dir}")
        
        if not self.glossary_dir.exists():
            print(f"Warning: Glossary directory not found: {self.glossary_dir}")
            return
        
        count = 0
        for md_file in self.glossary_dir.glob("*.md"):
            if md_file.name == "_index.md":
                continue
            
            try:
                content = md_file.read_text(encoding='utf-8')
                title, url = self._extract_title_and_url(content, md_file)
                
                if title and url:
                    variations = self._get_keyword_variations(title)
                    for variant in variations:
                        normalized = self._normalize_keyword(variant)
                        if normalized:
                            self.glossary_index[normalized] = (title, url)
                    count += 1
                    
            except Exception as e:
                print(f"Error loading {md_file.name}: {e}")
        
        print(f"Loaded {count} glossary entries")
        print(f"Generated {len(self.glossary_index)} keyword variations")
    
    def _extract_title_and_url(self, content: str, filepath: Path) -> Tuple[str, str]:
        """Extract title and construct URL from frontmatter"""
        fm_match = re.search(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
        if not fm_match:
            return None, None
        
        frontmatter = fm_match.group(1)
        title_match = re.search(r'^title:\s*["\']?(.+?)["\']?\s*$', frontmatter, re.MULTILINE)
        if not title_match:
            return None, None
        
        title = title_match.group(1).strip().strip('"').strip("'")
        slug = filepath.stem
        url = f"/{self.lang}/glossary/{slug}/"
        
        return title, url
    
    def _get_keyword_variations(self, title: str) -> Set[str]:
        """Generate keyword variations with parenthetical content handling"""
        variations = set()
        variations.add(title)
        
        if '(' in title and ')' in title:
            without_parens = re.sub(r'\s*\([^)]*\)\s*', '', title).strip()
            if without_parens:
                variations.add(without_parens)
            
            parens_content = re.findall(r'\(([^)]+)\)', title)
            for content in parens_content:
                content = content.strip()
                if content:
                    variations.add(content)
        
        all_variations = set(variations)
        for variant in all_variations:
            variations.add(self._normalize_keyword(variant))
        
        return variations
    
    def _normalize_keyword(self, text: str) -> str:
        """Normalize keyword for matching"""
        return text.lower().strip()
    
    def convert_tooltips(self, content: str, filepath: Path, dry_run: bool = False) -> Tuple[str, int]:
        """Convert tooltips to internal links"""
        tooltip_pattern = re.compile(r'\[([^\]]+)\]\(#\s+"([^"]+)"\)')
        
        conversions = 0
        converted_content = content
        replacements = []
        
        for match in tooltip_pattern.finditer(content):
            display_text = match.group(1)
            tooltip_text = match.group(2)
            
            matched_url = None
            matched_title = None
            
            for candidate in [tooltip_text, display_text]:
                normalized = self._normalize_keyword(candidate)
                if normalized in self.glossary_index:
                    matched_title, matched_url = self.glossary_index[normalized]
                    break
            
            if matched_url:
                new_link = f'[{display_text}]({matched_url} "{tooltip_text}")'
                replacements.append((match.start(), match.end(), new_link, tooltip_text))
                conversions += 1
        
        for start, end, new_link, keyword in reversed(replacements):
            converted_content = converted_content[:start] + new_link + converted_content[end:]
            if not dry_run:
                print(f"  ✓ Converted: {keyword}")
        
        return converted_content, conversions
    
    def process_file(self, filepath: Path, dry_run: bool = False) -> bool:
        """Process a single blog file"""
        try:
            content = filepath.read_text(encoding='utf-8')
            modified_content, conversions = self.convert_tooltips(content, filepath, dry_run)
            
            if conversions > 0:
                if dry_run:
                    print(f"\n[DRY RUN] {filepath.name}: {conversions} tooltips would be converted")
                else:
                    filepath.write_text(modified_content, encoding='utf-8')
                    print(f"\n✅ {filepath.name}: {conversions} tooltips converted")
                return True
            else:
                print(f"\n  {filepath.name}: No tooltips found")
                return False
                
        except Exception as e:
            print(f"\n❌ Error processing {filepath.name}: {e}")
            return False
    
    def process_directory(self, blog_dir: Path, dry_run: bool = False):
        """Process all blog files in directory"""
        if not blog_dir.exists():
            print(f"❌ Blog directory not found: {blog_dir}")
            return
        
        blog_files = list(blog_dir.glob("*.md"))
        
        if not blog_files:
            print(f"No markdown files found in {blog_dir}")
            return
        
        print(f"\n{'='*60}")
        print(f"Processing {len(blog_files)} blog files")
        print(f"Mode: {'DRY RUN' if dry_run else 'LIVE'}")
        print(f"{'='*60}")
        
        files_modified = 0
        
        for blog_file in sorted(blog_files):
            if self.process_file(blog_file, dry_run):
                files_modified += 1
        
        print(f"\n{'='*60}")
        print(f"Summary:")
        print(f"  Files processed: {len(blog_files)}")
        print(f"  Files modified: {files_modified}")
        print(f"{'='*60}")


def main():
    parser = argparse.ArgumentParser(description="Convert blog tooltips to internal glossary links (V3)")
    parser.add_argument("blog_dir", type=Path, help="Path to blog directory")
    parser.add_argument("--convert-tooltips", action="store_true", help="Convert tooltips to internal links")
    parser.add_argument("--dry-run", action="store_true", help="Preview changes without modifying files")
    parser.add_argument("--glossary-dir", type=Path, default=None, help="Path to glossary directory")
    
    args = parser.parse_args()
    
    if args.glossary_dir is None:
        args.glossary_dir = args.blog_dir.parent / "glossary"
    
    lang = "en" if "/en/" in str(args.blog_dir) else "ja"
    enricher = GlossaryEnricher(args.glossary_dir, lang=lang)
    
    if args.convert_tooltips:
        enricher.process_directory(args.blog_dir, dry_run=args.dry_run)
    else:
        print("Please specify --convert-tooltips")


if __name__ == "__main__":
    main()
