---
title: "Flowise"
translationKey: "flowise"
description: "Flowise is an open-source, visual platform for building custom LLM flows and agentic AI systems with LangChainJS. Design, orchestrate, and deploy advanced AI workflows with minimal code."
keywords: ["Flowise", "LLM workflows", "AI agents", "LangChainJS", "open-source"]
category: "AI Chatbot & Automation"
type: "glossary"
date: 2025-12-03
draft: false
---
## **What is Flowise?**

Flowise is an open-source, generative AI development platform focused on visually building AI agents, chatbots, and complex LLM workflows with LangChainJS as its core orchestrator. Unlike conventional automation tools, Flowise is designed for the orchestration of advanced agentic systems, enabling both single-agent and multi-agent workflows through an intuitive drag-and-drop UI.  

- **Open Source:** Licensed under Apache 2.0 for unrestricted self-hosting and community-driven enhancements.  
- **Visual Builder:** Enables users to visually compose LLM workflows, agents, and pipelines without code.  
- **LangChainJS Ecosystem:** Deep integration with LangChainJS provides powerful tools for memory, retrieval, embeddings, and complex agent behaviors.  
- **Three Visual Builders:**
  - **Assistant:** Simplest, form-based for rapid chatbot creation.
  - **Chatflow:** Node-based for single-agent, flexible LLM flows.
  - **Agentflow:** Most advanced, supporting multi-agent orchestration, branching, looping, and state management.  

