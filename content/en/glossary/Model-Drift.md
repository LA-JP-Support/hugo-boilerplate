---
title: Model Drift
date: 2025-12-19
lastmod: 2026-04-02
translationKey: Model-Drift
description: The phenomenon where AI model prediction accuracy decreases over time in production environments, requiring continuous monitoring and maintenance.
keywords:
- model drift
- data drift
- concept drift
- model degradation
- prediction accuracy
category: AI & Machine Learning
type: glossary
draft: false
url: /en/glossary/Model-Drift/
---

## What is Model Drift?

**Model drift is when AI model prediction accuracy degrades over time in production.** The data patterns change between training and real-world operation. Models that worked perfectly may lose accuracy weeks later.

> **In a nutshell:** Like a calibrated seismograph that gradually gives inaccurate readings over time. Regular recalibration is needed.

**Key points:**

- **What it is:** Prediction accuracy decline in production environments
- **Why it matters:** Prevents business losses and maintains model reliability
- **Who handles it:** ML engineers, data scientists, MLOps engineers

## Why it matters

Models train on historical data, but reality constantly changes. Consumer behavior shifts with seasons and trends. Economic conditions shift suddenly. Users adopt new behavior patterns. Missing these changes means inaccurate predictions.

Fraud detection models lose detection rates as fraudsters evolve tactics. Recommendation systems fail to keep up with user preference changes. Ignoring this directly causes business losses.

## How it works

Two main drift types exist.

**Data drift** occurs when input data statistics change. If this year's user data has different age distributions or browsing patterns than last year's training data, predictions become misaligned.

**Concept drift** happens when the meaning of relationships changes despite identical input data. For example, "low customer purchase frequency" once signaled churn, but during recession, the indicator's meaning changed as everyone reduced purchasing.

Drift detection requires continuous monitoring. Compare training data metrics to production metrics; when thresholds are exceeded, retrain.

## Real-world use cases

**Credit scoring models** — During economic crises, accuracy drops. The model needs retraining on recession data.

**Demand forecasting** — Seasonal products show drift during promotions and campaigns. Models must learn promotion effects and update.

**Spam filters** — When spammers change tactics, filter accuracy drops. New spam patterns require periodic model retraining.

## Benefits and considerations

**Benefits** — Early drift detection prevents accuracy loss and sustains business value.

**Considerations** — Detecting drift itself requires determining "normal vs. abnormal," making threshold-setting difficult. Distinguishing temporary noise from real drift matters. Frequent retraining increases costs.

## Related terms

- **Model Monitoring** — Detecting drift through monitoring
- **Model Retraining** — Responding to detected drift
- **Model Evaluation** — Measuring accuracy on production data
- **Feature Engineering** — Robust feature design as drift defense
- **Data Quality** — Tracking input data changes

## Frequently asked questions

**Q: Should I retrain immediately after drift is detected?**
A: It depends. If it's temporary noise, wait and observe. For clear trends, retrain. Balance business impact and costs.

**Q: How often should I monitor accuracy?**
A: High-risk domains (healthcare, finance) warrant daily checks. Standard systems typically check weekly.

**Q: Can I completely prevent model drift?**
A: No, but continuous monitoring and regular retraining keep accuracy consistently high.
