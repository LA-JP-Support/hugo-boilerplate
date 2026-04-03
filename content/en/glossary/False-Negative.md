---
title: False Negative
translationKey: false-negative
lastmod: 2026-04-02
date: '2025-12-19'
description: A false negative occurs when AI systems fail to detect actual problems or intent. Chatbots missing refund requests, medical AI missing disease diagnoses, and fraud detection systems missing fraud all have severe consequences.
keywords:
- false negative
- error
- AI accuracy
- machine learning
- confusion matrix
category: AI & Machine Learning
type: glossary
draft: false
url: "/en/glossary/false-negative/"
---

## What is False Negative?

**A False Negative is "an error where AI fails to detect a problem that actually exists."** Chatbots missing refund requests, medical diagnosis AI missing cancer, fraud detection systems missing fraud—these are the most dangerous types of mistakes.

> **In a nutshell:** "Like airport security missing a passenger with a knife and allowing them to board—a critical error."

**Key points:**

- **What it is:** AI judges that a real problem "doesn't exist"
- **Why it's dangerous:** Issues go unprocessed, causing customer dissatisfaction, security breaches, medical accidents
- **Who should address it:** Healthcare, finance, security, customer support industries

## Calculation Method

False negatives are measured by the "recall" metric:

**Recall = TP / (TP + FN)**
Example: Of 100 refund requests, bot correctly identifies 85, misses 15
Recall = 85 / (85 + 15) = 85% (15% false negative rate)

This means "of 100 actual requests, only 85% were detected." The 15 legitimate requests go unprocessed.

## Benchmarks and Targets

Acceptable false negative rates (by industry):

- **Medical diagnosis** — 1% or below (missed disease threatens patient life)
- **Fraud detection** — 3-5% (fraud damage occurs despite acceptable FN rate)
- **Customer support** — 5-10% (high miss rate erodes trust)
- **Security** — 0.5% or below (missed threats cause severe damage)

## Why it Matters

False negatives are more dangerous than [false positives](False-Positive.md) (incorrectly detecting nonexistent problems) because users feel "no response" and potential harm accumulates.

Examples:
- **Healthcare** — AI misses early-stage cancer; months later it's found as advanced cancer. Treatment becomes difficult, prognosis worsens.
- **Fraud detection** — Fraud goes undetected, victims lose millions unknowingly.
- **Customer support** — Refund request is missed, customer distrusts and cancels.

## How it Works

When AI judges "positive (problem exists)" vs "negative (no problem)," 4 results occur:

| Prediction \ Actual | Positive (Really has problem) | Negative (Really no problem) |
|---|---|---|
| **Predicted Positive** | ✓ Correct (TP) | ✗ False Positive (FP)|
| **Predicted Negative** | **✗ False Negative (FN)** | ✓ Correct (TN) |

False negative is the case where **"it's actually positive but AI predicted negative."**

Common causes:
- Training data lacks special cases that AI didn't learn
- Model confidence threshold is too high (overly cautious, missing real signals)
- Testing lacks complex scenarios at test time

## Real-world Use Cases

**Medical chatbot**
User enters "chest pain." AI fails to recognize myocardial infarction possibility and suggests "it might be stress." User believes suggestion; hours later has actual MI and collapses. Missing this threatens life.

**Software quality assurance**
Automated tests check only "standard scenarios." High-load memory leak goes undetected and reaches production. Production crash occurs.

**Bank fraud detection**
New fraud method (different from traditional patterns) goes undetected. Multiple fraudulent transactions aren't detected for weeks.

## Mitigation Strategies

To reduce false negatives: diversify training data to include edge cases, properly adjust confidence thresholds, continuously monitor live data, escalate to humans under uncertainty, and conduct production-equivalent testing.

## Benefits and Considerations

Benefits include reduced critical issue misses and improved customer satisfaction and safety. Considerations include overly lowering thresholds to reduce false negatives increases false positives. Balance between precision and recall is important.

## Related Terms

- **[False Positive](False-Positive.md)** — The opposite error: incorrectly detecting nonexistent problems
- **[Confusion Matrix](Confusion-Matrix.md)** — A table visualizing TP, FP, FN, TN
- **[Recall](Recall.md)** — Metric measuring how much true positive is detected
- **[Precision](Precision.md)** — Metric measuring how much detected positive is truly positive
- **[Sensitivity and Specificity](Sensitivity-Specificity.md)** — Standard healthcare terminology

## Frequently Asked Questions

**Q: Which is worse—false negative or false positive?**
A: Context matters. False negatives are dangerous in healthcare. False positives are problematic in spam detection.

**Q: Can false negatives be completely eliminated?**
A: No. Training data has limits and new patterns always emerge. Continuous improvement can reduce them.

**Q: How to detect false negatives?**
A: User feedback, sample audits, and continuous monitoring are primary methods.
