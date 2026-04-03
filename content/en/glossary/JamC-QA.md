---
title: JamC-QA
lastmod: 2026-04-02
date: '2025-12-19'
translationKey: jamc-qa
description: JamC-QA is a benchmark dataset for evaluating large language models in Japanese. Tests knowledge specific to Japan's culture and understanding.
keywords:
- JamC-QA
- Japanese LLM
- benchmark
- AI evaluation
- language models
category: AI & Machine Learning
type: glossary
draft: false
url: /en/glossary/jamc-qa/
---

## What is JamC-QA?

**JamC-QA is a benchmark test that measures how well Japanese [Large Language Models](LLM.md) understand Japan's culture, history, and geography.** It stands for "Japanese Multiple Choice Question Answering," comprising over 2,300 multiple-choice questions (four-option questions).

This test covers eight domains: Japanese culture, social customs, regional knowledge, geography, history, politics, law, and medicine. It's designed to fairly evaluate the capabilities of Japanese language LLMs.

> **In a nutshell:** A test sheet that grades Japanese AI on "how much it knows about Japan."

**Key points:**

- **What it does:** Evaluates the knowledge of Japanese language LLMs with a test dataset
- **Why it's needed:** Standard tests don't cover Japan-specific knowledge
- **Target audience:** AI companies, language model researchers, companies deploying AI in Japan

## Why it matters

Historically, [Large Language Models](LLM.md) like [ChatGPT](ChatGPT.md) were evaluated primarily using "MMLU," an English-based test. However, this test contains almost no Japan-specific knowledge.

Companies creating AI services for Japanese markets need to know precisely "This LLM is excellent in English, but what about Japanese culture?" JamC-QA makes this possible. Simultaneously, researchers aiming to improve [language models](Language-Model.md) use JamC-QA results as a crucial indicator for identifying improvement areas.

## Test structure

JamC-QA provides several hundred questions each in these eight domains:

**Culture (640 questions)**
Knowledge about movies, literature, music, art. Examples: "What is the dialogue from this movie?"

**Customs (200 questions)**
Japanese social customs, etiquette, festivals. Examples: "What is the correct explanation of Tanabata?"

**Regionality (397 questions)**
Dialects, region-specific customs, regional character. Examples: "Which agricultural product is Hokkaido's #1 producer?"

**Geography (272 questions)**
Natural geography like mountains and rivers. Examples: "What is Japan's highest mountain?" from basics to advanced.

**History (343 questions)**
Japanese historical events, figures, periods. Requires historical accuracy.

**Politics (110 questions)**
Political systems, policies, government roles. Tests understanding of Japan's unique political systems.

**Law (299 questions)**
Japanese legal systems and laws. Examples: "From what age is someone legally an adult under civil law?"—practical knowledge.

**Medicine (48 questions)**
Japan's medical system and terminology. Medical accuracy is important.

## Evaluation method

Tests use "four-option questions" with only one correct answer. Scoring is based on whether you select the correct answer exactly—there's no partial credit for "almost correct."

When companies develop Japanese [chatbots](Chatbot.md), generally 70-75% correct rates indicate a certain level of knowledge.

## Leaderboard results and examples

The highest-performing model "sarashina2-70b" (as of 2024) achieved approximately 72% accuracy, showing "jagged intelligence" with medicine domain (92%) being strong while regional knowledge (67%) remains weak.

This gives [LLM](LLM.md) developers the insight that "medical terminology is abundant in training data, but region-specific knowledge is insufficient"—a hint for improvement.

## Real-world usage

**Model selection**
When companies deploy Japanese AI chatbots, they can compare multiple models using JamC-QA and select the optimal one.

**Research and development**
Language model researchers identify weak domains with JamC-QA and improve them through additional learning or [fine-tuning](Fine-Tuning.md).

**Trustworthiness evaluation**
Users learn "This AI is strong in history but weak in regional knowledge" and can use it appropriately.

## Related terms

- **[Large Language Model (LLM)](LLM.md)** — The AI being evaluated by JamC-QA
- **[Language Model](Language-Model.md)** — AI specialized in text processing
- **[Benchmark](Benchmark.md)** — Standard tests measuring AI performance
- **[Fine-Tuning](Fine-Tuning.md)** — Optimization to specialize models in specific domains
- **[Jagged Intelligence](Jagged-Intelligence.md)** — Uneven model capability across domains

## Frequently asked questions

**Q: Are all Japanese models evaluated with JamC-QA?**
A: No. Many major models are evaluated, but smaller or proprietary models may not be tested.

**Q: Can I view the test questions beforehand?**
A: Yes. JamC-QA is public on [Hugging Face](Hugging-Face.md), and developers can view it beforehand.

**Q: Does high JamC-QA score mean perfect Japanese?**
A: No. JamC-QA measures knowledge quantity, not natural conversation ability or nuanced understanding.
