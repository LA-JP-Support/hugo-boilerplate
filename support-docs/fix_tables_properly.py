#!/usr/bin/env python3
"""
Properly fix markdown tables by cleaning up broken separators and adding correct ones.
"""

import re
from pathlib import Path

def fix_table_in_content(content):
    """Fix all tables in content."""
    lines = content.split('\n')
    fixed_lines = []
    in_table = False
    table_lines = []
    
    for i, line in enumerate(lines):
        stripped = line.strip()
        
        # Check if this is a table line
        if stripped.startswith('|') and '|' in stripped[1:]:
            if not in_table:
                # Start of new table
                in_table = True
                table_lines = [line]
            else:
                # Continue table
                table_lines.append(line)
        else:
            # Not a table line
            if in_table:
                # End of table - process it
                fixed_table = fix_single_table(table_lines)
                fixed_lines.extend(fixed_table)
                in_table = False
                table_lines = []
            
            fixed_lines.append(line)
    
    # Handle table at end of file
    if in_table and table_lines:
        fixed_table = fix_single_table(table_lines)
        fixed_lines.extend(fixed_table)
    
    return '\n'.join(fixed_lines)

def fix_single_table(table_lines):
    """Fix a single table."""
    if not table_lines:
        return []
    
    # Remove any existing separator lines (lines with only |, -, :, and spaces)
    data_lines = []
    for line in table_lines:
        if not re.match(r'^\|\s*[-:\s]+\|', line.strip()):
            data_lines.append(line)
    
    if not data_lines:
        return []
    
    # First line is header
    header = data_lines[0]
    
    # Count columns
    cols = header.count('|') - 1
    
    # Ensure header ends with |
    if not header.rstrip().endswith('|'):
        header = header.rstrip() + ' |'
    
    # Create separator
    separator = '| ' + ' | '.join(['---'] * cols) + ' |'
    
    # Fix data rows - ensure they end with |
    fixed_data = [header, separator]
    for row in data_lines[1:]:
        if not row.rstrip().endswith('|'):
            row = row.rstrip() + ' |'
        fixed_data.append(row)
    
    return fixed_data

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
        
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        fixed_content = fix_table_in_content(content)
        
        if fixed_content != content:
            with open(md_file, 'w', encoding='utf-8') as f:
                f.write(fixed_content)
            fixed_count += 1
            print(f"✓ Fixed: {md_file.relative_to(docs_dir)}")
    
    print(f"\nTotal files fixed: {fixed_count}")

if __name__ == '__main__':
    main()
