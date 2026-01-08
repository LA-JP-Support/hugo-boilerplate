#!/usr/bin/env python3
"""
Detect unrendered Markdown bold syntax in HTML files.
Scans for literal '**' in text nodes which indicates Hugo failed to render it.
"""

import os
from pathlib import Path
from bs4 import BeautifulSoup, NavigableString
import argparse
import re

def scan_file(file_path: Path) -> list[str]:
    issues = []
    try:
        content = file_path.read_text(encoding='utf-8')
        soup = BeautifulSoup(content, 'html.parser')
        
        # We are looking for text nodes that contain '**'
        # But we need to be careful not to match code blocks where ** is valid
        
        # Iterate over all text nodes
        for text_node in soup.find_all(string=True):
            if isinstance(text_node, NavigableString):
                text = str(text_node)
                if "**" in text:
                    # Check parent tags to exclude code/pre
                    parent = text_node.parent
                    is_code = False
                    while parent:
                        if parent.name in ['code', 'pre', 'script', 'style']:
                            is_code = True
                            break
                        parent = parent.parent
                    
                    if not is_code:
                        # Found literal ** in non-code text
                        # Extract a snippet
                        idx = text.find("**")
                        start = max(0, idx - 20)
                        end = min(len(text), idx + 50)
                        snippet = text[start:end].strip()
                        issues.append(f"Unrendered bold: ...{snippet}...")
                        
    except Exception as e:
        # print(f"Error scanning {file_path}: {e}")
        pass
        
    return issues

def main():
    parser = argparse.ArgumentParser(description="Detect unrendered bold Markdown")
    parser.add_argument('--dir', default='public/ja', help='Directory to scan')
    parser.add_argument('--limit', type=int, default=100, help='Max files to report')
    args = parser.parse_args()
    
    public_dir = Path(args.dir)
    print(f"Scanning {public_dir} for unrendered bold syntax...")
    
    count = 0
    files_with_issues = 0
    
    for root, _, files in os.walk(public_dir):
        for file in files:
            if file.endswith('.html'):
                file_path = Path(root) / file
                issues = scan_file(file_path)
                
                if issues:
                    print(f"\n{file_path}:")
                    for issue in issues:
                        print(f"  - {issue}")
                    files_with_issues += 1
                    count += 1
                    if count >= args.limit:
                        print(f"\nLimit of {args.limit} files reached.")
                        return

    print(f"\nScan complete.")
    print(f"Files with unrendered bold: {files_with_issues}")

if __name__ == '__main__':
    main()
