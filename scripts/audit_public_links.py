#!/usr/bin/env python3

import argparse
import csv
import os
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Set, Tuple
from urllib.parse import unquote, urlsplit

from bs4 import BeautifulSoup


@dataclass
class Finding:
    source_file: str
    href: str
    normalized_href: str
    suggested_href: str
    suggestion_reason: str


def _is_external_href(href: str) -> bool:
    if not href:
        return True
    href = href.strip()
    if not href:
        return True
    if href.startswith(('#', 'mailto:', 'tel:', 'javascript:')):
        return True
    if href.startswith(('http://', 'https://')):
        return True
    if href.startswith('//'):
        return True
    return False


def _split_href(href: str) -> Tuple[str, str, str]:
    href = href.strip()
    parts = urlsplit(href)
    path = parts.path or ""
    return path, parts.query or "", parts.fragment or ""


def _normalize_href(href: str) -> str:
    path, query, fragment = _split_href(href)
    path = unquote(path)
    out = path
    if query:
        out += "?" + query
    if fragment:
        out += "#" + fragment
    return out


def _href_path_only(href: str) -> str:
    path, _, _ = _split_href(href)
    return unquote(path)


def _public_targets_for_path(public_dir: Path, path: str) -> List[Path]:
    path = path.lstrip('/')
    if not path:
        return [public_dir / 'index.html']
    if path.endswith('/'):
        return [public_dir / path / 'index.html']
    last = Path(path).name
    if '.' in last:
        return [public_dir / path]
    return [public_dir / path / 'index.html', public_dir / f"{path}.html"]


def _exists_in_public(public_dir: Path, href_path: str) -> bool:
    for target in _public_targets_for_path(public_dir, href_path):
        if target.exists():
            return True
    return False


def _candidate_fixes(path: str) -> List[Tuple[str, str]]:
    out: List[Tuple[str, str]] = []

    if any('A' <= c <= 'Z' for c in path):
        out.append((path.lower(), 'lowercase_path'))

    if path.endswith('/'):
        base = path[:-1]
        if base and base.endswith('s'):
            out.append((base[:-1] + '/', 'drop_trailing_s'))
    else:
        if path.endswith('s'):
            out.append((path[:-1], 'drop_trailing_s'))

    if path.endswith('/'):
        out.append((path[:-1], 'remove_trailing_slash'))
    else:
        out.append((path + '/', 'add_trailing_slash'))

    seen: Set[str] = set()
    deduped: List[Tuple[str, str]] = []
    for p, reason in out:
        if p and p not in seen:
            seen.add(p)
            deduped.append((p, reason))
    return deduped


def audit_public(public_dir: Path, apply: bool) -> Tuple[List[Finding], int]:
    findings: List[Finding] = []
    files_modified = 0

    html_files: List[Path] = []
    for root, _, files in os.walk(public_dir):
        for f in files:
            if f.endswith('.html'):
                html_files.append(Path(root) / f)

    for html_path in html_files:
        try:
            raw = html_path.read_text(encoding='utf-8', errors='replace')
            soup = BeautifulSoup(raw, 'html.parser')
        except Exception:
            continue

        changed = False

        for a in soup.find_all('a', href=True):
            href = str(a.get('href', '')).strip()
            if _is_external_href(href):
                continue

            normalized = _normalize_href(href)
            path_only = _href_path_only(href)

            if not path_only.startswith('/'):
                continue

            if _exists_in_public(public_dir, path_only):
                continue

            candidates = _candidate_fixes(path_only)
            valid: List[Tuple[str, str]] = []
            for cand_path, reason in candidates:
                if _exists_in_public(public_dir, cand_path):
                    valid.append((cand_path, reason))

            suggested_href = ''
            suggestion_reason = ''
            if len(valid) == 1:
                suggested_href = valid[0][0]
                suggestion_reason = valid[0][1]

                if apply:
                    _, query, fragment = _split_href(href)
                    new_href = suggested_href
                    if query:
                        new_href += '?' + query
                    if fragment:
                        new_href += '#' + fragment
                    if new_href != href:
                        a['href'] = new_href
                        changed = True
            
            findings.append(
                Finding(
                    source_file=str(html_path.relative_to(public_dir)),
                    href=href,
                    normalized_href=normalized,
                    suggested_href=suggested_href,
                    suggestion_reason=suggestion_reason,
                )
            )

        if apply and changed:
            try:
                html_path.write_text(str(soup), encoding='utf-8')
                files_modified += 1
            except Exception:
                pass

    return findings, files_modified


def write_report_csv(findings: List[Finding], report_path: Path) -> None:
    report_path.parent.mkdir(parents=True, exist_ok=True)
    with report_path.open('w', encoding='utf-8', newline='') as f:
        w = csv.writer(f)
        w.writerow(['source_file', 'href', 'normalized_href', 'suggested_href', 'suggestion_reason'])
        for r in findings:
            w.writerow([r.source_file, r.href, r.normalized_href, r.suggested_href, r.suggestion_reason])


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--public-dir', default='public')
    ap.add_argument('--apply', action='store_true')
    ap.add_argument('--report', default='broken_links_report.csv')
    args = ap.parse_args()

    public_dir = Path(args.public_dir).resolve()
    if not public_dir.exists():
        raise SystemExit(f"public dir not found: {public_dir}")

    findings, files_modified = audit_public(public_dir, apply=args.apply)

    broken = [f for f in findings if not f.suggested_href]
    fixed = [f for f in findings if f.suggested_href]

    write_report_csv(findings, Path(args.report))

    print(f"HTML files scanned: {sum(1 for _ in public_dir.rglob('*.html'))}")
    print(f"Broken links found: {len(findings)}")
    print(f"Auto-fixable (unique suggestion): {len(fixed)}")
    print(f"Not auto-fixable: {len(broken)}")
    if args.apply:
        print(f"HTML files modified: {files_modified}")
    print(f"Report: {args.report}")

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
