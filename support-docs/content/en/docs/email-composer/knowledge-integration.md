---
title: "Knowledge Base Integration for AI Email Response Composer"
date: 2026-02-03
lastmod: 2026-02-03
draft: false
translationKey: "email-composer-knowledge"
description: "AI Email Response Composer can utilize knowledge bases such as product information, FAQs, and response manuals that have been pre-trained in AI chatbots. The same information can be shared for both chat and email support."
keywords: ["AI Email Response Composer", "Knowledge Base", "Knowledge Integration", "Learning Information", "FlowHunt"]
category: "email-composer"
---

## Knowledge Base Integration

AI Email Response Composer (AI Answer Composer) can **utilize knowledge bases such as product information, FAQs, and response manuals that have been pre-trained in AI chatbots for email responses as well**.

## Shareable Knowledge Sources

FlowHunt's knowledge source functionality allows you to configure and share various information sources.

### Regular Website Crawling (Schedules)

Regularly crawl specified websites and automatically learn the latest information.

**Use cases:**
- Product information pages
- Help centers
- Blog articles

### Q&A

Register frequently asked questions and their answers for AI to reference during response creation.

**Use cases:**
- Customer support FAQ
- Technical questions and answers
- Pricing-related Q&A

### Documents

Train AI with documents such as PDFs and Word files.

**Use cases:**
- Product manuals
- Specifications
- Internal knowledge

## Benefits

### Centralized Information Management

Information learned once is shared between both chatbots and email support, eliminating the need for duplicate information management.

### Cross-Channel Consistency

Efficiently achieve consistent, high-quality customer support across all channels.

### Reduced Operational Load

Knowledge updates are completed in one place, minimizing operational overhead.

## Integration Mechanism

```
[Knowledge Base]
    ↓ Learning
[FlowHunt]
    ↓ Integration
[AI Chatbot] ← Customer (Chat)
    ↓ References same knowledge
[AI Email Response Composer] ← Customer (Email/Form)
```

## Important Notes

### Knowledge Quality

AI response quality heavily depends on the quality of the knowledge it learns. Ensure accurate and up-to-date information is maintained.

### Update Reflection Timing

Website crawling is executed at the configured frequency. If you need immediate reflection of changes, manually execute crawling or update directly through Q&A or documents.

## Related Information

For knowledge base configuration methods and crawling frequency settings, please contact our support team.