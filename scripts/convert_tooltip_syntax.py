#!/usr/bin/env python3
"""
Smart Tooltip Syntax Converter
hugo-boilerplate用

用語（説明：詳細な説明文） パターンまたは **用語**（説明：詳細な説明文） パターンを
{{< tooltip text="詳細な説明文" >}}用語{{< /tooltip >}} に変換

使用方法:
    python convert_tooltip_syntax.py --input file.md
    python convert_tooltip_syntax.py --dir content/ja/blog/
    python convert_tooltip_syntax.py --dir content/ja/blog/ --no-backup
"""

import re
import os
import argparse
import shutil
from pathlib import Path
from datetime import datetime


class TooltipConverter:
    """ツールチップ構文変換クラス"""
    
    # マッチパターン: 
    # パターン1: **用語**（説明：詳細な説明文）
    # パターン2: 用語（説明：詳細な説明文）
    PATTERN_BOLD = r'\*\*([^*]+)\*\*[（(]説明[：:]\s*([^)）]+)[)）]'
    PATTERN_NORMAL = r'([^\s（(]+)[（(]説明[：:]\s*([^)）]+)[)）]'
    
    def __init__(self, create_backup=True, verbose=True):
        self.create_backup = create_backup
        self.verbose = verbose
        self.stats = {
            'files_processed': 0,
            'files_modified': 0,
            'tooltips_converted': 0,
            'errors': 0
        }
    
    def convert_text(self, text):
        """
        テキスト内のツールチップパターンをショートコードに変換
        
        Args:
            text (str): 変換対象のテキスト
            
        Returns:
            tuple: (変換後のテキスト, 変換数)
        """
        conversion_count = 0
        
        def replace_match(match):
            nonlocal conversion_count
            term = match.group(1).strip()
            explanation = match.group(2).strip()
            
            # ショートコード形式に変換
            # エスケープが必要な文字の処理
            explanation_escaped = explanation.replace('"', '&quot;')
            
            conversion_count += 1
            return f'{{{{< tooltip text="{explanation_escaped}" >}}}}{term}{{{{< /tooltip >}}}}'
        
        # まず太字パターンを変換
        converted_text = re.sub(self.PATTERN_BOLD, replace_match, text)
        
        # 次に通常パターンを変換
        converted_text = re.sub(self.PATTERN_NORMAL, replace_match, converted_text)
        
        return converted_text, conversion_count
    
    def convert_file(self, file_path):
        """
        単一ファイルを変換
        
        Args:
            file_path (Path): 変換対象ファイルのパス
            
        Returns:
            bool: 変換が成功したかどうか
        """
        try:
            # ファイル読み込み
            with open(file_path, 'r', encoding='utf-8') as f:
                original_content = f.read()
            
            # 変換実行
            converted_content, count = self.convert_text(original_content)
            
            # 変化がない場合はスキップ
            if count == 0:
                if self.verbose:
                    print(f"⏭️  スキップ: {file_path} (変換対象なし)")
                self.stats['files_processed'] += 1
                return True
            
            # バックアップ作成
            if self.create_backup:
                backup_path = file_path.with_suffix(file_path.suffix + '.bak')
                shutil.copy2(file_path, backup_path)
                if self.verbose:
                    print(f"💾 バックアップ作成: {backup_path}")
            
            # 変換後のファイルを保存
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(converted_content)
            
            # 統計更新
            self.stats['files_processed'] += 1
            self.stats['files_modified'] += 1
            self.stats['tooltips_converted'] += count
            
            if self.verbose:
                print(f"✅ 変換完了: {file_path} ({count}個のツールチップ)")
            
            return True
            
        except Exception as e:
            self.stats['errors'] += 1
            print(f"❌ エラー: {file_path} - {str(e)}")
            return False
    
    def convert_directory(self, dir_path, recursive=True):
        """
        ディレクトリ内の全mdファイルを変換
        
        Args:
            dir_path (Path): 変換対象ディレクトリのパス
            recursive (bool): サブディレクトリも処理するか
        """
        pattern = '**/*.md' if recursive else '*.md'
        md_files = list(dir_path.glob(pattern))
        
        if not md_files:
            print(f"⚠️  警告: {dir_path} にmdファイルが見つかりません")
            return
        
        print(f"\n📁 ディレクトリ: {dir_path}")
        print(f"📄 対象ファイル数: {len(md_files)}\n")
        
        for md_file in md_files:
            self.convert_file(md_file)
    
    def print_summary(self):
        """変換結果のサマリーを表示"""
        print("\n" + "="*60)
        print("📊 変換結果サマリー")
        print("="*60)
        print(f"処理したファイル数: {self.stats['files_processed']}")
        print(f"変更されたファイル数: {self.stats['files_modified']}")
        print(f"変換したツールチップ数: {self.stats['tooltips_converted']}")
        print(f"エラー数: {self.stats['errors']}")
        print("="*60 + "\n")


def main():
    """メイン処理"""
    parser = argparse.ArgumentParser(
        description='ツールチップ構文を変換（用語（説明：詳細） → ショートコード形式）',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
使用例:
  # 単一ファイルを変換
  python convert_tooltip_syntax.py --input content/ja/blog/article.md
  
  # ディレクトリ内の全ファイルを変換（再帰的）
  python convert_tooltip_syntax.py --dir content/ja/blog/
  
  # バックアップなしで変換
  python convert_tooltip_syntax.py --dir content/ja/ --no-backup
  
  # サブディレクトリを含めずに変換
  python convert_tooltip_syntax.py --dir content/ja/blog/ --no-recursive
        """
    )
    
    parser.add_argument(
        '--input',
        type=str,
        help='変換する単一のmdファイルパス'
    )
    
    parser.add_argument(
        '--dir',
        type=str,
        help='変換するディレクトリパス（再帰的に処理）'
    )
    
    parser.add_argument(
        '--no-backup',
        action='store_true',
        help='バックアップファイルを作成しない'
    )
    
    parser.add_argument(
        '--no-recursive',
        action='store_true',
        help='サブディレクトリを処理しない'
    )
    
    parser.add_argument(
        '--quiet',
        action='store_true',
        help='詳細な出力を抑制'
    )
    
    args = parser.parse_args()
    
    # 引数チェック
    if not args.input and not args.dir:
        parser.error("--input または --dir のいずれかを指定してください")
    
    # 変換器初期化
    converter = TooltipConverter(
        create_backup=not args.no_backup,
        verbose=not args.quiet
    )
    
    print("\n" + "="*60)
    print("🔧 Smart Tooltip Syntax Converter")
    print("="*60)
    print(f"開始時刻: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"バックアップ: {'なし' if args.no_backup else 'あり'}")
    print("="*60 + "\n")
    
    # 変換実行
    if args.input:
        # 単一ファイル変換
        input_path = Path(args.input)
        if not input_path.exists():
            print(f"❌ エラー: ファイルが見つかりません - {input_path}")
            return 1
        
        converter.convert_file(input_path)
    
    elif args.dir:
        # ディレクトリ変換
        dir_path = Path(args.dir)
        if not dir_path.exists():
            print(f"❌ エラー: ディレクトリが見つかりません - {dir_path}")
            return 1
        
        converter.convert_directory(dir_path, recursive=not args.no_recursive)
    
    # 結果サマリー表示
    converter.print_summary()
    
    return 0 if converter.stats['errors'] == 0 else 1


if __name__ == '__main__':
    exit(main())
