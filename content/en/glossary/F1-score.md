---
title: F1 Score
date: 2025-12-19
lastmod: 2026-04-02
translationKey: f1-score
description: F1 Score is a critical evaluation metric in machine learning, calculated as the harmonic mean of precision and recall. It's especially effective for evaluating classification models on imbalanced datasets.
keywords:
- F1 Score
- Precision
- Recall
- Machine Learning
- Classification Evaluation
category: Data & Analytics
type: glossary
draft: false
url: /en/glossary/f1-score/
---

## What is F1 Score?

**F1 Score is a metric for evaluating classification model performance, calculated as the harmonic mean of precision and recall.** Unlike simple accuracy (what % of predictions were correct), it reveals false positive and false negative balance. "99% accuracy" might mean missing fraud entirely. F1 Score prevents such pitfalls, determining if models are truly useful in practice.

> **In a nutshell:** A report card showing whether both "accuracy" and "comprehensiveness" are balanced. Excellence in only one dimension doesn't raise the score.

**Key points:**

- **What it does:** Quantifies whether classification models balance false positives and false negatives
- **Why it matters:** Imbalanced datasets (e.g., fraud 1% of total) make accuracy unreliable
- **Who uses it:** Data scientists, ML engineers, business analysts

## Why it matters

A medical diagnosis system "correctly identifies 990 of 1,000 patients as normal" shows 99% accuracy. Yet it might miss 45 of 50 actual patients. F1 Score resolves this dilemma.

F1 also helps cross-domain comparison. Precision-priority scenarios (email filters blocking legitimate mail is costly) differ from recall-priority scenarios (medicine missing disease is costly). F1 considers both, answering "is this model truly usable?"

## How it works

### Confusion Matrix and Basics

Understanding F1 requires knowing four classification result patterns. Comparing model "positive" and "negative" predictions against actual values creates four cases.

True Positive (TP) is "correctly identified positive," False Positive (FP) is "incorrectly identified positive," False Negative (FN) is "incorrectly identified negative," True Negative (TN) is "correctly identified negative."

### Precision and Recall

**Precision** = "of items called positive, how many actually were." Formula: "True Positive ÷ (True Positive + False Positive)." High spam filter precision means identified spam is mostly actual spam.

**Recall** = "of actually positive items, how many were identified." Formula: "True Positive ÷ (True Positive + False Negative)." High medical diagnosis recall means disease patients aren't missed.

F1 integrates these via harmonic mean; extreme weakness in either lowers overall score, automatically penalizing imbalanced models.

## Calculation Method

### Formula

F1 Score = 2 × (Precision × Recall) / (Precision + Recall)

With precision 0.8 and recall 0.6: F1 = 2 × (0.8 × 0.6) / (0.8 + 0.6) = 0.686

Alternative: F1 = 2TP / (2TP + FP + FN)

### Python Implementation

scikit-learn makes calculation simple—just pass actual and predicted values, getting F1 Score immediately. For multi-class problems, select averaging methods. Macro-average treats all classes equally; micro-average weights by class frequency.

### F-beta Score

Generalizing F1 as "F-beta Score" adjusts precision and recall weighting. F2 emphasizes recall 2x (medical diagnosis), F0.5 emphasizes precision 2x (spam filtering), enabling domain-specific evaluation.

## Benchmarks

### Score Interpretation

F1 ranges 0–1, with 1 being perfect. Practice typically considers 0.7+ "good." 0.5–0.7 is "needs improvement," below 0.5 is "needs reconsideration."

Field expectations vary. Medical diagnosis targets 0.85+, emerging fields accept 0.6.

### Industry Benchmarks

Fraud detection systems typically target 0.7–0.8 F1. Imbalanced data (fraud <1%) makes perfection unrealistic.

Medical diagnosis and cancer detection employ 0.8–0.9 standards. High miss costs require maintaining both recall and overall F1.

Text classification and sentiment analysis typically achieve ~0.8. NLP task complexity requires practical balance over perfection.

## Real-world use cases

**Fraud detection system evaluation**
Financial institutions assess new fraud models with F1 Score, showing precision (reducing false alerts) and recall (missing actual fraud) balance. 0.75 F1 lets operations determine workability.

**Medical diagnosis AI verification**
Cancer-detection AI prioritizes recall but needs reasonable precision. 0.82 F1 indicates medically and statistically trustworthy models for clinical deployment.

**Text classification quality assurance**
Article auto-classification with 0.78 F1 indicates reader recommendation reliability. Lower scores trigger training data enhancement and model adjustment.

## Benefits and considerations

**Benefits**
F1 expresses complex tradeoffs in single metrics. Comparing models becomes faster than reporting precision and recall separately. Imbalanced data evaluation is more reliable than accuracy.

**Considerations**
F1 hides individual precision and recall characteristics. Same 0.75 F1 differs significantly: precision 0.9/recall 0.6 versus precision 0.6/recall 0.9. Always verify F1 alongside constituting precision and recall.

## Related terms

- **[Precision](Precision.md)** — F1 component. Shows false positive control.
- **[Recall](Recall.md)** — F1 component. Shows true positive capture.
- **[Confusion Matrix](Confusion-Matrix.md)** — F1 calculation foundation showing four classification patterns.
- **[Machine Learning](Machine-Learning.md)** — F1 evaluates classification task performance.
- **[ROC-AUC](ROC-AUC.md)** — Alternative metric evaluating model performance across all thresholds.

## Frequently asked questions

**Q: Is 0.5+ F1 truly usable model?**
A: Depends on domain. Early-stage models might have 0.5 value. Medical and finance standards require 0.8+. Determine use-case goals first.

**Q: Isn't reporting precision and recall separately better?**
A: Detailed analysis needs both. But comparing multiple models benefits from unified metrics. Using both is optimal.

**Q: Can F1 handle extremely imbalanced data (0.1% positive)?**
A: F1 alone isn't sufficient. Use precision-recall curves or business cost matrices alongside F1, adding practical context.
