---
title: Named Entity Recognition (NER)
date: 2025-12-19
lastmod: 2026-04-02
translationKey: named-entity-recognition-ner
description: A technology that automatically recognizes and classifies important information such as people's names, organization names, and place names within text. It converts unstructured data into structured information.
keywords:
- Named Entity Recognition
- NER
- Natural Language Processing
- Entity Extraction
- Text Analysis
category: Data & Analytics
type: glossary
draft: false
url: /en/glossary/Named-Entity-Recognition--NER-/
---

## What is Named Entity Recognition (NER)?

**NER is a technology that automatically recognizes and classifies important information from text, such as names of people, organizations, and places.** From the sentence "The Bank of Japan issued a statement about the dollar exchange rate," it automatically extracts "Bank of Japan" as an organization and "dollar" as a currency. This transforms text into structured data, making search and analysis simpler.

> **In a nutshell:** "Automatically finding 'important names' in sentences and determining which type (person? company? location?) they belong to."

**Key points:**

- **What it does:** Extracts named entities from text and classifies them into categories
- **Why it's needed:** So machines can understand important information from massive amounts of text
- **Who uses it:** Search engine companies, NLP technologists, content analysis departments

## Why it Matters

Most text on the internet is unstructured data. For search engines to understand text and return accurate results, they must extract important information (names, places, organizations) from it.

There are also many practical applications: automatically extracting important people and companies from news articles to build knowledge bases, automatically extracting dates and amounts from contracts, or extracting disease names and treatment methods from medical text. When combined with LLMs, even more sophisticated analysis becomes possible.

## How It Works

NER operates through multiple steps.

**Text preprocessing** First, text is divided into words (tokens) and sentences are segmented.

**Feature extraction** Information is extracted from surrounding context for each word to determine whether it's a named entity. For example, a word following "Mr." is likely a person's name.

**Boundary detection and classification** The boundaries of multi-word named entities (such as "University of Tokyo," which is three words) are identified, and the entire entity is classified into a category. Classification uses traditional machine learning models (like CRF) or deep learning (like Transformer).

The latest NER systems achieve high accuracy by fine-tuning pre-trained models like BERT.

## Real-World Use Cases

**Improving search engine results**
When a user searches for "Apple," the system automatically determines whether it refers to the company or the fruit, displaying appropriate search results.

**Automatic classification of news articles**
Extracting people, organizations, and geopolitical entities from news, then automatically categorizing and recommending related articles.

**Medical record processing**
Automatically extracting disease names, medications, and surgical procedures from patient medical records, storing them in a structured database, and enabling statistical analysis.

## Benefits and Considerations

**Benefits** include automatically converting unstructured text to structured format, achieving greater speed and accuracy than manual extraction, and scalability across large datasets.

**Considerations** include dependence on context ("Washington" could be a person's name or a place name depending on context), requiring thoughtful approaches for multilingual support, and requiring special training for domain-specific terminology. Additionally, it struggles with expressions not present in training data, such as new company names or slang.

## Related Terms

- **[NLP (Natural Language Processing)](NLP.md)** — NER is one part of this. The comprehensive field of text analysis
- **[Information Extraction](Information-Extraction.md)** — Text information retrieval technology that includes NER
- **[BERT](BERT.md)** — A pre-trained language model used for Named Entity Recognition
- **[Transformer](Transformer.md)** — The underlying technology for modern NER systems
- **[Knowledge Graph](Knowledge-Graph.md)** — A network constructed from entities extracted by NER

## Frequently Asked Questions

**Q: Does NER work perfectly?**
A: No. Errors occur especially with ambiguous expressions and new proper nouns. Human verification is often necessary.

**Q: How accurate is NER for Japanese?**
A: Japanese morphology is complex, making accuracy slightly lower than English. Using Japanese-specific models (like Japanese BERT) is recommended.
