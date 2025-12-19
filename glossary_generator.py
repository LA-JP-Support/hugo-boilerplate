#!/usr/bin/env python3
"""
Glossary Article Generator
==========================
Claude API を使用した用語集記事の自動生成システム

機能:
- CSV からキーワードを読み込み
- Claude API で高品質な記事を生成
- 品質検証（語数、フォーマット、References）
- マルチスレッド処理による高速化
- 進捗管理とエラーハンドリング
- Hugo用マークダウン出力

使用方法:
    python glossary_generator.py --keywords docs/prioritized_keywords.csv --threads 3 --batch 10

環境変数:
    CLAUDE_API_KEY または ANTHROPIC_API_KEY: Claude API キー
    （.env ファイルから自動読み込み）
"""

import os
import sys
import csv
import json
import time
import re
import argparse
import logging
from datetime import datetime
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass, asdict
from typing import List, Dict, Optional, Tuple
import threading

# .env ファイルから環境変数を読み込み
def load_env_file(env_path: str = ".env"):
    """Load environment variables from .env file"""
    if Path(env_path).exists():
        with open(env_path, 'r') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    key, value = line.split('=', 1)
                    # Remove quotes if present
                    value = value.strip().strip('"').strip("'")
                    os.environ[key] = value

# Load .env from current directory
load_env_file()

# Anthropic SDK
try:
    import anthropic
except ImportError:
    print("Please install anthropic: pip install anthropic")
    sys.exit(1)

# Get API key
API_KEY = os.environ.get("CLAUDE_API_KEY") or os.environ.get("ANTHROPIC_API_KEY")
if not API_KEY:
    print("Error: CLAUDE_API_KEY or ANTHROPIC_API_KEY not found in environment or .env file")
    sys.exit(1)

# ===== Configuration =====

@dataclass
class Config:
    """システム設定"""
    # API設定
    model: str = "claude-sonnet-4-20250514"  # claude-sonnet-4-20250514 または claude-opus-4-5-20251101
    max_tokens: int = 8000
    temperature: float = 0.7
    
    # 品質基準
    target_word_count_min: int = 2000
    target_word_count_max: int = 3000
    max_retries: int = 3
    
    # 処理設定
    threads: int = 3  # 同時処理スレッド数
    batch_size: int = 10  # バッチサイズ
    delay_between_calls: float = 1.0  # API呼び出し間の遅延（秒）
    
    # 出力設定
    output_dir: str = "./content/en/glossary"
    log_dir: str = "./logs"
    progress_file: str = "./docs/generation_progress.json"


# ===== System Prompt =====

SYSTEM_PROMPT = """You are a professional content writer specializing in technology glossary articles.

## Your Task
Generate a comprehensive glossary article for the given keyword following these exact specifications:

## Article Specifications

### Length & Format
- **Target word count**: 2,500 words (aim for 2,500 words, minimum 2,000)
- **Format ratio**: 30% prose (paragraphs), 70% structured content (bullets, tables)
- **Language**: English only
- **IMPORTANT**: Write comprehensive, detailed content. Each section should be thorough.

### Required Structure

1. **What is [Term]?** (2-3 paragraphs of prose)
   - Clear, comprehensive definition
   - Context and importance
   - Key characteristics

2. **Key Features / Core Concepts** (bullet points)
   - 5-8 main features with 1-2 sentence descriptions each
   - Use **bold subheadings** for each point

3. **How It Works / Technical Architecture** (if applicable)
   - Step-by-step explanation
   - Diagrams described in text if helpful

4. **Benefits / Advantages** (bullet points)
   - Organized by stakeholder (Users, Organizations) if appropriate

5. **Common Use Cases / Examples** (bullet points or short paragraphs)
   - Real-world applications
   - Industry-specific examples

6. **Best Practices** (bullet points)
   - Implementation guidance
   - Tips for success

7. **Challenges and Considerations** (bullet points)
   - Common pitfalls
   - Mitigation strategies

8. **FAQ** (Optional, if space allows)
   - 3-5 common questions with brief answers

9. **References**
   - All external links consolidated here
   - Format: `- [Title - Source](URL)`
   - Include 5-8 authoritative sources
   - Use real, verifiable URLs from authoritative sources

### Formatting Rules

✅ DO:
- Use **bold subheadings** for bullet points
- Keep paragraphs short (3-4 sentences)
- Include specific examples
- Maintain technical accuracy
- Use clear, professional language

❌ DON'T:
- No inline external links (all in References)
- No redundant explanations
- No excessive headers
- No content in any language other than English

### Frontmatter Template
```yaml
---
title: "[Keyword]"
date: [YYYY-MM-DD]
translationKey: [keyword-slug]
description: "[150-160 character SEO description]"
keywords:
- [primary keyword]
- [related keyword 1]
- [related keyword 2]
- [related keyword 3]
category: "[Category from input]"
type: glossary
draft: false
---
```

## Important - READ CAREFULLY
- **WORD COUNT IS CRITICAL**: Aim for 2,500 words (minimum 2,000 words).
- Write comprehensive, authoritative content with detailed explanations
- Include multiple examples in each section
- Ensure technical accuracy
- All content must be in English
- References must include real, working URLs
- Each bullet point should be 2-3 sentences, not just one sentence
- The "What is" section should be 3 full paragraphs
- Include at least 6-8 items in each bullet list section
"""


