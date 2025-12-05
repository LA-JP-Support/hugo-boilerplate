#!/usr/bin/env python3
"""Update the `lastmod` frontmatter field for changed Markdown files.

Usage:
    python scripts/update_lastmod.py

The script inspects `git status --porcelain` to find modified/added Markdown files
under the `content/` directory. For each file, it updates (or inserts) the
`lastmod: YYYY-MM-DD` field with today's date. Use it manually before committing,
or add it to a Git pre-commit hook for automation.
"""
from __future__ import annotations

import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable

REPO_ROOT = Path(__file__).resolve().parents[1]
TODAY = datetime.now(timezone.utc).astimezone().strftime("%Y-%m-%d")


def get_changed_files() -> set[Path]:
    """Return Markdown files under content/ that are staged or modified."""
    try:
        output = subprocess.check_output(
            ["git", "status", "--porcelain"], text=True, cwd=REPO_ROOT
        )
    except subprocess.CalledProcessError as exc:  # pragma: no cover - unexpected
        raise SystemExit(exc)

    files: set[Path] = set()
    for line in output.splitlines():
        if not line or len(line) < 4:
            continue
        status, path_part = line[:2], line[3:]
        # Handle renames which look like: "R  old -> new"
        if status.strip().startswith("R") and "->" in path_part:
            path_part = path_part.split("->", 1)[1].strip()
        path = Path(path_part)
        # Only care about Markdown files in content/
        try:
            path.relative_to("content")
        except ValueError:
            continue
        if path.suffix.lower() != ".md":
            continue
        files.add(REPO_ROOT / path)
    return files


def update_lastmod(file_path: Path) -> bool:
    """Update/insert the lastmod field. Returns True if the file was changed."""
    text = file_path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return False

    lines = text.splitlines()
    try:
        fm_end = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")
    except StopIteration:
        return False

    fm_lines = lines[1:fm_end]
    body_lines = lines[fm_end + 1 :]

    def _strip(line: str) -> str:
        return line.split(":", 1)[0].strip().lower() if ":" in line else ""

    changed = False
    lastmod_index = next((i for i, l in enumerate(fm_lines) if _strip(l) == "lastmod"), None)

    new_entry = f"lastmod: {TODAY}"
    if lastmod_index is not None:
        current_value = fm_lines[lastmod_index].split(":", 1)[1].strip()
        if current_value != TODAY:
            fm_lines[lastmod_index] = new_entry
            changed = True
    else:
        insert_idx = next((i + 1 for i, l in enumerate(fm_lines) if _strip(l) == "date"), len(fm_lines))
        fm_lines.insert(insert_idx, new_entry)
        changed = True

    if not changed:
        return False

    new_content_lines: list[str] = ["---", *fm_lines, "---", *body_lines]
    file_path.write_text("\n".join(new_content_lines) + "\n", encoding="utf-8")
    return True


def main() -> None:
    files = sorted(get_changed_files())
    if not files:
        print("No modified Markdown files detected under content/.")
        return

    updated: list[Path] = []
    for file_path in files:
        if update_lastmod(file_path):
            updated.append(file_path.relative_to(REPO_ROOT))

    if updated:
        print("Updated lastmod for:")
        for path in updated:
            print(f"  - {path}")
    else:
        print("lastmod already up to date for modified files.")


if __name__ == "__main__":
    main()
