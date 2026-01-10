#!/usr/bin/env python3
"""
Linkbuilding Module for Hugo Static Sites
Processes HTML files and adds internal links based on keyword definitions.
Supports multilingual sites with different link definitions per language.
"""

import os
import sys
import json
import csv
import re
import argparse
import yaml
from pathlib import Path
from typing import Dict, List, Tuple, Optional
from urllib.parse import urlsplit, urlunsplit
from dataclasses import dataclass, field
from collections import defaultdict
from datetime import datetime
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup, NavigableString, Tag
import html
try:
    from janome.tokenizer import Tokenizer
    HAS_JANOME = True
except ImportError:
    HAS_JANOME = False


def normalize_url(url: str) -> str:
    """Normalize URLs to match Hugo's default lowercase path behavior.

    Amplify/S3 hosting is case-sensitive. If a keyword DB contains mixed-case
    paths (e.g., /ja/glossary/LiveAgent/), generated links can 404 even though
    Hugo outputs lowercase paths.
    
    This normalizes only the path portion, preserving query and fragment.
    """
    if url is None:
        return ""
    url = str(url).strip()
    if not url:
        return ""

    parts = urlsplit(url)
    if parts.scheme or parts.netloc:
        return urlunsplit((parts.scheme, parts.netloc, parts.path.lower(), parts.query, parts.fragment))

    # Relative URL: preserve query/fragment while lowercasing path
    path = url
    fragment = ""
    query = ""

    if "#" in path:
        path, fragment = path.split("#", 1)
    if "?" in path:
        path, query = path.split("?", 1)

    path = path.lower()

    out = path
    if query:
        out += "?" + query
    if fragment:
        out += "#" + fragment
    return out


@dataclass
class Keyword:
    """Represents a keyword to be linked"""
    keyword: str
    url: str
    title: str = ""
    priority: int = 0
    exact_match: bool = False
    
    def __post_init__(self):
        # Normalize keyword for case-insensitive matching
        self.keyword_lower = self.keyword.lower()
        self.keyword_pattern = self._create_pattern()
        self.is_cjk = self._has_cjk()
    
    def _has_cjk(self) -> bool:
        """Check if keyword contains CJK (Chinese, Japanese, Korean) characters"""
        for char in self.keyword:
            code = ord(char)
            # CJK Unified Ideographs and extensions
            if 0x4E00 <= code <= 0x9FFF:  # CJK Unified Ideographs
                return True
            if 0x3400 <= code <= 0x4DBF:  # CJK Extension A
                return True
            if 0x20000 <= code <= 0x2A6DF:  # CJK Extension B
                return True
            # Japanese specific
            if 0x3040 <= code <= 0x309F:  # Hiragana
                return True
            if 0x30A0 <= code <= 0x30FF:  # Katakana
                return True
            # Korean specific
            if 0xAC00 <= code <= 0xD7AF:  # Hangul Syllables
                return True
            if 0x1100 <= code <= 0x11FF:  # Hangul Jamo
                return True
        return False
    
    def _create_pattern(self) -> re.Pattern:
        """Create regex pattern for keyword matching
        
        For CJK (Japanese, Chinese, Korean) keywords:
        - No word boundary check needed (these languages don't use spaces)
        - Direct substring matching
        
        For ASCII/Latin keywords:
        - Use word boundary pattern to avoid partial matches
        - e.g., 'AI' should not match 'MAIL'
        """
        escaped = re.escape(self.keyword)
        
        # Check if keyword contains CJK characters
        if self._has_cjk():
            # CJK: Direct matching without word boundaries
            # Japanese/Chinese/Korean don't use spaces between words
            pattern = f'({escaped})'
            return re.compile(pattern)
        else:
            # ASCII/Latin: Use word boundary matching
            # But use lookahead/lookbehind for better control
            if self.exact_match:
                pattern = r'(?<![A-Za-z0-9_])' + escaped + r'(?![A-Za-z0-9_])'
            else:
                pattern = r'(?<![A-Za-z0-9_])' + escaped + r'(?![A-Za-z0-9_])'
            return re.compile(pattern, re.IGNORECASE)


@dataclass
class LinkConfig:
    """Configuration for linkbuilding"""
    max_replacements_per_keyword: int = 2  # Reduced from 2
    max_replacements_per_url: int = 2  # Reduced from 5
    max_replacements_per_keyword_url: int = 1
    max_links_on_page: int = 50  # Dramatically reduced from 500!
    max_replacements_per_page: int = 30  # Reduced from 50
    max_replacements_per_paragraph: int = 3  # Reduced from 10
    min_chars_between_links: int = 1  # Increased from 2 to avoid link clustering
    min_paragraph_length: int = 30  # Increased from 30
    max_paragraph_density: int = 30  # Increased from 30 - min chars per link in paragraph
    skip_existing_links: bool = True
    preserve_case: bool = True
    add_title_attribute: bool = True
    external_link_target: str = "_blank"
    internal_link_target: str = ""
    nofollow_external: bool = True
    track_statistics: bool = True
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'LinkConfig':
        """Create config from dictionary"""
        return cls(**{k: v for k, v in data.items() if hasattr(cls, k)})


