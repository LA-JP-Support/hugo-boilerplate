#!/usr/bin/env python3
"""
Detect missed linkbuilding opportunities in bold tags.
Scans HTML files in public directory and reports bold tags that contain keywords
but are not linked.
"""

import json
import os
import re
from pathlib import Path
from bs4 import BeautifulSoup
import argparse
from typing import List, Dict, Set

def load_keywords(json_path: str) -> Dict[str, str]:
    """Load keywords from JSON file. Returns dict of {keyword: url}"""
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            keywords = {}
            for item in data.get('keywords', []):
                kw = item.get('Keyword', '').strip()
                url = item.get('URL', '').strip()
                if kw and url:
                    keywords[kw] = url
            return keywords
    except Exception as e:
        print(f"Error loading keywords: {e}")
        return {}

def create_keyword_pattern(keywords: List[str]) -> re.Pattern:
    """Create regex pattern for keywords"""
    # Sort by length descending to match longest first
    sorted_kws = sorted(keywords, key=len, reverse=True)
    
    parts = []
    for kw in sorted_kws:
        if any(ord(c) > 127 for c in kw):
            # CJK - no word boundaries
            parts.append(re.escape(kw))
        else:
            # ASCII - word boundaries
            parts.append(r'\b' + re.escape(kw) + r'\b')
            
    return re.compile('|'.join(parts), re.IGNORECASE)

def scan_file(file_path: Path, keywords: Dict[str, str], pattern: re.Pattern) -> List[str]:
    """Scan a single HTML file for missed bold links"""
    issues = []
    try:
        content = file_path.read_text(encoding='utf-8')
        soup = BeautifulSoup(content, 'html.parser')
        
        # Find all bold tags
        bold_tags = soup.find_all(['strong', 'b'])
        
        for tag in bold_tags:
            text = tag.get_text()
            
            # Skip if tag contains an anchor directly
            if tag.find('a'):
                continue
                
            # Skip if tag is inside an anchor
            if tag.find_parent('a'):
                continue
            
            # Find matches in the bold text
            matches = pattern.finditer(text)
            for match in matches:
                matched_text = match.group(0)
                # Check if this specific matched keyword is linked
                # Since we already checked the tag doesn't contain 'a', 
                # and isn't inside 'a', this match is definitely NOT linked.
                
                # Verify it's not a false positive (e.g. part of a longer word in ASCII)
                # The regex handles boundaries, so it should be fine.
                
                issues.append(f"Missed link in bold: '{matched_text}' in '{text[:50]}...'")
                
    except Exception as e:
        pass
        # print(f"Error scanning {file_path}: {e}")
        
    return issues

def main():
    parser = argparse.ArgumentParser(description="Detect broken bold links")
    parser.add_argument('--public-dir', default='public/ja', help='Public directory to scan')
    parser.add_argument('--keywords-json', default='data/linkbuilding/ja_automatic.json', help='Keywords JSON file')
    parser.add_argument('--limit', type=int, default=100, help='Max files to scan')
    args = parser.parse_args()
    
    print(f"Loading keywords from {args.keywords_json}...")
    keywords = load_keywords(args.keywords_json)
    print(f"Loaded {len(keywords)} keywords.")
    
    pattern = create_keyword_pattern(list(keywords.keys()))
    
    public_dir = Path(args.public_dir)
    files = list(public_dir.rglob('*.html'))
    print(f"Found {len(files)} HTML files. Scanning first {args.limit}...")
    
    total_issues = 0
    files_with_issues = 0
    
    # Prioritize the repro file if it exists
    repro_file = public_dir / 'blog/linkbuilding-repro/index.html'
    if repro_file.exists():
        files.insert(0, repro_file)
    
    # Also prioritize the reported problematic file
    rag_file = public_dir / 'blog/rag-vs-cag-knowledge-augmentation/index.html'
    if rag_file.exists():
        files.insert(0, rag_file)

    seen_files = set()
    
    for i, file_path in enumerate(files):
        if file_path in seen_files:
            continue
        seen_files.add(file_path)
        
        if len(seen_files) > args.limit:
            break
            
        issues = scan_file(file_path, keywords, pattern)
        if issues:
            print(f"\n{file_path}:")
            for issue in issues:
                print(f"  - {issue}")
            total_issues += len(issues)
            files_with_issues += 1
            
    print(f"\nScan complete.")
    print(f"Files with issues: {files_with_issues}")
    print(f"Total missed links in bold: {total_issues}")

if __name__ == '__main__':
    main()
