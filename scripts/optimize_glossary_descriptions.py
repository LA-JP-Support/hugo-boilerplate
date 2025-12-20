#!/usr/bin/env python3
"""
Glossary Description Optimizer
用語集のdescriptionフィールドを最適化するスクリプト

このスクリプトは、用語集ファイルのdescriptionフィールドをチェックし、
"Comprehensive guide to..."のような冗長な前置きを削除して、
本文の"What is a [Term]?"セクションから簡潔な要約を抽出します。
"""

import os
import re
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple
import anthropic
from dotenv import load_dotenv
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

# .envファイルから環境変数を読み込み
load_dotenv()

# 設定（ANTHROPIC_API_KEY または CLAUDE_API_KEY を使用）
ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY") or os.environ.get("CLAUDE_API_KEY")
if not ANTHROPIC_API_KEY:
    print("エラー: ANTHROPIC_API_KEY または CLAUDE_API_KEY が設定されていません")
    print("使用方法: .envファイルに ANTHROPIC_API_KEY='your-api-key-here' を追加")
    sys.exit(1)

# Claude APIクライアントの初期化
client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

# 問題のあるdescriptionパターン（英語）
PROBLEMATIC_PATTERNS_EN = [
    r"^Comprehensive guide to",
    r"^Complete guide to",
    r"^Detailed guide to",
    r"^In-depth guide to",
    r"^Ultimate guide to",
    r"^Essential guide to",
]

# 問題のあるdescriptionパターン（日本語）
PROBLEMATIC_PATTERNS_JA = [
    r"について詳しく解説",
    r"の包括的なガイド",
    r"の完全ガイド",
]


def extract_frontmatter_and_content(file_path: Path) -> Tuple[str, str, str]:
    """
    Markdownファイルからfront matter、description、本文を抽出
    
    Returns:
        (frontmatter, description, content)
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Front matterの抽出
    frontmatter_match = re.match(r'^---\n(.*?)\n---\n(.*)$', content, re.DOTALL)
    if not frontmatter_match:
        return "", "", content
    
    frontmatter = frontmatter_match.group(1)
    body = frontmatter_match.group(2)
    
    # descriptionの抽出
    desc_match = re.search(r'^description:\s*["\']?(.*?)["\']?\s*$', frontmatter, re.MULTILINE)
    description = desc_match.group(1) if desc_match else ""
    
    return frontmatter, description, body


def is_problematic_description(description: str, lang: str) -> bool:
    """descriptionが問題のあるパターンに該当するかチェック"""
    patterns = PROBLEMATIC_PATTERNS_EN if lang == "en" else PROBLEMATIC_PATTERNS_JA
    
    for pattern in patterns:
        if re.search(pattern, description, re.IGNORECASE):
            return True
    
    # 長すぎる場合も問題とみなす（150文字以上）
    if len(description) > 150:
        return True
    
    return False


def generate_better_description(title: str, current_desc: str, content: str, lang: str) -> Optional[str]:
    """
    Claude APIを使用して、より良いdescriptionを生成
    """
    
    # 本文から"What is"セクションを抽出（最初の500文字程度）
    content_preview = content[:1500]
    
    prompt = f"""あなたは用語集の編集者です。以下の用語について、一般の人にもわかりやすい簡潔な説明を生成してください。

用語: {title}
現在のdescription: {current_desc}

本文の抜粋:
{content_preview}

要件:
1. 1-2文、最大100文字以内
2. 用語の定義と、何のために使うのかを簡潔に説明
3. 専門用語は最小限に、一般の人にも理解できる表現を使う
4. 本文の"What is a {title}?"または"{title}とは?"セクションから抽出
5. {"英語" if lang == "en" else "日本語"}で出力
6. 引用符は含めない

例（良い例 - わかりやすい）:
- "A reusable code snippet in Hugo that adds dynamic features to static web pages."
- "Software that helps teams create, edit, and publish website content without coding."
- "AI technology that copies a person's voice to generate new speech in their voice."

例（悪い例 - 専門的すぎる）:
- "A templating abstraction layer utilizing parametric encapsulation for content injection."

新しいdescription:"""

    try:
        message = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=300,
            temperature=0.3,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        
        new_description = message.content[0].text.strip()
        # 引用符を削除
        new_description = new_description.strip('"\'')
        
        return new_description
    
    except Exception as e:
        print(f"  ⚠️  Claude API エラー: {e}")
        return None


def update_description_in_file(file_path: Path, new_description: str) -> bool:
    """
    ファイル内のdescriptionを更新
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # descriptionを置換（引用符の有無に対応）
        updated_content = re.sub(
            r'^description:\s*["\']?.*?["\']?\s*$',
            f'description: "{new_description}"',
            content,
            count=1,
            flags=re.MULTILINE
        )
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        
        return True
    
    except Exception as e:
        print(f"  ⚠️  ファイル更新エラー: {e}")
        return False


