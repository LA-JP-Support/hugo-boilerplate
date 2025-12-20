#!/usr/bin/env python3
"""
Parallel Translation Script
並列翻訳スクリプト
"""

import csv
from pathlib import Path
import subprocess
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

def translate_file(filename: str, en_dir: Path, ja_dir: Path) -> tuple:
    """1ファイルを翻訳"""
    try:
        result = subprocess.run(
            ["python3", "scripts/translate_glossary_en_to_ja.py", "--one-file", filename],
            capture_output=True,
            timeout=180,
            text=True
        )
        
        # 日本語ファイルが作成されたか確認
        ja_file = ja_dir / filename
        if ja_file.exists():
            return (filename, True, None)
        else:
            return (filename, False, "ファイル未作成")
            
    except subprocess.TimeoutExpired:
        return (filename, False, "Timeout")
    except Exception as e:
        return (filename, False, str(e))

def main():
    csv_path = Path("docs/prioritized_keywords.csv")
    en_dir = Path("content/en/glossary")
    ja_dir = Path("content/ja/glossary")
    
    print("📋 CSVから未翻訳ファイルを取得中...")
    
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    
    to_translate = []
    for row in rows:
        filename = row.get('filename', '')
        if not filename:
            continue
        
        en_file = en_dir / filename
        ja_file = ja_dir / filename
        
        if en_file.exists() and not ja_file.exists():
            to_translate.append(filename)
    
    print(f"✅ 未翻訳ファイル: {len(to_translate)}件")
    
    if not to_translate:
        print("✅ 全てのファイルが翻訳済みです")
        return
    
    limit = min(100, len(to_translate))
    files_to_process = to_translate[:limit]
    
    print(f"📝 今回翻訳: {limit}件")
    
    # 並列数の設定
    max_workers = 5  # 5並列（調整可能）
    
    print(f"\n{'='*70}")
    print(f"🚀 並列翻訳開始（{max_workers}並列）")
    print(f"{'='*70}")
    print(f"予想時間: {limit / max_workers * 3 / 60:.1f}分")
    print(f"{'='*70}\n")
    
    success = 0
    failed = 0
    failed_list = []
    completed = 0
    
    start_time = time.time()
    
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        # 全ファイルを並列投入
        futures = {
            executor.submit(translate_file, filename, en_dir, ja_dir): filename
            for filename in files_to_process
        }
        
        # 完了したものから処理
        for future in as_completed(futures):
            filename = futures[future]
            completed += 1
            
            file, ok, error = future.result()
            
            if ok:
                success += 1
                print(f"✅ {completed:3d}/{limit}: {file}")
            else:
                failed += 1
                failed_list.append((file, error))
                print(f"❌ {completed:3d}/{limit}: {file} - {error}")
            
            if completed % 10 == 0:
                elapsed = (time.time() - start_time) / 60
                remaining = (limit - completed) / completed * elapsed if completed > 0 else 0
                print(f"\n📊 進捗: {completed}/{limit} ({completed*100//limit}%)")
                print(f"   成功:{success} 失敗:{failed}")
                print(f"   経過:{elapsed:.1f}分 残り:{remaining:.1f}分（予測）\n")
    
    total_time = (time.time() - start_time) / 60
    
    print(f"\n{'='*70}")
    print(f"📊 翻訳完了")
    print(f"{'='*70}")
    print(f"成功: {success}/{limit} ({success*100//limit if limit > 0 else 0}%)")
    print(f"失敗: {failed}/{limit}")
    print(f"総時間: {total_time:.1f}分")
    print(f"{'='*70}")
    
    if failed_list:
        print(f"\n⚠️  失敗したファイル: {len(failed_list)}件")
        for f, err in failed_list[:10]:
            print(f"  - {f}: {err}")
    
    remaining_count = len(to_translate) - limit
    if remaining_count > 0:
        print(f"\n📋 残りの未翻訳ファイル: {remaining_count}件")
        print(f"   次回も同じコマンドを実行すれば続きから処理されます")
    
    print(f"\n✅ 翻訳処理完了！")

if __name__ == "__main__":
    main()
