---
title: "Glossary: PagedAttention and Advanced Memory Management for LLM Inference"
date: 2025-11-25
translationKey: "glossary-pagedattention-and-advanced-memory-management-for-llm-inference"
description: "Explore PagedAttention, a memory management algorithm that partitions the KV cache of LLMs into fixed-size blocks, reducing GPU memory waste during inference and powering vLLM."
keywords: ["PagedAttention", "LLM inference", "KV cache", "vLLM", "memory management"]
category: "LLM Inference"
type: "glossary"
draft: false
---
## PagedAttention

PagedAttention is a memory management algorithm that partitions the Key-Value (KV) cache of a large language model (LLM) into fixed-size blocks ("pages"), enabling non-contiguous allocation and dramatically reducing GPU memory waste during inference. The method was introduced by Kwon et al. in ["Efficient Memory Management for Large Language Model Serving with PagedAttention"](https://arxiv.org/abs/2309.06180) and is the foundation of the [vLLM](https://github.com/vllm-project/vllm) inference engine.

**Key Features:**
- KV cache is split into small, fixed-size blocks (pages) rather than large, contiguous buffers.
- Each sequence tracks its logical-to-physical memory mapping via a block table (page table).
- Blocks for a sequence can be scattered across memory, reducing both internal and external fragmentation.
- Memory can be shared among sequences, enabling efficient parallel sampling and advanced decoding.
- Out-of-memory (OOM) errors are prevented by on-demand allocation and prompt block reuse.

**Technical Overview and Visuals:**  
- In traditional LLM serving, each request's KV cache is pre-allocated as a single contiguous chunk, which leads to significant memory waste if sequences are short or batch sizes/sequence lengths vary.
- PagedAttention, inspired by OS virtual memory paging, allows sequences to use only as much memory as needed, with nearly optimal utilization ([vLLM blog](https://blog.vllm.ai/2023/06/20/vllm.html), [Hopsworks dictionary](https://www.hopsworks.ai/dictionary/pagedattention)).

> For animated diagrams and deeper explanations, see official [vLLM blog](https://blog.vllm.ai/2023/06/20/vllm.html).

## KV Cache

The Key-Value (KV) cache is a core component of transformer-based LLM inference. At each decoding step, the model generates key and value tensors for each token, which encode contextual relationships for the attention mechanism.

- **Purpose:** Stores precomputed attention keys and values so that the model doesn't have to recompute them for every token, drastically speeding up inference.
- **Size:** For models like LLaMA-13B, a single sequence's KV cache can reach 1.7GB; for [batch processing](/en/glossary/batch-processing/) and longer sequences, total cache size can reach 40GB ([source](https://arxiv.org/pdf/2309.06180), [Hopsworks](https://www.hopsworks.ai/dictionary/pagedattention)).
- **Challenge:** The cache is both large and dynamic—its size depends on the number of active sequences, their lengths, and batch size.
- **Impact:** Inefficient KV cache management severely limits the number of requests that can be processed in parallel, increasing costs and reducing hardware utilization.

For a deep dive into the role and optimization of KV cache in LLMs, see ["KV Cache Optimization: A Deep Dive"](https://medium.com/foundation-models-deep-dive/kv-cache-guide-part-4-of-5-system-superpowers-framework-realities-kv-cache-in-action-6fb4fb575cf8).

## Memory Fragmentation

Fragmentation refers to the inefficient use of available memory due to rigid allocation and deallocation schemes, a critical problem in LLM inference on GPUs.

### Internal Fragmentation

Occurs when pre-allocated memory blocks are larger than the actual memory needed by a sequence, leaving unused space "inside" the allocation.

- **Example:** If each sequence is allocated space for 2048 tokens but only uses 200, the rest is wasted.
- **Severity:** Traditional LLM serving systems can waste up to 80% of GPU memory due to internal fragmentation ([arXiv paper, Fig. 2](https://arxiv.org/pdf/2309.06180), [Doubleword technical guide](https://www.doubleword.ai/resources/optimizing-gpu-memory-for-llms-a-deep-dive-into-paged-attention)).

### External Fragmentation

Occurs as sequences of varying lengths start and finish. Free memory becomes scattered in small, non-contiguous chunks that are too small to be used for new allocations.

- **Result:** Even if total free memory is sufficient, it's unusable for new requests due to lack of contiguous space.

PagedAttention eliminates both types of fragmentation by allocating and releasing small blocks on-demand, similar to OS virtual memory paging ([Red Hat developer article](https://developers.redhat.com/articles/2025/07/24/how-pagedattention-resolves-memory-waste-llm-systems)).

## Virtual Memory & Paging

A classic operating system concept adapted for LLMs in PagedAttention.

- **Virtual Memory:** Separates logical memory addresses (used by processes/sequences) from physical memory locations, allowing non-contiguous storage and efficient allocation.
- **Paging:** Memory is divided into small, fixed-size pages (blocks). Logical pages are mapped to physical memory via a page table.
- **In LLM Serving:** KV cache for each sequence is divided into blocks; each block can reside anywhere in GPU memory. Sequences keep a block table mapping logical token positions to physical memory blocks.

This abstraction supports:
- On-demand allocation
- Immediate reuse of freed blocks
- Memory sharing between sequences (copy-on-write for modifications)

For technical background: ["Operating Systems: Three Easy Pieces" (Virtual Memory)](https://pages.cs.wisc.edu/~remzi/OSTEP/vm-intro.pdf).

## Block Table (Page Table)

A data structure maintained by PagedAttention to map the logical order of tokens in a sequence to the actual physical memory blocks.

- **Purpose:** Allows each sequence to reconstruct its context for attention computation, regardless of where its blocks are physically stored.
- **Functionality:** Supports fast lookup and allocation/deallocation of blocks as tokens are generated or sequences are terminated.
- **Overhead:** The lookup table introduces a small computational overhead, but the reduction in memory waste far outweighs this cost ([arXiv paper, Sec. 4.1](https://arxiv.org/pdf/2309.06180)).

## Memory Sharing

PagedAttention allows memory blocks to be shared between sequences and requests, which is especially beneficial for parallel sampling and advanced decoding.

### Parallel Sampling

- **Use Case:** Generate multiple completions from the same prompt.
- **Benefit:** The prompt's KV cache blocks are shared (not duplicated) among all outputs, reducing memory usage and enabling higher throughput ([vLLM blog, parallel sampling diagram](https://blog.vllm.ai/2023/06/20/vllm.html)).
- **Technical Mechanism:** Block tables for each sample point to the same physical blocks for shared portions of the sequence.

### Beam Search and Mixed Decoding

- **Beam Search:** Multiple beams often share the same prefix; PagedAttention enables prefix blocks to be shared among beams.
- **Mixed Decoding:** Simultaneously serves requests with greedy, sampling, and beam search strategies without redundant memory allocation.

## Copy-on-Write

A memory management technique to ensure safe modification of shared memory blocks.

- **How it works:** When a sequence needs to modify a block that is shared (multiple references), a new copy is created for that sequence only. Other sequences continue to reference the original block.
- **Benefit:** Enables memory sharing without risk of data corruption or race conditions.
- **Reference Counting:** Each block tracks how many sequences reference it, triggering a copy when a write is needed and count > 1 ([vLLM blog, animation](https://blog.vllm.ai/2023/06/20/vllm.html)).

## Attention Computation with Paging

Traditional attention kernels expect contiguous memory regions for keys and values. PagedAttention introduces a custom attention kernel that can efficiently fetch keys and values from non-contiguous blocks as specified in the block table.

- **Implementation:** During each inference step, the kernel consults the block table to gather all necessary key and value vectors from potentially scattered blocks ([arXiv Sec. 4.1](https://arxiv.org/pdf/2309.06180)).
- **Performance:** Minor computational overhead, but massive reduction in wasted memory and corresponding throughput boost.

## vLLM

[vLLM](https://github.com/vllm-project/vllm) is an open-source, high-performance LLM inference and serving engine developed at UC Berkeley. It implements PagedAttention as its core memory management algorithm.

- **Key Features:**
    - State-of-the-art throughput (up to 24x over HuggingFace Transformers)
    - Dramatically lower memory waste (from 60–80% to under 4%)
    - Support for massive batch sizes, long sequences, and advanced decoding
    - Compatible with HuggingFace models, PyTorch, and OpenAI API
    - Used in LMSYS Chatbot Arena, Databricks, Dropbox, AWS, AMD, NVIDIA, and more

For benchmarks and deployment guides, see [vLLM documentation](https://docs.vllm.ai/en/latest/getting_started/quickstart.html).

## Implementation Details and Usage

PagedAttention is accessible via [vLLM](https://github.com/vllm-project/vllm).  
**Installation:**
```bash
pip install vllm
```
**Running a model:**
```bash
python -m vllm.entrypoints.openai.api_server --model <model_name>
```
- Replace `<model_name>` with any [supported model](https://docs.vllm.ai/en/latest/models/supported_models.html).

**Key Usage Scenarios:**
- High-throughput chatbots (e.g., Chatbot Arena)
- Batch document/question serving
- Parallel sampling and beam search
- Mixed decoding workloads
- Edge and resource-constrained deployments

For serverless deployment, see [Runpod guide](https://www.runpod.io/blog/introduction-to-vllm-and-pagedattention).

**Supported Models:**  
Classic transformers (Llama, GPT-2, GPT-J), Mixture-of-Experts (Mixtral, Qwen2MoE), multimodal LLMs (LLaVA, StableLM). [Full list](https://docs.vllm.ai/en/latest/models/supported_models.html).

## Technical Benchmarks and Industry Adoption

**Quantitative Improvements:**
- Throughput: up to 24x over HuggingFace Transformers, 3.5x over TGI ([vLLM blog](https://blog.vllm.ai/2023/06/20/vllm.html))
- Memory waste: reduced from 60–80% to under 4% ([Doubleword](https://www.doubleword.ai/resources/optimizing-gpu-memory-for-llms-a-deep-dive-into-paged-attention))
- LMSYS Chatbot Arena: 2–3x more requests per second, 50% reduction in GPU usage ([Runpod blog](https://www.runpod.io/blog/introduction-to-vllm-and-pagedattention))

**Real-World Usage:**
- LMSYS Chatbot Arena, Databricks, Dropbox, AWS, AMD, NVIDIA, Roblox, and thousands of developers.
- [Open source ecosystem](https://github.com/vllm-project/vllm): >20,000 GitHub stars, active community, frequent updates.

## References and Further Reading

- [Efficient Memory Management for Large Language Model Serving with PagedAttention (arXiv paper)](https://arxiv.org/abs/2309.06180)
- [vLLM Blog: Easy, Fast, and Cheap LLM Serving with PagedAttention](https://blog.vllm.ai/2023/06/20/vllm.html)
- [Hopsworks Dictionary: PagedAttention](https://www.hopsworks.ai/dictionary/pagedattention)
- [Doubleword: Optimizing GPU Memory for LLMs – Deep Dive](https://www.doubleword.ai/resources/optimizing-gpu-memory-for-llms-a-deep-dive-into-paged-attention)
- [Runpod Blog: Introduction to vLLM and PagedAttention](https://www.runpod.io/blog/introduction-to-vllm-and-pagedattention)
- [KV Cache Optimization: Medium Deep Dive](https://medium.com/foundation-models-deep-dive/kv-cache-guide-part-4-of-5-system-superpowers-framework-realities-kv-cache-in-action-6fb4fb575cf8)
- [Red Hat Developer: How PagedAttention resolves memory waste of LLM systems](https://developers.redhat.com/articles/2025/07/24/how-pagedattention-resolves-memory-waste-llm-systems)
- [YouTube: vLLM/PagedAttention Technical Explanation](https://www.youtube.com/watch?v=5ZlavKF_98U&t=351s)
- [vLLM Documentation](https://docs.vllm.ai/en/latest/getting_started/quickstart.html)

*For the latest guides, community support, and updates, see [vLLM on GitHub](https://github.com/vllm-project/vllm) and [official docs](https://docs.vllm.ai/en/latest/).*

