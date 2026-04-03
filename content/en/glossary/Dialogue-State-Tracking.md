---
title: Dialogue State Tracking
date: 2025-12-19
lastmod: 2026-04-02
translationKey: dialogue-state-tracking
description: Technology that tracks conversation progress as "who wants to do what." A core capability for managing multi-turn dialogues.
keywords:
- Dialogue State Tracking
- DST
- Conversation Flow
- Chatbot
type: glossary
draft: false
url: /en/glossary/dialogue-state-tracking/
category: Chatbot & Conversational AI
---

## What is Dialogue State Tracking?

**Dialogue State Tracking (DST) is the technology by which conversational AI tracks "what stage we're at," "what the user wants," and "what information has been collected" as the conversation progresses.** Using the concept of slots (information units), it organizes multiple pieces of information like "station: Narita," "destination: New York," "departure date: next Monday," and determines whether all information needed to achieve the user's goal is complete.

> **In a nutshell:** It's like a doctor's intake form where "symptoms?", "when did it start?", "medical history?" are filled in one by one. Unfilled items are "information that needs confirmation," and when all items are complete, "diagnosis can be made."

**Key points:**

- **What it does:** Structured system that tracks conversation progress
- **Why it matters:** To understand which information has been collected across multiple turns
- **Who uses it:** Chatbot developers, conversational AI researchers

## Why it matters

Without dialogue state tracking, the AI must determine "what is the user saying?" from scratch each turn. This increases misrecognition risk and creates unnatural conversations like asking the same question twice.

With dialogue state tracking, previously collected information is recognized, allowing conversation management like "I already asked about departure location, so now I'll ask about destination." When users reference earlier turns ("about that XX I mentioned before"), the system can search that context and respond accurately.

## How it works

Dialogue state tracking requires multiple components. First, **user goal extraction** (goal tracking) recognizes what the user wants to do, like "airline ticket booking" or "restaurant search." Second, **slot tracking** records information needed to complete the task (departure location, destination, date, etc.).

Third, **conversation status judgment** determines "which slots are filled?" and "which are unclear?" For example, from "I want to go to New York," the system confirms "destination = New York" but recognizes missing information: "when?" and "from where?"

Implementation typically manages each slot with 1-5 confidence levels. If a user clearly states "from Narita," it gets 100% confidence. If they say "somewhere near Tokyo," it gets 50% confidence. When confidence is low, the system inserts confirmation questions like "Did you mean Narita, Tokyo?" to improve accuracy.

## Real-world use cases

**Hotel booking chatbot**

When a user says "next week, preferably window side, smoking-allowed room," DST tracks: "Check-in: next week (confidence 80%, specific date needed)", "window side: Yes (95%)", "smoking: Yes (95%)", "check-out: uncollected". It then prioritizes questions: "When do you check in?" and "When do you check out?"

**Financial product consultation chatbot**

A customer says "I want to save money until I'm 60." DST tracks: "Goal: wealth building (100%)", "timeframe: now to age 60 (95%)", "current savings: uncollected", "risk tolerance: uncollected". It prioritizes the most critical missing information and asks "what's your current savings level?"

**Medical consultation chatbot**

When a patient says "I have a headache and fever," DST organizes: "symptoms: headache, fever", "onset: unconfirmed", "severity: unconfirmed", "other symptoms: unconfirmed". Medically important information is confirmed first: "How long have you had it?" "What's your temperature?"

## Benefits and considerations

Benefits of dialogue state tracking include improved conversation efficiency and accuracy. Systematically tracking needed information eliminates redundant questions, reducing user stress. Managing slot confidence allows insertion of confirmation questions for unclear information, improving final accuracy.

A key consideration is the **difficulty of defining slots**. Applying uniform slot structure across all tasks is impractical—each business requires different slot design. Managing situations where multiple slot values depend on each other (e.g., "2 adults, 2 children") becomes complex.

Additionally, handling unexpected user input is challenging. If a user suddenly mentions transportation mode ("I'll take the bullet train") that isn't in the slot structure, the system can't utilize that information.

## Related terms

- **[Dialogue Management](Dialogue-Management.md)** — Higher-level layer that determines next response based on state
- **[Dialog Turn](Dialog-Turn.md)** — State updates with each turn
- **[Natural Language Understanding](Natural-Language-Understanding.md)** — Extraction preprocessing before state tracking
- **[Intent Recognition](Intent-Recognition.md)** — Recognizing user objectives
- **[Slot Filling](Slot-Filling.md)** — Implementation pattern of dialogue state tracking

## Frequently asked questions

**Q: How do I judge slot value confidence?**

A: Multiple methods exist. One: "Did the user explicitly state it?" ("tomorrow 9am" = 100%). Two: "Did AI infer from words?" ("early morning" = 70%). Three: "Did multiple sources confirm?" (AI extraction matching user confirmation = 95%). Set judgment rules accordingly.

**Q: What if slot values change later?**

A: Establish confirmation phases. Before task completion, present all slot values: "So, departure is next Monday, destination is New York, smoking room... correct?" This gives opportunity to modify.

**Q: What if multiple slot values depend on each other?**

A: Codify dependencies as rules. For example: "If children present, confirm crib availability." Use if-then rules so dependent slots are automatically confirmed. However, complex dependencies become difficult to manage, so simple task design is important.
