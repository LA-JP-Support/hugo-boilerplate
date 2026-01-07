#!/usr/bin/env python3

"""Translate English blog Markdown files to Japanese using Claude API.

Scope is intentionally limited:
- Source: content/en/blog/*.md
- Target: content/ja/blog/*.md

Features:
- Dry-run supported (no API key required)
- Skip existing output files by default
- Supports YAML (---) and TOML (+++) frontmatter input
- Outputs YAML frontmatter for consistency
- Translates selected frontmatter fields + Markdown body
- Post-processes Markdown to:
  - Remove link title attributes for /en|/ja glossary links
  - Normalize /en/glossary/<Slug>/ -> /ja/glossary/<Slug>/ when the JA glossary page exists
  - Prevent Markdown links from remaining inside HTML tags (protect embeds)

Requirements:
- CLAUDE_API_KEY or ANTHROPIC_API_KEY
- pip install anthropic pyyaml python-dotenv

Usage:
  python3 scripts/translate_blog_en_to_ja.py --dry-run
  python3 scripts/translate_blog_en_to_ja.py

Optional:
  python3 scripts/translate_blog_en_to_ja.py --one-file how-to-use-large-language-models-effectively.md
  python3 scripts/translate_blog_en_to_ja.py --model claude-sonnet-4-5-20250929
"""

from __future__ import annotations

import argparse
import os
import re
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple

import yaml

try:
    from dotenv import load_dotenv

    load_dotenv(dotenv_path=Path(__file__).resolve().parents[1] / ".env")
except ImportError:
    pass

try:
    import anthropic
except ImportError:
    anthropic = None


DEFAULT_MODEL = "claude-sonnet-4-5-20250929"

YAML_FM_RE = re.compile(r"^---\s*\n(?P<fm>[\s\S]*?)\n---\s*\n", re.MULTILINE)
TOML_FM_RE = re.compile(r"^\+\+\+\s*\n(?P<fm>[\s\S]*?)\n\+\+\+\s*\n", re.MULTILINE)


@dataclass(frozen=True)
class Task:
    src: Path
    dst: Path


def build_claude_client() -> "anthropic.Anthropic":
    api_key = os.getenv("CLAUDE_API_KEY") or os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        raise RuntimeError(
            "CLAUDE_API_KEY (or fallback ANTHROPIC_API_KEY) is not set. "
            "Either export it or add to .env file in project root."
        )
    if anthropic is None:
        raise RuntimeError("anthropic package is not installed. Run: pip install anthropic")
    return anthropic.Anthropic(api_key=api_key)


def split_frontmatter(text: str) -> Tuple[str, str, str]:
    """Return (kind, fm_raw, body). kind is 'yaml' | 'toml' | ''"""
    m = YAML_FM_RE.match(text)
    if m:
        end = m.end()
        return "yaml", m.group("fm"), text[end:]

    m = TOML_FM_RE.match(text)
    if m:
        end = m.end()
        return "toml", m.group("fm"), text[end:]

    return "", "", text


def parse_frontmatter(kind: str, fm_raw: str) -> Dict[str, Any]:
    if not kind:
        return {}

    if kind == "yaml":
        try:
            data = yaml.safe_load(fm_raw) or {}
            return data if isinstance(data, dict) else {}
        except Exception:
            return {}

    if kind == "toml":
        try:
            import tomllib
        except ImportError:
            try:
                import toml as tomllib  # type: ignore
            except ImportError:
                return {}

        try:
            data = tomllib.loads(fm_raw)
            return data if isinstance(data, dict) else {}
        except Exception:
            return {}

    return {}


def dump_yaml_frontmatter(frontmatter: Dict[str, Any]) -> str:
    fm_yaml = yaml.safe_dump(frontmatter, allow_unicode=True, sort_keys=False).strip()
    return f"---\n{fm_yaml}\n---\n\n"


def iter_en_blog_files(content_root: Path) -> Iterable[Path]:
    en_dir = content_root / "en" / "blog"
    if not en_dir.exists():
        return
    for p in sorted(en_dir.glob("*.md")):
        if p.name == "_index.md":
            continue
        yield p


