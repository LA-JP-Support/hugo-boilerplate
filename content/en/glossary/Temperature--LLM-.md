---
title: Temperature (LLM)
date: 2025-12-19
lastmod: 2026-04-02
translationKey: temperature-llm
description: A setting that adjusts how creative or predictable an AI's responses are by controlling randomness in text generation—lower values produce focused, consistent answers, while higher values create more diverse, creative outputs.
keywords:
- Temperature (LLM)
- Large Language Model
- Text Generation
- Randomness Control
- Output Diversity
category: AI & Machine Learning
type: glossary
draft: false
url: /en/glossary/temperature--llm-/
---

## What is Temperature (LLM)?

**Temperature is a parameter that controls randomness in text generation by an LLM (Large Language Model). Adjusting its value progressively changes output from "creative" to "precise."** A lower temperature (like 0.1) produces consistent, predictable text ideal for technical documentation. A higher temperature (like 1.5) produces diverse, unpredictable outputs with novel ideas, suitable for creative writing.

> **In a nutshell:** A "dial" controlling how much diversity the LLM includes—turning it up makes responses more creative and unpredictable.

### Key points:

- **Low (0.1-0.3):** Consistency-focused, factual and predictable output (for technical documents)
- **Medium (0.7-0.9):** Balanced, conversational with good diversity (for chatbots)
- **High (1.2-1.5):** Creativity-focused, unpredictable with many novel ideas (for creative writing)
- **Computation cost:** Essentially zero. No model retraining needed; applies instantly

## Why it matters

Temperature directly affects output quality for different use cases. Using temperature 0.1 for creative writing produces boring, repetitive text. Using temperature 1.5 for customer support produces inconsistent, inappropriate responses. Choosing the right temperature makes the difference between "feels human and helpful" versus "clearly robotic or nonsensical."

Different applications need different temperature settings. Medical diagnosis AI needs low temperature (accuracy first). Creative brainstorming assistants need higher temperature (novelty important). Chatbots typically use medium temperature for natural conversation with some variation.

## How it works

Temperature operates on probability distributions. First, the model calculates "scores" (logits) representing likelihood of each next word. Without temperature control, it would always pick the highest-scoring word, creating repetitive output. Temperature adjusts these scores before converting to probabilities.

**Low temperature example:** If word A scores 8.5 and word B scores 6.2, temperature 0.3 amplifies the difference, making A chosen 99% of the time.

**High temperature example:** The same scores become much closer in probability, making both A and B chosen roughly equally often, even if A scores higher.

The formula: probability_distribution = softmax(scores / temperature)

At temperature 0, the model deterministically picks the highest-scoring token every time. At very high temperatures, all words become nearly equally likely, producing random nonsense.

## Real-world use cases

**Customer Support Chatbot** - Use temperature 0.7-0.8. Low enough to provide consistent, helpful answers. High enough for natural variation ("Thanks!" vs. "You're welcome!" vs. "Happy to help!").

**Code Generation Assistant** - Use temperature 0.3-0.5. Must generate syntactically correct code. Too much creativity creates non-functional code.

**Brainstorming Partner** - Use temperature 1.0-1.3. Encourages novel ideas and unexpected connections that spark creativity.

**Medical Diagnosis AI** - Use temperature 0.1-0.2. Accuracy and consistency paramount. Cannot afford creative hallucinations.

## Benefits and considerations

Temperature is simple to adjust and has zero computational cost. No retraining required—just change the parameter. However, "optimal" temperature depends on use case, and no single value works for everything. Finding the right temperature requires experimentation. Additionally, very high temperature can cause LLMs to generate incorrect information or offensive content.

## Related terms

- **[Large Language Model (LLM)](Large-Language-Model.md)** — The AI system being controlled
- **[Prompt Engineering](Prompt-Engineering.md)** — Designing inputs to get desired outputs
- **[Sampling Methods](Sampling-Methods.md)** — Techniques for selecting next tokens

## Frequently asked questions

**Q: What's the difference between temperature and top-p sampling?**
A: Temperature controls the shape of the probability distribution. Top-p (nucleus sampling) limits choices to the most probable tokens. They're complementary techniques often used together.

**Q: Can temperature be zero?**
A: Yes, temperature 0 makes the model deterministic—always picking the highest-scoring token. Useful for reproducible outputs but very repetitive.

**Q: What if temperature is above 2.0?**
A: The output becomes increasingly random and nonsensical. Most practical uses stay between 0.1 and 1.5.

**Q: How do I know what temperature to use?**
A: Start with 0.7 (balanced default). If output is too repetitive, increase it. If output is too random, decrease it. Experiment based on your use case.

**Q: Does temperature affect response latency?**
A: No. It only changes probability calculations, not computational complexity.
