
import os
import re
from pathlib import Path

def fix_content(content):
    lines = content.split('\n')
    new_lines = []
    in_frontmatter = False
    in_codeblock = False
    
    # Regex to find **text** patterns
    # We look for ** followed by non-newline characters until **, but not empty.
    # We perform this replacement on the line level.
    bold_pattern = re.compile(r'\*\*(?P<text>[^*\n]+?)\*\*')

    for i, line in enumerate(lines):
        # Handle Frontmatter
        if i == 0 and line.strip() == '---':
            in_frontmatter = True
            new_lines.append(line)
            continue
        
        if in_frontmatter:
            if line.strip() == '---':
                in_frontmatter = False
            new_lines.append(line)
            continue

        # Handle Codeblocks
        if line.strip().startswith('```'):
            in_codeblock = not in_codeblock
            new_lines.append(line)
            continue
        
        if in_codeblock:
            new_lines.append(line)
            continue

        # Process normal text
        # We replace **text** with <strong>text</strong>
        # This fixes issues where Hugo/Goldmark fails to render bold due to surrounding characters (e.g. colon, parentheses)
        
        # Function to replace match with strong tag
        def replace_bold(match):
            text = match.group('text')
            return f"<strong>{text}</strong>"

        # Apply replacement
        # We only replace if there is a match.
        # Note: This replaces ALL bold syntax with strong tags in text areas.
        # This is the most robust way to ensure rendering consistency.
        new_line = bold_pattern.sub(replace_bold, line)
        new_lines.append(new_line)

    return '\n'.join(new_lines)

def fix_file(file_path):
    try:
        content = file_path.read_text(encoding='utf-8')
    except UnicodeDecodeError:
        print(f"Skipping binary/unreadable file: {file_path}")
        return 0

    original_content = content
    new_content = fix_content(content)
    
    if new_content != original_content:
        # Calculate approximate number of changes
        diff_count = abs(len(new_content) - len(original_content)) // 5 # rough estimate
        if diff_count > 0:
            file_path.write_text(new_content, encoding='utf-8')
            print(f"Fixed {file_path}")
            return 1 # Count files, not instances
    
    return 0

def main():
    # Allow running on specific file pattern if needed, but defaults to all
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--target', help='Specific file or directory to process', default='content/ja')
    args = parser.parse_args()

    target_path = Path(args.target)
    files_fixed = 0
    
    if target_path.is_file():
        if fix_file(target_path):
            files_fixed += 1
    else:
        for root, _, files in os.walk(target_path):
            for file in files:
                if file.endswith(".md"):
                    file_path = Path(root) / file
                    if fix_file(file_path):
                        files_fixed += 1

    print(f"Total files updated: {files_fixed}")

if __name__ == "__main__":
    main()
