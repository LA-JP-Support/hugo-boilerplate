#!/usr/bin/env python3

import argparse
import re
import shutil
from datetime import datetime
from pathlib import Path


YAML_DELIM = "---"
TOML_DELIM = "+++"


def _make_delim_re(delim: str) -> re.Pattern:
    return re.compile(rf"^[ \t]*{re.escape(delim)}\s*$", re.MULTILINE)


def extract_frontmatter(text: str):
    m = re.match(r"^\ufeff?(?:[ \t]*\n)*[ \t]*(---|\+\+\+)\s*\n", text)
    if not m:
        return None

    delim = m.group(1)
    delim_re = _make_delim_re(delim)
    matches = list(delim_re.finditer(text))
    if len(matches) < 2:
        return None

    start = matches[0].end()
    end = matches[1].start()
    fm = text[start:end]
    body = text[matches[1].end() :]
    return delim, fm, body


def has_key(fm: str, key: str, is_toml: bool) -> bool:
    op = "=" if is_toml else ":"
    return re.search(rf"^\s*{re.escape(key)}\s*{re.escape(op)}", fm, flags=re.MULTILINE) is not None


def get_simple_value(fm: str, key: str, is_toml: bool):
    op = "=" if is_toml else ":"
    m = re.search(rf"^\s*{re.escape(key)}\s*{re.escape(op)}\s*(.+?)\s*$", fm, flags=re.MULTILINE)
    if not m:
        return None
    return m.group(1).strip()


def is_youtube_article(fm: str, is_toml: bool) -> bool:
    if is_toml:
        if re.search(r'^\s*layout\s*=\s*"?single-youtube"?\s*$', fm, flags=re.MULTILINE):
            return True
        if re.search(r'^\s*youtubeVideoID\s*=\s*.+$', fm, flags=re.MULTILINE):
            return True
        return False

    if re.search(r"^\s*layout\s*:\s*single-youtube\s*$", fm, flags=re.MULTILINE):
        return True
    if re.search(r"^\s*youtubeVideoID\s*:\s*.+$", fm, flags=re.MULTILINE):
        return True
    return False


def normalize_url_value(url_value_unquoted: str, filename_stem: str) -> str:
    v = url_value_unquoted.strip()
    if re.fullmatch(rf"/?(ja|en)/blog/{re.escape(filename_stem)}/?", v):
        return f"blog/{filename_stem}/"
    return v


def build_patch_lines(fm: str, filename_stem: str, normalize_url: bool, is_toml: bool):
    add_lines = []
    fm_changed = False

    if normalize_url and "\\1" in fm:
        fm_cleaned = re.sub(r"^\s*\\1.*\n", "", fm, flags=re.MULTILINE)
        if fm_cleaned != fm:
            fm = fm_cleaned
            fm_changed = True

    if not has_key(fm, "translationKey", is_toml):
        if is_toml:
            add_lines.append(f'translationKey = "{filename_stem}"')
        else:
            add_lines.append(f'translationKey: "{filename_stem}"')

    date_val = get_simple_value(fm, "date", is_toml)
    if not has_key(fm, "lastmod", is_toml) and date_val:
        if is_toml:
            add_lines.append(f"lastmod = {date_val}")
        else:
            add_lines.append(f"lastmod: {date_val}")

    if not has_key(fm, "keywords", is_toml):
        add_lines.append("keywords = []" if is_toml else "keywords: []")

    if not has_key(fm, "url", is_toml):
        add_lines.append((f'url = "blog/{filename_stem}/"' if is_toml else f'url: "blog/{filename_stem}/"'))
    elif normalize_url:
        current_url = get_simple_value(fm, "url", is_toml)
        if current_url:
            current_unquoted = current_url.strip().strip('"').strip("'").strip()
            needs_repair = "\\1" in current_url
            if needs_repair:
                normalized_unquoted = f"blog/{filename_stem}/"
            else:
                normalized_unquoted = normalize_url_value(current_unquoted, filename_stem)
            if needs_repair or (normalized_unquoted != current_unquoted):
                if is_toml:
                    fm = re.sub(
                        r"(^\s*url\s*=\s*).+$",
                        rf'\g<1>"{normalized_unquoted}"',
                        fm,
                        flags=re.MULTILINE,
                    )
                else:
                    fm = re.sub(
                        rf"(^\s*url\s*:\s*).+$",
                        rf'\g<1>"{normalized_unquoted}"',
                        fm,
                        flags=re.MULTILINE,
                    )
                fm_changed = True

    if not add_lines and not fm_changed:
        return fm, False

    fm_stripped = fm.rstrip("\n")
    if fm_stripped and not fm_stripped.endswith("\n"):
        fm_stripped += "\n"
    if fm_stripped and not fm_stripped.endswith("\n\n"):
        fm_stripped += "\n"

    fm_new = fm_stripped + "\n".join(add_lines) + "\n"
    return fm_new, True


def process_file(path: Path, write: bool, backup: bool, normalize_url: bool, include_youtube: bool):
    original = path.read_text(encoding="utf-8")
    extracted = extract_frontmatter(original)
    if extracted is None:
        return False, "missing_frontmatter"

    delim, fm, body = extracted
    is_toml = delim == TOML_DELIM

    if (not include_youtube) and is_youtube_article(fm, is_toml):
        return False, "skipped_youtube"

    fm_new, changed = build_patch_lines(fm, path.stem, normalize_url, is_toml)
    if not changed and fm_new == fm:
        return False, "no_change"

    new_text = f"{delim}\n" + fm_new + delim + body

    if not write:
        return True, "dry_run"

    if backup:
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = path.with_suffix(path.suffix + f".bak.{ts}")
        shutil.copy2(path, backup_path)

    path.write_text(new_text, encoding="utf-8")
    return True, "written"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", default=str(Path(__file__).resolve().parents[1]))
    parser.add_argument("--langs", nargs="+", default=["ja", "en"])
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--no-backup", action="store_true")
    parser.add_argument("--normalize-url", action="store_true")
    parser.add_argument("--include-youtube", action="store_true")

    args = parser.parse_args()

    repo_root = Path(args.repo_root)
    backup = not args.no_backup

    summary = {
        "processed": 0,
        "changed": 0,
        "dry_run": 0,
        "written": 0,
        "skipped_youtube": 0,
        "no_change": 0,
        "missing_frontmatter": 0,
    }

    for lang in args.langs:
        blog_dir = repo_root / "content" / lang / "blog"
        if not blog_dir.exists():
            continue

        for md_path in sorted(blog_dir.glob("*.md")):
            summary["processed"] += 1
            ok, status = process_file(
                md_path,
                write=args.write,
                backup=backup,
                normalize_url=args.normalize_url,
                include_youtube=args.include_youtube,
            )
            if status in summary:
                summary[status] += 1
            if ok:
                summary["changed"] += 1
                if not args.write:
                    print(f"DRY-RUN: {md_path.relative_to(repo_root)}")
                else:
                    print(f"UPDATED: {md_path.relative_to(repo_root)}")

    print("\nSUMMARY")
    for k in [
        "processed",
        "changed",
        "dry_run",
        "written",
        "skipped_youtube",
        "no_change",
        "missing_frontmatter",
    ]:
        print(f"{k}: {summary[k]}")


if __name__ == "__main__":
    main()
