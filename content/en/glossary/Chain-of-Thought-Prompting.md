---
title: Chain-of-Thought Prompting
date: 2025-12-19
lastmod: 2026-04-02
translationKey: Chain-of-Thought-Prompting
description: A technique where language models solve complex problems step-by-step, making their reasoning process explicit. Dramatically improves accuracy in math, logic, and analytical tasks.
keywords:
- chain-of-thought prompting
- AI reasoning
- prompt engineering
- step-by-step thinking
- LLM optimization
category: AI & Machine Learning
type: glossary
draft: false
url: /en/glossary/chain-of-thought-prompting/
aliases:
- /en/glossary/chain-of-thought-prompting/
---

## What is Chain-of-Thought Prompting?

**Chain-of-Thought Prompting is a technique that improves reasoning accuracy by making language models solve problems step-by-step.** It explicitly reveals the "chain of thought" to the final answer, reducing hallucination (false outputs) and enabling accurate handling of complex logic. Instead of asking "what's the answer?" you ask "think about this first, then that..." and guide the model through step-by-step reasoning.

> **In a nutshell:** It's like instructing AI to "work through the entire solution process with all intermediate steps" instead of "just give me the answer."

**Key points:**

- **What it does:** Prompts AI to verbalize its thought process and encourage step-by-step reasoning
- **Why it's needed:** Complex problems see 40-50% accuracy improvement; error causes become clearer
- **Who uses it:** Data scientists, AI developers, engineers, educators

## Why it matters

Traditional prompting makes models jump directly to final answers, causing them to fail on multi-stage logic problems. Medical diagnosis, legal analysis, and complex calculations often collapse when wrong assumptions undermine the final answer. Chain-of-Thought makes each step "visible," allowing both AI and users to identify error locations.

## How it works

The system operates in four main steps. **Stage 1 is exemplification:** show "here's how problem A is solved" with 1-2 examples. **Stage 2 is learning the reasoning process:** the model internalizes the example's logical patterns. **Stage 3 is presenting the user's problem:** a new problem is provided. **Stage 4 is step-by-step answer generation:** each step is shown while reaching the answer.

For example in math: instead of "what is 12×3+8?" ask "calculate 12×3, then add 8 to that result." Or the zero-shot version using simple triggers like "think slowly" or "first... then..." works too (see Zero-Shot-Chain-of-Thought for reference).

## Real-world use cases

**Medical diagnosis support**
Instead of "what disease might cause these symptoms?" ask "evaluate based on patient age, symptoms, then test results in order," reducing misdiagnosis.

**Legal contract analysis**
To detect contradictions in complex contracts, instead of judging everything at once, direct "first verify this clause, next check its relationship to that clause," making contradictions clear.

**Programming problem-solving**
For algorithm selection or optimization, by having "which data structure should be chosen and why?" explained step-by-step, more appropriate and explainable solutions emerge.

## Benefits and considerations

**Benefits** include dramatically improved reasoning accuracy (40-50% improvement), clearer error identification, expanded capability on complex problems, and increased user trust. Conversely, **considerations** include higher token requirements for execution, increased response time, and unnecessary verbosity for simple questions. Additionally, if the model itself isn't logical, detailed explanation may expose bigger errors.

## Related terms

- **[Zero-Shot-Chain-of-Thought](Zero-Shot-Chain-of-Thought.md)** — The variant that achieves similar effects with just "think" without showing examples
- **[Prompt-Engineering](Prompt-Engineering.md)** — The broader set of practical prompt design techniques
- **[LLM](LLM.md)** — The foundational concept of large language models
- **[Few-Shot-Learning](Few-Shot-Learning.md)** — The basic technique of learning from a few examples
- **[Tree-of-Thought](Tree-of-Thought.md)** — The advanced variant that simultaneously explores multiple reasoning paths

## Frequently asked questions

**Q: Should I always use it for simple questions?**
A: No. For simple factual questions like "what's Tokyo's population?" shorter responses are more efficient. It's effective for questions requiring judgment or analysis.

**Q: Does it work with every AI model?**
A: GPT-4, Claude, and Gemini and other large models show higher effectiveness. Smaller models may not function as expected.

**Q: Does it cost more?**
A: Token usage increases, so API billing rises. However, reduced correction and re-query costs may lower overall expenses.
