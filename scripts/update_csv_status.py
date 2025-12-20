#!/usr/bin/env python3
"""
CSV Status Updater
実ファイルの存在を確認してCSVのステータスを更新
"""

import csv
from pathlib import Path

# パス設定
CSV_PATH = Path("/Users/TM-MBP1/Documents/GitHub/hugo-boilerplate/docs/prioritized_keywords.csv")
EN_DIR = Path("/Users/TM-MBP1/Documents/GitHub/hugo-boilerplate/content/en/glossary")
JA_DIR = Path("/Users/TM-MBP1/Documents/GitHub/hugo-boilerplate/content/ja/glossary")

def update_csv_status():
    """CSVステータスを実ファイル存在状況に基づいて更新"""
    
    # CSVを読み込み
    with open(CSV_PATH, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        rows = list(reader)
    
    # status_en, status_ja列がない場合は追加
    if 'status_en' not in fieldnames:
        fieldnames = list(fieldnames) + ['status_en', 'status_ja']
    
    # 各行のステータスを更新
    updated_count = 0
    for row in rows:
        filename = row.get('filename', '')
        if not filename:
            continue
        
        en_file = EN_DIR / filename
        ja_file = JA_DIR / filename
        
        old_status_en = row.get('status_en', 'pending')
        old_status_ja = row.get('status_ja', 'pending')
        
        # 実ファイルの存在確認
        new_status_en = 'completed' if en_file.exists() else 'pending'
        new_status_ja = 'completed' if ja_file.exists() else 'pending'
        
        row['status_en'] = new_status_en
        row['status_ja'] = new_status_ja
        
        # 変更があった場合カウント
        if old_status_en != new_status_en or old_status_ja != new_status_ja:
            updated_count += 1
            print(f"📝 {filename}: EN {old_status_en}→{new_status_en}, JA {old_status_ja}→{new_status_ja}")
    
    # CSVに書き戻し
    with open(CSV_PATH, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    
    # サマリー表示
    completed_en = sum(1 for r in rows if r.get('status_en') == 'completed')
    completed_ja = sum(1 for r in rows if r.get('status_ja') == 'completed')
    total = len(rows)
    
    print(f"\n{'='*60}")
    print(f"📊 CSV更新完了")
    print(f"{'='*60}")
    print(f"更新件数: {updated_count}")
    print(f"英語版: {completed_en}/{total} 完了")
    print(f"日本語版: {completed_ja}/{total} 完了")
    print(f"{'='*60}\n")
    
    return updated_count

if __name__ == "__main__":
    update_csv_status()
