#!/usr/bin/env python3
"""
CSV-based Batch Article Creation (v3)
CSVから未作成記事を取得して一括生成
"""

import os
import csv
import anthropic
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
import time
import argparse
import re
from dotenv import load_dotenv

# .envファイルから環境変数を読み込む
load_dotenv()

# 設定
API_KEY = os.environ.get("ANTHROPIC_API_KEY") or os.environ.get("CLAUDE_API_KEY")
MODEL = "claude-sonnet-4-5-20250929"
OUTPUT_DIR = Path("/Users/TM-MBP1/Documents/GitHub/hugo-boilerplate/content/en/glossary")
DEFAULT_CSV_PATH = Path("/Users/TM-MBP1/Documents/GitHub/hugo-boilerplate/docs/prioritized_keywords.csv")

def needs_article(keyword: str) -> bool:
    """冠詞が必要かを判定"""
    if keyword.endswith('s') or keyword.endswith('es'):
        return False
    uncountable = ['forecasting', 'analysis', 'learning', 'intelligence', 'processing', 
                   'management', 'optimization', 'automation', 'segmentation', 'modeling',
                   'mining', 'clustering', 'classification', 'recognition', 'detection']
    if any(uc in keyword.lower() for uc in uncountable):
        return False
    return True

def get_article(keyword: str) -> str:
    """適切な冠詞を返す"""
    if not needs_article(keyword):
        return ""
    if keyword[0].lower() in 'aeiou':
        return "an "
    return "a "

ARTICLE_PROMPT = """You are an expert technical writer creating a comprehensive glossary article.

TOPIC: {keyword}

CRITICAL REQUIREMENTS:
✓ Language: ENGLISH ONLY
✓ Word count: 2,700-2,900 words (STRICT - do not exceed 3,000 words)
✓ Format: 30% prose in opening sections, 70% structured content (bullets, tables)
✓ Write complete, detailed content - do not summarize or abbreviate
✓ Use proper English grammar including articles (a/an/the) where appropriate

EXACT FRONTMATTER (copy this format):
---
title: "{keyword}"
date: {date}
translationKey: {slug}
description: "SEO-optimized description (150-160 chars)"
keywords:
- keyword1
- keyword2
- keyword3
- keyword4
- keyword5
category: "Application & Use-Cases"
type: glossary
draft: false
---

EXACT STRUCTURE (use these H2 headings, no H3):

## What is {article}{keyword}?
Write 3 full paragraphs (800-1000 words total)

## Core [Specific Technologies/Approaches/Components]
List 5-7 main concepts with **Bold Names** and 2-3 sentence explanations

## How {keyword} Works
Detailed workflow with 6-10 steps and example workflow

## Key Benefits
List 8-10 benefits with **Bold Headers** and explanations

## Common Use Cases
List 8-10 real-world applications with **Bold Headers**

## [Appropriate Comparison Table]
Create comparison table with 5-6 items

## Challenges and Considerations
List 8-10 challenges with **Bold Headers**

## Implementation Best Practices
List 10 best practices with **Bold Headers**

## Advanced Techniques
List 5-6 advanced concepts with **Bold Headers**

## Future Directions
List 5-6 future trends with **Bold Headers**

## References
Include 6-8 authoritative references

IMPORTANT: Keep total length under 3,000 words. Write the COMPLETE article."""

def generate_article(keyword: str, slug: str, date: str, output_dir: Path) -> tuple:
    """1記事を生成"""
    client = anthropic.Anthropic(api_key=API_KEY)
    article = get_article(keyword)
    
    start_time = time.time()
    
    try:
        message = client.messages.create(
            model=MODEL,
            max_tokens=16000,
            temperature=0.1,
            messages=[{
                "role": "user",
                "content": ARTICLE_PROMPT.format(
                    keyword=keyword,
                    slug=slug,
                    date=date,
                    article=article
                )
            }]
        )
        
        content = message.content[0].text
        elapsed = time.time() - start_time
        
        input_tokens = message.usage.input_tokens
        output_tokens = message.usage.output_tokens
        cost = (input_tokens * 3 / 1_000_000) + (output_tokens * 15 / 1_000_000)
        words = len(re.findall(r'\b\w+\b', content))
        
        filepath = output_dir / f"{slug}.md"
        filepath.write_text(content, encoding='utf-8')
        
        print(f"✅ {keyword}: {words} words, ${cost:.4f}, {elapsed:.1f}s")
        
        return (keyword, True, words, output_tokens, cost, elapsed)
        
    except Exception as e:
        print(f"❌ {keyword}: Error - {e}")
        return (keyword, False, 0, 0, 0.0, 0.0)

