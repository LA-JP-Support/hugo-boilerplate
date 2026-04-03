---
title: Few-Shot In-Context Learning
date: 2025-03-01
lastmod: 2026-04-02
description: AI learns new tasks by providing just a few examples without retraining. Responds flexibly without model updates.
translationKey: Few-Shot-In-Context-Learning
category: AI & Machine Learning
type: glossary
draft: false
url: /en/glossary/few-shot-in-context-learning/
keywords:
  - In-Context Learning
  - Prompt Engineering
  - Zero-Shot
  - Demonstration Learning
  - Adaptability
---

## What is Few-Shot In-Context Learning?

**Few-shot in-context learning is a technique where you teach a [large language model](LLM.md) to perform new tasks or patterns by including a few examples in the prompt, without modifying the model's parameters.** Rather than retraining (fine-tuning) the model, you simply provide instructions: "Look at these examples and respond to new inputs using the same pattern." The model adapts to the new task without further training. Variations include Zero-Shot (no examples), Few-Shot (a few examples), and One-Shot (just one example), making it a crucial technique for maximizing [large language model](LLM.md) flexibility.

> **In a nutshell:** Just as humans can handle new tasks after seeing 2-3 examples, AI can quickly adapt without going back to school. You can respond on the spot.

**Key points:**

- **What it does:** Show a few input-output examples in the prompt to make the model recognize new task formats
- **Why it matters:** New tasks don't require model retraining, which is time-consuming, so few-shot learning enables rapid and flexible responses
- **Who uses it:** [Large language model](LLM.md) application developers, data analysts, chatbot operations teams

## Why it matters

The importance of few-shot in-context learning lies in dramatically accelerating the practical application of [large language models](LLM.md). In traditional machine learning, responding to new tasks required collecting large amounts of labeled data and spending weeks retraining the model. This was time-consuming, expensive, and unrealistic for many organizations.

Few-shot in-context learning dramatically solved this challenge. For example, suppose a company wants to "create a system that categorizes internal emails into three categories: urgent, normal, and reviewed." Traditionally, this required thousands of pre-classified emails. With few-shot in-context learning, simply including 5-10 examples in the prompt allows the [large language model](LLM.md) to understand the pattern and perform new email categorization.

Even more importantly, this approach handles business environment changes. When customer requirements change, simply modify the prompt examples to adapt. In today's world of rapid business requirement changes, this flexibility becomes a competitive advantage.

## How it works

Few-shot in-context learning is based on the "context understanding ability" of [transformer architecture](Transformer-Architecture.md). [Transformers](Transformer-Architecture.md) process entire input text simultaneously and understand how each part relates to others. This ability lets them automatically recognize relationships between "examples" and "new questions" in prompts.

The execution process of few-shot in-context learning proceeds as follows. First, the prompt includes a "demonstration section." This shows task description and a few "input-output examples." For sentiment analysis, it might look like:

"Classify the sentiment of the following text as 'Positive', 'Neutral', or 'Negative'.

Example 1: 'This service is wonderful!' → Positive
Example 2: 'Regarding this service' → Neutral
Example 3: 'Terrible service' → Negative

Now classify the following text: 'I'm satisfied with the new update'"

When the [large language model](LLM.md) processes this prompt, it infers from the examples "positive text contains affirming expressions" and applies the same logic to new input. The model's parameters don't change; it infers how to handle the new task based solely on provided context information.

The "shot" count in Few-Shot is typically 3-5. Sometimes one example works (One-Shot), sometimes 10+ are used (Many-Shot). Example quality and diversity affect model understanding accuracy. Good examples clearly demonstrate the task's essential pattern and include edge cases with variety. Poor examples lack diversity or contain noise.

## Real-world use cases

**Customer Support Intent Classification**

When support teams auto-classify customer inquiries, traditionally thousands of past inquiries needed labeled training data. With few-shot in-context learning, when new inquiry categories are added, simply add a few examples to the prompt and the system recognizes the new category. For instance, if a "refund claim" category is added, showing 5 real examples lets the model understand its characteristics and auto-classify new refund claims.

**Multilingual Adaptation**

Rather than training separate models per language, few-shot in-context learning shows a few translation examples per language, letting the model understand language correspondences and handle new language translation.

**Domain-Specific Terminology**

Medical fields have industry-specific terminology. When niche specialized terms appear that general medical models can't handle, few-shot in-context learning shows "this term means ○○ in this context" with a few examples, and the model acquires that domain knowledge.

## Benefits and considerations

Few-shot in-context learning's greatest benefits are speed and flexibility. Handling new tasks needs no model retraining step, only prompt design. Continuous model updates aren't necessary, simplifying operations. Small datasets (just a few examples) suffice, lowering labeling costs and reducing privacy risks (managing large training datasets).

Considerations exist too. Few-shot in-context learning heavily depends on prompt quality. Poor example selection causes the model to infer wrong patterns, significantly lowering accuracy. When tasks are too complex or patterns ambiguous, Few-Shot is insufficient and fine-tuning becomes necessary. Additionally, token limits prevent very long prompts.

## Related terms

- **[Large Language Models](LLM.md)** — The foundation enabling few-shot in-context learning
- **[Prompt Engineering](Prompt-Engineering.md)** — The technique for maximizing few-shot in-context learning effectiveness
- **[Chain-of-Thought Prompting](Chain-of-Thought-Prompting.md)** — Prompting technique encouraging step-by-step thinking, used alongside few-shot in-context learning
- **[Fine-Tuning](Fine-Tuning.md)** — Modifying model parameters to train, an alternative to few-shot in-context learning

## Frequently asked questions

**Q: How do you choose between Few-Shot and Zero-Shot?**
A: Simple, clear tasks may work with Zero-Shot (no examples). Complex or niche pattern tasks benefit more from Few-Shot with a few examples to improve accuracy.

**Q: What's the optimal number of examples?**
A: Generally 3-5 suffice, but task complexity matters. Simple tasks: 1-2 examples; complex: 8-10. Experimental adjustment is recommended.

**Q: Is few-shot in-context learning always inferior to fine-tuning?**
A: No. For small-scale tasks, privacy-critical cases, and quick response needs, few-shot in-context learning excels. Fine-tuning suits large-scale, stable response requirements.
