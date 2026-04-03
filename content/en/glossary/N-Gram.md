---
title: N-Gram
date: 2025-12-19
lastmod: 2026-04-02
translationKey: n-gram
description: A sequence of n consecutive units (words, characters, etc.) extracted from text. A foundational technique in natural language processing.
keywords:
- N-gram
- Natural language processing
- NLP
- Text analysis
- Language model
category: Data & Analytics
type: glossary
draft: false
url: /en/glossary/n-gram/
---

## What is N-Gram?

**N-gram is a set of n consecutive units (words or characters) extracted from text.** For example, from "natural language processing," unigrams (1-word) are "natural," "language," "processing"; bigrams (2-word) are "natural language," "language processing."

> **In a nutshell:** "Split sentences into small consecutive chunks and search for patterns."

**Key points:**

- **What it does:** Divide text into small units and analyze word/character connection patterns
- **Why it matters:** Capture text's semantic structure concisely for language prediction and classification
- **Who uses it:** NLP engineers, search engine companies, text analysis specialists

## Why it matters

N-gram is one of natural language processing's most basic and powerful techniques. When spell checkers suggest "type" after "typo," or smartphones propose suggestions after typing, language models using n-grams drive these features.

Text classification (spam detection) and machine translation also use n-grams. Simple yet effective with low computational requirements, it remains widely used today.

## How it works

N-gram relies on statistical probability models.

**Basic concept:** "After a word appears, which word likely follows?" is learned from historical text. If "hello" precedes "world" with 0.95 probability, the system strongly suggests "world" after "hello."

**Probability calculation:** Count each n-gram's occurrences in text corpora (large text collections). Bigram probability = "times (previous word + current word) appears" ÷ "times (previous word) appears."

**Smoothing techniques:** Unseen n-grams become probability-zero, so special adjustments (smoothing) enable handling unknown text.

Libraries like NLTK and spaCy simplify n-gram extraction and probability calculation.

## Real-world use cases

**Predictive text and autocomplete**

Email composition: typing "thank" suggests "you" via bigram models.

**Spell checking**

Typing "teh" triggers suggesting the high-frequency correct n-gram "the."

**Machine translation**

When translation candidates exist, the target language's n-gram model selects the most natural expression.

## Benefits and considerations

**Benefits:** Simple implementation, low computational cost, effectively captures basic language patterns. Often learns from limited data.

**Considerations:** Cannot capture long-form context (n increasing worsens data scarcity), lacks deep semantic understanding. Recent Transformer neural networks replace n-grams, though n-grams still serve simple tasks and small systems.

## Related terms

- **[NLP (Natural Language Processing)](NLP.md)** — Comprehensive text analysis field where n-gram is foundational
- **[Language Model](Language-Model.md)** — Models estimating word appearance probability
- **[Transformer](Transformer.md)** — Modern successor to n-gram neural network methods
- **[NLTK](NLTK.md)** — Python natural language processing library
- **[Text Classification](Text-Classification.md)** — Application using n-grams as features

## Frequently asked questions

**Q: What's the difference between bigram and trigram?**
A: Bigram examines 2-word connections; trigram examines 3-word connections. Larger n provides richer context but needs more data.

**Q: Is n-gram sufficient for spell checking?**
A: N-gram works effectively, but complex contexts benefit from advanced techniques like LLM.
