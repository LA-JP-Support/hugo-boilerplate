#!/usr/bin/env python3
"""
ja.yamlで見つからなかった88個のキーワードを分析し、
ja_automatic.jsonに短縮形で存在するか確認するスクリプト
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

def load_automatic_keywords():
    """ja_automatic.jsonからキーワードのセットを作成"""
    json_path = Path('data/linkbuilding/ja_automatic.json')
    
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # キーワード（小文字）→ データのマッピング
    keyword_map = {}
    for item in data['keywords']:
        keyword_lower = item['Keyword'].lower()
        keyword_map[keyword_lower] = {
            'keyword': item['Keyword'],
            'title': item['Title'],
            'url': item['URL']
        }
    
    return keyword_map

def analyze_missing_keywords():
    """見つからなかったキーワードを分析"""
    yaml_path = Path('data/linkbuilding/ja.yaml')
    
    with open(yaml_path, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    
    automatic_keywords = load_automatic_keywords()
    
    # 見つからなかったキーワードを収集
    missing = []
    for entry in data['keywords']:
        title = entry.get('title', '')
        if title.endswith('の用語集ページ'):
            keyword = entry['keyword']
            missing.append({
                'original': keyword,
                'normalized': normalize_keyword(keyword),
                'url': entry['url']
            })
    
    print(f"見つからなかったキーワード: {len(missing)}個\n")
    
    # 分析結果
    found_normalized = []
    still_missing = []
    
    for item in missing:
        original = item['original']
        normalized = item['normalized']
        
        # 正規化したキーワードで検索
        if normalized.lower() in automatic_keywords:
            auto_data = automatic_keywords[normalized.lower()]
            found_normalized.append({
                'original': original,
                'normalized': normalized,
                'found_as': auto_data['keyword'],
                'title': auto_data['title']
            })
        else:
            still_missing.append(item)
    
    # 結果を表示
    print("=" * 80)
    print(f"正規化後に見つかったキーワード: {len(found_normalized)}個")
    print("=" * 80)
    for item in found_normalized[:10]:
        print(f"\n元のキーワード: {item['original']}")
        print(f"正規化: {item['normalized']}")
        print(f"見つかった形: {item['found_as']}")
        print(f"Title: {item['title'][:80]}...")
    
    if len(found_normalized) > 10:
        print(f"\n... 他 {len(found_normalized) - 10} 件")
    
    print("\n" + "=" * 80)
    print(f"それでも見つからないキーワード: {len(still_missing)}個")
    print("=" * 80)
    for item in still_missing[:20]:
        print(f"- {item['original']} (正規化: {item['normalized']})")
    
    if len(still_missing) > 20:
        print(f"... 他 {len(still_missing) - 20} 件")
    
    return found_normalized, still_missing

if __name__ == '__main__':
    found, missing = analyze_missing_keywords()
