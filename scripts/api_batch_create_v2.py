#!/usr/bin/env python3
"""
Improved Batch Article Creation using Claude API
改善版API自動化記事生成
"""

import os
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
MODEL = "claude-sonnet-4-20250514"
OUTPUT_DIR = Path("/Users/TM-MBP1/Documents/GitHub/hugo-boilerplate/content/en/glossary")

# 改善版プロンプト
ARTICLE_PROMPT = """You are an expert technical writer creating a comprehensive glossary article.

TOPIC: {keyword}

CRITICAL REQUIREMENTS:
✓ Language: ENGLISH ONLY
✓ Word count: 2,700-2,900 words (STRICT - do not stop early)
✓ Format: 30% prose in opening sections, 70% structured content (bullets, tables)
✓ Write complete, detailed content - do not summarize or abbreviate

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

EXACT STRUCTURE (use these H2 headings, no H3 unless within lists):

## What is {keyword}?
Write 3 full paragraphs (800-1000 words total):
- Paragraph 1: Comprehensive definition and core concept
- Paragraph 2: How it differs from traditional approaches, transformation it enables
- Paragraph 3: Business impact, measurable outcomes, real-world significance

## Core [Specific Technologies/Approaches/Components for {keyword}]
Use topic-specific subheading. List 5-7 main concepts with **Bold Names**
Each with 2-3 sentence explanations. Examples:
**Technology Name** - Detailed explanation of what it is, how it works, why it matters.

## How [Topic] Works
Detailed workflow explanation:
1. Step-by-step process (6-10 steps)
2. Each step: 2-3 sentences
3. Include "Example Workflow:" section at end (150+ words)

## Key Benefits
List 8-10 benefits with **Bold Headers**
Format: **Benefit Name** - 2-3 sentence explanation with specific metrics/outcomes

## Common Use Cases
List 8-10 real-world applications with **Bold Headers**
Format: **Use Case Name** - 2-3 sentence explanation with industry examples

## [Appropriate Comparison Table]
Create comparison table relevant to topic. Include 5-6 items compared across 4-6 dimensions.

## Challenges and Considerations
List 8-10 challenges with **Bold Headers**
Format: **Challenge Name** - 2-3 sentence explanation with mitigation strategies

## Implementation Best Practices
List 10 best practices with **Bold Headers**
Format: **Practice Name** - 2-3 sentence detailed guidance

## [Advanced/Future Section]
Choose appropriate: "Advanced Techniques", "Future Directions", or similar
List 5-6 advanced concepts with **Bold Headers** and explanations

## References
Include 6-8 authoritative references:
- [Title - Source](https://full-url.com)

QUALITY CHECKLIST:
✓ 2,700-2,900 words (count carefully)
✓ 3 paragraphs for "What is" section (800-1000 words)
✓ All sections present with appropriate depth
✓ Comparison table included
✓ Professional tone, specific examples
✓ No redundancy, clear structure
✓ All external links in References only

DO NOT:
✗ Use H3 headings (use **bold** for sub-items instead)
✗ Stop writing before 2,700 words
✗ Summarize or abbreviate content
✗ Include inline external links outside References

IMPORTANT: Write the COMPLETE article to 2,700-2,900 words. Do not stop early."""

