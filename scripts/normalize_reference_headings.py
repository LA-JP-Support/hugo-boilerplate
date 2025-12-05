#!/usr/bin/env python3
"""Normalize reference section headings in glossary articles.

Replaces various reference-related headings with a consistent format:
- English: ## References
- Japanese: ## 参考資料
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

# Patterns to match reference headings (must be at start of line)
# Only match headings that contain "Reading", "Resources", "References", etc.
# Exclude "Related Terms", "Glossary of Terms", etc.
EN_HEADING_PATTERNS = [
    # Main patterns with Reading/Resources/References
    r"^## \*?\*?(?:\d+\.\s*)?(?:References?|Further|Additional|Authoritative|Recommended|Key|In-depth|Deep Dive|Suggested|Practical|Source|Expert|Industry|Visual|Video|Tools|FAQs)[^#\n]*(?:Reading|Resources?|References?|Learning|Exploration|Sources?|Tutorials?)[^#\n]*\*?\*?$",
    # Standalone patterns (exclude Visual Reference which is for diagrams)
    r"^## \*?\*?(?:\d+\.\s*)?(?:Further Reading|Further Resources|References|Additional Resources|Authoritative Resources|Authoritative References|Suggested Reading|Video Resources?|Tools and Resources|Further Learning|Further Exploration)\*?\*?$",
    r"^## \*?\*?(?:\d+\.\s*)?For Further Technical Reading\*?\*?$",
    r"^## \*?\*?(?:\d+\.\s*)?Conclusion and Further Resources\*?\*?$",
    # With & or /
    r"^## \*?\*?(?:\d+\.\s*)?(?:References?|Further Reading|Further Resources|Additional Resources|Authoritative Resources)\s*[&/]\s*(?:Further Reading|Resources?|References?|Next Steps)\*?\*?$",
]

JA_HEADING_PATTERNS = [
    # 参考文献/参考資料 + 何か
    r"^## \*?\*?(?:\d+\.\s*)?参考文献[^#\n]*\*?\*?$",
    r"^## \*?\*?(?:\d+\.\s*)?参考資料[^#\n]*\*?\*?$",
    # さらなる読み物系
    r"^## \*?\*?(?:\d+\.\s*)?さらなる読み物[^#\n]*\*?\*?$",
    r"^## \*?\*?(?:\d+\.\s*)?さらに読む[^#\n]*\*?\*?$",
    r"^## \*?\*?(?:\d+\.\s*)?さらに詳しく[^#\n]*\*?\*?$",
    r"^## \*?\*?(?:\d+\.\s*)?さらなる参考資料[^#\n]*\*?\*?$",
    # リソース系
    r"^## \*?\*?(?:\d+\.\s*)?(?:追加|権威ある|詳細な|推奨|業界|その他の|さらなる|関連)[^#\n]*リソース[^#\n]*\*?\*?$",
    # 関連概念系（参考文献/参考資料を含む）
    r"^## \*?\*?(?:\d+\.\s*)?関連概念[^#\n]*(?:参考文献|参考資料)[^#\n]*\*?\*?$",
    # まとめと参考資料
    r"^## \*?\*?(?:\d+\.\s*)?まとめと参考資料\*?\*?$",
    # 権威ある参考文献
    r"^## \*?\*?(?:\d+\.\s*)?権威ある参考文献\*?\*?$",
    # その他
    r"^## \*?\*?(?:\d+\.\s*)?ソースリンク[^#\n]*\*?\*?$",
    r"^## \*?\*?(?:\d+\.\s*)?エキスパート[^#\n]*リソース[^#\n]*\*?\*?$",
    r"^## \*?\*?(?:\d+\.\s*)?ビジュアル[^#\n]*リソース[^#\n]*\*?\*?$",
]


def normalize_headings(text: str, lang: str) -> str:
    """Replace reference headings with normalized version."""
    if lang == "en":
        patterns = EN_HEADING_PATTERNS
        replacement = "## References"
    else:
        patterns = JA_HEADING_PATTERNS
        replacement = "## 参考資料"
    
    updated = text
    for pattern in patterns:
        updated = re.sub(pattern, replacement, updated, flags=re.MULTILINE)
    
    return updated


def process_file(file_path: Path, dry_run: bool = False) -> bool:
    """Process a single file."""
    # Determine language from path
    if "/en/" in str(file_path):
        lang = "en"
    elif "/ja/" in str(file_path):
        lang = "ja"
    else:
        return False
    
    original = file_path.read_text(encoding="utf-8")
    updated = normalize_headings(original, lang)
    
    if updated == original:
        return False
    
    if dry_run:
        # Show what would change
        for i, (orig_line, new_line) in enumerate(zip(original.split('\n'), updated.split('\n'))):
            if orig_line != new_line:
                print(f"[DRY-RUN] {file_path}")
                print(f"  - {orig_line}")
                print(f"  + {new_line}")
        return True
    
    file_path.write_text(updated, encoding="utf-8")
    print(f"[OK] {file_path}")
    return True


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", help="File or directory to process")
    parser.add_argument("--dry-run", action="store_true", help="Show changes without applying")
    args = parser.parse_args()
    
    target = Path(args.path)
    
    if target.is_file():
        files = [target]
    else:
        files = sorted(target.rglob("*.md"))
    
    changed = 0
    for f in files:
        if process_file(f, args.dry_run):
            changed += 1
    
    print(f"Processed {len(files)} file(s); updated {changed}")


if __name__ == "__main__":
    main()
