#!/usr/bin/env python3
"""
Translate blog articles from English to Japanese using Claude API.
Ensures consistent terminology and proper formatting using translation glossary.
"""

import os
import sys
import csv
import re
import json
from pathlib import Path
from anthropic import Anthropic

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

def translate_with_claude(prompt, api_key, model="claude-3-5-sonnet-20241022"):
    """Translate using Claude API"""
    
    client = Anthropic(api_key=api_key)
    
    print(f"Calling Claude API (model: {model})...")
    
    try:
        message = client.messages.create(
            model=model,
            max_tokens=16000,
            temperature=0.3,  # Lower temperature for more consistent translations
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
        
        # Extract translated content
        translated_content = message.content[0].text
        
        # Token usage info
        input_tokens = message.usage.input_tokens
        output_tokens = message.usage.output_tokens
        
        print(f"✓ Translation completed")
        print(f"  Input tokens: {input_tokens:,}")
        print(f"  Output tokens: {output_tokens:,}")
        print(f"  Total tokens: {input_tokens + output_tokens:,}")
        
        return translated_content
        
    except Exception as e:
        print(f"❌ API Error: {e}")
        return None

def validate_translation(translated_content):
    """Quick validation of translated content"""
    issues = []
    
    # Check for unclosed bold syntax
    bold_opens = translated_content.count('**')
    if bold_opens % 2 != 0:
        issues.append("⚠️  Unclosed bold syntax detected (odd number of **)")
    
    # Check for particles inside bold (common mistake)
    particle_in_bold = re.findall(r'\*\*[^\*]+[のはがをにへとからまでよりでや]\*\*', translated_content)
    if particle_in_bold:
        issues.append(f"⚠️  Particles inside bold detected: {len(particle_in_bold)} instances")
    
    # Check for very long lines (>500 chars)
    lines = translated_content.split('\n')
    long_lines = [i for i, line in enumerate(lines, 1) if len(line) > 500 and not line.startswith('http')]
    if long_lines:
        issues.append(f"⚠️  Very long lines detected: {len(long_lines)} lines")
    
    return issues

def main():
    """Main translation workflow"""
    
    # Paths
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent
    glossary_path = repo_root / 'databases' / 'translation_glossary.csv'
    
    print("=" * 70)
    print("Blog Article Translation Tool (Claude API)")
    print("=" * 70)
    print()
    
    # Check for API key
    api_key = os.environ.get('ANTHROPIC_API_KEY')
    if not api_key:
        print("❌ ANTHROPIC_API_KEY environment variable not set")
        print()
        print("Please set your API key:")
        print("  export ANTHROPIC_API_KEY='your-api-key-here'")
        print()
        sys.exit(1)
    
    # Load glossary
    print(f"Loading glossary from: {glossary_path}")
    glossary = load_glossary(glossary_path)
    print(f"✓ Loaded {len(glossary)} terms from glossary")
    print()
    
    # Get article to translate
    if len(sys.argv) < 2:
        print("Usage: python translate_blog_api.py <article_filename>")
        print()
        print("Example:")
        print("  python translate_blog_api.py how-to-use-large-language-models-effectively.md")
        print()
        print("Options:")
        print("  --all           Translate all blog articles")
        print("  --dry-run       Show what would be translated without calling API")
        sys.exit(1)
    
    article_filename = sys.argv[1]
    dry_run = '--dry-run' in sys.argv
    
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
    print(f"✓ Prompt created ({len(prompt):,} chars)")
    print()
    
    if dry_run:
        print("🔍 DRY RUN MODE - Not calling API")
        print()
        print("Prompt preview (first 500 chars):")
        print("-" * 70)
        print(prompt[:500])
        print("...")
        print("-" * 70)
        return 0
    
    # Translate using Claude API
    translated_content = translate_with_claude(prompt, api_key)
    
    if not translated_content:
        print("❌ Translation failed")
        sys.exit(1)
    
    print()
    print(f"✓ Received translation ({len(translated_content):,} bytes)")
    print()
    
    # Quick validation
    print("Running quick validation...")
    issues = validate_translation(translated_content)
    
    if issues:
        print("⚠️  Validation warnings:")
        for issue in issues:
            print(f"  {issue}")
        print()
        print("Note: Run full validation after saving:")
        print(f"  python scripts/validate_translation.py {article_filename}")
        print()
    else:
        print("✓ Quick validation passed")
        print()
    
    # Save translated content
    print(f"Saving to: {ja_article_path}")
    
    # Backup existing file if it exists
    if ja_article_path.exists():
        backup_path = ja_article_path.with_suffix('.md.backup')
        ja_article_path.rename(backup_path)
        print(f"  Backed up existing file to: {backup_path}")
    
    with open(ja_article_path, 'w', encoding='utf-8') as f:
        f.write(translated_content)
    
    print(f"✓ Translation saved")
    print()
    
    print("=" * 70)
    print("NEXT STEPS:")
    print("=" * 70)
    print()
    print("1. Run full validation:")
    print(f"   python scripts/validate_translation.py {article_filename}")
    print()
    print("2. Review the translated file:")
    print(f"   {ja_article_path}")
    print()
    print("3. If validation passes, rebuild Hugo:")
    print("   hugo --cleanDestinationDir")
    print()
    print("4. Run internal linking:")
    print("   python scripts/linkbuilding.py -d public/ja -k data/linkbuilding/ja.yaml -a data/linkbuilding/ja_automatic.json --denylist databases/danger_terms_ja.csv")
    print()
    
    return 0

if __name__ == '__main__':
    sys.exit(main())
