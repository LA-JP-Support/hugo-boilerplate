---
title: "KV Cache"
date: 2025-12-18
lastmod: 2025-12-18
translationKey: "kv-cache"
description: "A memory technique that speeds up AI text generation by saving and reusing calculations from previous words instead of redoing them for each new word."
keywords: ["KV Cache", "LLMs", "Transformer models", "inference optimization", "token generation"]
category: "AI Infrastructure & Deployment"
type: "glossary"
draft: false
---

## What is KV Cache?

KV Cache (Key-Value Cache) is an inference-time optimization for transformer models, especially large language models (LLMs), that stores the key (K) and value (V) tensors computed during attention for all previously processed tokens. Instead of recalculating these tensors for every token at each inference step, the model reuses them from cache and computes only the new token's K and V. This approach is foundational for efficient, high-speed autoregressive text generation.

KV Cache acts as auxiliary memory holding intermediate key and value tensors from previous tokens so that, as new tokens are generated, only the new token's K and V need computation and appending. All prior K/Vs are instantly available from cache, dramatically reducing computational overhead.

## How KV Cache Is Used

KV Cache is used exclusively during inference in transformer-based models for generating text token-by-token.

**Core Usage Pattern**Autoregressive generation involves LLMs producing text one token at a time, conditioning each prediction on all prior tokens. At each inference step, the model needs K and V for the full sequence to compute attention for the next token. With KV Cache, instead of recomputing K and V for all previous tokens at every step, only the new token's K and V are computed and appended to cache.

**Outcome:**Dramatically reduced computation, lower latency, and notable cost savings during inference—especially for long sequences.

**Common Usage Contexts**- Text generation with LLMs (GPT, Llama, Claude, Gemini)
- Chatbots and conversational agents
- Code completion and code assistants
- Real-time and batch inference serving

## Why KV Cache Is Critical for LLMs

### Challenge Without KV Cache

The transformer attention mechanism involves three projections per token:

- **Query (Q):**What the current token "wants to know"
- **Key (K):**The "address label" of each token
- **Value (V):**The "content" of each token

During inference, LLMs process input one token at a time. Standard inference recomputes K and V for every token in the current sequence, including already processed tokens. This is highly inefficient for long sequences.

**Inefficiency Example**Generating "The cat sits":
- Generate "The": compute K/V for "The"
- Generate "The cat": recompute K/V for both "The" and "cat"
- Generate "The cat sits": recompute K/V for all three tokens

**With KV Cache**- Compute K/V for "The" once, store it
- On "cat", compute K/V for "cat", append to cache
- On "sits", compute K/V for "sits", append to cache; "The" and "cat" K/V are reused

**Optimization Benefits**- **Speed:**Up to 5–20× faster inference
- **Cost:**Significant reduction in compute and API costs
- **Scalability:**Enables long-context and multi-turn conversations

## How KV Cache Works: Detailed Example

### Without KV Cache

For prompt: `["The", "cat", "sits"]`

Each step recomputes K and V for all tokens in current sequence:

```
Step 1: "The"           --> K1, V1    (computed)
Step 2: "The cat"       --> K1, V1, K2, V2  (K1, V1 recomputed)
Step 3: "The cat sits"  --> K1, V1, K2, V2, K3, V3 (all recomputed)
```

### With KV Cache

Each step computes/appends K/V only for new token; cache holds prior K/Vs:

```
Step 1: "The"      --> K1, V1    (stored in cache)
Step 2: "cat"      --> K2, V2    (appended to cache)
Step 3: "sits"     --> K3, V3    (appended to cache)
```

**Cache after step 3:**```
K-cache: [K1, K2, K3]
V-cache: [V1, V2, V3]
```

## Technical Implementation

### Mathematical Formulation

For a sequence of n input tokens, the transformer layer computes:

```
Attention(Q, K, V) = softmax(Q K^T / √d_k) V
```

- **During training:**All tokens' Q, K, V computed in parallel
- **During inference with KV cache:**Only new token's Q, K, V computed; prior K and V retrieved from cache

### PyTorch KV Cache Example

```python
class KVCache:
    def __init__(self):
        self.cache = {"key": None, "value": None}

    def update(self, key, value):
        if self.cache["key"] is None:
            self.cache["key"] = key
            self.cache["value"] = value
        else:
            self.cache["key"] = torch.cat([self.cache["key"], key], dim=1)
            self.cache["value"] = torch.cat([self.cache["value"], value], dim=1)

    def get_cache(self):
        return self.cache
```

### Hugging Face Transformers Usage

Most modern libraries handle KV cache automatically:

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained('gpt2')
model = AutoModelForCausalLM.from_pretrained('gpt2')

