---
title: Flowise Glossary and In-Depth Technical Guide
translationKey: flowise
description: Flowise is an open-source, visual platform for building custom LLM flows
  and agentic AI systems with LangChainJS. Design, orchestrate, and deploy advanced
  AI workflows with minimal code.
keywords:
- Flowise
- LLM workflows
- AI agents
- LangChainJS
- open-source
category: AI Chatbot & Automation
type: glossary
date: 2025-12-05
lastmod: 2025-12-05
draft: false
---
## <strong>What is Flowise?</strong>Flowise is an open-source, generative AI development platform focused on visually building AI agents, chatbots, and complex LLM workflows with LangChainJS as its core orchestrator. Unlike conventional automation tools, Flowise is designed for the orchestration of advanced agentic systems, enabling both single-agent and multi-agent workflows through an intuitive drag-and-drop UI.  

- <strong>Open Source:</strong>Licensed under Apache 2.0 for unrestricted self-hosting and community-driven enhancements.  
- <strong>Visual Builder:</strong>Enables users to visually compose LLM workflows, agents, and pipelines without code.  
- <strong>LangChainJS Ecosystem:</strong>Deep integration with LangChainJS provides powerful tools for memory, retrieval, embeddings, and complex agent behaviors.  
- <strong>Three Visual Builders:</strong>- <strong>Assistant:</strong>Simplest, form-based for rapid chatbot creation.
  - <strong>Chatflow:</strong>Node-based for single-agent, flexible LLM flows.
  - <strong>Agentflow:</strong>Most advanced, supporting multi-agent orchestration, branching, looping, and state management.  
## <strong>Core Features and Capabilities</strong>### <strong>1. Visual Workflow Builder</strong>Flowise provides a modular, node-based canvas for building LLM-powered workflows:
- <strong>Drag & Drop Interface:</strong>Construct flows by connecting nodes representing LLMs, retrievers, databases, memory, and logic.
- <strong>Reusable Templates:</strong>Access a marketplace/library of pre-built templates and community-contributed flows.
- <strong>Assistant, Chatflow, Agentflow:</strong>Choose between beginner-friendly, single-agent, or advanced multi-agent orchestration builders.
### <strong>2. Multi-Agent Orchestration</strong>

<strong>Agentflow</strong>supports the design of multi-agent systems:
- <strong>Explicit Workflow Orchestration:</strong>Each node executes a discrete operation; connections define the flow’s control and data sequence.
- <strong>Agent-to-Agent Communication:</strong>Supervisor agents can delegate tasks to workers, aggregate results, and manage state. All agents access conversation history and shared flow state.
- <strong>Loops, Branching, Human-in-the-Loop:</strong>Supports conditional logic, iterative loops, and pauses for human approval or review at any workflow stage.
- <strong>Stateful, Long-Running Agents:</strong>Checkpoints and resume logic for persistent, resilient workflows.
### <strong>3. Chat Assistants & Single-Agent Flows</strong>- <strong>Chatflow:</strong>Flexible canvas for building single-agent bots, RAG (Retrieval-Augmented Generation) chatbots, and simple LLM-driven applications.
- <strong>Assistant:</strong>Rapid setup via forms; attach knowledge bases, files, and tools for conversational bots.
- <strong>Advanced RAG:</strong>Incorporate tools like retrievers, rerankers, and graph-based retrieval for high-accuracy Q&A on custom data.
### <strong>4. Data Connectivity & Integration</strong>- <strong>100+ Data Formats Supported:</strong>TXT, PDF, DOCX, HTML, CSV, MD, JSON, XML, SQL, and more.
- <strong>Vector Database Integration:</strong>Built-in support for Pinecone, ChromaDB, Weaviate, Milvus, and others.
- <strong>API, SDK, and Embedding:</strong>Expose flows via REST API, Python/Typescript SDKs, or web-embeddable chat widgets.
### <strong>5. Observability & Monitoring</strong>- <strong>Execution Tracing:</strong>Visualize step-by-step execution and data flow for debugging and optimization.
- <strong>Analytics & Metrics:</strong>Track performance, token usage, costs, and other metrics.
- <strong>External Monitoring:</strong>Integrate with observability platforms such as Prometheus and OpenTelemetry.

