#!/usr/bin/env python3

import argparse
import re
from pathlib import Path
from typing import Dict, List, Optional, Sequence, Set, Tuple


_FRONTMATTER_YAML_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
_FRONTMATTER_TOML_RE = re.compile(r"^\+\+\+\s*\n(.*?)\n\+\+\+\s*\n", re.DOTALL)


def _split_frontmatter(content: str) -> Tuple[str, str]:
    m = _FRONTMATTER_YAML_RE.search(content)
    if m:
        fm = m.group(0)
        return fm, content[len(fm):]

    m = _FRONTMATTER_TOML_RE.search(content)
    if m:
        fm = m.group(0)
        return fm, content[len(fm):]

    return "", content


def _extract_frontmatter_value(frontmatter: str, key: str) -> Optional[str]:
    # YAML: key: "value" OR key: value
    yaml_pat = re.compile(rf"^{re.escape(key)}:\s*[\"']?(.+?)[\"']?\s*$", re.MULTILINE)
    m = yaml_pat.search(frontmatter)
    if m:
        return m.group(1).strip()

    # TOML: key = "value" OR key = 'value'
    toml_pat = re.compile(rf"^{re.escape(key)}\s*=\s*[\"'](.+?)[\"']\s*$", re.MULTILINE)
    m = toml_pat.search(frontmatter)
    if m:
        return m.group(1).strip()

    return None


def _normalize_keyword(s: str) -> str:
    s = s.lower()
    s = re.sub(r"[\s\-_]+", " ", s)
    s = re.sub(r"[^a-z0-9\s]", "", s)
    return re.sub(r"\s+", " ", s).strip()


def _collect_keyword_variations(title: str) -> Set[str]:
    variations: Set[str] = {title}

    # Handle formats like: "ITIL – Information Technology Infrastructure Library"
    if "–" in title or "—" in title or " - " in title:
        parts = re.split(r"\s*[–—-]\s*", title, maxsplit=1)
        for p in parts:
            p = p.strip()
            if p:
                variations.add(p)

    # Parenthetical content: "User Experience (UX)"
    paren = re.findall(r"\(([^)]+)\)", title)
    for p in paren:
        p = p.strip()
        if p:
            variations.add(p)

    return variations


def _protect_segments(pattern: re.Pattern, text: str, store: List[str], token_prefix: str) -> str:
    def repl(m: re.Match) -> str:
        store.append(m.group(0))
        return f"{token_prefix}{len(store) - 1}@@"

    return pattern.sub(repl, text)


def _restore_segments(text: str, store: Sequence[str], token_prefix: str) -> str:
    def repl(m: re.Match) -> str:
        idx = int(m.group(1))
        return store[idx]

    token_re = re.compile(re.escape(token_prefix) + r"(\d+)@@")
    return token_re.sub(repl, text)


def _normalize_bold_links(text: str) -> str:
    stores: Dict[str, List[str]] = {
        "fences": [],
        "inline": [],
        "html": [],
        "shortcodes": [],
    }

    masked = text
    masked = _protect_segments(
        re.compile(r"```[\s\S]*?```", re.MULTILINE),
        masked,
        stores["fences"],
        "@@FENCE",
    )
    masked = _protect_segments(
        re.compile(r"`[^`\n]+`"),
        masked,
        stores["inline"],
        "@@INLINE",
    )
    masked = _protect_segments(
        re.compile(r"<[^>]+>"),
        masked,
        stores["html"],
        "@@HTML",
    )
    masked = _protect_segments(
        re.compile(r"\{\{[<%][\s\S]*?[>%]\}\}"),
        masked,
        stores["shortcodes"],
        "@@SC",
    )

    masked = re.sub(
        r"\*\*\[([^\]]+)\]\(([^)\s]+)\)([^*\n]+?)\*\*",
        r"[**\1**](\2)**\3**",
        masked,
    )
    masked = re.sub(
        r"\*\*\[([^\]]+)\]\(([^)\s]+)\)\*\*",
        r"[**\1**](\2)",
        masked,
    )
    masked = re.sub(
        r"\*\*([^*\n]+?)\[([^\]]+)\]\(([^)\s]+)\)\*\*",
        r"**\1**[**\2**](\3)",
        masked,
    )
    masked = re.sub(r"\[([^\]]*?)\s+\]\(([^)]+)\)", r"[\1](\2)", masked)
    masked = re.sub(r"\*\*([^*\n]*?)\s+\*\*", r"**\1**", masked)

    restored = masked
    restored = _restore_segments(restored, stores["shortcodes"], "@@SC")
    restored = _restore_segments(restored, stores["html"], "@@HTML")
    restored = _restore_segments(restored, stores["inline"], "@@INLINE")
    restored = _restore_segments(restored, stores["fences"], "@@FENCE")
    return restored


