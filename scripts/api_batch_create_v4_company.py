#!/usr/bin/env python3
"""
Company/Service Article Creation with Auto-Translation (v4)
会社・サービス記事用API自動化記事生成 + 日本語翻訳
"""

import os
import anthropic
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
import time
import argparse
import re
import textwrap
from typing import Dict, List, Tuple, Optional
import yaml

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

# 設定
API_KEY = os.environ.get("ANTHROPIC_API_KEY") or os.environ.get("CLAUDE_API_KEY")
MODEL = "claude-sonnet-4-5-20250929"  # 英語記事生成
TRANSLATION_MODEL = "claude-sonnet-4-5-20250929"  # 日本語翻訳

# ディレクトリ設定
BASE_DIR = Path("/Users/TM-MBP1/Documents/GitHub/hugo-boilerplate")
EN_OUTPUT_DIR = BASE_DIR / "content/en/glossary"
JA_OUTPUT_DIR = BASE_DIR / "content/ja/glossary"

# ============================================
# 会社/サービス用プロンプト
# ============================================

COMPANY_PROMPT = """You are an expert technical writer creating a comprehensive company/service glossary article.

COMPANY/SERVICE: {company_name}
ADDITIONAL CONTEXT: {context}

CRITICAL REQUIREMENTS:
✓ Language: ENGLISH ONLY
✓ Word count: 3,500-4,000 words (company articles are longer than general terms)
✓ Format: Professional, authoritative tone
✓ Include latest information provided in context
✓ Use proper English grammar throughout

EXACT FRONTMATTER (copy this format exactly):
---
title: "{company_name}"
date: {date}
translationKey: {slug}
description: "{description}"
keywords: {keywords}
category: "{category}"
type: glossary
draft: false
---

EXACT STRUCTURE (follow OpenAI.md as template):

## What is {company_name}?

Write 2-3 comprehensive paragraphs covering:
- Company overview, founding, headquarters location
- Core business focus and market position
- Key differentiators (e.g., open-source approach, European AI leader)

Then include:

**Key Products and Services:**
- **[Product 1]** - Brief description (1-2 sentences)
- **[Product 2]** - Brief description
- **[Product 3]** - Brief description
(List 5-8 main products/services)

## Company Background

First paragraph: Founding story (when, where, by whom, their backgrounds)

**Key Events:**
- **[Year]:** Event description
- **[Year]:** Event description
(Include 8-12 key milestones chronologically, especially recent events)

## Mission and Objectives

Brief intro paragraph about company mission.

**Objectives:**

**[Objective 1]:** Description (1-2 sentences)
**[Objective 2]:** Description
(List 4-6 key objectives)

## Major Products

### [Product Category 1] (e.g., Large Language Models)

**[Model/Product Name]:**
Detailed description including:
- Key specifications (parameters, context window, etc.)
- Capabilities and features
- Use cases
- Pricing if available

(Repeat for each major product category using H3 subheadings)

### [Product Category 2] (e.g., Chat Interface)

...

### [Product Category 3] (e.g., API Platform)

...

## How It Works

### Training and Development
Description of how the company develops its technology

### Model Architecture
Technical details appropriate for the company

### Deployment Options
How customers can access/deploy the technology

## Key Benefits

**[Benefit 1]:** 2-3 sentence explanation
**[Benefit 2]:** 2-3 sentence explanation
(List 8-10 key benefits)

## Common Use Cases

**[Use Case 1]:** Description with industry examples
**[Use Case 2]:** Description
(List 8-10 use cases)

## Challenges and Considerations

**[Challenge 1]:** Description and mitigation
**[Challenge 2]:** Description
(List 6-8 challenges)

## Corporate Structure and Security Considerations

### Jurisdiction and Corporate Structure
- Headquarters location
- Legal structure
- Ownership/control details

### Capital Structure and Major Investors
- Total funding raised
- Major investors (list top 5-8)
- Strategic partnerships
- Valuation if publicly available

### Data Governance and Sovereignty
- Data center locations
- Data residency options
- Data retention policies
- Government data access considerations

### Regulatory Compliance and Certifications
- Security certifications (SOC 2, ISO 27001, etc.)
- Privacy compliance (GDPR, CCPA, etc.)
- Industry-specific compliance

### Geopolitical and Security Considerations
- National security status
- Export restrictions if applicable
- Strategic considerations for international customers
- Relevant alliance memberships

## Future Directions

**[Direction 1]:** Description of future plans
**[Direction 2]:** Description
(List 5-6 future directions)

## References

Include 8-12 authoritative references using NUMBERED ACADEMIC CITATION FORMAT.

FORMAT (use numbered list, NOT bullet points):
1. Organization/Author. (Year). Title. Publication/Source. URL: https://...
2. Organization/Author. (Year). Title. Publication/Source. URL: https://...

EXAMPLES:
1. Mistral AI. (2025). Mistral Large 3 Announcement. Mistral AI Blog. URL: https://mistral.ai/news/mistral-large-3/
2. TechCrunch. (2025). Mistral AI raises €1.7B Series C led by ASML. TechCrunch. URL: https://techcrunch.com/2025/09/mistral-ai-series-c-funding/
3. Mistral AI. (n.d.). Official Documentation. Mistral AI Docs. URL: https://docs.mistral.ai/
4. Financial Times. (2025). ASML invests €1.3B in Mistral AI. Financial Times.

NOTE: Use "(n.d.)" for sources without specific dates. Include URL when available.

QUALITY CHECKLIST:
✓ 3,500-4,000 words
✓ All sections present with appropriate depth
✓ Latest information from context included
✓ Professional, authoritative tone
✓ Accurate technical details
✓ Proper attribution in References
✓ H3 subheadings used appropriately within Major Products section

IMPORTANT: Write complete, detailed content. Do not summarize or abbreviate. Include specific details like model specifications, pricing, investor names, funding amounts where available."""


