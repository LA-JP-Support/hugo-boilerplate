---
title: Speculative Decoding
date: 2025-12-19
lastmod: 2026-04-02
translationKey: speculative-decoding
description: Speculative decoding is an optimization technique that accelerates LLM inference by having a small draft model propose multiple tokens while a large model verifies them, achieving 2-3x speedups while preserving output quality.
keywords:
- speculative decoding
- LLM inference optimization
- token generation
- draft model
- latency reduction
category: AI & Machine Learning
type: glossary
draft: false
url: /en/glossary/Speculative-Decoding/
---

## What is Speculative Decoding?

**Speculative decoding is a technique that accelerates LLM inference by having a small draft model predict multiple tokens ahead, while a large target model verifies them.** Traditional LLMs generate tokens sequentially—one at a time—making the process very slow. Speculative decoding parallelizes this sequential process, achieving 2-3x or greater speedups without sacrificing output quality.

> **In a nutshell:** Have a fast small model "guess," and a accurate large model "verify"—this parallelization speeds up the entire process.

**Key points:**

- **What it does:** A two-stage draft-and-verify process for LLM inference optimization.
- **Why it's needed:** LLM inference latency is a major bottleneck for real-time applications.
- **Who uses it:** LLM-based application developers, inference engineers.

## Why It Matters

LLMs generate tokens one at a time, so producing 100 tokens requires 100 network round-trips. For real-time applications like Google's AI Overview or chatbots, this latency directly affects user experience. Speculative decoding significantly improves response speed without degrading quality, enabling efficient service to more users.

## How It Works

The process consists of three steps.

**In the draft stage**, a small model proposes the next 3-8 tokens. This is fast but not perfectly accurate.

**In the verification stage**, the large model checks these proposals in parallel, determining which tokens are "correct" (matching the large model's own top prediction). Verification stops at the first mismatch.

**In the next round**, accepted tokens become the new context, and the draft model runs again.

An important mathematical property: the final output is statistically identical to what the large model would generate sequentially—there is no quality degradation.

## Real-World Use Cases

**Google Search AI Overview**
Delivers summaries to users quickly by using speculative decoding for significant latency reduction.

**IDE Code Completion**
Developers see next code suggestions within seconds, requiring latency optimization.

**Chatbot Response Generation**
Maintaining conversational fluency requires minimizing delays between tokens.

## Benefits and Considerations

**Benefits:** Achieves 2-3x or greater speedups, output quality remains unchanged, and server costs decrease.

**Considerations:** Both draft and target models must fit in memory. If the draft model is too imprecise, speedup is limited. High batch-size environments may see reduced benefits.

## Related Terms

- **[Large Language Models (LLMs)](large-language-models.md)** — The target models for speculative decoding.
- **[Tokenization](Tokenization.md)** — The minimal unit of LLM output.
- **[Inference Optimization](Inference-Optimization.md)** — General LLM acceleration techniques.
- **[Model Compression](Model-Compression.md)** — Technology to create smaller draft models.

## Frequently Asked Questions

**Q: How do you select the draft model?**
A: Start with a smaller version of the same architecture as the target. Ideally fine-tune it for the target if possible.

**Q: What's a good acceptance rate (what percentage of draft tokens are correct)?**
A: Typically 50-80% is ideal. Lower rates suggest the draft model needs improvement.
