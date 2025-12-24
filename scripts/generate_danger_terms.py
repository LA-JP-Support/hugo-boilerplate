#!/usr/bin/env python3

import argparse
import csv
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Set, Tuple


@dataclass(frozen=True)
class DangerTerm:
    keyword: str
    normalized: str
    reason: str
    score: int
    source: str


EN_COMMON_WORDS: Set[str] = {
    "make",
    "did",
    "do",
    "get",
    "set",
    "use",
    "platform",
    "token",
    "workflow",
}

JA_GENERIC: Set[str] = {
    "トークン",
    "プロンプト",
    "精度",
    "推論",
    "メタ",
    "自動化",
}


def normalize_en(s: str) -> str:
    return re.sub(r"\s+", " ", s.strip().lower())


def normalize_ja(s: str) -> str:
    return s.strip()


def load_existing(path: Path) -> Dict[str, DangerTerm]:
    if not path.exists():
        return {}

    out: Dict[str, DangerTerm] = {}
    with open(path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            keyword = (row.get("keyword") or "").strip()
            normalized = (row.get("normalized") or keyword).strip()
            if not keyword or not normalized:
                continue
            reason = (row.get("reason") or "").strip()
            try:
                score = int((row.get("score") or "0").strip() or 0)
            except ValueError:
                score = 0
            source = (row.get("source") or "manual").strip()
            out[normalized.lower()] = DangerTerm(
                keyword=keyword,
                normalized=normalized,
                reason=reason,
                score=score,
                source=source,
            )
    return out


def iter_link_database_rows(path: Path) -> Iterable[Dict[str, str]]:
    with open(path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        yield from reader


def suggest_danger_terms_en(database_csv: Path, min_score: int) -> Dict[str, DangerTerm]:
    out: Dict[str, DangerTerm] = {}
    for row in iter_link_database_rows(database_csv):
        keyword = (row.get("keyword") or "").strip()
        normalized = (row.get("normalized") or "").strip() or normalize_en(keyword)
        variation_type = (row.get("variation_type") or "").strip()

        if not keyword:
            continue

        norm = normalize_en(normalized)
        score = 0
        reasons: List[str] = []

        if norm in EN_COMMON_WORDS:
            score += 50
            reasons.append("common_word")

        # single ASCII word gets extra risk
        if re.fullmatch(r"[A-Za-z]+", keyword):
            if len(keyword) <= 4:
                score += 30
                reasons.append("short_ascii")
            else:
                score += 10
                reasons.append("ascii_word")

        if variation_type == "without_parens":
            score += 15
            reasons.append("without_parens")

        if score >= min_score:
            out[norm] = DangerTerm(
                keyword=keyword,
                normalized=norm,
                reason=";".join(reasons) if reasons else "heuristic",
                score=score,
                source="auto",
            )

    return out


def suggest_danger_terms_ja(database_csv: Path, min_score: int) -> Dict[str, DangerTerm]:
    out: Dict[str, DangerTerm] = {}
    for row in iter_link_database_rows(database_csv):
        keyword = (row.get("keyword") or "").strip()
        normalized = (row.get("normalized") or "").strip() or normalize_ja(keyword)
        variation_type = (row.get("variation_type") or "").strip()

        if not keyword:
            continue

        norm = normalize_ja(normalized)
        score = 0
        reasons: List[str] = []

        if keyword in JA_GENERIC or norm in JA_GENERIC:
            score += 60
            reasons.append("generic_term")

        if len(keyword) <= 2:
            score += 25
            reasons.append("very_short")

        if re.fullmatch(r"[\u30A0-\u30FFー]+", keyword) and len(keyword) <= 6:
            score += 10
            reasons.append("short_katakana")

        if variation_type == "without_parens" or variation_type == "without_fullwidth_parens":
            score += 10
            reasons.append("without_parens")

        if score >= min_score:
            out[norm] = DangerTerm(
                keyword=keyword,
                normalized=norm,
                reason=";".join(reasons) if reasons else "heuristic",
                score=score,
                source="auto",
            )

    return out


def write_csv(path: Path, terms: List[DangerTerm]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["keyword", "normalized", "reason", "score", "source"])
        writer.writeheader()
        for t in terms:
            writer.writerow(
                {
                    "keyword": t.keyword,
                    "normalized": t.normalized,
                    "reason": t.reason,
                    "score": str(t.score),
                    "source": t.source,
                }
            )


def write_markdown(report_path: Path, en_terms: List[DangerTerm], ja_terms: List[DangerTerm]) -> None:
    report_path.parent.mkdir(parents=True, exist_ok=True)

    def row(t: DangerTerm) -> str:
        return f"| {t.keyword} | {t.normalized} | {t.score} | {t.source} | {t.reason} |"

    lines: List[str] = []
    lines.append("# Danger Terms (Auto-link Denylist)")
    lines.append("")
    lines.append("This file is generated. Edit `databases/danger_terms_en.csv` / `databases/danger_terms_ja.csv` for the authoritative denylist.")
    lines.append("")

    lines.append("## EN")
    lines.append("")
    lines.append("| keyword | normalized | score | source | reason |")
    lines.append("|---|---|---:|---|---|")
    for t in en_terms[:200]:
        lines.append(row(t))
    lines.append("")

    lines.append("## JA")
    lines.append("")
    lines.append("| keyword | normalized | score | source | reason |")
    lines.append("|---|---|---:|---|---|")
    for t in ja_terms[:200]:
        lines.append(row(t))
    lines.append("")

    report_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def merge(existing: Dict[str, DangerTerm], suggested: Dict[str, DangerTerm]) -> List[DangerTerm]:
    merged: Dict[str, DangerTerm] = dict(existing)
    for norm, term in suggested.items():
        if norm not in merged:
            merged[norm] = term
    out = list(merged.values())
    out.sort(key=lambda t: (-t.score, t.normalized.lower()))
    return out


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate danger term denylist from link_database_*.csv")
    parser.add_argument("--lang", choices=["en", "ja"], required=True)
    parser.add_argument("--database", type=Path, default=None)
    parser.add_argument("--output", type=Path, default=None)
    parser.add_argument("--report", type=Path, default=Path("docs/danger_terms.md"))
    parser.add_argument("--min-score", type=int, default=60)

    args = parser.parse_args()

    database = args.database or Path(f"databases/link_database_{args.lang}.csv")
    output = args.output or Path(f"databases/danger_terms_{args.lang}.csv")

    existing = load_existing(output)

    if args.lang == "en":
        suggested = suggest_danger_terms_en(database, min_score=args.min_score)
    else:
        suggested = suggest_danger_terms_ja(database, min_score=args.min_score)

    merged_terms = merge(existing, suggested)
    write_csv(output, merged_terms)

    # Build combined report (read both outputs)
    en_terms = merge(load_existing(Path("databases/danger_terms_en.csv")), {})
    ja_terms = merge(load_existing(Path("databases/danger_terms_ja.csv")), {})
    write_markdown(args.report, en_terms, ja_terms)

    print(f"Wrote: {output} (terms={len(merged_terms)})")
    print(f"Wrote: {args.report}")


if __name__ == "__main__":
    main()