# ============================================
# 翻訳関連
# ============================================

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n(.*)$", re.DOTALL)

DEFAULT_STYLE_GUIDE = textwrap.dedent(
    """# FlowHunt Glossary Translation Guide
- Maintain a professional yet approachable tone suitable for enterprise readers.
- Prefer standard Japanese technical terms; keep product names in English if commonly used.
- Use Japanese punctuation (、。) and full-width brackets when appropriate.
- When translating bullet lists, keep indentation and marker style identical to the source.
- Keep measurements, code snippets, CLI commands, URLs, and file paths exactly as provided.
"""
).strip()


def parse_markdown_with_frontmatter(text: str) -> Tuple[Dict, str]:
    m = FRONTMATTER_RE.match(text)
    if not m:
        return {}, text
    fm_raw, body = m.groups()
    try:
        fm = yaml.safe_load(fm_raw) or {}
    except Exception:
        fm = {}
    return fm, body


def dump_markdown_with_frontmatter(frontmatter: Dict, body: str) -> str:
    fm_yaml = yaml.safe_dump(frontmatter, allow_unicode=True, sort_keys=False).strip()
    return f"---\n{fm_yaml}\n---\n\n{body.lstrip()}"


class ClaudeTranslator:
    """日本語翻訳クラス"""
    
    def __init__(self, client, *, model: str, style_guide: Optional[str] = None,
                 temperature: float = 0.2, max_tokens: int = 32000):  # 長い記事の翻訳に対応
        self.client = client
        self.model = model
        self.style_guide = style_guide.strip() if style_guide else DEFAULT_STYLE_GUIDE
        self.temperature = temperature
        self.max_tokens = max_tokens

    def _run(self, *, user_text: str, system_prompt: str) -> str:
        """ストリーミングを使用して長時間リクエストに対応"""
        system_full = f"{self.style_guide}\n\n{system_prompt}".strip() if self.style_guide else system_prompt

        # ストリーミングを使用（10分以上かかる可能性があるリクエスト用）
        chunks = []
        with self.client.messages.stream(
            model=self.model,
            max_tokens=self.max_tokens,
            temperature=self.temperature,
            system=system_full,
            messages=[{"role": "user", "content": [{"type": "text", "text": user_text}]}],
        ) as stream:
            for text in stream.text_stream:
                chunks.append(text)
                # 進捗表示（オプション）
                if len(chunks) % 100 == 0:
                    print(".", end="", flush=True)
        
        print()  # 改行
        return "".join(chunks).strip()

    def translate_body(self, body_md: str) -> str:
        body_prompt = textwrap.dedent(
            """You are translating a technical glossary body from English to natural, professional Japanese.

- Input is Markdown.
- Preserve Markdown structure (headings, lists, code blocks, links, emphasis) exactly.
- Translate all prose into Japanese.
- Do NOT translate code inside fenced code blocks or inline code (backticks). Keep code as-is.
- Translate link anchor text, but keep URLs unchanged.
- Keep product names, company names, and technical terms in English where appropriate.
- IMPORTANT: Do NOT translate the "## References" section. Keep the entire References section in English exactly as-is, including all citations, author names, titles, publications, and URLs.

Return ONLY the translated Markdown body, with no extra commentary.
"""
        ).strip()
        return self._run(user_text=body_md, system_prompt=body_prompt)

    def translate_meta(self, title: str, description: str, keywords: List[str]) -> Tuple[str, str, List[str], str]:
        meta_prompt = f"""TITLE:
{title}

DESCRIPTION:
{description}

KEYWORDS (comma separated):
{', '.join(map(str, keywords))}

Please translate these into Japanese and respond ONLY in the following format:

TITLE_JA: <Japanese title - keep company/product names in English, add Japanese reading in parentheses if needed>
TERM_JA: <reading of the title in Japanese hiragana/katakana only>
DESCRIPTION_JA: <Japanese description>
KEYWORDS_JA: <keyword1>, <keyword2>, ...
"""
        meta_system = "You are translating glossary metadata (title, description, keywords) from English to Japanese. Follow the requested output format exactly."
        meta_text = self._run(user_text=meta_prompt, system_prompt=meta_system)

        title_ja = title
        desc_ja = description
        term_ja = ""
        keywords_ja = []
        
        for line in meta_text.splitlines():
            line = line.strip()
            if line.startswith("TITLE_JA:"):
                title_ja = line[len("TITLE_JA:"):].strip()
            elif line.startswith("TERM_JA:"):
                term_ja = line[len("TERM_JA:"):].strip()
            elif line.startswith("DESCRIPTION_JA:"):
                desc_ja = line[len("DESCRIPTION_JA:"):].strip()
            elif line.startswith("KEYWORDS_JA:"):
                raw = line[len("KEYWORDS_JA:"):].strip()
                if raw:
                    keywords_ja = [k.strip() for k in raw.split(",") if k.strip()]
        
        return title_ja, term_ja or title, keywords_ja or keywords, desc_ja


