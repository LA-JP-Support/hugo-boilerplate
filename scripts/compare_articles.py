#!/usr/bin/env python3
"""
Article Quality Comparison Tool
対話型 vs API自動化の記事品質を比較
"""

import re
from pathlib import Path
from typing import Dict

def parse_markdown(content: str) -> Dict:
    """マークダウンを解析"""
    
    # フロントマター抽出
    fm_match = re.match(r'^---\n(.*?)\n---\n(.*)$', content, re.DOTALL)
    if fm_match:
        frontmatter = fm_match.group(1)
        body = fm_match.group(2)
    else:
        frontmatter = ""
        body = content
    
    # 語数カウント
    words = len(re.findall(r'\b\w+\b', body))
    
    # 見出し抽出
    headings = re.findall(r'^(#{1,6})\s+(.+)$', body, re.MULTILINE)
    h2_count = sum(1 for h in headings if h[0] == '##')
    h3_count = sum(1 for h in headings if h[0] == '###')
    
    # セクション抽出
    sections = [h[1].strip() for h in headings if h[0] == '##']
    
    # References確認
    has_references = bool(re.search(r'^## References', body, re.MULTILINE))
    ref_count = len(re.findall(r'^\- \[.*?\]\(https?://.*?\)', body, re.MULTILINE))
    
    # 箇条書きカウント
    bullet_count = len(re.findall(r'^\s*[-*]\s+', body, re.MULTILINE))
    
    # 表カウント
    table_count = len(re.findall(r'^\|.*\|$', body, re.MULTILINE))
    
    # コードブロック
    code_blocks = len(re.findall(r'```', body))
    
    return {
        'word_count': words,
        'h2_count': h2_count,
        'h3_count': h3_count,
        'sections': sections,
        'has_references': has_references,
        'reference_count': ref_count,
        'bullet_count': bullet_count,
        'table_count': table_count,
        'code_blocks': code_blocks,
    }

def compare_articles(file1: Path, file2: Path) -> Dict:
    """2つの記事を比較"""
    
    if not file1.exists():
        return {'error': f'{file1} not found'}
    if not file2.exists():
        return {'error': f'{file2} not found'}
    
    content1 = file1.read_text(encoding='utf-8')
    content2 = file2.read_text(encoding='utf-8')
    
    stats1 = parse_markdown(content1)
    stats2 = parse_markdown(content2)
    
    # 差分計算
    diff = {
        'word_count_diff': stats2['word_count'] - stats1['word_count'],
        'word_count_pct': ((stats2['word_count'] - stats1['word_count']) / stats1['word_count'] * 100) if stats1['word_count'] > 0 else 0,
        'h2_diff': stats2['h2_count'] - stats1['h2_count'],
        'h3_diff': stats2['h3_count'] - stats1['h3_count'],
        'bullet_diff': stats2['bullet_count'] - stats1['bullet_count'],
        'table_diff': stats2['table_count'] - stats1['table_count'],
        'reference_diff': stats2['reference_count'] - stats1['reference_count'],
    }
    
    # セクション比較
    sections1_set = set(stats1['sections'])
    sections2_set = set(stats2['sections'])
    
    missing_sections = sections1_set - sections2_set
    extra_sections = sections2_set - sections1_set
    
    # 構造的類似度
    structural_similarity = (
        (1.0 if abs(diff['word_count_pct']) < 10 else 0.5) +
        (1.0 if diff['h2_diff'] == 0 else 0.5) +
        (1.0 if stats1['has_references'] == stats2['has_references'] else 0.0) +
        (1.0 if len(missing_sections) == 0 else 0.5)
    ) / 4.0 * 100
    
    return {
        'file1': file1.name,
        'file2': file2.name,
        'stats1': stats1,
        'stats2': stats2,
        'diff': diff,
        'missing_sections': list(missing_sections),
        'extra_sections': list(extra_sections),
        'structural_similarity': structural_similarity,
    }

def print_comparison(result: Dict):
    """比較結果を表示"""
    
    if 'error' in result:
        print(f"❌ エラー: {result['error']}")
        return
    
    print(f"\n{'='*70}")
    print(f"📊 記事品質比較: {result['file1']} vs {result['file2']}")
    print(f"{'='*70}")
    
    stats1 = result['stats1']
    stats2 = result['stats2']
    diff = result['diff']
    
    print(f"\n【語数】")
    print(f"  対話型: {stats1['word_count']:,} 語")
    print(f"  API版:  {stats2['word_count']:,} 語")
    print(f"  差分:   {diff['word_count_diff']:+,} 語 ({diff['word_count_pct']:+.1f}%)")
    
    print(f"\n【構造】")
    print(f"  H2見出し: {stats1['h2_count']} → {stats2['h2_count']} ({diff['h2_diff']:+d})")
    print(f"  H3見出し: {stats1['h3_count']} → {stats2['h3_count']} ({diff['h3_diff']:+d})")
    print(f"  箇条書き: {stats1['bullet_count']} → {stats2['bullet_count']} ({diff['bullet_diff']:+d})")
    print(f"  表:       {stats1['table_count']} → {stats2['table_count']} ({diff['table_diff']:+d})")
    
    print(f"\n【References】")
    print(f"  対話型: {'✅' if stats1['has_references'] else '❌'} ({stats1['reference_count']}件)")
    print(f"  API版:  {'✅' if stats2['has_references'] else '❌'} ({stats2['reference_count']}件)")
    print(f"  差分:   {diff['reference_diff']:+d}件")
    
    print(f"\n【セクション比較】")
    if result['missing_sections']:
        print(f"  ⚠️  API版に欠けているセクション:")
        for sec in result['missing_sections']:
            print(f"    - {sec}")
    
    if result['extra_sections']:
        print(f"  ➕ API版にのみあるセクション:")
        for sec in result['extra_sections']:
            print(f"    - {sec}")
    
    if not result['missing_sections'] and not result['extra_sections']:
        print(f"  ✅ セクション構造は同一")
    
    print(f"\n【総合評価】")
    similarity = result['structural_similarity']
    
    if similarity >= 90:
        grade = "🌟 優秀（本番使用可）"
    elif similarity >= 75:
        grade = "✅ 良好（軽微な調整で使用可）"
    elif similarity >= 60:
        grade = "⚠️  要改善（プロンプト調整推奨）"
    else:
        grade = "❌ 不合格（再設計必要）"
    
    print(f"  構造的類似度: {similarity:.1f}%")
    print(f"  評価: {grade}")
    print(f"{'='*70}\n")

def main():
    """メイン処理"""
    import sys
    
    if len(sys.argv) < 3:
        print("使用方法: python compare_articles.py <対話型ファイル> <API版ファイル>")
        print("例: python compare_articles.py content/en/glossary/Test1.md content/en/glossary-api-test/Test1.md")
        sys.exit(1)
    
    file1 = Path(sys.argv[1])
    file2 = Path(sys.argv[2])
    
    result = compare_articles(file1, file2)
    print_comparison(result)

if __name__ == "__main__":
    main()
