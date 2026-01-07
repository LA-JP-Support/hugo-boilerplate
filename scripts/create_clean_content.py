#!/usr/bin/env python3
"""
Create clean content directory without internal glossary links.
Copies content to a new directory while removing all internal glossary links.

This script is useful for:
1. Creating a baseline for testing HTML-based linkbuilding
2. Comparing MD-based vs HTML-based internal linking approaches
3. Resetting content to a clean state
"""

import re
import shutil
import argparse
from pathlib import Path
from typing import Tuple


def remove_internal_links(content: str) -> Tuple[str, int]:
    """
    Remove internal glossary links and keep only the text.
    Returns: (modified_content, count_of_removals)
    """
    count = 0
    
    # Pattern to match glossary links with optional title attributes:
    # [text](/ja/glossary/.../) 
    # [text](/en/glossary/.../ "description")
    # [**text**](/ja/glossary/.../)
    pattern = r'\[([^\]]+)\]\(/(?:ja|en)/glossary/[^)]+\)'
    
    def replace_link(match):
        nonlocal count
        count += 1
        return match.group(1)  # Return only the link text
    
    modified_content = re.sub(pattern, replace_link, content)
    
    return modified_content, count


def process_file(src_path: Path, dst_path: Path, dry_run: bool = False) -> Tuple[int, bool]:
    """
    Process a single markdown file: remove links and copy to destination.
    Returns: (links_removed, was_modified)
    """
    try:
        content = src_path.read_text(encoding='utf-8')
        modified_content, count = remove_internal_links(content)
        
        if not dry_run:
            dst_path.parent.mkdir(parents=True, exist_ok=True)
            dst_path.write_text(modified_content, encoding='utf-8')
        
        return count, count > 0
        
    except Exception as e:
        print(f"❌ Error processing {src_path}: {e}")
        return 0, False


def copy_non_markdown(src_path: Path, dst_path: Path, dry_run: bool = False):
    """Copy non-markdown files as-is."""
    if not dry_run:
        dst_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src_path, dst_path)


def process_directory(
    src_dir: Path, 
    dst_dir: Path, 
    include_patterns: list = None,
    dry_run: bool = False
) -> dict:
    """
    Process all files in a directory recursively.
    
    Args:
        src_dir: Source directory
        dst_dir: Destination directory
        include_patterns: List of glob patterns to include (default: all)
        dry_run: If True, don't actually write files
    
    Returns:
        Statistics dictionary
    """
    stats = {
        'files_processed': 0,
        'files_modified': 0,
        'links_removed': 0,
        'files_copied': 0,
        'errors': []
    }
    
    # Default patterns
    if include_patterns is None:
        include_patterns = ['**/*.md', '**/*.html', '**/*.json', '**/*.yaml', '**/*.toml']
    
    # Collect all source files
    all_files = set()
    for pattern in include_patterns:
        all_files.update(src_dir.glob(pattern))
    
    # Also include _index.md files and other important files
    all_files.update(src_dir.glob('**/_index.md'))
    
    for src_file in sorted(all_files):
        if not src_file.is_file():
            continue
        
        # Calculate destination path
        rel_path = src_file.relative_to(src_dir)
        dst_file = dst_dir / rel_path
        
        if src_file.suffix == '.md':
            # Process markdown files
            links_removed, was_modified = process_file(src_file, dst_file, dry_run)
            stats['files_processed'] += 1
            stats['links_removed'] += links_removed
            
            if was_modified:
                stats['files_modified'] += 1
                print(f"✅ {rel_path}: {links_removed} links removed")
            else:
                print(f"   {rel_path}: copied (no links)")
        else:
            # Copy other files as-is
            copy_non_markdown(src_file, dst_file, dry_run)
            stats['files_copied'] += 1
    
    return stats


def main():
    parser = argparse.ArgumentParser(
        description="Create clean content directory without internal glossary links",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Create clean version of Japanese blog
  python create_clean_content.py content/ja/blog content-clean/ja/blog
  
  # Create clean version of entire content directory
  python create_clean_content.py content content-clean
  
  # Dry run to see what would be changed
  python create_clean_content.py content/ja/blog content-clean/ja/blog --dry-run
  
  # Process specific content types
  python create_clean_content.py content/ja content-clean/ja --include blog glossary
        """
    )
    
    parser.add_argument("src_dir", type=Path, help="Source content directory")
    parser.add_argument("dst_dir", type=Path, help="Destination directory for clean content")
    parser.add_argument("--dry-run", action="store_true", help="Preview changes without writing files")
    parser.add_argument("--include", nargs='+', default=None,
                       help="Subdirectories to include (e.g., blog glossary)")
    parser.add_argument("--force", action="store_true", help="Overwrite destination if exists")
    
    args = parser.parse_args()
    
    # Validate source
    if not args.src_dir.exists():
        print(f"❌ Error: Source directory not found: {args.src_dir}")
        return 1
    
    # Check destination
    if args.dst_dir.exists() and not args.force:
        print(f"❌ Error: Destination already exists: {args.dst_dir}")
        print("   Use --force to overwrite")
        return 1
    
    # If force and exists, remove first
    if args.dst_dir.exists() and args.force and not args.dry_run:
        print(f"🗑️  Removing existing destination: {args.dst_dir}")
        shutil.rmtree(args.dst_dir)
    
    print(f"\n{'='*60}")
    print(f"Creating clean content (no internal links)")
    print(f"{'='*60}")
    print(f"Source:      {args.src_dir}")
    print(f"Destination: {args.dst_dir}")
    print(f"Mode:        {'DRY RUN' if args.dry_run else 'LIVE'}")
    if args.include:
        print(f"Include:     {', '.join(args.include)}")
    print(f"{'='*60}\n")
    
    total_stats = {
        'files_processed': 0,
        'files_modified': 0,
        'links_removed': 0,
        'files_copied': 0
    }
    
    # Process directories
    if args.include:
        # Process specific subdirectories
        for subdir in args.include:
            src_subdir = args.src_dir / subdir
            dst_subdir = args.dst_dir / subdir
            
            if not src_subdir.exists():
                print(f"⚠️  Skipping (not found): {src_subdir}")
                continue
            
            print(f"\n📁 Processing: {subdir}/")
            print("-" * 40)
            
            stats = process_directory(src_subdir, dst_subdir, dry_run=args.dry_run)
            
            for key in total_stats:
                total_stats[key] += stats.get(key, 0)
    else:
        # Process entire directory
        stats = process_directory(args.src_dir, args.dst_dir, dry_run=args.dry_run)
        total_stats = stats
    
    # Print summary
    print(f"\n{'='*60}")
    print(f"Summary")
    print(f"{'='*60}")
    print(f"  Markdown files processed: {total_stats['files_processed']}")
    print(f"  Files with links removed: {total_stats['files_modified']}")
    print(f"  Total links removed:      {total_stats['links_removed']}")
    print(f"  Other files copied:       {total_stats['files_copied']}")
    print(f"{'='*60}\n")
    
    if args.dry_run:
        print("ℹ️  This was a dry run. No files were actually written.")
        print(f"   Run without --dry-run to create: {args.dst_dir}")
    else:
        print(f"✅ Clean content created at: {args.dst_dir}")
    
    return 0


if __name__ == "__main__":
    exit(main())
