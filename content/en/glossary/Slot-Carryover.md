---
title: Slot Carryover
date: 2025-12-19
lastmod: 2026-04-02
translationKey: slot-carryover
description: A chatbot capability where previously extracted information (slots) from earlier conversation turns is remembered and reused in subsequent turns.
keywords:
- slot carryover
- ai chatbot
- dialogue system
- dialogue state tracking
- context management
category: AI & Machine Learning
type: glossary
draft: false
url: /en/glossary/Slot-Carryover/
---

## What is Slot Carryover?

**Slot carryover is a chatbot capability where information extracted from earlier conversation turns (slots) is remembered and reused in subsequent turns.** When a user initially says "Find flights to Paris," then later says "Also find hotels there," the bot understands "there" means "Paris" and reuses the previously extracted "Paris" information for hotel search.

> **In a nutshell:** Like humans remembering conversation flow, chatbots "remember what you said earlier" and use it.

**Key points:**

- **What it does:** Reuses parameters extracted from past turns in new turns
- **Why it's needed:** Saves users from repeatedly entering the same information
- **Who uses it:** Travel booking bots, financial service chatbots, customer support

## Why it matters

Without slot carryover, user frustration builds. Saying "Paris flights" then "Find hotels" only to hear "Which city?" creates frustration. With slot carryover, bots automatically remember prior information, asking more naturally: "How many nights in Paris?" As a result, conversations flow smoothly and completion requires far fewer turns.

## How it works

The key is "Dialogue State Tracking (DST)." Each turn, the bot: ①determines if past slot values remain valid, ②updates if new information arrives, ③selects slots required for current intent.

Machine learning approaches use Transformer models understanding entire dialogue context, determining which slots to carry forward. In complex multi-domain dialogue (switching from weather to flight booking), slot names differ, so embedding representations learn semantic similarities between slots.

## Real-world use cases

**Travel booking**
User says "flights to Tokyo," bot extracts destination. User then says "5-star hotels there"—bot knows "there" refers to Tokyo and searches accordingly.

**Customer support**
Customer identifies their issue in first turn; bot remembers the context for subsequent questions without repeating problem descriptions.

**Financial services**
Customer provides account information in initial turn; bot carries forward for transaction processing without requesting redundant information.

## Benefits and considerations

The biggest benefit is **improved user experience** and **dialogue efficiency**. However, **error propagation** is a complex challenge. Initial turn extraction errors carry forward to later turns.

Additionally, **privacy is a concern**. Storing personal information (addresses, phone numbers) in slot memory creates privacy risks.

## Related terms

- **[Slot Filling](Slot-Filling.md)** — Process of extracting slot values each turn
- **[Dialogue State Tracking](Dialog-State-Tracking.md)** — Foundational technology for slot carryover
- **[Intent](Intent.md)** — User goals; intents can change across turns
- **[Multi-Domain Dialogue](Multi-Domain-Dialog.md)** — Area where slot carryover particularly matters
- **[Natural Language Understanding](NLU.md)** — Foundational technology for slot extraction

## Frequently asked questions

**Q: How long should slots be retained?**
A: Until session end or explicit reset instruction, typically.

**Q: Can slots map across multiple domains?**
A: Embedding technology enables this. Sufficient training data improves accuracy.
