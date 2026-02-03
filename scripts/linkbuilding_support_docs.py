#!/usr/bin/env python3
"""
Linkbuilding for Support Docs
Adds external links to main site glossary from support-docs HTML files.
Uses the same keyword definitions as the main site but converts URLs to absolute external links.
"""

import os
import sys
import re
import argparse
import yaml
from pathlib import Path
from typing import Dict, List, Optional
from dataclasses import dataclass, field
from collections import defaultdict
from datetime import datetime
from bs4 import BeautifulSoup, NavigableString, Tag
import html


# Base URL for external links to main site
DEFAULT_BASE_URL = "https://smartweb.co.jp"


@dataclass
class Keyword:
    """Represents a keyword to be linked"""
    keyword: str
    url: str
    title: str = ""
    priority: int = 0
    exact_match: bool = False
    
    def __post_init__(self):
        self.keyword_lower = self.keyword.lower()
        self.keyword_pattern = self._create_pattern()
        self.is_cjk = self._has_cjk()
    
    def _has_cjk(self) -> bool:
        """Check if keyword contains CJK characters"""
        for char in self.keyword:
            code = ord(char)
            if 0x4E00 <= code <= 0x9FFF:  # CJK Unified Ideographs
                return True
            if 0x3040 <= code <= 0x309F:  # Hiragana
                return True
            if 0x30A0 <= code <= 0x30FF:  # Katakana
                return True
        return False
    
    def _create_pattern(self) -> re.Pattern:
        """Create regex pattern for keyword matching"""
        escaped = re.escape(self.keyword)
        
        if self._has_cjk():
            pattern = f'({escaped})'
            return re.compile(pattern)
        else:
            if self.exact_match:
                pattern = r'(?<![A-Za-z0-9_])' + escaped + r'(?![A-Za-z0-9_])'
            else:
                pattern = r'(?<![A-Za-z0-9_])' + escaped + r'(?![A-Za-z0-9_])'
            return re.compile(pattern, re.IGNORECASE)


@dataclass
class LinkConfig:
    """Configuration for linkbuilding"""
    max_replacements_per_keyword: int = 2
    max_replacements_per_url: int = 2
    max_links_on_page: int = 30
    min_paragraph_length: int = 30
    skip_existing_links: bool = True
    add_title_attribute: bool = True
    external_link_target: str = "_blank"
    nofollow_external: bool = False  # Same domain, no nofollow needed


@dataclass
class LinkStatistics:
    """Statistics for link additions"""
    total_files_processed: int = 0
    total_files_modified: int = 0
    total_links_added: int = 0
    links_per_keyword: Dict[str, int] = field(default_factory=dict)
    links_per_file: Dict[str, int] = field(default_factory=dict)
    
    def add_link(self, keyword: str, file_path: str):
        self.total_links_added += 1
        self.links_per_keyword[keyword] = self.links_per_keyword.get(keyword, 0) + 1
        self.links_per_file[file_path] = self.links_per_file.get(file_path, 0) + 1


