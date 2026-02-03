---
title: "Fundamentals of AI Features"
date: 2026-02-03
lastmod: 2026-02-03
draft: false
translationKey: "ai-fundamentals"
description: "Learn about the fundamentals, learning methods, and security of SmartWeb's AI features (AI Chatbot, AI Response Assistant, AI Email Reply Generation)."
keywords: ["AI", "FlowHunt", "LiveAgent", "RAG", "learning", "security", "fundamentals"]
weight: 15
---

SmartWeb is an AI customer support service that fully integrates the AI platform "**FlowHunt**" with the ticketing system "**LiveAgent**". This section explains the fundamental knowledge common to all AI features.

## SmartWeb's 3 AI Features

| Feature | Target | Purpose | AI Provider |
|---------|--------|---------|-------------|
| **AI Chatbot** | Customers | 24/7 automated responses | FlowHunt |
| **AI Email Reply Generation** | Operators | Automatic reply draft generation | FlowHunt only |
| **AI Response Assistant** | Operators | Text improvement and adjustment | FlowHunt or OpenAI |

## Contents of This Section

### AI Feature Overview
- [What are SmartWeb's AI Features](/en/support/ai-fundamentals/ai-features-overview/) - Differences and use cases of the 3 AI features

### Core Technology
- [About FlowHunt](/en/support/ai-fundamentals/flowhunt-about/) - Introduction to the no-code AI platform
- [AI Provider Configuration](/en/support/ai-fundamentals/ai-provider-setup/) - Differences and setup methods for FlowHunt and OpenAI
- [About RAG Technology](/en/support/ai-fundamentals/rag-technology/) - Technology that enables high-precision responses

### Knowledge and Learning
- [AI Learning Methods](/en/support/ai-fundamentals/ai-learning/) - Knowledge sources, content formats, and configuration guide

### Security
- [Security and Data Protection](/en/support/ai-fundamentals/ai-security-data/) - Data protection and GDPR compliance

## Knowledge Base Sharing

AI Chatbot and AI Email Reply Generation **share the same knowledge base**.

```
┌─────────────────────────────────────────┐
│         FlowHunt Knowledge Sources       │
│  ┌─────────┬─────────┬─────────┐        │
│  │Schedules│   Q&A   │Documents│        │
│  │(Web     │(Questions│(File    │        │
│  │crawling)│& Answers)│Upload)  │        │
│  │         │         │         │        │
│  └────┬────┴────┬────┴────┬────┘        │
│       │         │         │             │
│       └─────────┼─────────┘             │
│                 ▼                       │
│         RAG (Retrieval Augmented        │
│              Generation)                │
└─────────────────┬───────────────────────┘
                  │
     ┌────────────┼────────────┐
     ▼            ▼            ▼
┌─────────┐ ┌──────────┐ ┌──────────┐
│AI Chat  │ │AI Email  │ │AI Response│
│bot      │ │Reply     │ │Assistant │
│         │ │Generation│ │(Improver)│
│         │ │(Composer)│ │          │
└─────────┘ └──────────┘ └──────────┘
     ▼            ▼            ▼
  Customers   Operators    Operators
 (Automatic) (Send after  (Send after
             review)       review)
```

**Benefits**:
- Support multiple channels with single setup
- Ensure consistency in responses
- Streamline maintenance
