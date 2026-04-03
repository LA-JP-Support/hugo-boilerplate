---
title: Chaos Engineering
date: 2025-12-19
lastmod: 2026-04-02
translationKey: Chaos-Engineering
description: A development practice that intentionally injects failures into production systems to verify resilience and recovery capabilities before real incidents occur.
keywords:
- chaos engineering
- system resilience
- failure injection testing
- reliability improvement
- SRE practice
category: AI & Machine Learning
type: glossary
draft: false
url: /en/glossary/chaos-engineering/
---

## What is Chaos Engineering?

**Chaos engineering intentionally causes failures in production environments—server crashes, network delays, database stops—to verify system resilience.** This isn't random destruction; it's controlled experimentation based on scientific hypotheses.

> **In a nutshell:** Before a water shortage happens, simulate it to practice response strategies.

**Key points:**

- **What it does:** Executes controlled failure injection tests in production to verify system recovery ability
- **Why it matters:** Prevents catastrophic outages from unexpected failures; cuts recovery time 50-80%
- **Who uses it:** SREs (Site Reliability Engineers), DevOps teams, infrastructure engineers

## Why it matters

Complex distributed systems work fine individually but sometimes fail unexpectedly in combination. Discovering this for the first time in production causes massive damage. Chaos engineering safely tests scenarios like "what if this service fails?" or "what if that database slows down?" in controlled ways, letting you build solutions before real problems strike.

## How it works

Execution follows 5 steps. **Stage 1 is hypothesis building**, setting premises like "if this service drops, backup handles it." **Stage 2 is experiment design**, deciding conditions like "stop service A for 5 minutes, observe." **Stage 3 is execution**, using tools like Chaos Monkey to inject failures. **Stage 4 is observation**, collecting data on system response. **Stage 5 is analysis and improvement**, identifying unexpected behavior.

Crucially: start with simple, isolated failures, gradually increasing complexity.

## Real-world use cases

**E-commerce reliability**
Netflix uses "Chaos Monkey" to randomly crash production servers daily, confirming service continues.

**Financial systems**
Testing that failover functions work when payment systems partially degrade.

**Healthcare systems**
Verifying that backup automatically handles patient database outages.

## Benefits and considerations

**Benefits** include discovering hidden weaknesses, improving team response skills, reducing downtime, and building customer trust. **Considerations** include risk of actual outages from inadequate safeguards, difficulty designing tests, and requiring an organizational culture of "learning from failure."

## Related terms

- **[Disaster-Recovery](Disaster-Recovery.md)** — Overall failure recovery planning
- **[High-Availability](High-Availability.md)** — System design achieving high availability
- **[System-Resilience](System-Resilience.md)** — The recovery capability chaos engineering targets
- **[Monitoring-and-Observability](Monitoring-and-Observability.md)** — Essential foundation for chaos experiments
- **[Fault-Tolerance](Fault-Tolerance.md)** — System design that tolerates failures

## Frequently asked questions

**Q: Isn't testing in production dangerous?**
A: Yes. Always start small with safety measures to minimize impact. Proceeding gradually is critical.

**Q: Isn't staging environment sufficient?**
A: No. Staging can't fully reproduce production complexity and live traffic. At some point, production testing becomes essential.

**Q: Could experiments cause real outages?**
A: Yes. That's why safety mechanisms (auto-rollback, time limits) are essential. Netflix runs thousands of chaos experiments while preventing actual incidents through safeguards.
