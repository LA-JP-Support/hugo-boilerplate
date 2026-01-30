#!/usr/bin/env python3
"""
Improve heading structure in markdown files using Claude API.
Analyzes content and suggests/implements better heading organization.
"""

import os
import re
from pathlib import Path
from anthropic import Anthropic
from dotenv import load_dotenv

# Load environment variables
load_dotenv('../.env')

# Try both possible API key names
api_key = os.environ.get("ANTHROPIC_API_KEY") or os.environ.get("CLAUDE_API_KEY")
if not api_key:
    raise ValueError("API key not found. Please set ANTHROPIC_API_KEY or CLAUDE_API_KEY in .env file")

client = Anthropic(api_key=api_key)

def extract_frontmatter_and_content(filepath):
    """Extract frontmatter and content from markdown file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    match = re.match(r'^---\n(.*?)\n---\n(.*)$', content, re.DOTALL)
    if match:
        return match.group(1), match.group(2)
    return None, content

def analyze_and_improve_headings(title, content):
    """Use Claude to analyze content and suggest improved heading structure."""
    
    prompt = f"""記事のタイトル: {title}

以下の日本語サポート記事の内容を分析して、適切な見出し構造（h2 ##、h3 ###）を提案してください。

現在の内容:
{content[:3000]}

要件:
1. 記事の内容を論理的なセクションに分割
2. h2（##）で主要なセクションを作成
3. h3（###）で詳細なサブセクションを作成
4. 既存の見出しがある場合は改善
5. 見出しは簡潔で分かりやすく
6. Table of Contentsとして機能するように構造化

元の内容をそのまま保持し、見出しのみを追加・改善したMarkdownを出力してください。
フロントマターは含めず、本文のみを出力してください。"""

    try:
        message = client.messages.create(
            model="claude-3-5-haiku-20241022",
            max_tokens=4000,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        
        return message.content[0].text
    except Exception as e:
        print(f"Error calling Claude API: {e}")
        return None

def process_file(filepath, dry_run=True):
    """Process a single markdown file."""
    frontmatter, content = extract_frontmatter_and_content(filepath)
    
    if not frontmatter:
        print(f"⚠️  No frontmatter found: {filepath}")
        return False
    
    # Extract title from frontmatter
    title_match = re.search(r'^title:\s*"([^"]+)"', frontmatter, re.MULTILINE)
    title = title_match.group(1) if title_match else "Unknown"
    
    print(f"Processing: {title}")
    
    # Analyze and improve headings
    improved_content = analyze_and_improve_headings(title, content)
    
    if not improved_content:
        print(f"  ✗ Failed to improve")
        return False
    
    if dry_run:
        print(f"  ✓ Analysis complete (dry run)")
        return True
    
    # Write back to file
    new_content = f"---\n{frontmatter}\n---\n{improved_content}"
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"  ✓ Updated")
    return True

def main():
    """Process all markdown files."""
    docs_dir = Path('content/ja/docs')
    
    if not docs_dir.exists():
        print(f"Directory not found: {docs_dir}")
        return
    
    # Get all markdown files
    md_files = [f for f in docs_dir.rglob('*.md') if f.name != '_index.md']
    
    print(f"Found {len(md_files)} markdown files\n")
    print("=" * 60)
    print("DRY RUN MODE - Testing on first 3 files")
    print("=" * 60)
    
    # Test on first 3 files
    success_count = 0
    for md_file in md_files[:3]:
        rel_path = md_file.relative_to(docs_dir)
        print(f"\n📄 {rel_path}")
        if process_file(md_file, dry_run=True):
            success_count += 1
    
    print(f"\n{'='*60}")
    print(f"Test Results: {success_count}/3 successful")
    print(f"{'='*60}")
    
    if success_count == 3:
        response = input(f"\nTest successful! Process all {len(md_files)} files? (yes/no): ")
        if response.lower() == 'yes':
            print("\nProcessing all files...")
            total_success = 0
            for i, md_file in enumerate(md_files, 1):
                print(f"\n[{i}/{len(md_files)}] {md_file.relative_to(docs_dir)}")
                if process_file(md_file, dry_run=False):
                    total_success += 1
            
            print(f"\n{'='*60}")
            print(f"✅ Completed: {total_success}/{len(md_files)} files updated")
            print(f"{'='*60}")
        else:
            print("Operation cancelled.")
    else:
        print("\n⚠️  Test failed. Please check the errors above.")

if __name__ == '__main__':
    main()
