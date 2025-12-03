#!/usr/bin/env python3
"""Unified translation pipeline for FlowHunt glossary articles.

This script automates the entire workflow from draft to published Japanese article:

1. Detect new/updated files in content-drafts/en/
2. Cleanup FlowHunt output
3. Enrich with keywords and links (EN)
4. Copy to content/en/glossary/
5. Translate to Japanese using Claude API
6. Enrich with keywords and links (JA)
7. Add kana index metadata
8. Fix term readings
9. Compare outlines (EN vs JA)
10. Optionally publish (draft: false)

Usage:
    # Auto-detect and process new files
    python scripts/pipeline_translate.py --auto

    # Process specific file
    python scripts/pipeline_translate.py --file Copilot.md

    # Dry run (no changes)
    python scripts/pipeline_translate.py --auto --dry-run

    # Skip to specific step
    python scripts/pipeline_translate.py --file Copilot.md --from-step translate

    # Run only a specific step
    python scripts/pipeline_translate.py --file Copilot.md --only-step translate

    # Cleanup temp files after processing
    python scripts/pipeline_translate.py --auto --cleanup
"""

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

# Project paths
PROJECT_ROOT = Path(__file__).parent.parent
DRAFTS_EN = PROJECT_ROOT / "content-drafts" / "en"
DRAFTS_EN_CLEAN = DRAFTS_EN / "clean"
CONTENT_EN = PROJECT_ROOT / "content" / "en" / "glossary"
CONTENT_JA = PROJECT_ROOT / "content" / "ja" / "glossary"
SCRIPTS_DIR = PROJECT_ROOT / "scripts"
CONFIG_DIR = PROJECT_ROOT / "config"
LOGS_DIR = PROJECT_ROOT / "logs"

# Pipeline steps
STEPS = [
    "cleanup",
    "enrich_en",
    "copy_to_content",
    "translate",
    "enrich_ja",
    "add_kana",
    "fix_term",
    "compare",
    "refresh_links",  # New: refresh all links after adding new pages
    "publish",
]


class PipelineLogger:
    """Simple logger for pipeline operations."""

    def __init__(self, log_file: Optional[Path] = None, verbose: bool = True):
        self.verbose = verbose
        self.log_file = log_file
        self.entries: List[str] = []

        if log_file:
            log_file.parent.mkdir(parents=True, exist_ok=True)

    def log(self, message: str, level: str = "INFO") -> None:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = f"[{timestamp}] [{level}] {message}"
        self.entries.append(entry)

        if self.verbose:
            icon = {"INFO": "ℹ️", "OK": "✓", "WARN": "⚠", "ERROR": "✗", "STEP": "▶"}.get(level, "")
            print(f"{icon} {message}")

    def save(self) -> None:
        if self.log_file and self.entries:
            with self.log_file.open("a", encoding="utf-8") as f:
                f.write("\n".join(self.entries) + "\n")


def detect_new_files(drafts_dir: Path, content_dir: Path) -> List[Path]:
    """Detect files in drafts that don't exist in content or are newer."""
    new_files = []

    if not drafts_dir.exists():
        return new_files

    for draft_file in drafts_dir.glob("*.md"):
        if draft_file.name.startswith("_") or draft_file.name == "README.md":
            continue

        content_file = content_dir / draft_file.name
        if not content_file.exists():
            new_files.append(draft_file)
        elif draft_file.stat().st_mtime > content_file.stat().st_mtime:
            new_files.append(draft_file)

    return new_files


def run_script(script_name: str, args: List[str], logger: PipelineLogger, dry_run: bool = False) -> bool:
    """Run a Python script with arguments."""
    script_path = SCRIPTS_DIR / script_name
    if not script_path.exists():
        # Try project root
        script_path = PROJECT_ROOT / script_name

    if not script_path.exists():
        logger.log(f"Script not found: {script_name}", "ERROR")
        return False

    cmd = [sys.executable, str(script_path)] + args

    if dry_run:
        logger.log(f"[DRY-RUN] Would run: {' '.join(cmd)}", "INFO")
        return True

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, cwd=str(PROJECT_ROOT))
        if result.returncode != 0:
            logger.log(f"Script failed: {script_name}\n{result.stderr}", "ERROR")
            return False
        if result.stdout.strip():
            for line in result.stdout.strip().split("\n"):
                logger.log(line, "INFO")
        return True
    except Exception as e:
        logger.log(f"Error running {script_name}: {e}", "ERROR")
        return False