def rewrite_internal_links(body_ja: str) -> str:
    """内部リンクを /en/ から /ja/ に書き換え"""
    pattern = re.compile(r"/en/glossary/([^/]+)/")
    return pattern.sub(r"/ja/glossary/\1/", body_ja)


def translate_article(client, en_filepath: Path, ja_filepath: Path, slug: str) -> Tuple[bool, int, float]:
    """英語記事を日本語に翻訳"""
    
    # 長い会社記事用にmax_tokensを増加
    translator = ClaudeTranslator(client, model=TRANSLATION_MODEL, max_tokens=32000)
    
    start_time = time.time()
    
    try:
        # 英語ファイル読み込み
        raw = en_filepath.read_text(encoding="utf-8")
        fm, body = parse_markdown_with_frontmatter(raw)
        
        # 本文翻訳
        body_ja = translator.translate_body(body)
        body_ja = rewrite_internal_links(body_ja)
        
        # メタ翻訳
        title_en = fm.get("title", "")
        desc_en = fm.get("description", "")
        keywords_en = fm.get("keywords", []) or []
        
        title_ja, term_ja, keywords_ja, desc_ja = translator.translate_meta(
            title_en, desc_en, keywords_en
        )
        
        # 日本語フロントマター作成
        fm_ja = dict(fm)
        fm_ja["title"] = title_ja
        fm_ja["e-title"] = title_en
        fm_ja["term"] = term_ja
        fm_ja["url"] = f"/ja/glossary/{slug}/"
        fm_ja["description"] = desc_ja
        fm_ja["keywords"] = keywords_ja
        
        # ファイル保存
        ja_filepath.parent.mkdir(parents=True, exist_ok=True)
        ja_text = dump_markdown_with_frontmatter(fm_ja, body_ja)
        ja_filepath.write_text(ja_text, encoding="utf-8")
        
        elapsed = time.time() - start_time
        
        # 語数カウント
        ja_words = len(re.findall(r'[\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FFF\w]+', body_ja))
        
        return True, ja_words, elapsed
        
    except Exception as e:
        print(f"    ❌ Translation error: {e}")
        return False, 0, 0.0


