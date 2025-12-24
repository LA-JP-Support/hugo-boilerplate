import os
import re

TARGET_LINK_PART = "Risk-Assessment--Customer-"

def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Pattern to match: [text](/.../Risk-Assessment--Customer-/ "tooltip")
    # We want to keep 'text' and remove the link.
    
    # Regex: \[([^\]]+)\]\([^\)]*Risk-Assessment--Customer-[^\)]*\)
    pattern = r'\[([^\]]+)\]\([^\)]*Risk-Assessment--Customer-[^\)]*\)'
    
    new_content = re.sub(pattern, r'\1', content)
    
    if new_content != content:
        print(f"Fixed: {filepath}")
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

def main():
    root_dir = "content"
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".md"):
                fix_file(os.path.join(root, file))

if __name__ == "__main__":
    main()
