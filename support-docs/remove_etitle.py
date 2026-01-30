#!/usr/bin/env python3
"""
Remove e-title field from all markdown files.
This field is unnecessary since English titles will be added during translation.
"""

import re
from pathlib import Path

def remove_etitle_from_file(filepath):
    """Remove e-title line from frontmatter."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove e-title line from frontmatter
    # Match: e-title: "..." or e-title: '...' or e-title: ...
    pattern = r'^e-title:.*$\n?'
    new_content = re.sub(pattern, '', content, flags=re.MULTILINE)
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

def main():
    """Process all markdown files."""
    docs_dir = Path('content/ja/docs')
    
    if not docs_dir.exists():
        print(f"Directory not found: {docs_dir}")
        return
    
    removed_count = 0
    
    print("Removing e-title fields...\n")
    
    for md_file in docs_dir.rglob('*.md'):
        if remove_etitle_from_file(md_file):
            removed_count += 1
            print(f"✓ {md_file.relative_to(docs_dir)}")
    
    print(f"\n{'='*60}")
    print(f"✅ Removed e-title from {removed_count} files")

if __name__ == '__main__':
    main()
