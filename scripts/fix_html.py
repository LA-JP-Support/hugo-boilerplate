#!/usr/bin/env python3
"""
Fix HTML file that was corrupted by Apple's text editor.
Extracts actual HTML content from <p> tags.
"""

import re
import html as html_module
import sys

def fix_html_file(input_file, output_file):
    """Extract and clean HTML from Apple-formatted file."""
    
    # Read the corrupted file
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract body content
    body_match = re.search(r'<body>(.*?)</body>', content, re.DOTALL)
    if not body_match:
        print("Error: Could not find <body> tag")
        return False
    
    body_content = body_match.group(1)
    
    # Extract all <p> tag contents
    p_tags = re.findall(r'<p class="p[12]">(.*?)</p>', body_content, re.DOTALL)
    
    # Decode and clean each line
    decoded_lines = []
    for line in p_tags:
        # Skip empty lines and <br/> tags
        if not line.strip() or line.strip() == '<br/>':
            continue
        
        # Decode HTML entities
        decoded = html_module.unescape(line)
        
        # Remove Apple-specific spans
        decoded = re.sub(r'<span class="Apple-converted-space">\s*</span>', ' ', decoded)
        decoded = re.sub(r'<span class="Apple-tab-span">.*?</span>', '', decoded)
        
        decoded_lines.append(decoded.strip())
    
    # Join lines
    result = '\n'.join(decoded_lines)
    
    # Write cleaned HTML
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(result)
    
    print(f"✓ Fixed HTML saved to: {output_file}")
    print(f"  Original lines: {len(p_tags)}")
    print(f"  Cleaned lines: {len(decoded_lines)}")
    
    return True

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python fix_html.py <input_file> <output_file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    if fix_html_file(input_file, output_file):
        sys.exit(0)
    else:
        sys.exit(1)
