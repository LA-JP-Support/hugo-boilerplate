#!/usr/bin/env python3
"""
Validate Hugo frontmatter for all content types.

Checks required fields, field types, and cross-file consistency
(e.g. translationKey matching between EN/JA).

Usage:
    # Validate a single file
    python scripts/validate_frontmatter.py content/ja/blog/my-article.md

    # Validate a directory
    python scripts/validate_frontmatter.py content/ja/glossary/

    # Validate all content
    python scripts/validate_frontmatter.py --all

    # Check translationKey consistency between EN/JA
    python scripts/validate_frontmatter.py --check-translations

    # Show only errors (no warnings/info)
    python scripts/validate_frontmatter.py --errors-only content/ja/blog/
"""

import argparse
import sys
from pathlib import Path
from collections import defaultdict

try:
    import frontmatter
except ImportError:
    print("Error: python-frontmatter is required.")
    print("Install: pip install python-frontmatter")
    sys.exit(1)


# ---------------------------------------------------------------------------
# Content type detection
# ---------------------------------------------------------------------------

def detect_content_type(filepath: Path, meta: dict) -> str:
    """Detect content type from path and frontmatter."""
    parts = filepath.parts
    # Normalise to posix-style segments for matching
    path_str = filepath.as_posix()

    # Explicit type field
    fm_type = meta.get("type", "")

    if fm_type == "support" or "/support/" in path_str:
        return "support"
    if fm_type == "services" or "/services/" in path_str:
        return "services"
    if fm_type == "glossary" or "/glossary/" in path_str:
        return "glossary"

    # YouTube blog variant
    if "/blog/" in path_str:
        if meta.get("layout") == "single-youtube":
            return "blog-youtube"
        return "blog"

    return "unknown"


# ---------------------------------------------------------------------------
# Validation rules per content type
# ---------------------------------------------------------------------------

# (field_name, required, expected_type_or_None, description)
# expected_type: str, list, bool, int, dict, or None (any)

COMMON_FIELDS = [
    ("title",          True,  str,  "Page title"),
    ("description",    True,  str,  "Meta description"),
    ("draft",          False, bool, "Draft flag"),
    ("translationKey", True,  str,  "Multilingual linking key"),
]

RULES = {
    "glossary": COMMON_FIELDS + [
        ("date",       True,  None, "Creation date"),
        ("lastmod",    False, None, "Last modification date"),
        ("keywords",   True,  list, "SEO keywords list"),
        ("category",   False, str,  "Glossary category"),
        ("type",       True,  str,  "Must be 'glossary'"),
        ("url",        False, str,  "Explicit URL path (required for JA)"),
    ],
    "glossary_ja": COMMON_FIELDS + [
        ("date",       True,  None, "Creation date"),
        ("lastmod",    False, None, "Last modification date"),
        ("keywords",   True,  list, "SEO keywords list"),
        ("category",   False, str,  "Glossary category"),
        ("type",       True,  str,  "Must be 'glossary'"),
        ("url",        True,  str,  "Explicit URL path"),
        ("e-title",    True,  str,  "English title for JA glossary"),
        ("term",       True,  str,  "Reading / kana for search"),
    ],
    "blog": COMMON_FIELDS + [
        ("date",       True,  None, "Creation date"),
        ("lastmod",    False, None, "Last modification date"),
        ("keywords",   True,  list, "SEO keywords list"),
        ("tags",       False, list, "Tags"),
        ("categories", False, list, "Categories"),
        ("url",        True,  str,  "Explicit URL path"),
        ("image",      False, str,  "OG image path"),
    ],
    "blog-youtube": COMMON_FIELDS + [
        ("date",           True,  None, "Creation date"),
        ("lastmod",        False, None, "Last modification date"),
        ("layout",         True,  str,  "Must be 'single-youtube'"),
        ("youtubeVideoID", True,  str,  "YouTube video ID"),
        ("youtubeTitle",   True,  str,  "YouTube video title"),
        ("keywords",       True,  list, "SEO keywords list"),
        ("tags",           False, list, "Tags"),
        ("categories",     False, list, "Categories"),
        ("url",            True,  str,  "Explicit URL path"),
        ("image",          False, str,  "OG image (YouTube thumbnail)"),
    ],
    "services": [
        ("title",          True,  str,  "Service name"),
        ("description",    True,  str,  "Service description"),
        ("type",           True,  str,  "Must be 'services'"),
        ("translationKey", False, str,  "Multilingual linking key"),
        ("badge",          False, str,  "Hero badge text"),
        ("hero_heading",   False, str,  "Hero heading"),
        ("hero_description", False, str, "Hero description"),
        ("features",       False, list, "Feature list"),
    ],
    "support": [
        ("title",          True,  str,  "Article title"),
        ("description",    True,  str,  "Article description"),
        ("type",           True,  str,  "Must be 'support'"),
        ("translationKey", False, str,  "Multilingual linking key"),
        ("weight",         True,  int,  "Display order weight"),
    ],
    "support_article": [
        ("title",          True,  str,  "Article title"),
        ("description",    True,  str,  "Article description"),
        ("type",           True,  str,  "Must be 'support'"),
        ("translationKey", True,  str,  "Multilingual linking key"),
        ("date",           True,  None, "Creation date"),
        ("weight",         True,  int,  "Display order weight"),
        ("keywords",       False, list, "SEO keywords"),
    ],
    "unknown": COMMON_FIELDS,
}


