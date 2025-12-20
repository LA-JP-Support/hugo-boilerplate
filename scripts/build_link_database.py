#!/usr/bin/env python3
"""
Build comprehensive link database from glossary
Creates a CSV database of all linkable terms with priorities and variations
"""

import csv
import re
from pathlib import Path
from typing import List, Set, Tuple
import argparse

def extract_glossary_info(md_file: Path, lang: str) -> Tuple[str, str, str]:
    """Extract title, URL, and description from glossary file"""
    try:
        content = md_file.read_text(encoding='utf-8')
        
        # Extract frontmatter
        fm_match = re.search(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
        if not fm_match:
            return None, None, None
        
        frontmatter = fm_match.group(1)
        
        # Extract title
        title_match = re.search(r'^title:\s*["\']?(.+?)["\']?\s*$', frontmatter, re.MULTILINE)
        if not title_match:
            return None, None, None
        
        title = title_match.group(1).strip().strip('"').strip("'")
        
        # Extract description
        description_match = re.search(r'^description:\s*["\']?(.+?)["\']?\s*$', frontmatter, re.MULTILINE)
        description = description_match.group(1).strip().strip('"').strip("'") if description_match else ""
        
        # Construct URL
        slug = md_file.stem
        url = f"/{lang}/glossary/{slug}/"
        
        return title, url, description
        
    except Exception as e:
        print(f"Error processing {md_file.name}: {e}")
        return None, None, None

def generate_keyword_variations(title: str) -> List[Tuple[str, int, str]]:
    """
    Generate keyword variations with priority and type
    Returns: List of (keyword, priority, variation_type)
    """
    variations = []
    
    # Original title - highest priority
    variations.append((title, 1000, "exact"))
    
    # Handle parenthetical content
    if '(' in title and ')' in title:
        # Without parentheses
        without_parens = re.sub(r'\s*\([^)]*\)\s*', '', title).strip()
        if without_parens and len(without_parens) > 2:
            variations.append((without_parens, 900, "without_parens"))
        
        # Parenthetical content only (e.g., "NLP" from "Natural Language Processing (NLP)")
        parens_content = re.findall(r'\(([^)]+)\)', title)
        for content in parens_content:
            content = content.strip()
            if content and len(content) > 1:
                # Acronyms get high priority
                if content.isupper() and 2 <= len(content) <= 6:
                    variations.append((content, 950, "acronym"))
                else:
                    variations.append((content, 800, "parens_content"))
                
                # Also add variations of parenthetical content
                if '、' in content or ',' in content:
                    # Split by comma or Japanese comma
                    parts = re.split(r'[、,]', content)
                    for part in parts:
                        part = part.strip()
                        if part and len(part) > 1:
                            variations.append((part, 750, "parens_part"))
    
    # Handle slashes (e.g., "AI/ML" -> "AI", "ML")
    if '/' in title:
        parts = title.split('/')
        for part in parts:
            part = part.strip()
            if part and len(part) > 1:
                variations.append((part, 700, "slash_part"))
    
    # Handle hyphens for compound words
    if '-' in title and '(' not in title:
        without_hyphens = title.replace('-', ' ')
        if without_hyphens != title:
            variations.append((without_hyphens, 600, "without_hyphens"))
    
    # Handle Japanese patterns
    if title.endswith('とは'):
        variations.append((title[:-2], 500, "without_toha"))
    
    # Handle common patterns with （）full-width parentheses
    if '（' in title and '）' in title:
        without_fullwidth = re.sub(r'\s*（[^）]*）\s*', '', title).strip()
        if without_fullwidth and len(without_fullwidth) > 2:
            variations.append((without_fullwidth, 880, "without_fullwidth_parens"))
        
        fullwidth_content = re.findall(r'（([^）]+)）', title)
        for content in fullwidth_content:
            content = content.strip()
            if content and len(content) > 1:
                variations.append((content, 780, "fullwidth_parens_content"))
    
    # Handle common English patterns
    if title.endswith(' (AI)') or title.endswith(' (ML)'):
        base = re.sub(r'\s*\([^)]*\)$', '', title)
        if base:
            variations.append((base, 850, "without_ai_ml"))
    
    # Add singular/plural variations for common terms
    if title.endswith('s') and len(title) > 3:
        singular = title[:-1]
        variations.append((singular, 400, "singular"))
    
    return variations

def build_database(glossary_dir: Path, output_csv: Path, lang: str):
    """Build link database CSV from glossary directory"""
    print(f"\n{'='*60}")
    print(f"Building link database from: {glossary_dir}")
    print(f"Output: {output_csv}")
    print(f"Language: {lang}")
    print(f"{'='*60}\n")
    
    if not glossary_dir.exists():
        print(f"Error: Glossary directory not found: {glossary_dir}")
        return
    
    rows = []
    glossary_count = 0
    
    for md_file in sorted(glossary_dir.glob("*.md")):
        if md_file.name == "_index.md":
            continue
        
        title, url, description = extract_glossary_info(md_file, lang)
        
        if not title or not url:
            continue
        
        glossary_count += 1
        
        # Generate variations
        variations = generate_keyword_variations(title)
        
        for keyword, priority, variation_type in variations:
            # Adjust priority based on keyword length
            adjusted_priority = priority + (len(keyword) * 2)
            
            rows.append({
                'keyword': keyword,
                'normalized': keyword.lower().strip(),
                'title': title,
                'url': url,
                'description': description[:200] if description else "",  # Limit description length
                'priority': adjusted_priority,
                'variation_type': variation_type,
                'exact_match': 'true' if variation_type == 'exact' else 'false'
            })
    
    # Sort by priority (descending), then by keyword length (descending)
    rows.sort(key=lambda x: (x['priority'], len(x['keyword'])), reverse=True)
    
    # Write to CSV
    output_csv.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_csv, 'w', encoding='utf-8', newline='') as f:
        fieldnames = ['keyword', 'normalized', 'title', 'url', 'description', 'priority', 'variation_type', 'exact_match']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    
    print(f"\n{'='*60}")
    print(f"✅ Link database created successfully!")
    print(f"   Glossary entries: {glossary_count}")
    print(f"   Total keyword variations: {len(rows)}")
    print(f"   Output file: {output_csv}")
    print(f"{'='*60}\n")
    
    # Show top 20 keywords by priority
    print("Top 20 keywords by priority:")
    for i, row in enumerate(rows[:20], 1):
        print(f"  {i:2d}. {row['keyword']:40s} (priority: {row['priority']:4d}, type: {row['variation_type']})")

def main():
    parser = argparse.ArgumentParser(description="Build link database from glossary")
    parser.add_argument("--glossary-dir", type=Path, required=True, help="Path to glossary directory")
    parser.add_argument("--output", type=Path, required=True, help="Output CSV file path")
    parser.add_argument("--lang", default="ja", help="Language code (default: ja)")
    
    args = parser.parse_args()
    
    build_database(args.glossary_dir, args.output, args.lang)

if __name__ == "__main__":
    main()
