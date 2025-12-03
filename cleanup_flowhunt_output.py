#!/usr/bin/env python3
"""
FlowHunt Desktop出力のクリーンアップスクリプト（最終版）

削除対象:
1. フロントマター直後～最初の ## 見出しまでの全て（H1, **Category:**, **Definition:** など）
2. ## Table of Contents セクション
3. 本文中の区切り線（---）

保持対象:
- フロントマター（YAML形式に変換、日付を自動挿入）
- 最初の ## 見出し以降の全コンテンツ（これが本文）
"""

import re
from pathlib import Path
from datetime import date


def clean_flowhunt_output(content):
    """
    フロントマター後の不要部分を削除
    """
    # フロントマターと本文を分離
    parts = content.split('---\n', 2)
    
    if len(parts) < 3:
        return content
    
    frontmatter_content = parts[1]
    body = parts[2]
    
    # フロントマターをTOMLからYAMLに変換
    frontmatter_content = re.sub(r'^(\w+)\s*=\s*', r'\1: ', frontmatter_content, flags=re.MULTILINE)
    frontmatter_content = re.sub(r'draft:\s*true', 'draft: false', frontmatter_content)
    
    # 日付フィールドが存在しない場合は追加
    if not re.search(r'^date:', frontmatter_content, flags=re.MULTILINE):
        # 現在の日付を取得
        today = date.today().strftime('%Y-%m-%d')
        
        # draft: の行の前に date: を挿入
        if 'draft:' in frontmatter_content:
            frontmatter_content = re.sub(
                r'(draft:)',
                f'date: {today}\n\\1',
                frontmatter_content
            )
        else:
            frontmatter_content = frontmatter_content.rstrip() + f'\ndate: {today}\n'
    
    frontmatter = f"---\n{frontmatter_content}---\n"
    
    # 最初の ## 見出しを探す
    lines = body.split('\n')
    first_h2_index = -1
    
    for i, line in enumerate(lines):
        if re.match(r'^##\s+', line) and not re.search(r'Table of Contents', line, re.IGNORECASE):
            first_h2_index = i
            break
    
    if first_h2_index == -1:
        return frontmatter + body
    
    # 最初の ## 見出し以降を本文として保持
    body_content = '\n'.join(lines[first_h2_index:])
    
    # Table of Contents を削除
    body_content = re.sub(
        r'##\s+(\*\*)?Table of Contents(\*\*)?\s*\n.+?(?=\n##|\Z)',
        '',
        body_content,
        flags=re.DOTALL | re.IGNORECASE
    )
    
    # 本文中の区切り線（---）を削除
    body_content = re.sub(r'^\s*---\s*$', '', body_content, flags=re.MULTILINE)
    body_content = re.sub(r'\n\s*---\s*\n', '\n\n', body_content)
    
    # 余分な空行を整理
    body_content = re.sub(r'\n{4,}', '\n\n', body_content)
    
    return frontmatter + '\n' + body_content


def process_file(input_file, output_file=None, output_dir=None):
    """ファイルを処理"""
    input_path = Path(input_file)
    
    if not input_path.exists():
        raise FileNotFoundError(f"ファイルが見つかりません: {input_file}")
    
    # 入力ファイルを読み込み
    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # クリーンアップ
    cleaned_content = clean_flowhunt_output(content)
    
    # 出力ファイル名を決定
    if output_file:
        output_path = Path(output_file)
    elif output_dir:
        output_path = Path(output_dir) / input_path.name
    else:
        # デフォルト: 同じディレクトリに /clean サブディレクトリ
        clean_dir = input_path.parent / "clean"
        clean_dir.mkdir(exist_ok=True)
        output_path = clean_dir / input_path.name
    
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    # 出力
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(cleaned_content)
    
    print(f"✅ {input_path.name}")
    print(f"   → {output_path}")
    
    return output_path


def batch_process(directory, output_dir=None):
    """ディレクトリ内の全.mdファイルを処理"""
    dir_path = Path(directory)
    
    if not dir_path.is_dir():
        raise NotADirectoryError(f"ディレクトリが見つかりません: {directory}")
    
    # 除外するファイル名
    exclude_files = {
        'START_HERE.md',
        'QUICKSTART_cleanup.md',
        'README.md',
        '_index.md'
    }
    
    # .mdファイルを取得
    all_md_files = dir_path.glob("*.md")
    md_files = [f for f in all_md_files if f.name not in exclude_files]
    
    if not md_files:
        print(f"⚠️  {directory} に.mdファイルが見つかりません")
        return
    
    # 出力先を決定
    if output_dir:
        out_dir = Path(output_dir)
        out_dir.mkdir(parents=True, exist_ok=True)
        print(f"📁 出力先: {out_dir}\n")
    else:
        clean_dir = dir_path / "clean"
        clean_dir.mkdir(exist_ok=True)
        out_dir = None
        print(f"📁 出力先: {clean_dir}\n")
    
    print(f"🚀 {len(md_files)}個のファイルを処理します...\n")
    
    success_count = 0
    for md_file in md_files:
        try:
            process_file(md_file, output_dir=output_dir)
            success_count += 1
        except Exception as e:
            print(f"❌ エラー ({md_file.name}): {e}")
    
    print(f"\n{'='*50}")
    print(f"✅ 完了: {success_count}/{len(md_files)} 個のファイルを処理しました")
    print(f"{'='*50}")


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("FlowHunt記事クリーンアップツール")
        print()
        print("使い方:")
        print()
        print("  # 単一ファイルを処理（/cleanに出力）")
        print("  python3 cleanup_flowhunt_output.py file.md")
        print()
        print("  # 単一ファイルを指定した場所に出力")
        print("  python3 cleanup_flowhunt_output.py input.md output.md")
        print()
        print("  # ディレクトリ内の全ファイルを処理（/cleanに出力）")
        print("  python3 cleanup_flowhunt_output.py ./content-drafts/en/")
        print()
        print("  # ディレクトリ内の全ファイルを指定した場所に出力")
        print("  python3 cleanup_flowhunt_output.py ./content-drafts/en/ --output ./content/en/glossary/")
        print()
        print("オプション:")
        print("  --output DIR    出力先ディレクトリを指定")
        sys.exit(1)
    
    input_path = sys.argv[1]
    output_path = None
    output_dir = None
    
    # オプション解析
    if '--output' in sys.argv:
        idx = sys.argv.index('--output')
        if idx + 1 < len(sys.argv):
            output_dir = sys.argv[idx + 1]
    elif len(sys.argv) > 2 and not sys.argv[2].startswith('--'):
        output_path = sys.argv[2]
    
    if Path(input_path).is_dir():
        # ディレクトリの場合：一括処理
        batch_process(input_path, output_dir=output_dir)
    else:
        # ファイルの場合：単一ファイル処理
        process_file(input_path, output_file=output_path, output_dir=output_dir)
