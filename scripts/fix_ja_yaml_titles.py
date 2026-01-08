#!/usr/bin/env python3
"""
ja.yamlの簡易的なtitle（「〜の用語集ページ」）を
ja_automatic.jsonの正しいdescriptionに置き換えるスクリプト
v2: 正規化マッチング対応
"""

import json
import yaml
import re
from pathlib import Path

def normalize_keyword(keyword):
    """キーワードを正規化（括弧や記号を除去）"""
    # 括弧内の内容を除去
    normalized = re.sub(r'\([^)]*\)', '', keyword)
    # コロンや特殊文字を除去
    normalized = re.sub(r'[:：].*$', '', normalized)
    # 前後の空白を除去
    normalized = normalized.strip()
    return normalized

def load_automatic_titles():
    """ja_automatic.jsonからキーワードとtitleのマッピングを作成"""
    json_path = Path('data/linkbuilding/ja_automatic.json')
    
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # キーワード（小文字）→ titleのマッピング
    keyword_to_title = {}
    for item in data['keywords']:
        keyword = item['Keyword'].lower()
        title = item['Title']
        url = item['URL']
        
        # より良いtitleがあれば更新（優先度が高いものを優先）
        if keyword not in keyword_to_title or len(title) > len(keyword_to_title[keyword]['title']):
            keyword_to_title[keyword] = {
                'title': title,
                'url': url
            }
    
    return keyword_to_title

def fix_yaml_titles():
    """ja.yamlのtitleを修正"""
    yaml_path = Path('data/linkbuilding/ja.yaml')
    
    # YAMLを読み込み
    with open(yaml_path, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    
    # 自動生成されたtitleを読み込み
    automatic_titles = load_automatic_titles()
    
    # 統計
    total_entries = len(data['keywords'])
    updated_count = 0
    not_found_count = 0
    not_found_keywords = []
    
    # 各エントリを処理
    for entry in data['keywords']:
        keyword = entry['keyword']
        current_title = entry.get('title', '')
        
        # 「〜の用語集ページ」で終わるtitleのみ処理
        if current_title.endswith('の用語集ページ'):
            keyword_lower = keyword.lower()
            
            # 1. 完全一致で検索
            if keyword_lower in automatic_titles:
                auto_data = automatic_titles[keyword_lower]
                new_title = auto_data['title']
                
                # titleを更新（長いdescriptionがある場合のみ）
                if len(new_title) > len(current_title):
                    entry['title'] = new_title
                    updated_count += 1
                    print(f"✓ 更新（完全一致）: {keyword}")
                    print(f"  旧: {current_title}")
                    print(f"  新: {new_title[:80]}...")
                    print()
            else:
                # 2. 正規化して検索
                normalized = normalize_keyword(keyword).lower()
                if normalized in automatic_titles:
                    auto_data = automatic_titles[normalized]
                    new_title = auto_data['title']
                    
                    # titleを更新（長いdescriptionがある場合のみ）
                    if len(new_title) > len(current_title):
                        entry['title'] = new_title
                        updated_count += 1
                        print(f"✓ 更新（正規化一致）: {keyword}")
                        print(f"  正規化: {normalized}")
                        print(f"  旧: {current_title}")
                        print(f"  新: {new_title[:80]}...")
                        print()
                else:
                    not_found_count += 1
                    not_found_keywords.append(keyword)
                    print(f"⚠️  見つかりません: {keyword} (正規化: {normalized})")
    
    # 結果を保存
    with open(yaml_path, 'w', encoding='utf-8') as f:
        yaml.dump(data, f, allow_unicode=True, sort_keys=False, default_flow_style=False)
    
    # 統計を表示
    print("\n" + "="*60)
    print("修正完了")
    print("="*60)
    print(f"総エントリ数: {total_entries}")
    print(f"更新したエントリ: {updated_count}")
    print(f"見つからなかったエントリ: {not_found_count}")
    
    if not_found_keywords:
        print("\n見つからなかったキーワード:")
        for kw in not_found_keywords[:10]:
            print(f"  - {kw}")
        if len(not_found_keywords) > 10:
            print(f"  ... 他 {len(not_found_keywords) - 10} 件")

if __name__ == '__main__':
    fix_yaml_titles()