**References:**  
- [FlowiseAI Official Documentation](https://docs.flowiseai.com)  
- [Agentflow V2 Details](https://docs.flowiseai.com/using-flowise/agentflowv2)  

## **Core Features and Capabilities**

### **1. Visual Workflow Builder**

Flowise provides a modular, node-based canvas for building LLM-powered workflows:
- **Drag & Drop Interface:** Construct flows by connecting nodes representing LLMs, retrievers, databases, memory, and logic.
- **Reusable Templates:** Access a marketplace/library of pre-built templates and community-contributed flows.
- **Assistant, Chatflow, Agentflow:** Choose between beginner-friendly, single-agent, or advanced multi-agent orchestration builders.

**Reference:**  
- [Visual Builders Overview](https://docs.flowiseai.com)

### **2. Multi-Agent Orchestration**

**Agentflow** supports the design of multi-agent systems:
- **Explicit Workflow Orchestration:** Each node executes a discrete operation; connections define the flow’s control and data sequence.
- **Agent-to-Agent Communication:** Supervisor agents can delegate tasks to workers, aggregate results, and manage state. All agents access conversation history and shared flow state.
- **Loops, Branching, Human-in-the-Loop:** Supports conditional logic, iterative loops, and pauses for human approval or review at any workflow stage.
- **Stateful, Long-Running Agents:** Checkpoints and resume logic for persistent, resilient workflows.

**Reference:**  
- [Agentflow V2 Architecture](https://docs.flowiseai.com/using-flowise/agentflowv2#core-concept)

### **3. Chat Assistants & Single-Agent Flows**

- **Chatflow:** Flexible canvas for building single-agent bots, RAG (Retrieval-Augmented Generation) chatbots, and simple LLM-driven applications.
- **Assistant:** Rapid setup via forms; attach knowledge bases, files, and tools for conversational bots.
- **Advanced RAG:** Incorporate tools like retrievers, rerankers, and graph-based retrieval for high-accuracy Q&A on custom data.

**Reference:**  
- [Assistant and Chatflow Documentation](https://docs.flowiseai.com#assistant)

### **4. Data Connectivity & Integration**

- **100+ Data Formats Supported:** TXT, PDF, DOCX, HTML, CSV, MD, JSON, XML, SQL, and more.
- **Vector Database Integration:** Built-in support for Pinecone, ChromaDB, Weaviate, Milvus, and others.
- **API, SDK, and Embedding:** Expose flows via REST API, Python/Typescript SDKs, or web-embeddable chat widgets.

**Reference:**  
- [Flowise Data Integrations](https://docs.flowiseai.com)

### **5. Observability & Monitoring**

- **Execution Tracing:** Visualize step-by-step execution and data flow for debugging and optimization.
- **Analytics & Metrics:** Track performance, token usage, costs, and other metrics.
- **External Monitoring:** Integrate with observability platforms such as Prometheus and OpenTelemetry.

### **6. Human-in-the-Loop (HITL)**

- **Task Review:** Insert checkpoints that pause execution for human input, review, or approval. These are stateful and can survive application restarts.
- **Permission Controls:** Require human approval before executing sensitive actions, similar to human supervision in autonomous systems.

### **7. Security & Enterprise Readiness**

- **RBAC & SSO:** Fine-grained role-based access control, Single Sign-On for enterprise deployments.
- **Credential Management:** Encrypted storage for API keys and secrets.
- **Horizontal Scalability:** Message queues and worker-based architecture for scaling flows across clusters or cloud environments.

### **8. Extensibility**

- **Custom Nodes:** Implement and add your own logic, models, or integrations.
- **Marketplace/Community Components:** Share and reuse nodes and flow templates.

**Reference:**  
- [Marketplace and Extensibility](https://cloud.flowiseai.com/marketplace)

## **How Flowise is Used**

### **Building AI Agents Visually**

Users construct LLM-powered workflows by visually linking modular nodes:
- **No/Low-Code:** Build flows visually, configure nodes for models, memory, tools, and logic.
- **Scale from Simple to Advanced:** Rapid prototyping of chatbots, then expansion to multi-agent or autonomous orchestration.

#### **RAG (Retrieval-Augmented Generation) Integration**
- **Ingest Custom Data:** Drag in data source nodes for PDFs, DOCX, or websites.
- **Index and Retrieve:** Connect to vector database nodes for efficient retrieval.
- **LLM Node:** Attach a GPT-4, Claude, or local model node for generation.
- **Memory Node:** Add context retention for multi-turn conversations.

#### **Workflow Creation Steps**

1. **Install Flowise:**  
   ```bash
   npm install -g flowise
   npx flowise start
   ```
   - Or register for [Flowise Cloud](https://cloud.flowiseai.com/signin).

2. **Create New Flow:**  
   - Access dashboard at `http://localhost:3000` or cloud.
   - Choose Assistant, Chatflow, or Agentflow.
   - Drag and connect nodes to define workflow logic.

3. **Configure Nodes:**  
   - Set up LLMs (OpenAI, Ollama, etc.).
   - Integrate retrievers, databases, and memory.
   - Use advanced prompts and few-shot templates.

4. **Test and Debug:**  
   - Use built-in chat window for live testing.
   - Trace execution, inspect outputs, and profile performance.

5. **Deploy:**  
   - Use REST API, SDK, embed chat widget, or share via public URL.

**References:**  
- [Official Getting Started Guide](https://docs.flowiseai.com/getting-started)
- [YouTube: Building AI Chatbot in 10 Minutes](https://www.youtube.com/watch?v=riXpu1tHzl0)

## **Use Cases & Real-World Examples**

### **Enterprise Chatbots & Assistants**

- **Customer Support:** Automate FAQ responses, resolve tickets, escalate complex issues.
- **Internal Knowledge Base:** Employees retrieve company policies, technical docs, SOPs via conversational interface.

### **Multi-Agent AI Systems**

- **Research Teams:** Supervisor agent delegates information gathering to multiple workers, each specializing in sources or analysis.
- **AI Teams:** Orchestrate retrieval, summarization, analysis, and reporting across agent hierarchy.

### **Embedded AI in SaaS Products**

- **InsightSoftware:** Enhanced embedded analytics with AI-driven conversational insights.
- **UneeQ Digital Humans:** Streamlined deployment of digital avatars with advanced conversational AI.

### **Custom Integrations & Automation**

- **Project Management:** Automate creation of Notion tasks directly from Slack using LLM-driven bots.
- **Multi-Modal Chatbots:** Blend text and image processing in a single conversational flow.

### **Education & Personalization**

- **Persona Bots:** Emulate specific teaching or mentoring styles.
- **Translation and Multilingual Bots:** Deploy LLMs with prompt templates for rapid language adaptation.

### **Developer Prototyping & Community**

- **Rapid Prototyping:** Drag-and-drop agent creation for hackathons, demos, and production pilots.
- **Open Source Collaboration:** Active GitHub and Discord communities for sharing flows and troubleshooting.

**Reference:**  
- [Flowise Real-World Examples](https://cobusgreyling.medium.com/flowise-for-langchain-b7c4023ffa71)

## **Key Advantages: Why Use Flowise?**

| Feature             | Flowise Benefit                                             |
|---------------------|------------------------------------------------------------|
| Open Source         | Complete transparency, no vendor lock-in, self-hosting      |
| Visual Development  | Drag-and-drop interface cuts development time               |
| Modular & Flexible  | Compose any LLM workflow, from chatbot to multi-agent team  |
| LLM Agnostic        | 100+ supported models and vector DBs, including local       |
| Community Driven    | Active Discord, GitHub, marketplace of flows and nodes      |
| Enterprise Ready    | RBAC, SSO, encrypted secrets, scalable, on-prem/cloud       |
| Extensible          | Custom nodes, integrations, reusable templates              |
| Observability       | Tracing, analytics, and monitoring support                  |
| Human in the Loop   | Human review/approval embedded in workflows                 |
| Easy Deployment     | APIs, SDKs, embedded widgets, public URLs                   |

**Reference:**  
- [Flowise Feature Matrix](https://docs.flowiseai.com)

## **Technical Architecture & Integrations**

### **Visual Builders**

- **Assistant:** Easiest, form-based, rapid chatbot creation.
- **Chatflow:** Node-based, flexible flows for single-agent systems.
- **Agentflow (V2):** Advanced orchestration, supports explicit workflow design, multi-agent collaboration, loops, branching, and human-in-the-loop.

**Reference:**  
- [Agentflow V2 Deep Dive](https://docs.flowiseai.com/using-flowise/agentflowv2#core-concept)

### **Data Formats Supported**

- **Textual:** TXT, PDF, DOCX, HTML, MD, CSV, JSON, XML, SQL.
- **Multimedia:** Image nodes for multimodal flows.

### **LLM, Tool, and Memory Integrations**

- **LLMs:** OpenAI (GPT-3/4), Ollama (local models), Claude, Llama2, and more.
- **Vector DBs:** Pinecone, ChromaDB, Weaviate, Milvus, and others.
- **Memory:** Buffer, windowed, summary, and custom implementations for conversational context.
- **APIs/SDKs:** REST, Python, Typescript; custom tool integration possible.

### **Security & Scalability**

- **RBAC/SSO:** Enterprise-grade access controls.
- **Encrypted Credentials:** Secure API key and secret storage.
- **Horizontal Scaling:** Message queue and worker model for distributed deployments.

**Reference:**  
- [Security and Scalability Docs](https://docs.flowiseai.com)

## **Getting Started: Installation & First Steps**

### **Installation**

- **Local/Self-Hosted:**
  ```bash
  npm install -g flowise
  npx flowise start
  ```
  - Requires Node.js. Dashboard at `http://localhost:3000`.

- **Cloud Version:**  
  - [Register for Flowise Cloud](https://cloud.flowiseai.com/signin) for instant setup.

### **First Flow**

- **Assistant:** Fill out form, attach tools and files for simple chatbot.
- **Chatflow/Agentflow:** Use canvas to build node-based flows, connect LLMs, retrievers, memory, and tools.
- **Test & Debug:** Use integrated chat window and execution tracing.

### **Deployment**

- **Embed:** Add chat widget to your site.
- **API/SDK:** Integrate with REST, Python, or Typescript SDKs.
- **Public Link:** Share bots with a URL.

### **Community & Support**

- **Docs:** [https://docs.flowiseai.com](https://docs.flowiseai.com)
- **GitHub:** [https://github.com/FlowiseAI/Flowise](https://github.com/FlowiseAI/Flowise)
- **Discord:** [https://discord.gg/jbaHfsRVBW](https://discord.gg/jbaHfsRVBW)
- **YouTube Tutorials:** [Complete Flowise v3 Tutorial](https://www.youtube.com/watch?v=riXpu1tHzl0)

## **Glossary: Related Terms**

- **LLM (Large Language Model):** Deep neural networks trained on massive text data, enabling generation and comprehension of human language.
- **RAG (Retrieval-Augmented Generation):** LLM technique that retrieves relevant context from external sources to improve output accuracy.
- **Agentic Systems:** Architectures with multiple autonomous AI agents collaborating or competing to solve tasks.
- **Vector Database:** Specialized data stores (e.g., Pinecone, ChromaDB) for high-speed similarity search of embeddings.
- **Human-in-the-Loop (HITL):** System design pattern where humans review, approve, or correct automated AI outputs.
- **Chat Window:** UI component for interacting with bots and testing flows in Flowise.
- **API/SDK:** Developer tools for integrating Flowise bots into external applications.
- **Few-shot Learning:** Method where LLMs are guided with a handful of input-output examples within prompts.
- **Open Source:** Software with public, modifiable source code, fostering community contribution.

**Extended Glossary:**  
- [Comprehensive LLM Glossary](https://main--dasarpai.netlify.app/dsblog/Comprehensive-Glossary-of-LLM/#what-is-flowiseai)

## **Links, Community & Further Resources**

- **Official Website:** [https://flowiseai.com](https://flowiseai.com/)
- **Documentation:** [https://docs.flowiseai.com](https://docs.flowiseai.com)
- **GitHub Repo:** [https://github.com/FlowiseAI/Flowise](https://github.com/FlowiseAI/Flowise)
- **YouTube Tutorial:** [How to Build an AI Document Chatbot](https://www.youtube.com/watch?v=riXpu1tHzl0)
- **Discord Community:** [https://discord.gg/jbaHfsRVBW](https://discord.gg/jbaHfsRVBW)
- **Marketplace:** [Flowise Community Flows & Templates](https://cloud.flowiseai.com/marketplace)
- **Third-Party Glossary:** [Comprehensive Glossary of LLM](https://main--dasarpai.netlify.app/dsblog/Comprehensive-Glossary-of-LLM/#what-is-flowiseai)

## **Frequently Asked Questions**

### **How is Flowise different from n8n, Zapier, or Make.com?**
Flowise is tailored for agentic AI workflows, providing native support for LLM orchestration, multi-agent collaboration, RAG, and memory, features not present in general-purpose automation platforms. Flowise is open source, self-hostable, and designed for advanced AI/LLM use cases.

### **Can I use custom LLMs and data?**
Yes. Flowise supports over 100 LLMs (including local models via Ollama and open-source options) and ingestion of all common data formats for RAG-based flows.

### **Is Flowise enterprise-ready?**
Yes, with RBAC, SSO, encrypted credential management, horizontal scalability, and support for both on-premises and cloud deployments.

### **How do I contribute or get support?**
Join the [Discord community](https://discord.gg/jbaHfsRVBW), submit PRs or issues on [GitHub](https://github.com/FlowiseAI/Flowise), and access onboarding guides in the [docs](https://docs.flowiseai.com).

## **User Testimonials**

> "Flowise allows us to supercharge our existing embedded analytics platform with built-in AI features that our clients absolutely love."  
> — Terrence Sheflin, Director of Engineering, InsightSoftware

> "With Flowise, we were able to accelerate our internal 'Build your own AI assistants easily & intuitively' initiative. Truly a game-changer in our tech journey."  
> — Iokin Pardo, Senior Director, BTS Digital

> "Flowise has truly changed how we approach AI. It's simple enough to prototype an idea in minutes, yet powerful enough to take all the way to production."  
> — David Micotto, Senior Director of DX & AI, Publicis Groupe

## **Get Started with Flowise**

- **Start building:** [Sign up free](https://cloud.flowiseai.com/signin) or [install locally](https://docs.flowiseai.com/getting-started).
- **Join the community:** [Discord](https://discord.gg/jbaHfsRVBW)
- **Explore the code:** [GitHub](https://github.com/FlowiseAI/Flowise)
- **Watch tutorials:** [YouTube](https://www.youtube.com/watch?v=ri

