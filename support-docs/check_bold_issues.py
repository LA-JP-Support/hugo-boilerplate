#!/usr/bin/env python3
"""
Check for bold markdown issues with Japanese punctuation.
Finds patterns where **text）** or similar is not followed by &#8203;
"""

import os
import re
from pathlib import Path

def find_bold_issues(content, filepath):
    """Find bold patterns ending with Japanese punctuation without zero-width space."""
    issues = []
    
    # Pattern: **...Japanese_punctuation** followed by non-entity character
    # Japanese punctuation: ）」】》。、
    pattern = r'\*\*[^*]+[）」】》。、]\*\*(?!&#8203;)(?!$)(?!\s*$)(?!\s*\|)(?!\n)'
    
    lines = content.split('\n')
    for line_num, line in enumerate(lines, 1):
        matches = re.finditer(pattern, line)
        for match in matches:
            # Skip if it's at end of line or followed by space/newline
            after_match = line[match.end():] if match.end() < len(line) else ''
            if after_match and not after_match.startswith((' ', '\t', '|', '\n', '')):
                issues.append({
                    'file': filepath,
                    'line': line_num,
                    'match': match.group(),
                    'context': line.strip()[:100]
                })
    
    return issues

def scan_directory(base_path):
    """Scan all markdown files in directory."""
    all_issues = []
    
    for root, dirs, files in os.walk(base_path):
        for file in files:
            if file.endswith('.md'):
                filepath = os.path.join(root, file)
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()
                    issues = find_bold_issues(content, filepath)
                    all_issues.extend(issues)
                except Exception as e:
                    print(f"Error reading {filepath}: {e}")
    
    return all_issues

if __name__ == '__main__':
    base_path = '/Users/TM-MBP1/Documents/GitHub/hugo-boilerplate/support-docs/content/ja/docs'
    
    print(f"Scanning: {base_path}\n")
    issues = scan_directory(base_path)
    
    if issues:
        print(f"Found {len(issues)} potential issues:\n")
        for issue in issues:
            rel_path = issue['file'].replace(base_path + '/', '')
            print(f"File: {rel_path}")
            print(f"Line {issue['line']}: {issue['match']}")
            print(f"Context: {issue['context']}")
            print("-" * 60)
    else:
        print("No issues found!")
