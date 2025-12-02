#!/usr/bin/env python3
"""
Simple linkbuilding tool for this project.

- Reads keyword rules from data/linkbuilding/<lang>.yaml
- Scans generated HTML files in public/ and replaces matching text with <a> links

This is a lightweight Python replacement for the original Go "linkbuilder" tool
that existed in themes/boilerplate/linkbuilding.

Usage (from scripts/ directory):

    python linkbuilder_py.py \
      --linkbuilding-dir ../data/linkbuilding \
      --public-dir ../public \
      --langs en,ja

Run this AFTER `hugo` has generated the public/ directory.

YAML format example (data/linkbuilding/en.yaml):

    keywords:
      - keyword: "autonomous agents"
        url: "/en/glossary/autonomous-agents/"
        exact: true
        priority: 10
        title: "Autonomous Agents glossary entry"

Requirements (already present in scripts/requirements.txt):
    pyyaml, tqdm

Note: This implementation does a simple text-based replacement on the full
HTML content. It is intentionally conservative and processes keywords
from higher to lower priority to reduce conflicting replacements.
"""

import argparse
import os
import re
from dataclasses import dataclass
from typing import List, Dict, Any

import yaml
from bs4 import BeautifulSoup, NavigableString
from tqdm import tqdm


@dataclass
class KeywordRule:
    keyword: str
    url: str
    exact: bool = False
    priority: int = 1
    title: str | None = None


def load_rules_for_lang(path: str) -> List[KeywordRule]:
    if not os.path.exists(path):
        print(f"[WARN] Linkbuilding config not found: {path}")
        return []

    with open(path, "r", encoding="utf-8") as f:
        data: Dict[str, Any] = yaml.safe_load(f) or {}

    raw_keywords = data.get("keywords", []) or []
    rules: List[KeywordRule] = []

    for entry in raw_keywords:
        if not isinstance(entry, dict):
            continue
        kw = entry.get("keyword")
        url = entry.get("url")
        if not kw or not url:
            continue
        rule = KeywordRule(
            keyword=str(kw),
            url=str(url),
            exact=bool(entry.get("exact", False)),
            priority=int(entry.get("priority", 1)),
            title=str(entry.get("title")) if entry.get("title") else None,
        )
        rules.append(rule)

    # Sort by priority (desc), then by keyword length (desc) to avoid shorter
    # keywords capturing text before longer ones.
    rules.sort(key=lambda r: (r.priority, len(r.keyword)), reverse=True)

    print(f"[INFO] Loaded {len(rules)} keyword rules from {path}")
    return rules


def build_pattern(rule: KeywordRule) -> re.Pattern:
    # Escape keyword for regex use
    escaped = re.escape(rule.keyword)

    if rule.exact:
        # Word boundary based, case-sensitive
        pattern = rf"\b({escaped})\b"
        flags = 0
    else:
        # Substring match, case-insensitive
        pattern = rf"({escaped})"
        flags = re.IGNORECASE

    return re.compile(pattern, flags)


def apply_rules_to_html(html: str, rules: List[KeywordRule]) -> str:
    """Apply link rules only to visible text nodes using BeautifulSoup.

    We skip head/script/style and operate only on NavigableString nodes that are
    not inside <a> already, to avoid corrupting attributes or titles.
    """

    soup = BeautifulSoup(html, "html.parser")

    # Tags whose text content we should never touch
    skip_parents = {"script", "style", "head", "title", "meta", "link"}

    # Precompile patterns per rule (as list, not dict keys)
    rule_patterns: list[tuple[KeywordRule, re.Pattern]] = [
        (r, build_pattern(r)) for r in rules
    ]

    # Iterate over all text nodes
    for text_node in soup.find_all(string=True):
        parent = text_node.parent
        if not isinstance(text_node, NavigableString):
            continue

        # Skip whitespace-only
        if not text_node.strip():
            continue

        # Skip if inside unwanted tags
        if parent and parent.name in skip_parents:
            continue

        # Skip if already inside a link
        if parent and parent.name == "a":
            continue

        original_text = str(text_node)
        new_fragments: list[str] = [original_text]

        # Apply rules in priority order; rebuild fragments each time
        for rule, pattern in rule_patterns:
            updated_fragments: list[str] = []
            title_attr = f' title="{rule.title}"' if rule.title else ""

            for frag in new_fragments:
                # Only operate on plain text fragments, not HTML snippets
                if "<" in frag or ">" in frag:
                    updated_fragments.append(frag)
                    continue

                def repl(m: re.Match) -> str:
                    text = m.group(1)
                    return f"<a href=\"{rule.url}\"{title_attr}>{text}</a>"

                replaced = pattern.sub(repl, frag)
                updated_fragments.append(replaced)

            new_fragments = updated_fragments

        # If nothing changed, continue
        new_text = "".join(new_fragments)
        if new_text == original_text:
            continue

        # Replace the text node with parsed HTML from new_text
        new_nodes = BeautifulSoup(new_text, "html.parser")
        text_node.replace_with(new_nodes)

    return str(soup)