### <strong>6. Human-in-the-Loop (HITL)</strong>- <strong>Task Review:</strong>Insert checkpoints that pause execution for human input, review, or approval. These are stateful and can survive application restarts.
- <strong>Permission Controls:</strong>Require human approval before executing sensitive actions, similar to human supervision in autonomous systems.

### <strong>7. Security & Enterprise Readiness</strong>- <strong>RBAC & SSO:</strong>Fine-grained role-based access control, Single Sign-On for enterprise deployments.
- <strong>Credential Management:</strong>Encrypted storage for API keys and secrets.
- <strong>Horizontal Scalability:</strong>Message queues and worker-based architecture for scaling flows across clusters or cloud environments.

### <strong>8. Extensibility</strong>- <strong>Custom Nodes:</strong>Implement and add your own logic, models, or integrations.
- <strong>Marketplace/Community Components:</strong>Share and reuse nodes and flow templates.
## <strong>How Flowise is Used</strong>### <strong>Building AI Agents Visually</strong>Users construct LLM-powered workflows by visually linking modular nodes:
- <strong>No/Low-Code:</strong>Build flows visually, configure nodes for models, memory, tools, and logic.
- <strong>Scale from Simple to Advanced:</strong>Rapid prototyping of chatbots, then expansion to multi-agent or autonomous orchestration.

#### <strong>RAG (Retrieval-Augmented Generation) Integration</strong>- <strong>Ingest Custom Data:</strong>Drag in data source nodes for PDFs, DOCX, or websites.
- <strong>Index and Retrieve:</strong>Connect to vector database nodes for efficient retrieval.
- <strong>LLM Node:</strong>Attach a GPT-4, Claude, or local model node for generation.
- <strong>Memory Node:</strong>Add context retention for multi-turn conversations.

#### <strong>Workflow Creation Steps</strong>1. <strong>Install Flowise:</strong>```bash
   npm install -g flowise
   npx flowise start
   ```
   - Or register for [Flowise Cloud](https://cloud.flowiseai.com/signin).

2. **Create New Flow:**- Access dashboard at `http://localhost:3000` or cloud.
   - Choose Assistant, Chatflow, or Agentflow.
   - Drag and connect nodes to define workflow logic.

3. **Configure Nodes:**- Set up LLMs (OpenAI, Ollama, etc.).
   - Integrate retrievers, databases, and memory.
   - Use advanced prompts and few-shot templates.

4. **Test and Debug:**- Use built-in chat window for live testing.
   - Trace execution, inspect outputs, and profile performance.

5. **Deploy:**- Use REST API, SDK, embed chat widget, or share via public URL.
## **Use Cases & Real-World Examples**### **Enterprise Chatbots & Assistants**- **Customer Support:**Automate FAQ responses, resolve tickets, escalate complex issues.
- **Internal Knowledge Base:**Employees retrieve company policies, technical docs, SOPs via conversational interface.

### **Multi-Agent AI Systems**- **Research Teams:**Supervisor agent delegates information gathering to multiple workers, each specializing in sources or analysis.
- **AI Teams:**Orchestrate retrieval, summarization, analysis, and reporting across agent hierarchy.

### **Embedded AI in SaaS Products**- **InsightSoftware:**Enhanced embedded analytics with AI-driven conversational insights.
- **UneeQ Digital Humans:**Streamlined deployment of digital avatars with advanced conversational AI.

### **Custom Integrations & Automation**- **Project Management:**Automate creation of Notion tasks directly from Slack using LLM-driven bots.
- **Multi-Modal Chatbots:**Blend text and image processing in a single conversational flow.

