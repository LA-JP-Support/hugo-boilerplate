#!/usr/bin/env python3
"""
Remove all tooltip shortcodes from markdown files
Removes {{< tooltip ... >}}...{{< /tooltip >}} and keeps only the inner text
"""

import re
import argparse
from pathlib import Path

def remove_tooltips_from_content(content: str) -> tuple[str, int]:
    """
    Remove all tooltip shortcodes and keep only the inner text
    Returns: (modified_content, count_of_removals)
    """
    count = 0
    
    # Pattern to match: {{< tooltip text="..." >}}[link text](url){{< /tooltip >}}
    # or: {{< tooltip text="..." >}}plain text{{< /tooltip >}}
    pattern = r'\{\{<\s*tooltip\s+text="[^"]*"\s*>\}\}(.*?)\{\{<\s*/tooltip\s*>\}\}'
    
    def replace_tooltip(match):
        nonlocal count
        count += 1
        return match.group(1)  # Return only the inner content
    
    modified_content = re.sub(pattern, replace_tooltip, content, flags=re.DOTALL)
    
    return modified_content, count

def process_file(filepath: Path, dry_run: bool = False) -> int:
    """Process a single markdown file"""
    try:
        content = filepath.read_text(encoding='utf-8')
        modified_content, count = remove_tooltips_from_content(content)
        
        if count > 0:
            if not dry_run:
                filepath.write_text(modified_content, encoding='utf-8')
            print(f"✅ {filepath.name}: {count} tooltips removed")
            return count
        else:
            print(f"  {filepath.name}: No tooltips found")
            return 0
            
    except Exception as e:
        print(f"❌ Error processing {filepath.name}: {e}")
        return 0

def main():
    parser = argparse.ArgumentParser(description="Remove all tooltip shortcodes from markdown files")
    parser.add_argument("content_dir", type=Path, help="Directory containing markdown files")
    parser.add_argument("--dry-run", action="store_true", help="Preview changes without modifying files")
    
    args = parser.parse_args()
    
    if not args.content_dir.exists():
        print(f"Error: Directory not found: {args.content_dir}")
        return
    
    print(f"\n{'='*60}")
    print(f"Removing tooltips from: {args.content_dir}")
    print(f"Mode: {'DRY RUN' if args.dry_run else 'LIVE'}")
    print(f"{'='*60}\n")
    
    total_count = 0
    files_modified = 0
    
    for md_file in sorted(args.content_dir.glob("*.md")):
        if md_file.name == "_index.md":
            continue
        
        count = process_file(md_file, dry_run=args.dry_run)
        if count > 0:
            files_modified += 1
            total_count += count
    
    print(f"\n{'='*60}")
    print(f"Summary:")
    print(f"  Files modified: {files_modified}")
    print(f"  Total tooltips removed: {total_count}")
    print(f"{'='*60}\n")

if __name__ == "__main__":
    main()
