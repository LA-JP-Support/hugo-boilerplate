#!/usr/bin/env python3
"""
Fix YAML front matter quote issues in support content files.

This script fixes description fields that contain unescaped double quotes
which cause YAML parsing errors in Hugo.

Usage:
    python3 scripts/fix_support_yaml_quotes.py
"""

import os
import re
from pathlib import Path

def fix_yaml_quotes(file_path):
    """Fix YAML quote issues in a single file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split into front matter and body
    parts = content.split('---', 2)
    if len(parts) < 3:
        return False  # No front matter
    
    front_matter = parts[1]
    body = parts[2]
    
    # Pattern to match description lines with problematic quotes
    # Matches: description: "text with "quoted" text"
    pattern = r'(description:\s*)"([^"]*"[^"]*"[^"]*)"'
    
    modified = False
    
    # Check if the pattern exists
    if re.search(pattern, front_matter):
        # Replace curly quotes with straight quotes first
        front_matter = front_matter.replace('"', '"').replace('"', '"')
        
        # Find description line
        desc_pattern = r'description:\s*"(.+)"'
        match = re.search(desc_pattern, front_matter)
        
        if match:
            original_desc = match.group(1)
            # Escape internal double quotes
            fixed_desc = original_desc.replace('"', '\\"')
            
            # Replace in front matter
            front_matter = re.sub(
                desc_pattern,
                f'description: "{fixed_desc}"',
                front_matter
            )
            modified = True
    
    if modified:
        # Reconstruct the file
        new_content = '---' + front_matter + '---' + body
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        return True
    
    return False

def main():
    """Process all markdown files in support directory."""
    support_dir = Path('content/ja/support')
    
    if not support_dir.exists():
        print(f"Error: {support_dir} does not exist")
        return
    
    fixed_count = 0
    processed_count = 0
    
    # Find all .md files
    for md_file in support_dir.rglob('*.md'):
        processed_count += 1
        
        try:
            if fix_yaml_quotes(md_file):
                fixed_count += 1
                print(f"✓ Fixed: {md_file.relative_to('content/ja/support')}")
        except Exception as e:
            print(f"✗ Error processing {md_file}: {e}")
    
    print(f"\n{'='*60}")
    print(f"Processed: {processed_count} files")
    print(f"Fixed: {fixed_count} files")
    print(f"{'='*60}")

if __name__ == '__main__':
    main()
