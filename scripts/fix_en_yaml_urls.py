#!/usr/bin/env python3

import argparse
import difflib
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Set, Tuple

import yaml


@dataclass
class Suggestion:
    keyword: str
    old_url: str
    new_url: str
    reason: str
    score: float


_URL_LINE_RE = re.compile(r"^(?P<indent>\s*)url:\s*(?P<q>['\"]?)(?P<url>[^'\"\n]+)(?P=q)\s*$")


def slugify(text: str) -> str:
    s = text.strip().lower()
    # remove parenthetical content like (NLP)
    s = re.sub(r"\s*\([^)]*\)", "", s)
    # common punctuation to spaces
    s = re.sub(r"[\\/,:;]+", " ", s)
    s = re.sub(r"[^a-z0-9\s-]", "", s)
    s = re.sub(r"\s+", "-", s)
    s = re.sub(r"-+", "-", s)
    return s.strip("-")


def existing_en_glossary_urls(public_dir: Path) -> Set[str]:
    base = public_dir / "en" / "glossary"
    if not base.exists():
        return set()

    urls: Set[str] = set()
    for p in base.iterdir():
        if not p.is_dir():
            continue
        idx = p / "index.html"
        if idx.exists():
            urls.add(f"/en/glossary/{p.name}/")
    return urls


def url_exists(public_dir: Path, url: str) -> bool:
    if not url.startswith("/en/"):
        return True
    if not url.endswith("/"):
        url = url + "/"
    p = public_dir / url.lstrip("/") / "index.html"
    return p.exists()


def best_match_url(
    keyword: str,
    old_url: str,
    existing_urls: Set[str],
) -> Optional[Suggestion]:
    # Normalize
    old = old_url.strip()
    if not old.endswith("/"):
        old += "/"

    if old in existing_urls:
        return None

    # Candidate from keyword slug
    kslug = slugify(keyword)
    if kslug:
        cand = f"/en/glossary/{kslug}/"
        if cand in existing_urls:
            return Suggestion(keyword, old, cand, "slugify(keyword)", 1.0)

    # Candidate from old slug similarity
    old_slug = old.rstrip("/").split("/")[-1]
    existing_slugs = [u.rstrip("/").split("/")[-1] for u in existing_urls]

    # Try close matches
    matches = difflib.get_close_matches(old_slug, existing_slugs, n=5, cutoff=0.0)
    if matches:
        top = matches[0]
        score = difflib.SequenceMatcher(a=old_slug, b=top).ratio()

        # Heuristic: require high confidence and clear separation from 2nd
        second_score = 0.0
        if len(matches) > 1:
            second_score = difflib.SequenceMatcher(a=old_slug, b=matches[1]).ratio()

        if score >= 0.92 and (score - second_score) >= 0.03:
            cand = f"/en/glossary/{top}/"
            if cand in existing_urls:
                return Suggestion(keyword, old, cand, "close_match(old_slug)", score)

    # Try keyword slug similarity (use raw keyword too)
    if kslug:
        kmatches = difflib.get_close_matches(kslug, existing_slugs, n=5, cutoff=0.0)
        if kmatches:
            top = kmatches[0]
            score = difflib.SequenceMatcher(a=kslug, b=top).ratio()
            second_score = 0.0
            if len(kmatches) > 1:
                second_score = difflib.SequenceMatcher(a=kslug, b=kmatches[1]).ratio()
            if score >= 0.92 and (score - second_score) >= 0.03:
                cand = f"/en/glossary/{top}/"
                if cand in existing_urls:
                    return Suggestion(keyword, old, cand, "close_match(slugify(keyword))", score)

    return None


def compute_missing_and_suggestions(en_yaml: Path, public_dir: Path) -> Tuple[List[Tuple[str, str]], List[Suggestion]]:
    data = yaml.safe_load(en_yaml.read_text(encoding="utf-8")) or {}
    items = data.get("keywords", []) or []

    existing_urls = existing_en_glossary_urls(public_dir)

    missing: List[Tuple[str, str]] = []
    suggestions: List[Suggestion] = []

    for it in items:
        if not isinstance(it, dict):
            continue
        kw = (it.get("keyword") or "").strip()
        url = (it.get("url") or "").strip()
        if not url.startswith("/en/"):
            continue
        if not url_exists(public_dir, url):
            missing.append((kw, url))
            sug = best_match_url(kw, url, existing_urls)
            if sug:
                suggestions.append(sug)

    return missing, suggestions


def apply_line_replacements(en_yaml: Path, mapping: Dict[str, str]) -> int:
    # mapping keys should be normalized with trailing slash
    lines = en_yaml.read_text(encoding="utf-8").splitlines(keepends=True)
    changed = 0

    for i, raw in enumerate(lines):
        m = _URL_LINE_RE.match(raw.rstrip("\n"))
        if not m:
            continue
        url = m.group("url").strip()
        if not url.endswith("/"):
            url_norm = url + "/"
        else:
            url_norm = url

        if url_norm not in mapping:
            continue

        new_url = mapping[url_norm]
        # preserve original trailing slash style
        if not url.endswith("/") and new_url.endswith("/"):
            new_url_out = new_url.rstrip("/")
        else:
            new_url_out = new_url

        indent = m.group("indent")
        q = m.group("q")
        lines[i] = f"{indent}url: {q}{new_url_out}{q}\n"
        changed += 1

    if changed:
        en_yaml.write_text("".join(lines), encoding="utf-8")

    return changed


def main() -> int:
    parser = argparse.ArgumentParser(description="Fix missing /en/glossary URLs in data/linkbuilding/en.yaml by matching existing public/en/glossary slugs.")
    parser.add_argument("--en-yaml", default="data/linkbuilding/en.yaml")
    parser.add_argument("--public-dir", default="public")
    parser.add_argument("--apply", action="store_true", help="Write changes to en.yaml")
    parser.add_argument("--max-report", type=int, default=50)

    args = parser.parse_args()
    en_yaml = Path(args.en_yaml)
    public_dir = Path(args.public_dir)

    missing, suggestions = compute_missing_and_suggestions(en_yaml, public_dir)

    print(f"Missing targets in en.yaml (based on public/): {len(missing)}")
    print(f"High-confidence auto-fix suggestions: {len(suggestions)}")

    if suggestions:
        print("\nSuggestions (top):")
        for s in suggestions[: args.max_report]:
            print(f"- {s.keyword}: {s.old_url} -> {s.new_url} ({s.reason}, {s.score:.2f})")
        if len(suggestions) > args.max_report:
            print(f"... and {len(suggestions) - args.max_report} more")

    if not args.apply:
        print("\nDRY-RUN: no files modified (re-run with --apply)")
        return 0

    mapping = {s.old_url: s.new_url for s in suggestions}
    changed = apply_line_replacements(en_yaml, mapping)
    print(f"\nAPPLY MODE: updated {changed} url: lines in {en_yaml}")
    print("NOTE: Remaining missing URLs still need manual resolution.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
