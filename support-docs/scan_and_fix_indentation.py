#!/usr/bin/env python3
"""
Scan all markdown files and fix incorrect indentation that causes text to be treated as code blocks.
"""

import re
from pathlib import Path

def has_indentation_issues(content):
    """Check if file has indentation issues."""
    lines = content.split('\n')
    
    # Look for lines with tabs or 4+ spaces at the start (after frontmatter)
    in_frontmatter = False
    in_code_block = False
    frontmatter_count = 0
    
    for line in lines:
        # Track frontmatter
        if line.strip() == '---':
            frontmatter_count += 1
            if frontmatter_count == 2:
                in_frontmatter = False
            else:
                in_frontmatter = True
            continue
        
        if in_frontmatter:
            continue
        
        # Track code blocks
        if line.strip().startswith('```'):
            in_code_block = not in_code_block
            continue
        
        if in_code_block:
            continue
        
        # Check for problematic indentation
        if line.startswith('\t') or (line.startswith('    ') and not line.strip().startswith('-')):
            # This line has indentation that might cause issues
            return True
    
    return False

def fix_indentation(content):
    """Fix indentation issues in content."""
    lines = content.split('\n')
    fixed_lines = []
    
    in_frontmatter = False
    in_code_block = False
    frontmatter_count = 0
    
    for line in lines:
        # Track frontmatter
        if line.strip() == '---':
            frontmatter_count += 1
            if frontmatter_count == 2:
                in_frontmatter = False
            else:
                in_frontmatter = True
            fixed_lines.append(line)
            continue
        
        if in_frontmatter:
            fixed_lines.append(line)
            continue
        
        # Track code blocks
        if line.strip().startswith('```'):
            in_code_block = not in_code_block
            fixed_lines.append(line)
            continue
        
        if in_code_block:
            fixed_lines.append(line)
            continue
        
        # Fix problematic indentation
        if line.startswith('\t'):
            # Remove all leading tabs
            line = line.lstrip('\t')
        elif line.startswith('    '):
            # Check if it's a list continuation (should keep some indent)
            # Otherwise remove the indent
            if not any(prev_line.strip().startswith(('-', '*', '1.', '2.', '3.', '4.', '5.', '6.', '7.', '8.', '9.')) 
                      for prev_line in fixed_lines[-3:] if prev_line.strip()):
                line = line.lstrip()
        
        fixed_lines.append(line)
    
    return '\n'.join(fixed_lines)

def main():
    """Process all markdown files."""
    docs_dir = Path('content/ja/docs')
    
    if not docs_dir.exists():
        print(f"Directory not found: {docs_dir}")
        return
    
    issues_found = []
    
    # First scan for issues
    print("Scanning for indentation issues...")
    for md_file in docs_dir.rglob('*.md'):
        if md_file.name == '_index.md':
            continue
        
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if has_indentation_issues(content):
            issues_found.append(md_file)
    
    print(f"\nFound {len(issues_found)} files with indentation issues\n")
    
    # Fix all issues
    fixed_count = 0
    for md_file in issues_found:
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        fixed_content = fix_indentation(content)
        
        if fixed_content != content:
            with open(md_file, 'w', encoding='utf-8') as f:
                f.write(fixed_content)
            fixed_count += 1
            print(f"✓ Fixed: {md_file.relative_to(docs_dir)}")
    
    print(f"\nTotal files fixed: {fixed_count}")

if __name__ == '__main__':
    main()