def build_tasks(*, content_root: Path, overwrite: bool, one_file: Optional[str]) -> List[Task]:
    ja_dir = content_root / "ja" / "blog"
    tasks: List[Task] = []

    if one_file:
        src = content_root / "en" / "blog" / one_file
        if not src.exists():
            raise RuntimeError(f"Source file not found: {src}")
        dst = ja_dir / src.name
        if dst.exists() and not overwrite:
            return []
        return [Task(src=src, dst=dst)]

    for src in iter_en_blog_files(content_root):
        dst = ja_dir / src.name
        if dst.exists() and not overwrite:
            continue
        tasks.append(Task(src=src, dst=dst))

    return tasks


def _mask_segments(text: str) -> Tuple[str, Dict[str, str]]:
    placeholders: Dict[str, str] = {}
    counter = 0

    def create_placeholder(content: str) -> str:
        nonlocal counter
        counter += 1
        key = f"__MASKED_{counter}__"
        placeholders[key] = content
        return key

    # fenced code blocks
    text = re.sub(r"```[\s\S]*?```", lambda m: create_placeholder(m.group(0)), text)
    # inline code
    text = re.sub(r"`[^`\n]+`", lambda m: create_placeholder(m.group(0)), text)
    # hugo shortcodes
    text = re.sub(r"\{\{[<%][\s\S]*?[>%]\}\}", lambda m: create_placeholder(m.group(0)), text)
    # html tags
    text = re.sub(r"<[^>]+>", lambda m: create_placeholder(m.group(0)), text)

    return text, placeholders


def _unmask_segments(text: str, placeholders: Dict[str, str]) -> str:
    for key, value in placeholders.items():
        text = text.replace(key, value)
    return text


def strip_tooltip_titles(md: str) -> str:
    masked, store = _mask_segments(md)
    glossary_title_re = re.compile(
        r"\]\((/(?:(?:en)|(?:ja))/glossary/[^)\s]+)\s+[\"\u201C][^)]*[\"\u201D]\)"
    )
    masked = glossary_title_re.sub(r"](\1)", masked)
    return _unmask_segments(masked, store)


def fix_malformed_markdown_links(md: str) -> str:
    masked, store = _mask_segments(md)

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

    masked = re.sub(r"\[\[([^\]]+)\]\(([^)\s]+)\)\]\(\2\)", r"[\1](\2)", masked)
    masked = re.sub(r"\[\[([^\]]+)\]\(([^)]+)\)", r"[\1](\2)", masked)
    masked = re.sub(r"\[([^\]]*?)\s+\]\(([^)]+)\)", r"[\1](\2)", masked)
    masked = re.sub(r"\*\*([^*\n]*?)\s+\*\*", r"**\1**", masked)

    return _unmask_segments(masked, store)


def sanitize_markdown_links_inside_html(md: str) -> str:
    def fix_tag(m: re.Match) -> str:
        tag = m.group(0)
        tag = re.sub(r"\[([^\]]+)\]\([^\)]+\)", r"\1", tag)
        return tag

    return re.sub(r"<[^>]+>", fix_tag, md)


def normalize_en_glossary_links_to_ja(md: str, ja_glossary_dir: Path) -> str:
    def ja_exists(slug: str) -> bool:
        if (ja_glossary_dir / f"{slug}.md").exists():
            return True
        if (ja_glossary_dir / slug / "_index.md").exists():
            return True
        return False

    masked, store = _mask_segments(md)
    pat = re.compile(r"(\]\()(/en/glossary/)([^/]+)/([^)]*)(\))")

    def repl(m: re.Match) -> str:
        slug = m.group(3)
        if ja_exists(slug):
            return f"{m.group(1)}/ja/glossary/{slug}/{m.group(4)}{m.group(5)}"
        return m.group(0)

    masked = pat.sub(repl, masked)
    return _unmask_segments(masked, store)


