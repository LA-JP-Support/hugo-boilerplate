---
title: Spot Instances
date: 2025-12-19
lastmod: 2026-04-02
translationKey: spot-instances
description: Spot instances are discounted cloud computing resources from AWS, Azure, and GCP that offer up to 90% savings on surplus capacity in exchange for potential termination with short notice.
keywords:
- spot instances
- cloud computing
- AWS
- cost savings
- fault-tolerant workloads
category: Cloud & Infrastructure
type: glossary
draft: false
url: /en/glossary/Spot-Instances/
---

## What are Spot Instances?

**Spot instances are computing resources using cloud provider surplus capacity, available at up to 90% discount compared to on-demand pricing.** In exchange, the provider may terminate instances with short notice (AWS: 2 minutes, Azure/GCP: 30 seconds) when capacity is needed. This represents a trade-off: "cheap but potentially unstable" becomes "genuinely inexpensive if shutdown is managed correctly."

> **In a nutshell:** Like last-minute airline ticket discounts—very cheap, but "might be cancelled with short notice."

**Key points:**

- **What it is:** Discounted cloud resources (with termination risk).
- **Why it's needed:** Cost savings is the top priority for certain workloads (batch processing, testing, ML training).
- **Who uses it:** Startups, research institutions, scalability-focused companies.

## Why It Matters

Cloud cost reduction is a critical concern for many organizations. Development and testing environments, batch processing, and machine learning training—workloads where "execution timing is flexible and interruption-tolerant"—previously created substantial cost burdens. Spot instances enable these workloads to run at drastically lower cost, making machine learning and large-scale simulation accessible to general enterprises.

## How It Works

Spot instances operate through pricing mechanisms and interruption policies.

**In the pricing mechanism**, spot prices dynamically adjust based on supply and demand for each instance type and region. You set a maximum price; as long as actual price stays below it, you run at a discount.

**In the capacity pool**, unused resources for a given instance type and availability zone are pooled. Pool pricing and interruption risk vary by pool.

**In the interruption mechanism**, when the provider needs resources for high-priority requests (on-demand or reserved instances), spot instances receive notice (2-30 seconds) and terminate. AWS may issue "rebalance recommendation" warnings.

**In design requirements**, workloads must be "stateless" or "checkpoint-capable." Otherwise, interruption causes data loss.

## Real-World Use Cases

**Batch Processing and ETL Jobs**
Running large nightly data processing with 80%+ cost savings via spot instances.

**Machine Learning Model Training**
Running hyperparameter search in parallel across instances, with auto-restart capability if interrupted, achieving low-cost training.

**CI/CD Pipeline Builds**
Launching large numbers of parallel build agents for testing, then scaling down immediately after completion.

## Benefits and Considerations

**Benefits:** Up to 90% cost savings, scalability, ideal for short-term compute needs.

**Considerations:** Interruption risk (no SLA) makes them unsuitable for mission-critical production, and application design complexity increases. Requires fault-tolerant architecture.

## Related Terms

- **[Cloud Computing](Cloud-Computing.md)** — The delivery model for spot instances.
- **[Auto-Scaling](Auto-Scaling.md)** — Efficient spot instance management.
- **[Cost Optimization](Cost-Optimization.md)** — The primary use case for spot instances.
- **[Fault Tolerance](Fault-Tolerance.md)** — Essential design pattern for spot instances.
- **[Kubernetes](Kubernetes.md)** — Automation platform for spot instance orchestration.

## Frequently Asked Questions

**Q: Can spot instances be used for production workloads?**
A: Yes, but use a hybrid approach: spot + on-demand + reserved instances for both reliability and economy.

**Q: What's the typical interruption frequency for spot instances?**
A: Depends on region, instance type, and time of day, but AWS Spot Instance Advisor shows historical data. Generally 1-5% per day interruption rates.