class SupportDocsLinkBuilder:
    """Linkbuilding processor for support-docs"""
    
    SKIP_TAGS = {
        'a', 'script', 'style', 'code', 'pre', 'button', 'input', 'textarea',
        'select', 'option', 'label', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6',
        'nav', 'header', 'footer', 'aside', 'meta', 'link', 'img', 'svg',
        'iframe', 'video', 'audio', 'canvas', 'form', 'title', 'head'
    }
    
    def __init__(
        self,
        keywords: List[Keyword],
        base_url: str,
        config: LinkConfig = None,
        dry_run: bool = False,
    ):
        # Sort by priority (higher first), then by length (longer first)
        self.keywords = sorted(keywords, key=lambda k: (-k.priority, -len(k.keyword)))
        self.base_url = base_url.rstrip('/')
        self.config = config or LinkConfig()
        self.stats = LinkStatistics()
        self.dry_run = dry_run
        self.reset_page_counters()
    
    def reset_page_counters(self):
        self.page_keyword_counts = defaultdict(int)
        self.page_url_counts = defaultdict(int)
        self.page_total_links = 0
    
    def _should_skip_element(self, element) -> bool:
        """Check if element should be skipped"""
        if element.parent is None:
            return True
        
        parent = element.parent
        while parent:
            if parent.name in self.SKIP_TAGS:
                return True
            # Skip elements with data-lb attribute (already processed)
            if hasattr(parent, 'get') and parent.get('data-lb'):
                return True
            parent = parent.parent
        
        return False
    
    def _create_link(self, keyword: Keyword, matched_text: str) -> Tag:
        """Create an anchor tag for the keyword"""
        soup = BeautifulSoup('', 'html.parser')
        
        # Convert relative URL to absolute external URL
        url = keyword.url
        if not url.startswith('http'):
            if not url.startswith('/'):
                url = '/' + url
            url = self.base_url + url
        
        link = soup.new_tag('a', href=url)
        link.string = matched_text
        
        if self.config.add_title_attribute and keyword.title:
            link['title'] = keyword.title
        
        if self.config.external_link_target:
            link['target'] = self.config.external_link_target
            link['rel'] = 'noopener'
        
        # Mark as processed
        link['data-lb'] = '1'
        
        return link
    
    def _process_text_node(self, text_node: NavigableString, file_path: str) -> bool:
        """Process a text node and add links"""
        if self._should_skip_element(text_node):
            return False
        
        text = str(text_node)
        if len(text.strip()) < self.config.min_paragraph_length:
            return False
        
        # Track positions that have been linked: (start, end, keyword, matched_text)
        matches_to_link = []
        
        for keyword in self.keywords:
            if self.page_total_links >= self.config.max_links_on_page:
                break
            
            if self.page_keyword_counts[keyword.keyword] >= self.config.max_replacements_per_keyword:
                continue
            
            if self.page_url_counts[keyword.url] >= self.config.max_replacements_per_url:
                continue
            
            for match in keyword.keyword_pattern.finditer(text):
                start, end = match.span()
                matched_text = match.group()
                
                # Check if this position overlaps with already linked text
                overlaps = False
                for m in matches_to_link:
                    if start < m[1] and end > m[0]:
                        overlaps = True
                        break
                
                if overlaps:
                    continue
                
                # Check limits again
                if self.page_total_links >= self.config.max_links_on_page:
                    break
                if self.page_keyword_counts[keyword.keyword] >= self.config.max_replacements_per_keyword:
                    break
                
                matches_to_link.append((start, end, keyword, matched_text))
                self.page_keyword_counts[keyword.keyword] += 1
                self.page_url_counts[keyword.url] += 1
                self.page_total_links += 1
                self.stats.add_link(keyword.keyword, file_path)
        
        if not matches_to_link:
            return False
        
        # Sort by position
        matches_to_link.sort(key=lambda x: x[0])
        
        # Build new content
        new_content = []
        last_end = 0
        
        for start, end, keyword, matched_text in matches_to_link:
            if start > last_end:
                new_content.append(text[last_end:start])
            
            link = self._create_link(keyword, matched_text)
            new_content.append(link)
            last_end = end
        
        if last_end < len(text):
            new_content.append(text[last_end:])
        
        # Replace the text node
        parent = text_node.parent
        try:
            idx = list(parent.children).index(text_node)
        except ValueError:
            return False
        
        text_node.extract()
        
        for i, content in enumerate(new_content):
            if isinstance(content, str):
                content = NavigableString(content)
            parent.insert(idx + i, content)
        
        return True
    
    def process_html(self, html_content: str, file_path: str) -> str:
        """Process HTML content and add links"""
        self.reset_page_counters()
        
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Find the main content area (article or main)
        main_content = soup.find('article') or soup.find('main') or soup.find('div', class_='content')
        if not main_content:
            main_content = soup.body if soup.body else soup
        
        # Find all text nodes in main content
        text_nodes = list(main_content.find_all(string=True))
        
        modified = False
        for text_node in text_nodes:
            if isinstance(text_node, NavigableString):
                if self._process_text_node(text_node, file_path):
                    modified = True
        
        if modified:
            return str(soup)
        return html_content
    
    def process_file(self, file_path: Path) -> bool:
        """Process a single HTML file"""
        self.stats.total_files_processed += 1
        
        try:
            content = file_path.read_text(encoding='utf-8')
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
            return False
        
        new_content = self.process_html(content, str(file_path))
        
        if new_content != content:
            self.stats.total_files_modified += 1
            if not self.dry_run:
                file_path.write_text(new_content, encoding='utf-8')
            return True
        
        return False
    
    def process_directory(self, directory: Path, language: str = 'ja'):
        """Process all HTML files in a directory"""
        # Only process files in the specified language directory
        lang_dir = directory / language
        if not lang_dir.exists():
            print(f"Language directory not found: {lang_dir}")
            return
        
        html_files = list(lang_dir.rglob('*.html'))
        total = len(html_files)
        
        print(f"Processing {total} HTML files in {lang_dir}...")
        
        for i, file_path in enumerate(html_files, 1):
            # Skip index files in root
            if file_path.name == 'index.html' and file_path.parent == lang_dir:
                continue
            
            self.process_file(file_path)
            
            if i % 50 == 0:
                print(f"  Processed {i}/{total} files...")
        
        print(f"\nCompleted!")
        print(f"  Files processed: {self.stats.total_files_processed}")
        print(f"  Files modified: {self.stats.total_files_modified}")
        print(f"  Links added: {self.stats.total_links_added}")
        print(f"  Keywords used: {len(self.stats.links_per_keyword)}")


