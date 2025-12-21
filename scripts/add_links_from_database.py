#!/usr/bin/env python3
"""
Add internal links using CSV database with content protection and Japanese support
Improved masking for existing links and smart boundary detection for mixed script
"""

import csv
import re
import uuid
from pathlib import Path
from typing import Dict, List, Tuple
from collections import defaultdict
import argparse

class DatabaseLinkBuilder:
    def __init__(self, database_csv: Path):
        self.database_csv = database_csv
        self.link_database: List[Dict] = []
        self.load_database()
        self.debug = False
    
    def load_database(self):
        """Load link database from CSV and sort by keyword length (longest first)"""
        if self.database_csv.exists():
            with open(self.database_csv, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                self.link_database = list(reader)
            
            # Sort by keyword length descending
            self.link_database.sort(key=lambda x: len(x['keyword']), reverse=True)
            print(f"Loaded {len(self.link_database)} keyword variations")
        else:
            print(f"Error: Database file not found: {self.database_csv}")

    def mask_content(self, text: str) -> Tuple[str, Dict[str, str]]:
        """Mask parts of content that should not be linked using a robust parser"""
        placeholders = {}
        
        def create_placeholder(content):
            key = f"__MASKED_{uuid.uuid4().hex}__"
            placeholders[key] = content
            return key

        # 1. Mask Code Blocks (```...```) and Inline Code (`...`) first using Regex
        text = re.sub(r'```[\s\S]*?```', lambda m: create_placeholder(m.group(0)), text)
        text = re.sub(r'`[^`\n]+`', lambda m: create_placeholder(m.group(0)), text)
        
        # 2. Mask Shortcodes {{< ... >}}
        text = re.sub(r'{{<[\s\S]*?>}}', lambda m: create_placeholder(m.group(0)), text)
        
        # 3. Mask HTML Tags
        text = re.sub(r'<[^>]+>', lambda m: create_placeholder(m.group(0)), text)

        # 4. Mask Headings
        text = re.sub(r'^#+ .*$', lambda m: create_placeholder(m.group(0)), text, flags=re.MULTILINE)

        # 5. Mask Existing Links [text](url "title")
        new_text = []
        i = 0
        length = len(text)
        
        while i < length:
            if text[i] == '[':
                bracket_depth = 1
                j = i + 1
                text_end = -1
                
                while j < length:
                    if text[j] == '[':
                        bracket_depth += 1
                    elif text[j] == ']':
                        bracket_depth -= 1
                        if bracket_depth == 0:
                            text_end = j
                            break
                    j += 1
                
                if text_end != -1 and text_end + 1 < length and text[text_end + 1] == '(':
                    paren_depth = 1
                    k = text_end + 2
                    url_end = -1
                    
                    while k < length:
                        if text[k] == '(':
                            paren_depth += 1
                        elif text[k] == ')':
                            paren_depth -= 1
                            if paren_depth == 0:
                                url_end = k
                                break
                        k += 1
                    
                    if url_end != -1:
                        full_link = text[i:url_end+1]
                        new_text.append(create_placeholder(full_link))
                        i = url_end + 1
                        continue

            new_text.append(text[i])
            i += 1
            
        return "".join(new_text), placeholders

    def unmask_content(self, text: str, placeholders: Dict[str, str]) -> str:
        """Restore masked content"""
        for key, value in placeholders.items():
            text = text.replace(key, value)
        return text

    def add_links_to_content(self, content: str, current_url: str) -> Tuple[str, int]:
        """Add internal links to content using database"""
        fm_match = re.search(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
        if not fm_match:
            return content, 0
        
        frontmatter = fm_match.group(0)
        body = content[len(frontmatter):]
        
        masked_body, placeholders = self.mask_content(body)
        
        linked_terms = defaultdict(int)
        links_added = 0
        max_links_per_term = 3
        max_total_links = 100
        
        def has_cjk(s):
            return any(ord(c) > 0x2E80 for c in s)

        for entry in self.link_database:
            if links_added >= max_total_links:
                break
            
            keyword = entry['keyword']
            url = entry['url']
            
            if url == current_url:
                continue
            
            normalized_keyword = keyword.lower().strip()
            if linked_terms[normalized_keyword] >= max_links_per_term:
                continue
            
            if self.debug and keyword in ["自然言語処理", "機械学習", "AI", "チャットボット"]:
                print(f"Checking keyword: {keyword}")

            escaped_keyword = re.escape(keyword)
            
            if has_cjk(keyword):
                # CJK keywords: just match the keyword
                pattern = f'({escaped_keyword})'
            else:
                # ASCII keywords: verify boundaries are NOT alphanumeric
                # This allows "AI" in "AIカスタマー" (Japanese boundary) but not in "MAIL" (English boundary)
                # (?<![a-zA-Z0-9_]) matches if previous char is NOT alphanumeric
                # (?![a-zA-Z0-9_]) matches if next char is NOT alphanumeric
                pattern = r'(?<![a-zA-Z0-9_])(' + escaped_keyword + r')(?![a-zA-Z0-9_])'
            
            def replace_link(match):
                nonlocal links_added
                if linked_terms[normalized_keyword] >= max_links_per_term:
                    return match.group(0)
                
                links_added += 1
                linked_terms[normalized_keyword] += 1
                
                new_link = f'[{match.group(1)}]({url})'
                key = f"__MASKED_{uuid.uuid4().hex}__"
                placeholders[key] = new_link
                
                if self.debug:
                    print(f"  Linked: {keyword} -> {url}")
                
                return key
            
            masked_body = re.sub(pattern, replace_link, masked_body, flags=re.IGNORECASE)

        final_body = self.unmask_content(masked_body, placeholders)
        return frontmatter + final_body, links_added
    
    def process_file(self, filepath: Path, dry_run: bool = False) -> int:
        try:
            content = filepath.read_text(encoding='utf-8')
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
    
    def process_directory(self, content_dir: Path, dry_run: bool = False, debug: bool = False):
        self.debug = debug
        print(f"\n{'='*60}")
        print(f"Adding links from database to: {content_dir}")
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
    parser = argparse.ArgumentParser(description="Add internal links safely")
    parser.add_argument("content_dir", type=Path, help="Directory containing markdown files")
    parser.add_argument("--database", type=Path, required=True, help="Path to link database CSV")
    parser.add_argument("--dry-run", action="store_true", help="Preview changes")
    parser.add_argument("--debug", action="store_true", help="Enable debug logging")
    
    args = parser.parse_args()
    
    if not args.content_dir.exists():
        print(f"Error: Directory not found: {args.content_dir}")
        return
    
    builder = DatabaseLinkBuilder(args.database)
    builder.process_directory(args.content_dir, dry_run=args.dry_run, debug=args.debug)

if __name__ == "__main__":
    main()
