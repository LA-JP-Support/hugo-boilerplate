#!/usr/bin/env python3
"""
Move all LiveAgent articles from getting-started to ticket-system.
"""

import shutil
from pathlib import Path
import re

# Define moves: (source_file, destination_dir, new_category)
MOVES = [
    ('liveagent-about.md', 'ticket-system', 'ticket-system'),
    ('liveagent-first-time.md', 'ticket-system/tickets', 'ticket-system/tickets'),
    ('liveagent-flowhunt-usage.md', 'ticket-system', 'ticket-system'),
    ('liveagent-glossary.md', 'ticket-system', 'ticket-system'),
    ('liveagent-multichannel-handling.md', 'ticket-system', 'ticket-system'),
    ('liveagent-operation-screen.md', 'ticket-system/tickets', 'ticket-system/tickets'),
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
    """Move all LiveAgent articles."""
    source_dir = Path('content/ja/docs/getting-started')
    base_dir = Path('content/ja/docs')
    
    if not source_dir.exists():
        print(f"Source directory not found: {source_dir}")
        return
    
    print("Moving LiveAgent articles from getting-started to ticket-system...\n")
    
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
        print(f"  From: getting-started/")
        print(f"  To:   {dest_subdir}/")
        print(f"  Category updated to: {new_category}\n")
    
    print(f"{'='*60}")
    print(f"✅ Successfully moved {moved_count} files")

if __name__ == '__main__':
    main()