def postprocess_markdown(md: str, project_root: Path) -> str:
    md = sanitize_markdown_links_inside_html(md)
    md = fix_malformed_markdown_links(md)
    md = strip_tooltip_titles(md)

    ja_glossary_dir = project_root / "content" / "ja" / "glossary"
    if ja_glossary_dir.exists():
        md = normalize_en_glossary_links_to_ja(md, ja_glossary_dir)

    md = fix_malformed_markdown_links(md)
    md = strip_tooltip_titles(md)
    md = sanitize_markdown_links_inside_html(md)
    return md


def should_translate_key(key: str) -> bool:
    return key in {
        "title",
        "description",
        "ctaHeading",
        "ctaDescription",
        "youtubeTitle",
        "keywords",
        "tags",
        "categories",
        "faq",
    }


def ensure_date_fields(fm: Dict[str, Any]) -> None:
    today = time.strftime("%Y-%m-%d")
    if not fm.get("date"):
        fm["date"] = today
    if not fm.get("lastmod"):
        fm["lastmod"] = fm.get("date") or today


class ClaudeTranslator:
    def __init__(self, client: "anthropic.Anthropic", *, model: str, temperature: float = 0.2, max_tokens: int = 16000) -> None:
        self.client = client
        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens

    def _run(self, *, system_prompt: str, user_text: str) -> str:
        resp = self.client.messages.create(
            model=self.model,
            max_tokens=self.max_tokens,
            temperature=self.temperature,
            system=system_prompt,
            messages=[{"role": "user", "content": [{"type": "text", "text": user_text}]}],
        )
        chunks: List[str] = []
        for block in resp.content:
            if getattr(block, "type", None) == "text":
                chunks.append(block.text)
        return "".join(chunks).strip()

    def translate_text(self, text: str) -> str:
        prompt = (
            "Translate the following text from English to natural Japanese. "
            "Return ONLY the Japanese translation, no commentary."
        )
        return self._run(system_prompt=prompt, user_text=text)

    def translate_keywords(self, items: Sequence[str]) -> List[str]:
        if not items:
            return []
        payload = "\n".join(f"- {x}" for x in items)
        prompt = (
            "Translate each bullet item from English to Japanese. "
            "Return the same bullet list format using '- '. Do not add extra items."
        )
        out = self._run(system_prompt=prompt, user_text=payload)
        results: List[str] = []
        for line in out.splitlines():
            line = line.strip()
            if line.startswith("-"):
                results.append(line[1:].strip())
        return results or list(items)

    def translate_faq(self, faqs: Any) -> Any:
        if not isinstance(faqs, list) or not faqs:
            return faqs
        to_translate: List[Dict[str, str]] = []
        for item in faqs:
            if not isinstance(item, dict):
                continue
            q = str(item.get("question", ""))
            a = str(item.get("answer", ""))
            to_translate.append({"question": q, "answer": a})

        # Build a deterministic payload to parse back.
        parts: List[str] = []
        for i, qa in enumerate(to_translate, start=1):
            parts.append(f"<<FAQ {i}>>\nQ: {qa['question']}\nA: {qa['answer']}\n<<END FAQ>>")
        user_payload = "\n\n".join(parts)
        system_prompt = (
            "Translate each FAQ from English to Japanese. Preserve the delimiters exactly. "
            "Inside each block keep 'Q:' and 'A:' lines. Return ONLY the translated blocks."
        )
        out = self._run(system_prompt=system_prompt, user_text=user_payload)

        pat = re.compile(r"<<FAQ (?P<i>\d+)>>\s*Q:\s*(?P<q>[\s\S]*?)\nA:\s*(?P<a>[\s\S]*?)\n<<END FAQ>>")
        idx_to_qa: Dict[int, Tuple[str, str]] = {}
        for m in pat.finditer(out):
            idx_to_qa[int(m.group("i"))] = (m.group("q").strip(), m.group("a").strip())

        if not idx_to_qa:
            return faqs

        # Rebuild preserving any extra keys.
        out_list: List[Dict[str, Any]] = []
        j = 1
        for item in faqs:
            if not isinstance(item, dict):
                out_list.append(item)
                continue
            q, a = idx_to_qa.get(j, (str(item.get("question", "")), str(item.get("answer", ""))))
            new_item = dict(item)
            new_item["question"] = q
            new_item["answer"] = a
            out_list.append(new_item)
            j += 1
        return out_list

    def translate_body_markdown(self, body_md: str) -> str:
        system_prompt = (
            "You are translating a blog article from English to natural, professional Japanese.\n\n"
            "Rules:\n"
            "- Input is Markdown. Preserve Markdown structure (headings, lists, code blocks, links) exactly.\n"
            "- Do NOT translate URLs. Keep them unchanged.\n"
            "- Do NOT change placeholders like __MASKED_1__. Keep them exactly as-is.\n"
            "- Do NOT translate code inside fenced code blocks or inline code.\n"
            "- Translate prose into Japanese.\n\n"
            "Return ONLY the translated Markdown body."
        )
        return self._run(system_prompt=system_prompt, user_text=body_md)


