---
title: Decision Tree
date: 2025-12-19
lastmod: 2026-04-02
translationKey: Decision-Tree
description: Learn machine learning techniques for expressing decision logic as tree diagrams and learning predictive patterns from data.
keywords:
- decision tree
- machine learning
- classification
- regression
- data mining
category: Data & Analytics
type: glossary
draft: false
url: /en/glossary/decision-tree/
---

## What is Decision Tree?

**A decision tree is a machine learning method that automatically discovers patterns in data like "if A then choose B, otherwise choose C."** Expressed as a flowchart-like tree diagram, it's inherently understandable to humans. Applied in many scenarios including loan approval assessment, medical diagnosis, and sales forecasting.

> **In a nutshell:** "A method that automatically learns 'if...then...' decision rules from data and expresses them as tree diagrams."

**Key points:**

- **What it does:** Machine learning algorithm that recursively divides data for classification and prediction
- **Why it's needed:** Learn complex patterns in understandable form and predict new data
- **Who uses it:** Data scientists, analysts, healthcare and finance professionals

## Why it matters

Unlike blackbox models like [neural networks](Neural-Network.md), decision trees let you understand "why the prediction happened." Critical for healthcare diagnostics and financial loan decisions where explaining the reasoning is required.

Additionally, complex preprocessing is unnecessary. You can mix categorical and numerical data, handle missing values naturally, and learn from small datasets. Ease of implementation is also an advantage.

## How it works

Decision tree learning proceeds through three main steps.

**Stage 1: Explore split candidates** - For multiple features (age, income, employment status, etc.), calculate where to split data so "groups become most uniform." For example, compare splitting at "age 35+" versus "income 500K+" to see which better separates groups.

**Stage 2: Select optimal split** - Choose the most effective split and divide data into two groups.

**Stage 3: Recursive splitting** - Repeat the same process for each group until reaching "leaves" (final decision results).

For example, a loan approval tree might learn "first split by credit score → then by income → then by employment status." The result expresses as a tree: "credit score 650+, annual income 5M+, employed full-time → approve loan."

## Real-world use cases

**Medical diagnosis**
Built a decision tree to predict "what disease?" from symptoms (fever, cough, headache) and test results. Supplemented physician diagnosis, reducing misdiagnosis risk.

**Churn prediction**
A telecom company predicted "which customers likely to cancel?" from usage patterns. Targeted retention efforts reduced churn 30%.

**Fraud detection**
Detected credit card fraud from transaction amount, time, location using decision tree. Combined multiple trees with [random forest](Random-Forest.md) achieved 97%+ accuracy.

## Benefits and considerations

The greatest benefit is interpretability—the tree diagram clearly shows why decisions were made. Complex preprocessing is unnecessary, making implementation easy.

However, single trees tend toward "overfitting" (adapting too closely to training data, failing on new data). Mitigations include pruning unnecessary branches, using ensemble methods like [random forest](Random-Forest.md) or [gradient boosting](Gradient-Boosting.md). Strong seasonality or trends in data may also exceed single tree capability.

## Related terms

- **[Machine Learning](Machine-Learning.md)** — Field that decision trees belong to
- **[Random Forest](Random-Forest.md)** — Powerful model combining multiple trees
- **[Gradient Boosting](Gradient-Boosting.md)** — Building multiple trees sequentially
- **[Classification](Classification.md)** — Primary use of decision trees
- **[Explainability](Explainability.md)** — Major advantage of decision trees

## Frequently asked questions

**Q: How do I prevent decision tree overfitting?**
A: Use "pruning" to remove unnecessary branches. Also, combining multiple trees with [random forest](Random-Forest.md) is effective.

**Q: Should I choose decision tree or [neural network](Neural-Network.md)?**
A: Choose decision tree if reasoning is important; [neural network](Neural-Network.md) if highest accuracy is priority. Actually, combinations also work.

**Q: Can decision trees do image recognition?**
A: Directly it's difficult, but after extracting features from images first, decision trees can classify. Complex image recognition typically uses [deep learning](Deep-Learning.md).
