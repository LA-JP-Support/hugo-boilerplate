#!/usr/bin/env python3

"""Translate missing English blog posts to Japanese using FlowHunt API.

- Source: content/en/blog/*.md
- Destination: content/ja/blog/*.md
- Only creates files that do not already exist (unless --overwrite)

Post-processing:
- Remove Markdown link title attributes ("tooltips") for /en/glossary and /ja/glossary links
- Optionally normalize /en/glossary/<Slug>/ to /ja/glossary/<Slug>/ if the JA glossary page exists

Requirements:
- FLOWHUNT_API_KEY in environment (or .env)
- flowhunt python package

Usage:
  python3 scripts/translate_blog_with_flowhunt.py --dry-run
  python3 scripts/translate_blog_with_flowhunt.py

Optional:
  python3 scripts/translate_blog_with_flowhunt.py --flow-id <FLOW_ID> --check-interval 30
"""

from __future__ import annotations

import argparse
import json
import os
import re
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Set, Tuple

from dotenv import load_dotenv
import flowhunt


DEFAULT_FLOW_ID = "7389730a-fbaf-48a2-bb77-3b6814c23b20"


@dataclass(frozen=True)
class Task:
    src: Path
    dst: Path
    content: str


def project_root_from_script() -> Path:
    return Path(__file__).resolve().parents[1]


def load_env(project_root: Path) -> None:
    env_path = project_root / ".env"
    if env_path.exists():
        load_dotenv(env_path)


def get_api_key() -> str:
    api_key = os.getenv("FLOWHUNT_API_KEY")
    if not api_key:
        raise RuntimeError(
            "FLOWHUNT_API_KEY not found in environment variables or .env file."
        )
    return api_key


def initialize_api_client(api_key: str) -> flowhunt.ApiClient:
    configuration = flowhunt.Configuration(host="https://api.flowhunt.io")
    configuration.api_key["APIKeyHeader"] = api_key
    return flowhunt.ApiClient(configuration)


def get_workspace_id(api_client: flowhunt.ApiClient) -> str:
    api_instance = flowhunt.WebAuthApi(api_client)
    resp = api_instance.get_user()
    return resp.api_key_workspace_id


def iter_en_blog_files(content_root: Path) -> Iterable[Path]:
    en_dir = content_root / "en" / "blog"
    if not en_dir.exists():
        return
    for p in sorted(en_dir.glob("*.md")):
        if p.name == "_index.md":
            continue
        yield p


def build_tasks(*, content_root: Path, overwrite: bool) -> List[Task]:
    ja_dir = content_root / "ja" / "blog"
    tasks: List[Task] = []
    for src in iter_en_blog_files(content_root):
        dst = ja_dir / src.name
        if dst.exists() and not overwrite:
            continue
        try:
            content = src.read_text(encoding="utf-8")
        except Exception:
            continue
        tasks.append(Task(src=src, dst=dst, content=content))
    return tasks


def invoke_flow_for_translation(
    flows_api: flowhunt.FlowsApi,
    *,
    flow_id: str,
    workspace_id: str,
    content: str,
) -> str:
    req = flowhunt.FlowInvokeRequest(
        variables={
            "source_language": "English",
            "target_language": "Japanese",
            "today": time.strftime("%Y-%m-%d %H:00:00"),
        },
        human_input=content,
    )
    resp = flows_api.invoke_flow_singleton(
        flow_id=flow_id,
        workspace_id=workspace_id,
        flow_invoke_request=req,
    )
    return resp.id


def check_flow_results(
    flows_api: flowhunt.FlowsApi,
    *,
    flow_id: str,
    workspace_id: str,
    process_id: str,
) -> Tuple[bool, Optional[str]]:
    resp = flows_api.get_invoked_flow_results(
        flow_id=flow_id,
        task_id=process_id,
        workspace_id=workspace_id,
    )
    if resp.status != "SUCCESS":
        return False, None

    translated_text = json.loads(resp.result)
    translated_text = translated_text["outputs"][0]["outputs"][0]["results"]["message"][
        "result"
    ]
    translated_text = (translated_text or "").strip()

    if translated_text.startswith("```"):
        translated_text = translated_text[3:]
    if translated_text.endswith("```"):
        translated_text = translated_text[:-3]

    return True, translated_text.strip()