def load_glossary_keywords(yaml_path: Path) -> List[Keyword]:
    """Load keywords from YAML file, filtering for glossary URLs only"""
    with open(yaml_path, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    
    keywords = []
    for item in data.get('keywords', []):
        url = item.get('url', '')
        
        # Only include glossary URLs
        if '/glossary/' not in url:
            continue
        
        keywords.append(Keyword(
            keyword=item.get('keyword', ''),
            url=url,
            title=item.get('title', ''),
            priority=item.get('priority', 0),
            exact_match=item.get('exact', False)
        ))
    
    print(f"Loaded {len(keywords)} glossary keywords from {yaml_path}")
    return keywords


def main():
    parser = argparse.ArgumentParser(description='Add glossary links to support-docs')
    parser.add_argument('--linkbuilding-yaml', type=str, 
                        default='data/linkbuilding/ja.yaml',
                        help='Path to linkbuilding YAML file')
    parser.add_argument('--public-dir', type=str,
                        default='support-docs/public',
                        help='Path to support-docs public directory')
    parser.add_argument('--base-url', type=str,
                        default=DEFAULT_BASE_URL,
                        help='Base URL for external links')
    parser.add_argument('--language', type=str, default='ja',
                        help='Language code to process')
    parser.add_argument('--dry-run', action='store_true',
                        help='Do not write changes, just report')
    parser.add_argument('--max-links', type=int, default=30,
                        help='Maximum links per page')
    parser.add_argument('--max-keyword', type=int, default=2,
                        help='Maximum links per keyword per page')
    
    args = parser.parse_args()
    
    # Load keywords
    yaml_path = Path(args.linkbuilding_yaml)
    if not yaml_path.exists():
        print(f"Error: YAML file not found: {yaml_path}")
        sys.exit(1)
    
    keywords = load_glossary_keywords(yaml_path)
    if not keywords:
        print("No glossary keywords found!")
        sys.exit(1)
    
    # Configure
    config = LinkConfig(
        max_links_on_page=args.max_links,
        max_replacements_per_keyword=args.max_keyword,
    )
    
    # Process
    builder = SupportDocsLinkBuilder(
        keywords=keywords,
        base_url=args.base_url,
        config=config,
        dry_run=args.dry_run,
    )
    
    public_dir = Path(args.public_dir)
    if not public_dir.exists():
        print(f"Error: Public directory not found: {public_dir}")
        sys.exit(1)
    
    builder.process_directory(public_dir, args.language)
    
    # Print top keywords
    if builder.stats.links_per_keyword:
        print("\nTop 10 keywords by link count:")
        sorted_keywords = sorted(builder.stats.links_per_keyword.items(), 
                                  key=lambda x: x[1], reverse=True)[:10]
        for kw, count in sorted_keywords:
            print(f"  {kw}: {count}")


if __name__ == '__main__':
    main()