def translate_frontmatter(translator: ClaudeTranslator, fm: Dict[str, Any]) -> Dict[str, Any]:
    out = dict(fm)

    for key, value in list(out.items()):
        if not should_translate_key(key):
            continue

        if key in {"title", "description", "ctaHeading", "ctaDescription", "youtubeTitle"}:
            if isinstance(value, str) and value.strip():
                out[key] = translator.translate_text(value)
            continue

        if key in {"keywords", "tags", "categories"}:
            if isinstance(value, list) and all(isinstance(x, str) for x in value):
                out[key] = translator.translate_keywords(value)
            continue

        if key == "faq":
            out[key] = translator.translate_faq(value)
            continue

    ensure_date_fields(out)
    return out


def translate_file(*, translator: ClaudeTranslator, src: Path, dst: Path, project_root: Path) -> None:
    raw = src.read_text(encoding="utf-8")
    kind, fm_raw, body = split_frontmatter(raw)
    fm = parse_frontmatter(kind, fm_raw)

    masked_body, placeholders = _mask_segments(body)
    body_ja = translator.translate_body_markdown(masked_body)
    body_ja = _unmask_segments(body_ja, placeholders)

    fm_ja = translate_frontmatter(translator, fm)

    out_text = dump_yaml_frontmatter(fm_ja) + body_ja.lstrip()
    out_text = postprocess_markdown(out_text, project_root)

    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(out_text, encoding="utf-8")
    print(f"✓ Translated {src.name} -> {dst}")


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Translate EN blog posts to JA using Claude API (blog only).")
    parser.add_argument(
        "--content-root",
        default=str(Path(__file__).resolve().parents[1] / "content"),
        help="Path to Hugo content root (default: <repo>/content)",
    )
    parser.add_argument("--model", default=DEFAULT_MODEL, help="Claude model name")
    parser.add_argument("--dry-run", action="store_true", help="Show planned work without calling the API")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing content/ja/blog/*.md")
    parser.add_argument("--one-file", help="Translate only this filename in content/en/blog")

    args = parser.parse_args(list(argv) if argv is not None else None)

    content_root = Path(args.content_root).resolve()
    project_root = content_root.parent

    tasks = build_tasks(content_root=content_root, overwrite=args.overwrite, one_file=args.one_file)

    print(f"EN blog: {(content_root / 'en' / 'blog').resolve()}")
    print(f"JA blog: {(content_root / 'ja' / 'blog').resolve()}")
    print(f"To translate: {len(tasks)} (overwrite={'yes' if args.overwrite else 'no'})")

    if not tasks:
        print("Nothing to do.")
        return 0

    if args.dry_run:
        print("[DRY-RUN] Would translate:")
        for t in tasks:
            print(f"  {t.src} -> {t.dst}")
        return 0

    client = build_claude_client()
    translator = ClaudeTranslator(client, model=args.model)

    for t in tasks:
        translate_file(translator=translator, src=t.src, dst=t.dst, project_root=project_root)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
