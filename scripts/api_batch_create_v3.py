#!/usr/bin/env python3
"""
Grammar-Fixed Batch Article Creation (v3)
文法修正版API自動化記事生成
"""

import os
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
MODEL = "claude-sonnet-4-20250514"
OUTPUT_DIR = Path("/Users/TM-MBP1/Documents/GitHub/smartweb/content/en/glossary")

def needs_article(keyword: str) -> bool:
    """冠詞が必要かを判定"""
    # 複数形で終わる場合は不要
    if keyword.endswith('s') or keyword.endswith('es'):
        return False
    # 不可算名詞のキーワード（部分一致）
    uncountable = ['forecasting', 'analysis', 'learning', 'intelligence', 'processing', 
                   'management', 'optimization', 'automation', 'segmentation']
    if any(uc in keyword.lower() for uc in uncountable):
        return False
    # デフォルトで冠詞必要
    return True

def get_article(keyword: str) -> str:
    """適切な冠詞を返す"""
    if not needs_article(keyword):
        return ""
    # 母音で始まる場合はan
    if keyword[0].lower() in 'aeiou':
        return "an "
    return "a "

# 文法修正版プロンプト
ARTICLE_PROMPT = """You are an expert technical writer creating a comprehensive glossary article.

TOPIC: {keyword}

CRITICAL REQUIREMENTS:
✓ Language: ENGLISH ONLY
✓ Word count: 2,700-2,900 words (STRICT - do not stop early)
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

EXACT STRUCTURE (use these H2 headings, no H3 unless within lists):

## What is {article}{keyword}?
Write 3 full paragraphs (800-1000 words total):
- Paragraph 1: Comprehensive definition and core concept
- Paragraph 2: How it differs from traditional approaches, transformation it enables
- Paragraph 3: Business impact, measurable outcomes, real-world significance

IMPORTANT: Use proper grammar - "{article}{keyword}" is correct (include "a" or "an" if it's a singular countable noun)

## Core [Specific Technologies/Approaches/Components]
Use topic-specific subheading appropriate for {keyword}. List 5-7 main concepts with **Bold Names**
Each with 2-3 sentence explanations. Examples:
**Technology Name** - Detailed explanation of what it is, how it works, why it matters.

## How {keyword} Works
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
Title should be specific to the topic (e.g., "Recommendation Algorithms Comparison", "Forecasting Approach Comparison")

## Challenges and Considerations
List 8-10 challenges with **Bold Headers**
Format: **Challenge Name** - 2-3 sentence explanation with mitigation strategies

## Implementation Best Practices
List 10 best practices with **Bold Headers**
Format: **Practice Name** - 2-3 sentence detailed guidance

## Advanced Techniques
List 5-6 advanced concepts with **Bold Headers** and explanations (each 2-3 sentences)

## Future Directions
List 5-6 future trends with **Bold Headers** and explanations (each 2-3 sentences)

## References
Include 6-8 authoritative references in standard bibliographic format.
- For articles/reports/books: Author/Organization. (Year). Title. Source Name. (NO LINKS/URLs)
- For services/tools: Name of Service. Description. URL: https://... (Explicit URL)

QUALITY CHECKLIST:
✓ 2,700-2,900 words (count carefully)
✓ 3 paragraphs for "What is" section (800-1000 words)
✓ All sections present with appropriate depth
✓ Comparison table included
✓ Professional tone, specific examples
✓ No redundancy, clear structure
✓ References formatted correctly (Text-only for articles, URL text for services)
✓ Proper English grammar throughout

DO NOT:
✗ Use H3 headings (use **bold** for sub-items instead)
✗ Stop writing before 2,700 words
✗ Summarize or abbreviate content
✗ Include inline external links outside References
✗ Include Markdown links in References (use text citations or explicit URL text)
✗ Forget articles (a/an/the) where grammatically required

IMPORTANT: Write the COMPLETE article to 2,700-2,900 words. Do not stop early."""

