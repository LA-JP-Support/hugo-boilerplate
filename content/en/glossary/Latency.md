---
title: Latency
date: '2025-12-19'
lastmod: 2026-04-02
translationKey: latency
description: The time delay from a user request to system response during data transmission. A critical performance indicator in AI systems and web applications.
keywords:
- Latency
- AI Infrastructure
- Network Latency
- Performance Optimization
- Real-Time Systems
category: AI & Machine Learning
type: glossary
draft: false
url: "/en/glossary/Latency/"
---

## What is Latency?

**Latency is the time delay from a user request to system response, a critical performance indicator.** Measured across network communication, AI model inference, and web application responses, it's typically expressed in milliseconds (ms) and directly affects perceived response speed.

> **In a nutshell:** The "wait time" in milliseconds from button press to response.

**Key points:**

- **What it does:** Measure the time until system response
- **Why it matters:** Directly impacts user experience, system reliability, and business outcomes
- **Who uses it:** Infrastructure engineers, AI engineers, application developers

## Why it matters

Latency functions as perceived time. Google research shows 100ms response delays reduce user satisfaction, while delays exceeding 1 second cause major engagement drops. In e-commerce, 100ms additional delay can reduce conversion rate up to 1%, decreasing sales. [Inference latency](Inference-Latency.md) similarly matters in AI systems—millisecond delays affect safety in autonomous vehicles and robotics requiring real-time decisions.

## How it works

Latency comprises multiple components. Network latency is time for data to physically travel from source to destination, governed by the speed of light even on fiber optic cables. Server processing latency is time for CPU to process requests and generate responses. Database query latency is retrieval time, varying greatly by storage type (SSD vs HDD). Client processing latency is final computation time.

These all add together. For example, 50ms network round-trip + 200ms server processing + 100ms database + 50ms client processing = 400ms total latency users experience. Reducing overall latency requires balancing optimization across all stages.

## How it's measured

**Time to First Byte (TTFB)** measures time from request transmission to first response byte, reflecting combined network and server processing. **Round-Trip Time (RTT)** is packet round-trip time, typically 5-200ms. **Percentile Latency** expressed as P50 (median), P95, P99 reveals outliers that averages miss.

In practice, prioritize P95 and P99 over averages since they reflect actual user experience.

## Benchmarks

| Use Case | Target | Perception |
|----------|--------|-----------|
| Interactive UI | <100ms | Instant response |
| Web page load | <1,000ms | No stress |
| Real-time gaming | <50ms | No delay felt |
| Video calls | <150ms | Natural conversation |
| Financial trading | <10ms | Millisecond competition |

Typical latency by medium: fiber optic 1-10ms, 4G LTE 20-50ms, 5G <10ms, satellite 500+ms. By storage: NVMe SSD <0.1ms, SSD <1ms, HDD 5-10ms.

## Real-world use cases

**E-commerce Optimization**

Reducing checkout latency from 50ms to 30ms can lower cart abandonment by 3%, potentially increasing annual sales by millions.

**AI Inference Pipeline**

Improving chatbot response from 200ms to 100ms significantly boosts user satisfaction and reduces abandonment.

**Global Content Delivery**

[CDN](Content-Delivery-Network.md) distribution from geographically dispersed servers minimizes physical distance delays.

## Benefits and considerations

Low latency greatly improves user experience and business KPIs. However, excessive latency reduction increases development costs, potentially yielding negative ROI. The key is setting appropriate latency targets matching business needs and achieving them efficiently. Mobile environments particularly require worst-case planning due to variable network conditions.

## Related terms

- **[Inference Latency](Inference-Latency.md)** — AI model response time
- **[CDN](Content-Delivery-Network.md)** — Important latency reduction technology
- **[Edge Computing](Edge-Computing.md)** — Reduce latency through physical proximity
- **[Core Web Vitals](Core-Web-Vitals.md)** — Performance indicators including latency
- **[Page Speed](Page-Speed.md)** — Page load speed and latency

## Frequently asked questions

**Q: What's "good" latency?**

A: Application-dependent. Websites aim for <1 second, real-time games <50ms, but judge by business model.

**Q: Does higher bandwidth improve latency?**

A: No. Bandwidth (throughput) and latency (speed) are separate concepts. 100 Gbps satellite still has 500+ms latency due to physical distance.

**Q: Can latency be completely eliminated?**

A: No. Physical laws limit it. Minimum is "physical distance ÷ speed of light."
