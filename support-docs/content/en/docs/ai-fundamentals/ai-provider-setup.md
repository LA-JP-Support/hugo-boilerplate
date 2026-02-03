---
title: "AI Provider Setup (FlowHunt / OpenAI)"
date: 2026-02-03
lastmod: 2026-02-03
draft: false
translationKey: "ai-provider-setup"
description: "Learn about the differences between AI providers (FlowHunt and OpenAI) used in SmartWeb's AI features and how to set them up. AI Answer Composer supports FlowHunt only, while AI Answer Improver supports both FlowHunt and OpenAI."
keywords: ["FlowHunt", "OpenAI", "AI provider", "setup", "API", "LiveAgent"]
category: "ai-fundamentals"
---

SmartWeb's AI features can use either **FlowHunt** or **OpenAI** as AI providers. However, the supported providers differ depending on the feature.

## AI Provider Compatibility Chart

| Feature | FlowHunt | OpenAI | Notes |
|---------|:--------:|:------:|-------|
| **AI Chatbot** | ✓ | - | FlowHunt only |
| **AI Email Response Creation** (AI Answer Composer) | ✓ | - | FlowHunt only |
| **AI Answer Assistant** (AI Answer Improver) | ✓ | ✓ | Both supported |

## FlowHunt vs OpenAI Differences

### FlowHunt

| Item | Content |
|------|---------|
| **Developer** | Quality Unit (same as LiveAgent developer) |
| **Knowledge Base** | Integrated (RAG supported) |
| **Data Security** | No external leak risk with same company product integration |
| **Supported Features** | All AI features (Chatbot, Composer, Improver) |
| **Pricing** | Included in SmartWeb plan |

### OpenAI

| Item | Content |
|------|---------|
| **Developer** | OpenAI Inc. |
| **Knowledge Base** | Not integrated (processes input text only) |
| **Data Security** | Complies with OpenAI's policies |
| **Supported Features** | AI Answer Assistant (Improver) only |
| **Pricing** | Direct contract with OpenAI (separate API usage fees) |

## Recommended Provider

### Why FlowHunt is Recommended

1. **Data Security**: Same developer as LiveAgent, eliminating risk of external data leaks
2. **Knowledge Base Integration**: RAG technology enables accurate responses based on your company's FAQ and manuals
3. **Seamless Integration**: Smooth coordination between AI Answer Composer and AI Answer Improver
4. **Cost Efficiency**: Included in SmartWeb plan, no additional API contracts needed

### When to Choose OpenAI

- When using only AI Answer Assistant (Improver)
- When already using OpenAI API with other systems
- When you want to specify particular OpenAI models (GPT-4, etc.)

## FlowHunt Setup Procedure

### 1. Create a Flow in FlowHunt

1. Log in to FlowHunt
2. Click "Create New Flow"
3. Select template "**LiveAgent AI Answer Assistant (Composer & Improver)**"
4. Set flow name and save

### 2. Add Knowledge Sources

Connect knowledge sources to the flow:

| Knowledge Source | Purpose |
|------------------|---------|
| **Schedules** | Regular crawling of website URLs |
| **Q&A** | Manually register frequently asked questions and answers |
| **Documents** | Upload PDF, Word, Excel, etc. |

### 3. Register API Key in LiveAgent

1. Get API key from "API Keys" in FlowHunt
2. LiveAgent admin panel → "Settings" → "AI"
3. Enter key in "FlowHunt API Key"
4. Select the flow to use

### 4. Test Operation

- Confirm AI Answer Composer icon appears in ticket screen
- Create test reply and confirm AI Answer Improver works

## OpenAI Setup Procedure

### 1. Obtain OpenAI API Key

1. Log in to [OpenAI Platform](https://platform.openai.com/)
2. Create new key from "API Keys"
3. Store key in secure location

### 2. Register API Key in LiveAgent

1. LiveAgent admin panel → "Settings" → "AI"
2. Enter key in "OpenAI API Key"
3. Select model to use (GPT-4, GPT-3.5-turbo, etc.)

### 3. Usage Notes

- OpenAI integration supports **AI Answer Assistant (Improver) only**
- AI Chatbot and AI Email Response Creation (Composer) do not work with OpenAI
- API usage fees are billed directly by OpenAI

## Using Both Simultaneously

It's possible to configure both FlowHunt and OpenAI:

```
AI Chatbot ──────────────────→ FlowHunt
AI Email Response Creation (Composer) → FlowHunt
AI Answer Assistant (Improver) ────→ FlowHunt or OpenAI (selectable)
```

For AI Answer Assistant, you can choose which provider to use at the time of usage.

## Troubleshooting

### When FlowHunt Doesn't Work

- Confirm API key is entered correctly
- Confirm flow is in "Published" state
- Confirm knowledge sources are properly connected

### When OpenAI Doesn't Work

- Confirm API key is valid (check in OpenAI Dashboard)
- Check if rate limit has been reached
- Confirm billing information is set up correctly

## Related Information

- [About FlowHunt](/ja/support/ai-fundamentals/flowhunt-about/) - FlowHunt overview
- [AI Learning Methods](/ja/support/ai-fundamentals/ai-learning/) - Knowledge source configuration
- [Security and Data Protection](/ja/support/ai-fundamentals/ai-security-data/) - Data protection policies
