#!/usr/bin/env python3
"""
Analyze keyword sources and compare EN/JA discrepancies.

This script provides detailed statistics about keyword dictionaries,
denylist terms, and helps identify why EN/JA keyword counts differ.
"""

import json
import yaml
import csv
from pathlib import Path
from collections import defaultdict


def analyze_csv_database(csv_path: Path) -> dict:
    """Analyze link_database CSV file."""
    stats = {
        'total_entries': 0,
        'unique_keywords': set(),
        'unique_urls': set(),
        'exact_match_count': 0,
        'priority_distribution': defaultdict(int),
    }
    
    if not csv_path.exists():
        return stats
    
    with csv_path.open('r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            stats['total_entries'] += 1
            keyword = row.get('keyword', '').strip()
            url = row.get('url', '').strip()
            exact = row.get('exact_match', 'false').strip().lower() == 'true'
            priority = int(row.get('priority', '1000'))
            
            if keyword:
                stats['unique_keywords'].add(keyword.lower())
            if url:
                stats['unique_urls'].add(url)
            if exact:
                stats['exact_match_count'] += 1
            
            stats['priority_distribution'][priority // 100 * 100] += 1
    
    return stats


def analyze_json_automatic(json_path: Path) -> dict:
    """Analyze automatic JSON file."""
    stats = {
        'total_entries': 0,
        'unique_keywords': set(),
        'unique_urls': set(),
        'exact_match_count': 0,
    }
    
    if not json_path.exists():
        return stats
    
    with json_path.open('r', encoding='utf-8') as f:
        data = json.load(f)
        
        # Handle both array format and object with 'keywords' key
        if isinstance(data, dict) and 'keywords' in data:
            data = data['keywords']
        
        stats['total_entries'] = len(data)
        for entry in data:
            keyword = entry.get('Keyword', '').strip()
            url = entry.get('URL', '').strip()
            exact = entry.get('Exact', False)
            
            if keyword:
                stats['unique_keywords'].add(keyword.lower())
            if url:
                stats['unique_urls'].add(url)
            if exact:
                stats['exact_match_count'] += 1
    
    return stats


def analyze_yaml_manual(yaml_path: Path) -> dict:
    """Analyze manual YAML file."""
    stats = {
        'total_entries': 0,
        'unique_keywords': set(),
        'unique_urls': set(),
        'exact_match_count': 0,
    }
    
    if not yaml_path.exists():
        return stats
    
    with yaml_path.open('r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
        if not data:
            return stats
        
        # Handle both array format and object with 'keywords' key
        if isinstance(data, dict) and 'keywords' in data:
            data = data['keywords']
        
        stats['total_entries'] = len(data)
        for entry in data:
            keyword = entry.get('keyword', '').strip()
            url = entry.get('url', '').strip()
            exact = entry.get('exact', False)
            
            if keyword:
                stats['unique_keywords'].add(keyword.lower())
            if url:
                stats['unique_urls'].add(url)
            if exact:
                stats['exact_match_count'] += 1
    
    return stats


def analyze_denylist(csv_path: Path) -> dict:
    """Analyze danger_terms CSV file."""
    stats = {
        'total_terms': 0,
        'unique_terms': set(),
    }
    
    if not csv_path.exists():
        return stats
    
    with csv_path.open('r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            stats['total_terms'] += 1
            term = (row.get('normalized') or row.get('keyword') or '').strip()
            if term:
                stats['unique_terms'].add(term.lower())
    
    return stats


def main():
    print("=" * 70)
    print("KEYWORD SOURCE ANALYSIS - EN vs JA Comparison")
    print("=" * 70)
    
    # Analyze CSV databases (used by add_links_from_database.py for Markdown)
    print("\n📊 CSV Databases (databases/link_database_*.csv)")
    print("   Used by: add_links_from_database.py (Markdown-based linking)")
    print("-" * 70)
    
    en_csv = analyze_csv_database(Path('databases/link_database_en.csv'))
    ja_csv = analyze_csv_database(Path('databases/link_database_ja.csv'))
    
    print(f"  EN: {en_csv['total_entries']:5} entries, {len(en_csv['unique_keywords']):5} unique keywords, {len(en_csv['unique_urls']):5} unique URLs")
    print(f"  JA: {ja_csv['total_entries']:5} entries, {len(ja_csv['unique_keywords']):5} unique keywords, {len(ja_csv['unique_urls']):5} unique URLs")
    print(f"  Δ:  {en_csv['total_entries'] - ja_csv['total_entries']:+5} entries, {len(en_csv['unique_keywords']) - len(ja_csv['unique_keywords']):+5} keywords, {len(en_csv['unique_urls']) - len(ja_csv['unique_urls']):+5} URLs")
    
    # Analyze JSON automatic (used by linkbuilding.py for HTML)
    print("\n📊 Automatic JSON (data/linkbuilding/*_automatic.json)")
    print("   Used by: linkbuilding.py (HTML post-processing)")
    print("-" * 70)
    
    en_auto = analyze_json_automatic(Path('data/linkbuilding/en_automatic.json'))
    ja_auto = analyze_json_automatic(Path('data/linkbuilding/ja_automatic.json'))
    
    print(f"  EN: {en_auto['total_entries']:5} entries, {len(en_auto['unique_keywords']):5} unique keywords, {len(en_auto['unique_urls']):5} unique URLs")
    print(f"  JA: {ja_auto['total_entries']:5} entries, {len(ja_auto['unique_keywords']):5} unique keywords, {len(ja_auto['unique_urls']):5} unique URLs")
    print(f"  Δ:  {en_auto['total_entries'] - ja_auto['total_entries']:+5} entries, {len(en_auto['unique_keywords']) - len(ja_auto['unique_keywords']):+5} keywords, {len(en_auto['unique_urls']) - len(ja_auto['unique_urls']):+5} URLs")
    
    # Analyze YAML manual (used by linkbuilding.py for HTML)
    print("\n📊 Manual YAML (data/linkbuilding/*.yaml)")
    print("   Used by: linkbuilding.py (HTML post-processing)")
    print("-" * 70)
    
    en_manual = analyze_yaml_manual(Path('data/linkbuilding/en.yaml'))
    ja_manual = analyze_yaml_manual(Path('data/linkbuilding/ja.yaml'))
    
    print(f"  EN: {en_manual['total_entries']:5} entries, {len(en_manual['unique_keywords']):5} unique keywords, {len(en_manual['unique_urls']):5} unique URLs")
    print(f"  JA: {ja_manual['total_entries']:5} entries, {len(ja_manual['unique_keywords']):5} unique keywords, {len(ja_manual['unique_urls']):5} unique URLs")
    print(f"  Δ:  {en_manual['total_entries'] - ja_manual['total_entries']:+5} entries, {len(en_manual['unique_keywords']) - len(ja_manual['unique_keywords']):+5} keywords, {len(en_manual['unique_urls']) - len(ja_manual['unique_urls']):+5} URLs")
    
    # Analyze denylists
    print("\n🚫 Denylist (databases/danger_terms_*.csv)")
    print("   Used by: add_links_from_database.py (Markdown), linkbuilding.py (HTML, new)")
    print("-" * 70)
    
    en_deny = analyze_denylist(Path('databases/danger_terms_en.csv'))
    ja_deny = analyze_denylist(Path('databases/danger_terms_ja.csv'))
    
    print(f"  EN: {en_deny['total_terms']:5} terms, {len(en_deny['unique_terms']):5} unique")
    print(f"  JA: {ja_deny['total_terms']:5} terms, {len(ja_deny['unique_terms']):5} unique")
    print(f"  Δ:  {en_deny['total_terms'] - ja_deny['total_terms']:+5} terms, {len(en_deny['unique_terms']) - len(ja_deny['unique_terms']):+5} unique")
    
    # Summary for HTML post-processing (current workflow)
    print("\n" + "=" * 70)
    print("🎯 SUMMARY: HTML Post-Processing Workflow (linkbuilding.py)")
    print("=" * 70)
    
    en_total = en_auto['total_entries'] + en_manual['total_entries']
    ja_total = ja_auto['total_entries'] + ja_manual['total_entries']
    
    print(f"  EN total keywords: {en_total:5} (automatic: {en_auto['total_entries']}, manual: {en_manual['total_entries']})")
    print(f"  JA total keywords: {ja_total:5} (automatic: {ja_auto['total_entries']}, manual: {ja_manual['total_entries']})")
    print(f"  Difference:        {en_total - ja_total:+5}")
    
    print(f"\n  EN denylist terms: {len(en_deny['unique_terms']):5}")
    print(f"  JA denylist terms: {len(ja_deny['unique_terms']):5}")
    print(f"  Difference:        {len(en_deny['unique_terms']) - len(ja_deny['unique_terms']):+5}")
    
    print("\n💡 Notes:")
    print("  - CSV databases have ~1600 entries but automatic JSON only has 1-2")
    print("  - This suggests automatic JSON needs regeneration from frontmatter")
    print("  - Use extract_automatic_links.py to regenerate *_automatic.json")
    print("  - Use generate_linkbuilding_yaml_from_glossary.py to regenerate *.yaml")
    print("  - Denylist is now integrated into linkbuilding.py (auto-detected)")
    print("=" * 70)


if __name__ == '__main__':
    main()