@dataclass
class LinkStatistics:
    """Statistics for link additions"""
    total_files_processed: int = 0
    total_files_modified: int = 0
    total_links_added: int = 0
    links_per_keyword: Dict[str, int] = field(default_factory=dict)
    links_per_url: Dict[str, int] = field(default_factory=dict)
    links_per_file: Dict[str, int] = field(default_factory=dict)
    errors: List[str] = field(default_factory=list)
    
    def add_link(self, keyword: str, url: str, file_path: str):
        """Record a link addition"""
        self.total_links_added += 1
        self.links_per_keyword[keyword] = self.links_per_keyword.get(keyword, 0) + 1
        self.links_per_url[url] = self.links_per_url.get(url, 0) + 1
        self.links_per_file[file_path] = self.links_per_file.get(file_path, 0) + 1
    
    def to_html(self) -> str:
        """Generate HTML report"""
        html_parts = [
            '<!DOCTYPE html>',
            '<html lang="en">',
            '<head>',
            '<meta charset="UTF-8">',
            '<meta name="viewport" content="width=device-width, initial-scale=1.0">',
            '<title>Linkbuilding Report</title>',
            '<style>',
            'body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif; margin: 20px; background: #f5f5f5; }',
            '.container { max-width: 1200px; margin: 0 auto; background: white; padding: 20px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }',
            'h1 { color: #333; border-bottom: 2px solid #007bff; padding-bottom: 10px; }',
            'h2 { color: #555; margin-top: 30px; }',
            '.stats { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 20px; margin: 20px 0; }',
            '.stat-card { background: #f8f9fa; padding: 15px; border-radius: 5px; border-left: 4px solid #007bff; }',
            '.stat-value { font-size: 2em; font-weight: bold; color: #007bff; }',
            '.stat-label { color: #666; margin-top: 5px; }',
            'table { width: 100%; border-collapse: collapse; margin: 20px 0; }',
            'th, td { padding: 10px; text-align: left; border-bottom: 1px solid #ddd; }',
            'th { background: #007bff; color: white; position: sticky; top: 0; }',
            'tr:hover { background: #f8f9fa; }',
            '.error { background: #f8d7da; color: #721c24; padding: 10px; border-radius: 5px; margin: 10px 0; }',
            '.success { background: #d4edda; color: #155724; padding: 10px; border-radius: 5px; margin: 10px 0; }',
            '</style>',
            '</head>',
            '<body>',
            '<div class="container">',
            f'<h1>Linkbuilding Report - {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</h1>',
            
            '<div class="stats">',
            '<div class="stat-card">',
            f'<div class="stat-value">{self.total_files_processed}</div>',
            '<div class="stat-label">Files Processed</div>',
            '</div>',
            '<div class="stat-card">',
            f'<div class="stat-value">{self.total_files_modified}</div>',
            '<div class="stat-label">Files Modified</div>',
            '</div>',
            '<div class="stat-card">',
            f'<div class="stat-value">{self.total_links_added}</div>',
            '<div class="stat-label">Links Added</div>',
            '</div>',
            '<div class="stat-card">',
            f'<div class="stat-value">{len(self.links_per_keyword)}</div>',
            '<div class="stat-label">Keywords Used</div>',
            '</div>',
            '</div>',
        ]
        
        if self.total_links_added > 0:
            html_parts.append('<div class="success">✓ Successfully added links to content</div>')
        
        # Links per keyword table
        if self.links_per_keyword:
            html_parts.extend([
                '<h2>Links Added per Keyword</h2>',
                '<table>',
                '<thead><tr><th>Keyword</th><th>Count</th></tr></thead>',
                '<tbody>'
            ])
            for keyword, count in sorted(self.links_per_keyword.items(), key=lambda x: x[1], reverse=True):
                html_parts.append(f'<tr><td>{html.escape(keyword)}</td><td>{count}</td></tr>')
            html_parts.extend(['</tbody>', '</table>'])
        
        # Links per URL table
        if self.links_per_url:
            html_parts.extend([
                '<h2>Links Added per URL</h2>',
                '<table>',
                '<thead><tr><th>URL</th><th>Count</th></tr></thead>',
                '<tbody>'
            ])
            for url, count in sorted(self.links_per_url.items(), key=lambda x: x[1], reverse=True):
                html_parts.append(f'<tr><td>{html.escape(url)}</td><td>{count}</td></tr>')
            html_parts.extend(['</tbody>', '</table>'])
        
        # Modified files table
        if self.links_per_file:
            html_parts.extend([
                '<h2>Modified Files</h2>',
                '<table>',
                '<thead><tr><th>File</th><th>Links Added</th></tr></thead>',
                '<tbody>'
            ])
            for file_path, count in sorted(self.links_per_file.items(), key=lambda x: x[1], reverse=True):
                html_parts.append(f'<tr><td>{html.escape(file_path)}</td><td>{count}</td></tr>')
            html_parts.extend(['</tbody>', '</table>'])
        
        # Errors
        if self.errors:
            html_parts.append('<h2>Errors</h2>')
            for error in self.errors:
                html_parts.append(f'<div class="error">{html.escape(error)}</div>')
        
        html_parts.extend(['</div>', '</body>', '</html>'])
        return '\n'.join(html_parts)


