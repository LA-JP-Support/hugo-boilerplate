#!/usr/bin/env python3
"""
内部リンクチェックスクリプト

Hugo生成後のHTMLファイルに内部リンク（data-lb="1"）が正しく追加されているかをチェックします。

使用方法:
    python3 scripts/check_internal_links.py --public-dir public
    python3 scripts/check_internal_links.py --public-dir public --language ja
    python3 scripts/check_internal_links.py --public-dir public --min-links 5
"""

import argparse
from pathlib import Path
from bs4 import BeautifulSoup
import sys


def check_internal_links(public_dir, language=None, min_links=0, verbose=False):
    """
    HTMLファイルの内部リンクをチェック
    
    Args:
        public_dir: publicディレクトリのパス
        language: チェックする言語（None=全言語）
        min_links: 最小リンク数の閾値
        verbose: 詳細出力
    
    Returns:
        dict: チェック結果
    """
    public_path = Path(public_dir)
    
    if not public_path.exists():
        print(f"❌ エラー: {public_dir} が見つかりません")
        return None
    
    # 言語ごとのディレクトリを決定
    if language:
        search_dirs = [public_path / language]
    else:
        # 主要言語のみチェック（en, ja）
        search_dirs = [public_path / 'en', public_path / 'ja', public_path]
    
    results = {
        'total_files': 0,
        'files_with_links': 0,
        'files_without_links': [],
        'total_links': 0,
        'files_below_threshold': []
    }
    
    for search_dir in search_dirs:
        if not search_dir.exists():
            continue
        
        # HTMLファイルを検索
        html_files = list(search_dir.rglob('*.html'))
        
        for html_file in html_files:
            # index.htmlのみをチェック（ページコンテンツ）
            if html_file.name != 'index.html':
                continue
            
            results['total_files'] += 1
            
            try:
                with open(html_file, 'r', encoding='utf-8') as f:
                    soup = BeautifulSoup(f.read(), 'html.parser')
                
                # data-lb="1"属性を持つリンクを検索
                internal_links = soup.find_all('a', {'data-lb': '1'})
                link_count = len(internal_links)
                
                results['total_links'] += link_count
                
                if link_count > 0:
                    results['files_with_links'] += 1
                else:
                    rel_path = html_file.relative_to(public_path)
                    results['files_without_links'].append(str(rel_path))
                
                # 閾値チェック
                if 0 < link_count < min_links:
                    rel_path = html_file.relative_to(public_path)
                    results['files_below_threshold'].append({
                        'path': str(rel_path),
                        'count': link_count
                    })
                
                if verbose and link_count > 0:
                    rel_path = html_file.relative_to(public_path)
                    print(f"✓ {rel_path}: {link_count}件")
                
            except Exception as e:
                print(f"⚠️  エラー: {html_file} - {e}")
    
    return results


def print_report(results, min_links=0):
    """チェック結果のレポートを出力"""
    print("\n" + "=" * 60)
    print("📊 内部リンクチェック結果")
    print("=" * 60)
    
    print(f"\n✅ 統計:")
    print(f"  総ファイル数: {results['total_files']}件")
    print(f"  内部リンクあり: {results['files_with_links']}件")
    print(f"  内部リンクなし: {len(results['files_without_links'])}件")
    print(f"  総リンク数: {results['total_links']:,}件")
    
    if results['total_files'] > 0:
        avg_links = results['total_links'] / results['total_files']
        print(f"  平均リンク数: {avg_links:.1f}件/ファイル")
    
    # 内部リンクがないファイル
    if results['files_without_links']:
        print(f"\n❌ 内部リンクが0件のファイル ({len(results['files_without_links'])}件):")
        for path in results['files_without_links'][:20]:
            print(f"  - {path}")
        if len(results['files_without_links']) > 20:
            print(f"  ... 他{len(results['files_without_links']) - 20}件")
    
    # 閾値未満のファイル
    if min_links > 0 and results['files_below_threshold']:
        print(f"\n⚠️  内部リンクが{min_links}件未満のファイル ({len(results['files_below_threshold'])}件):")
        for item in results['files_below_threshold'][:20]:
            print(f"  - {item['path']}: {item['count']}件")
        if len(results['files_below_threshold']) > 20:
            print(f"  ... 他{len(results['files_below_threshold']) - 20}件")
    
    print("\n" + "=" * 60)
    
    # 終了コード
    if results['files_without_links']:
        return 1
    return 0


def main():
    parser = argparse.ArgumentParser(
        description='Hugo生成後のHTMLファイルの内部リンクをチェック'
    )
    parser.add_argument(
        '--public-dir',
        default='public',
        help='publicディレクトリのパス（デフォルト: public）'
    )
    parser.add_argument(
        '--language',
        choices=['en', 'ja'],
        help='チェックする言語（指定しない場合は全言語）'
    )
    parser.add_argument(
        '--min-links',
        type=int,
        default=0,
        help='最小リンク数の閾値（この数未満のファイルを警告）'
    )
    parser.add_argument(
        '--verbose',
        action='store_true',
        help='詳細出力'
    )
    
    args = parser.parse_args()
    
    results = check_internal_links(
        args.public_dir,
        language=args.language,
        min_links=args.min_links,
        verbose=args.verbose
    )
    
    if results is None:
        sys.exit(1)
    
    exit_code = print_report(results, min_links=args.min_links)
    sys.exit(exit_code)


if __name__ == '__main__':
    main()
