#!/usr/bin/env python3
"""
Remove category prefixes from filenames and metadata fields.
This makes it easier to move files between categories.

Example:
- Filename: social-customer-support-merge-feature.md → customer-support-merge-feature.md
- translationKey: "social-customer-support-merge-feature" → "customer-support-merge-feature"
- e-title: "Social - Customer - Support - Merge - Feature" → "Customer - Support - Merge - Feature"
"""

import re
from pathlib import Path
import shutil

# Common category prefixes to remove
CATEGORY_PREFIXES = [
    'social-',
    'ticket-',
    'chat-',
    'call-',
    'auto-',
    'portal-',
    'report-',
    'settings-',
    'security-',
    'pricing-',
    'chatbot-',
    'start-',
]

def extract_frontmatter(content):
    """Extract frontmatter from markdown content."""
    match = re.match(r'^---\n(.*?)\n---\n(.*)$', content, re.DOTALL)
    if match:
        return match.group(1), match.group(2)
    return None, content

def update_frontmatter(frontmatter, old_filename, new_filename):
    """Update translationKey and e-title in frontmatter."""
    lines = frontmatter.split('\n')
    updated_lines = []
    
    old_base = old_filename.replace('.md', '')
    new_base = new_filename.replace('.md', '')
    
    for line in lines:
        if line.startswith('translationKey:'):
            # Update translationKey
            line = f'translationKey: "{new_base}"'
        elif line.startswith('e-title:'):
            # Update e-title - remove category prefix from title
            match = re.match(r'e-title:\s*"(.+)"', line)
            if match:
                old_title = match.group(1)
                # Remove first word if it matches a category prefix pattern
                parts = old_title.split(' - ')
                if len(parts) > 1:
                    # Check if first part is a category name
                    first_part = parts[0].lower()
                    if any(first_part.startswith(prefix.replace('-', '')) for prefix in CATEGORY_PREFIXES):
                        new_title = ' - '.join(parts[1:])
                        line = f'e-title: "{new_title}"'
        
        updated_lines.append(line)
    
    return '\n'.join(updated_lines)

def should_rename(filename):
    """Check if filename should be renamed."""
    for prefix in CATEGORY_PREFIXES:
        if filename.startswith(prefix):
            return True, prefix
    return False, None

def get_new_filename(old_filename, prefix):
    """Generate new filename without category prefix."""
    return old_filename[len(prefix):]

def main():
    """Process all markdown files."""
    docs_dir = Path('content/ja/docs')
    
    if not docs_dir.exists():
        print(f"Directory not found: {docs_dir}")
        return
    
    changes = []
    
    print("Scanning for files with category prefixes...\n")
    
    for md_file in docs_dir.rglob('*.md'):
        if md_file.name == '_index.md':
            continue
        
        filename = md_file.name
        should_change, prefix = should_rename(filename)
        
        if should_change:
            new_filename = get_new_filename(filename, prefix)
            new_path = md_file.parent / new_filename
            
            # Read file content
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extract and update frontmatter
            frontmatter, body = extract_frontmatter(content)
            if frontmatter:
                updated_frontmatter = update_frontmatter(frontmatter, filename, new_filename)
                new_content = f"---\n{updated_frontmatter}\n---\n{body}"
            else:
                new_content = content
            
            changes.append({
                'old_path': md_file,
                'new_path': new_path,
                'old_name': filename,
                'new_name': new_filename,
                'new_content': new_content,
                'category': str(md_file.parent.relative_to(docs_dir))
            })
    
    if not changes:
        print("No files found with category prefixes.")
        return
    
    print(f"Found {len(changes)} files to rename:\n")
    
    # Show preview
    for change in changes[:10]:  # Show first 10
        print(f"  {change['category']}/")
        print(f"    {change['old_name']} → {change['new_name']}")
    
    if len(changes) > 10:
        print(f"  ... and {len(changes) - 10} more files")
    
    print(f"\n{'='*60}")
    response = input(f"Proceed with renaming {len(changes)} files? (yes/no): ")
    
    if response.lower() != 'yes':
        print("Operation cancelled.")
        return
    
    # Perform changes
    renamed_count = 0
    for change in changes:
        try:
            # Write updated content to new file
            with open(change['new_path'], 'w', encoding='utf-8') as f:
                f.write(change['new_content'])
            
            # Remove old file
            change['old_path'].unlink()
            
            renamed_count += 1
            print(f"✓ Renamed: {change['old_name']} → {change['new_name']}")
        except Exception as e:
            print(f"✗ Error renaming {change['old_name']}: {e}")
    
    print(f"\n{'='*60}")
    print(f"✅ Successfully renamed {renamed_count} files")
    print(f"\n⚠️  Note: Please check for any internal links that may need updating.")

if __name__ == '__main__':
    main()