class LinkBuilder:
    """Main linkbuilding processor"""
    
    # Elements to skip when processing
    SKIP_TAGS = {
        'a', 'script', 'style', 'code', 'pre', 'button', 'input', 'textarea',
        'select', 'option', 'label', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6',
        'nav', 'header', 'footer', 'aside', 'meta', 'link', 'img', 'svg',
        'iframe', 'video', 'audio', 'canvas', 'map', 'area', 'form', 'title',
        'head', 'footer'
    }
    
    # Paths to skip (taxonomy pages, pagination, etc.) - same as precompute_linkbuilding.py
    SKIP_PATHS = {
        '/tags/', '/categories/', '/page/', '/author/',
        '/search/', '/404.html', '/index.xml', '/sitemap.xml'
    }
    
    def __init__(
        self,
        keywords: List[Keyword],
        config: LinkConfig = None,
        language: str = None,
        dry_run: bool = False,
    ):
        self.keywords = sorted(keywords, key=lambda k: (-k.priority, -len(k.keyword)))
        self.config = config or LinkConfig()
        self.stats = LinkStatistics()
        self.current_file = None
        self.language = language or ''  # Language code for progress reporting
        self.dry_run = dry_run
        self.reset_page_counters()
        
        # Initialize Janome tokenizer for Japanese content
        self.tokenizer = None
        if HAS_JANOME and self.language.upper() == 'JA':
            self.tokenizer = Tokenizer()
    
    def reset_page_counters(self):
        """Reset counters for a new page"""
        self.page_keyword_counts = defaultdict(int)
        self.page_url_counts = defaultdict(int)
        self.page_keyword_url_counts = defaultdict(int)
        self.page_total_links = 0
        self.page_replacements = 0
        self.existing_links = 0
        self.current_page_url = None
    
    def _extract_page_url(self, soup) -> Optional[str]:
        """Extract the current page URL from HTML meta tags or canonical link"""
        # Try canonical link first
        canonical = soup.find('link', rel='canonical')
        if canonical and canonical.get('href'):
            url = canonical.get('href')
            # Extract path from full URL
            parsed = urlparse(url)
            return parsed.path
        
        # Try og:url meta tag
        og_url = soup.find('meta', property='og:url')
        if og_url and og_url.get('content'):
            url = og_url.get('content')
            parsed = urlparse(url)
            return parsed.path
        
        return None
    
    def _should_skip_url(self, keyword_url: str) -> bool:
        """Check if a keyword URL should be skipped (e.g., self-reference)"""
        if not self.current_page_url or not keyword_url:
            return False
        
        # Normalize URLs for comparison
        current_normalized = self.current_page_url.rstrip('/')
        keyword_normalized = keyword_url.rstrip('/')
        
        # Skip if keyword URL matches current page URL exactly
        if current_normalized == keyword_normalized:
            return True
        
        # Also check if keyword URL matches when language prefix is removed
        # e.g., /ja/blog/article/ should match /blog/article/
        # or /en/blog/article/ should match /blog/article/
        if current_normalized.startswith('/ja/') or current_normalized.startswith('/en/'):
            # Remove language prefix from current URL
            current_without_lang = '/' + '/'.join(current_normalized.split('/')[2:])
            if current_without_lang == keyword_normalized:
                return True
        
        # Also check the reverse: if keyword has language prefix but current doesn't
        if keyword_normalized.startswith('/ja/') or keyword_normalized.startswith('/en/'):
            keyword_without_lang = '/' + '/'.join(keyword_normalized.split('/')[2:])
            if current_normalized == keyword_without_lang:
                return True
        
        return False
    
    def should_skip_file(self, file_path: Path) -> bool:
        """Check if a file should be skipped based on its path."""
        path_str = str(file_path).replace('\\', '/')
        
        # Skip paths containing any of the skip patterns
        for skip_pattern in self.SKIP_PATHS:
            if skip_pattern in path_str:
                return True
        
        # Don't skip index.html files - they are important content pages in Hugo
        # Only skip if they match the skip patterns above
        
        return False
    
    def should_skip_for_english(self, file_path: Path, base_dir: Path) -> bool:
        """Check if a file should be skipped when processing English content.
        
        English content is at the root of public/, but other languages are in
        subdirectories like /ar/, /cs/, /de/, etc. We need to skip these.
        """
        path_str = str(file_path).replace('\\', '/')
        base_str = str(base_dir).replace('\\', '/')
        
        # Get relative path from base directory
        try:
            rel_path = file_path.relative_to(base_dir)
            parts = rel_path.parts
            
            # Check if first directory is a 2-letter language code
            if len(parts) > 0:
                first_dir = parts[0]
                # Skip if it's a 2-letter directory name (language code)
                if len(first_dir) == 2 and first_dir.isalpha() and first_dir.islower():
                    return True
        except ValueError:
            pass
        
        return False
    
    def process_directory(
        self,
        directory: str,
        exclude_dirs: List[str] = None,
        is_english: bool = False,
        file_pattern: str = None,
    ) -> LinkStatistics:
        """Process all HTML files in a directory
        
        Args:
            directory: Directory to process
            exclude_dirs: List of directory names to exclude
            is_english: True if processing English content (to skip language subdirs)
            file_pattern: Optional regex pattern to filter files to process
        """
        directory = Path(directory)
        exclude_dirs = exclude_dirs or []
        
        # Find all HTML files
        all_html_files = []
        for root, dirs, files in os.walk(directory):
            # Remove excluded directories from dirs to prevent walking into them
            dirs[:] = [d for d in dirs if d not in exclude_dirs]
            
            for file in files:
                if file.endswith('.html'):
                    all_html_files.append(Path(root) / file)
        
        # Filter out unwanted files
        html_files = []
        skipped_lang = 0
        skipped_other = 0
        skipped_pattern = 0
        
        for file_path in all_html_files:
            # Skip if it doesn't match the file pattern (if provided)
            if file_pattern and not re.search(file_pattern, str(file_path)):
                skipped_pattern += 1
                continue

            # Skip based on path patterns
            if self.should_skip_file(file_path):
                skipped_other += 1
                continue
            
            # For English, also skip language subdirectories
            if is_english and self.should_skip_for_english(file_path, directory):
                skipped_lang += 1
                continue
            
            html_files.append(file_path)
        
        print(f"Found {len(html_files)} HTML files to process")
        if skipped_lang > 0:
            print(f"  Skipped {skipped_lang} files from other language directories")
        if skipped_other > 0:
            print(f"  Skipped {skipped_other} files (categories, tags, pagination, etc.)")
        
        # Process each file with progress reporting
        total_files = len(html_files)
        for index, html_file in enumerate(html_files, 1):
            self.process_file(html_file)
            
            # Report progress every 100 files
            if index % 100 == 0:
                lang_prefix = f"[{self.language}] " if self.language else ""
                print(f"{lang_prefix}Processed {index}/{total_files} files...")
        
        # Final progress if not already shown
        if total_files > 0 and total_files % 100 != 0:
            lang_prefix = f"[{self.language}] " if self.language else ""
            print(f"{lang_prefix}Processed {total_files}/{total_files} files - completed")
        
        return self.stats
    
    def process_file(self, file_path: Path) -> bool:
        """Process a single HTML file"""
        self.current_file = str(file_path)
        self.reset_page_counters()
        
        try:
            # Read file
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Parse HTML
            parser = 'lxml'
            try:
                __import__('lxml')
            except Exception:
                parser = 'html.parser'
            soup = BeautifulSoup(content, parser)
            
            # Extract current page URL from canonical link or meta tags
            self.current_page_url = self._extract_page_url(soup)
            
            # Count existing links
            self.existing_links = len(soup.find_all('a'))
            
            # Process the document
            modified = self.process_element(soup)
            
            self.stats.total_files_processed += 1
            
            if modified and self.page_replacements > 0:
                if not self.dry_run:
                    # Write back modified content
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(str(soup))

                self.stats.total_files_modified += 1
                if self.dry_run:
                    print(f"[DRY-RUN] {file_path}: Would add {self.page_replacements} links")
                else:
                    print(f"✓ {file_path}: Added {self.page_replacements} links")
                return True
            else:
                print(f"  {file_path}: No changes")
                return False
                
        except Exception as e:
            error_msg = f"Error processing {file_path}: {str(e)}"
            self.stats.errors.append(error_msg)
            print(f"✗ {error_msg}")
            return False
    
    def process_element(self, element) -> bool:
        """Process an HTML element recursively"""
        if not element:
            return False
        
        modified = False
        
        # Skip if we've reached limits
        if (self.page_total_links >= self.config.max_links_on_page or
            self.page_replacements >= self.config.max_replacements_per_page):
            return False
        
        # Never modify inside existing links to avoid invalid nested anchors.
        if hasattr(element, 'name') and element.name == 'a':
            return False
        
        # Process children
        if hasattr(element, 'children'):
            # Create a list of children to avoid modification during iteration
            children = list(element.children)
            
            for child in children:
                if isinstance(child, NavigableString):
                    # Process text node
                    if child.parent and child.parent.name not in self.SKIP_TAGS:
                        # Skip if inside ANY link to avoid nested anchors
                        if child.parent.name == 'a' or child.parent.find_parent('a') is not None:
                            continue
                        new_content = self.process_text_node(child, child.parent)
                        if new_content != str(child):
                            # Replace the text node with new content
                            new_soup = BeautifulSoup(new_content, 'html.parser')
                            child.replace_with(new_soup)
                            modified = True
                elif isinstance(child, Tag):
                    # Skip certain tags and existing linkbuilding links
                    if child.name not in self.SKIP_TAGS:
                        # Skip ANY link element and anything inside a link
                        if child.name == 'a' or child.find_parent('a') is not None:
                            continue
                        if self.process_element(child):
                            modified = True
        
        return modified
    
    def process_text_node(self, text_node: NavigableString, parent_element) -> str:
        """Process a text node and add links
        
        Special handling for bold/strong tags to preserve formatting:
        - If parent is <strong> or <b>, wrap the entire keyword match in the link
        - This prevents breaking bold formatting in the middle
        """
        text = str(text_node)
        
        # Calculate valid boundaries for Japanese using Janome
        valid_boundaries = None
        if self.tokenizer:
            try:
                valid_boundaries = set()
                current_pos = 0
                valid_boundaries.add(0)
                for token in self.tokenizer.tokenize(text):
                    current_pos += len(token.surface)
                    valid_boundaries.add(current_pos)
            except Exception as e:
                # Use debug print only if needed, otherwise silent fail to regex-only matching
                pass

        # Check if we're inside a bold/strong tag
        is_bold_context = parent_element and parent_element.name in ('strong', 'b', 'em', 'i')
        
        # Skip short text (unless in bold context, where short text is common)
        if not is_bold_context and len(text.strip()) < self.config.min_paragraph_length:
            return text
        
        # Calculate paragraph density limit
        text_length = len(text)
        max_links_density = max(1, text_length // self.config.max_paragraph_density)
        paragraph_links = 0
        
        # Track occupied ranges to prevent overlaps: (start, end)
        occupied_ranges = []
        # Track replacements to apply: (start, end, html_content)
        replacements = []
        
        # Process keywords (already sorted by priority/length)
        for keyword in self.keywords:
            # Skip self-referencing URLs
            if self._should_skip_url(keyword.url):
                continue
            
            # Check if we can add more links (global/page limits)
            if (self.page_replacements >= self.config.max_replacements_per_page):
                break
                
            # Check paragraph density limit (skip for bold context)
            if not is_bold_context:
                if (paragraph_links >= self.config.max_replacements_per_paragraph or
                    paragraph_links >= max_links_density):
                    break
            
            # Find keyword in text
            matches = list(keyword.keyword_pattern.finditer(text))
            
            for match in matches:
                # Check keyword-specific limits INSIDE the loop to handle multiple matches in one text node
                if (self.page_keyword_counts[keyword.keyword] >= self.config.max_replacements_per_keyword or
                    self.page_url_counts[keyword.url] >= self.config.max_replacements_per_url):
                    break
                
                keyword_url_key = f"{keyword.keyword}|{keyword.url}"
                if self.page_keyword_url_counts[keyword_url_key] >= self.config.max_replacements_per_keyword_url:
                    break

                start, end = match.span()
                
                # Check morphological boundaries for Japanese
                if valid_boundaries is not None:
                    if start not in valid_boundaries or end not in valid_boundaries:
                        continue

                # Check for overlap with existing replacements
                is_overlapping = False
                for occ_start, occ_end in occupied_ranges:
                    # Check if ranges overlap
                    if max(start, occ_start) < min(end, occ_end):
                        is_overlapping = True
                        break
                    # Also enforce minimum distance between links
                    if min(abs(start - occ_end), abs(occ_start - end)) < self.config.min_chars_between_links:
                        is_overlapping = True
                        break
                
                if is_overlapping:
                    continue
                
                # Valid match found!
                matched_text = match.group(0)
                
                # Build link HTML
                link_attrs = [f'href="{keyword.url}"']
                if self.config.add_title_attribute and keyword.title:
                    link_attrs.append(f'title="{html.escape(keyword.title)}"')
                
                # Add marker attribute for linkbuilding-generated links
                link_attrs.append('data-lb="1"')
                
                # Determine if external link
                if keyword.url.startswith(('http://', 'https://', '//')):
                    parsed = urlparse(keyword.url)
                    if parsed.netloc and parsed.netloc != urlparse(self.current_file).netloc:
                        # External link
                        if self.config.external_link_target:
                            link_attrs.append(f'target="{self.config.external_link_target}"')
                        if self.config.nofollow_external:
                            link_attrs.append('rel="nofollow noopener"')
                elif self.config.internal_link_target:
                    link_attrs.append(f'target="{self.config.internal_link_target}"')
                
                link_html = f'<a {" ".join(link_attrs)}>{html.escape(matched_text)}</a>'
                
                # Record replacement
                replacements.append((start, end, link_html))
                occupied_ranges.append((start, end))
                
                # Update counters
                self.page_keyword_counts[keyword.keyword] += 1
                self.page_url_counts[keyword.url] += 1
                self.page_keyword_url_counts[keyword_url_key] += 1
                self.page_replacements += 1
                self.page_total_links += 1
                paragraph_links += 1
                
                # Update statistics
                self.stats.add_link(keyword.keyword, keyword.url, self.current_file)
        
        # If no replacements, return original text
        if not replacements:
            return text
            
        # Sort replacements by start position
        replacements.sort(key=lambda x: x[0])
        
        # Build final string
        result_parts = []
        last_idx = 0
        
        for start, end, link_html in replacements:
            # Append text before link
            if start > last_idx:
                result_parts.append(html.escape(text[last_idx:start]))
            # Append link
            result_parts.append(link_html)
            last_idx = end
            
        # Append remaining text
        if last_idx < len(text):
            result_parts.append(html.escape(text[last_idx:]))
            
        return ''.join(result_parts)


def load_denylist_terms(denylist_csv: Path) -> set[str]:
    """Load danger-term denylist and return a set of normalized terms (lowercased)."""
    terms: set[str] = set()
    try:
        with denylist_csv.open('r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                raw = (row.get('normalized') or row.get('keyword') or '').strip()
                if not raw:
                    continue
                terms.add(raw.lower())
    except Exception as e:
        print(f"Warning: Failed to load denylist {denylist_csv}: {e}")
    return terms


def load_keywords_from_csv(file_path: str) -> List[Keyword]:
    """Load keywords from CSV file"""
    keywords = []
    
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            keyword = Keyword(
                keyword=row.get('keyword', '').strip(),
                url=normalize_url(row.get('url', '').strip()),
                title=row.get('title', '').strip(),
                priority=int(row.get('priority', 0)),
                exact_match=row.get('exact_match', '').lower() in ('true', '1', 'yes')
            )
            if keyword.keyword and keyword.url:
                keywords.append(keyword)
    
    return keywords


def load_keywords_from_json(file_path: str) -> List[Keyword]:
    """Load keywords from JSON file (supports both manual and automatic formats)
    
    Both formats use the same structure with capitalized field names:
    {
        "keywords": [
            {
                "Keyword": "AI Tools",
                "URL": "/tools/",
                "Title": "Browse AI Tools",
                "Priority": 10,
                "Exact": false
            }
        ]
    }
    
    Note: The code also supports lowercase field names for backward compatibility.
    """
    keywords = []
    
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Check if data has "keywords" wrapper (for backwards compatibility)
    if isinstance(data, dict) and "keywords" in data:
        items = data["keywords"]
    elif isinstance(data, list):
        items = data
    else:
        # Support old automatic format where keywords are dict keys
        # {"AI workflow": {"url": "/flows/ai-workflow", "title": "AI Workflow Automation"}}
        items = []
        for keyword_text, values in data.items():
            if isinstance(values, dict):
                items.append({
                    "keyword": keyword_text,
                    "url": values.get("url", ""),
                    "title": values.get("title", ""),
                    "priority": values.get("priority", 0),
                    "exact_match": values.get("exact_match", False)
                })
    
    # Process each item
    for item in items:
        if isinstance(item, dict):
            # Support both lowercase and capitalized field names for compatibility
            keyword_text = item.get('Keyword', item.get('keyword', '')).strip()
            url = normalize_url(item.get('URL', item.get('url', '')).strip())
            title = item.get('Title', item.get('title', '')).strip()
            priority = item.get('Priority', item.get('priority', 0))
            exact_match = item.get('Exact', item.get('exact_match', item.get('exact', False)))
            
            keyword = Keyword(
                keyword=keyword_text,
                url=url,
                title=title,
                priority=priority,
                exact_match=exact_match
            )
            if keyword.keyword and keyword.url:
                keywords.append(keyword)
    
    return keywords


def load_keywords_from_yaml(file_path: str) -> List[Keyword]:
    """Load keywords from YAML file
    
    Expected format:
    keywords:
      - keyword: "AI Tools"
        url: "/tools/"
        title: "Browse AI Tools"
        priority: 10
        exact: false
    """
    keywords = []
    
    with open(file_path, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    
    if not data:
        return keywords
    
    # Check if data has "keywords" wrapper
    if isinstance(data, dict) and "keywords" in data:
        items = data["keywords"]
    elif isinstance(data, list):
        items = data
    else:
        return keywords
    
    # Process each item
    for item in items:
        if isinstance(item, dict):
            keyword_text = item.get('keyword', '').strip()
            url = normalize_url(item.get('url', '').strip())
            title = item.get('title', '').strip()
            priority = item.get('priority', 0)
            exact_match = item.get('exact', item.get('exact_match', False))
            
            keyword = Keyword(
                keyword=keyword_text,
                url=url,
                title=title,
                priority=priority,
                exact_match=exact_match
            )
            if keyword.keyword and keyword.url:
                keywords.append(keyword)
    
    return keywords


def load_keywords_from_multiple_sources(manual_file: Optional[str] = None,
                                       automatic_file: Optional[str] = None,
                                       manual_priority_boost: int = 10) -> List[Keyword]:
    """Load keywords from both manual and automatic sources
    
    Args:
        manual_file: Path to manual keywords file (CSV or JSON)
        automatic_file: Path to automatic keywords file (JSON)
        manual_priority_boost: Priority boost for manual keywords over automatic ones
    
    Returns:
        Combined list of keywords with manual keywords having higher priority
    """
    keywords = []
    
    # Load automatic keywords first (lower priority)
    if automatic_file and os.path.exists(automatic_file):
        try:
            auto_keywords = load_keywords_from_json(automatic_file)
            print(f"Loaded {len(auto_keywords)} automatic keywords from {automatic_file}")
            keywords.extend(auto_keywords)
        except Exception as e:
            print(f"Warning: Failed to load automatic keywords from {automatic_file}: {e}")
    
    # Load manual keywords (higher priority)
    if manual_file and os.path.exists(manual_file):
        try:
            if manual_file.endswith('.json'):
                manual_keywords = load_keywords_from_json(manual_file)
            elif manual_file.endswith('.yaml') or manual_file.endswith('.yml'):
                manual_keywords = load_keywords_from_yaml(manual_file)
            else:
                manual_keywords = load_keywords_from_csv(manual_file)
            
            # Boost priority for manual keywords
            for kw in manual_keywords:
                kw.priority += manual_priority_boost
            
            print(f"Loaded {len(manual_keywords)} manual keywords from {manual_file}")
            keywords.extend(manual_keywords)
        except Exception as e:
            print(f"Warning: Failed to load manual keywords from {manual_file}: {e}")
    
    # Remove duplicates (manual keywords take precedence due to higher priority)
    # Keep the highest priority version of each keyword
    keyword_dict = {}
    for kw in keywords:
        key = kw.keyword.lower()
        if key not in keyword_dict or kw.priority > keyword_dict[key].priority:
            keyword_dict[key] = kw
    
    return list(keyword_dict.values())


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description='Linkbuilding tool for Hugo static sites',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Process English content with manual keywords only
  python linkbuilding.py -k keywords_en.csv -d public/
  
  # Process with both manual and automatic keywords
  python linkbuilding.py -k keywords_en.csv -a en_automatic.json -d public/en/
  
  # Process with automatic keywords only
  python linkbuilding.py -a en_automatic.json -d public/en/
  
  # Process German content with German keywords, excluding other languages
  python linkbuilding.py -k keywords_de.csv -a de_automatic.json -d public/de/ --exclude en es fr
  
  # Use JSON configuration
  python linkbuilding.py -k keywords.json -d public/ -c config.json
  
  # Generate report without modifying files
  python linkbuilding.py -k keywords.csv -d public/ --dry-run

CSV Format:
  keyword,url,title,priority,exact_match
  "AI Tools",/tools/,Browse AI Tools,10,false
  "machine learning",/ml/,Learn about ML,5,true

JSON Format (Manual and Automatic - same structure):
  {
    "keywords": [
      {
        "Keyword": "AI Tools",
        "URL": "/tools/",
        "Title": "Browse AI Tools",
        "Priority": 10,
        "Exact": false
      },
      {
        "Keyword": "chatbot",
        "URL": "/flows/chatbot",
        "Title": "Build Custom Chatbots",
        "Priority": 5,
        "Exact": true
      }
    ]
  }
  
Note: Field names are capitalized (Keyword, URL, Title, Priority, Exact) but lowercase versions are also supported for compatibility.
        """
    )
    
    parser.add_argument('-k', '--keywords',
                       help='Path to manual keywords file (CSV or JSON)')
    parser.add_argument('-a', '--automatic',
                       help='Path to automatic keywords file (JSON)')
    parser.add_argument('-d', '--directory', required=True,
                       help='Directory to process HTML files')
    parser.add_argument('-c', '--config',
                       help='Configuration file (JSON)')
    parser.add_argument('--exclude', nargs='+', default=[],
                       help='Directories to exclude from processing')
    parser.add_argument('--language',
                       help='Language code being processed (for progress reporting)')
    parser.add_argument('--dry-run', action='store_true',
                       help='Analyze without modifying files')
    parser.add_argument('--max-links', type=int,
                       help='Override max links per page')
    parser.add_argument('--max-keyword', type=int,
                       help='Override max replacements per keyword')
    parser.add_argument('--max-url', type=int,
                       help='Override max replacements per URL')
    parser.add_argument('--manual-priority-boost', type=int, default=10,
                       help='Priority boost for manual keywords over automatic (default: 10)')
    parser.add_argument('--denylist', type=str, default=None,
                       help='Path to danger-term denylist CSV (optional)')
    parser.add_argument('--file-pattern', type=str,
                       help='Process only files matching this regex pattern')
    
    args = parser.parse_args()
    
    # Validate that at least one keyword source is provided
    if not args.keywords and not args.automatic:
        parser.error("At least one keyword source is required: use -k/--keywords or -a/--automatic")
    
    # Determine language being processed (code for logic vs display for progress)
    language_display = args.language  # could be e.g. "EN" for nicer progress output
    language: Optional[str] = args.language.lower() if args.language else None

    if not language:
        # Try to auto-detect language from directory
        dir_path = Path(args.directory).resolve()

        if dir_path.name in ['ar', 'cs', 'da', 'de', 'es', 'fi', 'fr', 'it', 'ja', 'ko',
                             'nl', 'no', 'pl', 'pt', 'ro', 'sk', 'sv', 'tr', 'vi', 'zh']:
            language = dir_path.name
        elif dir_path.name == 'public' or (args.exclude and len(args.exclude) >= 10):
            # Check if we're excluding language directories (indicates English processing)
            common_langs = {'ar', 'cs', 'da', 'de', 'es', 'fi', 'fr', 'it', 'ja', 'ko',
                           'nl', 'no', 'pl', 'pt', 'ro', 'sk', 'sv', 'tr', 'vi', 'zh'}
            if args.exclude:
                excluded_set = set(args.exclude)
                if len(excluded_set.intersection(common_langs)) >= 10:
                    language = 'en'

    # Load keywords from both sources
    keywords = load_keywords_from_multiple_sources(
        manual_file=args.keywords,
        automatic_file=args.automatic,
        manual_priority_boost=args.manual_priority_boost
    )

    if not keywords:
        print("Error: No keywords loaded from any source")
        sys.exit(1)

    deny_terms: set[str] = set()
    denylist_path: Optional[Path] = Path(args.denylist) if args.denylist else None
    if denylist_path is None and language in ("en", "ja"):
        auto_path = Path(f"databases/danger_terms_{language}.csv")
        if auto_path.exists():
            denylist_path = auto_path

    if denylist_path is not None and denylist_path.exists():
        deny_terms = load_denylist_terms(denylist_path)
        if deny_terms:
            before = len(keywords)
            keywords = [kw for kw in keywords if kw.keyword.lower().strip() not in deny_terms]
            after = len(keywords)
            print(f"Loaded denylist terms: {len(deny_terms)} from {denylist_path}")
            print(f"Filtered keywords via denylist: {before - after}")

    print(f"Loaded {len(keywords)} total keywords")
    
    # Load or create config
    config = LinkConfig()
    if args.config:
        with open(args.config, 'r') as f:
            config_data = json.load(f)
            config = LinkConfig.from_dict(config_data)
    
    # Override config with command line arguments
    if args.max_links:
        config.max_replacements_per_page = args.max_links
    if args.max_keyword:
        config.max_replacements_per_keyword = args.max_keyword
    if args.max_url:
        config.max_replacements_per_url = args.max_url
    
    # Create link builder with language info
    language_for_progress = language_display or (language.upper() if language else '')
    builder = LinkBuilder(keywords, config, language=language_for_progress, dry_run=args.dry_run)
    
    # Process directory
    if args.dry_run:
        print("DRY-RUN MODE: No files will be written")
    print(f"Processing directory: {args.directory}")
    if args.exclude:
        print(f"Excluding: {', '.join(args.exclude)}")
    
    # Determine if we're processing English content
    is_english = (language == 'en')
    if is_english:
        print("  Processing English content - will skip 2-letter language subdirectories")
    
    stats = builder.process_directory(args.directory, args.exclude, is_english, file_pattern=args.file_pattern)
    
    # Don't generate HTML report file, just output to console
    
    # Print detailed summary
    print(f"\n{'='*60}")
    print(f"LINKBUILDING REPORT SUMMARY")
    print(f"{'='*60}")
    print(f"  Files processed: {stats.total_files_processed}")
    if args.dry_run:
        print(f"  Files modified: {stats.total_files_modified} (dry-run: would modify)")
    else:
        print(f"  Files modified: {stats.total_files_modified}")
    print(f"  Links added: {stats.total_links_added}")
    print(f"  Keywords used: {len(stats.links_per_keyword)}")
    
    # Show top keywords by usage
    if stats.links_per_keyword:
        print(f"\nTop 10 Keywords by Usage:")
        top_keywords = sorted(stats.links_per_keyword.items(), key=lambda x: x[1], reverse=True)[:10]
        for keyword, count in top_keywords:
            print(f"  {count:4} - {keyword}")
    
    # Show top URLs by usage
    if stats.links_per_url:
        print(f"\nTop 10 URLs by Usage:")
        top_urls = sorted(stats.links_per_url.items(), key=lambda x: x[1], reverse=True)[:10]
        for url, count in top_urls:
            print(f"  {count:4} - {url}")
    
    # Don't save JSON report file, summary is already printed to console
    
    if stats.errors:
        print(f"\nErrors encountered: {len(stats.errors)}")
        for error in stats.errors[:5]:
            print(f"  - {error}")
    
    print(f"{'='*60}")
    
    # Exit with appropriate code
    sys.exit(0 if stats.errors == [] else 1)


if __name__ == '__main__':
    main()