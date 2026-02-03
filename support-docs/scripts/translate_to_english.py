#!/usr/bin/env python3
"""
Translate Japanese support-docs content to English using Claude API.

Usage:
    python3 scripts/translate_to_english.py --dry-run
    python3 scripts/translate_to_english.py --workers 3
    python3 scripts/translate_to_english.py --file content/ja/docs/ai-chatbot/ai-service-about.md
"""

import os
import sys
import re
import yaml
import argparse
import time
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime

try:
    import anthropic
except ImportError:
    print("Error: anthropic package not installed. Run: pip install anthropic")
    sys.exit(1)


# Translation prompt for Japanese to English
TRANSLATION_PROMPT = """Translate the following Japanese Markdown content to English. Follow these critical rules:

1. FRONTMATTER: 
   - Keep all frontmatter keys unchanged (title, date, lastmod, draft, translationKey, description, keywords, category)
   - Translate only the values (title, description, keywords)
   - Keep translationKey value unchanged (it's an identifier)
   - Keep date/lastmod values unchanged
   - Keep draft value unchanged
   - Keep category value unchanged

2. MARKDOWN STRUCTURE:
   - Preserve all heading levels (##, ###, etc.)
   - Preserve all list formatting (-, *, 1., etc.)
   - Preserve all code blocks and inline code unchanged
   - Preserve all links and URLs unchanged

3. TRANSLATION QUALITY:
   - Use natural, professional English
   - Keep technical terms accurate (AI, chatbot, API, etc.)
   - Maintain the same tone and style as the original
   - Keep brand names unchanged (SmartWeb, FlowHunt, etc.)

4. BOLD SYNTAX:
   - Preserve bold markdown (**text**) formatting
   - Ensure all bold syntax is properly opened and closed

Content to translate:
---
{content}
---

Return ONLY the translated Markdown content, nothing else. Start with the frontmatter (---).
"""


def load_api_key():
    """Load Anthropic API key from environment"""
    api_key = os.environ.get("ANTHROPIC_API_KEY") or os.environ.get("CLAUDE_API_KEY")
    if not api_key:
        # Try loading from .env file
        env_file = Path(__file__).parent.parent.parent / ".env"
        if env_file.exists():
            with open(env_file) as f:
                for line in f:
                    if line.startswith("ANTHROPIC_API_KEY=") or line.startswith("CLAUDE_API_KEY="):
                        api_key = line.strip().split("=", 1)[1].strip('"\'')
                        break
    return api_key


def translate_content(client, content: str, model: str = "claude-sonnet-4-20250514") -> str:
    """Translate content using Claude API"""
    message = client.messages.create(
        model=model,
        max_tokens=4096,
        messages=[
            {
                "role": "user",
                "content": TRANSLATION_PROMPT.format(content=content)
            }
        ]
    )
    return message.content[0].text


def get_ja_files(content_dir: Path) -> list:
    """Get all Japanese markdown files"""
    ja_docs = content_dir / "ja" / "docs"
    if not ja_docs.exists():
        return []
    return list(ja_docs.rglob("*.md"))


def get_en_output_path(ja_path: Path, content_dir: Path) -> Path:
    """Convert Japanese path to English output path"""
    rel_path = ja_path.relative_to(content_dir / "ja")
    return content_dir / "en" / rel_path


def file_needs_translation(ja_path: Path, en_path: Path) -> bool:
    """Check if file needs translation (EN doesn't exist or JA is newer)"""
    if not en_path.exists():
        return True
    return ja_path.stat().st_mtime > en_path.stat().st_mtime


def translate_file(client, ja_path: Path, en_path: Path, dry_run: bool = False) -> dict:
    """Translate a single file"""
    result = {
        "ja_path": str(ja_path),
        "en_path": str(en_path),
        "status": "skipped",
        "error": None
    }
    
    try:
        # Read Japanese content
        with open(ja_path, "r", encoding="utf-8") as f:
            ja_content = f.read()
        
        if dry_run:
            result["status"] = "would_translate"
            return result
        
        # Translate
        en_content = translate_content(client, ja_content)
        
        # Ensure output directory exists
        en_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Write English content
        with open(en_path, "w", encoding="utf-8") as f:
            f.write(en_content)
        
        result["status"] = "translated"
        
    except Exception as e:
        result["status"] = "error"
        result["error"] = str(e)
    
    return result


def main():
    parser = argparse.ArgumentParser(description="Translate support-docs from Japanese to English")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be translated without making changes")
    parser.add_argument("--workers", type=int, default=3, help="Number of parallel workers (default: 3)")
    parser.add_argument("--file", type=str, help="Translate a specific file only")
    parser.add_argument("--force", action="store_true", help="Force re-translation even if EN exists")
    parser.add_argument("--model", type=str, default="claude-sonnet-4-20250514", help="Claude model to use")
    args = parser.parse_args()
    
    # Setup paths
    script_dir = Path(__file__).parent
    content_dir = script_dir.parent / "content"
    
    # Load API key
    api_key = load_api_key()
    if not api_key and not args.dry_run:
        print("Error: ANTHROPIC_API_KEY not found in environment or .env file")
        sys.exit(1)
    
    # Initialize client
    client = None
    if not args.dry_run:
        client = anthropic.Anthropic(api_key=api_key)
    
    # Get files to translate
    if args.file:
        ja_files = [Path(args.file)]
    else:
        ja_files = get_ja_files(content_dir)
    
    if not ja_files:
        print("No Japanese files found to translate")
        return
    
    # Filter files that need translation
    files_to_translate = []
    for ja_path in ja_files:
        en_path = get_en_output_path(ja_path, content_dir)
        if args.force or file_needs_translation(ja_path, en_path):
            files_to_translate.append((ja_path, en_path))
    
    print(f"Found {len(ja_files)} Japanese files")
    print(f"Files needing translation: {len(files_to_translate)}")
    
    if not files_to_translate:
        print("All files are up to date")
        return
    
    if args.dry_run:
        print("\n[DRY RUN] Would translate:")
        for ja_path, en_path in files_to_translate:
            print(f"  {ja_path.name} -> {en_path}")
        return
    
    # Translate files
    print(f"\nTranslating with {args.workers} workers using {args.model}...")
    
    results = {"translated": 0, "error": 0, "skipped": 0}
    errors = []
    
    with ThreadPoolExecutor(max_workers=args.workers) as executor:
        futures = {
            executor.submit(translate_file, client, ja_path, en_path, args.dry_run): (ja_path, en_path)
            for ja_path, en_path in files_to_translate
        }
        
        for future in as_completed(futures):
            ja_path, en_path = futures[future]
            result = future.result()
            
            results[result["status"]] = results.get(result["status"], 0) + 1
            
            if result["status"] == "translated":
                print(f"✓ {ja_path.name}")
            elif result["status"] == "error":
                print(f"✗ {ja_path.name}: {result['error']}")
                errors.append(result)
            
            # Rate limiting
            time.sleep(0.5)
    
    # Summary
    print(f"\n=== Translation Summary ===")
    print(f"Translated: {results.get('translated', 0)}")
    print(f"Errors: {results.get('error', 0)}")
    print(f"Skipped: {results.get('skipped', 0)}")
    
    if errors:
        print("\nErrors:")
        for err in errors:
            print(f"  - {err['ja_path']}: {err['error']}")


if __name__ == "__main__":
    main()
