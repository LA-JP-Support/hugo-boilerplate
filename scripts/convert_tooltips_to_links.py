#!/usr/bin/env python3
"""
Convert Hugo tooltip shortcodes to internal glossary links (Enhanced Version v4)
Features:
- Plural form handling
- Acronym and full name matching
- Flexible separator handling (parentheses, dashes, colons)
- Partial matching with suffix removal (Learning, Prompting, problem, technology, etc.)
- Special case: prompts → prompting conversion
"""

import re
import argparse
from pathlib import Path
from typing import Dict, Set, Tuple, List

class TooltipConverter:
    def __init__(self, glossary_dir: Path, lang: str = "en"):
        self.glossary_dir = glossary_dir
        self.lang = lang
        self.glossary_index: Dict[str, Tuple[str, str]] = {}
        self.glossary_titles: List[Tuple[str, str, str]] = []  # (normalized_title, title, url)
        self.load_glossary()
    
    def load_glossary(self):
        print(f"Loading glossary from {self.glossary_dir}")
        if not self.glossary_dir.exists():
            print(f"Warning: Glossary directory not found")
            return
        
        count = 0
        for md_file in self.glossary_dir.glob("*.md"):
            if md_file.name == "_index.md":
                continue
            
            try:
                content = md_file.read_text(encoding='utf-8')
                title, url = self._extract_title_and_url(content, md_file)
                
                if title and url:
                    # Store for partial matching
                    normalized_title = self._normalize_keyword(title)
                    self.glossary_titles.append((normalized_title, title, url))
                    
                    # Store variations for exact matching
                    variations = self._get_keyword_variations(title)
                    for variant in variations:
                        normalized = self._normalize_keyword(variant)
                        if normalized and normalized not in self.glossary_index:
                            self.glossary_index[normalized] = (title, url)
                    count += 1
            except Exception as e:
                print(f"Error loading {md_file.name}: {e}")
        
        # Sort titles by length (longest first) for better partial matching
        self.glossary_titles.sort(key=lambda x: len(x[0]), reverse=True)
        
        print(f"Loaded {count} glossary entries")
        print(f"Generated {len(self.glossary_index)} keyword variations")
    
    def _extract_title_and_url(self, content: str, filepath: Path) -> Tuple[str, str]:
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
        """Generate comprehensive keyword variations including acronyms and different separators"""
        variations = set()
        variations.add(title)
        
        # Handle dash-separated format: "ITIL – Information Technology Infrastructure Library"
        if '–' in title or '—' in title or ' - ' in title:
            parts = re.split(r'\s*[–—-]\s*', title, maxsplit=1)
            for part in parts:
                part = part.strip()
                if part:
                    variations.add(part)
                    variations.add(self._normalize_keyword(part))
        
        # Handle parenthetical content (acronyms and expansions)
        if '(' in title and ')' in title:
            without_parens = re.sub(r'\s*\([^)]*\)\s*', '', title).strip()
            if without_parens:
                variations.add(without_parens)
            
            parens_content = re.findall(r'\(([^)]+)\)', title)
            for content in parens_content:
                content = content.strip()
                if content:
                    variations.add(content)
                    
                    if ':' in content:
                        parts = content.split(':', 1)
                        for part in parts:
                            part = part.strip()
                            if part:
                                variations.add(part)
        
        # Generate plural/singular variations for all base forms
        all_variations = set(variations)
        for variant in all_variations:
            variations.add(self._normalize_keyword(variant))
            
            plural_forms = self._generate_plural_forms(variant)
            for plural in plural_forms:
                variations.add(plural)
                variations.add(self._normalize_keyword(plural))
        
        return variations
    
    def _generate_plural_forms(self, word: str) -> List[str]:
        """Generate both singular and plural forms of a word"""
        forms = []
        normalized = word.lower().strip()
        
        if normalized.endswith('s'):
            singular = normalized[:-1]
            forms.append(singular)
            forms.append(word[:-1])
            
            if normalized.endswith('ies') and len(normalized) > 3:
                singular_y = normalized[:-3] + 'y'
                forms.append(singular_y)
                forms.append(word[:-3] + 'y')
            
            if normalized.endswith('ses') and len(normalized) > 3:
                singular_sis = normalized[:-2]
                forms.append(singular_sis)
                forms.append(word[:-2])
        else:
            forms.append(normalized + 's')
            forms.append(word + 's')
            
            if normalized.endswith('y') and len(normalized) > 1:
                if normalized[-2] not in 'aeiou':
                    plural_ies = normalized[:-1] + 'ies'
                    forms.append(plural_ies)
                    forms.append(word[:-1] + 'ies')
            
            if normalized.endswith(('s', 'x', 'z', 'ch', 'sh')):
                forms.append(normalized + 'es')
                forms.append(word + 'es')
        
        return forms
    
    def _normalize_keyword(self, text: str) -> str:
        """Normalize keyword for matching"""
        normalized = ' '.join(text.lower().strip().split())
        return normalized
    
    def _remove_common_suffixes(self, text: str) -> List[str]:
        """Remove common suffixes to enable partial matching"""
        variations = [text]
        normalized = text.lower().strip()
        
        # Special case: "prompts" → "prompting"
        if normalized.endswith(' prompts'):
            with_prompting = normalized[:-7] + 'prompting'
            variations.append(with_prompting)
        
        # Common suffixes to remove
        suffixes = [
            'learning', 'prompting', 'prompts', 'problem', 'problems', 
            'technology', 'technologies', 'system', 'systems',
            'assistant', 'assistants', 'phenomena', 'phenomenon'
        ]
        
        for suffix in suffixes:
            if normalized.endswith(' ' + suffix):
                without_suffix = normalized[:-len(suffix)-1].strip()
                if without_suffix:
                    variations.append(without_suffix)
        
        return variations
    
    def _find_partial_match(self, keyword: str) -> Tuple[str, str]:
        """Find partial match in glossary titles"""
        normalized_keyword = self._normalize_keyword(keyword)
        
        # Try suffix removal variations
        keyword_variations = self._remove_common_suffixes(normalized_keyword)
        
        for kw_variant in keyword_variations:
            # Check if keyword is prefix of any glossary title
            for norm_title, title, url in self.glossary_titles:
                # Check if keyword matches beginning of title
                if norm_title.startswith(kw_variant + ' ') or norm_title == kw_variant:
                    return (title, url)
                
                # Check if title without suffix matches keyword
                for title_variant in self._remove_common_suffixes(norm_title):
                    if title_variant == kw_variant:
                        return (title, url)
        
        return (None, None)
    
    def _extract_keyword_variations_from_tooltip(self, keyword: str) -> List[str]:
        """Extract all possible matching variations from a tooltip keyword"""
        variations = [keyword]
        normalized = self._normalize_keyword(keyword)
        variations.append(normalized)
        
        # Handle parenthetical content in tooltip
        if '(' in keyword and ')' in keyword:
            without_parens = re.sub(r'\s*\([^)]*\)\s*', '', keyword).strip()
            if without_parens:
                variations.append(without_parens)
                variations.append(self._normalize_keyword(without_parens))
            
            parens_content = re.findall(r'\(([^)]+)\)', keyword)
            for content in parens_content:
                content = content.strip()
                if content:
                    variations.append(content)
                    variations.append(self._normalize_keyword(content))
                    
                    if ':' in content:
                        parts = content.split(':', 1)
                        for part in parts:
                            part = part.strip()
                            if part:
                                variations.append(part)
                                variations.append(self._normalize_keyword(part))
        
        # Handle comma-separated text
        if ',' in keyword:
            before_comma = keyword.split(',')[0].strip()
            if before_comma:
                variations.append(before_comma)
                variations.append(self._normalize_keyword(before_comma))
        
        # Add suffix-removed variations
        for variant in list(variations):
            variations.extend(self._remove_common_suffixes(variant))
        
        return variations
    
    def convert_tooltips(self, content: str, filepath: Path, dry_run: bool = False) -> Tuple[str, int]:
        """Convert Hugo tooltip shortcodes to internal links"""
        tooltip_pattern = re.compile(
            r'\{\{<\s*tooltip\s+text="([^"]*)"\s*>\}\}(.*?)\{\{<\s*/tooltip\s*>\}\}',
            re.DOTALL
        )
        
        conversions = 0
        converted_content = content
        replacements = []
        
        for match in tooltip_pattern.finditer(content):
            definition = match.group(1).strip()
            keyword = match.group(2).strip()
            
            matched_url = None
            matched_title = None
            
            # Try exact matching first
            for variant in self._extract_keyword_variations_from_tooltip(keyword):
                normalized = self._normalize_keyword(variant)
                if normalized in self.glossary_index:
                    matched_title, matched_url = self.glossary_index[normalized]
                    break
            
            # If no exact match, try partial matching
            if not matched_url:
                matched_title, matched_url = self._find_partial_match(keyword)
            
            if matched_url:
                new_link = f'[{keyword}]({matched_url} "{definition}")'
                replacements.append((match.start(), match.end(), new_link, keyword))
                conversions += 1
            else:
                if not dry_run:
                    print(f"  ⚠️  No match for: {keyword}")
        
        # Apply replacements in reverse order
        for start, end, new_link, keyword in reversed(replacements):
            converted_content = converted_content[:start] + new_link + converted_content[end:]
            if not dry_run:
                print(f"  ✓ Converted: {keyword}")
        
        return converted_content, conversions
    
    def process_file(self, filepath: Path, dry_run: bool = False) -> bool:
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
    parser = argparse.ArgumentParser(
        description="Convert Hugo tooltip shortcodes to internal links (v4: prompts→prompting)"
    )
    parser.add_argument("blog_dir", type=Path, help="Path to blog directory")
    parser.add_argument("--dry-run", action="store_true", help="Preview changes")
    parser.add_argument("--glossary-dir", type=Path, default=None, help="Glossary directory")
    
    args = parser.parse_args()
    
    if args.glossary_dir is None:
        args.glossary_dir = args.blog_dir.parent / "glossary"
    
    lang = "en" if "/en/" in str(args.blog_dir) else "ja"
    converter = TooltipConverter(args.glossary_dir, lang=lang)
    converter.process_directory(args.blog_dir, dry_run=args.dry_run)

if __name__ == "__main__":
    main()