class InternalLinkBuilder:
    def __init__(self, glossary_dir: Path, lang: str):
        self.glossary_dir = glossary_dir
        self.lang = lang
        self.glossary_index: Dict[str, Tuple[str, str]] = {}  # normalized -> (display_title, url)
        self._sorted_terms: List[Tuple[str, str, str]] = []  # (normalized, title, url)
        self._load_glossary()

    def _load_glossary(self) -> None:
        if not self.glossary_dir.exists():
            return

        for md_file in self.glossary_dir.glob("*.md"):
            if md_file.name == "_index.md":
                continue

            try:
                content = md_file.read_text(encoding="utf-8")
            except Exception:
                continue

            fm, _ = _split_frontmatter(content)
            if not fm:
                continue

            title = _extract_frontmatter_value(fm, "title")
            if not title:
                continue

            slug = md_file.stem
            url = f"/{self.lang}/glossary/{slug}/"

            for variant in _collect_keyword_variations(title):
                norm = _normalize_keyword(variant)
                if norm and norm not in self.glossary_index:
                    self.glossary_index[norm] = (title, url)

        self._sorted_terms = sorted(
            [(k, v[0], v[1]) for k, v in self.glossary_index.items()],
            key=lambda x: len(x[0]),
            reverse=True,
        )

    def add_links_to_content(self, content: str, current_url: str) -> Tuple[str, int]:
        fm, body = _split_frontmatter(content)
        if not fm:
            return content, 0

        existing_links: Set[str] = set()
        for m in re.finditer(r"\[([^\]]+)\]\(([^)]+)\)", body):
            existing_links.add(_normalize_keyword(m.group(1)))

        # Protect segments where we never want replacements.
        stores: Dict[str, List[str]] = {
            "fences": [],
            "inline": [],
            "links": [],
            "html": [],
            "shortcodes": [],
        }

        protected = body

        protected = _protect_segments(
            re.compile(r"```[\s\S]*?```", re.MULTILINE),
            protected,
            stores["fences"],
            "@@FENCE",
        )
        protected = _protect_segments(
            re.compile(r"`[^`\n]+`"),
            protected,
            stores["inline"],
            "@@INLINE",
        )
        protected = _protect_segments(
            re.compile(r"\[[^\]]+\]\([^\)]+\)"),
            protected,
            stores["links"],
            "@@LINK",
        )
        protected = _protect_segments(
            re.compile(r"<[^>]+>"),
            protected,
            stores["html"],
            "@@HTML",
        )
        protected = _protect_segments(
            re.compile(r"\{\{[<%][\s\S]*?[>%]\}\}"),
            protected,
            stores["shortcodes"],
            "@@SC",
        )

        links_added = 0

        for normalized, title, url in self._sorted_terms:
            if url == current_url:
                continue
            if normalized in existing_links:
                continue

            term_count = 0
            max_links_per_term = 3

            # Word-ish boundary match (works for multi-word titles too)
            pattern = re.compile(rf"(?i)(?<![A-Za-z0-9_])({re.escape(title)})(?![A-Za-z0-9_])")

            def replace(m: re.Match) -> str:
                nonlocal term_count, links_added
                if term_count >= max_links_per_term:
                    return m.group(0)

                # Avoid linking inside a URL-like context
                start = m.start()
                prev = protected[start - 1] if start > 0 else ""
                if prev in ["/", ".", "@", "-"]:
                    return m.group(0)

                term_count += 1
                links_added += 1
                return f"[{m.group(1)}]({url})"

            protected = pattern.sub(replace, protected)

        # Restore protected segments.
        restored = protected
        restored = _restore_segments(restored, stores["shortcodes"], "@@SC")
        restored = _restore_segments(restored, stores["html"], "@@HTML")
        restored = _restore_segments(restored, stores["links"], "@@LINK")
        restored = _restore_segments(restored, stores["inline"], "@@INLINE")
        restored = _restore_segments(restored, stores["fences"], "@@FENCE")

        restored = _normalize_bold_links(restored)

        return fm + restored, links_added

    def process_file(self, filepath: Path, dry_run: bool) -> Tuple[int, bool]:
        try:
            content = filepath.read_text(encoding="utf-8")
        except Exception:
            return 0, False

        fm, _ = _split_frontmatter(content)
        current_url = ""
        if fm:
            u = _extract_frontmatter_value(fm, "url")
            if u:
                current_url = u

        if not current_url:
            current_url = f"/{self.lang}/blog/{filepath.stem}/"

        modified, count = self.add_links_to_content(content, current_url)
        changed = modified != content
        if modified != content and not dry_run:
            filepath.write_text(modified, encoding="utf-8")
        return count, changed


def _iter_markdown_files(target: Path) -> List[Path]:
    if target.is_file():
        return [target]
    return sorted([p for p in target.rglob("*.md") if p.is_file()])


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=str, help="File or directory to process")
    parser.add_argument("--glossary-dir", required=True, type=str)
    parser.add_argument("--lang", required=True, type=str)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    target = Path(args.path)
    glossary_dir = Path(args.glossary_dir)

    builder = InternalLinkBuilder(glossary_dir=glossary_dir, lang=args.lang)

    total_links = 0
    total_changed_files = 0
    for md_file in _iter_markdown_files(target):
        added, changed = builder.process_file(md_file, dry_run=args.dry_run)
        total_links += added
        if changed:
            total_changed_files += 1
            if added > 0:
                print(f"✅ {md_file}: {added} links added")
            else:
                print(f"🛠️  {md_file}: normalized formatting")

    print(f"Total links added: {total_links}")
    print(f"Total files changed: {total_changed_files}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