# ============================================
# 英語記事生成
# ============================================

def generate_english_article(client, company_name: str, slug: str, date: str,
                             description: str, keywords: list, category: str,
                             context: str, output_dir: Path) -> Tuple[bool, int, int, float, float]:
    """英語記事を生成"""
    
    start_time = time.time()
    
    # キーワードをYAML形式に変換
    keywords_yaml = str(keywords)
    
    try:
        message = client.messages.create(
            model=MODEL,
            max_tokens=16000,
            temperature=0.1,
            messages=[{
                "role": "user",
                "content": COMPANY_PROMPT.format(
                    company_name=company_name,
                    slug=slug,
                    date=date,
                    description=description,
                    keywords=keywords_yaml,
                    category=category,
                    context=context
                )
            }]
        )
        
        content = message.content[0].text
        elapsed = time.time() - start_time
        
        # トークン数とコスト計算
        input_tokens = message.usage.input_tokens
        output_tokens = message.usage.output_tokens
        cost = (input_tokens * 3 / 1_000_000) + (output_tokens * 15 / 1_000_000)
        
        # 語数カウント
        words = len(re.findall(r'\b\w+\b', content))
        
        # ファイル保存
        output_dir.mkdir(parents=True, exist_ok=True)
        filepath = output_dir / f"{slug}.md"
        filepath.write_text(content, encoding='utf-8')
        
        return True, words, output_tokens, cost, elapsed
        
    except Exception as e:
        print(f"❌ English generation error: {e}")
        return False, 0, 0, 0.0, 0.0


# ============================================
# 会社データ定義
# ============================================

