#!/usr/bin/env python3
"""
Generate data/linkbuilding/<lang>.yaml automatically from glossary content.

- Scans content/<lang>/glossary/*.md
- Reads frontmatter (title, translationKey, url)
- Produces a YAML file in data/linkbuilding/<lang>.yaml with entries like:

  keywords:
    - keyword: "Autonomous Agents"
      url: "/en/glossary/autonomous-agents/"
      exact: true
      priority: 10
      title: "Autonomous Agents glossary entry"

Usage (from scripts/ directory):

    python generate_linkbuilding_yaml_from_glossary.py \
      --lang en \
      --content-dir ../content \
      --output ../data/linkbuilding/en.yaml

    python generate_linkbuilding_yaml_from_glossary.py \
      --lang ja \
      --content-dir ../content \
      --output ../data/linkbuilding/ja.yaml

Requirements: python-frontmatter, pyyaml, tqdm
"""

import argparse
import os
import pathlib
from typing import Any, Dict, List

import re
import yaml
from tqdm import tqdm


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate linkbuilding YAML from glossary content")
    parser.add_argument("--lang", required=True, help="Language code (e.g. en, ja)")
    parser.add_argument(
        "--content-dir",
        type=str,
        default="../content",
        help="Root content directory (containing <lang>/glossary)",
    )
    parser.add_argument(
        "--output",
        type=str,
        default=None,
        help="Output YAML path (default: ../data/linkbuilding/<lang>.yaml)",
    )
    parser.add_argument(
        "--section",
        type=str,
        default="glossary",
        help="Section name for glossary (default: glossary)",
    )
    return parser.parse_args()


def find_glossary_files(content_root: str, lang: str, section: str) -> List[pathlib.Path]:
    lang_dir = pathlib.Path(content_root).joinpath(lang, section)
    if not lang_dir.is_dir():
        print(f"[WARN] Glossary directory not found: {lang_dir}")
        return []

    files = sorted(lang_dir.glob("*.md"))
    print(f"[INFO] Found {len(files)} markdown files in {lang_dir}")
    return files


def build_slug(meta: Dict[str, Any], file_path: pathlib.Path) -> str:
    # Prefer translationKey, then explicit url, then file stem
    translation_key = meta.get("translationKey") or meta.get("translation_key")
    if translation_key:
        return str(translation_key).strip().strip("/")

    url = meta.get("url")
    if isinstance(url, str) and url.strip():
        # Extract last segment of URL (/en/glossary/slug/ -> slug)
        slug = url.strip().strip("/").split("/")[-1]
        return slug

    # Fallback: file name (without extension), lowercased
    return file_path.stem.strip().strip().lower()


def main() -> None:
    args = parse_args()

    content_root = os.path.abspath(args.content_dir)
    lang = args.lang
    section = args.section

    if args.output:
        output_path = pathlib.Path(args.output)
    else:
        output_path = pathlib.Path(content_root).parent.joinpath("data", "linkbuilding", f"{lang}.yaml")

    print(f"[INFO] Language: {lang}")
    print(f"[INFO] Content root: {content_root}")
    print(f"[INFO] Section: {section}")
    print(f"[INFO] Output YAML: {output_path}")

    files = find_glossary_files(content_root, lang, section)
    if not files:
        print("[WARN] No glossary files found. Nothing to do.")
        return

    keywords: List[Dict[str, Any]] = []

    for path in tqdm(files, desc=f"Processing {lang} glossary"):
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            print(f"[WARN] Skipping non-UTF8 file: {path}")
            continue

        # Extract frontmatter block between leading --- ... --- or +++ ... +++
        fm_match = re.match(r"^(---|\+\+\+)\n(.*?\n)(---|\+\+\+)\n",
                            text,
                            re.DOTALL)
        frontmatter_text = fm_match.group(2) if fm_match else ""

        # title
        title_match = re.search(r"^title:\s*\"?(?P<title>.+?)\"?\s*$",
                                frontmatter_text,
                                re.MULTILINE)
        if not title_match:
            continue
        title = title_match.group("title").strip()

        # translationKey (optional)
        tk_match = re.search(r"^translationKey:\s*\"?(?P<tk>.+?)\"?\s*$",
                             frontmatter_text,
                             re.MULTILINE)
        meta: Dict[str, Any] = {}
        meta["title"] = title
        if tk_match:
            meta["translationKey"] = tk_match.group("tk").strip()

        slug = build_slug(meta, path)

        # Build URL: /<lang>/<section>/<slug>/
        url = f"/{lang}/{section}/{slug}/"

        # Use a stable, high priority for glossary terms
        entry: Dict[str, Any] = {
            "keyword": str(title),
            "url": url,
            "exact": True,
            "priority": 10,
            "title": f"{title} glossary entry" if lang == "en" else f"{title} の用語集ページ",
        }
        keywords.append(entry)

    if not keywords:
        print("[WARN] No keywords generated. Nothing to write.")
        return

    # Ensure output directory exists
    output_path.parent.mkdir(parents=True, exist_ok=True)

    data: Dict[str, Any] = {"keywords": keywords}

    with output_path.open("w", encoding="utf-8") as f:
        yaml.safe_dump(data, f, sort_keys=False, allow_unicode=True)

    print(f"[INFO] Wrote {len(keywords)} keyword entries to {output_path}")


if __name__ == "__main__":
    main()