### **Education & Personalization**- **Persona Bots:**Emulate specific teaching or mentoring styles.
- **Translation and Multilingual Bots:**Deploy LLMs with prompt templates for rapid language adaptation.

### **Developer Prototyping & Community**- **Rapid Prototyping:**Drag-and-drop agent creation for hackathons, demos, and production pilots.
- **Open Source Collaboration:**Active GitHub and Discord communities for sharing flows and troubleshooting.
## **Key Advantages: Why Use Flowise?**| Feature             | Flowise Benefit                                             |
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
## **Technical Architecture & Integrations**### **Visual Builders**- **Assistant:**Easiest, form-based, rapid chatbot creation.
- **Chatflow:**Node-based, flexible flows for single-agent systems.
- **Agentflow (V2):**Advanced orchestration, supports explicit workflow design, multi-agent collaboration, loops, branching, and human-in-the-loop.
### **Data Formats Supported**- **Textual:**TXT, PDF, DOCX, HTML, MD, CSV, JSON, XML, SQL.
- **Multimedia:**Image nodes for multimodal flows.

### **LLM, Tool, and Memory Integrations**- **LLMs:**OpenAI (GPT-3/4), Ollama (local models), Claude, Llama2, and more.
- **Vector DBs:**Pinecone, ChromaDB, Weaviate, Milvus, and others.
- **Memory:**Buffer, windowed, summary, and custom implementations for conversational context.
- **APIs/SDKs:**REST, Python, Typescript; custom tool integration possible.

### **Security & Scalability**- **RBAC/SSO:**Enterprise-grade access controls.
- **Encrypted Credentials:**Secure API key and secret storage.
- **Horizontal Scaling:**Message queue and worker model for distributed deployments.
## **Getting Started: Installation & First Steps**### **Installation**- **Local/Self-Hosted:**```bash
  npm install -g flowise
  npx flowise start
  ```
  - Requires Node.js. Dashboard at `http://localhost:3000`.

