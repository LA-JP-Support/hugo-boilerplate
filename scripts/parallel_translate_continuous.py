#!/usr/bin/env python3
"""並行翻訳スクリプト - 生成された記事を追跡して翻訳"""

import csv
from pathlib import Path
import subprocess
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

def translate_file(filename: str, en_dir: Path, ja_dir: Path) -> tuple:
    try:
        result = subprocess.run(
            ["python3", "scripts/translate_glossary_en_to_ja.py", "--one-file", filename],
            capture_output=True,
            timeout=240,
            text=True
        )
        
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
    
    print("📋 並行翻訳モード起動...")
    print("   英語記事の生成を追跡しながら翻訳します\n")
    
    processed_total = 0
    round_num = 0
    
    while True:
        round_num += 1
        
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
        
        if not to_translate:
            print(f"\n✅ 全て翻訳完了！累計処理: {processed_total}件")
            break
        
        files_to_process = to_translate[:100]
        
        print(f"\n{'='*70}")
        print(f"🚀 ラウンド{round_num}: {len(files_to_process)}件を翻訳（3並列）")
        print(f"{'='*70}\n")
        
        success = 0
        failed = 0
        failed_list = []
        
        start_time = time.time()
        
        with ThreadPoolExecutor(max_workers=3) as executor:
            futures = {
                executor.submit(translate_file, filename, en_dir, ja_dir): filename
                for filename in files_to_process
            }
            
            completed = 0
            for future in as_completed(futures):
                filename = futures[future]
                completed += 1
                
                file, ok, error = future.result()
                
                if ok:
                    success += 1
                    print(f"✅ {completed:3d}/{len(files_to_process)}: {file}")
                else:
                    failed += 1
                    failed_list.append((file, error))
                    print(f"❌ {completed:3d}/{len(files_to_process)}: {file}")
                
                if completed % 10 == 0:
                    remaining = len(to_translate) - completed
                    print(f"\n📊 進捗: {completed}/{len(files_to_process)} - 成功:{success} 失敗:{failed}")
                    print(f"   残り未翻訳: {remaining}件\n")
        
        processed_total += success
        
        print(f"\n{'='*70}")
        print(f"📊 ラウンド{round_num}完了")
        print(f"{'='*70}")
        print(f"成功: {success}/{len(files_to_process)}")
        print(f"失敗: {failed}/{len(files_to_process)}")
        print(f"累計処理: {processed_total}件")
        print(f"残り未翻訳: {len(to_translate) - len(files_to_process)}件")
        print(f"{'='*70}")
        
        if failed_list:
            print(f"\n⚠️  失敗: {len(failed_list)}件")
        
        if len(to_translate) <= len(files_to_process):
            break
        
        print(f"\n⏳ 10秒待機して次のラウンドへ...")
        time.sleep(10)
    
    print(f"\n🎉 並行翻訳完了！総処理: {processed_total}件")

if __name__ == "__main__":
    main()
