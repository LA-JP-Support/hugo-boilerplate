#!/usr/bin/env python3
"""
Quick CSV Status Update
英語記事作成後にこのスクリプトを実行してCSVを更新
"""

import csv
from pathlib import Path

CSV_PATH = Path("docs/prioritized_keywords.csv")
EN_DIR = Path("content/en/glossary")
JA_DIR = Path("content/ja/glossary")

def quick_update():
    if not CSV_PATH.exists():
        print(f"❌ CSV not found: {CSV_PATH}")
        return
    
    with open(CSV_PATH, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fieldnames = list(reader.fieldnames or [])
        rows = list(reader)
    
    if 'status_en' not in fieldnames:
        fieldnames.append('status_en')
    if 'status_ja' not in fieldnames:
        fieldnames.append('status_ja')
    
    updated = 0
    for row in rows:
        filename = row.get('filename', '')
        if not filename:
            continue
        
        en_exists = (EN_DIR / filename).exists()
        ja_exists = (JA_DIR / filename).exists()
        
        old_en = row.get('status_en', 'pending')
        old_ja = row.get('status_ja', 'pending')
        
        row['status_en'] = 'completed' if en_exists else 'pending'
        row['status_ja'] = 'completed' if ja_exists else 'pending'
        
        if old_en != row['status_en'] or old_ja != row['status_ja']:
            updated += 1
            print(f"✓ {filename}: EN={row['status_en']}, JA={row['status_ja']}")
    
    with open(CSV_PATH, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    
    completed_en = sum(1 for r in rows if r.get('status_en') == 'completed')
    completed_ja = sum(1 for r in rows if r.get('status_ja') == 'completed')
    
    print(f"\n{'='*50}")
    print(f"📊 CSV更新完了")
    print(f"{'='*50}")
    print(f"更新: {updated}件")
    print(f"英語: {completed_en}/{len(rows)} 完了")
    print(f"日本語: {completed_ja}/{len(rows)} 完了")
    print(f"{'='*50}")

if __name__ == "__main__":
    quick_update()
