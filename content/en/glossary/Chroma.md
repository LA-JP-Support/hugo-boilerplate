---
title: Chroma
date: '2025-12-19'
lastmod: 2026-04-02
translationKey: chroma
description: An open-source vector database for AI-native applications. Learn core concepts, architecture, use cases like RAG and semantic search, and comparisons with alternative solutions.
keywords:
- Chroma
- vector database
- embedding
- AI-native applications
- semantic search
category: "AI & Machine Learning"
type: glossary
draft: false
url: "/en/glossary/chroma/"
---

## What is Chroma?

**Chroma is an open-source vector database that converts text and image data into numbers (embeddings) and stores them, enabling AI applications to instantly search for semantically similar data.** Large language models (LLMs) use Chroma with RAG (Retrieval Augmented Generation) technology to extract accurate answers. Developers can integrate Chroma with just a few lines of code and implement semantic search functionality without complex setup.

> **In a nutshell:** A "brain" that helps AI find "similar information" instantly, working like a librarian searching for books by meaning rather than exact titles.

**Key points:**

- **What it does:** Stores data as numbers and performs fast searches for semantically similar data
- **Why it's needed:** LLMs need external knowledge bases to provide accurate answers; Chroma efficiently retrieves relevant information
- **Who uses it:** AI developers, chatbot development companies, search system builders

## Why it matters

Traditional text search (keyword search) has a fundamental problem: if an exact match isn't found, the search fails. Chroma understands and searches data by meaning, reducing such search misses. As AI technology advances and large language model usage expands, LLMs have outdated or limited knowledge. Chroma allows organizations to provide their latest documents, customer data, and expert knowledge as "reference materials" to LLMs, enabling more accurate and reliable answers. This is the core of retrieval augmented generation (RAG).

## How it works

Chroma's basic flow is as follows. First, an organization converts its documents (manuals, FAQs, blog posts, etc.) into numerical vectors called embeddings and stores them. When a user asks a question, that question is converted to an embedding using the same method and compared with stored document embeddings. Chroma quickly finds documents with the "closest" embeddings (semantically similar documents) and provides them to the LLM. The LLM can then generate more accurate answers based on these reference materials. This reduces LLM "hallucination" (answers without basis).

## Core concepts

### Embedding
Embeddings are dense vectors that encode the semantic meaning of data. Text, images, or audio clips can be converted into vectors of hundreds or thousands of numbers. Data with similar meaning has similar embeddings even if the original data differs significantly.

Chroma supports embeddings generated with popular models including OpenAI text-embedding models, HuggingFace models, Cohere, OpenCLIP, and custom embeddings.

### Collections
Chroma collections are logical groups of documents, embeddings, and associated metadata. Each collection has its own configuration including embedding function, storage location, and optional custom settings for performance and filtering.

### Metadata and hybrid search
In Chroma, arbitrary key-value metadata can be associated with each document or vector. This enables hybrid search: filtering results by metadata and ranking by vector similarity.

## How Chroma works

### Vector indexing and similarity search
Chroma uses Hierarchical Navigable Small World (HNSW) graphs for fast approximate nearest neighbor search. HNSW is a state-of-the-art algorithm for high-dimensional vector similarity search, balancing recall and speed while scaling to millions of vectors.

### Document and metadata storage
Each Chroma entry contains raw document/content, vector embeddings, and associated metadata. This enables hybrid queries and complete semantic search. Chroma can store data in-memory, on disk, or in Chroma Cloud.

### API and client libraries
Chroma provides a minimal and intuitive API with four main operations: Add, Update, Delete, and Query. Client libraries exist for Python and JavaScript/TypeScript.

## Related terms

- **[Large Language Model (LLM)](LLM.md)** — Combined with Chroma for text generation; RAG significantly improves accuracy
- **[Retrieval Augmented Generation (RAG)](RAG.md)** — Retrieves information from external knowledge bases to increase LLM accuracy
- **[Vector Database](Vector-Database.md)** — Efficiently stores and searches numerical vectors
- **[Embedding](Embedding.md)** — Converting text and images to numerical vectors
- **[Semantic Search](Semantic-Search.md)** — Searching by semantic relevance rather than exact keyword match

## Key use cases

**Semantic search** - Find information by meaning, not just keywords
**Recommendation systems** - Find similar items through embedding similarity
**Retrieval augmented generation (RAG)** - Improve LLM accuracy with external knowledge
**Multimodal search** - Search across text, images, and other media
**Chatbots and AI applications** - Provide persistent semantic memory
**Data science and analysis** - Explore high-dimensional data and detect anomalies

## References

- [Chroma GitHub repository](https://github.com/chroma-core/chroma)
- [Chroma documentation](https://docs.trychroma.com/)
- [LangChain Chroma integration](https://docs.langchain.com/oss/python/integrations/providers/chroma)
