#!/usr/bin/env python3
"""Debug script to check if Ticket-System.md is being indexed correctly"""

from pathlib import Path
import re

glossary_dir = Path("/Users/TM-MBP1/Documents/GitHub/hugo-boilerplate/content/en/glossary")

# Check if Ticket-System.md exists
ticket_system_file = glossary_dir / "Ticket-System.md"
print(f"Ticket-System.md exists: {ticket_system_file.exists()}")

if ticket_system_file.exists():
    content = ticket_system_file.read_text(encoding='utf-8')
    fm_match = re.search(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
    if fm_match:
        frontmatter = fm_match.group(1)
        title_match = re.search(r'^title:\s*["\']?(.+?)["\']?\s*$', frontmatter, re.MULTILINE)
        if title_match:
            title = title_match.group(1).strip().strip('"').strip("'")
            print(f"Title: '{title}'")
            print(f"Normalized: '{title.lower().strip()}'")
            
            # Check if it matches "ticket system"
            search_term = "ticket system"
            print(f"\nSearching for: '{search_term}'")
            print(f"Match: {title.lower().strip() == search_term}")
