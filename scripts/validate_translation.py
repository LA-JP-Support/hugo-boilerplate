#!/usr/bin/env python3
"""
Validate Japanese blog article translations for common issues.
Checks against translation glossary and formatting guidelines.
"""

import os
import sys
import csv
import re
from pathlib import Path
from collections import defaultdict

def load_glossary(csv_path):
    """Load translation glossary from CSV"""
    glossary = {}
    
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            glossary[row['english']] = {
                'japanese': row['japanese'],
                'type': row['type'],
                'category': row['category']
            }
    
    return glossary

def check_bold_syntax(content):
    """Check for bold syntax issues"""
    issues = []
    
    # Count bold markers
    bold_count = content.count('**')
    if bold_count % 2 != 0:
        issues.append({
            'severity': 'ERROR',
            'type': 'bold_unclosed',
            'message': f'Unclosed bold syntax: {bold_count} markers (should be even)',
            'line': None
        })
    
    # Check for particles inside bold
    particle_pattern = r'\*\*[^\*]+[のはがをにへとからまでよりでや]\*\*'
    matches = re.finditer(particle_pattern, content)
    
    for match in matches:
        # Get line number
        line_num = content[:match.start()].count('\n') + 1
        issues.append({
            'severity': 'ERROR',
            'type': 'particle_in_bold',
            'message': f'Particle inside bold: {match.group()}',
            'line': line_num
        })
    
    return issues

def check_product_names(content, glossary):
    """Check if product names are kept in English"""
    issues = []
    
    # Get all product names from glossary
    product_names = [
        eng for eng, data in glossary.items() 
        if data['type'] == 'keep_english' and data['category'] == 'product'
    ]
    
    for product in product_names:
        # Check if product name exists in content
        if product in content:
            continue  # Good, product name is in English
        
        # Check if it might have been translated (case-insensitive check)
        if product.lower() in content.lower() and product not in content:
            issues.append({
                'severity': 'WARNING',
                'type': 'product_translated',
                'message': f'Product name "{product}" may have been translated',
                'line': None
            })
    
    return issues

def check_line_length(content):
    """Check for very long lines"""
    issues = []
    
    lines = content.split('\n')
    for i, line in enumerate(lines, 1):
        # Skip URLs and frontmatter
        if line.startswith('http') or line.startswith('---') or line.strip().startswith('url'):
            continue
        
        if len(line) > 500:
            issues.append({
                'severity': 'WARNING',
                'type': 'long_line',
                'message': f'Very long line ({len(line)} chars)',
                'line': i
            })
    
    return issues

def check_terminology_consistency(content, glossary):
    """Check if terms are translated consistently with glossary"""
    issues = []
    
    # Sample check for common terms
    common_terms = {
        'Machine Learning': '機械学習',
        'Artificial Intelligence': '人工知能',
        'Customer Support': 'カスタマーサポート',
        'Chatbot': 'チャットボット',
        'Knowledge Base': 'ナレッジベース'
    }
    
    for eng, expected_ja in common_terms.items():
        if eng in content and expected_ja not in content:
            issues.append({
                'severity': 'INFO',
                'type': 'terminology',
                'message': f'Term "{eng}" found but expected translation "{expected_ja}" not found',
                'line': None
            })
    
    return issues

def check_frontmatter(content):
    """Check frontmatter structure"""
    issues = []
    
    # Check if frontmatter exists
    if not content.startswith('---'):
        issues.append({
            'severity': 'ERROR',
            'type': 'frontmatter',
            'message': 'Frontmatter missing (should start with ---)',
            'line': 1
        })
        return issues
    
    # Extract frontmatter
    parts = content.split('---', 2)
    if len(parts) < 3:
        issues.append({
            'severity': 'ERROR',
            'type': 'frontmatter',
            'message': 'Frontmatter not properly closed',
            'line': 1
        })
        return issues
    
    frontmatter = parts[1]
    
    # Check for required fields
    required_fields = ['title', 'description']
    for field in required_fields:
        if f'{field}:' not in frontmatter and f'{field} =' not in frontmatter:
            issues.append({
                'severity': 'WARNING',
                'type': 'frontmatter',
                'message': f'Required field "{field}" may be missing',
                'line': None
            })
    
    return issues

def generate_report(issues, article_name):
    """Generate validation report"""
    
    print("=" * 70)
    print(f"TRANSLATION VALIDATION REPORT: {article_name}")
    print("=" * 70)
    print()
    
    if not issues:
        print("✅ No issues found! Translation looks good.")
        print()
        return True
    
    # Group by severity
    errors = [i for i in issues if i['severity'] == 'ERROR']
    warnings = [i for i in issues if i['severity'] == 'WARNING']
    info = [i for i in issues if i['severity'] == 'INFO']
    
    # Summary
    print(f"Total Issues: {len(issues)}")
    print(f"  Errors:   {len(errors)}")
    print(f"  Warnings: {len(warnings)}")
    print(f"  Info:     {len(info)}")
    print()
    
    # Errors
    if errors:
        print("❌ ERRORS (Must Fix)")
        print("-" * 70)
        for issue in errors:
            line_info = f"Line {issue['line']}: " if issue['line'] else ""
            print(f"  {line_info}{issue['message']}")
        print()
    
    # Warnings
    if warnings:
        print("⚠️  WARNINGS (Should Fix)")
        print("-" * 70)
        for issue in warnings:
            line_info = f"Line {issue['line']}: " if issue['line'] else ""
            print(f"  {line_info}{issue['message']}")
        print()
    
    # Info
    if info:
        print("ℹ️  INFO (Review Recommended)")
        print("-" * 70)
        for issue in info:
            line_info = f"Line {issue['line']}: " if issue['line'] else ""
            print(f"  {line_info}{issue['message']}")
        print()
    
    return len(errors) == 0

def main():
    """Main validation workflow"""
    
    # Paths
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent
    glossary_path = repo_root / 'databases' / 'translation_glossary.csv'
    
    # Get article to validate
    if len(sys.argv) < 2:
        print("Usage: python validate_translation.py <article_filename>")
        print()
        print("Example:")
        print("  python validate_translation.py how-to-use-large-language-models-effectively.md")
        sys.exit(1)
    
    article_filename = sys.argv[1]
    ja_article_path = repo_root / 'content' / 'ja' / 'blog' / article_filename
    
    # Check if Japanese article exists
    if not ja_article_path.exists():
        print(f"❌ Japanese article not found: {ja_article_path}")
        sys.exit(1)
    
    # Load glossary
    glossary = load_glossary(glossary_path)
    
    # Read Japanese article
    with open(ja_article_path, 'r', encoding='utf-8') as f:
        ja_content = f.read()
    
    # Run all checks
    all_issues = []
    
    all_issues.extend(check_frontmatter(ja_content))
    all_issues.extend(check_bold_syntax(ja_content))
    all_issues.extend(check_product_names(ja_content, glossary))
    all_issues.extend(check_line_length(ja_content))
    all_issues.extend(check_terminology_consistency(ja_content, glossary))
    
    # Generate report
    success = generate_report(all_issues, article_filename)
    
    return 0 if success else 1

if __name__ == '__main__':
    sys.exit(main())
