---
title: "JamC-QA"
lastmod: 2025-12-18
date: 2025-12-18
translationKey: "jamc-qa"
description: "A Japanese knowledge test with 2,341 multiple-choice questions that evaluates how well AI models understand Japanese culture, history, geography, customs, and other areas important to Japanese society."
keywords: ["JamC-QA", "Japanese LLMs", "benchmark dataset", "multiple-choice QA", "LLM evaluation"]
category: "Natural Language Processing"
type: "glossary"
draft: false
---

## What is JamC-QA?

JamC-QA (Japanese Multiple Choice Question Answering) is a large-scale benchmark dataset specifically designed to evaluate large language models on Japanese-specific knowledge and cultural understanding. The dataset tests models across eight carefully selected domains including Japanese culture, customs, regional identity, geography, history, government, law, and healthcare.

The benchmark fills a critical gap in LLM evaluation by focusing on knowledge areas underrepresented or entirely absent in major international benchmarks like MMLU, HellaSwag, or SQuAD. JamC-QA enables fair, domain-specific comparison of Japanese and multilingual LLMs, supports leaderboard evaluations and ablation studies, and provides essential validation for AI systems serving Japanese-speaking users.

JamC-QA is widely adopted for benchmarking Japanese language models, appears on major leaderboards including the Swallow LLM Leaderboard, and is referenced in academic literature as a gold standard for Japan-centric factual and general knowledge proficiency.

## Dataset Composition

### Knowledge Categories

JamC-QA comprises 2,341 multiple-choice questions across eight knowledge categories selected for their relevance to Japanese society and absence from other popular QA benchmarks:

| Category | Dev | Test | Focus Area |
|----------|-----|------|------------|
| Culture | 4 | 640 | Arts, cinema, literature, music, cultural literacy |
| Custom | 4 | 200 | Social customs, etiquette, festivals, traditions |
| Regional Identity | 4 | 397 | Regional knowledge, dialects, local phenomena |
| Geography | 4 | 272 | Physical geography, place names, natural features |
| History | 4 | 343 | Historical events, figures, periods, cultural shifts |
| Government | 4 | 110 | Political systems, policies, governmental roles |
| Law | 4 | 299 | Legislation, legal systems, rights, regulations |
| Healthcare | 4 | 48 | Medical systems, terminology, public health |
| **Total**|**32**|**2,309**| |**Category Selection Rationale:**- Core to Japanese daily life and culture
- Underrepresented in global benchmarks
- Requires specific cultural and linguistic knowledge
- Spans factual recall to contextual understanding

### Data Splits

**Development Split (32 questions)**- Four questions per category
- Used for few-shot evaluation
- Enables model calibration with minimal exposure
- Supports prompt engineering and fine-tuning

**Test Split (2,309 questions)**- Main evaluation testbed
- Statistically robust sample per category
- Used for leaderboard rankings
- Enables detailed performance analysis

## Dataset Structure

### Data Format

Each instance is a single multiple-choice question with four answer options and one correct answer. The dataset is formatted for Hugging Face `datasets` library integration and supports evaluation frameworks like FlexEval.

**Example Instance:**```json
{
  "qid": "jamcqa-test-culture-00001",
  "category": "culture",
  "question": "「狂った世で気が狂うなら気は確かだ」の名言を残した映画はどれ?",
  "choice0": "影武者",
  "choice1": "羅生門",
  "choice2": "隠し砦の三悪人",
  "choice3": "乱",
  "answer_index": 3
}
```

### Field Definitions

| Field | Type | Description |
|-------|------|-------------|
| `qid` | string | Unique question identifier |
| `category` | string | Knowledge category label |
| `question` | string | Question text in Japanese (half-width except katakana) |
| `choice0-3` | string | Four answer options (half-width except katakana) |
| `answer_index` | integer | Index of correct answer (0-3) |

**Data Constraints:**- No line breaks in any field
- Leading and trailing whitespace removed
- Half-width characters except for katakana
- Each question curated for cultural accuracy

## Evaluation Methodology

### Primary Metric

**Exact Match Accuracy**Models must output the exact answer string (not just the label or index). This strict criterion ensures true retrieval or generation capability, not approximation.**Calculation:**```
Accuracy = (Number of exact matches) / (Total number of questions)
```**Category-Level Analysis**Accuracy reported per category enables fine-grained analysis of model strengths and weaknesses across knowledge domains.**Why Exact Match?**- Ensures precise answer generation capability
- Critical for factual and culturally nuanced questions
- Prevents partial credit for close but incorrect answers
- Validates true understanding versus pattern matching

### Performance Analysis

Category-level results reveal:
- Domain-specific model strengths
- Knowledge gaps requiring attention
- Transfer learning effectiveness
- Cultural adaptation success

## Leaderboard Results

Representative performance from major Japanese LLM leaderboard (accuracy scores):

| Model | All | Culture | Custom | Regional | Geography | History | Government | Law | Healthcare |
|-------|-----|---------|--------|----------|-----------|---------|------------|-----|------------|
| sarashina2-8x70b | 0.725 | 0.714 | 0.775 | 0.761 | 0.654 | 0.784 | 0.736 | 0.632 | 0.917 |
| sarashina2-70b | 0.725 | 0.719 | 0.745 | 0.736 | 0.673 | 0.764 | 0.764 | 0.666 | 0.917 |
| Llama-3.3-Swallow-70B-v0.4 | 0.697 | 0.689 | 0.775 | 0.589 | 0.566 | 0.776 | 0.773 | 0.783 | 0.854 |
| RakutenAI-2.0-8x7B | 0.633 | 0.622 | 0.725 | 0.617 | 0.511 | 0.714 | 0.709 | 0.575 | 0.813 |
| plamo-100b | 0.603 | 0.602 | 0.650 | 0.637 | 0.504 | 0.682 | 0.609 | 0.515 | 0.688 |

