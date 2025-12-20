#!/usr/bin/env python3
"""Debug: Check what variations are generated for Ticket System"""

from pathlib import Path
import re
from typing import Set, List

def normalize_keyword(text: str) -> str:
    return ' '.join(text.lower().strip().split())

def generate_plural_forms(word: str) -> List[str]:
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

def get_keyword_variations(title: str) -> Set[str]:
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
        variations.add(normalize_keyword(variant))
        
        plural_forms = generate_plural_forms(variant)
        for plural in plural_forms:
            variations.add(plural)
            variations.add(normalize_keyword(plural))
    
    return variations

# Test with "Ticket System"
title = "Ticket System"
variations = get_keyword_variations(title)

print(f"Title: '{title}'")
print(f"\nGenerated {len(variations)} variations:")
for v in sorted(variations):
    print(f"  '{v}'")

# Check specific searches
searches = ["ticket system", "Ticket System", "ticket systems"]
print(f"\nSearching for:")
for search in searches:
    normalized = normalize_keyword(search)
    found = normalized in variations
    print(f"  '{search}' (normalized: '{normalized}'): {found}")
