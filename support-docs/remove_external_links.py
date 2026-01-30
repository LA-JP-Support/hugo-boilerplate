#!/usr/bin/env python3
"""
Remove external support.smartweb.jp links from markdown files.
Converts [text](https://support.smartweb.jp/...) to just text.
"""

import re
from pathlib import Path

def remove_external_links(filepath):
    """Remove external support.smartweb.jp links from a file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Pattern: [text](https://support.smartweb.jp/...)
    # Replace with just: text
    pattern = r'\[([^\]]+)\]\(https?://support\.smartweb\.jp/[^\)]+\)'
    content = re.sub(pattern, r'\1', content)
    
    # Pattern: [text](http://support.smartweb.jp/...)
    pattern = r'\[([^\]]+)\]\(http://support\.smartweb\.jp/[^\)]+\)'
    content = re.sub(pattern, r'\1', content)
    
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    """Process all markdown files."""
    docs_dir = Path('content/ja/docs')
    
    if not docs_dir.exists():
        print(f"Directory not found: {docs_dir}")
        return
    
    fixed_count = 0
    for md_file in docs_dir.rglob('*.md'):
        if md_file.name == '_index.md':
            continue
            
        if remove_external_links(md_file):
            fixed_count += 1
            print(f"✓ Fixed: {md_file.relative_to(docs_dir)}")
    
    print(f"\nTotal files fixed: {fixed_count}")

if __name__ == '__main__':
    main()
