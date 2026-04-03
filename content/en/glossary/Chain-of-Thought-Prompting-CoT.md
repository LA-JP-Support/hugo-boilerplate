---
title: Chain-of-Thought Prompting (CoT)
date: 2025-03-01
lastmod: 2026-04-02
description: A prompting technique that draws out complex problem-solving abilities from AI by having it reason step-by-step.
translationKey: chain-of-thought-prompting-cot
category: AI & Machine Learning
type: glossary
draft: false
url: /en/glossary/chain-of-thought-prompting-cot/
aliases:
  - /en/glossary/chain-of-thought-prompting-cot/
keywords:
  - chain of thought
  - CoT
  - prompting
  - reasoning ability
  - step-by-step
---

## What is Chain-of-Thought Prompting?

**Chain-of-Thought (CoT) is a technique that prompts AI models not to "directly output the final answer" but rather to "explain the thought process leading to that answer in stages."** Instead of asking "what is 5+3?," you ask "what is 5+3?—explain the calculation process while answering." This simple change dramatically improves the model's ability to solve complex problems.

> **In a nutshell:** It's like instructing students to "explain how you solved it, not just give the answer."

**Key points:**

- **What it does:** Prompts AI to explicitly output intermediate reasoning steps
- **Why it's needed:** Logical thinking enables models to solve more complex and accurate problems
- **Who uses it:** Anyone using AI for math, logic, and complex decision-making

## Why it matters

A notable characteristic of AI models, especially large language models (LLMs), is that they "optimize only for the final token." In other words, they're trained to minimize results rather than process. This works well for simple problems but fails easily at complex multi-stage reasoning tasks.

In 2022, a Google Research team published findings that revealed a solution to this problem. Using CoT prompting dramatically improved success rates on complex reasoning tasks without model or architecture changes. For example, math word problems improved from 40% success rate without CoT to over 60% with CoT.

Business importance is high. Existing models can be used as-is while improving performance through prompt engineering alone, gaining benefits without additional training costs. Applicability dramatically increases in domains where reasoning matters: financial analysis, medical diagnosis, legal analysis.

## How it works

CoT's basic principle is simple but profound. When AI models are in "output final answer only" mode (called "direct prompting"), they resort to guessing when facing complex problems, without reliable reasoning.

CoT changes the prompt as follows. Direct prompting asks "what is the answer?"; CoT prompting includes "thought step examples" like "to solve this, first calculate A, then calculate B, and...". These are called "few-shot examples."

Here's an example. For a math problem like "An apple costs 100 yen for 5, a tangerine costs 150 yen for 3. What is the total cost of 10 apples and 6 tangerines?", direct prompting simply asks "what's the answer?" But CoT prompting includes an example like "Q: An apple costs 60 yen for 3, a tangerine costs 100 yen for 2. What's the total cost of 2 apples and 3 tangerines? A: Step 1: Price per apple = 60÷3 = 20 yen. Step 2: Total for 2 apples = 20×2 = 40 yen. Step 3: Price per tangerine = 100÷2 = 50 yen. Step 4: Total for 3 tangerines = 50×3 = 150 yen. Step 5: Total cost = 40 + 150 = 190 yen." Showing this example to the model makes it tend to solve the original problem similarly step-by-step.

The key is "why does step-by-step thinking work?" When solving complex problems, humans automatically break them into subproblems. AI models similarly become capable of more genuine reasoning when the "final token only" constraint relaxes. Technically, models can self-correct at "intermediate tokens," reducing the likelihood that early errors affect the final answer.

## Real-world use cases

**Automated math and logic problem solving**

When AI assistants solve student math problems, CoT prompting dramatically improves accuracy. For problems like "solve 2x + 5 = 13 for x," without CoT it sometimes gives wrong answers, but with CoT—prompting "Step 1: subtract 5 from both sides... Step 2: divide both sides by 2..."—accuracy improves above 80%.

**Step-by-step medical diagnosis**

When physician-assistant AI infers diagnosis from patient symptoms, CoT prompting like "first, what common diseases combine symptoms A and B?; next, considering patient age and history, which disease has highest probability?" yields medically sound diagnoses rather than mere statistical matching.

**Legal analysis and judgment**

When legal counsel AI interprets contracts, CoT like "what's the intent of this clause? how does it interact with other clauses? what are potential risks?" enables deeper legal analysis beyond surface keyword searches.

## Benefits and considerations

CoT's greatest benefit is **implementation simplicity and massive effectiveness**. Success comes from prompt engineering alone—no model changes required. No additional training or fine-tuning needed; immediate application works.

The second benefit is **visible reasoning process**. Since models explain intermediate steps, it's easier to understand why they reached that answer. This improves trust and error detection.

However, considerations exist. First, **increased token cost**. Explaining each step uses more tokens, raising API costs.

Second, **erroneous reasoning step propagation**. Mistakes in intermediate steps may cause wrong final answers. Rather than "complete mistakes from the start," situations of "each step seems valid but contradicts overall" arise more easily.

Third, **model "reasoning style" dependence**. Different models have different reasoning styles, so CoT prompts that work with one model may not work with another.

Fourth, **potential increased "hallucination."** Generating multiple steps increases risk of confidently stating incorrect information, especially when models don't recognize uncertainty.

## Related terms

- **[LLM (Large Language Model)](LLM.md)** — CoT is most effective with LLMs.
- **[Prompt Engineering](Prompt-Engineering.md)** — CoT is an advanced prompting technique.
- **[Few-Shot Learning](Few-Shot-Learning.md)** — CoT is typically implemented with examples in a "few-shot" approach.
- **[Hallucination](Hallucination-AI.md)** — CoT helps reduce hallucinations but doesn't prevent them entirely.
- **[Self-Consistency Prompting](Self-Consistency-Prompting.md)** — Generate multiple CoT paths and select the most consistent answer.

## Frequently asked questions

**Q: Is CoT effective for all tasks?**
A: No. CoT is highly effective for reasoning-required tasks (math, logic, complex analysis) but less so for simple classification or sentiment analysis. For simple tasks, CoT just adds unnecessary computation.

**Q: Does CoT depend on model size?**
A: Yes. Larger models tend to benefit more from CoT. Smaller models may see limited effectiveness. This is because larger models have more complex reasoning capabilities.

**Q: Can CoT-generated steps be trusted?**
A: Partially. Intermediate steps provide useful insights but aren't necessarily accurate. Models may generate plausible-looking explanations while actually reasoning incorrectly. For important decisions, expert verification of CoT output is recommended.