def step_cleanup(file_path: Path, logger: PipelineLogger, dry_run: bool) -> Optional[Path]:
    """Step 1: Cleanup FlowHunt output."""
    logger.log(f"Cleaning up: {file_path.name}", "STEP")

    output_dir = DRAFTS_EN_CLEAN
    output_dir.mkdir(parents=True, exist_ok=True)

    if dry_run:
        logger.log(f"[DRY-RUN] Would cleanup {file_path} -> {output_dir / file_path.name}", "INFO")
        return output_dir / file_path.name

    success = run_script(
        "cleanup_flowhunt_output.py",
        [str(file_path), "--output", str(output_dir)],
        logger,
        dry_run,
    )

    if success:
        return output_dir / file_path.name
    return None


def step_enrich_en(file_path: Path, logger: PipelineLogger, dry_run: bool) -> bool:
    """Step 2: Enrich English article with keywords and links."""
    logger.log(f"Enriching (EN): {file_path.name}", "STEP")

    dict_path = CONFIG_DIR / "keyword_dictionary.json"
    if not dict_path.exists():
        logger.log("EN keyword dictionary not found, skipping enrichment", "WARN")
        return True

    return run_script(
        "enrich_glossary.py",
        [str(file_path), "--dict", str(dict_path)],
        logger,
        dry_run,
    )


def step_copy_to_content(file_path: Path, logger: PipelineLogger, dry_run: bool) -> Optional[Path]:
    """Step 3: Copy cleaned file to content/en/glossary/."""
    logger.log(f"Copying to content: {file_path.name}", "STEP")

    dest_path = CONTENT_EN / file_path.name
    CONTENT_EN.mkdir(parents=True, exist_ok=True)

    if dry_run:
        logger.log(f"[DRY-RUN] Would copy {file_path} -> {dest_path}", "INFO")
        return dest_path

    try:
        shutil.copy2(file_path, dest_path)
        logger.log(f"Copied to {dest_path}", "OK")
        return dest_path
    except Exception as e:
        logger.log(f"Copy failed: {e}", "ERROR")
        return None


def step_translate(file_path: Path, logger: PipelineLogger, dry_run: bool) -> Optional[Path]:
    """Step 4: Translate to Japanese using Claude API."""
    logger.log(f"Translating: {file_path.name}", "STEP")

    # Check API key
    api_key = os.getenv("CLAUDE_API_KEY") or os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        logger.log("CLAUDE_API_KEY not set. Add to .env or export.", "ERROR")
        return None

    dest_path = CONTENT_JA / file_path.name

    success = run_script(
        "translate_glossary_en_to_ja.py",
        ["--one-file", file_path.name, "--model", "claude-sonnet-4-5-20250929"],
        logger,
        dry_run,
    )

    if success:
        return dest_path
    return None


def step_enrich_ja(file_path: Path, logger: PipelineLogger, dry_run: bool) -> bool:
    """Step 5: Enrich Japanese article with keywords and links."""
    logger.log(f"Enriching (JA): {file_path.name}", "STEP")

    dict_path = CONFIG_DIR / "keyword_dictionary_ja.json"
    if not dict_path.exists():
        logger.log("JA keyword dictionary not found, skipping enrichment", "WARN")
        return True

    # Use enrich_glossary.py with JA dictionary
    return run_script(
        "enrich_glossary.py",
        [str(file_path), "--dict", str(dict_path)],
        logger,
        dry_run,
    )


def step_add_kana(file_path: Path, logger: PipelineLogger, dry_run: bool) -> bool:
    """Step 6: Add kana index metadata."""
    logger.log(f"Adding kana index: {file_path.name}", "STEP")

    args = [str(file_path)]
    if dry_run:
        args.append("--dry-run")

    return run_script("add_kana_index.py", args, logger, dry_run=False)


def step_fix_term(file_path: Path, logger: PipelineLogger, dry_run: bool) -> bool:
    """Step 7: Fix term readings (kanji -> kana)."""
    logger.log(f"Fixing term readings: {file_path.name}", "STEP")

    # This script processes the whole directory, so we run it once
    # For single file, we'd need to modify the script or skip
    if dry_run:
        logger.log("[DRY-RUN] Would fix term readings", "INFO")
        return True

    # Check if term starts with kanji - if not, skip
    try:
        content = file_path.read_text(encoding="utf-8")
        term_match = re.search(r"^term:\s*(.+)$", content, re.MULTILINE)
        if term_match:
            term = term_match.group(1).strip()
            first_char = term[0] if term else ""
            # Check if first char is kanji
            code = ord(first_char) if first_char else 0
            is_kanji = 0x4E00 <= code <= 0x9FFF or 0x3400 <= code <= 0x4DBF
            if not is_kanji:
                logger.log("Term already in kana, skipping fix", "INFO")
                return True

        return run_script(
            "fix_term_readings_ja.py",
            ["--ja-dir", str(file_path.parent)],
            logger,
            dry_run,
        )
    except Exception as e:
        logger.log(f"Error checking term: {e}", "WARN")
        return True


