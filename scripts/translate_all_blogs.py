#!/usr/bin/env python3
"""
Batch translate all blog articles from English to Japanese using Claude API.
"""

import os
import sys
import time
from pathlib import Path
import subprocess

def get_blog_articles(en_blog_dir):
    """Get list of English blog articles"""
    articles = []
    
    for file in sorted(en_blog_dir.glob('*.md')):
        if file.name.startswith('.'):
            continue
        articles.append(file.name)
    
    return articles

def translate_article(article_filename, script_path):
    """Translate a single article"""
    
    print("=" * 70)
    print(f"Translating: {article_filename}")
    print("=" * 70)
    print()
    
    # Run translation script
    result = subprocess.run(
        ['python3', str(script_path), article_filename],
        capture_output=False,
        text=True
    )
    
    return result.returncode == 0

def main():
    """Main batch translation workflow"""
    
    # Paths
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent
    en_blog_dir = repo_root / 'content' / 'en' / 'blog'
    translate_script = script_dir / 'translate_blog_api.py'
    
    print("=" * 70)
    print("Batch Blog Translation Tool")
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
    
    # Get all blog articles
    articles = get_blog_articles(en_blog_dir)
    
    print(f"Found {len(articles)} blog articles to translate")
    print()
    
    # Show list
    print("Articles:")
    for i, article in enumerate(articles, 1):
        print(f"  {i:2d}. {article}")
    print()
    
    # Confirm
    if '--yes' not in sys.argv:
        response = input("Proceed with translation? [y/N]: ")
        if response.lower() != 'y':
            print("Cancelled")
            return 0
        print()
    
    # Translate each article
    success_count = 0
    failed_articles = []
    
    start_time = time.time()
    
    for i, article in enumerate(articles, 1):
        print()
        print(f"[{i}/{len(articles)}] Processing: {article}")
        print()
        
        success = translate_article(article, translate_script)
        
        if success:
            success_count += 1
            print(f"✓ Successfully translated: {article}")
        else:
            failed_articles.append(article)
            print(f"❌ Failed to translate: {article}")
        
        # Rate limiting: wait between API calls
        if i < len(articles):
            wait_time = 2  # seconds
            print(f"Waiting {wait_time}s before next article...")
            time.sleep(wait_time)
    
    # Summary
    elapsed_time = time.time() - start_time
    
    print()
    print("=" * 70)
    print("BATCH TRANSLATION SUMMARY")
    print("=" * 70)
    print()
    print(f"Total articles: {len(articles)}")
    print(f"Successful: {success_count}")
    print(f"Failed: {len(failed_articles)}")
    print(f"Elapsed time: {elapsed_time:.1f}s ({elapsed_time/60:.1f}m)")
    print()
    
    if failed_articles:
        print("Failed articles:")
        for article in failed_articles:
            print(f"  - {article}")
        print()
    
    print("=" * 70)
    print("NEXT STEPS:")
    print("=" * 70)
    print()
    print("1. Review translated articles in:")
    print("   content/ja/blog/")
    print()
    print("2. Run validation on all articles:")
    print("   for f in content/ja/blog/*.md; do")
    print("     python scripts/validate_translation.py $(basename $f)")
    print("   done")
    print()
    print("3. Rebuild Hugo:")
    print("   hugo --cleanDestinationDir")
    print()
    print("4. Run internal linking:")
    print("   python scripts/linkbuilding_parallel.py \\")
    print("     --linkbuilding-dir data/linkbuilding \\")
    print("     --public-dir public \\")
    print("     --denylist-dir databases")
    print()
    
    return 0 if len(failed_articles) == 0 else 1

if __name__ == '__main__':
    sys.exit(main())
