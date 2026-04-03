---
title: Edge Computing
date: 2025-03-01
lastmod: 2026-04-02
description: Technology processing data at network edges near users and devices rather than central data centers.
translationKey: edge-computing
category: Cloud & Infrastructure
type: glossary
draft: false
url: /en/glossary/edge-computing/
keywords:
  - Edge Processing
  - Real-time Processing
  - Latency Reduction
  - IoT
  - Distributed Computing
---

## What is Edge Computing?

**Edge computing processes data at network edges near users and devices rather than central data centers.** Various devices—smartphones, smartwatches, manufacturing equipment, autonomous vehicles—gain processing power, making real-time decisions without cloud reliance. No more sending data to distant servers and waiting for processing results; response time (latency) drops dramatically.

> **In a nutshell:** Like doing needed processing locally in small shops instead of shipping parts to distant factories.

**Key points:**

- **What it does:** Local edge devices directly process and analyze data
- **Why it's needed:** Handles real-time applications requiring low latency, fast decisions
- **Who uses it:** IoT device makers, autonomous driving companies, manufacturing

## Why it matters

Traditional [Cloud Computing](Cloud-Computing.md) sent all data to central data centers, then received results. Reliable but faced network latency challenges. Self-driving cars detecting obstacles then sending to central server, waiting for decision—by then, already traveled meters. Medical devices needing real-time anomaly detection work similarly.

Edge computing solves this. On-device processing capability enables immediate decisions. No need sending all data to central servers—saves bandwidth, improves privacy. Massive manufacturing facilities generating sensor data every second—processing locally, extracting necessary data, sending only important information to cloud saves network and storage costs.

## How it works

Edge computing distributes processing capability. Traditionally, smartphones and sensors collected data only; cloud decided. Edge computing means these devices themselves do simple analysis and decisions.

Consider smart city streetlights. Traditionally, all sensor data reached cloud, central analysis sent "brighten this light" commands. Edge approach: each streetlight senses surrounding brightness and foot traffic, itself deciding "set this brightness"—cloud handles major decisions like "optimize all nighttime streetlight placement."

[Fog Computing](Fog-Computing.md) extends this thinking, adding intermediate layer between edge and cloud, sharing more complex processing. IoT devices handle many small tasks at edge, multiple-device integration analysis at fog, company-strategy analysis at cloud—dividing responsibilities.

## Real-world use cases

**Autonomous vehicle safe driving**

Self-driving cars detect obstacles via front-facing cameras in real-time. Sending to cloud for response is impossible. In-vehicle edge computing immediately signals brakes, ensuring safety. Cloud focuses on higher-level decisions like optimal route selection and traffic pattern analysis.

**Smart factory predictive maintenance**

Large auto plants operate hundreds of robot arms. Each arm's sensors detect vibration and temperature in real-time; edge computers identify bearing degradation, warning before failure. Avoiding downtime, production efficiency improves greatly.

**Video surveillance system facial recognition**

Retail store cameras sending all video to cloud overloads networks. Edge computing approach: cameras perform facial recognition, sending only "suspicious person" judgments to cloud. Network bandwidth drops; privacy improves.

## Benefits and considerations

Edge computing's greatest benefit is low latency and fast response. Independent of network delays, immediate decisions are possible; safety and user experience improve. Network traffic reduction saves bandwidth; privacy protection is advantaged. Devices processing independently means if central servers fail, edge devices continue working—strong resilience.

However, distributed operation complicates management. Updating thousands of devices' software becomes difficult, not batch-updateable. Devices need sufficient processing power, increasing initial development costs. Weak edge device security lets attackers enter entire networks.

## Related terms

- **[Cloud Computing](Cloud-Computing.md)** — Edge computing is distributed-architecture alternative/complement to traditional cloud-intensive models
- **[Fog Computing](Fog-Computing.md)** — Adds intermediate layer between edge and cloud, sharing more complex processing
- **[IoT](IoT.md)** — Edge computing efficiently handles massive IoT devices
- **[API](API.md)** — APIs control edge-cloud communication, managing necessary data exchange
- **[Latency](Latency.md)** — Reducing network delay is a primary edge computing goal

## Frequently asked questions

**Q: What's the relationship between edge and cloud computing?**

A: Choose neither alone; combine them. Real-time processing happens at edge; large-scale data analysis happens at cloud. Divide responsibilities.

**Q: If everything runs at edge, isn't cloud unnecessary?**

A: Edge devices have limited processing capability, unsuitable for complex analysis and big data. Multi-location data integration or finding trends in vast data still needs cloud.

**Q: How do we ensure edge computing security?**

A: Embed encryption, authentication, firewall features on each edge device with regular updates. Encrypt inter-device communication, prevent unauthorized access.
