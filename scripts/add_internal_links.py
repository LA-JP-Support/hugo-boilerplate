#!/usr/bin/env python3
"""
Add internal links to markdown files based on glossary terms
Automatically detects glossary terms in text and converts them to links
"""

import re
import argparse
from pathlib import Path
from typing import Dict, Set, Tuple, List

class InternalLinkBuilder:
    def __init__(self, glossary_dir: Path, lang: str = "ja"):
        self.glossary_dir = glossary_dir
        self.lang = lang
        self.glossary_index: Dict[str, Tuple[str, str, str]] = {}  # normalized_term -> (title, url, description)
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
                title, url, description = self._extract_title_url_description(content, md_file)
                
                if title and url:
                    # Generate variations
                    variations = self._get_keyword_variations(title)
                    for variant in variations:
                        normalized = self._normalize_keyword(variant)
                        if normalized and normalized not in self.glossary_index:
                            self.glossary_index[normalized] = (title, url, description or "")
                    count += 1
                    
            except Exception as e:
                print(f"Error loading {md_file.name}: {e}")
        
        print(f"Loaded {count} glossary entries")
        print(f"Generated {len(self.glossary_index)} keyword variations")
    
    def _extract_title_url_description(self, content: str, filepath: Path) -> Tuple[str, str, str]:
        """Extract title, URL, and description from frontmatter"""
        fm_match = re.search(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
        if not fm_match:
            return None, None, None
        
        frontmatter = fm_match.group(1)
        
        # Extract title
        title_match = re.search(r'^title:\s*["\']?(.+?)["\']?\s*$', frontmatter, re.MULTILINE)
        if not title_match:
            return None, None, None
        
        title = title_match.group(1).strip().strip('"').strip("'")
        
        # Extract description
        description_match = re.search(r'^description:\s*["\']?(.+?)["\']?\s*$', frontmatter, re.MULTILINE)
        description = description_match.group(1).strip().strip('"').strip("'") if description_match else ""
        
        # Construct URL
        slug = filepath.stem
        url = f"/{self.lang}/glossary/{slug}/"
        
        return title, url, description
    
    def _get_keyword_variations(self, title: str) -> Set[str]:
        """Generate keyword variations with more intelligent patterns"""
        variations = set()
        variations.add(title)
        
        # Remove parenthetical content
        if '(' in title and ')' in title:
            without_parens = re.sub(r'\s*\([^)]*\)\s*', '', title).strip()
            if without_parens and len(without_parens) > 2:
                variations.add(without_parens)
            
            # Extract parenthetical content (e.g., "NLP" from "Natural Language Processing (NLP)")
            parens_content = re.findall(r'\(([^)]+)\)', title)
            for content in parens_content:
                content = content.strip()
                if content and len(content) > 1:
                    variations.add(content)
        
        # Handle slashes (e.g., "AI/ML" -> "AI", "ML")
        if '/' in title:
            parts = title.split('/')
            for part in parts:
                part = part.strip()
                if part and len(part) > 2:
                    variations.add(part)
        
        # Handle hyphens for compound words
        if '-' in title and '(' not in title:
            without_hyphens = title.replace('-', ' ')
            if without_hyphens != title:
                variations.add(without_hyphens)
        
        # Handle common Japanese patterns
        # Remove trailing "とは" if present
        if title.endswith('とは'):
            variations.add(title[:-2])
        
        return variations
    
    def _normalize_keyword(self, keyword: str) -> str:
        """Normalize keyword for matching"""
        return keyword.lower().strip()
    
    def add_links_to_content(self, content: str, current_url: str) -> Tuple[str, int]:
        """Add internal links to content"""
        # Split into frontmatter and body
        fm_match = re.search(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
        if not fm_match:
            return content, 0
        
        frontmatter = fm_match.group(0)
        body = content[len(frontmatter):]
        
        # Track already linked terms and existing links
        linked_terms = set()
        existing_links = set()
        
        # Find existing links
        for match in re.finditer(r'\[([^\]]+)\]\(([^)]+)\)', body):
            existing_links.add(self._normalize_keyword(match.group(1)))
        
        # Calculate priority for each keyword
        keyword_priorities = {}
        for normalized_keyword, (title, url, description) in self.glossary_index.items():
            priority = len(normalized_keyword) * 2  # Longer terms get higher priority
            if '(' in title:
                priority += 50  # Terms with parentheses get bonus
            if normalized_keyword == self._normalize_keyword(title):
                priority += 100  # Exact title match gets highest priority
            keyword_priorities[normalized_keyword] = priority
        
        # Sort keywords by priority (highest first), then by length (longest first)
        sorted_keywords = sorted(
            self.glossary_index.items(),
            key=lambda x: (keyword_priorities.get(x[0], 0), len(x[0])),
            reverse=True
        )
        
        links_added = 0
        max_links_per_term = 3  # Increased from 2
        
        for normalized_keyword, (title, url, description) in sorted_keywords:
            # Skip self-links
            if url == current_url:
                continue
            
            # Skip if already linked
            if normalized_keyword in linked_terms:
                continue
            
            # Skip if already exists as a link
            if normalized_keyword in existing_links:
                continue
            
            # Count existing occurrences
            term_count = 0
            
            # Create pattern for case-insensitive matching
            # Match whole words only
            pattern = r'\b(' + re.escape(title) + r')\b'
            
            def replace_match(match):
                nonlocal term_count, links_added
                
                # Check if we're inside a link or code block
                start_pos = match.start()
                # Check for existing link
                before_text = body[:match.start()]
                if before_text.rstrip().endswith('[') or before_text.rstrip().endswith(']('):
                    return match.group(0)
                
                # Check for code block (inline code)
                if '`' in before_text[-50:] if len(before_text) >= 50 else before_text:
                    backticks_before = before_text.count('`')
                    if backticks_before % 2 != 0:  # Inside code block
                        return match.group(0)
                
                # Check for heading (more robust)
                line_start = before_text.rfind('\n')
                if line_start == -1:
                    line_start = 0
                else:
                    line_start += 1
                line_prefix = before_text[line_start:match.start()]
                if line_prefix.strip().startswith('#'):
                    return match.group(0)
                
                # Limit links per term
                if term_count >= max_links_per_term:
                    return match.group(0)
                
                term_count += 1
                links_added += 1
                linked_terms.add(normalized_keyword)
                
                # Add title attribute with description for hover tooltip
                if description:
                    # Escape quotes in description
                    escaped_desc = description.replace('"', '&quot;')
                    return f'[{match.group(1)}]({url} "{escaped_desc}")'
                else:
                    return f'[{match.group(1)}]({url})'
            
            body = re.sub(pattern, replace_match, body, flags=re.IGNORECASE)
        
        return frontmatter + body, links_added
    
    def process_file(self, filepath: Path, dry_run: bool = False) -> int:
        """Process a single markdown file"""
        try:
            content = filepath.read_text(encoding='utf-8')
            
            # Extract current URL from frontmatter
            url_match = re.search(r'^url:\s*["\']?(.+?)["\']?\s*$', content, re.MULTILINE)
            current_url = url_match.group(1) if url_match else ""
            
            modified_content, links_added = self.add_links_to_content(content, current_url)
            
            if links_added > 0:
                if not dry_run:
                    filepath.write_text(modified_content, encoding='utf-8')
                print(f"✅ {filepath.name}: {links_added} links added")
                return links_added
            else:
                print(f"  {filepath.name}: No links added")
                return 0
                
        except Exception as e:
            print(f"❌ Error processing {filepath.name}: {e}")
            return 0
    
    def process_directory(self, content_dir: Path, dry_run: bool = False):
        """Process all markdown files in directory"""
        print(f"\n{'='*60}")
        print(f"Adding internal links to: {content_dir}")
        print(f"Mode: {'DRY RUN' if dry_run else 'LIVE'}")
        print(f"{'='*60}\n")
        
        total_links = 0
        files_modified = 0
        
        for md_file in sorted(content_dir.glob("*.md")):
            if md_file.name == "_index.md":
                continue
            
            links_added = self.process_file(md_file, dry_run=dry_run)
            if links_added > 0:
                files_modified += 1
                total_links += links_added
        
        print(f"\n{'='*60}")
        print(f"Summary:")
        print(f"  Files modified: {files_modified}")
        print(f"  Total links added: {total_links}")
        print(f"{'='*60}\n")

def main():
    parser = argparse.ArgumentParser(description="Add internal links to markdown files")
    parser.add_argument("content_dir", type=Path, help="Directory containing markdown files")
    parser.add_argument("--glossary-dir", type=Path, required=True, help="Path to glossary directory")
    parser.add_argument("--lang", default="ja", help="Language code (default: ja)")
    parser.add_argument("--dry-run", action="store_true", help="Preview changes without modifying files")
    
    args = parser.parse_args()
    
    if not args.content_dir.exists():
        print(f"Error: Directory not found: {args.content_dir}")
        return
    
    if not args.glossary_dir.exists():
        print(f"Error: Glossary directory not found: {args.glossary_dir}")
        return
    
    builder = InternalLinkBuilder(args.glossary_dir, lang=args.lang)
    builder.process_directory(args.content_dir, dry_run=args.dry_run)

if __name__ == "__main__":
    main()
