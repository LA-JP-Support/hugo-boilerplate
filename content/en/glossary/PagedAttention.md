---
title: "PagedAttention"
date: 2025-12-18
lastmod: 2025-12-18
translationKey: "pagedattention"
description: "Explore PagedAttention, a memory management algorithm that partitions the KV cache of LLMs into fixed-size blocks, reducing GPU memory waste during inference and powering vLLM."
keywords: ["PagedAttention", "LLM inference", "KV cache", "vLLM", "memory management"]
category: "LLM Inference"
type: "glossary"
draft: false
---

## What Is PagedAttention?

PagedAttention is a memory management algorithm that partitions the Key-Value (KV) cache of large language models (LLMs) into fixed-size blocks ("pages"), enabling non-contiguous memory allocation and dramatically reducing GPU memory waste during inference. Introduced by Kwon et al. in their 2023 paper, PagedAttention serves as the foundation of vLLM, a high-performance LLM inference engine developed at UC Berkeley.

Traditional LLM serving systems pre-allocate KV cache as single contiguous memory chunks, leading to significant waste when sequences vary in length or when batch sizes fluctuate. PagedAttention, inspired by operating system virtual memory paging, allows sequences to use only the memory they need, achieving near-optimal utilization. This architectural innovation transforms how LLMs handle memory during inference, enabling higher throughput, larger batch sizes, and more efficient hardware usage.

The algorithm's impact extends beyond academic interest—major production systems including LMSYS Chatbot Arena, Databricks, Dropbox, AWS, AMD, and NVIDIA have adopted vLLM and PagedAttention for their LLM inference workloads. The open-source vLLM project has garnered over 20,000 GitHub stars and continues to drive innovation in efficient LLM serving.

## Core Concepts

### KV Cache Fundamentals

The Key-Value cache is a critical component of transformer-based LLM inference. During each decoding step, the model generates key and value tensors for each token, encoding contextual relationships for the attention mechanism.

**Purpose and Function**
- Stores precomputed attention keys and values, eliminating redundant computation for previously processed tokens
- Dramatically accelerates inference by avoiding recalculation of context at each step
- Enables efficient autoregressive text generation

**Scale and Impact**
- For models like LLaMA-13B, a single sequence's KV cache can reach 1.7GB
- Batch processing with longer sequences can push total cache sizes to 40GB or more
- The cache is both large and dynamic—its size depends on active sequences, their lengths, and batch size
- Inefficient KV cache management severely limits concurrent request handling, increasing costs and reducing hardware utilization

### Memory Fragmentation Challenge

Fragmentation represents one of the most critical bottlenecks in GPU-based LLM inference, arising from rigid memory allocation schemes.

**Internal Fragmentation**

Occurs when pre-allocated memory blocks exceed actual sequence requirements, leaving unused space within allocations.

- **Example scenario:** Pre-allocating space for 2048 tokens when a sequence uses only 200 tokens wastes the remaining capacity
- **Severity:** Traditional systems can waste 60-80% of GPU memory due to internal fragmentation
- **Performance impact:** Limits concurrent requests and reduces effective throughput

**External Fragmentation**

Develops as sequences of varying lengths start and finish, scattering free memory into small, non-contiguous chunks unsuitable for new allocations.

- **Result:** Even with sufficient total free memory, lack of contiguous space prevents new request allocation
- **Consequence:** Premature out-of-memory errors despite available capacity

PagedAttention eliminates both fragmentation types through on-demand block allocation and release, similar to OS virtual memory paging.

### Virtual Memory and Paging Architecture

PagedAttention adapts classic operating system virtual memory concepts for LLM inference.

**Core Principles**
- **Virtual memory:** Separates logical memory addresses from physical locations, enabling non-contiguous storage
- **Paging:** Divides memory into fixed-size pages with logical-to-physical mapping via page tables
- **LLM application:** KV cache is divided into blocks that can reside anywhere in GPU memory, with sequences maintaining block tables for logical-to-physical mapping

