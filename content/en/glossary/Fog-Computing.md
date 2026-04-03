---
title: Fog Computing
date: 2025-03-01
lastmod: 2026-04-02
description: A computing layer placed between edge devices and cloud datacenters. Aggregates and processes data from multiple devices before sending to the cloud.
translationKey: fog-computing
category: Cloud & Infrastructure
type: glossary
draft: false
url: /en/glossary/fog-computing/
keywords:
- Distributed computing
- Edge processing
- Intermediate layer
- Real-time processing
- IoT
---

## What is Fog Computing?

**Fog computing places a processing layer between edge devices and cloud datacenters, enabling multiple IoT sensors and devices to aggregate and process their data locally before sending it to the cloud.** Edge handles lightweight processing within individual devices; fog aggregates and analyzes data from multiple devices; cloud performs enterprise-wide strategic analysis. This three-tier architecture optimizes real-time responsiveness, network efficiency, and cloud processing capacity.

> **In a nutshell:** Like shipping products from small workshops (edge) through regional distribution centers (fog) before reaching the main factory (cloud). Data flows through increasingly powerful processing stages.

**Key points:**

- **What it does:** Deploy computing power at the network intermediate layer to share data processing between devices and cloud
- **Why it's needed:** Efficiently process vast IoT data volumes while maintaining real-time response capability
- **Who uses it:** Smart cities, manufacturing, healthcare, telecommunications carriers

## Why it matters

[Edge computing](Edge-Computing.md) and cloud alone are insufficient for large-scale IoT. Consider a smart city with thousands of sensors across regions. Individual sensors making local decisions miss cross-region patterns and long-term trends. Sending all sensor data to cloud strains bandwidth, costs balloon, and latency spikes.

Fog computing solves this. Placing fog nodes regionally allows local aggregation and analysis, sending only critical information to cloud. Network costs drop, latency shrinks, and cloud infrastructure optimizes. As 5G adoption grows, edge-fog-cloud coordination becomes increasingly vital.

## How it works

Fog computing operates as a three-tier architecture.

**Tier one: Edge computing.** IoT devices—smart meters, cameras, temperature sensors—perform lightweight local processing. A temperature sensor determines "temperature exceeds 30°C" locally, transmitting only the decision, not raw data streams.

**Tier two: Fog.** Fog nodes (small servers or edge gateways) distributed across regions receive data from multiple edge devices, performing integrated analysis. A building's ten floors send temperature data to fog nodes, which detect "third and fourth floor temps rising simultaneously"—triggering HVAC (air conditioning) adjustments.

**Tier three: Cloud.** Multi-building, multi-region aggregated data flows to cloud for enterprise analysis: "summer power consumption trends," "facility efficiency rankings."

## Real-world use cases

**Smart city traffic control**

Thousands of traffic sensors city-wide. Individual lights (edge) detect traffic flow. Fog nodes process multiple intersections, detecting "region-wide congestion," dynamically adjusting signal timing. Cloud identifies "this time-slot always clogs this route," informing urban planning.

**Manufacturing predictive maintenance**

Hundreds of factory machines. Each machine (edge) monitors vibration real-time. Fog nodes (per production line) integrate multiple machines, determining "line-wide performance degraded," issuing warnings. Cloud analyzes factory-wide data: "maintenance costs down 30% this month vs. last year."

**Healthcare remote patient monitoring**

Multiple patients wear wearable devices. Devices (edge) monitor vital signs. Facility-level fog nodes integrate patient data, alerting "two ICU patients deteriorating." Cloud provides national guidance: "this symptom pattern responds well to this protocol."

## Benefits and considerations

Fog computing's greatest merit is efficiency and real-time responsiveness combined. Bandwidth shrinks, latency drops, only critical data reaches cloud, cutting storage and compute costs. Fog-layer integration detects complex patterns and anomalies individual devices miss. Local processing protects privacy—detailed medical data doesn't flood cloud; only critical alerts do.

However, fog node management grows complex. Thousands of nodes need software installation and updates. Fog nodes themselves become security targets. Edge-fog-cloud data models must align. Debugging distributed systems is difficult.

## Related terms

- **[Edge Computing](Edge-Computing.md)** — Fog computing extends edge concepts, adding intermediate processing for more complex analytics
- **[Cloud Computing](Cloud-Computing.md)** — Fog serves as the intermediate processing layer, forming three-tier architecture
- **[IoT](IoT.md)** — Fog computing efficiently manages vast device networks
- **[API](API.md)** — APIs coordinate edge-fog-cloud data exchange and consistency
- **[Network](Network.md)** — Fog nodes are critical network architecture components, optimizing communication

## Frequently asked questions

**Q: What's the difference between fog and edge computing?**

A: Edge focuses on lightweight processing within individual devices. Fog focuses on higher-level processing aggregating multiple devices. Edge is device-immediate; fog is its upper layer.

**Q: Where are fog nodes physically located?**

A: Fog nodes place near groups of edge devices. In factories: per production line. In buildings: per floor. In cities: per region—covering multiple devices.

**Q: Does fog computing replace cloud?**

A: No. Fog complements cloud. Fog handles real-time response and efficiency. Cloud performs long-term trend analysis and enterprise strategy. Both are needed.
