---
title: Fact-Score (FActScore)
date: 2025-12-19
lastmod: 2026-04-02
translationKey: fact-score
description: FActScore is an automated evaluation metric quantifying factual accuracy in AI-generated text by decomposing content into atomic facts and verifying against authoritative sources.
keywords:
- FActScore
- Factual Accuracy
- AI-Generated Text
- LLM Evaluation
- Hallucination Detection
category: AI & Machine Learning
type: glossary
draft: false
url: /en/glossary/fact-score/
---

## What is FActScore?

**FActScore is an automated evaluation metric quantifying factual accuracy in AI-generated long-form text.** It decomposes text into minimal "atomic facts," comparing each against authoritative sources like Wikipedia, calculating what percentage of facts are supported.

> **In a nutshell:** "An automated grading machine checking each article sentence against encyclopedias."

**Key points:**

- **What it does:** Verifies whether AI-generated text contains truths
- **Why it matters:** AI confidently writes falsehoods (hallucination), requiring accuracy monitoring
- **Who uses it:** LLM developers, AI quality assurance teams, medical/legal fields requiring high accuracy

## Calculation Method

FActScore uses this formula:

**FActScore = (Supported Facts / Total Facts) × 100%**

Example: If 45 of 50 extracted facts verify against reliable sources:
FActScore = (45 / 50) × 100% = **90%**

Implementation flow:
1. Decompose text into atomic facts (via LLM or rule processing)
2. Search Wikipedia for relevant passages per fact
3. Human experts or AI judge "is this fact supported?"
4. Calculate score

## Benchmarks

Model FActScores:
- **GPT-4** — ~68% (high-performance)
- **ChatGPT** — ~58% (general purpose)
- **Alpaca 65B** — ~65% (open model)
- **Human writing** — ~88% (gold standard)

Score interpretation:
- **80%+** — Trustworthy. Suitable for medical information and high-accuracy applications
- **70–80%** — Practical, though important information needs human verification
- **Below 60%** — Poor. Using directly is risky

## Why it matters

[Hallucination](Hallucination.md) (AI generating false information) is a critical weakness. Traditional metrics (BLEU, ROUGE) don't catch subtle factual errors—FActScore does.

Example: "Einstein was born in Germany in 1879" is fully true. But "Einstein won Nobel Prizes in both physics and chemistry" is partially wrong (physics only). FActScore catches such errors.

Medical information, legal documents, journalism, and scientific communication critically need rigorous evaluation. User decisions based on false information cause serious harm.

## Real-World Use Cases

**Healthcare AI chatbot quality management**
Medical companies evaluate AI using FActScore. Below-80% scores undergo physician review, preventing patient misinformation.

**Academic publisher AI draft verification**
Academic journals verify AI-generated summaries with FActScore. Sub-50% scores skip adoption, using manual abstracts maintaining credibility.

**Multi-language LLM evaluation**
Research teams compare factual accuracy across Japanese, Chinese, Arabic and other languages objectively.

## Benefits and Considerations

**Benefits:** Automated FActScore rapidly evaluates massive AI-generated text. More efficient than manual full checking, providing objective standards. Teams identify accuracy weak points, improving models.

**Considerations:** FActScore accuracy depends heavily on reference source quality. Niche domains and recent information lack Wikipedia coverage, risking unfairly low scores. Multiple phrasings of same facts may trigger over-strict scoring.

## Related Terms

- **[Hallucination](Hallucination.md)** — AI-generated false information FActScore detects
- **[Large Language Model (LLM)](LLM.md)** — FActScore evaluation targets
- **[Fact-Checking](Fact-Checking.md)** — Human process FActScore automates
- **[AI Quality Assurance](AI-Quality-Assurance.md)** — FActScore is critical evaluation tool
- **[Natural Language Processing (NLP)](NLP.md)** — FActScore's foundational technology

## Frequently Asked Questions

**Q: Is 90%+ FActScore fully trustworthy?**
A: Nearly, but not completely. Reference sources may contain errors; complex nuances may elude detection. Important information needs human final verification.

**Q: Can FActScore evaluate Japanese text?**
A: Yes, but Japanese Wikipedia coverage is lower than English, risking unfairly low scores.

**Q: How do we improve FActScore?**
A: Training data curation, fine-tuning, and stronger fact-verification prompts help improve scores.
