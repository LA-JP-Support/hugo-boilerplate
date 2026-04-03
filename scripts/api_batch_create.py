#!/usr/bin/env python3
"""
Batch Article Creation using Claude API (Test Mode Available)
API自動化記事生成（テストモード対応）
"""

import os
import csv
import re
import anthropic
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
import time
import argparse
from dotenv import load_dotenv

# .envファイルから環境変数を読み込む
load_dotenv()

# 設定
API_KEY = os.environ.get("ANTHROPIC_API_KEY") or os.environ.get("CLAUDE_API_KEY")
MODEL = "claude-sonnet-4-5-20250929" # User specified model
OUTPUT_DIR = Path("/Users/TM-MBP1/Documents/GitHub/smartweb/content/en/glossary")

# 記事生成用プロンプトテンプレート
ARTICLE_PROMPT = """Create a comprehensive glossary article for: {keyword}

CRITICAL REQUIREMENTS:
- Language: ENGLISH ONLY (all content must be in English)
- Word count: 2,000-2,500 words
- Format: 30% prose, 70% structured content (bullets, tables)
- Include frontmatter with these fields:
  - title: "{keyword}"
  - date: {date}
  - translationKey: {slug}
  - description: (SEO-optimized, 150-160 chars)
  - keywords: (5-8 keywords, lowercase)
  - category: "Application & Use-Cases"
  - type: glossary
  - draft: false

STRUCTURE (must include):
1. What is {keyword}? (2-3 paragraphs prose)
2. Core Technologies/Concepts (bullets with descriptions)
3. How It Works (workflow explanation)
4. Key Benefits (bullets)
5. Common Use Cases (5-7 examples)
6. Comparison Table (if applicable)
7. Challenges and Considerations
8. Implementation Best Practices
9. References (markdown links with full URLs)

QUALITY STANDARDS:
- Professional, technical tone
- Specific examples and metrics
- No redundancy
- Clear, scannable structure
- All external links in References section only
- Follow the style of AI-chatbot.md and RAG.md

Write the complete article in English."""

def generate_article(keyword: str, slug: str, date: str, output_dir: Path) -> tuple:
    """1記事を生成"""
    client = anthropic.Anthropic(api_key=API_KEY)
    
    start_time = time.time()
    
    try:
        message = client.messages.create(
            model=MODEL,
            max_tokens=8000,
            temperature=0.2,
            messages=[{
                "role": "user",
                "content": ARTICLE_PROMPT.format(
                    keyword=keyword,
                    slug=slug,
                    date=date
                )
            }]
        )
        
        content = message.content[0].text
        elapsed = time.time() - start_time
        
        # トークン数とコスト計算
        input_tokens = message.usage.input_tokens
        output_tokens = message.usage.output_tokens
        # Sonnet 3.5 pricing (approximate)
        cost = (input_tokens * 3 / 1_000_000) + (output_tokens * 15 / 1_000_000)
        
        # ファイル保存
        filepath = output_dir / f"{slug}.md"
        filepath.write_text(content, encoding='utf-8')
        
        print(f"✅ {keyword}: {output_tokens} tokens, ${cost:.4f}, {elapsed:.1f}s")
        
        return (keyword, True, output_tokens, cost, elapsed)
        
    except Exception as e:
        print(f"❌ {keyword}: Error - {e}")
        return (keyword, False, 0, 0.0, 0.0)

def parse_flowhunt_csv(csv_path: Path) -> list:
    """glossaries_flowhunt.csv形式のファイルをパースする"""
    keywords = []
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            filename = row.get('filename', '').strip()
            flow_input = row.get('flow_input', '')
            
            if not filename or not flow_input:
                continue
                
            # Extract TERM from flow_input
            term_match = re.search(r'TERM:\s*(.+)', flow_input)
            if term_match:
                term = term_match.group(1).strip()
                slug = filename.replace('.md', '')
                keywords.append((term, slug))
    return keywords

def parse_prioritized_csv(csv_path: Path) -> list:
    """prioritized_keywords.csv形式のファイルをパースする"""
    keywords = []
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            term = row.get('keyword', '').strip()
            filename = row.get('filename', '').strip()
            
            if term and filename:
                slug = filename.replace('.md', '')
                keywords.append((term, slug))
    return keywords