# ---------------------------------------------------------------------------
# Validators
# ---------------------------------------------------------------------------

def validate_file(filepath: Path) -> list[dict]:
    """Validate a single Markdown file. Returns list of issue dicts."""
    issues = []

    # Parse frontmatter
    try:
        post = frontmatter.load(str(filepath))
    except Exception as e:
        issues.append(issue("ERROR", "parse", f"Failed to parse frontmatter: {e}", filepath))
        return issues

    meta = dict(post.metadata)
    ctype = detect_content_type(filepath, meta)

    # Determine which rule set to use
    if ctype == "glossary" and is_ja(filepath):
        rule_key = "glossary_ja"
    elif ctype == "support" and filepath.name == "_index.md":
        rule_key = "support"
    elif ctype == "support":
        rule_key = "support_article"
    else:
        rule_key = ctype

    rules = RULES.get(rule_key, RULES["unknown"])

    # Check each required/typed field
    for field, required, expected_type, desc in rules:
        value = meta.get(field)

        if value is None or value == "" or value == []:
            if required:
                issues.append(issue("ERROR", "missing_field",
                    f"Required field '{field}' is missing or empty ({desc})", filepath))
            continue

        if expected_type is not None and not isinstance(value, expected_type):
            issues.append(issue("WARNING", "wrong_type",
                f"Field '{field}' expected {expected_type.__name__}, got {type(value).__name__}: {repr(value)[:80]}",
                filepath))

    # Content-type specific value checks
    issues.extend(check_type_values(filepath, meta, ctype))

    # Description quality check
    desc_val = meta.get("description", "")
    if isinstance(desc_val, str) and len(desc_val) > 200:
        issues.append(issue("INFO", "long_description",
            f"Description is {len(desc_val)} chars (recommended: ≤160 for SEO)", filepath))

    return issues


def check_type_values(filepath: Path, meta: dict, ctype: str) -> list[dict]:
    """Value-level checks specific to content types."""
    issues = []

    if ctype == "glossary":
        if meta.get("type") and meta["type"] != "glossary":
            issues.append(issue("ERROR", "wrong_type_value",
                f"type should be 'glossary', got '{meta['type']}'", filepath))

    if ctype == "blog-youtube":
        if meta.get("layout") != "single-youtube":
            issues.append(issue("ERROR", "wrong_layout",
                f"layout must be 'single-youtube' for YouTube blog, got '{meta.get('layout')}'",
                filepath))
        vid = meta.get("youtubeVideoID", "")
        if vid and len(vid) < 5:
            issues.append(issue("WARNING", "short_video_id",
                f"youtubeVideoID looks too short: '{vid}'", filepath))

    if ctype == "services":
        if meta.get("type") and meta["type"] != "services":
            issues.append(issue("ERROR", "wrong_type_value",
                f"type should be 'services', got '{meta['type']}'", filepath))

    if ctype in ("support", "support_article"):
        if meta.get("type") and meta["type"] != "support":
            issues.append(issue("ERROR", "wrong_type_value",
                f"type should be 'support', got '{meta['type']}'", filepath))

    # URL should start with /
    url_val = meta.get("url", "")
    if isinstance(url_val, str) and url_val and not url_val.startswith("/") and not url_val.startswith("blog/"):
        issues.append(issue("INFO", "url_format",
            f"url '{url_val}' does not start with '/' — verify this is intentional", filepath))

    return issues


