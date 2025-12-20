#!/usr/bin/env python3
"""Test the tooltip pattern matching"""

import re

# Test tooltip from the blog file
test_tooltip = '''{{< tooltip text="A system that manages customer inquiries and requests individually as 'tickets,' tracking response status and history" >}}ticket system{{< /tooltip >}}'''

# Pattern from the script
tooltip_pattern = re.compile(
    r'\{\{<\s*tooltip\s+text="([^"]*)"\s*>\}\}(.*?)\{\{<\s*/tooltip\s*>\}\}',
    re.DOTALL
)

match = tooltip_pattern.search(test_tooltip)

if match:
    print("✅ Pattern matched!")
    print(f"Definition: '{match.group(1)}'")
    print(f"Keyword: '{match.group(2)}'")
    print(f"Keyword stripped: '{match.group(2).strip()}'")
    print(f"Keyword normalized: '{match.group(2).strip().lower()}'")
else:
    print("❌ Pattern did NOT match!")
