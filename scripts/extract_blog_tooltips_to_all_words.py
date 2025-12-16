#!/usr/bin/env python3

import argparse
import csv
import html
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Set, Tuple

import yaml


@dataclass(frozen=True)
class TooltipTerm:
    keyword: str
    definition: str
    glossary_slug: Optional[str]


TOOLTIP_RE = re.compile(
    r"\{\{<\s*tooltip\s+text=\"(?P<text>[^\"]*)\"\s*>\}\}(?P<body>.*?)\{\{<\s*/tooltip\s*>\}\}",
    re.DOTALL,
)

MD_LINK_RE = re.compile(r"^\[(?P<text>[^\]]+)\]\((?P<url>[^)]+)\)$")
MD_LINK_ANY_RE = re.compile(r"\[(?P<text>[^\]]+)\]\((?P<url>[^)]+)\)")


def iter_markdown_files(root: Path) -> Iterable[Path]:
    for p in sorted(root.rglob("*.md")):
        if p.is_file():
            yield p


def strip_fenced_code(text: str) -> str:
    lines = text.splitlines(keepends=True)
    out: List[str] = []
    in_fence = False
    for line in lines:
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            out.append("\n")
            continue
        if in_fence:
            out.append("\n")
        else:
            out.append(line)
    return "".join(out)


def extract_terms_from_markdown(md: str) -> List[TooltipTerm]:
    md = strip_fenced_code(md)

    terms: List[TooltipTerm] = []
    for m in TOOLTIP_RE.finditer(md):
        text_raw = html.unescape(m.group("text").strip())
        body_raw = m.group("body").strip()

        keyword = body_raw
        glossary_slug: Optional[str] = None

        def _replace_links_and_capture_slug(s: str) -> str:
            nonlocal glossary_slug

            def repl(match: re.Match) -> str:
                nonlocal glossary_slug
                url = match.group("url").strip()
                parts = url.strip().strip("/").split("/")
                if len(parts) >= 3 and parts[-2] == "glossary":
                    glossary_slug = glossary_slug or parts[-1].lower()
                return match.group("text")

            return MD_LINK_ANY_RE.sub(repl, s)

        # Normalize keyword body: replace any markdown links with link text.
        keyword = _replace_links_and_capture_slug(keyword)

        # Also normalize definition text.
        definition = _replace_links_and_capture_slug(text_raw)

        # If the entire body is a single markdown link, prefer its slug.
        link_m = MD_LINK_RE.match(body_raw)
        if link_m:
            url = link_m.group("url").strip()
            parts = url.strip().strip("/").split("/")
            if len(parts) >= 3 and parts[-2] == "glossary":
                glossary_slug = parts[-1].lower()

        keyword = html.unescape(keyword).replace("`", "").replace("**", "").replace("*", "").strip()
        keyword = re.sub(r"\s+", " ", keyword)
        definition = html.unescape(definition).replace("`", "").strip()

        if keyword and definition:
            terms.append(TooltipTerm(keyword=keyword, definition=definition, glossary_slug=glossary_slug))

    return terms


def load_csv_existing(all_words_csv: Path) -> Tuple[Set[str], Dict[str, Tuple[str, str]]]:
    """Returns (existing_keyword_keys, meta_by_keyword_key).

    meta_by_keyword_key maps normalized keyword -> (category, filename)
    """
    existing: Set[str] = set()
    meta: Dict[str, Tuple[str, str]] = {}

    with all_words_csv.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            kw = (row.get("Keyword") or "").strip()
            if not kw:
                continue
            key = kw.casefold()
            existing.add(key)
            cat = (row.get("Category") or "").strip()
            fn = (row.get("filename") or "").strip()
            if key not in meta:
                meta[key] = (cat, fn)

    return existing, meta


def load_glossary_index(glossary_dir: Path) -> Tuple[Dict[str, str], Dict[str, str]]:
    """Return (filename_by_slug, category_by_slug) where slug is stem.lower()."""
    filename_by_slug: Dict[str, str] = {}
    category_by_slug: Dict[str, str] = {}

    for p in glossary_dir.glob("*.md"):
        if not p.is_file() or p.name == "_index.md":
            continue
        slug = p.stem.lower()
        filename_by_slug[slug] = p.name

        try:
            raw = p.read_text(encoding="utf-8")
        except Exception:
            continue

        fm_match = re.match(r"^---\s*\n(.*?)\n---\s*\n", raw, re.DOTALL)
        if not fm_match:
            continue
        try:
            fm = yaml.safe_load(fm_match.group(1)) or {}
        except Exception:
            fm = {}
        cat = fm.get("category")
        if isinstance(cat, str) and cat.strip():
            category_by_slug[slug] = cat.strip()

    return filename_by_slug, category_by_slug


def normalize_filename_from_keyword(keyword: str) -> str:
    s = keyword.strip()
    s = s.replace("/", "---")
    s = s.replace("(", "--")
    s = s.replace(")", "-")
    s = re.sub(r"\s+", "-", s)
    s = re.sub(r"[^A-Za-z0-9\-_'’]", "-", s)
    s = re.sub(r"-{4,}", "---", s)
    if not s.endswith(".md"):
        s = f"{s}.md"
    return s


def ensure_unique_filename(filename: str, reserved: Set[str]) -> str:
    if filename not in reserved:
        reserved.add(filename)
        return filename

    stem = filename
    suffix = ""
    if filename.lower().endswith(".md"):
        stem = filename[:-3]
        suffix = ".md"

    i = 2
    while True:
        candidate = f"{stem}-{i}{suffix}"
        if candidate not in reserved:
            reserved.add(candidate)
            return candidate
        i += 1


