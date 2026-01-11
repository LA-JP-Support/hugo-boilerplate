#!/usr/bin/env python3

import argparse
import re
from pathlib import Path
from typing import List, Tuple
from urllib.parse import urlsplit, urlunsplit


def _normalize_path_lower(url: str) -> str:
    u = (url or "").strip()
    if not u:
        return ""

    parts = urlsplit(u)
    if parts.scheme or parts.netloc:
        return urlunsplit((parts.scheme, parts.netloc, parts.path.lower(), parts.query, parts.fragment))

    path = u
    fragment = ""
    query = ""

    if "#" in path:
        path, fragment = path.split("#", 1)
    if "?" in path:
        path, query = path.split("?", 1)

    path = path.lower()

    out = path
    if query:
        out += "?" + query
    if fragment:
        out += "#" + fragment
    return out


def _ensure_trailing_slash(url: str) -> str:
    u = (url or "").strip()
    if not u:
        return ""

    parts = urlsplit(u)
    if parts.scheme or parts.netloc:
        if parts.path and not parts.path.endswith("/") and "." not in parts.path.split("/")[-1]:
            return urlunsplit((parts.scheme, parts.netloc, parts.path + "/", parts.query, parts.fragment))
        return u

    path = u
    fragment = ""
    query = ""
    if "#" in path:
        path, fragment = path.split("#", 1)
    if "?" in path:
        path, query = path.split("?", 1)

    if path and not path.endswith("/") and "." not in path.split("/")[-1]:
        path += "/"

    out = path
    if query:
        out += "?" + query
    if fragment:
        out += "#" + fragment
    return out


def _split_front_matter(text: str) -> Tuple[bool, str, str, str]:
    if text.startswith('---\n'):
        end = text.find('\n---\n', 4)
        if end != -1:
            fm = text[4:end + 1]
            rest = text[end + 5:]
            return True, '---', fm, rest
    if text.startswith('+++\n'):
        end = text.find('\n+++\n', 4)
        if end != -1:
            fm = text[4:end + 1]
            rest = text[end + 5:]
            return True, '+++', fm, rest
    return False, '', '', text


def _format_list_item(value: str, quote: str) -> str:
    if quote in ('"', "'"):
        return f"- {quote}{value}{quote}"
    return f"- {value}"


def _process_file(path: Path) -> Tuple[bool, List[str]]:
    text = path.read_text(encoding='utf-8')
    has_fm, delim, fm, body = _split_front_matter(text)
    if not has_fm or delim != '---':
        return False, []

    lines = fm.splitlines()
    url_re = re.compile(r'^(url:\s*)(?P<q>["\']?)(?P<v>.+?)(?P=q)\s*$')

    url_idx = None
    url_prefix = None
    url_quote = ''
    url_value = ''
    for i, line in enumerate(lines):
        m = url_re.match(line)
        if m:
            url_idx = i
            url_prefix = m.group(1)
            url_quote = m.group('q') or ''
            url_value = m.group('v')
            break

    if url_idx is None:
        return False, []

    original = _ensure_trailing_slash(url_value)
    canonical = _normalize_path_lower(original)
    if not canonical or canonical == original:
        return False, []

    changes: List[str] = []

    lines[url_idx] = f"{url_prefix}{url_quote}{canonical}{url_quote}"
    changes.append(f"url: {original} -> {canonical}")

    alias_key_re = re.compile(r'^(?P<k>aliases:)\s*(?P<rest>.*)$')
    aliases_idx = None
    for i, line in enumerate(lines):
        if alias_key_re.match(line):
            aliases_idx = i
            break

    def value_present_in_inline(rest: str, val: str) -> bool:
        inner = rest.strip()
        if not (inner.startswith('[') and inner.endswith(']')):
            return False
        content = inner[1:-1].strip()
        if not content:
            return False
        items = [x.strip().strip('"\'') for x in content.split(',')]
        return val in items

    if aliases_idx is None:
        insert_at = url_idx + 1
        lines.insert(insert_at, 'aliases:')
        lines.insert(insert_at + 1, _format_list_item(original, url_quote))
        changes.append(f"aliases: +{original}")
    else:
        m = alias_key_re.match(lines[aliases_idx])
        rest = (m.group('rest') if m else '').strip()

        if rest:
            if rest.startswith('[') and rest.endswith(']'):
                if not value_present_in_inline(rest, original):
                    before = rest[:-1].strip()
                    sep = '' if before.endswith('[') else ', '
                    add = f"{url_quote}{original}{url_quote}" if url_quote else f"\"{original}\""
                    new_rest = before + sep + add + ']'
                    lines[aliases_idx] = 'aliases: ' + new_rest
                    changes.append(f"aliases: +{original}")
            else:
                # Unexpected inline form; do nothing
                pass
        else:
            # Block list
            j = aliases_idx + 1
            existing: List[str] = []
            while j < len(lines):
                if re.match(r'^[A-Za-z0-9_-]+:\s*', lines[j]):
                    break
                item_m = re.match(r'^\s*-\s*(?P<v>.+?)\s*$', lines[j])
                if item_m:
                    raw = item_m.group('v').strip().strip('"\'')
                    existing.append(raw)
                j += 1
            if original not in existing:
                lines.insert(j, _format_list_item(original, url_quote))
                changes.append(f"aliases: +{original}")

    if changes:
        new_fm = '\n'.join(lines) + '\n'
        out = f"---\n{new_fm}---\n{body}"
        path.write_text(out, encoding='utf-8')
        return True, changes

    return False, []


def _collect_glossary_files(content_root: Path, lang: str, section: str) -> List[Path]:
    root = content_root / lang / section
    if not root.exists():
        return []
    return sorted(root.glob("*.md"))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--content-root", default="content")
    parser.add_argument("--langs", default="en,ja")
    parser.add_argument("--section", default="glossary")
    parser.add_argument("--apply", action="store_true")

    args = parser.parse_args()

    content_root = Path(args.content_root)
    langs = [x.strip() for x in str(args.langs).split(",") if x.strip()]
    section = str(args.section)

    planned: List[Tuple[Path, List[str]]] = []

    for lang in langs:
        for md in _collect_glossary_files(content_root, lang, section):
            text = md.read_text(encoding='utf-8')
            has_fm, delim, fm, _body = _split_front_matter(text)
            if not has_fm or delim != '---':
                continue

            url_re = re.compile(r'^(url:\s*)(?P<q>["\']?)(?P<v>.+?)(?P=q)\s*$', re.MULTILINE)
            m = url_re.search(fm)
            if not m:
                continue

            original = _ensure_trailing_slash(m.group('v'))
            canonical = _normalize_path_lower(original)
            if canonical and canonical != original:
                changes = [f"url: {original} -> {canonical}", f"aliases: +{original}"]
                planned.append((md, changes))

    if not args.apply:
        print(f"Planned changes: {len(planned)} files")
        for p, changes in planned[:50]:
            print(str(p))
            for c in changes:
                print(f"  - {c}")
        if len(planned) > 50:
            print(f"... {len(planned) - 50} more")
        return

    applied = 0
    for p, _ in planned:
        changed, _changes = _process_file(p)
        if changed:
            applied += 1

    print(f"Applied changes: {applied} files")


if __name__ == "__main__":
    main()
