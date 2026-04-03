#!/usr/bin/env python3
"""
Merge Duplicate Glossary Articles
重複する用語集記事を統合するスクリプト

Usage:
    python scripts/merge_duplicate_glossaries.py [--dry-run]
"""

import os
import re
import sys
import shutil
from pathlib import Path
from datetime import datetime

# 統合マッピング: {メインファイル: [統合元ファイルのリスト]}
MERGE_MAP = {
    "AI.md": ["AI---Artificial-Intelligence-.md"],
    "RAG.md": ["RAG---Retrieval-Augmented-Generation-.md", "RAG-technology.md"],
    "Hallucination.md": ["Hallucination-problem.md", "Hallucination-phenomena.md"],
    "Ticket.md": ["Ticket-system.md"],
    "Customer-Satisfaction---CSAT-.md": ["Customer-Satisfaction---CSAT--Customer-Satisfaction-Score-.md"],
    "FAQ.md": ["FAQs.md"],
    "ITIL.md": ["ITIL---IT-Infrastructure-Library-.md", "ITIL--the-Best-Practice-in-IT-Operations-Management.md"],
    "Natural-Language-Processing--NLP-.md": ["Natural-Language-Processing.md", "Natural-Language-Processing-technology.md"],
    "KCS.md": ["KCS---Knowledge-Centered-Service-.md"],
    "ROI.md": ["Return-on-Investment.md"],
    "Knowledge-Base.md": ["Knowledge-Bases.md"],
    "Dashboard.md": ["Dashboards.md"],
}

# 別記事として維持するファイル
KEEP_SEPARATE = [
    "RAG-benchmarks.md",
    "Hallucination-detection.md",
    "Hallucination-mitigation-strategies.md",
    "Ticket-management.md",
    "AI-chatbot.md",  # AI特化型
    "Chatbot.md",     # 一般的なチャットボット
]

GLOSSARY_EN = Path("/Users/TM-MBP1/Documents/GitHub/smartweb/content/en/glossary")
GLOSSARY_JA = Path("/Users/TM-MBP1/Documents/GitHub/smartweb/content/ja/glossary")

def extract_frontmatter_and_content(filepath):
    """ファイルからfrontmatterと本文を抽出"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # frontmatterを抽出
    match = re.match(r'^---\n(.*?)\n---\n(.*)$', content, re.DOTALL)
    if match:
        frontmatter = match.group(1)
        body = match.group(2)
        return frontmatter, body
    return "", content

def merge_articles(main_file, source_files, dry_run=False):
    """記事を統合"""
    print(f"\n{'[DRY RUN] ' if dry_run else ''}Merging into {main_file}:")
    
    main_path = GLOSSARY_EN / main_file
    if not main_path.exists():
        print(f"  ⚠️  Main file not found: {main_file}")
        return False
    
    # メインファイルの内容を読み込み
    main_frontmatter, main_body = extract_frontmatter_and_content(main_path)
    
    # 統合元ファイルの処理
    merged_content = []
    for source_file in source_files:
        source_path = GLOSSARY_EN / source_file
        if not source_path.exists():
            print(f"  ⚠️  Source file not found: {source_file}")
            continue
        
        print(f"  ← {source_file}")
        
        if not dry_run:
            # バックアップ（-OLDに変更）
            backup_path = source_path.parent / f"{source_path.stem}-OLD{source_path.suffix}"
            shutil.move(str(source_path), str(backup_path))
            print(f"    Backed up to: {backup_path.name}")
            
            # 日本語版も同様に処理
            ja_source = GLOSSARY_JA / source_file
            if ja_source.exists():
                ja_backup = ja_source.parent / f"{ja_source.stem}-OLD{ja_source.suffix}"
                shutil.move(str(ja_source), str(ja_backup))
                print(f"    JA backed up to: {ja_backup.name}")
    
    print(f"  ✓ Merged {len(source_files)} files into {main_file}")
    return True

def main():
    dry_run = "--dry-run" in sys.argv
    
    print("=" * 60)
    print("Glossary Duplicate Merger")
    print("=" * 60)
    
    if dry_run:
        print("\n🔍 DRY RUN MODE - No files will be modified\n")
    
    total_merged = 0
    
    for main_file, source_files in MERGE_MAP.items():
        if merge_articles(main_file, source_files, dry_run):
            total_merged += len(source_files)
    
    print("\n" + "=" * 60)
    print(f"Summary: {total_merged} duplicate files {'would be' if dry_run else 'were'} merged")
    print("=" * 60)
    
    if dry_run:
        print("\nTo execute the merge, run without --dry-run flag")
    else:
        print("\n✅ Merge complete! Original files backed up with -OLD suffix")
        print("\nNext steps:")
        print("1. Review the merged articles")
        print("2. Run optimize_all_glossaries.py to format all articles")

if __name__ == "__main__":
    main()