**Capabilities Enabled**
- On-demand block allocation as sequences generate tokens
- Immediate reuse of freed blocks when sequences complete
- Memory sharing between sequences through copy-on-write mechanisms
- Efficient handling of variable-length sequences without pre-allocation waste

### Block Table (Page Table)

The block table is the data structure that maps logical token positions to physical memory blocks for each sequence.

**Functionality**
- Enables sequences to reconstruct context for attention computation regardless of physical block locations
- Supports fast lookup during inference and efficient allocation/deallocation
- Maintains sequence state across multiple inference steps

**Performance Considerations**
- Introduces small computational overhead for table lookups
- Overhead is far outweighed by dramatic reduction in memory waste
- Enables memory optimizations impossible with contiguous allocation

## Advanced Features

### Memory Sharing Mechanisms

PagedAttention enables sophisticated memory sharing between sequences and requests, particularly beneficial for parallel sampling and advanced decoding strategies.

**Parallel Sampling**

Generates multiple completions from the same prompt efficiently.

- **Mechanism:** Shared prompt KV cache blocks are referenced by all output sequences
- **Benefit:** Eliminates memory duplication, reducing usage and enabling higher throughput
- **Implementation:** Block tables for each sample point to the same physical blocks for shared sequence portions

**Beam Search Optimization**

Multiple beams often share the same prefix, enabling efficient memory usage.

- **Shared prefixes:** Common beam prefixes use shared memory blocks
- **Divergence handling:** Copy-on-write mechanism handles beam-specific modifications
- **Mixed decoding:** Simultaneously serves greedy, sampling, and beam search strategies without redundant allocation

### Copy-on-Write

A memory management technique ensuring safe modification of shared memory blocks.

**Operation**
- When a sequence modifies a shared block, a new copy is created for that sequence only
- Other sequences continue referencing the original block
- Prevents data corruption and race conditions in shared memory scenarios

**Benefits**
- Enables aggressive memory sharing without sacrificing correctness
- Maintains isolation when needed while maximizing shared resources
- Essential for parallel sampling and beam search efficiency

## Technical Implementation

### Attention Computation with Paging

Traditional attention kernels expect contiguous memory for keys and values. PagedAttention introduces custom kernels that efficiently fetch KV pairs from scattered blocks.

**Implementation Details**
- Kernel consults block table to gather necessary key-value vectors from potentially scattered blocks
- Optimized memory access patterns minimize overhead
- Supports both single-sequence and batched inference

**Performance Characteristics**
- Minor computational overhead from scattered memory access
- Massive reduction in wasted memory enables larger batches
- Net result: Significant throughput improvement despite small computational cost

### vLLM Integration

vLLM is an open-source, high-performance LLM inference engine implementing PagedAttention as its core memory management system.

**Key Features**
- State-of-the-art throughput: up to 24x faster than HuggingFace Transformers
- Dramatically reduced memory waste: from 60-80% to under 4%
- Support for massive batch sizes and long sequences
- Advanced decoding strategies: parallel sampling, beam search, mixed decoding
- Compatible with HuggingFace models, PyTorch, and OpenAI API

**Deployment Options**
- Local deployment via pip installation
- Cloud-native deployments on major platforms
- Serverless options through providers like RunPod
- Enterprise integration with Databricks, Dropbox, and others

**Model Support**

vLLM supports a wide range of model architectures:
- Classic transformers: Llama, GPT-2, GPT-J, Mistral
- Mixture-of-Experts: Mixtral, Qwen2MoE
- Multimodal LLMs: LLaVA, StableLM, Qwen-VL

## Usage and Implementation

### Installation and Setup

```bash
# Install vLLM
pip install vllm

# Run inference server
python -m vllm.entrypoints.openai.api_server --model <model_name>
```

Replace `<model_name>` with any supported model identifier.

### Key Use Cases

**High-Throughput Chatbots**
- Production chatbot services like LMSYS Chatbot Arena
- Concurrent handling of thousands of conversations
- Efficient resource utilization for cost-effective scaling

