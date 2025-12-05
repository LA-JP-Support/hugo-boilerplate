---
title: "Weaviate"
date: 2025-11-25
translationKey: "weaviate"
description: "Weaviate is an open-source, cloud-native vector database storing objects & high-dimensional embeddings. It enables semantic, hybrid search & large-scale AI/ML applications."
keywords: ["Weaviate", "vector database", "semantic search", "vector embeddings", "hybrid search"]
category: "AI Infrastructure & Deployment"
type: "glossary"
draft: false
---
## What is Weaviate?

**Weaviate** is an open-source, cloud-native vector database purpose-built for storing both structured data objects and high-dimensional vector embeddings. Its architecture enables advanced semantic search, hybrid search, and large-scale AI/ML applications.

- **Open-source**: Licensed under BSD-3-Clause, Weaviate features a strong developer community and transparent codebase ([Weaviate GitHub](https://github.com/weaviate/weaviate)).
- **Cloud-native**: Designed for distributed, resilient, and scalable deployments across Kubernetes, public clouds, or on-premise infrastructure ([Weaviate Deployment Docs](https://docs.weaviate.io/deploy)).
- **Objects and vectors together**: Uniquely, Weaviate stores both classic object properties and their corresponding vector representations, making it ideal for similarity and semantic search ([Weaviate Docs](https://docs.weaviate.io/weaviate)).

**In-depth resources:**  
- [Weaviate Platform Overview](https://weaviate.io/platform)  
- [A Gentle Introduction to Vector Databases](https://weaviate.io/blog/what-is-a-vector-database)

## Core Concepts

### Vectors and Vector Embeddings

- **Vector Embedding**: A vector embedding is a numeric array—often hundreds or thousands of floating-point numbers—produced by machine learning models to capture semantic meaning from data like text, images, or audio ([DataCamp: Vector Embeddings](https://www.datacamp.com/blog/vector-embedding)). For example, the phrase *"AI database"* might become `[0.12, -0.98, 1.54, ...]`.
- **Object**: In Weaviate, an object is a data entry (document, image, product, etc.) stored alongside its vector embedding. This pairing enables powerful semantic and similarity search directly in the database.

> **Deep dive:**  
> [Vector Embeddings Explained](https://weaviate.io/blog/vector-embeddings-explained)  
> [Embeddings and Vector Databases (Medium)](https://medium.com/@vladris/embeddings-and-vector-databases-732f9927b377)

### Vector Indexes

To search billions of vectors efficiently, Weaviate uses specialized index structures ([Vector Indexing Docs](https://docs.weaviate.io/weaviate/concepts/vector-index)):

- **Flat Index**: A simple, lightweight structure ideal for small datasets or multi-tenant cases. Stores vectors in sequence—search is exact but linear in time.
- **HNSW Index (Hierarchical Navigable Small World)**: A graph-based index with logarithmic search complexity, optimized for fast, approximate nearest neighbor (ANN) queries at massive scale. [HNSW](/en/glossary/hnsw--hierarchical-navigable-small-world-/) is the default for production use ([HNSW explained](https://docs.weaviate.io/weaviate/concepts/vector-index#hierarchical-navigable-small-world-hnsw-index)).
- **Dynamic Index**: Starts as a flat index, then automatically converts to HNSW beyond a configured threshold, balancing ingest speed and query performance.

> **Technical details:**  
> [Vector Index Configuration](https://docs.weaviate.io/weaviate/config-refs/indexing/vector-index)  
> [Choosing an Index Type](https://docs.weaviate.io/weaviate/concepts/vector-index#which-vector-index-is-right-for-me)

### Sharding and Clustering

**Sharding** divides collections into multiple shards, each with its own vector index and object store, distributed across nodes for horizontal scale and resilience. Shards enable a single logical database to span multiple servers, multiplying storage and compute ([Cluster Concepts](https://docs.weaviate.io/weaviate/concepts/cluster)).

**Replication** creates redundant copies of shards, ensuring [high availability](/en/glossary/high-availability--ha-/) and fault tolerance. Weaviate uses a leaderless, eventually consistent replication model for data, plus Raft consensus for metadata, allowing robust distributed deployments ([Cluster Architecture](https://docs.weaviate.io/weaviate/concepts/replication-architecture/cluster-architecture)).

![Weaviate Sharding](https://docs.weaviate.io/assets/images/shards_explained-9a5f2cea95faf0d860cbd63ec77f73cb.png)

**Further reading:**  
- [Scaling and Weaviate (Weaviate Blog)](https://weaviate.io/blog/scaling-and-weaviate)
- [Horizontal Scaling Docs](https://docs.weaviate.io/weaviate/concepts/cluster)

## Key Features of Weaviate

- **Semantic Search**: Queries retrieve data by meaning, not just keywords, using learned vector embeddings ([Weaviate Search Basics](https://docs.weaviate.io/weaviate/search/basics)).
- **Hybrid Search**: Combines vector similarity with classic keyword search (BM25, Boolean logic) for unparalleled relevance ([Hybrid Search Docs](https://docs.weaviate.io/weaviate/search/hybrid)).
- **Retrieval-Augmented Generation (RAG) Support**: Serves as a vector store backend to supply factual, up-to-date knowledge to LLMs ([Weaviate RAG](https://weaviate.io/rag), [LangChain Integration](https://weaviate.io/blog/enterprise-workflow-langchain-weaviate)).
- **Multi-Tenancy**: Isolates data and compute across tenants (e.g., customers, teams) in a single cluster ([Multi-Tenancy Docs](https://docs.weaviate.io/weaviate/concepts/data#multi-tenancy)).
- **Scalability and Clustering**: Shard and replicate data for linear scale and high availability ([Clustering Docs](https://docs.weaviate.io/weaviate/concepts/cluster)).
- **Model Integrations**: Out-of-the-box support for 15+ ML providers, including OpenAI, Cohere, HuggingFace, Google, AWS, NVIDIA, and more ([Model Provider List](https://docs.weaviate.io/weaviate/model-providers)).
- **Agentic AI**: Foundation for agent-driven applications that require autonomous reasoning and workflow execution ([Agent Framework](https://docs.weaviate.io/agents)).
- **Enterprise Readiness**: Features include RBAC, encryption, audit logs, and compliance with SOC 2, HIPAA, and more.
- **Flexible Deployment**: Run Weaviate self-hosted, as a managed service (Weaviate Cloud), on Kubernetes, or embedded in [Python/JS](/en/glossary/code-block--python-js-/)/TS apps ([Deployment Guide](https://docs.weaviate.io/deploy)).

> **Comprehensive feature list:**  
> [Weaviate Platform Features](https://weaviate.io/platform#open-source-vector-database-features)

## Technical Deep Dive

### Vector Embeddings

Vector embeddings in Weaviate are generated by machine learning models and encode the semantic properties of objects. They can be created natively using integrated model providers or imported from external pipelines ([Model Providers](https://docs.weaviate.io/weaviate/model-providers)).

- Embeddings place similar objects close together in vector space, enabling semantic search and clustering.

### Vector Indexing & Approximate Nearest Neighbor (ANN) Search

- **HNSW**: HNSW indexes build a multi-layered graph for fast, scalable ANN search. Efficient for datasets with millions or billions of vectors ([HNSW in Weaviate](https://docs.weaviate.io/weaviate/concepts/vector-index#hierarchical-navigable-small-world-hnsw-index)).
- **Flat**: Direct, linear scan—good for small datasets or multi-tenant scenarios.
- **Dynamic**: Automatically transitions from flat to HNSW as data grows.
- **Compression**: PQ, SQ, and BQ compression options further optimize memory use and search speed ([Compression Docs](https://docs.weaviate.io/weaviate/configuration/compression)).

### Hybrid Search

- Merges BM25 keyword search and vector similarity to combine lexical and semantic relevance in a single query ([Hybrid Search Docs](https://docs.weaviate.io/weaviate/search/hybrid)).
- Hybrid queries can tune the blend ratio for optimal results.

### Multi-Tenancy

- Each tenant gets an isolated shard (or set of shards), with strict separation of data and compute ([Multi-Tenancy Docs](https://docs.weaviate.io/weaviate/concepts/data#multi-tenancy)).

### Clustering, Sharding, and Replication

- Clusters scale out by distributing shards across nodes ([Cluster Docs](https://docs.weaviate.io/weaviate/concepts/cluster)).
- Replication uses a leaderless model for data and Raft for metadata, supporting high availability and resilience ([Replication Architecture](https://docs.weaviate.io/weaviate/concepts/replication-architecture/cluster-architecture)).

### Model & Language Integrations

- Connect to major providers—OpenAI, Anthropic, AWS, Cohere, HuggingFace, Google, NVIDIA, and more ([Full Model Provider List](https://docs.weaviate.io/weaviate/model-providers)).
- Supports both API-based and self-hosted inference.

### APIs & SDKs

- **GraphQL API**: Flexible, powerful querying for all operations.
- **REST API**: Classic HTTP endpoints for CRUD and search.
- **SDKs**: Official libraries for Python, Go, JavaScript, TypeScript, and Java ([SDK Reference](https://docs.weaviate.io/weaviate/client-libraries)).
- [Weaviate Recipes](https://github.com/weaviate/recipes): Practical code samples for all SDKs and use cases.

## Example Queries

#### 1. Pure Vector Search
```python
response = collection.query.near_vector(
    near_vector=[0.1, 0.1, 0.1],
    limit=5
)
```

#### 2. Semantic Search
```python
response = collection.query.near_text(
    query="login issues after OS upgrade",
    limit=5
)
```

#### 3. Hybrid Search
```python
response = collection.query.hybrid(
    query="login issues after OS upgrade",
    alpha=0.75,
    limit=5
)
```

> **Quickstart:** [Try Weaviate in 15–30 minutes](https://docs.weaviate.io/weaviate/quickstart)

## Use Cases & Industry Applications

| Use Case                       | Description                                                                                 | Example                                                   |
|---------------------------------|---------------------------------------------------------------------------------------------|-----------------------------------------------------------|
| **Semantic Search**             | Find by meaning, not just keywords.                                                         | Search support tickets related to "account lockout"       |
| **Retrieval-Augmented Generation (RAG)** | Enhance LLM output with your private data.                                      | Chatbot grounded in company knowledge base                |
| **Recommendation Systems**      | Suggest similar or personalized items.                                                      | Product recommendations in e-commerce                     |
| **Chatbots & Virtual Agents**   | Enable context-aware AI conversations.                                                      | Customer service bots with intent understanding           |
| **Content Classification**      | Tag and organize unstructured data.                                                        | Auto-label news by topic similarity                       |
| **Image & Multimedia Search**   | Search by content/image similarity, not just filename.                                     | Find images visually similar to a sample                   |
| **Fraud Detection**             | Spot anomalous transaction patterns in complex data.                                       | Detecting fraud via semantic similarity to known cases     |

> **More examples:** [Weaviate Use Cases](https://weaviate.io/solutions)

**Industry Examples**: E-commerce (semantic search, recommendations), media (content discovery), healthcare (clinical document search), finance (fraud detection), and enterprise AI search ([Industry Solutions](https://weaviate.io/solutions)).

## Deployment Options

- **Self-hosted**: Run on [Docker](/en/glossary/docker/), bare-metal, or VMs ([Local Install](https://docs.weaviate.io/weaviate/quickstart/local)).
- **Managed Cloud**: Fully managed by Weaviate with advanced security and enterprise features ([Weaviate Cloud](https://weaviate.io/cloud)).
- **Kubernetes**: Run as a scalable microservice using the official Helm chart ([K8s Deployment Guide](https://docs.weaviate.io/deploy/installation-guides/k8s-installation)).
- **Embedded**: Launch directly from Python or JS/TS for rapid prototyping ([Embedded deployment](https://docs.weaviate.io/deploy/embedded)).

## Integration and Ecosystem

- **Model Providers**: Integrate with Anthropic, AWS, Cohere, Google, [Hugging Face](/en/glossary/hugging-face/), NVIDIA, OpenAI, Mistral, Voyage AI, Databricks, JinaAI, and more ([Full List](https://docs.weaviate.io/weaviate/model-providers)).
- **Plugins and Frameworks**: Native integrations with Haystack, LangChain, LlamaIndex, CrewAI, Semantic Kernel, and more ([Integrations](https://docs.weaviate.io/integrations/llm-agent-frameworks/langchain)).
- **Data Platforms**: Airbyte, Box, Databricks, IBM, Unstructured, and more ([Data Platform Integrations](https://docs.weaviate.io/integrations/data-platforms/airbyte)).
- **Monitoring & Ops**: Arize, Comet, Cleanlab, Weights & Biases, Langtrace, and more ([Ops Integrations](https://docs.weaviate.io/integrations/operations/arize)).
- **Community**: 15k+ GitHub stars, 50k+ developers, and a vibrant [Slack channel](https://weaviate.io/slack).

## Comparison with Other Vector Databases

| Feature                           | **Weaviate**                | [Pinecone](/en/glossary/pinecone/) | Milvus | [Chroma](/en/glossary/chroma/) | Qdrant |
|------------------------------------|-----------------------------|----------|--------|--------|--------|
| **Open Source**                   | Yes (BSD-3-Clause)          | No       | Yes    | Yes    | Yes    |
| **Built-in Model Integrations**    | Yes (15+ providers)         | Limited  | Limited| No     | Limited|
| **Hybrid Search**                 | Yes (native)                | Partial  | Partial| No     | Yes    |
| **Multi-Tenancy**                 | Yes                         | Yes      | Yes    | No     | Yes    |
| **RAG & Agentic Support**         | Yes                         | Yes      | Yes    | Yes    | Yes    |
| **Deployment Flexibility**        | Local, Cloud, K8s, Embedded | Cloud    | Local  | Local  | Local  |
| **Enterprise Features**           | RBAC, encryption, audit     | Yes      | Yes    | No     | Yes    |

> **Further reading:**  
> [What is a Vector Database?](https://weaviate.io/blog/what-is-a-vector-database)

## Getting Started with Weaviate

### Quickstart Steps

1. **Spin up an instance:**  
   - [Weaviate Cloud Quickstart](https://docs.weaviate.io/weaviate/quickstart)
   - [Local Docker Quickstart](https://docs.weaviate.io/weaviate/quickstart/local)
2. **Connect your data:** Import objects and vectors using SDKs.
3. **Vectorize:** Use built-in model integrations or import precomputed vectors.
4. **Query:** Run semantic, hybrid, and filtered searches via API or SDK.
5. **Scale:** Add nodes, enable [multi-tenancy](/en/glossary/multi-tenancy/), and configure backups.

> **Full setup guide:** [Weaviate Quickstart](https://docs.weaviate.io/weaviate/quickstart)

## Example: Semantic Search with Python SDK

```python
import weaviate

client = weaviate.Client("https://my-weaviate-instance")
collection = client.collections.get("SupportTickets")

# Semantic search for tickets about "login issues"
response = collection.query.near_text(
    query="login issues after OS upgrade",
    limit=5
)

for ticket in response.objects:
    print(ticket["title"], ticket["description"])
```

**More code samples:**  
- [Weaviate Recipes GitHub](https://github.com/weaviate/recipes)

## Community & Support

- **Open Source:**  
  - [Weaviate GitHub](https://github.com/weaviate/weaviate)
  - Feature requests, contributions, and code browsing.
- **Documentation & Tutorials:**  
  - [Weaviate Docs](https://docs.weaviate.io/weaviate)
  - [Weaviate Academy](https://academy.weaviate.io/)
- **Community:**  
  - [Slack](https://weaviate.io/slack): Q&A, events, discussions.
  - [Blog](https://weaviate.io/blog): Technical posts, updates, case studies.
- **Support:**  
  - Community via forums and Slack.
  - Enterprise: Dedicated support with Weaviate Cloud.

> **Testimonial:**  
> “Weaviate's batteries-included approach, incorporating both [model serving](/en/glossary/model-serving/) and multi-tenancy, has helped us quickly prototype and build our vector search at Stack.” — Stack Overflow Team

## FAQ

**Q: Is Weaviate open source?**  
A: Yes, BSD-3-Clause license ([GitHub](https://github.com/weaviate/weaviate)).

**Q: Can I use Weaviate for Retrieval-Augmented Generation (RAG)?**  
A: Yes, Weaviate is widely used as a RAG backend ([RAG Docs](https://weaviate.io/rag)).

**Q: Does Weaviate support hybrid search?**  
A: Yes, it natively combines semantic (vector) and keyword (BM25) search ([Hybrid Search](https://docs.weaviate.io/weaviate/search/hybrid)).

**Q: What languages and SDKs are available?**  
A: Python, Go, JavaScript, TypeScript, Java, REST, and GraphQL ([SDK Reference](https://docs.weaviate.io/weaviate/client-libraries)).

**Q: How does Weaviate handle scaling and high availability?**  
A: Horizontal [sharding](/en/glossary/sharding/), clustering, and replication ([Scaling Guide](https://docs.weaviate.io/weaviate/concepts/cluster)).

**Q: Is Weaviate suitable for enterprise use?**  
A: Yes. It offers RBAC, encryption, audit

