---
title: "AI Email Response Composer"
description: "AI Email Response Composer (AI Answer Composer) is a feature that analyzes emails and inquiry forms from customers and automatically generates reply drafts. It creates accurate responses based on FlowHunt's knowledge base."
weight: 30
---

**AI Email Response Composer (AI Answer Composer)** is a feature that analyzes emails and inquiry forms from customers and automatically generates reply drafts.

## Key Features

| Feature | Description |
|---------|-------------|
| **Intent Analysis** | Automatically identifies the intent of questions from customer emails |
| **RAG Technology** | Searches for relevant information from the knowledge base to generate responses |
| **Multiple Question Support** | Handles cases where a single email contains multiple questions |
| **AI Answer Assist Integration** | Generated drafts can be directly refined using AI Answer Assist |

## AI Providers

AI Email Response Composer is **only compatible with FlowHunt** (OpenAI is not supported).

By training FlowHunt's knowledge sources (Schedules, Q&A, Documents), it generates accurate reply drafts based on your company's FAQ and manuals.

## Workflow

```
Incoming customer email
       ↓
AI Answer Composer (automatic draft generation)
       ↓
AI Answer Improver (text refinement)
       ↓
Operator review and editing
       ↓
     Send
```

## Contents of This Section

- [About AI Email Response Composer](/docs/email-composer/about-ai-answer-composer/)
- [Setup Method](/docs/email-composer/setup/)
- [Knowledge Base Preparation](/docs/email-composer/knowledge-base/)
- [Available Plans](/docs/email-composer/available-plans/)

## Related Information

- [AI Fundamentals](/docs/ai-fundamentals/) - Differences and use cases of the three AI features
- [AI Learning Methods](/docs/ai-fundamentals/ai-learning/) - Knowledge source configuration
- [About RAG Technology](/docs/ai-fundamentals/rag-technology/) - The mechanism that enables high-precision responses
- [AI Provider Setup](/docs/ai-fundamentals/ai-provider-setup/) - FlowHunt configuration method
- [AI Answer Assist](/docs/ai-answer-assist/) - Refining generated drafts
