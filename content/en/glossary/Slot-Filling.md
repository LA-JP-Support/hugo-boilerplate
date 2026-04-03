---
title: Slot Filling
date: 2025-12-19
lastmod: 2026-04-02
translationKey: slot-filling
description: A process where conversational AI automatically extracts necessary parameters from user queries and systematically collects information required to complete tasks.
keywords:
- slot filling
- conversational AI
- chatbot
- entity extraction
- intent recognition
category: AI & Machine Learning
type: glossary
draft: false
url: "/en/glossary/slot-filling/"
---

## What is Slot Filling?

**Slot filling is a process where conversational AI automatically extracts necessary parameters (slots) from user queries and systematically collects information required to complete tasks.** For example, a flight booking bot extracts "departure city: New York," "destination: London," and "date: July 20" from the input "July 20, from New York to London." If information is missing, the bot asks clarifying questions to fill the gaps.

> **In a nutshell:** A process that "collects" information step-by-step that is necessary for a user's intended task.

**Key points:**

- **What it does:** Extracts necessary parameters from user input and fills in missing information.
- **Why it's needed:** Even if users don't provide all information at once, bots can automatically confirm and collect what's missing.
- **Who uses it:** Reservation bots, order bots, customer support systems.

## Why it matters

Without slot filling, bots can only force users to "provide all required information at once," resulting in a terrible user experience. With slot filling, bots understand "what information is missing" and ask only necessary questions, creating natural conversation.

Slot filling also handles users who provide multiple pieces of information in random order. Instead of rigid progression like "first tell me the destination, then the departure city," the bot flexibly accepts "where to where" in any order.

## How it works

Slot filling proceeds in three main stages.

**Stage 1: Intent Recognition**
The bot determines "what the user wants to do" from their input. For "I want to order pizza," the intent is "pizza order."

**Stage 2: Entity Extraction**
The bot extracts necessary information from input. From "8-inch pepperoni pizza," it recognizes "size: 8-inch" and "type: pepperoni." This uses natural language processing or deep learning models like BERT.

**Stage 3: Slot Confirmation and Filling**
The bot verifies extracted slots and checks if all required fields are complete. If missing, the bot asks, "What size would you like?"

## Real-world use cases

**Pizza ordering bot**
"Give me an 8-inch pepperoni pizza" → Bot asks "What's your address?" "What time should it be delivered?"

**Hotel reservation**
User says "2 nights in Paris" → Bot asks "When do you want to check in?" and collects complete information before booking.

**Customer support**
"My iPhone won't start" → Bot asks "Which iPhone?" "What did you do when it stopped starting?" to understand the situation.

## Benefits and considerations

The benefits are **natural dialogue** and **efficiency**. Users provide information at their own pace while bots fill in gaps.

Important considerations include **excessive prompting**, which is problematic. Asking for the same information repeatedly frustrates users. Also, proceeding without a **confirmation step** can lead to misunderstandings and incorrect execution.

## Related terms

- **[Intent Recognition](Intent-Recognition.md)** — The first step of slot filling.
- **[Entity Extraction](Entity-Extraction.md)** — How slot values are extracted.
- **[Natural Language Understanding](NLU.md)** — The underlying technology.
- **[Slot Carryover](Slot-Carryover.md)** — Inheriting slot values across multiple turns.
- **[Dialog Management](Dialog-Management.md)** — The higher-level concept of slot filling.

## Frequently asked questions

**Q: Does the bot continue until all required slots are filled?**
A: It depends on configuration. Optional slots can be set as skippable.

**Q: Is it okay to execute without user confirmation?**
A: Confirmation is essential for important operations. Always confirm with the user "Is this correct?" before taking action.
