---
title: "Auto-Scaling"
date: 2025-03-01
lastmod: 2026-04-02
description: "A technology that automatically adjusts server resources based on system load"
translationKey: "auto-scaling"
category: "Cloud & Infrastructure"
type: glossary
draft: false
url: /en/glossary/Auto-Scaling/
keywords:
  - scaling
  - load balancing
  - resource management
  - cloud
  - performance
---

## What is Auto-Scaling?

**Auto-Scaling is a technology that automatically increases or decreases server resources (computing capacity) in response to system load, such as access volume or CPU usage.** Users no longer need to manually decide when to increase capacity during peak times or reduce it during low-demand periods. By flexibly adapting to demand, it maintains application performance while eliminating wasted costs.

> **In a nutshell:** "Just as a train station adds ticket gates during rush hours and removes them during night hours, servers are automatically adjusted based on traffic volume."

**Key points:**

- **What it does:** Automatically adds or removes server resources based on predefined rules
- **Why it matters:** Handles unpredictable access fluctuations while achieving cost efficiency
- **Who uses it:** Web service companies, online retailers, SaaS providers

## Why it matters

Before the cloud era, planning server resources was a difficult business decision. A miscalculation in year-end sales forecasts meant choosing between losing customers due to server shortages or inflating costs through over-investment. In reality, seasonal variations and unexpected media coverage often cause sudden access spikes.

Auto-Scaling solves this challenge fundamentally. When traffic increases, servers are automatically added, allowing users to access the service at comfortable speeds. When traffic drops, excess servers are automatically removed, eliminating wasted costs. As a result, companies can now deliver stable customer experiences while always operating at optimal cost. As a technology that maximizes the benefits of [Cloud Computing](Cloud-Computing.md), Auto-Scaling plays an extremely important role.

## How it works

Auto-Scaling works through three stages: metric monitoring, condition evaluation, and automatic execution.

First, the system continuously monitors metrics. Various indicators—CPU usage, memory consumption, request count, response time, queue length—are collected at regular intervals. Next, based on pre-configured rules (such as "if CPU usage exceeds 80%" or "if average response time exceeds 2 seconds"), the system determines whether scaling is needed. When conditions are met, the system automatically launches new server instances or stops existing ones.

For example, consider an e-commerce site on a sales day. In the morning, normal traffic levels require 2 servers. By afternoon, advertisements are distributed, traffic surges, and CPU usage reaches 85%. When the Auto-Scaling system detects this, it follows the configured rule ("add 1 server if CPU exceeds 80%") and launches a new server. If traffic increases further, additional servers are provisioned. At night, when traffic drops, unnecessary servers are shut down, reducing costs.

[Auto-Scaling Groups](Auto-Scaling-Group.md) refine this concept further by managing the pool of servers subject to scaling and enabling parallel scaling across multiple servers.

## Real-world use cases

**Video streaming platform handling sudden viewer increases**

When a popular artist releases a new music video, viewers flood in simultaneously. Auto-Scaling automatically strengthens servers instantaneously, allowing millions of people to watch simultaneously without playback interruptions or delays. After distribution ends, servers return to normal levels, so no wasted expenses occur.

**Cloud-based payroll system**

The day before payroll, a company's HR department performs massive computational processing, suddenly increasing system load. Auto-Scaling automatically adds servers during that period and removes them once processing is complete. This maintains optimal cloud costs while accommodating seasonal variations.

**Rapid spread of social media posts**

When a specific post unexpectedly goes viral, server access can multiply hundredfold in a short time. Without Auto-Scaling, the server would crash and the service would stop. However, with Auto-Scaling functioning properly, no matter how much access increases, the system automatically responds, and service remains uninterrupted.

## Benefits and considerations

The biggest benefit of Auto-Scaling is achieving both cost efficiency and performance. It prevents overload during peaks while eliminating wasted costs during downturns. Additionally, since it automatically responds to unpredictable access variations, manual adjustment by operations teams becomes unnecessary, reducing human error. Furthermore, scaling enables simultaneous handling of more users, improving customer satisfaction.

However, important considerations exist. Scaling takes several minutes, so when traffic increases suddenly, the system may experience overload during that interim period. Also, misconfiguring Auto-Scaling can cause unexpected cost increases. For example, if a bug causes resource usage to spike abnormally, it meets scaling conditions, and massive servers are launched, causing billing to skyrocket. Furthermore, scaling can increase database connections, creating cascading problems where the database becomes overloaded.

## Related terms

- **[Cloud Computing](Cloud-Computing.md)** — Auto-Scaling is one of cloud services' greatest advantages, providing flexibility difficult to achieve on-premises
- **[Infrastructure as Code (IaC)](Infrastructure-as-Code--IaC-/)** — IaC is leveraged to automate configuration of new servers accompanying scaling
- **[Load Balancing](Load-Balancing.md)** — Distributing load evenly across multiple servers maximizes Auto-Scaling's effectiveness
- **[Metrics](Metrics.md)** — Monitoring CPU usage and memory consumption provides the foundation for scaling decisions
- **[Monitoring and Alerting](Monitoring-and-Alerting.md)** — Continuous system monitoring is required to configure and execute scaling conditions

## Frequently asked questions

**Q: Does performance degrade while Auto-Scaling is adding servers?**

A: Scaling takes several minutes, so some slight delays may occur during that short period. To minimize this, it's important to adjust scaling rules beforehand and arrange to add servers before load increases.

**Q: Can database connections grow too much during Auto-Scaling?**

A: As you note, scaling can cause DB connections to surge suddenly, overloading the database. To prevent this, multi-layered measures are necessary, including database connection pooling, caching, and read replicas.

**Q: What problems occur if Auto-Scaling is misconfigured?**

A: Misconfiguration can cause scaling to trigger unnecessarily, resulting in unexpected high billing. Also, if scaling speed is set too fast, server startup processing can't keep up, potentially degrading performance. Regular reviews and validation in test environments are essential.