def batch_generate(keywords: list, output_dir: Path, max_workers: int = 5, limit: int = 0):
    """複数記事を並列生成"""
    date = "2025-12-21"
    results = []
    total_cost = 0.0
    total_time = 0.0
    total_tokens = 0
    
    # 出力ディレクトリ作成
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # 既存チェック（本番ディレクトリと出力先ディレクトリの両方を確認）
    production_dir = Path("/Users/TM-MBP1/Documents/GitHub/smartweb/content/en/glossary")
    existing_files = {f.stem.lower() for f in output_dir.glob("*.md")}
    if production_dir.exists():
        existing_files.update(f.stem.lower() for f in production_dir.glob("*.md"))
    
    target_keywords = []
    seen_slugs = set()
    
    print(f"Checking {len(keywords)} candidates against {len(existing_files)} existing files")
    
    for term, slug in keywords:
        slug_lower = slug.lower()
        if slug_lower in existing_files:
            print(f"Skipping existing: {term} ({slug})")
            continue
        if slug_lower in seen_slugs:
            print(f"Skipping duplicate in list: {term} ({slug})")
            continue
            
        seen_slugs.add(slug_lower)
        target_keywords.append((term, slug))
    
    if limit > 0:
        target_keywords = target_keywords[:limit]
        
    if not target_keywords:
        print("No new articles to generate.")
        return []

    print(f"\n{'='*70}")
    print(f"🚀 バッチ生成開始")
    print(f"{'='*70}")
    print(f"生成予定数: {len(target_keywords)}")
    print(f"並列数: {max_workers}")
    print(f"出力先: {output_dir}")
    print(f"{'='*70}\n")
    
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {
            executor.submit(generate_article, kw, slug, date, output_dir): (kw, slug)
            for kw, slug in target_keywords
        }
        
        for future in as_completed(futures):
            keyword, slug = futures[future]
            kw, success, tokens, cost, elapsed = future.result()
            
            if success:
                total_cost += cost
                total_time += elapsed
                total_tokens += tokens
                
                results.append({
                    "keyword": kw,
                    "slug": slug,
                    "tokens": tokens,
                    "cost": f"${cost:.4f}",
                    "time": f"{elapsed:.1f}s",
                    "status": "✅"
                })
            else:
                results.append({
                    "keyword": kw,
                    "slug": slug,
                    "tokens": 0,
                    "cost": "$0.0000",
                    "time": "0.0s",
                    "status": "❌"
                })
    
    # サマリー表示
    successful = sum(1 for r in results if r['status'] == '✅')
    
    print(f"\n{'='*70}")
    print(f"📊 完了サマリー")
    print(f"{'='*70}")
    print(f"成功:         {successful}/{len(target_keywords)}")
    print(f"合計トークン: {total_tokens:,}")
    print(f"合計コスト:   ${total_cost:.4f}")
    if len(target_keywords) > 0:
        print(f"平均時間:     {total_time/len(target_keywords):.1f}秒/記事")
    print(f"総時間:       {total_time/60:.1f}分")
    print(f"{'='*70}\n")
    
    return results

def main():
    parser = argparse.ArgumentParser(description="Claude API記事自動生成")
    parser.add_argument('--test', action='store_true', help='テストモード（別ディレクトリに出力）')
    parser.add_argument('--csv', help='キーワードCSVファイルパス')
    parser.add_argument('--keywords', nargs='+', help='キーワードリスト（直接指定）')
    parser.add_argument('--workers', type=int, default=3, help='並列数（デフォルト: 3）')
    parser.add_argument('--limit', type=int, default=0, help='生成する最大記事数（0は無制限）')
    parser.add_argument('--output-dir', help='出力ディレクトリ指定')
    
    args = parser.parse_args()
    
    # ディレクトリ設定
    if args.output_dir:
        output_dir = Path(args.output_dir)
    elif args.test:
        output_dir = Path("/Users/TM-MBP1/Documents/GitHub/smartweb/content/en/glossary-api-test")
    else:
        output_dir = OUTPUT_DIR
        
    print(f"Output Directory: {output_dir}")
    
    # キーワード読み込み
    keywords = []
    if args.csv:
        csv_path = Path(args.csv)
        if not csv_path.exists():
            print(f"Error: CSV file not found: {csv_path}")
            return
            
        if "flowhunt" in csv_path.name:
            keywords = parse_flowhunt_csv(csv_path)
        else:
            keywords = parse_prioritized_csv(csv_path)
        print(f"Loaded {len(keywords)} keywords from {csv_path.name}")
        
    elif args.keywords:
        keywords = [(kw, kw.replace(' ', '-')) for kw in args.keywords]
    else:
        # デフォルト（テスト用）
        keywords = [
            ("Customer Segmentation", "Customer-Segmentation"),
            ("Sentiment Analysis", "Sentiment-Analysis"),
        ]
    
    # 実行
    results = batch_generate(keywords, output_dir, max_workers=args.workers, limit=args.limit)
    
    # 結果詳細
    if results:
        print("\n📋 詳細結果:")
        for r in results:
            print(f"{r['status']} {r['keyword']:35s} {r['tokens']:>6} tokens  {r['cost']:>10s}  {r['time']:>8s}")

if __name__ == "__main__":
    main()
