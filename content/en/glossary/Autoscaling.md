---
title: Autoscaling
date: 2025-12-19
lastmod: 2026-04-02
translationKey: autoscaling
description: Autoscaling automatically increases or decreases computing resources (servers, capacity) according to application load, maintaining performance while achieving cost efficiency.
keywords:
- autoscaling
- cloud computing
- resource management
- scalability
- cloud infrastructure
category: Business & Strategy
type: glossary
draft: false
url: /en/glossary/autoscaling/
---

## What is Autoscaling?

**Autoscaling is a mechanism that automatically adds or removes computing resources such as servers and containers as application load increases or decreases.** In cloud-based systems, it addresses user access volume variations, maintaining consistent system performance while reducing costs during unnecessary hours. Major cloud providers like AWS, Google Cloud, and Azure offer it as a standard feature, making it indispensable for modern business.

> **In a nutshell:** "Just as a telephone switchboard automatically adds or removes lines based on call volume, the cloud adjusts server count based on demand." A Black Friday shopping site instantly increases servers upon detecting access surges.

**Key points:**

- **What it does:** Monitor metrics like CPU and memory usage, add servers when thresholds are exceeded, remove them when usage drops
- **Why it matters:** Prevent peak outages and access delays while minimizing costs during unnecessary hours
- **Who uses it:** E-commerce, SaaS companies, streaming services—organizations with volatile load patterns

## How it works

Autoscaling operates through three cyclical steps: monitoring, judgment, execution.

In the **Monitoring Phase**, the system continuously collects application metrics—CPU usage, memory, request count, response time, etc. Real-time dashboards aggregate information, displaying overall system "health." In the **Judgment Phase**, judgment proceeds based on configured scaling policy. For example: "if CPU usage exceeds 70% for 5 minutes, add 1 server." Rules can choose from multiple approaches: [Target Tracking](Target-Tracking.md) (auto-adjust based on target value), [Predictive Scaling](Predictive-Scaling.md) (forecast demand via machine learning), [Scheduled Scaling](Scheduled-Scaling.md) (fixed adjustment by time of day). In the **Execution Phase**, based on decisions, new servers are provisioned (created and initialized) and integrated into production within minutes. Monitoring continues until demand drops.

This automatic adjustment enables websites to rapidly scale up during 9 AM peak traffic, scaling down during quiet night hours to reduce wasted costs.

## Real-world use cases

**E-commerce platform sale preparation**
Black Friday and Cyber Monday expect 10x+ normal access. Autoscaling enables low-cost normal operation, automatically adding servers before sales, removing them after, handling demand without unnecessary expenses.

**SaaS company multi-tenant foundation**
When multiple client companies share systems, even if specific customers heavily use [CPU](CPU.md) for report generation, other customers remain unaffected. Autoscaling allocates appropriate resources to each workload.

**Streaming service simultaneous broadcast handling**
Celebrity live broadcasts attract millions of simultaneous connections. Autoscaling instantly responds, maintaining broadcast quality while balancing normal-time low-cost operation.

## Benefits and considerations

Autoscaling's biggest advantage is **cost efficiency.** No need to maintain excess servers; expense planning matches actual demand. **Performance guarantee** is also important. Server resources automatically increase with traffic, so users never experience slow response times, improving satisfaction. Furthermore, **operational burden reduction** eliminates manual scaling instructions by operators, preventing human errors.

However, important considerations exist. **Scaling delays** sometimes occur. New server startup takes several minutes, so sudden traffic spikes can exceed capacity during that interim. **Unpredictable cost increases** challenge budgets. Loose configuration can trigger massive server additions, causing unexpected high bills. Additionally, **complex configuration** mistakes prevent effectiveness. Wrong metric selection or inappropriate threshold settings risk "scaling hell"—frequent repeated addition and removal cycles.

## Related terms

- **[Load Balancing](Load-Balancing.md)** — Distributes requests evenly across servers, combining with autoscaling for maximum effect
- **[Cloud Computing](Cloud-Computing.md)** — Infrastructure foundation enabling autoscaling
- **[Containers](Containers.md)** — Lightweight execution environments scaled via [Orchestration](Orchestration.md) like Kubernetes
- **[Infrastructure as Code](Infrastructure-as-Code.md)** — Codifying scaling configuration for version control and automation
- **[SLA (Service Level Agreement)](SLA.md)** — Service quality standards like response time guaranteed by autoscaling

## Frequently asked questions

**Q: Is autoscaling alone sufficient? Is manual scaling unnecessary?**
A: Autoscaling excels at "steady variations," but combining with manual scaling for foreseeable events (sales, sports tournaments, product launches) is wise. Pre-increasing resources avoids scaling delays.

**Q: How should I configure scaling policies?**
A: Base decisions on industry benchmarks, past traffic data, and acceptable downtime. Initially configure conservatively, adjusting from operational data. Strengthen monitoring for weeks after configuration.

**Q: How much cost savings does autoscaling enable?**
A: Systems with large load variations can expect 30–50% cost reduction. However, constantly high-load systems gain limited savings. Analyze your traffic patterns and calculate ROI.
