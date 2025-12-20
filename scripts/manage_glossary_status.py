#!/usr/bin/env python3
"""CSVベースのグロッサリー進捗管理"""

import csv
from pathlib import Path

BASE_DIR = Path("/Users/TM-MBP1/Documents/GitHub/hugo-boilerplate")
CSV_FILE = BASE_DIR / "docs/prioritized_keywords.csv"
EN_DIR = BASE_DIR / "content/en/glossary"
JA_DIR = BASE_DIR / "content/ja/glossary"

def update_csv_status():
    """CSVに載っているファイルのみステータス更新"""
    print("=== CSV進捗管理 ===\n")
    
    # CSVを読み込み
    with open(CSV_FILE, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        fieldnames = list(reader.fieldnames) if reader.fieldnames else []
    
    # status列が存在しない場合は追加
    if 'status_en' not in fieldnames:
        print("📝 status列を追加...")
        fieldnames.extend(['status_en', 'status_ja'])
        for row in rows:
            row['status_en'] = 'pending'
            row['status_ja'] = 'pending'
    
    # CSVに載っているファイルのみチェック
    csv_files = set()
    updated_count = 0
    
    for row in rows:
        filename = row.get('filename', '').strip().strip('"')
        if not filename or not filename.endswith('.md'):
            continue
        
        csv_files.add(filename)
        
        # 英語版チェック
        en_exists = (EN_DIR / filename).exists()
        old_en = row.get('status_en', 'pending')
        new_en = 'completed' if en_exists else 'pending'
        
        # 日本語版チェック
        ja_exists = (JA_DIR / filename).exists()
        old_ja = row.get('status_ja', 'pending')
        new_ja = 'completed' if ja_exists else 'pending'
        
        # 更新
        if old_en != new_en or old_ja != new_ja:
            row['status_en'] = new_en
            row['status_ja'] = new_ja
            updated_count += 1
            
            status = []
            if old_en != new_en:
                status.append(f"EN: {old_en}→{new_en}")
            if old_ja != new_ja:
                status.append(f"JA: {old_ja}→{new_ja}")
            print(f"✓ {filename}: {', '.join(status)}")
    
    # CSVに書き戻し
    with open(CSV_FILE, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    
    print(f"\n✅ CSV更新完了: {updated_count}件変更")
    
    # 統計表示
    total = len([r for r in rows if r.get('filename', '').strip().strip('"').endswith('.md')])
    en_completed = sum(1 for r in rows if r.get('status_en') == 'completed')
    ja_completed = sum(1 for r in rows if r.get('status_ja') == 'completed')
    en_pending = total - en_completed
    ja_pending = total - ja_completed
    
    print(f"\n📊 CSV内の進捗状況:")
    print(f"  英語版: {en_completed}/{total} 完了 ({en_pending}件未作成)")
    print(f"  日本語版: {ja_completed}/{total} 完了 ({ja_pending}件未作成)")
    
    # CSVに載っていない既存ファイルを表示（参考情報）
    print(f"\n📋 参考情報: CSVに載っていない既存ファイル")
    all_en_files = set(f.name for f in EN_DIR.glob("*.md") if f.name != "_index.md")
    non_csv_files = all_en_files - csv_files
    
    if non_csv_files:
        print(f"  {len(non_csv_files)}件:")
        for f in sorted(list(non_csv_files))[:10]:
            print(f"    - {f}")
        if len(non_csv_files) > 10:
            print(f"    ... 他{len(non_csv_files)-10}件")
    else:
        print("  なし（全ファイルがCSVに登録済み）")
    
    return rows

def get_pending_files(n=10):
    """CSVから未作成ファイルを取得"""
    with open(CSV_FILE, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        pending = []
        
        for row in reader:
            if row.get('status_en') == 'pending':
                filename = row.get('filename', '').strip().strip('"')
                if filename and filename.endswith('.md'):
                    pending.append(filename)
                    if len(pending) >= n:
                        break
    
    return pending

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "--get-pending":
        n = int(sys.argv[2]) if len(sys.argv) > 2 else 10
        pending = get_pending_files(n)
        print(f"\n🎯 次に作成すべき{len(pending)}件:")
        for f in pending:
            print(f"  - {f}")
    else:
        # ステータス更新
        update_csv_status()
        
        # 次の10件を表示
        print("\n" + "="*50)
        pending = get_pending_files(10)
        print(f"\n🎯 次に作成すべき{len(pending)}件:")
        for f in pending:
            keyword = f.replace('.md', '').replace('-', ' ')
            print(f"  - {f:40s} ({keyword})")