**Key Observations:**- Best overall performance: sarashina2 models (0.725)
- Strongest category: Healthcare (up to 0.917)
- Greatest variation: Regional identity and geography
- Model diversity: Japanese-specialized and multilingual LLMs

## Usage and Implementation

### Loading with Hugging Face

```python
import datasets

# Load dataset
jamcqa = datasets.load_dataset('sbintuitions/JamC-QA', 'v1.0')

# Access splits
jamcqa_test = jamcqa['test']
jamcqa_dev = jamcqa['dev']

# Inspect question
print(jamcqa_test[0])
```

**Dataset Viewer:**Browse and filter interactively on Hugging Face Data Studio.

### Evaluation with FlexEval

FlexEval (v0.13.3+) provides unified evaluation for diverse tasks and metrics:

```bash
flexeval_lm \
  --language_model HuggingFaceLM \
  --language_model.model "sbintuitions/sarashina2.2-0.5b" \
  --language_model.default_gen_kwargs "{ do_sample: false }" \
  --eval_setup "jamcqa" \
  --save_dir "results/jamcqa"
```

**Configuration:**- `do_sample: false` ensures deterministic (greedy) decoding
- Output includes exact match accuracy and generation statistics
- Supports batch processing and parallel evaluation

## Practical Applications

### LLM Benchmarking

**Standard Comparison:**- Quantitative evaluation of Japanese LLMs
- Fair comparison across model architectures
- Performance tracking across versions
- Transfer learning assessment

**Model Selection:**- Identify best model for Japanese applications
- Validate cultural adaptation effectiveness
- Compare specialized vs multilingual models
- Guide deployment decisions

### Research Applications

**Ablation Studies:**- Identify domain-specific strengths and weaknesses
- Evaluate training data impact
- Test architecture variations
- Analyze fine-tuning effectiveness

**Cross-Lingual Transfer:**- Assess knowledge transfer from multilingual training
- Evaluate translation-based approaches
- Test cultural adaptation strategies
- Compare monolingual vs multilingual performance

### Educational Technology

**AI Tutor Development:**- Validate Japanese knowledge accuracy
- Test cultural understanding
- Ensure appropriate content delivery
- Verify regional awareness

**Assessment Systems:**- Benchmark question generation systems
- Validate answer evaluation accuracy
- Test adaptive learning algorithms
- Ensure cultural appropriateness

### Cultural Adaptation

**Localization Validation:**- Verify AI meets local knowledge expectations
- Test cultural sensitivity
- Validate regional understanding
- Ensure appropriate content generation

## Related Benchmarks

JamC-QA is part of a growing Japanese LLM evaluation ecosystem:

**Complementary Benchmarks:**-**MMLU-ProX (Japanese):**Multi-discipline college-level reasoning
- **GPQA (Japanese):**Graduate-level science QA
- **JHumanEval:**Japanese code generation
- **MATH-100 (Japanese):**Competition-level mathematics
- **M-IFEval-Ja:**Instruction following control**Benchmark Ecosystem Benefits:**- Cross-benchmark transfer studies
- Comprehensive model diagnostics
- Local relevance validation
- International comparison baseline

## Implementation Best Practices

**Evaluation Setup:**- Use deterministic decoding for reproducibility
- Report category-level results
- Include confidence intervals
- Document evaluation parameters

**Model Preparation:**- Validate Japanese text processing
- Test tokenization appropriately
- Verify encoding handling
- Ensure proper formatting

**Results Analysis:**- Compare across categories
- Identify systematic weaknesses
- Analyze error patterns
- Test edge cases

**Continuous Improvement:**- Regular benchmark updates
- Track performance over time
- Monitor distribution shifts
- Validate new model versions

## References


1. JamC-QA. Service. Dataset for Question Answering. URL: https://huggingface.co/datasets/sbintuitions/JamC-QA

2. JamC-QA. Report. Dataset README Documentation. URL: https://huggingface.co/datasets/sbintuitions/JamC-QA/blob/main/README.md

3. Chokkan. (n.d.). Swallow LLM Leaderboard. Social Media Post. URL: https://x.com/chokkanorg/status/1984170094076031297

4. Ryokan. (n.d.). FlexEval Framework. Research Project Website. URL: https://ryokan0123.github.io/

5. Anonymous. (2025). MMLU-ProX (Japanese). Research Paper. URL: https://arxiv.org/abs/2503.10497

6. Anonymous. (2025). GPQA (Japanese). Research Paper. URL: https://arxiv.org/abs/2502.07346

7. Anonymous. (2024). JHumanEval Benchmark. Conference Proceedings. URL: https://anlp.jp/proceedings/annual_meeting/2024/pdf_dir/B1-4.pdf

8. Anonymous. (2025). M-IFEval-Ja. Conference Paper. URL: https://aclanthology.org/2025.naacl-main.123/

9. Hugging Face. (n.d.). Hugging Face Datasets Documentation. Technical Documentation. URL: https://huggingface.co/docs/datasets/index