def generate_article(keyword: str, slug: str, date: str, output_dir: Path) -> tuple:
    """1記事を生成"""
    client = anthropic.Anthropic(api_key=API_KEY)
    
    start_time = time.time()
    
    try:
        message = client.messages.create(
            model=MODEL,
            max_tokens=16000,  # 増加
            temperature=0.1,   # 低下
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
        cost = (input_tokens * 3 / 1_000_000) + (output_tokens * 15 / 1_000_000)
        
        # 語数カウント
        import re
        words = len(re.findall(r'\b\w+\b', content))
        
        # ファイル保存
        filepath = output_dir / f"{slug}.md"
        filepath.write_text(content, encoding='utf-8')
        
        print(f"✅ {keyword}: {words} words, {output_tokens} tokens, ${cost:.4f}, {elapsed:.1f}s")
        
        return (keyword, True, words, output_tokens, cost, elapsed)
        
    except Exception as e:
        print(f"❌ {keyword}: Error - {e}")
        return (keyword, False, 0, 0, 0.0, 0.0)

def batch_generate(keywords: list, output_dir: Path, max_workers: int = 3):
    """複数記事を並列生成"""
    date = "2025-12-19"
    results = []
    total_cost = 0.0
    total_time = 0.0
    total_tokens = 0
    total_words = 0
    
    # 出力ディレクトリ作成
    output_dir.mkdir(parents=True, exist_ok=True)
    
    print(f"\n{'='*70}")
    print(f"🚀 改善版バッチ生成開始")
    print(f"{'='*70}")
    print(f"記事数: {len(keywords)}")
    print(f"並列数: {max_workers}")
    print(f"出力先: {output_dir}")
    print(f"目標語数: 2,700-2,900語/記事")
    print(f"{'='*70}\n")
    
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {
            executor.submit(generate_article, kw, slug, date, output_dir): (kw, slug)
            for kw, slug in keywords
        }
        
        for future in as_completed(futures):
            keyword, slug = futures[future]
            kw, success, words, tokens, cost, elapsed = future.result()
            
            if success:
                total_cost += cost
                total_time += elapsed
                total_tokens += tokens
                total_words += words
                
                # 語数チェック
                if 2700 <= words <= 2900:
                    word_status = "✅"
                elif 2500 <= words < 2700:
                    word_status = "⚠️"
                else:
                    word_status = "❌"
                
                results.append({
                    "keyword": kw,
                    "slug": slug,
                    "words": words,
                    "word_status": word_status,
                    "tokens": tokens,
                    "cost": f"${cost:.4f}",
                    "time": f"{elapsed:.1f}s",
                    "status": "✅"
                })
            else:
                results.append({
                    "keyword": kw,
                    "slug": slug,
                    "words": 0,
                    "word_status": "❌",
                    "tokens": 0,
                    "cost": "$0.0000",
                    "time": "0.0s",
                    "status": "❌"
                })
    
    # サマリー表示
    successful = sum(1 for r in results if r['status'] == '✅')
    word_compliant = sum(1 for r in results if r['word_status'] == '✅')
    
    print(f"\n{'='*70}")
    print(f"📊 完了サマリー")
    print(f"{'='*70}")
    print(f"成功:         {successful}/{len(keywords)}")
    print(f"語数達成:     {word_compliant}/{len(keywords)} (2,700-2,900語)")
    print(f"平均語数:     {total_words/len(keywords):.0f}語/記事")
    print(f"合計トークン: {total_tokens:,}")
    print(f"合計コスト:   ${total_cost:.4f}")
    print(f"平均時間:     {total_time/len(keywords):.1f}秒/記事")
    print(f"総時間:       {total_time/60:.1f}分")
    print(f"{'='*70}\n")
    
    return results

def main():
    parser = argparse.ArgumentParser(description="改善版Claude API記事自動生成")
    parser.add_argument('--test', action='store_true', help='テストモード（別ディレクトリに出力）')
    parser.add_argument('--keywords', nargs='+', help='キーワードリスト')
    parser.add_argument('--workers', type=int, default=3, help='並列数（デフォルト: 3）')
    parser.add_argument('--output-dir', help='出力ディレクトリ')
    
    args = parser.parse_args()
    
    # テストモードの場合
    if args.test:
        if args.output_dir:
            output_dir = Path(args.output_dir)
        else:
            output_dir = Path("/Users/TM-MBP1/Documents/GitHub/hugo-boilerplate/content/en/glossary-api-test-v2")
        print(f"🧪 テストモード（改善版）: {output_dir}")
    else:
        output_dir = OUTPUT_DIR
    
    # キーワード設定
    if args.keywords:
        keywords = [(kw, kw.replace(' ', '-')) for kw in args.keywords]
    else:
        keywords = [
            ("Customer Segmentation", "Customer-Segmentation"),
            ("Sentiment Analysis", "Sentiment-Analysis"),
            ("Recommendation Systems", "Recommendation-Systems"),
        ]
    
    # 実行
    results = batch_generate(keywords, output_dir, max_workers=args.workers)
    
    # 結果詳細
    print("\n📋 詳細結果:")
    print(f"{'ステータス':<6} {'キーワード':<35} {'語数':<12} {'トークン':<10} {'コスト':<10} {'時間':<8}")
    print("-" * 90)
    for r in results:
        print(f"{r['status']:<6} {r['keyword']:<35} {r['words']:>4}語 {r['word_status']:<6} {r['tokens']:>6}  {r['cost']:<10} {r['time']:<8}")

if __name__ == "__main__":
    main()
