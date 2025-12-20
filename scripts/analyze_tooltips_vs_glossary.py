#!/usr/bin/env python3
"""
Analyze tooltips in blog posts and compare with existing glossary entries.

This script:
1. Extracts all tooltip keywords from blog posts
2. Checks which ones already have glossary entries
3. Reports missing glossary entries

Usage:
    python3 scripts/analyze_tooltips_vs_glossary.py --lang en
    python3 scripts/analyze_tooltips_vs_glossary.py --lang ja
"""

import argparse
import re
import json
from pathlib import Path
from typing import Dict, List, Set, Tuple
from collections import defaultdict

# Tooltip pattern for Hugo shortcode
TOOLTIP_PATTERN = re.compile(
    r'\{\{<\s*tooltip\s+text="([^"]*)"\s*>\}\}(.*?)\{\{<\s*/tooltip\s*>\}\}',
    re.DOTALL
)

# Internal link pattern
INTERNAL_LINK_PATTERN = re.compile(r'\[([^\]]+)\]\((/[^)]+)\)')


class TooltipAnalyzer:
    def __init__(self, lang: str = "en"):
        self.lang = lang
        self.project_root = Path(__file__).parent.parent
        self.blog_dir = self.project_root / "content" / lang / "blog"
        self.glossary_dir = self.project_root / "content" / lang / "glossary"
        
        # Storage
        self.tooltips: Dict[str, List[Tuple[str, str, str]]] = defaultdict(list)  # keyword -> [(definition, file, context)]
        self.glossary_titles: Set[str] = set()  # Existing glossary titles (lowercase)
        self.glossary_slugs: Set[str] = set()   # Existing glossary slugs
        self.glossary_map: Dict[str, str] = {}  # slug -> title
    
    def load_glossary_entries(self):
        """Load existing glossary entries."""
        if not self.glossary_dir.exists():
            print(f"⚠️  Glossary directory not found: {self.glossary_dir}")
            return
        
        for md_file in self.glossary_dir.glob("*.md"):
            if md_file.name == "_index.md":
                continue
            
            try:
                content = md_file.read_text(encoding='utf-8')
                
                # Extract frontmatter
                fm_match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
                if not fm_match:
                    continue
                
                frontmatter = fm_match.group(1)
                
                # Extract title
                title_match = re.search(r'^title:\s*["\']?(.+?)["\']?\s*$', frontmatter, re.MULTILINE)
                if title_match:
                    title = title_match.group(1).strip().strip('"').strip("'")
                    slug = md_file.stem.lower()
                    
                    self.glossary_titles.add(title.lower())
                    self.glossary_slugs.add(slug)
                    self.glossary_map[slug] = title
                    
            except Exception as e:
                print(f"⚠️  Error reading {md_file.name}: {e}")
        
        print(f"✅ Loaded {len(self.glossary_titles)} glossary entries")
    
    def extract_tooltips_from_file(self, file_path: Path):
        """Extract tooltip keywords from a single markdown file."""
        try:
            content = file_path.read_text(encoding='utf-8')
            
            # Find all tooltips
            for match in TOOLTIP_PATTERN.finditer(content):
                definition = match.group(1).strip()
                keyword_raw = match.group(2).strip()
                
                # Remove internal links from keyword if present
                keyword = INTERNAL_LINK_PATTERN.sub(r'\1', keyword_raw)
                
                # Clean up keyword
                keyword = keyword.strip().strip('*').strip('`')
                
                if keyword and definition:
                    # Get context (50 chars before and after)
                    start = max(0, match.start() - 50)
                    end = min(len(content), match.end() + 50)
                    context = content[start:end].replace('\n', ' ')
                    
                    self.tooltips[keyword.lower()].append((
                        definition,
                        file_path.name,
                        context
                    ))
            
        except Exception as e:
            print(f"⚠️  Error processing {file_path.name}: {e}")
    
    def analyze_blog_posts(self):
        """Extract tooltips from all blog posts."""
        if not self.blog_dir.exists():
            print(f"⚠️  Blog directory not found: {self.blog_dir}")
            return
        
        blog_files = list(self.blog_dir.glob("*.md"))
        print(f"📝 Analyzing {len(blog_files)} blog posts...")
        
        for md_file in blog_files:
            self.extract_tooltips_from_file(md_file)
        
        print(f"✅ Found {len(self.tooltips)} unique tooltip keywords")
    
    def compare_and_report(self) -> Dict:
        """Compare tooltips with glossary and generate report."""
        # Categorize tooltips
        has_glossary = []
        missing_glossary = []
        
        for keyword, occurrences in self.tooltips.items():
            # Check if glossary exists
            found = False
            
            # Direct title match
            if keyword in self.glossary_titles:
                found = True
            
            # Check if any occurrence has internal link to glossary
            for def_text, file_name, context in occurrences:
                if '/glossary/' in context:
                    found = True
                    break
            
            if found:
                has_glossary.append((keyword, occurrences))
            else:
                missing_glossary.append((keyword, occurrences))
        
        # Generate report
        report = {
            "language": self.lang,
            "total_tooltips": len(self.tooltips),
            "has_glossary": len(has_glossary),
            "missing_glossary": len(missing_glossary),
            "glossary_entries": len(self.glossary_titles),
            "missing_details": []
        }
        
        # Print summary
        print(f"\n{'='*60}")
        print(f"📊 TOOLTIP ANALYSIS REPORT ({self.lang.upper()})")
        print(f"{'='*60}")
        print(f"Total unique tooltips:     {report['total_tooltips']:>5}")
        print(f"Already in glossary:       {report['has_glossary']:>5}")
        print(f"Missing from glossary:     {report['missing_glossary']:>5}")
        print(f"Total glossary entries:    {report['glossary_entries']:>5}")
        print(f"{'='*60}\n")
        
        # List missing glossary entries
        if missing_glossary:
            print(f"🔍 TOOLTIPS WITHOUT GLOSSARY ENTRIES ({len(missing_glossary)}):\n")
            
            for keyword, occurrences in sorted(missing_glossary, key=lambda x: -len(x[1])):
                definition = occurrences[0][0]  # First definition
                count = len(occurrences)
                files = set(occ[1] for occ in occurrences)
                
                print(f"  📌 {keyword}")
                print(f"     Definition: {definition[:80]}{'...' if len(definition) > 80 else ''}")
                print(f"     Used in: {count} location(s) across {len(files)} file(s)")
                
                # Add to report details
                report["missing_details"].append({
                    "keyword": keyword,
                    "definition": definition,
                    "usage_count": count,
                    "files": list(files)
                })
                
                print()
        
        return report
    
    def save_report(self, report: Dict, output_file: Path):
        """Save report to JSON file."""
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2)
        print(f"💾 Report saved to: {output_file}")


def main():
    parser = argparse.ArgumentParser(description="Analyze tooltips vs glossary entries")
    parser.add_argument('--lang', default='en', choices=['en', 'ja'],
                       help='Language to analyze (en or ja)')
    parser.add_argument('--output', default=None,
                       help='Output JSON file (default: docs/tooltip_analysis_{lang}.json)')
    
    args = parser.parse_args()
    
    # Create analyzer
    analyzer = TooltipAnalyzer(lang=args.lang)
    
    # Load glossary
    analyzer.load_glossary_entries()
    
    # Analyze blog posts
    analyzer.analyze_blog_posts()
    
    # Compare and report
    report = analyzer.compare_and_report()
    
    # Save report
    if args.output:
        output_file = Path(args.output)
    else:
        output_file = analyzer.project_root / "docs" / f"tooltip_analysis_{args.lang}.json"
    
    analyzer.save_report(report, output_file)


if __name__ == '__main__':
    main()