def infer_category(
    term: TooltipTerm,
    *,
    default_category: str,
    existing_meta_by_keyword: Dict[str, Tuple[str, str]],
    glossary_category_by_slug: Dict[str, str],
) -> str:
    if term.glossary_slug:
        cat = glossary_category_by_slug.get(term.glossary_slug)
        if cat:
            return cat

    meta = existing_meta_by_keyword.get(term.keyword.casefold())
    if meta and meta[0]:
        return meta[0]

    return default_category


def infer_filename(
    term: TooltipTerm,
    *,
    existing_meta_by_keyword: Dict[str, Tuple[str, str]],
    glossary_filename_by_slug: Dict[str, str],
    reserved_filenames: Set[str],
) -> str:
    if term.glossary_slug:
        existing_fn = glossary_filename_by_slug.get(term.glossary_slug)
        if existing_fn:
            reserved_filenames.add(existing_fn)
            return existing_fn

    meta = existing_meta_by_keyword.get(term.keyword.casefold())
    if meta and meta[1]:
        reserved_filenames.add(meta[1])
        return meta[1]

    filename = normalize_filename_from_keyword(term.keyword)
    return ensure_unique_filename(filename, reserved_filenames)


def append_to_all_words_csv(
    all_words_csv: Path,
    rows: List[Dict[str, str]],
    *,
    dry_run: bool,
) -> None:
    if dry_run:
        return

    # Ensure the CSV ends with a newline before appending, otherwise the first
    # appended row may be concatenated onto the last existing line.
    try:
        last = all_words_csv.read_bytes()[-1:]
    except Exception:
        last = b"\n"
    needs_newline = last not in (b"\n", b"\r")

    with all_words_csv.open("a", encoding="utf-8", newline="") as f:
        if needs_newline:
            f.write("\n")
        writer = csv.DictWriter(f, fieldnames=["Keyword", "Definition", "Category", "filename"])
        for row in rows:
            writer.writerow(row)


def write_flowhunt_csv(flowhunt_csv: Path, rows: List[Dict[str, str]], *, dry_run: bool) -> None:
    if dry_run:
        return

    with flowhunt_csv.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["flow_input", "filename"])
        writer.writeheader()
        for row in rows:
            flow_input = (
                f"Create an English glossary entry.\n\n"
                f"TERM: {row['Keyword']}\n"
                f"DEFINITION (short): {row['Definition']}\n"
                f"CATEGORY: {row['Category']}\n"
            )
            writer.writerow({"flow_input": flow_input, "filename": row["filename"]})


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--blog-dir", default="content/en/blog")
    parser.add_argument("--glossary-dir", default="content/en/glossary")
    parser.add_argument("--all-words-csv", default="docs/all-words.csv")
    parser.add_argument("--flowhunt-csv-out", default="docs/glossaries_flowhunt.csv")
    parser.add_argument("--default-category", default="AI Chatbot & Automation")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    project_root = Path(__file__).resolve().parents[1]
    blog_dir = (project_root / args.blog_dir).resolve()
    glossary_dir = (project_root / args.glossary_dir).resolve()
    all_words_csv = (project_root / args.all_words_csv).resolve()
    flowhunt_csv = (project_root / args.flowhunt_csv_out).resolve()

    if not blog_dir.is_dir():
        raise SystemExit(f"Blog directory not found: {blog_dir}")
    if not glossary_dir.is_dir():
        raise SystemExit(f"Glossary directory not found: {glossary_dir}")
    if not all_words_csv.is_file():
        raise SystemExit(f"CSV not found: {all_words_csv}")

    existing_keywords, existing_meta = load_csv_existing(all_words_csv)
    glossary_filename_by_slug, glossary_category_by_slug = load_glossary_index(glossary_dir)

    reserved_filenames: Set[str] = set()
    for _, (_, fn) in existing_meta.items():
        if fn:
            reserved_filenames.add(fn)
    for _, fn in glossary_filename_by_slug.items():
        reserved_filenames.add(fn)

    extracted: List[TooltipTerm] = []
    for md_file in iter_markdown_files(blog_dir):
        text = md_file.read_text(encoding="utf-8")
        extracted.extend(extract_terms_from_markdown(text))

    new_rows: List[Dict[str, str]] = []
    newly_added_keyword_keys: Set[str] = set()

    for term in extracted:
        key = term.keyword.casefold()
        if key in existing_keywords or key in newly_added_keyword_keys:
            continue

        category = infer_category(
            term,
            default_category=args.default_category,
            existing_meta_by_keyword=existing_meta,
            glossary_category_by_slug=glossary_category_by_slug,
        )
        filename = infer_filename(
            term,
            existing_meta_by_keyword=existing_meta,
            glossary_filename_by_slug=glossary_filename_by_slug,
            reserved_filenames=reserved_filenames,
        )

        new_rows.append(
            {
                "Keyword": term.keyword,
                "Definition": term.definition,
                "Category": category,
                "filename": filename,
            }
        )
        newly_added_keyword_keys.add(key)

    if not new_rows:
        print("No new tooltip terms found.")
        return

    append_to_all_words_csv(all_words_csv, new_rows, dry_run=args.dry_run)
    write_flowhunt_csv(flowhunt_csv, new_rows, dry_run=args.dry_run)

    print(f"Found {len(extracted)} tooltip occurrences.")
    print(f"Appended {len(new_rows)} new rows to {all_words_csv}.")
    print(f"Wrote FlowHunt input CSV: {flowhunt_csv} ({len(new_rows)} rows).")


if __name__ == "__main__":
    main()
