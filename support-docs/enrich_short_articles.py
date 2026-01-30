#!/usr/bin/env python3
"""
Enrich short articles by fetching content from reference sites and using Claude API.
Primary reference: SmartWeb renewal site
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

# Reference sites in priority order
REFERENCE_SITES = [
    "https://main.d1jtfhinlastnr.amplifyapp.com/ja/",  # SmartWeb renewal (primary)
    "https://www.liveagent.com/",
    "https://www.flowhunt.io/",
    "https://support.liveagent.com/"
]

def extract_frontmatter_and_content(filepath):
    """Extract frontmatter and content from markdown file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    match = re.match(r'^---\n(.*?)\n---\n(.*)$', content, re.DOTALL)
    if match:
        return match.group(1), match.group(2)
    return None, content

def count_japanese_chars(text):
    """Count Japanese characters (excluding whitespace and markdown syntax)."""
    # Remove markdown syntax
    text = re.sub(r'#+\s+', '', text)
    text = re.sub(r'\*\*|__', '', text)
    text = re.sub(r'\*|_', '', text)
    text = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', text)
    
    # Count only Japanese characters
    japanese_chars = re.findall(r'[ぁ-んァ-ヶー一-龯]', text)
    return len(japanese_chars)

def enrich_content(title, keywords, current_content, description):
    """Use Claude to enrich short article content."""
    
    prompt = f"""あなたはSmartWebのサポートドキュメントの執筆者です。

記事タイトル: {title}
キーワード: {', '.join(keywords)}
説明: {description}

現在の内容:
{current_content}

参照サイト（最優先）: {REFERENCE_SITES[0]}

タスク:
1. 現在の内容が短すぎる場合、以下を参考に内容を充実させてください：
   - SmartWebリニューアルサイト（{REFERENCE_SITES[0]}）の情報を最優先で参照
   - LiveAgent、FlowHuntの機能説明
   - 実用的な使い方や利点

2. 以下の要件を満たしてください：
   - 既存の見出し構造（h2 ##、h3 ###）を保持
   - 各見出しの下に具体的な内容を追加（2-3文程度）
   - 日本語で400-800文字程度に拡充
   - 箇条書きや具体例を含める
   - 専門用語は分かりやすく説明

3. 以下は変更しないでください：
   - フロントマター
   - 既存の見出し構造
   - 記事の主旨

拡充した本文のみを出力してください（フロントマターは含めない）。"""

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
        print(f"  ✗ Error calling Claude API: {e}")
        return None

def process_file(filepath, min_chars=200, dry_run=True):
    """Process a single markdown file if it's too short."""
    frontmatter, content = extract_frontmatter_and_content(filepath)
    
    if not frontmatter:
        return False, "No frontmatter"
    
    # Extract metadata from frontmatter
    title_match = re.search(r'^title:\s*"([^"]+)"', frontmatter, re.MULTILINE)
    title = title_match.group(1) if title_match else "Unknown"
    
    keywords_match = re.search(r'^keywords:\s*\[([^\]]+)\]', frontmatter, re.MULTILINE)
    keywords = []
    if keywords_match:
        keywords = [k.strip().strip('"') for k in keywords_match.group(1).split(',')]
    
    description_match = re.search(r'^description:\s*"([^"]+)"', frontmatter, re.MULTILINE)
    description = description_match.group(1) if description_match else ""
    
    # Count characters
    char_count = count_japanese_chars(content)
    
    if char_count >= min_chars:
        return False, f"Sufficient length ({char_count} chars)"
    
    print(f"  📏 Current: {char_count} chars (needs enrichment)")
    
    # Enrich content
    enriched_content = enrich_content(title, keywords, content, description)
    
    if not enriched_content:
        return False, "Failed to enrich"
    
    new_char_count = count_japanese_chars(enriched_content)
    print(f"  ✓ Enriched: {char_count} → {new_char_count} chars")
    
    if dry_run:
        return True, f"Would enrich ({char_count} → {new_char_count} chars)"
    
    # Write back to file
    new_content = f"---\n{frontmatter}\n---\n{enriched_content}"
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    return True, f"Enriched ({char_count} → {new_char_count} chars)"

def main():
    """Process all markdown files."""
    docs_dir = Path('content/ja/docs')
    
    if not docs_dir.exists():
        print(f"Directory not found: {docs_dir}")
        return
    
    # Get all markdown files
    md_files = [f for f in docs_dir.rglob('*.md') if f.name != '_index.md']
    
    print(f"Found {len(md_files)} markdown files")
    print(f"Scanning for short articles (< 200 Japanese characters)...\n")
    
    # Find short articles
    short_articles = []
    for md_file in md_files:
        frontmatter, content = extract_frontmatter_and_content(md_file)
        if frontmatter:
            char_count = count_japanese_chars(content)
            if char_count < 200:
                short_articles.append((md_file, char_count))
    
    short_articles.sort(key=lambda x: x[1])
    
    print(f"Found {len(short_articles)} short articles\n")
    print("=" * 60)
    print("DRY RUN MODE - Testing on first 3 articles")
    print("=" * 60)
    
    # Test on first 3 short articles
    success_count = 0
    for md_file, char_count in short_articles[:3]:
        rel_path = md_file.relative_to(docs_dir)
        print(f"\n📄 {rel_path}")
        success, message = process_file(md_file, dry_run=True)
        print(f"  {message}")
        if success:
            success_count += 1
    
    print(f"\n{'='*60}")
    print(f"Test Results: {success_count}/3 successful")
    print(f"Total short articles to process: {len(short_articles)}")
    print(f"{'='*60}")
    
    if success_count >= 2:
        response = input(f"\nProcess all {len(short_articles)} short articles? (yes/no): ")
        if response.lower() == 'yes':
            print("\nProcessing all short articles...")
            total_success = 0
            for i, (md_file, char_count) in enumerate(short_articles, 1):
                print(f"\n[{i}/{len(short_articles)}] {md_file.relative_to(docs_dir)}")
                success, message = process_file(md_file, dry_run=False)
                print(f"  {message}")
                if success:
                    total_success += 1
            
            print(f"\n{'='*60}")
            print(f"✅ Completed: {total_success}/{len(short_articles)} articles enriched")
            print(f"{'='*60}")
        else:
            print("Operation cancelled.")
    else:
        print("\n⚠️  Test failed. Please check the errors above.")

if __name__ == '__main__':
    main()