- <strong>Cloud Version:</strong>- [Register for Flowise Cloud](https://cloud.flowiseai.com/signin) for instant setup.

### <strong>First Flow</strong>- <strong>Assistant:</strong>Fill out form, attach tools and files for simple chatbot.
- <strong>Chatflow/Agentflow:</strong>Use canvas to build node-based flows, connect LLMs, retrievers, memory, and tools.
- <strong>Test & Debug:</strong>Use integrated chat window and execution tracing.

### <strong>Deployment</strong>- <strong>Embed:</strong>Add chat widget to your site.
- <strong>API/SDK:</strong>Integrate with REST, Python, or Typescript SDKs.
- <strong>Public Link:</strong>Share bots with a URL.

### <strong>Community & Support</strong>- <strong>Docs:</strong>[https://docs.flowiseai.com](https://docs.flowiseai.com)
- <strong>GitHub:</strong>[https://github.com/FlowiseAI/Flowise](https://github.com/FlowiseAI/Flowise)
- <strong>Discord:</strong>[https://discord.gg/jbaHfsRVBW](https://discord.gg/jbaHfsRVBW)
- <strong>YouTube Tutorials:</strong>[Complete Flowise v3 Tutorial](https://www.youtube.com/watch?v=riXpu1tHzl0)

## <strong>Glossary: Related Terms</strong>- <strong>LLM (Large Language Model):</strong>Deep neural networks trained on massive text data, enabling generation and comprehension of human language.
- <strong>RAG (Retrieval-Augmented Generation):</strong>LLM technique that retrieves relevant context from external sources to improve output accuracy.
- <strong>Agentic Systems:</strong>Architectures with multiple autonomous AI agents collaborating or competing to solve tasks.
- <strong>Vector Database:</strong>Specialized data stores (e.g., Pinecone, ChromaDB) for high-speed similarity search of embeddings.
- <strong>Human-in-the-Loop (HITL):</strong>System design pattern where humans review, approve, or correct automated AI outputs.
- <strong>Chat Window:</strong>UI component for interacting with bots and testing flows in Flowise.
- <strong>API/SDK:</strong>Developer tools for integrating Flowise bots into external applications.
- <strong>Few-shot Learning:</strong>Method where LLMs are guided with a handful of input-output examples within prompts.
- <strong>Open Source:</strong>Software with public, modifiable source code, fostering community contribution.

<strong>Extended Glossary:</strong>- [Comprehensive LLM Glossary](https://main--dasarpai.netlify.app/dsblog/Comprehensive-Glossary-of-LLM/#what-is-flowiseai)

## <strong>Links, Community & Further Resources</strong>- <strong>Official Website:</strong>[https://flowiseai.com](https://flowiseai.com/)
- <strong>Documentation:</strong>[https://docs.flowiseai.com](https://docs.flowiseai.com)
- <strong>GitHub Repo:</strong>[https://github.com/FlowiseAI/Flowise](https://github.com/FlowiseAI/Flowise)
- <strong>YouTube Tutorial:</strong>[How to Build an AI Document Chatbot](https://www.youtube.com/watch?v=riXpu1tHzl0)
- <strong>Discord Community:</strong>[https://discord.gg/jbaHfsRVBW](https://discord.gg/jbaHfsRVBW)
- <strong>Marketplace:</strong>[Flowise Community Flows & Templates](https://cloud.flowiseai.com/marketplace)
- <strong>Third-Party Glossary:</strong>[Comprehensive Glossary of LLM](https://main--dasarpai.netlify.app/dsblog/Comprehensive-Glossary-of-LLM/#what-is-flowiseai)

## <strong>Frequently Asked Questions</strong>### <strong>How is Flowise different from n8n, Zapier, or Make.com?</strong>Flowise is tailored for agentic AI workflows, providing native support for LLM orchestration, multi-agent collaboration, RAG, and memory, features not present in general-purpose automation platforms. Flowise is open source, self-hostable, and designed for advanced AI/LLM use cases.

### <strong>Can I use custom LLMs and data?</strong>Yes. Flowise supports over 100 LLMs (including local models via Ollama and open-source options) and ingestion of all common data formats for RAG-based flows.

### <strong>Is Flowise enterprise-ready?</strong>Yes, with RBAC, SSO, encrypted credential management, horizontal scalability, and support for both on-premises and cloud deployments.

### <strong>How do I contribute or get support?</strong>Join the [Discord community](https://discord.gg/jbaHfsRVBW), submit PRs or issues on [GitHub](https://github.com/FlowiseAI/Flowise), and access onboarding guides in the [docs](https://docs.flowiseai.com).

## <strong>User Testimonials</strong>> "Flowise allows us to supercharge our existing embedded analytics platform with built-in AI features that our clients absolutely love."  
> — Terrence Sheflin, Director of Engineering, InsightSoftware

> "With Flowise, we were able to accelerate our internal 'Build your own AI assistants easily & intuitively' initiative. Truly a game-changer in our tech journey."  
> — Iokin Pardo, Senior Director, BTS Digital

> "Flowise has truly changed how we approach AI. It's simple enough to prototype an idea in minutes, yet powerful enough to take all the way to production."  
> — David Micotto, Senior Director of DX & AI, Publicis Groupe

## <strong>Get Started with Flowise</strong>- <strong>Start building:</strong>[Sign up free](https://cloud.flowiseai.com/signin) or [install locally](https://docs.flowiseai.com/getting-started).
- <strong>Join the community:</strong>[Discord](https://discord.gg/jbaHfsRVBW)
- <strong>Explore the code:</strong>[GitHub](https://github.com/FlowiseAI/Flowise)
- <strong>Watch tutorials:</strong>[YouTube](https://www.youtube.com/watch?v=ri
