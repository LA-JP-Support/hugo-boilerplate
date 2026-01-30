#!/usr/bin/env python3
"""
Move additional articles from getting-started to appropriate ticket-system locations.
"""

import shutil
from pathlib import Path
import re

# Define moves: (source_file, destination_dir, new_category)
MOVES = [
    ('social-integration.md', 'ticket-system/social-media', 'ticket-system/social-media'),
    ('contact-browser-extension.md', 'settings', 'settings'),
    ('whatsapp-slack-line.md', 'ticket-system/social-media', 'ticket-system/social-media'),
    ('customize.md', 'settings', 'settings'),
    ('knowledge-base-feature-about.md', 'ticket-system/customer-portal', 'ticket-system/customer-portal'),
    ('phone-call-center-feature.md', 'ticket-system/call-center', 'ticket-system/call-center'),
]

def update_category_in_file(filepath, new_category):
    """Update category field in frontmatter."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Update category in frontmatter
    pattern = r'^category:\s*"[^"]*"'
    replacement = f'category: "{new_category}"'
    new_content = re.sub(pattern, replacement, content, flags=re.MULTILINE)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

def main():
    """Move additional articles."""
    source_dir = Path('content/ja/docs/getting-started')
    base_dir = Path('content/ja/docs')
    
    if not source_dir.exists():
        print(f"Source directory not found: {source_dir}")
        return
    
    print("Moving additional articles from getting-started...\n")
    
    moved_count = 0
    for filename, dest_subdir, new_category in MOVES:
        source_file = source_dir / filename
        dest_dir = base_dir / dest_subdir
        dest_file = dest_dir / filename
        
        if not source_file.exists():
            print(f"⚠️  Source file not found: {filename}")
            continue
        
        # Create destination directory if needed
        dest_dir.mkdir(parents=True, exist_ok=True)
        
        # Move file
        shutil.move(str(source_file), str(dest_file))
        
        # Update category in frontmatter
        update_category_in_file(dest_file, new_category)
        
        moved_count += 1
        print(f"✓ Moved: {filename}")
        print(f"  To: {dest_subdir}/")
        print(f"  Category: {new_category}\n")
    
    print(f"{'='*60}")
    print(f"✅ Successfully moved {moved_count} files")

if __name__ == '__main__':
    main()
