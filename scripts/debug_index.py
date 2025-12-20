#!/usr/bin/env python3
"""Debug: Check what's actually in the glossary index for 'ticket system'"""

import re
from pathlib import Path
from typing import Dict, Set, Tuple, List

class DebugTooltipConverter:
    def __init__(self, glossary_dir: Path, lang: str = "en"):
        self.glossary_dir = glossary_dir
        self.lang = lang
        self.glossary_index: Dict[str, Tuple[str, str]] = {}
        self.load_glossary()
    
    def load_glossary(self):
        print(f"Loading glossary from {self.glossary_dir}\n")
        
        count = 0
        for md_file in self.glossary_dir.glob("*.md"):
            if md_file.name == "_index.md":
                continue
            
            try:
                content = md_file.read_text(encoding='utf-8')
                title, url = self._extract_title_and_url(content, md_file)
                
                if title and url:
                    variations = self._get_keyword_variations(title)
                    
                    # Debug: Check for conflicts
                    for variant in variations:
                        normalized = self._normalize_keyword(variant)
                        if normalized:
                            if normalized == "ticket system":
                                print(f"Found 'ticket system' variation from:")
                                print(f"  File: {md_file.name}")
                                print(f"  Title: '{title}'")
                                print(f"  URL: {url}")
                                if normalized in self.glossary_index:
                                    existing_title, existing_url = self.glossary_index[normalized]
                                    print(f"  ⚠️  CONFLICT! Already indexed as:")
                                    print(f"    Title: '{existing_title}'")
                                    print(f"    URL: {existing_url}")
                                print()
                            
                            if normalized not in self.glossary_index:
                                self.glossary_index[normalized] = (title, url)
                    count += 1
            except Exception as e:
                print(f"Error loading {md_file.name}: {e}")
        
        print(f"Loaded {count} glossary entries")
        print(f"Generated {len(self.glossary_index)} keyword variations\n")
        
        # Final check
        if "ticket system" in self.glossary_index:
            title, url = self.glossary_index["ticket system"]
            print(f"✅ 'ticket system' IS in index:")
            print(f"   Title: '{title}'")
            print(f"   URL: {url}")
        else:
            print(f"❌ 'ticket system' NOT in index")
    
    def _extract_title_and_url(self, content: str, filepath: Path) -> Tuple[str, str]:
        fm_match = re.search(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
        if not fm_match:
            return None, None
        
        frontmatter = fm_match.group(1)
        title_match = re.search(r'^title:\s*["\']?(.+?)["\']?\s*$', frontmatter, re.MULTILINE)
        if not title_match:
            return None, None
        
        title = title_match.group(1).strip().strip('"').strip("'")
        slug = filepath.stem
        url = f"/{self.lang}/glossary/{slug}/"
        return title, url
    
    def _get_keyword_variations(self, title: str) -> Set[str]:
        variations = set()
        variations.add(title)
        
        if '(' in title and ')' in title:
            without_parens = re.sub(r'\s*\([^)]*\)\s*', '', title).strip()
            if without_parens:
                variations.add(without_parens)
            
            parens_content = re.findall(r'\(([^)]+)\)', title)
            for content in parens_content:
                content = content.strip()
                if content:
                    variations.add(content)
        
        all_variations = set(variations)
        for variant in all_variations:
            variations.add(self._normalize_keyword(variant))
            
            plural_forms = self._generate_plural_forms(variant)
            for plural in plural_forms:
                variations.add(plural)
                variations.add(self._normalize_keyword(plural))
        
        return variations
    
    def _generate_plural_forms(self, word: str) -> List[str]:
        forms = []
        normalized = word.lower().strip()
        
        if normalized.endswith('s'):
            singular = normalized[:-1]
            forms.append(singular)
            forms.append(word[:-1])
            
            if normalized.endswith('ies') and len(normalized) > 3:
                singular_y = normalized[:-3] + 'y'
                forms.append(singular_y)
                forms.append(word[:-3] + 'y')
            
            if normalized.endswith('ses') and len(normalized) > 3:
                singular_sis = normalized[:-2]
                forms.append(singular_sis)
                forms.append(word[:-2])
        else:
            forms.append(normalized + 's')
            forms.append(word + 's')
            
            if normalized.endswith('y') and len(normalized) > 1:
                if normalized[-2] not in 'aeiou':
                    plural_ies = normalized[:-1] + 'ies'
                    forms.append(plural_ies)
                    forms.append(word[:-1] + 'ies')
            
            if normalized.endswith(('s', 'x', 'z', 'ch', 'sh')):
                forms.append(normalized + 'es')
                forms.append(word + 'es')
        
        return forms
    
    def _normalize_keyword(self, text: str) -> str:
        return ' '.join(text.lower().strip().split())

# Run debug
glossary_dir = Path("/Users/TM-MBP1/Documents/GitHub/hugo-boilerplate/content/en/glossary")
converter = DebugTooltipConverter(glossary_dir, lang="en")