def step_compare(en_file: Path, ja_file: Path, logger: PipelineLogger, dry_run: bool) -> bool:
    """Step 8: Compare outlines between EN and JA."""
    logger.log(f"Comparing outlines: {en_file.name}", "STEP")

    if not en_file.exists() or not ja_file.exists():
        logger.log("Cannot compare - file missing", "WARN")
        return True

    return run_script(
        "compare_outline.py",
        [str(en_file), str(ja_file)],
        logger,
        dry_run,
    )


def step_refresh_links(logger: PipelineLogger, dry_run: bool) -> bool:
    """Step 9: Refresh all internal links in both EN and JA glossaries.
    
    This ensures all pages have up-to-date links to existing pages.
    """
    logger.log("Refreshing internal links for all glossary pages", "STEP")

    success = True

    # Refresh EN glossary
    en_dict = CONFIG_DIR / "keyword_dictionary.json"
    if en_dict.exists():
        if not run_script(
            "enrich_glossary.py",
            [str(CONTENT_EN), "--dict", str(en_dict)],
            logger,
            dry_run,
        ):
            logger.log("EN link refresh failed", "WARN")
            success = False
    else:
        logger.log("EN dictionary not found, skipping", "WARN")

    # Refresh JA glossary
    ja_dict = CONFIG_DIR / "keyword_dictionary_ja.json"
    if ja_dict.exists():
        if not run_script(
            "enrich_glossary.py",
            [str(CONTENT_JA), "--dict", str(ja_dict)],
            logger,
            dry_run,
        ):
            logger.log("JA link refresh failed", "WARN")
            success = False
    else:
        logger.log("JA dictionary not found, skipping", "WARN")

    return success


def step_publish(file_path: Path, logger: PipelineLogger, dry_run: bool) -> bool:
    """Step 10: Set draft: false."""
    logger.log(f"Publishing: {file_path.name}", "STEP")

    if dry_run:
        logger.log("[DRY-RUN] Would set draft: false", "INFO")
        return True

    try:
        content = file_path.read_text(encoding="utf-8")
        new_content = re.sub(r"draft:\s*true", "draft: false", content, flags=re.IGNORECASE)
        if new_content != content:
            file_path.write_text(new_content, encoding="utf-8")
            logger.log("Set draft: false", "OK")
        else:
            logger.log("Already published or no draft field", "INFO")
        return True
    except Exception as e:
        logger.log(f"Publish failed: {e}", "ERROR")
        return False


