---
title: Precision
lastmod: 2026-04-02
date: 2025-12-19
translationKey: precision
description: The percentage of positive predictions that were actually correct, measuring how reliable the model's positive judgments are
category: AI & Machine Learning
type: glossary
draft: false
url: /en/glossary/Precision/
keywords:
  - precision
  - AI
  - machine learning
  - model evaluation
  - false positives
---

## What is Precision?

**Precision is the percentage of items predicted as positive that were actually positive.** In other words, it's a metric representing the reliability and accuracy of model predictions. It's particularly important in scenarios where false alarms (predicting positive when actually negative) carry significant costs, such as spam detection, fraud detection, or disease diagnosis.

> **In a nutshell:** When a doctor says "this patient has disease," how accurate is that diagnosis? It measures the trustworthiness of positive judgments.

**Key points:**

- **What it does:** Measures how trustworthy a model's positive predictions are
- **Why it matters:** In systems where false alarms have large costs, prediction reliability is paramount
- **Who uses it:** Experts in security, healthcare, filtering, marketing, and similar domains

## Why It Matters

With low precision in spam detection, important emails frequently end up in the spam folder. Users may miss bank notifications or critical communications, losing trust. With low precision in medical diagnosis, healthy patients receive false "disease" diagnoses, leading to unnecessary surgery or treatment.

High precision models provide confidence that "this result is actually positive," which is essential for building user trust in systems.

## How It Works

Precision is calculated with the following formula:

> Precision = True Positives (TP) ÷ (True Positives (TP) + False Positives (FP))

Restated in words:

> Precision = Items predicted positive that were actually positive ÷ All items predicted positive

**Example:** A spam filter marks 50 emails as spam, with 40 being actual spam and 10 being legitimate emails (false alarms):

> Precision = 40 ÷ 50 = 0.8 (80%)

This means 80% of emails marked as spam by this filter are actually spam, while 20% are incorrectly identified.

The key difference from recall is that precision focuses on "what the model predicted" while recall focuses on "the actual situation."

## Real-World Use Cases

**Email Spam Filter**

Spam filters prioritize precision because incorrectly filtering legitimate emails (important work messages, bank notifications) is worst. Missing some spam in the inbox is more tolerable than losing important messages.

**Bank Fraud Detection**

When a credit card company determines "is this fraudulent before approval?", false alarms frustrate customers by preventing legitimate purchases. Maintaining high precision reduces customer frustration from false declines.

**Medical Screening**

When diagnosing "this patient may have disease?" based on symptoms, false positives (misdiagnosis) cause unnecessary treatment and psychological burden. High precision ensures diagnosis trustworthiness and narrows the need for follow-up testing.

## Benefits and Considerations

**Benefits:** High-precision models provide trustworthy predictions, minimizing secondary damage from false alarms. This is particularly effective when investigation costs are high or user trust is critical.

**Considerations:** Prioritizing precision too heavily decreases recall. For example, a "only predict when certain" strategy increases precision but misses actual positives. In medical diagnosis, missing patients (false negatives) is also serious. Balancing both metrics is important.

## Related Terms

- **Recall** — Actual positives that were correctly identified; the opposite perspective from precision
- **F1 Score** — The harmonic mean of precision and recall
- **Confusion Matrix** — Organizes true/false positives and negatives
- **Classification** — The machine learning task where precision is used
- **ROC Curve** — Visualizes model performance across various thresholds

## Frequently Asked Questions

**Q: Is there a model with 100% precision?**

A: Theoretically yes. For example, if you mark only one email as spam and it's actually spam, precision is 100%. However, you likely missed 99 other spam emails, making the approach impractical. Achieving both high precision and high recall simultaneously is difficult; there's usually a trade-off.

**Q: What's the difference between when precision matters versus when recall matters?**

A: Prioritize precision when false alarms carry large costs; prioritize recall when missed cases carry large costs. Spam detection prioritizes precision because false filtering is destructive. Medical diagnosis prioritizes recall because missing patients threatens life—accepting some false alarms is reasonable.

**Q: What's the difference between precision and accuracy (Accuracy)?**

A: Precision focuses on accuracy within "items predicted positive." Accuracy measures accuracy across all predictions. With imbalanced data (1% patients, 99% healthy), a model predicting everyone as healthy achieves 99% accuracy but is useless. Precision reveals this practical uselessness.
