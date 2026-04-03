---
title: "Entity Linking"
date: 2025-12-19
lastmod: 2026-04-02
description: "A technology that connects extracted entities in text to unique entries in a knowledge base, resolving ambiguity about what each entity actually refers to."
translationKey: "entity-linking"
category: "AI & Machine Learning"
type: glossary
draft: false
url: /en/glossary/Entity-Linking/
---

## What is Entity Linking?

**Entity linking is a technology that identifies what extracted expressions like "Apple" or "Paris" in text actually refer to and connects them to entries in a knowledge base (such as Wikipedia or Wikidata).** Is "Apple" a company, a fruit, or a person's name? Context determines the correct target.

> **In a nutshell:** It's automating the process of looking up words in a dictionary to determine what a word means.

**Key points:**

- **What it does:** Connects extracted entities to standardized knowledge base entries
- **Why it's needed:** Creates structured data from text, enabling semantic search and recommendations
- **Who uses it:** Search engines, recommendation systems, knowledge management systems

## Why it matters

When humans read the word "Apple," we intuitively determine "which Apple" from context. Machines find this difficult. Entity linking allows text to be processed not as mere strings but as meaningful data.

This enables semantic search. Searching for "the company founded by Steve Jobs" correctly returns Apple Inc. articles. Additionally, the same entity can be correctly identified across multiple languages.

## How it works

Entity linking operates in four stages.

**Stage 1: Candidate generation** — For the text "Apple," related candidates are gathered from the knowledge base (Apple Inc., Apple University, Apple as a personal name, etc.).

**Stage 2: Context analysis** — From context like "manufactures iPhones," "Apple Inc." is determined to be most relevant.

**Stage 3: Disambiguation** — When multiple candidates exist, language models or vector search select the most confident candidate.

**Stage 4: Link confirmation** — The selected entity is connected to a Wikidata ID (e.g., Q312), linking it to the knowledge base.

## Real-world use cases

**Medical search optimization** — "Dr. Smith" in a doctor profile page is correctly linked to the specific doctor's profile, helping patients find accurate information.

**E-commerce product search** — When searching "Apple iPad," the correct Apple Inc. products display rather than images of apples.

**Multilingual news integration** — Japanese "田中太郎" and English "Taro Tanaka" are recognized as the same person, displaying unified articles.

## Benefits and considerations

**Improved accuracy is a main benefit.** Search and recommendation result relevance improves significantly.

**Computational cost is challenging.** Searching large knowledge bases (Wikidata has millions of entities) takes time.

**Weakness with new entities** — Recently founded startups and other unlisted entities in the knowledge base cannot be recognized.

## Related terms

- **[Entity Extraction](Entity-Extraction.md)** — Extracts entities from text before linking occurs
- **[Semantic Search](Semantic-Search.md)** — Advanced search made possible through entity linking
- **[Knowledge Graph](Knowledge-Graph.md)** — Knowledge representation constructed through entity linking
- **[Natural Language Processing](NLP.md)** — Entity linking is an important NLP task
- **[Vector Embeddings](Vector-Embeddings.md)** — Technology used in disambiguation

## Frequently asked questions

**Q: How are newly created person names or organizations handled?**

A: If not registered in the knowledge base, they cannot be linked. The knowledge base must be periodically updated or new entities added.

**Q: Does it work 100% accurately?**

A: No. Complex contexts produce incorrect links, and sometimes multiple candidates have equal confidence.

**Q: Does it work across multiple languages?**

A: Yes. By using language-independent knowledge bases (like Wikidata), multilingual support is possible.