def process_file(
    file_path: Path,
    logger: PipelineLogger,
    dry_run: bool = False,
    from_step: str = "cleanup",
    only_step: Optional[str] = None,
    skip_publish: bool = True,
) -> bool:
    """Process a single file through the pipeline."""
    logger.log(f"{'='*60}", "INFO")
    logger.log(f"Processing: {file_path.name}", "INFO")
    logger.log(f"{'='*60}", "INFO")

    step_index = STEPS.index(from_step) if from_step in STEPS else 0
    # For --only-step, set end_index to same as start
    end_index = STEPS.index(only_step) if only_step else len(STEPS) - 1
    
    current_en_file = file_path
    current_ja_file: Optional[Path] = None
    
    def should_run(step_name: str) -> bool:
        """Check if a step should run based on from_step and only_step."""
        idx = STEPS.index(step_name)
        if only_step:
            return idx == step_index
        return step_index <= idx <= end_index

    # Step 1: Cleanup
    if should_run("cleanup"):
        cleaned = step_cleanup(file_path, logger, dry_run)
        if cleaned:
            current_en_file = cleaned
        elif not dry_run:
            return False

    # Step 2: Enrich EN
    if should_run("enrich_en"):
        if not step_enrich_en(current_en_file, logger, dry_run) and not dry_run:
            logger.log("Enrich EN failed, continuing anyway", "WARN")

    # Step 3: Copy to content
    if should_run("copy_to_content"):
        copied = step_copy_to_content(current_en_file, logger, dry_run)
        if copied:
            current_en_file = copied
        elif not dry_run:
            return False

    # Step 4: Translate
    if should_run("translate"):
        translated = step_translate(current_en_file, logger, dry_run)
        if translated:
            current_ja_file = translated
        elif not dry_run:
            return False

    # Steps 5-9 require JA file
    if current_ja_file is None:
        current_ja_file = CONTENT_JA / file_path.name

    if not current_ja_file.exists() and not dry_run and step_index >= STEPS.index("enrich_ja"):
        logger.log(f"JA file not found: {current_ja_file}", "ERROR")
        return False

    # Step 5: Enrich JA
    if should_run("enrich_ja"):
        if not step_enrich_ja(current_ja_file, logger, dry_run) and not dry_run:
            logger.log("Enrich JA failed, continuing anyway", "WARN")

    # Step 6: Add kana
    if should_run("add_kana"):
        if not step_add_kana(current_ja_file, logger, dry_run) and not dry_run:
            logger.log("Add kana failed, continuing anyway", "WARN")

    # Step 7: Fix term
    if should_run("fix_term"):
        if not step_fix_term(current_ja_file, logger, dry_run) and not dry_run:
            logger.log("Fix term failed, continuing anyway", "WARN")

    # Step 8: Compare
    if should_run("compare"):
        step_compare(current_en_file, current_ja_file, logger, dry_run)

    # Note: refresh_links is called once after all files are processed (in main)

    # Step 10: Publish (optional)
    if not skip_publish and should_run("publish"):
        step_publish(current_ja_file, logger, dry_run)
        step_publish(current_en_file, logger, dry_run)

    logger.log(f"Completed: {file_path.name}", "OK")
    return True


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Unified translation pipeline for FlowHunt glossary articles.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--auto",
        action="store_true",
        help="Auto-detect new/updated files in content-drafts/en/",
    )
    parser.add_argument(
        "--file",
        help="Process specific file (filename only, e.g., Copilot.md)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would happen without making changes",
    )
    parser.add_argument(
        "--from-step",
        choices=STEPS,
        default="cleanup",
        help="Start from specific step (default: cleanup)",
    )
    parser.add_argument(
        "--publish",
        action="store_true",
        help="Also set draft: false after processing",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        default=True,
        help="Verbose output (default: True)",
    )
    parser.add_argument(
        "--only-step",
        choices=STEPS,
        help="Run only this specific step (useful for debugging)",
    )
    parser.add_argument(
        "--cleanup",
        action="store_true",
        help="Delete content-drafts/en/clean/ files after successful processing",
    )
    parser.add_argument(
        "--skip-existing",
        action="store_true",
        help="Skip files that already have Japanese translations",
    )
    args = parser.parse_args()

    if not args.auto and not args.file:
        parser.error("Specify --auto or --file")

    # Handle --only-step (sets both from-step and to-step to same value)
    if args.only_step:
        args.from_step = args.only_step

    # Setup logging
    log_file = LOGS_DIR / f"pipeline_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
    logger = PipelineLogger(log_file=log_file, verbose=args.verbose)

    logger.log("=" * 60, "INFO")
    logger.log("FlowHunt Translation Pipeline v1.0.0", "INFO")
    logger.log(f"Mode: {'Auto-detect' if args.auto else 'Single file'}", "INFO")
    logger.log(f"Dry run: {args.dry_run}", "INFO")
    if args.only_step:
        logger.log(f"Only step: {args.only_step}", "INFO")
    else:
        logger.log(f"From step: {args.from_step}", "INFO")
    logger.log("=" * 60, "INFO")

    files_to_process: List[Path] = []

    if args.auto:
        # Detect new files
        new_files = detect_new_files(DRAFTS_EN, CONTENT_EN)
        if not new_files:
            logger.log("No new or updated files found in content-drafts/en/", "INFO")
            return
        files_to_process = new_files
        logger.log(f"Found {len(new_files)} file(s) to process", "INFO")
    else:
        # Single file
        file_path = DRAFTS_EN / args.file
        if not file_path.exists():
            # Try content/en/glossary
            file_path = CONTENT_EN / args.file
        if not file_path.exists():
            logger.log(f"File not found: {args.file}", "ERROR")
            sys.exit(1)
        files_to_process = [file_path]

    # Process files
    success_count = 0
    for file_path in files_to_process:
        if process_file(
            file_path,
            logger,
            dry_run=args.dry_run,
            from_step=args.from_step,
            only_step=args.only_step,
            skip_publish=not args.publish,
        ):
            success_count += 1

    # Step 9: Refresh all links (after all files are processed)
    # This ensures new pages can be linked from existing pages
    if success_count > 0 and not args.only_step:
        step_index = STEPS.index(args.from_step) if args.from_step in STEPS else 0
        if step_index <= STEPS.index("refresh_links"):
            step_refresh_links(logger, args.dry_run)

    # Cleanup temp files if requested
    if args.cleanup and success_count > 0 and not args.dry_run:
        logger.log("Cleaning up temporary files...", "STEP")
        cleaned_files = list(DRAFTS_EN_CLEAN.glob("*.md"))
        for f in cleaned_files:
            f.unlink()
            logger.log(f"Deleted: {f.name}", "INFO")
        logger.log(f"Cleaned {len(cleaned_files)} temp file(s)", "OK")

    # Summary
    logger.log("=" * 60, "INFO")
    logger.log(f"Completed: {success_count}/{len(files_to_process)} files", "INFO")
    logger.log("=" * 60, "INFO")

    logger.save()

    if success_count < len(files_to_process):
        sys.exit(1)


if __name__ == "__main__":
    main()
