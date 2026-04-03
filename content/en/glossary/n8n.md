---
title: n8n
lastmod: 2026-04-02
date: '2025-12-19'
translationKey: n8n
description: n8n is a node-based workflow automation platform offering AI model integration, complex business process orchestration, and self-hosting options.
keywords:
- n8n
- Workflow Automation
- AI Integration
- Nodes
- Self-Hosting
category: AI & Machine Learning
type: glossary
draft: false
url: "/en/glossary/n8n/"
---

## What is n8n?

**n8n** is a node-based workflow automation platform using drag-and-drop interfaces to automate complex business processes. It natively integrates with 500+ apps and services and supports custom code. Unlike closed-source alternatives like Zapier, n8n enables self-hosting for true data privacy and complete control.

> **In a nutshell:** "An automation platform that visually connects different tools and apps so they work together automatically and intelligently."

**Key points:**

- **What it does:** Design workflows through GUI, automatically transferring, transforming, and processing data between multiple apps and APIs
- **Why it matters:** Eliminates repetitive manual work, reduces errors, dramatically improves team productivity
- **Who uses it:** Marketing teams, sales teams, IT departments, DevOps engineers, data scientists, and entrepreneurs

## Why It Matters

Many business processes span multiple tools. When new customer leads arrive via web form, they need registering in CRM, notifying the sales team, and sending to billing—all automatically. Manual processing is slow, error-prone, and doesn't scale.

Workflow automation tools like n8n let you design this flow once, then run it automatically forever. Teams escape low-value work and focus on strategic tasks. Simultaneously, you achieve process optimization, error reduction, cost savings, and scalability.

## How It Works

n8n operates on two concepts: **nodes** and **workflows**. Nodes represent individual actions (fetch Gmail data, send Slack messages, transform data), while workflows connect nodes to create flows.

For a new customer lead acquisition workflow, a webhook node awaits form submission. When data arrives, validation checks format, [RAG](RAG.md) nodes fetch additional info, CRM nodes register customer data, and Slack nodes notify sales. Conditional branching is possible—execute different processes for different industries, or notify admins on error.

## Real-World Use Cases

**Lead Auto-Routing**
For multiple sales teams, automatically assign leads to appropriate salespeople based on region or industry via CRM and automation.

**AI-Driven Customer Support**
Auto-classify support tickets, set priority, and route to proper teams. Simple issues resolve via [chatbots](Chatbot.md).

**E-commerce Order Auto-Processing**
Detect new orders, check inventory, generate invoices, notify shipping, send customer emails—fully automated, zero manual work.

## Benefits and Considerations

Major advantages include flexibility—integrate with nearly any API, write custom code, and enable unlimited execution in self-hosted mode with complete cost control.

Disadvantages include steep learning curve for complex workflows (steeper than fully no-code alternatives like Zapier). Poor error-handling design causes automation failures. Complex workflow maintenance becomes challenging.

## Related Terms

- **[Workflow Automation](Workflow-Automation.md)** — Automatically executing business processes
- **[API Integration](API-Integration.md)** — Connecting multiple applications to work together
- **[RPA](RPA.md)** — Robotic Process Automation
- **[Zapier](Zapier.md)** — n8n competitor emphasizing no-code
- **[Make (Integromat)](Make.md)** — Scenario-based automation tool

## Frequently Asked Questions

**Q: Does using n8n require development experience?**
A: Simple workflows work with the visual editor alone. Complex custom processing benefits from JavaScript or Python knowledge but isn't required.

**Q: How difficult is self-hosting?**
A: With Docker experience, setup takes about 30 minutes. Basic Linux or cloud knowledge supports long-term server operation.

**Q: How much does n8n cost?**
A: Self-hosted is completely free (server costs only). Cloud version uses pay-as-you-go pricing—small usage is a few hundred yen monthly, large usage around several thousand yen.
