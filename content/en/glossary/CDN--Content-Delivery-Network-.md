---
title: CDN (Content Delivery Network)
date: 2025-12-19
lastmod: 2026-04-02
translationKey: CDN--Content-Delivery-Network-
description: A CDN is a global server network delivering web pages and videos from locations closest to users for fast content delivery.
keywords:
- CDN
- Content Delivery
- Web Performance
- Edge Server
- Global Network
category: Cloud & Infrastructure
type: glossary
draft: false
url: /en/glossary/cdn--content-delivery-network-/
---

## What is CDN (Content Delivery Network)?

**A CDN is a global server network delivering web pages and videos quickly from locations closest to users.** Traditionally, websites delivered all content from a single origin server. But fetching from distant servers took time, slowing load speeds. CDN solves this by placing "edge servers" (copy servers) worldwide, delivering from the server nearest each user.

> **In a nutshell:** "Like placing library books in branch libraries instead of only the main library—you borrow from the nearest branch, not traveling to headquarters."

**Key points:**

- **What it does:** Global server network delivering content from user-nearest locations
- **Why it's needed:** Dramatically accelerates page load speeds, distributes server load
- **Who uses it:** Large websites, video streaming, e-commerce and other global-audience services

## How it works

CDN operates in three steps: (1) When users access websites, CDN's system identifies user location. (2) CDN selects the edge server nearest that user. (3) Content delivers from that server. If the nearby server lacks content, it fetches from the origin server, caches it, and delivers immediately to future users. This can reduce page load times by 50-80%.

## Real-world use cases

**Video Streaming Services** — Netflix and YouTube need massive data delivery. CDN serves video from worldwide servers nearest users, enabling smooth viewing.

**Online Shopping** — Delivering product images and descriptions via CDN speeds up shopping cart and checkout, reducing abandoned carts and boosting sales.

**News Sites** — Major breaking news creates traffic spikes. CDN prevents origin server overload, maintaining stable service.

**API Caching** — API responses can cache via CDN too. Fast search results and data retrieval dramatically improve application response speed.

**SaaS Providers** — Global software services use CDN for fast application interface loading. Users anywhere enjoy comfortable experiences.

## Related terms

- **Edge Computing** — Processing data near users
- **Caching** — Temporarily storing frequently used data for quick access
- **Latency** — Time from sending to receiving data
- **Bandwidth** — Amount of data transferable through communication paths
- **DDoS Protection** — Technology defending servers from mass-access attacks

## Frequently asked questions

**Q: Does CDN usage compromise security?**
A: Modern CDN services include security features; security often improves. DDoS protection and SSL/TLS encryption are standard.

**Q: Do all websites need CDN?**
A: Small, regionally-focused sites don't need it. But as you grow and expand users, CDN becomes worth considering.

**Q: How much does CDN cost?**
A: Typically usage-based. Small-scale services start at thousands monthly; large sites may reach tens of thousands.

**Q: Is an origin server still needed?**
A: Yes. CDN distributes origin server copies—you always need the master origin server. You cannot operate with only CDN.

## Implementation considerations

When deploying CDN, analyze current traffic volume, forecast future growth, and identify geographic user distribution. Also consider caching strategy, security requirements, and cost-effectiveness, comparing multiple CDN providers for the best fit.