COMPANY_DATA = {
    "Mistral-AI": {
        "company_name": "Mistral AI",
        "description": "Mistral AI is a French artificial intelligence company developing open-weight large language models and the Le Chat assistant, positioned as Europe's leading AI challenger to OpenAI and Anthropic.",
        "keywords": ["Mistral AI", "Le Chat", "Mistral Large", "Mixtral", "open-weight AI", "European AI"],
        "category": "AI Chatbot & Automation",
        "context": """
LATEST INFORMATION (December 2025):

**Company Overview:**
- Founded: April 2023 in Paris, France
- Founders: Arthur Mensch (CEO, ex-Google DeepMind), Guillaume Lample (Chief Scientist, ex-Meta), Timothée Lacroix (CTO, ex-Meta)
- Founders met at École Polytechnique
- Headquarters: Paris, France
- Valuation: €11.7 billion ($13.8 billion) as of September 2025
- Total funding: ~€2.8 billion (~$3.05 billion)

**Latest Funding (September 2025 - Series C):**
- Amount: €1.7 billion
- Lead investor: ASML (€1.3 billion, 11% stake, largest shareholder)
- Other investors: NVIDIA, DST Global, Andreessen Horowitz, Bpifrance, General Catalyst, Index Ventures, Lightspeed
- ASML CFO Roger Dassen joins Strategic Committee
- Strategic partnership with ASML for semiconductor/AI value chain collaboration

**Latest Models (December 2025 - Mistral 3 Family):**

Mistral Large 3:
- 675 billion total parameters, 41 billion active (sparse MoE architecture)
- Multimodal (text + vision), multilingual (40+ languages)
- 256K context window
- Apache 2.0 license (open weights)
- Trained on 3,000 NVIDIA H200 GPUs
- Benchmarks: MMLU 88.7%, HumanEval 92.3%, MATH-500 93.6%
- LMArena: #2 in OSS non-reasoning models
- API pricing: ~80% cheaper than GPT-4o

Ministral 3 Family (edge/local deployment):
- 3B, 8B, 14B parameter dense models
- Each size has Base, Instruct, and Reasoning variants (9 models total)
- Native multimodal (vision) capabilities
- 256K context window
- Apache 2.0 license
- Optimized for: laptops, edge devices, robotics, drones
- 14B Reasoning achieves 85% on AIME '25

**Other Recent Models:**
- Mistral Medium 3 (May 2025): Balanced cost-performance, $0.40/M input, $2.00/M output
- Mistral Small 3.1 (March 2025): Efficient model
- Magistral (June 2025): Reasoning models (Small open-source, Medium proprietary)
- Voxtral (July 2025): First open-source audio model for voice
- Devstral 2 / Devstral Small 2 (December 2025): Coding-focused models
- Mistral Vibe (December 2025): CLI for AI-assisted development
- Mistral OCR (March 2025): PDF to text API
- Mistral Code (June 2025): Vibe-coding client (competes with Cursor, Copilot)

**Le Chat (Consumer Product):**
- Free tier with daily limits
- Le Chat Pro: €14.99/month ($14.99)
- Le Chat Team: For growing teams
- Le Chat Enterprise: Custom deployment, private infrastructure
- iOS/Android apps (February 2025, 1M downloads in 2 weeks)
- Features:
  - Flash Answers (~1000 words/sec generation)
  - Deep Research mode (July 2025)
  - Voice mode with Voxtral
  - Think mode with Magistral reasoning
  - Projects for organizing chats
  - Image generation (Black Forest Labs Flux)
  - Advanced image editing
  - Code interpreter
  - Memories feature (September 2025)
  - 20+ enterprise integrations (Asana, Atlassian, Box, Google Drive, Notion, Zapier)

**API Platform (La Plateforme):**
- Mistral Agents API (May 2025)
- Connectors directory (September 2025)
- Zero Data Retention option
- Generous free tier for experimentation

**Strategic Partnerships:**
- ASML: Semiconductor/AI collaboration, €1.3B investment
- NVIDIA: Training infrastructure, optimization partnership
- Microsoft Azure: Distribution partnership (€15M investment in 2024)
- Stellantis: In-car AI assistant
- Helsing: Defense tech, vision-language-action models for drones
- Singapore HTX: Robots, cybersecurity, fire safety
- HSBC: Financial services partnership

**Deployment Options:**
- Mistral AI Studio
- Amazon Bedrock (first to offer Mistral 3)
- Azure Foundry
- Hugging Face
- Modal, IBM WatsonX, OpenRouter, Fireworks, Together AI
- Self-deployment for Enterprise

**European AI Leadership:**
- Only European company competitive with OpenAI/Anthropic
- GDPR-native, EU data residency
- French president Macron publicly endorsed Le Chat
- Independence from US tech platforms emphasized
- AI Act alignment and transparency focus

**Revenue:**
- Annualized revenue exceeded $100M by June 2025
- Eight-digit range reported by multiple sources
"""
    },
}


# ============================================
# メイン処理
# ============================================