**Batch Document Processing**
- Simultaneous processing of large document collections
- Question-answering over extensive knowledge bases
- Summarization and analysis pipelines

**Advanced Decoding Workloads**
- Parallel sampling for diverse output generation
- Beam search for high-quality text generation
- Mixed decoding strategies for different request types

**Resource-Constrained Deployments**
- Edge inference scenarios with limited GPU memory
- Maximizing throughput on available hardware
- Cost optimization for cloud deployments

## Performance and Benchmarks

### Quantitative Improvements

**Throughput Gains**
- Up to 24x improvement over HuggingFace Transformers
- 3.5x improvement over Text Generation Inference (TGI)
- Enables serving more requests with same hardware

**Memory Efficiency**
- Reduces memory waste from 60-80% to under 4%
- Enables larger batch sizes for higher throughput
- Supports longer sequences without memory pressure

**Real-World Impact**
- LMSYS Chatbot Arena: 2-3x more requests per second
- 50% reduction in GPU usage for same workload
- Significant cost savings through improved resource utilization

### Industry Adoption

**Production Deployments**
- LMSYS Chatbot Arena for model evaluation
- Databricks for enterprise LLM applications
- Dropbox for document understanding
- AWS, AMD, NVIDIA for cloud and hardware platforms
- Roblox for gaming and social applications

**Open Source Ecosystem**
- Over 20,000 GitHub stars
- Active community contributions
- Frequent updates and improvements
- Growing ecosystem of extensions and integrations

## Best Practices

**Model Selection**
- Choose models from vLLM's supported list for guaranteed compatibility
- Consider model size relative to available GPU memory
- Evaluate throughput requirements for hardware sizing

**Batch Size Optimization**
- Start with conservative batch sizes and increase based on monitoring
- Monitor GPU memory utilization and adjust accordingly
- Balance batch size with latency requirements

**Performance Monitoring**
- Track throughput metrics: requests per second, tokens per second
- Monitor GPU memory utilization and fragmentation
- Analyze latency distributions for quality of service

**Deployment Considerations**
- Use appropriate hardware: NVIDIA GPUs with sufficient VRAM
- Configure resource limits based on workload characteristics
- Implement proper monitoring and alerting
- Plan for failover and high availability in production

## References

- [Efficient Memory Management for Large Language Model Serving with PagedAttention (arXiv)](https://arxiv.org/abs/2309.06180)
- [vLLM Blog: Easy, Fast, and Cheap LLM Serving with PagedAttention](https://blog.vllm.ai/2023/06/20/vllm.html)
- [Hopsworks Dictionary: PagedAttention](https://www.hopsworks.ai/dictionary/pagedattention)
- [Doubleword: Optimizing GPU Memory for LLMs](https://www.doubleword.ai/resources/optimizing-gpu-memory-for-llms-a-deep-dive-into-paged-attention)
- [Runpod Blog: Introduction to vLLM and PagedAttention](https://www.runpod.io/blog/introduction-to-vllm-and-pagedattention)
- [KV Cache Optimization Deep Dive - Medium](https://medium.com/foundation-models-deep-dive/kv-cache-guide-part-4-of-5-system-superpowers-framework-realities-kv-cache-in-action-6fb4fb575cf8)
- [Red Hat Developer: How PagedAttention Resolves Memory Waste](https://developers.redhat.com/articles/2025/07/24/how-pagedattention-resolves-memory-waste-llm-systems)
- [YouTube: vLLM/PagedAttention Technical Explanation](https://www.youtube.com/watch?v=5ZlavKF_98U&t=351s)
- [vLLM Documentation](https://docs.vllm.ai/en/latest/getting_started/quickstart.html)
- [vLLM GitHub Repository](https://github.com/vllm-project/vllm)
- [Operating Systems: Three Easy Pieces - Virtual Memory](https://pages.cs.wisc.edu/~remzi/OSTEP/vm-intro.pdf)
- [vLLM Supported Models](https://docs.vllm.ai/en/latest/models/supported_models.html)
