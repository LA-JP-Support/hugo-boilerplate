#!/usr/bin/env python3
"""
Add internal links using CSV database
Uses pre-built link database for intelligent and consistent linking
"""

import csv
import re
from pathlib import Path
from typing import Dict, List, Tuple
from collections import defaultdict
import argparse

class DatabaseLinkBuilder:
    def __init__(self, database_csv: Path):
        self.database_csv = database_csv
        self.link_database: List[Dict] = []
        self.load_database()
    
    def load_database(self):
        """Load link database from CSV"""
        print(f"Loading link database from {self.database_csv}")
        
        if not self.database_csv.exists():
            print(f"Error: Database file not found: {self.database_csv}")
            return
        
        with open(self.database_csv, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            self.link_database = list(reader)
        
        print(f"Loaded {len(self.link_database)} keyword variations")
    
    def add_links_to_content(self, content: str, current_url: str) -> Tuple[str, int]:
        """Add internal links to content using database"""
        # Split into frontmatter and body
        fm_match = re.search(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
        if not fm_match:
            return content, 0
        
        frontmatter = fm_match.group(0)
        body = content[len(frontmatter):]
        
        # Track linked terms
        linked_terms = defaultdict(int)
        existing_links = set()
        
        # Find existing links
        for match in re.finditer(r'\[([^\]]+)\]\(([^)]+)\)', body):
            existing_links.add(match.group(1).lower().strip())
        
        links_added = 0
        max_links_per_term = 5  # Increased from 3
        max_total_links = 500  # Increased from 200
        
        # Process keywords by priority
        for entry in self.link_database:
            if links_added >= max_total_links:
                break
            
            keyword = entry['keyword']
            url = entry['url']
            description = entry['description']
            priority = int(entry['priority'])
            
            # Skip self-links
            if url == current_url:
                continue
            
            # Skip if already linked enough times
            normalized_keyword = keyword.lower().strip()
            if linked_terms[normalized_keyword] >= max_links_per_term:
                continue
            
            # Skip if already exists as a link
            if normalized_keyword in existing_links:
                continue
            
            # Create pattern for whole-word matching
            escaped_keyword = re.escape(keyword)
            pattern = r'\b(' + escaped_keyword + r')\b'
            
            term_count = 0
            
            def replace_match(match):
                nonlocal term_count, links_added
                
                start_pos = match.start()
                before_text = body[:start_pos]
                
                # Check for existing link
                if before_text.rstrip().endswith('[') or '](' in before_text[-10:]:
                    return match.group(0)
                
                # Check for shortcode
                last_shortcode_start = before_text.rfind('{{<')
                if last_shortcode_start != -1:
                    shortcode_end = body.find('>}}', last_shortcode_start)
                    if shortcode_end != -1 and shortcode_end > start_pos:
                        return match.group(0)
                
                # Check for code block
                if '`' in (before_text[-50:] if len(before_text) >= 50 else before_text):
                    backticks_before = before_text.count('`')
                    if backticks_before % 2 != 0:
                        return match.group(0)
                
                # Check for heading
                line_start = before_text.rfind('\n')
                if line_start == -1:
                    line_start = 0
                else:
                    line_start += 1
                line_prefix = before_text[line_start:start_pos]
                if line_prefix.strip().startswith('#'):
                    return match.group(0)
                
                # Limit links per term
                if term_count >= max_links_per_term:
                    return match.group(0)
                
                term_count += 1
                links_added += 1
                linked_terms[normalized_keyword] += 1
                
                # Add link with title attribute
                if description:
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
            
            # Extract current URL
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
    parser = argparse.ArgumentParser(description="Add internal links using CSV database")
    parser.add_argument("content_dir", type=Path, help="Directory containing markdown files")
    parser.add_argument("--database", type=Path, required=True, help="Path to link database CSV")
    parser.add_argument("--dry-run", action="store_true", help="Preview changes without modifying files")
    
    args = parser.parse_args()
    
    if not args.content_dir.exists():
        print(f"Error: Directory not found: {args.content_dir}")
        return
    
    if not args.database.exists():
        print(f"Error: Database file not found: {args.database}")
        return
    
    builder = DatabaseLinkBuilder(args.database)
    builder.process_directory(args.content_dir, dry_run=args.dry_run)

if __name__ == "__main__":
    main()