# ---------------------------------------------------------------------------
# Translation consistency check
# ---------------------------------------------------------------------------

def check_translation_keys(repo_root: Path) -> list[dict]:
    """Check that translationKey values match between EN and JA."""
    issues = []
    en_keys = {}  # translationKey -> filepath
    ja_keys = {}

    for lang, store in [("en", en_keys), ("ja", ja_keys)]:
        content_dir = repo_root / "content" / lang
        if not content_dir.exists():
            continue
        for md in content_dir.rglob("*.md"):
            if md.name == "_index.md":
                continue
            try:
                post = frontmatter.load(str(md))
                tk = post.metadata.get("translationKey", "")
                if tk:
                    store[tk] = md
            except Exception:
                pass

    # Find orphans
    en_only = set(en_keys.keys()) - set(ja_keys.keys())
    ja_only = set(ja_keys.keys()) - set(en_keys.keys())

    for tk in sorted(en_only):
        issues.append(issue("WARNING", "missing_ja_translation",
            f"translationKey '{tk}' exists in EN but not JA", en_keys[tk]))

    for tk in sorted(ja_only):
        issues.append(issue("WARNING", "missing_en_translation",
            f"translationKey '{tk}' exists in JA but not EN", ja_keys[tk]))

    return issues


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def issue(severity: str, itype: str, message: str, filepath: Path = None) -> dict:
    return {
        "severity": severity,
        "type": itype,
        "message": message,
        "file": str(filepath) if filepath else None,
    }


def is_ja(filepath: Path) -> bool:
    return "/ja/" in filepath.as_posix()


def collect_files(target: Path) -> list[Path]:
    """Collect .md files from a file or directory."""
    if target.is_file():
        return [target]
    if target.is_dir():
        return sorted(target.rglob("*.md"))
    return []


# ---------------------------------------------------------------------------
# Report
# ---------------------------------------------------------------------------

def print_report(all_issues: list[dict], errors_only: bool = False):
    """Print a formatted report."""
    if errors_only:
        all_issues = [i for i in all_issues if i["severity"] == "ERROR"]

    if not all_issues:
        print("✅ No issues found!")
        return 0

    # Group by file
    by_file = defaultdict(list)
    for iss in all_issues:
        key = iss.get("file") or "(cross-file)"
        by_file[key].append(iss)

    errors = sum(1 for i in all_issues if i["severity"] == "ERROR")
    warnings = sum(1 for i in all_issues if i["severity"] == "WARNING")
    infos = sum(1 for i in all_issues if i["severity"] == "INFO")

    print("=" * 70)
    print(f"FRONTMATTER VALIDATION REPORT")
    print(f"  Files with issues: {len(by_file)}")
    print(f"  Errors: {errors}  Warnings: {warnings}  Info: {infos}")
    print("=" * 70)

    severity_icon = {"ERROR": "❌", "WARNING": "⚠️ ", "INFO": "ℹ️ "}

    for fpath, file_issues in sorted(by_file.items()):
        print(f"\n📄 {fpath}")
        for iss in file_issues:
            icon = severity_icon.get(iss["severity"], "?")
            print(f"  {icon} [{iss['severity']}] {iss['message']}")

    print()
    return 1 if errors > 0 else 0


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Validate Hugo frontmatter for all content types."
    )
    parser.add_argument(
        "target", nargs="?", default=None,
        help="File or directory to validate"
    )
    parser.add_argument(
        "--all", action="store_true",
        help="Validate all content/ files"
    )
    parser.add_argument(
        "--check-translations", action="store_true",
        help="Check translationKey consistency between EN/JA"
    )
    parser.add_argument(
        "--errors-only", action="store_true",
        help="Show only errors (no warnings/info)"
    )
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parent.parent

    if not args.target and not args.all and not args.check_translations:
        parser.print_help()
        sys.exit(1)

    all_issues = []

    # File / directory validation
    if args.all:
        target = repo_root / "content"
        files = collect_files(target)
    elif args.target:
        target = Path(args.target)
        if not target.is_absolute():
            target = repo_root / target
        files = collect_files(target)
    else:
        files = []

    if files:
        print(f"Validating {len(files)} file(s)...")
        for f in files:
            all_issues.extend(validate_file(f))

    # Translation consistency
    if args.check_translations:
        print("Checking translationKey consistency...")
        all_issues.extend(check_translation_keys(repo_root))

    exit_code = print_report(all_issues, errors_only=args.errors_only)
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