# ===== Data Classes =====

@dataclass
class Keyword:
    """キーワードデータ"""
    keyword: str
    definition: str
    category: str
    filename: str
    
    @property
    def slug(self) -> str:
        """URL用スラッグを生成"""
        # Convert to slug format matching existing files
        slug = self.keyword.replace(' ', '-').replace('/', '-')
        slug = re.sub(r'[()]', '', slug)
        slug = re.sub(r'--+', '-', slug)
        return slug


@dataclass
class GenerationResult:
    """生成結果"""
    keyword: str
    success: bool
    word_count: int = 0
    file_path: str = ""
    error: str = ""
    retries: int = 0
    generation_time: float = 0.0


# ===== Article Generator =====

class GlossaryGenerator:
    """用語集記事生成クラス"""
    
    def __init__(self, config: Config):
        self.config = config
        self.client = anthropic.Anthropic(api_key=API_KEY)
        self.lock = threading.Lock()
        self.progress = {"completed": [], "failed": [], "pending": []}
        
        # ディレクトリ作成
        Path(config.output_dir).mkdir(parents=True, exist_ok=True)
        Path(config.log_dir).mkdir(parents=True, exist_ok=True)
        Path(config.progress_file).parent.mkdir(parents=True, exist_ok=True)
        
        # ロギング設定
        log_file = f"{config.log_dir}/generator_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(log_file, encoding='utf-8'),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)
        self.logger.info(f"Log file: {log_file}")
    
    def count_words(self, text: str) -> int:
        """記事の語数をカウント（frontmatter除外）"""
        # frontmatter を除外
        if text.startswith('---'):
            parts = text.split('---', 2)
            if len(parts) >= 3:
                text = parts[2]
        
        # マークダウン記号を除去
        text = re.sub(r'[#*\-\[\]\(\)`]', ' ', text)
        words = text.split()
        return len(words)
    
    def validate_article(self, content: str) -> Tuple[bool, str]:
        """記事の品質を検証"""
        word_count = self.count_words(content)
        
        # 語数チェック
        if word_count < self.config.target_word_count_min:
            return False, f"Word count too low: {word_count} (min: {self.config.target_word_count_min})"
        if word_count > self.config.target_word_count_max + 200:  # 少し余裕を持たせる
            return False, f"Word count too high: {word_count} (max: {self.config.target_word_count_max})"
        
        # References セクションチェック
        if "## References" not in content and "## references" not in content.lower():
            return False, "Missing References section"
        
        # frontmatter チェック
        if not content.startswith('---'):
            return False, "Missing frontmatter"
        
        return True, f"Valid ({word_count} words)"
    
    def generate_article(self, keyword: Keyword) -> GenerationResult:
        """単一の記事を生成"""
        start_time = time.time()
        
        user_prompt = f"""Generate a glossary article for:

**Keyword**: {keyword.keyword}
**Category**: {keyword.category}
**Brief Definition**: {keyword.definition}

IMPORTANT REQUIREMENTS:
1. Write approximately 2,500 words (minimum 2,000 words)
2. Include detailed explanations with examples
3. Each bullet point should be 2-3 sentences
4. Include a References section with 5-8 real URLs

Today's date for frontmatter: {datetime.now().strftime('%Y-%m-%d')}
"""
        
        for retry in range(self.config.max_retries):
            try:
                self.logger.info(f"Generating: {keyword.keyword} (attempt {retry + 1})")
                
                response = self.client.messages.create(
                    model=self.config.model,
                    max_tokens=self.config.max_tokens,
                    temperature=self.config.temperature,
                    system=SYSTEM_PROMPT,
                    messages=[{"role": "user", "content": user_prompt}]
                )
                
                content = response.content[0].text
                
                # 品質検証
                is_valid, message = self.validate_article(content)
                
                if is_valid:
                    # ファイル保存
                    file_path = Path(self.config.output_dir) / f"{keyword.slug}.md"
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    
                    generation_time = time.time() - start_time
                    self.logger.info(f"✓ Generated: {keyword.keyword} ({self.count_words(content)} words, {generation_time:.1f}s)")
                    
                    return GenerationResult(
                        keyword=keyword.keyword,
                        success=True,
                        word_count=self.count_words(content),
                        file_path=str(file_path),
                        retries=retry,
                        generation_time=generation_time
                    )
                else:
                    self.logger.warning(f"Validation failed for {keyword.keyword}: {message}")
                    
                    # 語数調整のリトライプロンプト
                    if "too low" in message:
                        user_prompt = f"""The previous attempt was too short ({self.count_words(content)} words).

Please regenerate the article for **{keyword.keyword}** with MORE content.
Target: 2,600-2,800 words. Add more detailed explanations, examples, and use cases.

Category: {keyword.category}
Definition: {keyword.definition}
Date: {datetime.now().strftime('%Y-%m-%d')}
"""
                    elif "too high" in message:
                        user_prompt = f"""The previous attempt was too long ({self.count_words(content)} words).

Please regenerate the article for **{keyword.keyword}** with LESS content.
Target: 2,600-2,800 words. Be more concise while keeping essential information.

Category: {keyword.category}
Definition: {keyword.definition}
Date: {datetime.now().strftime('%Y-%m-%d')}
"""
                    
                    time.sleep(self.config.delay_between_calls)
                    
            except anthropic.RateLimitError as e:
                self.logger.warning(f"Rate limit hit, waiting 60 seconds...")
                time.sleep(60)
            except anthropic.APIError as e:
                self.logger.error(f"API error for {keyword.keyword}: {str(e)}")
                if retry < self.config.max_retries - 1:
                    time.sleep(self.config.delay_between_calls * 2)
            except Exception as e:
                self.logger.error(f"Error generating {keyword.keyword}: {str(e)}")
                if retry < self.config.max_retries - 1:
                    time.sleep(self.config.delay_between_calls * 2)
        
        return GenerationResult(
            keyword=keyword.keyword,
            success=False,
            error=f"Failed after {self.config.max_retries} retries",
            retries=self.config.max_retries,
            generation_time=time.time() - start_time
        )
    
    def update_progress(self, result: GenerationResult):
        """進捗を更新"""
        with self.lock:
            if result.success:
                self.progress["completed"].append(asdict(result))
            else:
                self.progress["failed"].append(asdict(result))
            
            # pending から削除
            if result.keyword in self.progress["pending"]:
                self.progress["pending"].remove(result.keyword)
            
            # 進捗ファイル保存
            with open(self.config.progress_file, 'w', encoding='utf-8') as f:
                json.dump(self.progress, f, indent=2, ensure_ascii=False)
    
    def run(self, keywords: List[Keyword], resume: bool = True):
        """メイン実行"""
        # 進捗ファイルから再開
        if resume and Path(self.config.progress_file).exists():
            with open(self.config.progress_file, 'r') as f:
                self.progress = json.load(f)
            completed_keywords = {r["keyword"] for r in self.progress["completed"]}
            keywords = [k for k in keywords if k.keyword not in completed_keywords]
            self.logger.info(f"Resuming from progress file. {len(completed_keywords)} already completed.")
        
        self.progress["pending"] = [k.keyword for k in keywords]
        
        if not keywords:
            self.logger.info("No keywords to process.")
            self.print_summary()
            return []
        
        self.logger.info(f"Starting generation of {len(keywords)} articles with {self.config.threads} threads")
        self.logger.info(f"Model: {self.config.model}")
        self.logger.info(f"Output directory: {self.config.output_dir}")
        
        results = []
        
        with ThreadPoolExecutor(max_workers=self.config.threads) as executor:
            futures = {executor.submit(self.generate_article, k): k for k in keywords}
            
            for future in as_completed(futures):
                keyword = futures[future]
                try:
                    result = future.result()
                    results.append(result)
                    self.update_progress(result)
                    
                    # 進捗表示
                    completed = len(self.progress["completed"])
                    failed = len(self.progress["failed"])
                    total = len(keywords) + len([r for r in self.progress["completed"] if r not in [asdict(res) for res in results]])
                    self.logger.info(f"Progress: {completed} completed, {failed} failed, {len(self.progress['pending'])} pending")
                    
                except Exception as e:
                    self.logger.error(f"Unexpected error for {keyword.keyword}: {str(e)}")
                
                # API負荷軽減
                time.sleep(self.config.delay_between_calls)
        
        # 最終レポート
        self.print_summary()
        
        return results
    
    def print_summary(self):
        """実行サマリーを表示"""
        completed = len(self.progress["completed"])
        failed = len(self.progress["failed"])
        
        total_words = sum(r["word_count"] for r in self.progress["completed"])
        avg_words = total_words / completed if completed > 0 else 0
        total_time = sum(r["generation_time"] for r in self.progress["completed"])
        
        print("\n" + "=" * 60)
        print("GENERATION SUMMARY")
        print("=" * 60)
        print(f"Completed: {completed}")
        print(f"Failed: {failed}")
        print(f"Total words generated: {total_words:,}")
        print(f"Average words per article: {avg_words:.0f}")
        print(f"Total generation time: {total_time/60:.1f} minutes")
        if completed > 0:
            print(f"Average time per article: {total_time/completed:.1f} seconds")
        print("=" * 60)
        
        if failed > 0:
            print("\nFailed keywords:")
            for r in self.progress["failed"]:
                print(f"  - {r['keyword']}: {r['error']}")


