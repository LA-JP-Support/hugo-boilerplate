---
title: Webhook
date: 2025-12-19
lastmod: 2026-04-02
description: A callback mechanism that automatically sends HTTP requests to another system when events occur, enabling real-time data synchronization.
translationKey: webhook
category: Cloud & Infrastructure
type: glossary
draft: false
url: /en/glossary/webhook/
keywords:
  - webhook
  - HTTP callback
  - event-driven
  - real-time notification
  - API integration
---

## What is a Webhook?

**A webhook is a mechanism that automatically sends an HTTP request from one system to another when a specific event occurs.** Traditional APIs require the client to actively ask "give me information," but webhooks are push-type communication where the server automatically notifies "something happened." This enables multiple systems to exchange information in real-time.

> **In a nutshell:** It's like LINE notifications from friends—when something happens, the system automatically tells you. You don't need to keep asking "did my friend message me?"—they notify you directly.

**Key points:**

- **What it does:** Automatically send HTTP requests on event occurrence and enable system coordination
- **Why it matters:** Eliminate polling waste and exchange information in real-time
- **Who uses it:** Companies and developers coordinating multiple systems like e-commerce, payment systems, CRM, marketing automation

## Why it matters

Traditional API integration relied on "polling"—systems repeatedly requesting "anything happened yet?" whenever information was needed. This generated frequent unnecessary requests, heavily burdening servers. Webhooks notify only when events occur, eliminating wasted requests and dramatically reducing server load.

Additionally, API polling inevitably creates seconds-to-minutes delays, but webhooks enable near real-time notification. When order management and shipping systems aren't synchronized, customers might receive products twice. With webhooks, shipping systems receive notifications simultaneously with order completion, preventing such errors.

Modern digital business combines multiple cloud services as standard. Coordinating these systems in real-time requires webhooks as essential technology. Implementation costs are low with high scalability, making them widely adopted from startups to enterprises.

## How it works

Webhooks operate through five steps: trigger, configuration retrieval, payload construction, transmission, and reception processing.

First, an "event" like registration, purchase, or data update occurs in the source application. If this event matches preconfigured targets, triggers activate. Next, retrieve webhook configuration associated with this event, containing destination URL, [API](API.md) key, payload format, etc.

When constructing the payload (data sent), pack event type, timestamp, affected object IDs into JSON format. For security, generate HMAC signature using shared secret and include in request headers, enabling the receiver to verify genuine system transmission.

Then send HTTP POST request containing constructed payload and signature to the configured URL (endpoint). The receiving application receives the request, verifies the signature, and executes processing based on event content. Finally, respond with HTTP status code (200=success, 400=error, etc.). The source application reviews this response to determine delivery success or failure, resending after seconds to minutes if failed.

For example, when order completes in payment platforms, webhooks automatically execute to shipping services. Order number, customer information, and shipping address arrive in the payload, and shipping systems automatically create shipping labels.

## Real-world use cases

**E-commerce order flow** – The moment a user completes payment in an online store, the payment gateway sends a webhook to inventory management. Inventory system extracts product ID and quantity from received data and decreases inventory. Simultaneously, another webhook reaches email system, automatically sending shipping notification emails to customers. Multiple downstream systems chain together, completing order processing with minimal human involvement.

**Slack notification automation** – When important tasks complete in project management tools, webhook events trigger to Slack. Messages like "【Task Complete】Testing finished" auto-post in designated Slack channels. Team members viewing Slack constantly learn of important developments in real-time.

**Security monitoring and alerts** – When security systems detect unauthorized login attempts or data access, webhooks simultaneously notify multiple systems. Ticket systems automatically create security alert tickets, Slack receives warning messages, and admin emails receive severity-categorized alerts, enabling swift response.

## Benefits and considerations

Webhooks' greatest benefits are real-time capability and cost efficiency. No need to repeatedly ask "anything happening now?" like polling does; notifications arrive only when events occur, dramatically reducing network bandwidth and server CPU consumption. Microservices [architecture](Architecture.md) achieves loosely coupled coordination between multiple services, offering excellent scalability.

However, considerations exist. If receiver endpoints are down or slow, senders treat delivery as failure and retry. Multiple retransmissions risk the receiver processing the same event multiple times. To avoid this, receiver-side implementation must guarantee idempotency (same processing yields same results regardless of repetition). Network failures or timeout delivery losses also occur, so for important data, dual-check verification after webhook delivery is recommended. Security is critical—with public URL endpoints, weak signature verification risks accepting unauthorized requests.

## Related terms

- **[API](API.md)** — Unlike webhooks, traditional integration method where clients actively send requests to retrieve data
- **[Event-Driven Architecture](Event-Driven-Architecture.md)** — Design pattern controlling system operation based on event occurrence, with webhooks as important implementation means
- **[Microservices](Microservices.md)** — Architecture composed of small independent service combinations, with webhooks enabling loose coupling coordination
- **[REST API](REST-API.md)** — General-purpose API communication method related to HTTP protocol underlying webhooks
- **[Asynchronous Processing](Asynchronous-Processing.md)** — Fire-and-forget asynchronous processing pattern realized by webhooks

## Frequently asked questions

**Q: What's the difference between webhooks and APIs?**
A: APIs are "pull" type where clients actively ask "give me information." Webhooks are "push" type where servers notify "this happened." Webhooks excel in real-time capability and server load perspective.

**Q: What if webhook delivery fails?**
A: Most webhook services feature automatic retry, resending multiple times after seconds to minutes. However, ultimate failure is possible, so periodically reconciling important data is recommended.

**Q: I'm concerned about webhook security. How do I protect it?**
A: HMAC signature verification is standard. Sender and receiver share secrets, verifying request signatures to confirm genuineness. Additionally protecting endpoints with HTTPS and adding [API](API.md) key authentication improves safety further.