def generate_article(keyword: str, slug: str, date: str, output_dir: Path) -> tuple:
    """1記事を生成"""
    client = anthropic.Anthropic(api_key=API_KEY)
    
    start_time = time.time()
    
    # 適切な冠詞を決定
    article = get_article(keyword)
    
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
        
        # トークン数とコスト計算
        input_tokens = message.usage.input_tokens
        output_tokens = message.usage.output_tokens
        cost = (input_tokens * 3 / 1_000_000) + (output_tokens * 15 / 1_000_000)
        
        # 語数カウント
        words = len(re.findall(r'\b\w+\b', content))
        
        # 文法チェック: "What is [keyword]?" の確認
        grammar_ok = True
        if needs_article(keyword):
            expected = f"What is {article}{keyword}?"
            if expected not in content:
                grammar_ok = False
                print(f"  ⚠️  文法警告: '{expected}' が見つかりません")
        
        # ファイル保存
        filepath = output_dir / f"{slug}.md"
        filepath.write_text(content, encoding='utf-8')
        
        status = "✅" if grammar_ok else "⚠️"
        print(f"{status} {keyword}: {words} words, {output_tokens} tokens, ${cost:.4f}, {elapsed:.1f}s")
        
        return (keyword, True, words, output_tokens, cost, elapsed, grammar_ok)
        
    except Exception as e:
        print(f"❌ {keyword}: Error - {e}")
        return (keyword, False, 0, 0, 0.0, 0.0, False)

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
    print(f"🚀 文法修正版バッチ生成開始 (v3)")
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
            kw, success, words, tokens, cost, elapsed, grammar_ok = future.result()
            
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
                
                grammar_status = "✅" if grammar_ok else "⚠️"
                
                results.append({
                    "keyword": kw,
                    "slug": slug,
                    "words": words,
                    "word_status": word_status,
                    "grammar_status": grammar_status,
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
                    "grammar_status": "❌",
                    "tokens": 0,
                    "cost": "$0.0000",
                    "time": "0.0s",
                    "status": "❌"
                })
    
    # サマリー表示
    successful = sum(1 for r in results if r['status'] == '✅')
    word_compliant = sum(1 for r in results if r['word_status'] == '✅')
    grammar_ok = sum(1 for r in results if r['grammar_status'] == '✅')
    
    print(f"\n{'='*70}")
    print(f"📊 完了サマリー")
    print(f"{'='*70}")
    print(f"成功:         {successful}/{len(keywords)}")
    print(f"語数達成:     {word_compliant}/{len(keywords)} (2,700-2,900語)")
    print(f"文法OK:       {grammar_ok}/{len(keywords)}")
    print(f"平均語数:     {total_words/len(keywords):.0f}語/記事")
    print(f"合計トークン: {total_tokens:,}")
    print(f"合計コスト:   ${total_cost:.4f}")
    print(f"平均時間:     {total_time/len(keywords):.1f}秒/記事")
    print(f"総時間:       {total_time/60:.1f}分")
    print(f"{'='*70}\n")
    
    return results

def main():
    parser = argparse.ArgumentParser(description="文法修正版Claude API記事自動生成 (v3)")
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
            output_dir = Path("/Users/TM-MBP1/Documents/GitHub/smartweb/content/en/glossary-api-test-v3")
        print(f"🧪 テストモード（文法修正版v3）: {output_dir}")
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
    print(f"{'ステータス':<6} {'キーワード':<35} {'語数':<12} {'文法':<6} {'トークン':<10} {'コスト':<10} {'時間':<8}")
    print("-" * 95)
    for r in results:
        print(f"{r['status']:<6} {r['keyword']:<35} {r['words']:>4}語 {r['word_status']:<6} {r['grammar_status']:<6} {r['tokens']:>6}  {r['cost']:<10} {r['time']:<8}")

if __name__ == "__main__":
    main()
