#!/usr/bin/env python3
"""
Fix markdown formatting issues in support docs.
Removes tabs and excessive indentation that causes content to be treated as code blocks.
"""

import os
import re
from pathlib import Path

def fix_markdown_file(filepath):
    """Fix markdown formatting in a single file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Remove leading tabs and excessive spaces
    lines = content.split('\n')
    fixed_lines = []
    
    for line in lines:
        # Remove leading tabs
        line = line.replace('\t', '')
        
        # Remove excessive leading spaces (more than 4)
        if line.startswith('        '):  # 8+ spaces
            line = line.lstrip()
        elif line.startswith('      '):  # 6+ spaces
            line = line.lstrip()
        elif line.startswith('    '):  # 4+ spaces
            # Keep if it's a list item continuation, otherwise remove
            if not any(prev_line.strip().startswith(('-', '*', '1.')) for prev_line in fixed_lines[-3:] if prev_line.strip()):
                line = line.lstrip()
        
        fixed_lines.append(line)
    
    content = '\n'.join(fixed_lines)
    
    # Fix bullet point formatting
    content = re.sub(r'^- \n\t### ', r'### ', content, flags=re.MULTILINE)
    content = re.sub(r'^- \n### ', r'### ', content, flags=re.MULTILINE)
    
    # Remove empty lines with just spaces/tabs
    content = re.sub(r'^\s+$', '', content, flags=re.MULTILINE)
    
    # Remove multiple consecutive blank lines (more than 2)
    content = re.sub(r'\n{4,}', '\n\n\n', content)
    
    # Fix table-like structures with pipes
    content = re.sub(r'^\|\s*$', '', content, flags=re.MULTILINE)
    
    # Only write if content changed
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    """Process all markdown files in getting-started directory."""
    docs_dir = Path('content/ja/docs/getting-started')
    
    if not docs_dir.exists():
        print(f"Directory not found: {docs_dir}")
        return
    
    fixed_count = 0
    for md_file in docs_dir.glob('*.md'):
        if md_file.name == '_index.md':
            continue
            
        print(f"Processing: {md_file.name}")
        if fix_markdown_file(md_file):
            fixed_count += 1
            print(f"  ✓ Fixed")
        else:
            print(f"  - No changes needed")
    
    print(f"\nTotal files fixed: {fixed_count}")

if __name__ == '__main__':
    main()
