---
title: Quick Replies
date: 2025-12-19
lastmod: 2026-04-02
translationKey: quick-replies
description: Quick replies are temporary buttons displayed in chatbots or messaging apps that let users select from predefined options, reducing text input needs and improving conversation flow.
keywords:
- quick replies
- chatbot
- chat interface
- user input
- messaging platforms
category: Data & Analytics
type: glossary
draft: false
url: /en/glossary/Quick-Replies/
---

## What are Quick Replies?

**Quick replies are temporary buttons displayed in chatbots or messaging apps that let users select from predefined options, reducing text input needs—a UI element that streamlines conversation.** For example, in response to "What do you need?" the bot displays "[Order Tracking] [Product Info] [Cancel]" buttons. When users tap a button, it disappears and the selection is sent to the bot. This simplicity and temporary nature keep conversations clean.

> **In a nutshell:** Like "What size coffee?" with buttons "[Small] [Medium] [Large]" to tap instead of typing.

**Key points:**

- **What it does:** Makes it easy for users to select from options.
- **Why it's needed:** It's easier than typing, the bot understands intent accurately, and conversations flow smoothly.
- **Who uses it:** Facebook Messenger, WhatsApp, Slack, LINE—all companies operating chatbots.

## Why it matters

One reason chatbots became popular is reducing user input burden. With quick replies, instead of typing "cancel," users just tap "[Cancel]." This reduces user stress and increases chatbot usage. For the bot, user intent transfers accurately, improving [Quality Assurance](Quality-Assurance--QA-.md) precision.

## How it works

Quick reply operation is very simple. When the bot sends a question, it simultaneously specifies multiple "response options" in JSON format. Chat platforms (Facebook, WhatsApp, etc.) display these as buttons at the screen bottom. When users tap a button, that button's payload (internal value) is sent to the bot. Simultaneously, buttons disappear from the user's screen and the conversation continues.

Platform limitations apply. Facebook Messenger allows up to 13 buttons, WhatsApp up to 3, etc., determined by space constraints. Each button text typically limits to 20-25 characters.

## Real-world use cases

**Customer support routing**
The question "What do you need?" displays "[Order Status] [Product Info] [Complaint] [Other]" to route users to appropriate flows.

**Appointment system smoothing**
The question "What time do you arrive?" displays "[10:00] [11:00] [12:00]" time slots simplifying booking.

**Survey collection**
The question "Satisfaction level?" displays "[Very Satisfied] [Satisfied] [Neutral] [Dissatisfied] [Very Dissatisfied]" collecting responses smoothly.

## Benefits and considerations

The main benefit is extremely low user input burden, greatly increasing chatbot usage. The bot accurately understands user intent, and success rates measured by [Quality Monitoring](Quality-Monitoring.md) improve. The consideration is handling only predefined options—if users have "other" needs, quick replies alone can't address them. Therefore, text input fallback is necessary.

## Related terms

- **[Quality Assurance (QA)](Quality-Assurance--QA-.md)** — Ensures chatbot quality
- **[Quality Score](Quality-Score.md)** — Evaluates bot response quality
- **[Queue Management](Queue-Management.md)** — Chatbot inquiry processing

## Frequently asked questions

**Q: Are there button count limits?**
A: Yes, it varies by platform. Facebook allows up to 13, WhatsApp up to 3. For more, use cascading across multiple steps.

**Q: Is text input forbidden?**
A: No. Users can always type. Quick replies just provide convenient options.

**Q: What options should we provide?**
A: Select the top 5-8 most frequently selected options. Use log analysis to identify "most common inquiries" and create buttons for those.
