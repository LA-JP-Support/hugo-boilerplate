---
title: Hallucination
date: 2025-12-19
lastmod: 2026-04-02
translationKey: hallucination
description: AI hallucination is the phenomenon where AI systems confidently generate plausible-sounding but false information. Learn causes, impacts, and mitigation strategies.
keywords:
- hallucination
- AI hallucination
- LLM errors
- misinformation
- fact-checking
category: AI & Machine Learning
type: glossary
draft: false
url: /en/glossary/hallucination/
---

## What is Hallucination?

**AI hallucination is when AI systems confidently generate plausible-sounding but false information.** If asked "What did AI researcher Jane Smith author in her 2022 book 'Neural Networks Future'?," AI might describe a non-existent book convincingly. Critically, this isn't intentional deception—it's a statistical pattern-matching byproduct.

> **In a nutshell:** "AI unconsciously makes up plausible lies." Because AI predicts words statistically, it invents when uncertain rather than saying "I don't know."

**Key points:**

- **What causes it:** LLMs predict next words probabilistically, filling knowledge gaps with pattern-matched plausibilities
- **Why it happens:** Unsure what comes next, AI outputs "likely" continuation without factual grounding
- **How often:** Occurs in 5-20% of outputs depending on model, task, and question

## Why It Matters

Hallucination isn't a funny bug—it's a serious risk. A US lawyer cited ChatGPT-invented case law in court; he was sanctioned. Medical AI might recommend non-existent treatments; patients suffer. Financial AI trades based on fake market analysis. Hallucinations spread rapidly through networks with credible-sounding authority. Once business trust erodes, reputation damage is permanent. In accuracy-dependent fields, hallucination is mission-critical to address.

## How It Works

AI (especially transformer-based LLMs) predicts "which word comes next" probabilistically. Given "Apple's Tim Cook in 2024...", it selects statistically likely words: "announced," "revealed," or "discussed." The problem: When AI lacks training data knowledge, it fills gaps with "plausible words" anyway. It doesn't know 2024 events and hasn't learned about non-existent people, but generates compelling text anyway. Without RAG (external database retrieval), AI is "frozen in time" at training cutoff—ignorant of 2024 news.

## Real-World Examples

**Law firm case citations**

Lawyers asked ChatGPT for IP law cases, submitted invented citations in court, faced sanctions. Real databases should have been consulted.

**Medical information**

Patients ask AI about treatment options and receive non-evidence-based recommendations. Doctor verification is essential in healthcare.

**Customer support**

Customers ask about inventory; AI says "available" when stock system says "sold out." Escalated complaints result.

## Benefits and Considerations

Hallucinations can't be eliminated—they're built into probabilistic models. Multi-layered mitigation (RAG for data grounding, prompt engineering for caution instructions, human verification) reduces risk to manageable levels. The key insight: Some use cases tolerate hallucinations (creative writing), but accuracy-dependent scenarios (medicine, law, finance) require controls.

Interestingly, hallucinations have creative value. Fiction, art, and game design benefit from "unexpected combinations." The problem is accuracy-dependent fields. System design should ask: "In this use case, can hallucination be tolerated?" That distinction is critical.

## Related Terms

- **[LLM](large-language-models.md)** — Probabilistic next-word selection creates hallucination
- **[RAG](RAG.md)** — Grounding AI with external database reduces hallucinations significantly
- **[Prompt Engineering](Prompt-Engineering.md)** — Instructing "cite sources" partially mitigates hallucinations
- **[Fine-tuning](Fine-tuning.md)** — Domain-specific training improves accuracy and reduces hallucinations
- **[ChatGPT](ChatGPT.md)** — Made hallucinations famous through court case incident

## Frequently Asked Questions

**Q: Can AI hallucinations be completely eliminated?**

A: No. Research consensus: they're fundamental to probabilistic architecture. RAG, verification, and human oversight mitigate effectively.

**Q: If I ask AI to "cite sources," am I safe?**

A: Partially. AI can invent sources. For critical decisions, verify sources independently.

**Q: Do larger, better-trained models hallucinate less?**

A: Generally yes. Larger models with better training data hallucinate less frequently.