tokens = tokenizer.encode("The cat sits", return_tensors="pt")
output = model.generate(tokens, max_new_tokens=10, use_cache=True)
print(tokenizer.decode(output[0]))
```

The `use_cache` parameter enables KV caching (default: `True`).

## Performance Impact

### Quantitative Benchmarks

| Feature | Standard Inference | KV Caching |
|---------|-------------------|------------|
| Computation per Token | Repeats calculations | Reuses cached values |
| Memory Usage | Less per step | Extra for cache, efficient overall |
| Speed | Slower with longer text | Fast even with long text |
| Cost | High compute, longer latency | Lower compute, reduced latency |

**Benchmarks (T4 GPU, SmolLM2-1.7B):**- Standard inference (no KV cache): 61 seconds
- KV caching enabled: 11.7 seconds
- **~5.2× speedup**

**API Cost Savings:**Many providers (Anthropic, OpenAI) charge less for cached tokens—up to 10× cheaper (e.g., $0.30 vs $3 per million tokens).

## Best Practices for Maximizing Efficiency

### Prompt Engineering & Context Management

**Stable Prompt Prefix:**Prompt prefixes must be identical between turns. Any change (even single token) breaks cache from that point onward.

**Append-only Context:**Always append new information; never rewrite or reorder previous context.

**Deterministic Ordering:**Structured data must have consistent order to avoid accidental cache invalidation.

**Explicit Cache Breakpoints:**For multi-turn agents, mark where context changes so frameworks can maintain efficiency.

### Production Cache Management

**Cache Size:**K/V tensors scale linearly with context length. Very long sequences can become memory bottleneck.

**Cache Lifetime:**Invalidate/expire cache entries when context changes or when memory must be freed.

**Concurrency:**Each concurrent request may require its own cache space.

**Best Practice:**Keep prompt prefix stable and context append-only. Avoid dynamic context that changes old entries.

## Advanced KV Cache Techniques

**Paged Attention**Divides context into "pages" (chunks). Only relevant pages kept in fast memory; old pages offloaded or recomputed as needed. Enables handling very long contexts (tens of thousands of tokens) without exhausting GPU memory.

**Radix Attention**Organizes cached tokens in radix-tree structure. Logarithmic scaling: attend to groups of tokens hierarchically.

**Multi-Query Attention**Reduces KV cache memory by sharing keys/values across attention heads.

**Emerging Trends**- Predictive cache warming: Pre-populate cache based on anticipated needs
- Hierarchical caching: Multi-level cache strategies (GPU, CPU, disk)
- Dynamic cache sizing: Adjust cache size in real-time

## Real-World Use Cases

**Chatbots and Conversational Agents**Multi-turn conversations reuse prompt prefixes. KV cache reduces time-to-first-token (TTFT) and overall latency.

**Code Generation and Completion**Code assistants (Copilot) use KV cache for instant completions based on existing code context.

**Customer Support Automation**Contextual chat histories efficiently managed for low-latency responses across multiple customer interactions.

**Document and Content Generation**Long-form content creation benefits from prompt caching, enabling efficient editing and iterative workflows.

**Gaming and Interactive Storytelling**In-game dialogue engines cache story context for immersive, low-latency player experiences.

**Case Study:**Anthropic Claude's API charges 10× less for cached tokens. Maintaining stable prefix in customer support chatbots reduces operational costs and boosts responsiveness.

## Limitations and Challenges

**Memory Growth:**K/V cache grows linearly with context. Very long contexts can exhaust GPU memory.

**Cache Invalidation:**Any change to previous tokens (prompt edits, context mutations) invalidates part or all of cache.

**Management Complexity:**Multi-user/multi-turn systems require careful cache management.

**Training Limitation:**KV cache is inference-only optimization, not used during training.

**Mitigation Strategies:**- Implement cache size limits and eviction policies
- Monitor memory usage and implement alerts
- Use advanced techniques like paged attention for long contexts
- Design prompts with cache efficiency in mind

## Frequently Asked Questions

**Does KV cache work during training?**No. KV cache is an inference-only optimization. Training computes all attention in parallel.

**How much memory does KV cache use?**Memory scales linearly with sequence length and model size. For long sequences, cache can consume significant GPU memory.

**Can KV cache be used with streaming responses?**Yes. KV cache is particularly effective for streaming, as each new token leverages cached computation from previous tokens.

**What happens if the prompt changes?**Any change invalidates cache from that point forward. Keep prompt prefixes stable for maximum efficiency.

**Do all LLM APIs use KV cache?**Most production LLM APIs use KV cache automatically. Check provider documentation for specific implementation details and pricing.

## References


1. Hugging Face. (n.d.). KV Caching Explained. Hugging Face Blog.
2. Raschka, Sebastian. (n.d.). Understanding and Coding the KV Cache in LLMs. Sebastian Raschka Magazine.
3. Neptune. (n.d.). Transformers Key-Value Caching Explained. Neptune Blog.
4. Data Science Dojo. (n.d.). Unlocking the Power of KV Cache. Data Science Dojo Blog.
5. Sharma, Kapil. (n.d.). KV Caching Illustrated. Personal Blog.
6. Akira AI. (n.d.). KV Caches and Time-to-First-Token. Akira AI Blog.
7. Szot, Andrew. (n.d.). KV Cache. Personal Blog.
8. Hugging Face. (n.d.). Generation Strategies - KV Caching. Transformers Documentation.
9. Lages, Joao. (n.d.). KV Caching Explained. Medium.
