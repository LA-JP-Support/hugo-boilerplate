---
title: Top-P Sampling
date: 2025-12-19
lastmod: 2026-04-02
translationKey: Top-P-Sampling
description: Also called nucleus sampling. A text generation technique that samples from candidate tokens until cumulative probability reaches P value, typically 0.9.
keywords:
- top-p sampling
- nucleus sampling
- text generation
- language model
- probability distribution
category: Knowledge & Collaboration
type: glossary
draft: false
url: /en/glossary/top-p-sampling/
---

## What is Top-P Sampling?

**Top-P sampling (nucleus sampling) is a text generation technique where the minimum token set reaches specified cumulative probability P value (typically 0.9) for sampling selection.** Unlike Top-K sampling targeting fixed token numbers, Top-P dynamically changes candidate numbers based on model confidence. When models show high confidence, it narrows candidates; when uncertainty is high, it expands them, enabling context-adaptive flexible sampling.

> **In a nutshell:** When generating text, sample from candidates where "sufficiently certain choice accumulation reaches 90%." Context automatically changes candidate numbers, yielding more natural results.

**Key points:**
- **What it does:** Dynamically select candidates based on model confidence, sample from these.
- **Why it matters:** More natural than Top-K, enables adaptive context-based text generation.
- **Who uses it:** ChatGPT, advanced chatbots, creative writing support tools, content generation platforms.

## Why it matters

Text generation quality closely relates to model confidence levels. Questions with clear answers show high model confidence, limited choices. Ambiguous situations show low confidence, needing consideration of more possibilities. Top-P sampling provides this dynamic adaptation, achieving balance where "AI narrows focus when confident, permits creativity when uncertain."

Since ChatGPT adopted Top-P sampling (default P=0.9), text generation naturalness dramatically improved. Users now receive non-repetitive responses with semantic consistency.

## How it works

Top-P sampling flow begins with models generating probability distributions across entire vocabularies. Tokens then sort descending by probability, accumulating probabilities upward until sum reaches P value (example: 0.9). Only tokens entering this "nucleus" become candidates, with probabilities renormalized for sampling.

Example: Following "yesterday was," if model predicts "sunny" (0.5), "cloudy" (0.3), "rainy" (0.1), "snowy" (0.05), "stormy" (0.05), with P=0.9, the first three (cumulative 0.9) become nucleus, excluding "snowy" and "stormy." When model confidence drops, nucleus automatically expands with more selection options.

## Real-world use cases

**ChatGPT natural conversation responses**
OpenAI setting Top-P sampling (P=0.9) as default for GPT-3.5 and GPT-4 dramatically improved conversation naturalness and quality. Users receive diverse context-appropriate responses without repetition feeling.

**Google Search Generative Experience**
Google adopted Top-P for integrated text generation in Search Generative Experience, making search result summaries more natural and readable, improving user satisfaction.

**Amazon Codewhisperer code completion**
AWS code generation tool utilizing Top-P sampling helps developers with context-adaptive multiple implementation proposals, increasing development flexibility.

**Healthcare response generation**
Medical AI chatbots adopting Top-P sampling enable responses maintaining medical accuracy while adapting to diverse patient questions.

## Benefits and considerations

Strengths include adaptability. Context automatically adjusts candidate numbers, eliminating manual hyperparameter adjustment needs, often yielding excellent results. Additionally, many cutting-edge models adopt this technique by default, with recommended values (P=0.9-0.95) becoming industry standards.

Considerations include P values that are too low making models conservative, losing creativity, while too high values increase noise degrading quality. Implementation complexity exceeds Top-K with slightly higher computational overhead. Model architecture and training dataset differences require optimal P value variations, demanding purpose-specific adjustment.

## Related terms

- **[Top-K sampling](Top-K-Sampling.md)** — Simple sampling selecting from fixed K candidates.
- **[Temperature scaling](Temperature.md)** — Adjusts probability distribution shape controlling overall randomness.
- **[Greedy decoding](Greedy-Decoding.md)** — Deterministic approach always selecting highest probability tokens.
- **[Language model](Language-Model.md)** — Neural network forming text generation foundation.
- **[Prompt engineering](Prompt-Engineering.md)** — Input design optimizing AI output.

## Frequently asked questions

**Q: Is P=0.9 always optimal?**
A: P=0.9 is common default but varies by use case. More creative results try P=0.7-0.8, more conservative accurate output tries P=0.95-0.99.

**Q: Can Top-P and Top-K be combined?**
A: Yes. Many models apply Top-P and Top-K simultaneously, constraining both candidate numbers and cumulative probability, producing more predictable high-quality output.

**Q: Should P values adjust for mobile environments?**
A: If mobile computational constraints become problematic, setting higher P values reduces computational load for candidate selection. However, quality impact requires evaluation.
