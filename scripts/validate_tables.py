#!/usr/bin/env python3
"""
validate_tables.py

Markdownファイル内の表をチェックし、問題を検出・修正します。

問題:
1. ヘッダー行の後に区切り線(|---|---|)がない
2. セル内に改行がある（<br>に変換が必要）

使用方法:
    python validate_tables.py [--fix] [--path /path/to/content]
    python validate_tables.py --fix --path ../content/ja
"""

import os
import re
import sys
import argparse
from pathlib import Path

def find_table_issues(content, filename):
    """
    Markdownコンテンツ内の表の問題を検出
    
    Returns:
        list: 問題のリスト [(line_number, issue_type, description)]
    """
    issues = []
    lines = content.split('\n')
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        # 表のヘッダー行を検出（|で始まり|で終わる）
        if line.startswith('|') and line.endswith('|') and line.count('|') >= 3:
            # 次の行が区切り線かチェック
            if i + 1 < len(lines):
                next_line = lines[i + 1].strip()
                # 区切り線のパターン: |---|---| または |-----|-----|
                if not re.match(r'^\|[\s\-:]+\|', next_line) or '---' not in next_line:
                    issues.append((i + 1, 'missing_separator', f'表のヘッダー行の後に区切り線がありません'))
        
        # 表のセル内に改行があるかチェック（複数行にまたがるセル）
        if line.startswith('|') and not re.match(r'^\|[\s\-:]+\|', line):
            # 次の行が|で始まらない場合、前の行の続きの可能性
            if i + 1 < len(lines) and not lines[i + 1].strip().startswith('|') and lines[i + 1].strip() != '':
                # 表の中で改行がある
                if not lines[i].strip().endswith('|'):
                    issues.append((i + 1, 'newline_in_cell', f'セル内に改行があります（<br>タグに変換が必要）'))
        
        i += 1
    
    return issues

def fix_table_issues(content):
    """
    表の問題を自動修正
    
    Returns:
        str: 修正後のコンテンツ
    """
    lines = content.split('\n')
    fixed_lines = []
    i = 0
    modifications = 0
    
    while i < len(lines):
        line = lines[i]
        line_stripped = line.strip()
        
        # 表のヘッダー行を検出
        if line_stripped.startswith('|') and line_stripped.endswith('|') and line_stripped.count('|') >= 3:
            fixed_lines.append(line)
            
            # 次の行をチェック
            if i + 1 < len(lines):
                next_line = lines[i + 1].strip()
                
                # 区切り線がない場合、追加
                if not re.match(r'^\|[\s\-:]+\|', next_line) or '---' not in next_line:
                    # ヘッダーの列数を数える
                    col_count = line_stripped.count('|') - 1
                    separator = '|' + '---|' * (col_count - 1) + '---|'
                    fixed_lines.append(separator)
                    modifications += 1
                    print(f"  ✓ 区切り線を追加: {col_count}列 (行 {i + 1})")
                    i += 1
                    continue
        
        # 表のセル内の改行を<br>に変換
        if line_stripped.startswith('|') and not re.match(r'^\|[\s\-:]+\|', line_stripped):
            if i + 1 < len(lines) and not lines[i + 1].strip().startswith('|') and lines[i + 1].strip() != '':
                if not line_stripped.endswith('|'):
                    # 次の行を結合して<br>を挿入
                    combined = line.rstrip() + '<br>' + lines[i + 1].strip()
                    fixed_lines.append(combined)
                    modifications += 1
                    print(f"  ✓ セル内改行を<br>に変換 (行 {i + 1})")
                    i += 2
                    continue
        
        fixed_lines.append(line)
        i += 1
    
    if modifications > 0:
        print(f"  → 合計 {modifications} 個の問題を修正")
    
    return '\n'.join(fixed_lines)

def process_file(file_path, fix=False, base_path=None):
    """
    単一のMarkdownファイルを処理
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        issues = find_table_issues(content, file_path.name)
        
        if issues:
            # 相対パスを表示
            if base_path:
                display_path = file_path.relative_to(base_path)
            else:
                display_path = file_path.name
            
            print(f"\n📄 {display_path}")
            for line_num, issue_type, description in issues:
                print(f"  ⚠️  行 {line_num}: {description}")
            
            if fix:
                fixed_content = fix_table_issues(content)
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(fixed_content)
                print(f"  ✅ 修正完了")
                return True
        
        return len(issues) > 0
        
    except Exception as e:
        print(f"❌ エラー: {file_path}: {str(e)}")
        return False

def main():
    parser = argparse.ArgumentParser(
        description='Markdownファイル内の表を検証・修正',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
例:
  # 問題を検出のみ
  python validate_tables.py --path ../content/ja
  
  # 問題を自動修正
  python validate_tables.py --fix --path ../content/ja
  
  # 全言語をチェック
  python validate_tables.py --fix --path ../content
        """
    )
    parser.add_argument('--fix', action='store_true', help='問題を自動修正')
    parser.add_argument('--path', type=str, default='../content', help='コンテンツディレクトリのパス')
    args = parser.parse_args()
    
    # スクリプトのディレクトリからの相対パスを解決
    script_dir = Path(__file__).parent
    content_dir = (script_dir / args.path).resolve()
    
    if not content_dir.exists():
        print(f"❌ ディレクトリが見つかりません: {content_dir}")
        sys.exit(1)
    
    print(f"🔍 表の検証を開始: {content_dir}")
    if args.fix:
        print("🔧 修正モード: 有効")
    else:
        print("👀 検証モード: 問題の検出のみ")
    
    # すべての.mdファイルを検索
    md_files = list(content_dir.rglob('*.md'))
    files_with_issues = 0
    
    for md_file in md_files:
        if process_file(md_file, args.fix, content_dir):
            files_with_issues += 1
    
    print(f"\n{'='*60}")
    print(f"📊 結果: {files_with_issues}/{len(md_files)} ファイルに問題が見つかりました")
    
    if files_with_issues > 0 and not args.fix:
        print("\n💡 修正するには --fix オプションを使用してください")
        print("   例: python validate_tables.py --fix --path ../content/ja")
    elif files_with_issues == 0:
        print("✅ すべての表は正しくフォーマットされています！")

if __name__ == '__main__':
    main()