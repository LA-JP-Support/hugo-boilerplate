#!/usr/bin/env python3
"""
Translate blog articles from English to Japanese using translation glossary.
This script ensures consistent terminology and proper formatting.
"""

import os
import sys
import csv
import re
from pathlib import Path

def load_glossary(csv_path):
    """Load translation glossary from CSV"""
    glossary = {}
    
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            glossary[row['english']] = {
                'japanese': row['japanese'],
                'type': row['type'],
                'category': row['category'],
                'notes': row['notes']
            }
    
    return glossary

def create_translation_prompt(glossary, content, article_title):
    """Create translation prompt with glossary terms"""
    
    # Extract relevant terms from glossary (limit to most common ones)
    common_terms = []
    for eng, data in list(glossary.items())[:100]:  # First 100 terms
        if data['type'] == 'keep_english':
            common_terms.append(f"- {eng} → {eng} (Keep in English)")
        elif data['type'] == 'translate':
            common_terms.append(f"- {eng} → {data['japanese']} (Translate)")
        elif data['type'] == 'katakana':
            common_terms.append(f"- {eng} → {data['japanese']} (Use katakana)")
        elif data['type'] == 'hybrid':
            common_terms.append(f"- {eng} → {data['japanese']} (Hybrid)")
    
    prompt = f"""Translate the following English Markdown blog article to Japanese. Follow these critical rules:

## CRITICAL FORMATTING RULES

1. **BOLD SYNTAX**: Keep bold markdown (**) tight around words, EXCLUDING Japanese particles
   - WRONG: **Anthropicの**Claude
   - CORRECT: **Anthropic**のClaude
   - WRONG: **Googleの**Gemini
   - CORRECT: **Google**のGemini

2. **CLOSURE**: Every opening ** MUST have a closing **
   - WRONG: **トークンと呼ばれます。トークンは...
   - CORRECT: **トークン**と呼ばれます。トークンは...

3. **PROPER NOUNS**: Keep technical terms and brand names in English
   - Keep: ChatGPT, API, Claude, Gemini, GitHub, OpenAI, Anthropic, Google, Microsoft, etc.

4. **LINE BREAKS**: Break long paragraphs at sentence boundaries for readability
   - Aim for 1-3 sentences per line
   - Add blank lines between paragraphs

5. **FRONTMATTER**: Translate only values, keep keys and syntax unchanged
   - Keep YAML/TOML structure intact
   - Translate: title, description, keywords values
   - Keep: tags, categories structure

6. **LINKS**: Do NOT translate URLs or link syntax
   - Keep all URLs unchanged
   - Keep Markdown link syntax unchanged

7. **CODE**: NEVER translate content in code blocks or inline code
   - Content between backticks (`) stays unchanged
   - Code fences (```) content stays unchanged

## TRANSLATION GLOSSARY (Use these exact translations)

{chr(10).join(common_terms)}

## ARTICLE TO TRANSLATE

Title: {article_title}

{content}

## OUTPUT REQUIREMENTS

1. Output ONLY the translated Markdown content
2. Do NOT add any explanations or comments
3. Maintain exact Markdown structure
4. Ensure all bold syntax is properly closed
5. Keep particles OUTSIDE of bold syntax
6. Break long lines at sentence boundaries
7. Preserve all frontmatter structure
"""
    
    return prompt

def validate_translation(translated_content):
    """Validate translated content for common issues"""
    issues = []
    
    # Check for unclosed bold syntax
    bold_opens = translated_content.count('**')
    if bold_opens % 2 != 0:
        issues.append("⚠️  Unclosed bold syntax detected (odd number of **)")
    
    # Check for particles inside bold (common mistake)
    particle_in_bold = re.findall(r'\*\*[^\*]+[のはがをにへとからまでよりでや]\*\*', translated_content)
    if particle_in_bold:
        issues.append(f"⚠️  Particles inside bold detected: {len(particle_in_bold)} instances")
        for match in particle_in_bold[:5]:  # Show first 5
            issues.append(f"    Example: {match}")
    
    # Check for very long lines (>500 chars)
    lines = translated_content.split('\n')
    long_lines = [i for i, line in enumerate(lines, 1) if len(line) > 500 and not line.startswith('http')]
    if long_lines:
        issues.append(f"⚠️  Very long lines detected: {len(long_lines)} lines")
        issues.append(f"    Line numbers: {long_lines[:10]}")
    
    # Check for translated product names (should stay in English)
    product_names = ['ChatGPT', 'Claude', 'Gemini', 'Copilot', 'OpenAI', 'Anthropic', 'Google', 'Microsoft']
    for product in product_names:
        if product not in translated_content and product.lower() in translated_content.lower():
            issues.append(f"⚠️  Product name '{product}' may have been incorrectly translated")
    
    return issues

def main():
    """Main translation workflow"""
    
    # Paths
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent
    glossary_path = repo_root / 'databases' / 'translation_glossary.csv'
    
    print("=" * 60)
    print("Blog Article Translation Tool")
    print("=" * 60)
    print()
    
    # Load glossary
    print(f"Loading glossary from: {glossary_path}")
    glossary = load_glossary(glossary_path)
    print(f"✓ Loaded {len(glossary)} terms from glossary")
    print()
    
    # Get article to translate
    if len(sys.argv) < 2:
        print("Usage: python translate_blog_with_glossary.py <article_filename>")
        print()
        print("Example:")
        print("  python translate_blog_with_glossary.py how-to-use-large-language-models-effectively.md")
        sys.exit(1)
    
    article_filename = sys.argv[1]
    
    # Paths
    en_article_path = repo_root / 'content' / 'en' / 'blog' / article_filename
    ja_article_path = repo_root / 'content' / 'ja' / 'blog' / article_filename
    
    # Check if English article exists
    if not en_article_path.exists():
        print(f"❌ English article not found: {en_article_path}")
        sys.exit(1)
    
    print(f"Source: {en_article_path}")
    print(f"Target: {ja_article_path}")
    print()
    
    # Read English article
    with open(en_article_path, 'r', encoding='utf-8') as f:
        en_content = f.read()
    
    print(f"✓ Read English article ({len(en_content):,} bytes)")
    print()
    
    # Extract title from frontmatter
    title_match = re.search(r'^title\s*[:=]\s*["\']?(.+?)["\']?$', en_content, re.MULTILINE)
    article_title = title_match.group(1) if title_match else article_filename
    
    # Create translation prompt
    print("Creating translation prompt...")
    prompt = create_translation_prompt(glossary, en_content, article_title)
    
    # Save prompt to file for manual translation
    prompt_file = repo_root / 'temp_translation_prompt.txt'
    with open(prompt_file, 'w', encoding='utf-8') as f:
        f.write(prompt)
    
    print(f"✓ Translation prompt saved to: {prompt_file}")
    print()
    print("=" * 60)
    print("NEXT STEPS:")
    print("=" * 60)
    print()
    print("1. Open the prompt file:")
    print(f"   {prompt_file}")
    print()
    print("2. Copy the entire prompt")
    print()
    print("3. Paste into Claude/ChatGPT for translation")
    print()
    print("4. Copy the translated output")
    print()
    print("5. Save to:")
    print(f"   {ja_article_path}")
    print()
    print("6. Run validation:")
    print(f"   python scripts/validate_translation.py {article_filename}")
    print()
    
    return 0

if __name__ == '__main__':
    sys.exit(main())
