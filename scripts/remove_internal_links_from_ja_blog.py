#!/usr/bin/env python3
"""
日本語ブログ記事から誤って追加された内部リンクを削除するスクリプト
Markdownファイルをクリーンな状態に戻す
"""

import re
from pathlib import Path

def remove_internal_links_from_content(content: str) -> str:
    """
    コンテンツから内部リンクを削除
    [テキスト](/en/glossary/term/) → テキスト
    """
    # 内部リンクのパターン: [テキスト](/en/glossary/.../)
    pattern = r'\[([^\]]+?)\]\(/en/glossary/[^\)]+?/\)'
    
    # リンクをテキストのみに置換
    cleaned = re.sub(pattern, r'\1', content)
    
    return cleaned

def clean_ja_blog_file(file_path: Path) -> bool:
    """
    日本語ブログファイルから内部リンクを削除
    """
    if not file_path.exists():
        print(f"⚠️  ファイルが存在しません: {file_path}")
        return False
    
    print(f"📝 処理中: {file_path.name}")
    
    # ファイルを読み込み
    content = file_path.read_text(encoding='utf-8')
    original_content = content
    
    # 内部リンクを削除
    content = remove_internal_links_from_content(content)
    
    # 変更があった場合のみ書き込み
    if content != original_content:
        file_path.write_text(content, encoding='utf-8')
        print(f"✅ クリーンアップ完了: {file_path.name}")
        return True
    else:
        print(f"ℹ️  変更なし: {file_path.name}")
        return False

def main():
    # パスの設定
    base_dir = Path(__file__).parent.parent
    ja_blog_dir = base_dir / 'content' / 'ja' / 'blog'
    
    if not ja_blog_dir.exists():
        print(f"❌ 日本語ブログディレクトリが見つかりません: {ja_blog_dir}")
        return
    
    # 日本語ブログファイルを処理
    ja_files = sorted(ja_blog_dir.glob('*.md'))
    total_files = len(ja_files)
    cleaned_files = 0
    
    print(f"\n🚀 日本語ブログ記事から内部リンクを削除します")
    print(f"📊 対象ファイル数: {total_files}\n")
    
    for ja_file in ja_files:
        if clean_ja_blog_file(ja_file):
            cleaned_files += 1
    
    print(f"\n✨ 完了!")
    print(f"📊 クリーンアップしたファイル: {cleaned_files}/{total_files}")

if __name__ == '__main__':
    main()