# ===== Main =====

def load_keywords(csv_path: str) -> List[Keyword]:
    """CSVからキーワードを読み込み"""
    keywords = []
    with open(csv_path, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for row in reader:
            keywords.append(Keyword(
                keyword=row['keyword'].strip(),
                definition=row.get('definition', '').strip(),
                category=row.get('category', '').strip(),
                filename=row.get('filename', '').strip()
            ))
    return keywords


def main():
    parser = argparse.ArgumentParser(description='Glossary Article Generator')
    parser.add_argument('--keywords', '-k', required=True, help='Path to keywords CSV file')
    parser.add_argument('--threads', '-t', type=int, default=3, help='Number of concurrent threads (default: 3)')
    parser.add_argument('--batch', '-b', type=int, default=0, help='Process only first N keywords (0 = all)')
    parser.add_argument('--model', '-m', default='claude-sonnet-4-20250514', 
                       choices=['claude-sonnet-4-20250514', 'claude-opus-4-5-20251101'],
                       help='Claude model to use')
    parser.add_argument('--output', '-o', default='./content/en/glossary', help='Output directory')
    parser.add_argument('--no-resume', action='store_true', help='Start fresh, ignore progress file')
    
    args = parser.parse_args()
    
    # 設定
    config = Config(
        model=args.model,
        threads=args.threads,
        output_dir=args.output
    )
    
    # キーワード読み込み
    keywords = load_keywords(args.keywords)
    
    if args.batch > 0:
        keywords = keywords[:args.batch]
    
    print("=" * 60)
    print("GLOSSARY ARTICLE GENERATOR")
    print("=" * 60)
    print(f"Keywords file: {args.keywords}")
    print(f"Keywords to process: {len(keywords)}")
    print(f"Model: {config.model}")
    print(f"Threads: {config.threads}")
    print(f"Output: {config.output_dir}")
    print("=" * 60)
    print()
    
    # コスト見積もり
    estimated_cost = len(keywords) * 0.16  # Sonnet 4.5 の場合
    print(f"Estimated cost (Sonnet 4.5): ${estimated_cost:.2f} (¥{estimated_cost * 150:.0f})")
    print(f"Estimated time: {len(keywords) * 45 / config.threads / 60:.1f} minutes")
    print()
    
    # 確認
    response = input(f"Generate {len(keywords)} articles? (y/n): ")
    if response.lower() != 'y':
        print("Cancelled.")
        return
    
    # 生成実行
    generator = GlossaryGenerator(config)
    generator.run(keywords, resume=not args.no_resume)


if __name__ == '__main__':
    main()
