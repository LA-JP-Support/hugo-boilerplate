---
title: Auto-Scaling Group
date: 2026-04-02
lastmod: 2026-04-02
translationKey: auto-scaling-group
description: An AWS service automatically increasing or decreasing EC2 instances based on demand to optimize performance and costs. Enables cloud elasticity.
keywords:
- auto-scaling group
- AWS
- automatic scaling
- EC2
- infrastructure
category: Cloud & Infrastructure
type: glossary
draft: false
url: /en/glossary/auto-scaling-group/
---

## What is Auto-Scaling Group?

**An Auto-Scaling Group (ASG) is an AWS service automatically increasing or decreasing EC2 instance numbers based on traffic and load.** During high load, it automatically launches new instances; during low load, it terminates unnecessary ones, always achieving optimal performance and cost. Unlike manual scaling, the system adjusts automatically without human judgment, enabling 24/7 stable service delivery.

> **In a nutshell:** Like a department store increasing staff during business hours and reducing before closing. Resources increase and decrease as needed.

**Key points:**

- **What it does:** Automatically increase or decrease server resources based on demand
- **Why it's needed:** Handle sudden traffic spikes and reduce costs during low activity
- **Who uses it:** DevOps engineers, infrastructure architects, cloud architects

## Why it matters

Traditionally, on-premises environments purchased servers for peak traffic, resulting in massive idle resources during normal times and wasted costs. With ASG, instances launch only when needed, dramatically reducing costs.

Real example: An e-commerce company implementing ASG reduced peak infrastructure costs 25% while achieving zero downtime. ASG simultaneously achieves cost reduction and availability improvement—extremely important strategically.

## How it works

ASG operates through three major steps. First, **monitoring** continuously watches CloudWatch metrics (CPU usage, request count, etc.). Second, **evaluation** compares against configured scaling rules (e.g., scale out if CPU exceeds 70%). Third, **execution**—when triggered, launches new instances or terminates existing ones per the launch template.

Concretely: Morning traffic increases, CPU reaches 75%, ASG detects scale-out trigger. Following launch template definitions, new EC2 instances launch in ~5 minutes. These instances auto-register with load balancers for traffic distribution. Evening traffic drops, CPU drops to 20%, scale-in trigger terminates unneeded instances, reducing costs.

## Real-world use cases

**Web application operations**
News sites automatically scale when breaking news hits. During quiet night hours, minimal instances operate.

**Batch processing efficiency**
Night log analysis taking hours—ASG temporarily launches massive instances for parallel processing, then immediately terminates for cost savings.

**Microservices independent scaling**
When user auth service loads high, only that service's ASG scales out; other services unaffected.

## Benefits and considerations

ASG's biggest benefit is simultaneous cost optimization and availability improvement through automation. Unpredictable traffic changes auto-handled without human error. Instance failures auto-replace, near-zero downtime.

However, application design is crucial. ASG assumes stateless design—storing session data locally means scaling loses data. Scaling delays exist (new instances take minutes)—immediate traffic spikes can't be answered immediately. Configuration errors (low max instances) cause performance degradation instead. Careful design is essential.

## Related terms

- **EC2** — AWS virtual server service
- **Load Balancer** — Traffic distribution across multiple instances
- **CloudWatch** — AWS monitoring service
- **Scaling Policy** — Rule definitions for scaling decisions
- **Health Check** — Instance wellness verification mechanism

## Frequently asked questions

**Q: How to decide minimum and maximum instance numbers?**
A: Minimum is "minimum necessary to avoid complete outage (typically 2-3)." Maximum considers budget and peak traffic needs. If 1 instance handles 100 requests/sec, 1000 requests/sec peak requires 10 maximum instances.

**Q: Scaling delays are a problem. Solutions?**
A: Use scheduled scaling. If campaigns launch every Friday 6pm, pre-schedule scale-out 30 minutes prior—resources ready when traffic arrives.

**Q: Can spot instances be used?**
A: Yes. Mixing spot instances (70% cheaper) with ASG further reduces costs. However, spot price fluctuation and interruption risks require higher on-demand ratios in production.
