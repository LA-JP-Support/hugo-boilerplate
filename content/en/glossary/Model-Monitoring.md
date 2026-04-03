---
title: Model Monitoring
date: 2025-12-19
lastmod: 2026-04-02
translationKey: Model-Monitoring
description: Continuous monitoring of AI models in production to detect performance degradation and anomalies early. Core to MLOps.
keywords:
- model monitoring
- performance tracking
- drift detection
- alerting
- operational monitoring
category: AI & Machine Learning
type: glossary
draft: false
url: /en/glossary/Model-Monitoring/
---

## What is Model Monitoring?

**Model monitoring continuously watches deployed AI models, detecting anomalies and degradation early.** After deployment, models don't sit idle—they undergo continuous health checks.

> **In a nutshell:** Like a car's ongoing engine and brake checks while driving. Early problem detection prevents accidents.

**Key points:**

- **What it does:** Continuous performance tracking of production models
- **Why it's needed:** Early degradation detection prevents business losses
- **Who does it:** MLOps engineers, data scientists, operations teams

## Why it matters

Deployed models degrade over time. Data drift reduces prediction accuracy. Concept drift changes prediction meanings. Unnoticed poor predictions accumulate, causing business loss.

Also detect system issues (API delays, memory shortage) and data quality problems (rising NULL values, outliers). Automatic anomaly detection enables quick problem-solving, maintaining service quality.

## How it works

Monitoring spans multiple layers.

**Performance metrics monitoring** tracks accuracy, recall, F1 score. When correct labels aren't immediately available, proxy metrics (input data statistics) suffice.

**Data drift detection** checks if input data distributions shifted from training. Statistical tests (KL divergence, Kolmogorov-Smirnov) identify changes.

**System metrics monitoring** tracks API response time, throughput, error rate, memory usage—ensuring service quality beyond just model performance.

**Alert settings** notify teams when thresholds are exceeded, enabling rapid response.

## Real-world use cases

**Recommendation systems** — User preference changes and site updates degrade recommendations. Daily purchase data monitoring detects satisfaction drops; retraining follows.

**Fraud detection** — Evolving fraud tactics reduce detection rates. Daily fraud pattern monitoring catches new techniques; retraining adapts.

**Medical diagnosis** — New patient populations (different ages, regions) sometimes show accuracy drops. Monitoring patient attribute distributions catches distribution shifts.

## Benefits and considerations

**Benefits** — Early problem detection enables quick response. Autoscaling becomes possible.

**Considerations** — Too many monitoring targets create noise, potentially missing real alerts. Threshold setting is difficult, requiring periodic adjustment.

## Related terms

- **Model Drift** — The main phenomenon being monitored
- **Model Retraining** — Response to detected problems
- **Data Drift** — Detecting input data changes
- **Alerting** — Anomaly notification systems
- **Observability** — Comprehensive monitoring implementation

## Frequently asked questions

**Q: What metrics should I monitor?**
A: Start with model prediction accuracy, input data statistics, and system response time. Add others based on business needs.

**Q: How often should I monitor?**
A: Real-time for high-risk (finance, healthcare); hourly to daily for standard operations. Balance cost and detection accuracy.

**Q: How do I set thresholds?**
A: Calculate initial values from training data, adjust during production. Machine learning tools for automatic threshold-setting exist.