def process_glossary_file(file_path: Path, lang: str, dry_run: bool = True) -> Dict:
    """
    用語集ファイルを処理
    
    Returns:
        処理結果の辞書
    """
    result = {
        "file": str(file_path.relative_to(file_path.parents[3])),
        "status": "skipped",
        "old_description": "",
        "new_description": "",
        "reason": ""
    }
    
    try:
        frontmatter, description, content = extract_frontmatter_and_content(file_path)
        
        if not description:
            result["reason"] = "descriptionなし"
            return result
        
        result["old_description"] = description
        
        # 問題のあるdescriptionかチェック
        if not is_problematic_description(description, lang):
            result["status"] = "ok"
            result["reason"] = "問題なし"
            return result
        
        # タイトルを抽出
        title_match = re.search(r'^title:\s*["\']?(.*?)["\']?\s*$', frontmatter, re.MULTILINE)
        title = title_match.group(1) if title_match else "Unknown"
        
        # 新しいdescriptionを生成
        new_description = generate_better_description(title, description, content, lang)
        
        if not new_description:
            result["status"] = "error"
            result["reason"] = "生成失敗"
            return result
        
        result["new_description"] = new_description
        
        if not dry_run:
            if update_description_in_file(file_path, new_description):
                result["status"] = "updated"
            else:
                result["status"] = "error"
                result["reason"] = "更新失敗"
        else:
            result["status"] = "would_update"
        
        return result
    
    except Exception as e:
        result["status"] = "error"
        result["reason"] = str(e)
        print(f"  ⚠️  エラー: {e}")
        return result


def main():
    """メイン処理"""
    import argparse
    
    parser = argparse.ArgumentParser(description="用語集のdescriptionを最適化")
    parser.add_argument("--path", default="content", help="用語集ディレクトリのパス")
    parser.add_argument("--lang", choices=["en", "ja", "both"], default="both", help="処理する言語")
    parser.add_argument("--dry-run", action="store_true", help="実際には更新せず、提案のみ表示")
    parser.add_argument("--limit", type=int, help="処理するファイル数の上限")
    parser.add_argument("--workers", type=int, default=5, help="並列処理のスレッド数（デフォルト: 5）")
    
    args = parser.parse_args()
    
    base_path = Path(args.path)
    
    if not base_path.exists():
        print(f"エラー: パス '{base_path}' が見つかりません")
        sys.exit(1)
    
    # 処理する言語を決定
    langs = []
    if args.lang in ["en", "both"]:
        langs.append("en")
    if args.lang in ["ja", "both"]:
        langs.append("ja")
    
    all_results = []
    
    for lang in langs:
        glossary_path = base_path / lang / "glossary"
        
        if not glossary_path.exists():
            print(f"⚠️  {lang} の用語集ディレクトリが見つかりません: {glossary_path}")
            continue
        
        print(f"\n{'='*60}")
        print(f"🌐 言語: {lang.upper()}")
        print(f"📂 ディレクトリ: {glossary_path}")
        print(f"{'='*60}")
        
        # すべての.mdファイルを取得
        md_files = list(glossary_path.glob("*.md"))
        
        if args.limit:
            md_files = md_files[:args.limit]
        
        print(f"📊 対象ファイル数: {len(md_files)}")
        print(f"🔧 並列スレッド数: {args.workers}")
        
        # 並列処理で実行
        start_time = time.time()
        with ThreadPoolExecutor(max_workers=args.workers) as executor:
            # 各ファイルの処理をスレッドプールに投入
            future_to_file = {
                executor.submit(process_glossary_file, file_path, lang, args.dry_run): (i, file_path)
                for i, file_path in enumerate(md_files, 1)
            }
            
            # 完了した順に結果を取得
            for future in as_completed(future_to_file):
                i, file_path = future_to_file[future]
                try:
                    result = future.result()
                    all_results.append(result)
                    print(f"✓ [{i}/{len(md_files)}] {file_path.name} 完了")
                except Exception as e:
                    print(f"✗ [{i}/{len(md_files)}] {file_path.name} エラー: {e}")
        
        elapsed_time = time.time() - start_time
        print(f"\n⏱️  処理時間: {elapsed_time:.1f}秒")
    
    # サマリーを表示
    print(f"\n{'='*60}")
    print("📊 処理結果サマリー")
    print(f"{'='*60}")
    
    status_counts = {}
    for result in all_results:
        status = result["status"]
        status_counts[status] = status_counts.get(status, 0) + 1
    
    for status, count in status_counts.items():
        emoji = {
            "ok": "✅",
            "updated": "🔄",
            "would_update": "💡",
            "skipped": "⏭️",
            "error": "❌"
        }.get(status, "❓")
        print(f"{emoji} {status}: {count}件")
    
    # 更新されたファイルのリストを表示
    updated = [r for r in all_results if r["status"] in ["updated", "would_update"]]
    if updated:
        print(f"\n{'='*60}")
        print(f"{'💡 提案' if args.dry_run else '🔄 更新済み'}ファイル一覧:")
        print(f"{'='*60}")
        for r in updated:
            print(f"\n📄 {r['file']}")
            print(f"   旧: {r['old_description'][:80]}...")
            print(f"   新: {r['new_description']}")
    
    if args.dry_run and updated:
        print(f"\n{'='*60}")
        print("ℹ️  実際に更新するには --dry-run フラグを外して再実行してください")
        print(f"{'='*60}")


if __name__ == "__main__":
    main()