def process_html_files(public_dir: str, rules_by_lang: Dict[str, List[KeywordRule]], langs: List[str]) -> None:
    # Collect all .html files under public_dir
    html_files: List[str] = []
    for root, _, files in os.walk(public_dir):
        for f in files:
            if f.endswith(".html"):
                html_files.append(os.path.join(root, f))

    if not html_files:
        print(f"[WARN] No HTML files found under {public_dir}")
        return

    print(f"[INFO] Processing {len(html_files)} HTML files in {public_dir}")

    for file_path in tqdm(html_files, desc="Linkbuilding"):
        rel = os.path.relpath(file_path, public_dir)
        rel_unix = rel.replace(os.sep, "/")

        # Skip glossary index listing pages; they already contain structured
        # links and our replacements can interfere with the card layout.
        if rel_unix.endswith("/glossary/index.html"):
            continue
        # Try to infer language from path: /en/... or /ja/...
        lang_for_file = None
        for lang in langs:
            if os.sep + lang + os.sep in os.sep + rel:
                lang_for_file = lang
                break

        # Fallback: if not matched, use first lang's rules
        if lang_for_file is None and langs:
            lang_for_file = langs[0]

        rules = rules_by_lang.get(lang_for_file or "", [])
        if not rules:
            continue

        try:
            with open(file_path, "r", encoding="utf-8") as f:
                original_html = f.read()
        except UnicodeDecodeError:
            # Skip files we cannot decode as UTF-8
            print(f"[WARN] Skipping non-UTF8 file: {rel}")
            continue

        new_html = apply_rules_to_html(original_html, rules)
        if new_html != original_html:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(new_html)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Simple linkbuilding for public HTML")
    parser.add_argument(
        "--linkbuilding-dir",
        type=str,
        default="../data/linkbuilding",
        help="Directory containing <lang>.yaml linkbuilding configs",
    )
    parser.add_argument(
        "--public-dir",
        type=str,
        default="../public",
        help="Directory containing generated HTML files",
    )
    parser.add_argument(
        "--langs",
        type=str,
        default="en,ja",
        help="Comma-separated list of languages to process (e.g. 'en,ja')",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    link_dir = os.path.abspath(args.linkbuilding_dir)
    public_dir = os.path.abspath(args.public_dir)
    langs = [x.strip() for x in args.langs.split(",") if x.strip()]

    print(f"[INFO] Linkbuilding directory: {link_dir}")
    print(f"[INFO] Public directory: {public_dir}")
    print(f"[INFO] Languages: {langs}")

    if not os.path.isdir(public_dir):
        print(f"[ERROR] Public directory not found: {public_dir}")
        return

    rules_by_lang: Dict[str, List[KeywordRule]] = {}
    for lang in langs:
        cfg_path = os.path.join(link_dir, f"{lang}.yaml")
        rules_by_lang[lang] = load_rules_for_lang(cfg_path)

    if all(not rules for rules in rules_by_lang.values()):
        print("[WARN] No keyword rules loaded for any language. Nothing to do.")
        return

    process_html_files(public_dir, rules_by_lang, langs)
    print("[INFO] Linkbuilding finished.")


if __name__ == "__main__":
    main()