def get_pending_keywords(csv_path: Path, output_dir: Path, limit: int = None) -> list:
    """未作成記事のキーワードリストを取得"""
    if not csv_path.exists():
        print(f"❌ CSV not found: {csv_path}")
        return []
    
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    
    pending = []
    for row in rows:
        filename = row.get('filename', '')
        keyword = row.get('keyword', '')
        
        if not filename or not keyword:
            continue
        
        filepath = output_dir / filename
        if not filepath.exists():
            slug = filename.replace('.md', '')
            pending.append((keyword, slug))
    
    if limit:
        pending = pending[:limit]
    
    return pending

def batch_generate(keywords: list, output_dir: Path, max_workers: int = 10):
    """複数記事を並列生成"""
    date = "2025-12-21"
    results = []
    total_cost = 0.0
    total_time = 0.0
    total_tokens = 0
    total_words = 0
    
    output_dir.mkdir(parents=True, exist_ok=True)
    
    print(f"\n{'='*70}")
    print(f"🚀 本番バッチ生成開始 (v3)")
    print(f"{'='*70}")
    print(f"記事数: {len(keywords)}")
    print(f"並列数: {max_workers}")
    print(f"出力先: {output_dir}")
    print(f"目標語数: 2,700-2,900語/記事")
    print(f"予想時間: {len(keywords) * 100 / max_workers / 60:.1f}分")
    print(f"予想コスト: ${len(keywords) * 0.088:.2f}")
    print(f"{'='*70}\n")
    
    start_time = time.time()
    completed = 0
    
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {
            executor.submit(generate_article, kw, slug, date, output_dir): (kw, slug)
            for kw, slug in keywords
        }
        
        for future in as_completed(futures):
            keyword, slug = futures[future]
            kw, success, words, tokens, cost, elapsed = future.result()
            
            completed += 1
            
            if success:
                total_cost += cost
                total_time += elapsed
                total_tokens += tokens
                total_words += words
                
                results.append({
                    "keyword": kw,
                    "words": words,
                    "tokens": tokens,
                    "cost": cost,
                    "status": "✅"
                })
            else:
                results.append({
                    "keyword": kw,
                    "words": 0,
                    "tokens": 0,
                    "cost": 0.0,
                    "status": "❌"
                })
            
            # 進捗表示
            if completed % 10 == 0:
                elapsed_total = time.time() - start_time
                remaining = len(keywords) - completed
                eta = (elapsed_total / completed) * remaining / 60
                print(f"\n📊 進捗: {completed}/{len(keywords)} ({completed/len(keywords)*100:.1f}%)")
                print(f"   経過: {elapsed_total/60:.1f}分, 残り: {eta:.1f}分（予測）")
                print(f"   コスト: ${total_cost:.2f}\n")
    
    # サマリー表示
    successful = sum(1 for r in results if r['status'] == '✅')
    
    print(f"\n{'='*70}")
    print(f"📊 完了サマリー")
    print(f"{'='*70}")
    print(f"成功:         {successful}/{len(keywords)} ({successful/len(keywords)*100:.1f}%)")
    print(f"平均語数:     {total_words/successful:.0f}語/記事" if successful > 0 else "")
    print(f"合計トークン: {total_tokens:,}")
    print(f"合計コスト:   ${total_cost:.2f}")
    print(f"総時間:       {(time.time()-start_time)/60:.1f}分")
    print(f"{'='*70}\n")
    
    return results

def main():
    parser = argparse.ArgumentParser(description="CSV-based batch article generation (v3)")
    parser.add_argument('--limit', type=int, help='生成する記事数（デフォルト: 全未作成記事）')
    parser.add_argument('--workers', type=int, default=10, help='並列数（デフォルト: 10）')
    parser.add_argument('--output-dir', help='出力ディレクトリ（デフォルト: content/en/glossary）')
    
    args = parser.parse_args()
    
    output_dir = Path(args.output_dir) if args.output_dir else OUTPUT_DIR
    
    # 未作成記事を取得
    print("📋 未作成記事を取得中...")
    keywords = get_pending_keywords(CSV_PATH, output_dir, limit=args.limit)
    
    if not keywords:
        print("✅ 全ての記事が作成済みです")
        return
    
    print(f"📝 未作成記事: {len(keywords)}件")
    if args.limit:
        print(f"   今回生成: {min(args.limit, len(keywords))}件")
    
    # 確認
    print(f"\n⚠️  これから{len(keywords)}件の記事を生成します")
    print(f"   予想時間: {len(keywords) * 100 / args.workers / 60:.1f}分")
    print(f"   予想コスト: ${len(keywords) * 0.088:.2f}")
    
    response = input("\n続行しますか？ (yes/no): ")
    if response.lower() not in ['yes', 'y']:
        print("❌ キャンセルしました")
        return
    
    # 実行
    results = batch_generate(keywords, output_dir, max_workers=args.workers)
    
    # 失敗した記事をリスト
    failed = [r for r in results if r['status'] == '❌']
    if failed:
        print("\n⚠️  失敗した記事:")
        for r in failed:
            print(f"   - {r['keyword']}")

if __name__ == "__main__":
    main()
