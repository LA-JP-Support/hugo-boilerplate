#!/usr/bin/env python3
"""
Fix markdown table formatting by adding missing separator rows.
"""

import re
from pathlib import Path

def fix_table_formatting(filepath):
    """Fix markdown table formatting in a file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    lines = content.split('\n')
    fixed_lines = []
    
    i = 0
    while i < len(lines):
        line = lines[i]
        fixed_lines.append(line)
        
        # Check if this is a table header line (starts with |)
        if line.strip().startswith('|') and '|' in line:
            # Check if next line is also a table row (not a separator)
            if i + 1 < len(lines):
                next_line = lines[i + 1].strip()
                
                # If next line is a data row (starts with |) but not a separator
                if next_line.startswith('|') and not re.match(r'^\|[\s\-:]+\|', next_line):
                    # Count columns in header
                    cols = line.count('|') - 1
                    
                    # Add separator row
                    separator = '| ' + ' | '.join(['---'] * cols) + ' |'
                    fixed_lines.append(separator)
        
        i += 1
    
    content = '\n'.join(fixed_lines)
    
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
            
        if fix_table_formatting(md_file):
            fixed_count += 1
            print(f"✓ Fixed: {md_file.relative_to(docs_dir)}")
    
    print(f"\nTotal files fixed: {fixed_count}")

if __name__ == '__main__':
    main()
