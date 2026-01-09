---
title: "JamC-QA – Japanese Multiple Choice Question Answering Benchmark"
date: 2025-12-17
translationKey: "jamc-qa-japanese-multiple-choice-question-answering-benchmark"
description: "JamC-QA is a large-scale benchmark dataset for evaluating Japanese LLMs on multiple-choice QA across diverse domains like culture, history, geography, and healthcare."
keywords: ["JamC-QA", "Japanese LLMs", "benchmark dataset", "multiple-choice QA", "LLM evaluation"]
category: "Natural Language Processing"
type: "glossary"
draft: false
---

## Overview

<strong>JamC-QA</strong>is a large-scale benchmark dataset specifically designed to test and evaluate large language models (LLMs) on Japanese-specific multiple-choice question answering. The questions span a wide range of domains including Japanese culture, customs, regional identity, geography, history, government, law, and healthcare.

- <strong>Official Hugging Face dataset card</strong>: [sbintuitions/JamC-QA](https://huggingface.co/datasets/sbintuitions/JamC-QA)
- <strong>Official dataset README</strong>: README.md

JamC-QA is widely adopted for benchmarking and leaderboard evaluations, such as the [Swallow LLM Leaderboard](https://x.com/chokkanorg/status/1984170094076031297) and is referenced in academic literature as a gold standard for Japan-centric factual and general knowledge proficiency.

## Purpose and Scope

JamC-QA fills a crucial gap in LLM evaluation by focusing on domains and knowledge areas that are underrepresented or entirely absent in major international benchmarks like MMLU, HellaSwag, or SQuAD. Its core objectives:

- <strong>Measure LLMs’ ability to answer factual multiple-choice questions relevant to Japanese society.</strong>- <strong>Enable fair, domain-specific comparison of Japanese and multilingual LLMs</strong>by focusing on topics not typically covered in global datasets.
- <strong>Support leaderboard evaluations, ablation studies, and transfer learning research</strong>for Japanese natural language processing (NLP).

This dataset is thus essential for:
- Researchers aiming for fair, rigorous LLM comparisons on Japanese knowledge.
- Developers of AI systems for Japanese-speaking users.
- Educational technology solutions that require reliable Japan-specific knowledge.

## Dataset Composition

### Categories

JamC-QA is meticulously structured into <strong>eight knowledge categories</strong>that are core to Japanese society and culture:

| Category           | dev | test |
|--------------------|-----|------|
| culture            | 4   | 640  |
| custom             | 4   | 200  |
| regional_identity  | 4   | 397  |
| geography          | 4   | 272  |
| history            | 4   | 343  |
| government         | 4   | 110  |
| law                | 4   | 299  |
| healthcare         | 4   | 48   |
| <strong>Total</strong>| 32  | 2,309|

<strong>Key features of the categories:</strong>- <strong>Culture:</strong>Japanese arts, cinema, literature, music, and general cultural literacy.
- <strong>Custom:</strong>Social customs, etiquette, festivals, and traditional practices.
- <strong>Regional_identity:</strong>Knowledge unique to specific regions, dialects, and local phenomena.
- <strong>Geography:</strong>Physical geography, place names, natural features, and population distributions.
- <strong>History:</strong>Chronological events, historical figures, periods, and cultural shifts.
- <strong>Government:</strong>Organizational structure, political systems, policies, and governmental roles.
- <strong>Law:</strong>Legislation, legal systems, rights, and societal regulations.
- <strong>Healthcare:</strong>Medical systems, terminology, public health, and healthcare policy.

These categories were selected based on their relevance to Japanese life and their absence from other popular QA benchmarks, ensuring robust evaluation of Japan-specific knowledge.

### Data Splits

| Split | Purpose                  | Size | Notes                         |
|-------|--------------------------|------|-------------------------------|
| dev   | Few-shot evaluation      | 32   | Four per category             |
| test  | Main evaluation          | 2,309| For leaderboard and analysis  |

- <strong>dev split:</strong>Used for few-shot or prompt-based evaluation, ensuring models can be calibrated or tuned with minimal exposure.
- <strong>test split:</strong>The main testbed for leaderboard rankings and scientific analysis; contains a statistically robust number of questions per category.

<strong>Total dataset size:</strong>2,341 examples across both splits ([source](https://huggingface.co/datasets/sbintuitions/JamC-QA)).

## Dataset Structure and Fields

Each data instance is a single multiple-choice question with four answer options and a single correct answer. The dataset is formatted for ease of use with the Hugging Face `datasets` library and supports integration with evaluation frameworks such as FlexEval.

### Example Instance

```json
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

### Field Definitions and Constraints

| Field          | Type    | Description                                                             |
|----------------|---------|-------------------------------------------------------------------------|
| `qid`          | string  | Unique identifier for the question instance.                            |
| `category`     | string  | Category label (e.g., culture, custom, etc.).                          |
| `question`     | string  | Question text in Japanese (half-width except for katakana).             |
| `choice0`-`3`  | string  | Four answer options, also half-width except for katakana.               |
| `answer_index` | integer | Index of the correct answer (0–3).                                      |

<strong>Constraints:</strong>- No line breaks in any string fields.
- Leading and trailing whitespace is removed from all fields.
- Each question is curated for both broad general and detailed knowledge of Japan.

For more schema details, see the [dataset card fields section](https://huggingface.co/datasets/sbintuitions/JamC-QA/blob/main/README.md#dataset-structure).

## Evaluation Metric

### Accuracy and Category-Level Analysis

<strong>Primary metric:</strong> <strong>Accuracy</strong>is used as the main evaluation criterion.
- The model must output the exact answer string (not just the label/index).
- <strong>Accuracy is calculated as:</strong>`Accuracy = (Number of exact matches) / (Total number of questions)`

<strong>Category-level accuracy</strong>is also reported, enabling fine-grained analysis of model strengths and weaknesses across domains.

<strong>Why exact match?</strong>- This strict criterion ensures that models are truly capable of retrieving or generating the precise correct answer, not merely a close approximation or the correct label.
- This is especially important for factual and culturally nuanced questions where partial correctness is not sufficient.

[JamC-QA Evaluation Metric Documentation](https://huggingface.co/datasets/sbintuitions/JamC-QA/blob/main/README.md#evaluation-metric)

## Leaderboard and Comparative Results

JamC-QA is an official benchmark on major Japanese LLM leaderboards such as [Swallow LLM Leaderboard](https://x.com/chokkanorg/status/1984170094076031297). The leaderboard ranks models by overall and per-category accuracy.

<strong>Representative results (as of latest available):</strong>| Model                                 | All   | culture | custom | regional_identity | geography | history | government | law   | healthcare |
|----------------------------------------|-------|---------|--------|------------------|-----------|---------|------------|-------|------------|
| sarashina2-8x70b                      | 0.725 | 0.714   | 0.775  | 0.761            | 0.654     | 0.784   | 0.736      | 0.632 | 0.917      |
| sarashina2-70b                        | 0.725 | 0.719   | 0.745  | 0.736            | 0.673     | 0.764   | 0.764      | 0.666 | 0.917      |
| Llama-3.3-Swallow-70B-v0.4             | 0.697 | 0.689   | 0.775  | 0.589            | 0.566     | 0.776   | 0.773      | 0.783 | 0.854      |
| RakutenAI-2.0-8x7B                    | 0.633 | 0.622   | 0.725  | 0.617            | 0.511     | 0.714   | 0.709      | 0.575 | 0.813      |
| plamo-100b                            | 0.603 | 0.602   | 0.650  | 0.637            | 0.504     | 0.682   | 0.609      | 0.515 | 0.688      |
| Mixtral-8x7B-v0.1-japanese            | 0.593 | 0.602   | 0.670  | 0.579            | 0.493     | 0.612   | 0.736      | 0.545 | 0.667      |
| Meta-Llama-3.1-405B                   | 0.571 | 0.558   | 0.545  | 0.484            | 0.500     | 0.679   | 0.646      | 0.629 | 0.688      |
| llm-jp-3.1-8x13b                      | 0.568 | 0.595   | 0.635  | 0.582            | 0.449     | 0.589   | 0.627      | 0.502 | 0.625      |
| Nemotron-4-340B-Base                  | 0.567 | 0.573   | 0.615  | 0.511            | 0.467     | 0.595   | 0.727      | 0.582 | 0.667      |
| Qwen2.5-72B                           | 0.527 | 0.522   | 0.595  | 0.426            | 0.438     | 0.606   | 0.609      | 0.562 | 0.688      |

- <strong>Best overall performance</strong>: sarashina2-8x70b and sarashina2-70b (accuracy 0.725).
- <strong>Strongest category</strong>: Healthcare (accuracy up to 0.917).
- <strong>Model diversity</strong>: Results include Japanese-specialized and leading multilingual LLMs.

For up-to-date results and model comparisons, see [Swallow LLM Leaderboard on X](https://x.com/chokkanorg/status/1984170094076031297).

## Usage and Loading

### Via Hugging Face Datasets

JamC-QA can be accessed and manipulated using the [Hugging Face `datasets` library](https://huggingface.co/docs/datasets/index):

```python
import datasets
jamcqa = datasets.load_dataset('sbintuitions/JamC-QA', 'v1.0')

# Access splits
jamcqa_test = jamcqa['test']
jamcqa_dev = jamcqa['dev']

# Inspect a sample question
print(jamcqa_test[0])
```

<strong>Dataset viewer:</strong>Browse, search, and filter the dataset interactively on the [Hugging Face Data Studio](https://huggingface.co/datasets/sbintuitions/JamC-QA/viewer/).

### Evaluation with FlexEval

JamC-QA can be evaluated efficiently with the [FlexEval](https://ryokan0123.github.io/) framework (v0.13.3+). FlexEval is a unified tool for LLM evaluation, supporting diverse tasks, metrics, and methods.

Run JamC-QA evaluation with FlexEval:

```bash
flexeval_lm \
  --language_model HuggingFaceLM \
  --language_model.model "sbintuitions/sarashina2.2-0.5b" \
  --language_model.default_gen_kwargs "{ do_sample: false }" \
  --eval_setup "jamcqa" \
  --save_dir "results/jamcqa"
```

- `do_sample: false` ensures deterministic (greedy) decoding.
- Output includes exact match accuracy and other generation statistics.

For details, see the [README evaluation section](https://huggingface.co/datasets/sbintuitions/JamC-QA/blob/main/README.md#evaluation-with-flexeval) and the [FlexEval project page](https://ryokan0123.github.io/).

## Licensing and Citation

- <strong>License:</strong>Creative Commons Attribution-ShareAlike 4.0 International ([CC-BY-SA-4.0](https://creativecommons.org/licenses/by-sa/4.0/))
- <strong>Citation:</strong>```
    @misc{JamCQA2025,
      title = {JamC-QA: Japanese Multiple Choice QA Benchmark},
      author = {SB Intuitions},
      year = {2025},
      howpublished = {\url{https://huggingface.co/datasets/sbintuitions/JamC-QA}},
      note = {CC-BY-SA-4.0}
    }
    ```

## Related Benchmarks and Context

JamC-QA is part of a growing ecosystem of Japanese LLM benchmarks. Notable related datasets include:

- **[MMLU-ProX (Japanese)](https://arxiv.org/abs/2503.10497):**Multi-discipline, college-level understanding and reasoning.
- **[GPQA (Japanese)](https://arxiv.org/abs/2502.07346):**Graduate-level, science-focused question answering.
- **[JHumanEval](https://anlp.jp/proceedings/annual_meeting/2024/pdf_dir/B1-4.pdf):**Japanese HumanEval for code generation.
- **MATH-100 (Japanese):**Competition-level mathematics QA.
- **[M-IFEval-Ja](https://aclanthology.org/2025.naacl-main.123/):**Instruction following/control in Japanese.

These benchmarks collectively allow:
- Cross-benchmark and cross-lingual transfer studies.
- In-depth diagnostics of LLMs for Japanese-language applications.
- Complementing international QA datasets to ensure local relevance.

## Use Cases and Applications

JamC-QA is utilized in a range of academic, commercial, and educational settings:

- **LLM benchmarking:**Standard for quantitative comparison of Japanese and multilingual LLMs.
- **Model ablation studies:**To identify domain strengths and weaknesses.
- **Cross-lingual transfer analysis:**For evaluating transfer of factual and cultural knowledge from multilingual models.
- **Educational technology:**For building and evaluating AI tutors and digital assistants in the Japanese language.
- **Cultural adaptation:**To ensure AI deployed in Japan meets local knowledge and user expectations.

## References and Further Reading

1. Official dataset: [sbintuitions/JamC-QA on Hugging Face](https://huggingface.co/datasets/sbintuitions/JamC-QA)
2. JamC-QA README: README.md
3. Swallow LLM Leaderboard: [Swallow Leaderboard on X](https://x.com/chokkanorg/status/1984170094076031297)
4. FlexEval LLM evaluation tool: [Ryokan Ri’s FlexEval](https://ryokan0123.github.io/)
5. MMLU-ProX (Japanese): ["MMLU-ProX: Proficient-level Multi-discipline Language Understanding and Reasoning in Japanese"](https://arxiv.org/abs/2503.10497)
6. GPQA (Japanese): ["GPQA: Graduate-level Google-proof Question Answering"](https://arxiv.org/abs/2502.07346)
7. JHumanEval: ["JHumanEval: Japanese HumanEval Benchmark for Code Generation"](https://anlp.jp/proceedings/annual_meeting/2024/pdf_dir/B1-4.pdf)
8. M-IFEval-Ja: ["M-IFEval-Ja: Controllability of Instruction Following in Japanese"](https://aclanthology.org/2025.naacl-main.123/)
9. Official Hugging Face documentation: [Hugging Face Datasets](https://huggingface.co/docs/datasets/index)

For dataset download, documentation, leaderboard, and community discussion, visit [sbintuitions/JamC-QA on Hugging Face](https://huggingface.co/datasets/sbintuitions/JamC-QA).