def _mask_segments(text: str) -> Tuple[str, Dict[str, str]]:
    placeholders: Dict[str, str] = {}
    counter = 0

    def repl(match: re.Match) -> str:
        nonlocal counter
        counter += 1
        key = f"__MASKED_{counter}__"
        placeholders[key] = match.group(0)
        return key

    # fenced code blocks
    text = re.sub(r"```[\s\S]*?```", repl, text)
    # inline code
    text = re.sub(r"`[^`\n]+`", repl, text)
    # shortcodes
    text = re.sub(r"\{\{[<%][\s\S]*?[>%]\}\}", repl, text)
    # html tags
    text = re.sub(r"<[^>]+>", repl, text)

    return text, placeholders


def _unmask_segments(text: str, placeholders: Dict[str, str]) -> str:
    for key, value in placeholders.items():
        text = text.replace(key, value)
    return text


def sanitize_markdown_links_inside_html(md: str) -> str:
    """Prevent broken HTML attributes by stripping markdown links inside HTML tags.

    Example:
      src="https://www.[youtube](/ja/glossary/YouTube/) .com/..."
    becomes:
      src="https://www.youtube .com/..."

    This intentionally keeps only the link text inside tags.
    """

    def fix_tag(m: re.Match) -> str:
        tag = m.group(0)
        # Replace any markdown link found inside HTML tag with its anchor text.
        tag = re.sub(r"\[([^\]]+)\]\([^\)]+\)", r"\1", tag)
        return tag

    return re.sub(r"<[^>]+>", fix_tag, md)


def strip_tooltip_titles(md: str) -> str:
    masked, store = _mask_segments(md)

    # Remove title attribute for glossary links.
    # Example: [Text](/ja/glossary/Slug/ "desc") -> [Text](/ja/glossary/Slug/)
    # Supports straight and smart quotes.
    glossary_title_re = re.compile(
        r"\]\((/(?:(?:en)|(?:ja))/glossary/[^)\s]+)\s+[\"\u201C][^)]*[\"\u201D]\)"
    )
    masked = glossary_title_re.sub(r"](\1)", masked)

    return _unmask_segments(masked, store)


def normalize_en_glossary_links_to_ja(md: str, ja_glossary_dir: Path) -> str:
    """Replace /en/glossary/<Slug>/ with /ja/glossary/<Slug>/ if the JA page exists."""

    def ja_exists(slug: str) -> bool:
        # common patterns
        if (ja_glossary_dir / f"{slug}.md").exists():
            return True
        if (ja_glossary_dir / slug / "_index.md").exists():
            return True
        return False

    def repl(match: re.Match) -> str:
        prefix = match.group(1)
        slug = match.group(2)
        suffix = match.group(3)
        if ja_exists(slug):
            return f"{prefix}/ja/glossary/{slug}/{suffix}"
        return match.group(0)

    masked, store = _mask_segments(md)

    # Match inside markdown link url: ](/en/glossary/Slug/)
    # Keep any trailing chars after the URL (e.g., fragment) via group 3.
    pat = re.compile(r"(\]\()(/en/glossary/)([^/]+)/([^)]*)(\))")

    def repl2(m: re.Match) -> str:
        # groups: 1=]( 2=/en/glossary/ 3=slug 4=rest 5=)
        if ja_exists(m.group(3)):
            return f"{m.group(1)}/ja/glossary/{m.group(3)}/{m.group(4)}{m.group(5)}"
        return m.group(0)

    masked = pat.sub(repl2, masked)

    return _unmask_segments(masked, store)


def postprocess_translation(md: str, project_root: Path) -> str:
    md = sanitize_markdown_links_inside_html(md)
    md = strip_tooltip_titles(md)

    # Convert leftover /en/glossary links to /ja/glossary where possible.
    ja_glossary_dir = project_root / "content" / "ja" / "glossary"
    if ja_glossary_dir.exists():
        md = normalize_en_glossary_links_to_ja(md, ja_glossary_dir)

    # Strip tooltips again (in case conversion introduced oddities)
    md = strip_tooltip_titles(md)
    return md


