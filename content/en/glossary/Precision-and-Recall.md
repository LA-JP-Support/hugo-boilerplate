---
title: Precision and Recall
translationKey: precision-and-recall
description: Two complementary metrics for measuring classification model performance. Precision measures the accuracy of positive predictions, while recall measures how many actual positive cases were found
category: Data & Analytics
type: glossary
date: 2025-12-19
lastmod: 2026-04-02
draft: false
url: /en/glossary/Precision-and-Recall/
keywords:
  - precision
  - recall
  - machine learning
  - classification metrics
  - confusion matrix
---

## What are Precision and Recall?

**Precision and recall are two complementary metrics that measure classification model performance.** They reveal the actual strengths and weaknesses of a model that a single accuracy metric might miss, particularly valuable when data classes are imbalanced or errors have significantly different costs.

> **In a nutshell:** Precision is like "the reliability of a triggered alarm," while recall is like "how many actual dangers were detected."

**Key points:**

- **What they do:** Separately measure the quality and coverage of model predictions
- **Why they matter:** Different applications have different consequences for "false alarms" versus "missed detections"
- **Who uses them:** Medical diagnosis, spam detection, fraud detection, and other systems where prediction errors carry high consequences

## Why They Matter

Consider developing a disease diagnosis AI. Missing a patient (false negative) can be life-threatening. Conversely, in email spam detection, incorrectly marking legitimate mail as spam (false positive) is problematic. A single accuracy metric cannot capture these differences. Evaluating precision and recall separately enables the judgment "this model is suitable for that application."

## How They Work

First, you need to understand the **confusion matrix**, which categorizes classification outcomes into four patterns:

- **True Positive (TP)** — Predicted positive and actually positive (correct)
- **False Positive (FP)** — Predicted positive but actually negative (false alarm)
- **True Negative (TN)** — Predicted negative and actually negative (correct)
- **False Negative (FN)** — Predicted negative but actually positive (missed case)

**Precision** is calculated as:

> Precision = TP ÷ (TP + FP)

This is the percentage of items predicted as positive that were actually positive. The fewer false alarms, the higher the precision.

**Recall** is calculated as:

> Recall = TP ÷ (TP + FN)

This is the percentage of actual positives that the model correctly identified. Fewer missed cases means higher recall.

Here's a concrete example. In disease screening for 100 people where 10 are actually patients, if the model identifies 8 as patients, with 7 being true patients and 1 being a false alarm:

- Precision = 7 ÷ (7 + 1) = 87.5% (87.5% of identified patients are actually patients)
- Recall = 7 ÷ (7 + 3) = 70% (70% of actual patients were detected)

## Real-World Use Cases

**Medical Diagnostic Systems**

In disease screening, missing patients is the worst outcome, so recall takes priority. With 95% recall, you detect 95% of patients. Some false alarms are tolerable and can be confirmed through follow-up testing.

**Email Spam Detection**

Here, precision is prioritized. If a message is marked as spam with 99% precision, 99% of flagged messages are actual spam, protecting important emails from being lost.

**Fraud Detection Systems**

Credit card fraud detection prioritizes recall. Missing fraud harms the cardholder, so some false alarms (temporarily blocking legitimate transactions) are acceptable.

## Benefits and Considerations

**Benefits:** You can accurately evaluate application-specific needs that a single accuracy metric would miss, enabling proper judgment of practical usefulness.

**Considerations:** Precision and recall operate as a trade-off. Increasing recall often decreases precision and vice versa. Additionally, the decision threshold (at what confidence level you predict "positive") affects these values.

## Related Terms

- **Confusion Matrix** — Organizes classification results and enables calculation of precision and recall
- **F1 Score** — The harmonic mean of precision and recall
- **ROC Curve** — Visualizes model performance across different thresholds
- **Classification** — The machine learning task where these metrics are most useful
- **Evaluation Metrics** — The broader category of model performance measurements

## Frequently Asked Questions

**Q: Should we prioritize precision or recall?**

A: It depends on the application. Prioritize recall when missing cases are life-threatening (medical diagnosis), and precision when false alarms create large costs (spam detection). Many real-world applications balance both using metrics like the F1 score.

**Q: Can a model have both 100% precision and 100% recall?**

A: Ideally, that would be wonderful, but practically it's nearly impossible. A trade-off exists: increasing one typically decreases the other. Normally, you set acceptable levels for both and calibrate accordingly.

**Q: Why do we need precision and recall instead of just accuracy?**

A: With imbalanced data, accuracy is unreliable. For example, a model that predicts "healthy" for everyone achieves 99% accuracy when only 1% have disease, but is utterly useless. Precision and recall immediately reveal this problem (recall = 0%).
