#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Draft記事を一括公開
draft = true → draft = false に一括変更

使用方法:
    python3 publish_drafts.py --dir content/en/glossary/
    python3 publish_drafts.py --dir content/ja/glossary/
    
    # 確認のみ（実際には変更しない）
    python3 publish_drafts.py --dir content/en/glossary/ --dry-run
"""

import os
import argparse
from pathlib import Path
import re


def publish_draft(file_path, dry_run=False):
    """
    1つのMarkdownファイルの draft = true を draft = false に変更
    
    Args:
        file_path: Markdownファイルのパス
        dry_run: Trueの場合、変更を表示するのみで実際には変更しない
    
    Returns:
        bool: 変更があったかどうか
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # draft = true を探す
        if 'draft = true' not in content.lower():
            return False
        
        # draft = true → draft = false に置換
        # TOML形式とYAML形式の両方に対応
        new_content = re.sub(
            r'draft\s*=\s*true',
            'draft = false',
            content,
            flags=re.IGNORECASE
        )
        
        # YAML形式も対応（draft: true）
        new_content = re.sub(
            r'draft:\s*true',
            'draft: false',
            new_content,
            flags=re.IGNORECASE
        )
        
        if dry_run:
            print(f"✓ 変更対象: {file_path.name}")
            return True
        
        # ファイルに書き込み
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"✅ 公開: {file_path.name}")
        return True
        
    except Exception as e:
        print(f"❌ エラー: {file_path.name} - {e}")
        return False


def publish_all_drafts(directory, dry_run=False):
    """
    ディレクトリ内の全Draft記事を公開
    
    Args:
        directory: 検索対象ディレクトリ
        dry_run: Trueの場合、変更を表示するのみ
    """
    dir_path = Path(directory)
    
    if not dir_path.exists():
        print(f"❌ ディレクトリが見つかりません: {directory}")
        return
    
    print("=" * 60)
    print("📝 Draft記事一括公開ツール")
    print("=" * 60)
    print(f"対象ディレクトリ: {directory}")
    print(f"モード: {'確認のみ（変更なし）' if dry_run else '実際に変更'}")
    print("=" * 60)
    print()
    
    # .mdファイルを検索
    md_files = list(dir_path.glob('*.md'))
    
    if not md_files:
        print("⚠️  Markdownファイルが見つかりません")
        return
    
    changed_count = 0
    
    for md_file in md_files:
        if publish_draft(md_file, dry_run):
            changed_count += 1
    
    print()
    print("=" * 60)
    print("📊 処理結果")
    print("=" * 60)
    print(f"処理したファイル数: {len(md_files)}")
    print(f"変更したファイル数: {changed_count}")
    print(f"変更なしファイル数: {len(md_files) - changed_count}")
    print("=" * 60)
    
    if dry_run and changed_count > 0:
        print()
        print("💡 実際に変更するには --dry-run なしで実行してください")
    elif changed_count > 0:
        print()
        print("✅ 完了！以下を実行して確認してください:")
        print("   hugo server")


def main():
    parser = argparse.ArgumentParser(
        description='Draft記事を一括公開（draft = true → draft = false）'
    )
    parser.add_argument(
        '--dir',
        required=True,
        help='対象ディレクトリパス（例: content/en/glossary/）'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='確認のみ（実際には変更しない）'
    )
    
    args = parser.parse_args()
    
    publish_all_drafts(args.dir, args.dry_run)


if __name__ == '__main__':
    main()
