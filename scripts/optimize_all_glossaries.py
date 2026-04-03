#!/usr/bin/env python3
"""
Optimize All Glossary Articles
全ての用語集記事を最適化フォーマットに変換

Usage:
    python scripts/optimize_all_glossaries.py [--batch 10] [--start-from filename.md]
"""

import os
import sys
import time
import anthropic
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

GLOSSARY_EN = Path("/Users/TM-MBP1/Documents/GitHub/smartweb/content/en/glossary")
OPTIMIZATION_PROMPT = """You are optimizing a glossary article for content marketing. Transform this article following these guidelines:

**Target Length:** 2,600-2,800 words
**Reading Time:** 13-14 minutes
**Format Balance:** 30% prose, 70% structured content (bullet points, sub-sections)

**Structure Requirements:**

REQUIRED SECTIONS:
1. **What is [Term]?** - Core definition (2-3 paragraphs of prose)
2. **Core concepts/Key Features** - Main features (use bullet points with 1-2 sentence descriptions)
3. **References** - All external links consolidated here

OPTIONAL SECTIONS (include based on content):
- How It Works / Technical Architecture
- Benefits / Advantages  
- Use Cases / Examples
- Best Practices
- Challenges / Considerations
- FAQ

**Formatting Rules:**

✓ Use **bold subheadings** for scannability
✓ Bullet points for features, benefits, lists
✓ Short paragraphs (3-4 sentences) for prose sections
✓ Remove ALL inline external links - move to References section
✓ Keep internal links intact (they will be added by another process)
✓ Use clear, concise language
✓ Avoid redundancy and over-explanation

**Content Optimization:**
- Cut redundant explanations by 25-30%
- Combine related concepts
- Use specific examples where relevant
- Maintain technical accuracy
- Keep SEO keywords natural

**References Section Format:**
```markdown
## References

- [Title - Source](URL)
- [Title - Source](URL)
```

Now optimize this article:

---
{article_content}
---

Return ONLY the optimized article with frontmatter intact. Do not add explanations or meta-commentary.
"""

def get_all_markdown_files():
    """全てのMarkdownファイルを取得"""
    files = [f for f in GLOSSARY_EN.glob("*.md") if f.name != "_index.md"]
    # 既に最適化済みのファイルを除外
    files = [f for f in files if not f.stem.endswith("-OLD") and not f.stem.endswith("-OPTIMIZED")]
    return sorted(files)

def read_file(filepath):
    """ファイル内容を読み込み"""
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(filepath, content):
    """ファイルに書き込み"""
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def optimize_article(client, filepath, dry_run=False):
    """記事を最適化"""
    content = read_file(filepath)
    
    # 既に最適化済みかチェック（簡易的）
    word_count = len(content.split())
    if 2400 <= word_count <= 3000:
        print(f"  ⏭️  Already optimized ({word_count} words)")
        return "skipped"
    
    if dry_run:
        print(f"  🔍 Would optimize ({word_count} words)")
        return "dry_run"
    
    try:
        # Claude APIで最適化
        message = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=16000,
            messages=[{
                "role": "user",
                "content": OPTIMIZATION_PROMPT.format(article_content=content)
            }]
        )
        
        optimized_content = message.content[0].text
        
        # 元ファイルをバックアップ
        backup_path = filepath.parent / f"{filepath.stem}-OLD{filepath.suffix}"
        if not backup_path.exists():
            write_file(backup_path, content)
        
        # 最適化版を保存
        write_file(filepath, optimized_content)
        
        new_word_count = len(optimized_content.split())
        print(f"  ✓ Optimized: {word_count} → {new_word_count} words")
        return "success"
        
    except Exception as e:
        print(f"  ❌ Error: {str(e)}")
        return "error"

def main():
    # コマンドライン引数の処理
    batch_size = 10
    start_from = None
    dry_run = "--dry-run" in sys.argv
    
    for i, arg in enumerate(sys.argv):
        if arg == "--batch" and i + 1 < len(sys.argv):
            batch_size = int(sys.argv[i + 1])
        elif arg == "--start-from" and i + 1 < len(sys.argv):
            start_from = sys.argv[i + 1]
    
    # Claude APIクライアント
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key and not dry_run:
        print("❌ Error: ANTHROPIC_API_KEY not found in environment")
        return
    
    client = None if dry_run else anthropic.Anthropic(api_key=api_key)
    
    print("=" * 60)
    print("Glossary Article Optimizer")
    print("=" * 60)
    
    if dry_run:
        print("\n🔍 DRY RUN MODE - No files will be modified\n")
    
    # ファイルリスト取得
    files = get_all_markdown_files()
    
    # 開始位置を設定
    if start_from:
        try:
            start_idx = next(i for i, f in enumerate(files) if f.name == start_from)
            files = files[start_idx:]
            print(f"\nStarting from: {start_from}\n")
        except StopIteration:
            print(f"❌ File not found: {start_from}")
            return
    
    # バッチ処理
    files_to_process = files[:batch_size]
    
    print(f"Processing {len(files_to_process)} of {len(files)} files\n")
    
    stats = {"success": 0, "skipped": 0, "error": 0, "dry_run": 0}
    
    for i, filepath in enumerate(files_to_process, 1):
        print(f"[{i}/{len(files_to_process)}] {filepath.name}")
        
        result = optimize_article(client, filepath, dry_run)
        stats[result] += 1
        
        # レート制限対策（APIリクエスト間に待機）
        if result == "success" and i < len(files_to_process):
            time.sleep(2)
    
    # サマリー表示
    print("\n" + "=" * 60)
    print("Summary:")
    print(f"  ✓ Optimized: {stats['success']}")
    print(f"  ⏭️  Skipped: {stats['skipped']}")
    print(f"  ❌ Errors: {stats['error']}")
    if dry_run:
        print(f"  🔍 Would process: {stats['dry_run']}")
    print("=" * 60)
    
    # 次のバッチの情報
    remaining = len(files) - len(files_to_process)
    if remaining > 0:
        next_file = files[len(files_to_process)].name
        print(f"\n📝 {remaining} files remaining")
        print(f"To continue, run:")
        print(f"  python scripts/optimize_all_glossaries.py --start-from {next_file}")
    else:
        print("\n✅ All files processed!")

if __name__ == "__main__":
    main()