def ensure_date_in_frontmatter(md: str) -> str:
    """Ensure 'date' exists in frontmatter to avoid Hugo zero date.

    Only adds date if YAML frontmatter is present and date is missing.
    For TOML frontmatter, this function leaves content unchanged.
    """

    today = time.strftime("%Y-%m-%d")

    # YAML frontmatter
    if md.startswith("---\n"):
        m = re.match(r"^---\n(?P<fm>[\s\S]*?)\n---\n", md)
        if not m:
            return md
        fm = m.group("fm")
        if re.search(r"^date:\s*\S+", fm, re.MULTILINE):
            return md
        fm2 = fm.rstrip() + f"\ndate: {today}\nlastmod: {today}\n"
        return md[: m.start()] + f"---\n{fm2}\n---\n" + md[m.end() :]

    # TOML frontmatter
    if md.startswith("+++\n"):
        m = re.match(r"^\+\+\+\n(?P<fm>[\s\S]*?)\n\+\+\+\n", md)
        if not m:
            return md
        fm = m.group("fm")
        if re.search(r"^date\s*=", fm, re.MULTILINE):
            return md
        fm2 = fm.rstrip() + f"\ndate = \"{today}\"\nlastmod = \"{today}\"\n"
        return md[: m.start()] + f"+++\n{fm2}\n+++\n" + md[m.end() :]

    return md


def translate_tasks(
    *,
    tasks: Sequence[Task],
    content_root: Path,
    flow_id: str,
    check_interval: int,
    dry_run: bool,
) -> None:
    project_root = content_root.parent
    if dry_run:
        print("[DRY-RUN] Would translate the following blog posts:")
        for t in tasks:
            print(f"  {t.src} -> {t.dst}")
        return

    api_key = get_api_key()

    with initialize_api_client(api_key) as api_client:
        workspace_id = get_workspace_id(api_client)
        flows_api = flowhunt.FlowsApi(api_client)

        for t in tasks:
            print(f"Translating: {t.src.name} -> {t.dst}")
            process_id = invoke_flow_for_translation(
                flows_api,
                flow_id=flow_id,
                workspace_id=workspace_id,
                content=t.content,
            )

            while True:
                time.sleep(check_interval)
                ready, translated = check_flow_results(
                    flows_api,
                    flow_id=flow_id,
                    workspace_id=workspace_id,
                    process_id=process_id,
                )
                if not ready:
                    continue
                if not translated:
                    raise RuntimeError(f"Flow returned empty translation for {t.src.name}")

                translated = postprocess_translation(translated, project_root)
                translated = ensure_date_in_frontmatter(translated)

                t.dst.parent.mkdir(parents=True, exist_ok=True)
                t.dst.write_text(translated, encoding="utf-8")
                print(f"Wrote: {t.dst}")
                break


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(
        description="Translate missing English blog posts to Japanese (blog only) via FlowHunt API."
    )
    parser.add_argument(
        "--content-root",
        default=str(project_root_from_script() / "content"),
        help="Path to Hugo content root (default: <repo>/content)",
    )
    parser.add_argument(
        "--flow-id",
        default=DEFAULT_FLOW_ID,
        help="FlowHunt flow ID for translation service",
    )
    parser.add_argument(
        "--check-interval",
        type=int,
        default=20,
        help="Seconds between polling FlowHunt task status",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite existing content/ja/blog/*.md",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print planned translations without calling the API",
    )

    args = parser.parse_args(list(argv) if argv is not None else None)

    content_root = Path(args.content_root).resolve()
    if not (content_root / "en" / "blog").exists():
        raise RuntimeError(f"Not found: {content_root / 'en' / 'blog'}")

    load_env(content_root.parent)

    tasks = build_tasks(content_root=content_root, overwrite=args.overwrite)
    missing = [t for t in tasks if not t.dst.exists()]

    print(f"EN blog: {(content_root / 'en' / 'blog').resolve()}")
    print(f"JA blog: {(content_root / 'ja' / 'blog').resolve()}")
    print(f"To translate: {len(tasks)} (missing={len(missing)}, overwrite={'yes' if args.overwrite else 'no'})")

    if not tasks:
        print("Nothing to do.")
        return 0

    translate_tasks(
        tasks=tasks,
        content_root=content_root,
        flow_id=args.flow_id,
        check_interval=args.check_interval,
        dry_run=args.dry_run,
    )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
