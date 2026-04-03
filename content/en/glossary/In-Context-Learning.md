---
title: In-Context Learning
date: 2025-12-19
translationKey: In-Context-Learning
description: The capability of large language models to learn from sample examples provided within prompts and execute new tasks without additional training or fine-tuning.
keywords:
- In-Context Learning
- Prompt Engineering
- Large Language Models
- LLM
- Few-Shot Learning
category: AI & Machine Learning
type: glossary
lastmod: 2026-04-02
draft: false
url: /en/glossary/in-context-learning/
---

## What is In-Context Learning?

**In-context learning (ICL) is the ability of large language models ([LLM](LLM.md)) to learn from sample examples provided within prompts and perform new tasks without additional training or [fine-tuning](Fine-Tuning.md).** Without further learning, it can handle new formats and instructions simply by examples. For instance, "if you show three translation examples, the model translates new Japanese to English in that format."

> **In a nutshell:** "Like when a teacher writes 'English translation examples' on a blackboard and students can then translate new sentences in that format."

**Key points:**

- **What it does:** By including examples in prompts, LLMs understand "this task works this way" and respond to new questions accordingly.
- **Why it's needed:** No need to train new models for every purpose; prompt engineering alone handles it, saving significant time and cost.
- **Who uses it:** [LLM](LLM.md)-using developers, [prompt engineers](Prompt-Engineering.md), and enterprise AI implementation specialists.

## Why it matters

Traditionally, handling new tasks (example: category classification, paragraph summarization style changes) required retraining models, demanding enormous time and data. In-context learning only requires including samples in prompts, responding immediately without waiting for training. Additionally, different tasks can be handled by the same model, eliminating multiple model management. Consequently, LLM implementation costs drop substantially, explaining the rapid adoption surge.

## How it works

In-context learning typically functions through three steps. **Prompt design** prepares task description and multiple samples (input-output pairs). For example, sentiment analysis includes "two positive review examples and two negative review examples." **Prompt submission** sends the designed prompt plus new input to the LLM. **Response generation** applies patterns learned from samples, generating appropriate output for new input. Process effectiveness heavily depends on sample count and quality. Typically, 2-5 quality samples produce effective results.

## Real-world use cases

**Customer Review Auto-Classification**
Online stores wanting to classify reviews as positive/negative. Simply include three examples per category in the prompt, and the [LLM](LLM.md) auto-classifies. No new training required.

**Industry-Specific Document Translation**
Translation requiring different industry-specific terminology. Prompt-included industry translation examples enable the same model to handle multiple industries. Eliminates custom model training costs.

**Customer Support Inquiry Classification**
Customer inquiries auto-classified into "billing," "technical support," "returns," etc. Showing typical questions per category enables auto-classification of new inquiries.

## Benefits and considerations

**Benefits** include rapid low-cost new task handling and elimination of multiple custom models. The flexibility to handle different tasks by only changing prompts is another major advantage.

**Considerations** include difficulty handling complex, specialized tasks where [fine-tuning](Fine-Tuning.md) is more effective. Additionally, prompt quality greatly affects task success, making sample selection critical. Furthermore, smaller language models show reduced effectiveness.

## Related terms

- **[Prompt Engineering](Prompt-Engineering.md)** – The technique for effectively using in-context learning.
- **[LLM](LLM.md)** – In-context learning is a capability of large language models.
- **[Fine-Tuning](Fine-Tuning.md)** – For more advanced tasks, combining with fine-tuning is also possible.
- **[Few-Shot Learning](Few-Shot-Learning.md)** – A similar concept to in-context learning.
- **[RAG](RAG.md)** – When using external knowledge, in-context learning is combined with RAG.

## Frequently asked questions

**Q: How many samples are sufficient?**
A: Typically 2-5 produce effective results. Depending on task complexity and model size, over 10 samples sometimes reduce effectiveness.

**Q: Which samples are most effective?**
A: Samples close to actual data, covering task pattern diversity are effective. For text classification, mix long text, short text, and ambiguous expression examples.

**Q: Are there tasks in-context learning cannot handle?**
A: Complex math problems, tasks requiring deep reasoning, and translation to new languages show difficulty handling, requiring specialized expertise.
