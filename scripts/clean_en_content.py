#!/usr/bin/env python3
"""
英語版コンテンツのクリーン化スクリプト
1. ハードコードされた内部リンクを削除（テキストのみ残す）
2. 太字構文（**text**）をHTMLタグ（<strong>text</strong>）に変換して表示崩れを修正
"""

import re
import os
from pathlib import Path

def clean_content(content: str) -> str:
    # 1. 内部リンクの削除 [text](/en/...) -> text
    # 絶対パスリンクの削除
    abs_link_pattern = r'\[([^\]]+?)\]\((?:/en/|/glossary/|/blog/)[^\)]+\)'
    content = re.sub(abs_link_pattern, r'\1', content)

    # 相対パスリンクの削除 (.md)
    rel_link_pattern = r'\[([^\]]+?)\]\([^)]+\.md\)'
    content = re.sub(rel_link_pattern, r'\1', content)

    # 2. 太字構文の修正: **text** -> <strong>text</strong>
    # コードブロックやフロントマターを除外して処理
    lines = content.split('\n')
    new_lines = []
    in_frontmatter = False
    in_codeblock = False
    
    # 太字パターン
    bold_pattern = re.compile(r'\*\*(?P<text>[^*\n]+?)\*\*')

    for i, line in enumerate(lines):
        # フロントマターの判定
        if i == 0 and line.strip() == '---':
            in_frontmatter = True
            new_lines.append(line)
            continue
        
        if in_frontmatter:
            if line.strip() == '---':
                in_frontmatter = False
            new_lines.append(line)
            continue

        # コードブロックの判定
        if line.strip().startswith('```'):
            in_codeblock = not in_codeblock
            new_lines.append(line)
            continue
        
        if in_codeblock:
            new_lines.append(line)
            continue

        # 通常のテキスト行: 太字を置換
        def replace_bold(match):
            text = match.group('text')
            return f"<strong>{text}</strong>"

        new_line = bold_pattern.sub(replace_bold, line)
        new_lines.append(new_line)

    return '\n'.join(new_lines)

def process_file(file_path: Path) -> bool:
    try:
        content = file_path.read_text(encoding='utf-8')
    except UnicodeDecodeError:
        print(f"⚠️  スキップ（バイナリ等）: {file_path}")
        return False

    original_content = content
    new_content = clean_content(content)
    
    if new_content != original_content:
        file_path.write_text(new_content, encoding='utf-8')
        print(f"✅ 修正完了: {file_path.name}")
        return True
    
    return False

def main():
    # パス設定
    base_dir = Path(__file__).parent.parent
    en_content_dir = base_dir / 'content' / 'en'
    
    if not en_content_dir.exists():
        print(f"❌ 英語コンテンツディレクトリが見つかりません: {en_content_dir}")
        return

    print(f"🚀 英語版コンテンツのクリーン化を開始します: {en_content_dir}")
    print("   - 内部リンクの除去")
    print("   - 太字構文のHTML化")
    
    count = 0
    modified_count = 0
    
    for root, _, files in os.walk(en_content_dir):
        for file in files:
            if file.endswith('.md'):
                file_path = Path(root) / file
                count += 1
                if process_file(file_path):
                    modified_count += 1
    
    print(f"\n✨ 完了しました!")
    print(f"📊 処理ファイル数: {count}")
    print(f"📝 修正ファイル数: {modified_count}")

if __name__ == '__main__':
    main()
