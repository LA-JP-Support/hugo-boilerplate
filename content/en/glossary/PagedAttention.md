---
title: PagedAttention
date: '2025-12-19'
lastmod: 2026-04-02
translationKey: pagedattention
description: PagedAttention is an algorithm that revolutionizes LLM memory efficiency. It manages KV cache in block units, accelerating GPU inference.
keywords:
- PagedAttention
- LLM inference
- memory optimization
- vLLM
- GPU efficiency
category: AI & Machine Learning
type: glossary
draft: false
url: /en/glossary/PagedAttention/
---

## What is PagedAttention?

**PagedAttention is an algorithm that divides the Key-Value (KV) cache of large language models (LLMs) into fixed-size blocks called "pages," enabling efficient memory management.** Introduced by UC Berkeley in 2023, this technology reduces GPU memory waste from massive inefficiency to less than 1/10th. By applying virtual memory paging concepts from operating systems to LLM inference, it enables larger batch sizes, longer input sequences, and more efficient resource utilization.

> **In a nutshell:** A technology that nearly eliminates memory waste during LLM inference, allowing the same GPU to handle more requests simultaneously.

**Key points:**

- **What it does:** Divides KV cache into pages and manages memory dynamically
- **Why it matters:** Inference memory waste was reducing throughput efficiency
- **Who uses it:** LLM inference engines (vLLM), Databricks, AWS, and other companies

## Why it matters

Traditional LLM inference pre-allocates memory based on input sequence length, but even when less memory is actually used, it remains underutilized. This limits the number of user requests a GPU can process, degrading responsiveness. PagedAttention fundamentally solves this problem, adopted by engines like vLLM, delivering significant cost savings to LLM chatbot and API providers.

## How it works

PagedAttention manages GPU memory similarly to how computers manage system memory. Rather than allocating large contiguous blocks, PagedAttention allocates only what's needed, in "page" units. Using a block table—a mapping structure—it maps logical memory addresses to physical locations. Even though pages are physically dispersed, they function as logically contiguous memory.

In the [Attention Mechanism](/en/glossary/Attention-Mechanism/) of Transformer models, past token information must be retained in memory. By dividing this memory into pages, completed sequences' pages are immediately available for reuse by other requests. Additionally, shared portions (prompts) don't require memory copying—only referencing is needed—further improving efficiency.

## Real-world use cases

**Chatbot Providers**
Multiple users' simultaneous requests can be processed efficiently, dramatically reducing infrastructure costs. Used by many services including LMSYS Chatbot Arena.

**Document Processing**
When batch-processing large document volumes, improved memory efficiency can increase processing speed 3x or more.

**API Services**
Improved throughput allows supporting more users with the same hardware.

## Benefits and considerations

PagedAttention's greatest benefit is memory efficiency—reducing traditional 60-80% waste to under 4%, enabling more processing with the same capacity. Improved throughput translates to reduced API latency and costs. However, block table lookup introduces minimal overhead, so single-request processing may show less obvious improvement. Also, compatible engines like vLLM are required.

## Related terms

- **[Attention Mechanism](/en/glossary/Attention-Mechanism/)** — The computational mechanism that requires KV cache