def main():
    parser = argparse.ArgumentParser(description="会社/サービス記事生成 + 日本語翻訳 (v4)")
    parser.add_argument('--company', required=True, help='会社スラッグ (e.g., Mistral-AI)')
    parser.add_argument('--test', action='store_true', help='テストモード（別ディレクトリに出力）')
    parser.add_argument('--en-only', action='store_true', help='英語のみ生成（翻訳スキップ）')
    parser.add_argument('--ja-only', action='store_true', help='日本語翻訳のみ（既存英語ファイルから）')
    parser.add_argument('--output-dir', help='出力ディレクトリ（テストモード用）')
    
    args = parser.parse_args()
    
    # 会社データ取得
    if args.company not in COMPANY_DATA:
        print(f"❌ Unknown company: {args.company}")
        print(f"Available: {list(COMPANY_DATA.keys())}")
        return
    
    data = COMPANY_DATA[args.company]
    
    # 出力ディレクトリ設定
    if args.test:
        base_test_dir = Path(args.output_dir) if args.output_dir else BASE_DIR / "content"
        en_output_dir = base_test_dir / "en/glossary-api-test-v4"
        ja_output_dir = base_test_dir / "ja/glossary-api-test-v4"
        print(f"🧪 テストモード")
    else:
        en_output_dir = EN_OUTPUT_DIR
        ja_output_dir = JA_OUTPUT_DIR
    
    # APIクライアント作成
    if not API_KEY:
        print("❌ ANTHROPIC_API_KEY is not set")
        return
    
    client = anthropic.Anthropic(api_key=API_KEY)
    
    # 実行開始
    print(f"\n{'='*70}")
    print(f"🏢 会社/サービス記事生成 (v4)")
    print(f"{'='*70}")
    print(f"会社: {data['company_name']}")
    print(f"英語出力: {en_output_dir}")
    print(f"日本語出力: {ja_output_dir}")
    print(f"モード: {'英語のみ' if args.en_only else '日本語のみ' if args.ja_only else '英語+日本語'}")
    print(f"{'='*70}\n")
    
    total_cost = 0.0
    total_time = 0.0
    
    en_filepath = en_output_dir / f"{args.company}.md"
    ja_filepath = ja_output_dir / f"{args.company}.md"
    
    # 英語記事生成
    if not args.ja_only:
        print("📝 英語記事を生成中...")
        en_success, en_words, en_tokens, en_cost, en_time = generate_english_article(
            client=client,
            company_name=data['company_name'],
            slug=args.company,
            date="2025-12-21",
            description=data['description'],
            keywords=data['keywords'],
            category=data['category'],
            context=data['context'],
            output_dir=en_output_dir
        )
        
        if en_success:
            word_status = "✅" if 3500 <= en_words <= 4000 else ("⚠️" if 3000 <= en_words else "❌")
            print(f"   ✅ 英語記事完了: {en_words}語 {word_status}, {en_tokens:,}トークン, ${en_cost:.4f}, {en_time:.1f}秒")
            total_cost += en_cost
            total_time += en_time
        else:
            print(f"   ❌ 英語記事生成失敗")
            if not args.ja_only:
                return
    
    # 日本語翻訳
    if not args.en_only:
        if not en_filepath.exists():
            print(f"❌ 英語ファイルが見つかりません: {en_filepath}")
            return
        
        print("\n🌐 日本語に翻訳中...")
        ja_success, ja_chars, ja_time = translate_article(
            client=client,
            en_filepath=en_filepath,
            ja_filepath=ja_filepath,
            slug=args.company
        )
        
        if ja_success:
            # 翻訳コスト概算（入力+出力で約10Kトークン想定）
            ja_cost_est = 0.03  # 概算
            print(f"   ✅ 日本語翻訳完了: {ja_chars:,}文字, ~${ja_cost_est:.4f}, {ja_time:.1f}秒")
            total_cost += ja_cost_est
            total_time += ja_time
        else:
            print(f"   ❌ 日本語翻訳失敗")
    
    # サマリー
    print(f"\n{'='*70}")
    print(f"📊 完了サマリー")
    print(f"{'='*70}")
    if not args.ja_only:
        print(f"英語ファイル: {en_filepath}")
    if not args.en_only:
        print(f"日本語ファイル: {ja_filepath}")
    print(f"合計コスト: ~${total_cost:.4f}")
    print(f"合計時間: {total_time:.1f}秒")
    print(f"{'='*70}\n")


if __name__ == "__main__":
    main()
