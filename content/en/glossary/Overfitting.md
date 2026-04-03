---
title: Overfitting
date: 2025-12-19
lastmod: 2026-04-02
translationKey: overfitting
description: Overfitting occurs when a machine learning model becomes excessively adapted to training data, losing its generalization ability and performing poorly on new data.
keywords:
- Overfitting
- Machine Learning
- Model Optimization
- Regularization
- Bias-Variance
category: AI & Machine Learning
type: glossary
draft: false
url: /en/glossary/Overfitting/
---

## What is Overfitting?

**Overfitting occurs when a machine learning model becomes excessively adapted to training data, losing its general pattern learning ability and performing poorly on new data.** The model performs nearly perfectly on training data but performance dramatically drops on real operational data because it learns even the noise as "important patterns."

> **In a nutshell:** Like studying only last year's test questions perfectly but failing completely different problems this year.

**Key points:**

- **What it does:** Excessive adaptation to training data eliminates generalization ability
- **Why it's problematic:** Real operational performance becomes poor, destroying business value
- **Solutions:** Regularization, cross-validation, early stopping, and other techniques

## Why it matters

Overfitting is a common problem companies face when adopting AI. Data scientists report 99% accuracy, but production performs at only 60%—a common failure scenario. Such failures waste investment and mislead critical business decisions. For instance, medical diagnosis models suffering from overfitting could misdiagnose patients with different conditions than training examples.

## How it works

Overfitting develops gradually during training. Initially, the model learns training data's essential patterns; both training and validation errors decrease (good state). Continued training makes it learn noise, outliers, and random patterns in training data. Training error approaches zero but validation error increases (worsens). The gap between these errors signals overfitting.

**Bias-variance tradeoff** is relevant. Simple models have high bias (skew) but overly complex models have high variance (sensitivity to training data changes), both hurting accuracy. Regularization techniques (L1, L2 penalties) "penalize" model complexity. Cross-validation prevents excessive adaptation to single datasets.

## Real-world use cases

**Medical Diagnostic System Development**
Training a diagnostic model on 500 patients achieved 95% accuracy. Applying it to 1,000 new hospital patients dropped to 70%. The original model was overfit to small-scale data.

**Financial Risk Assessment Improvement**
Banks built loan review models from 10 years of historical data. Strong training accuracy but failed predictions during economic crises—untested conditions. Training period expansion covering multiple economic cycles was necessary.

**Recommendation System Testing**
E-commerce built recommendation systems from existing customer purchase history but new customer recommendations were inaccurate. Overfitting to existing customer patterns prevented generalization.

## Benefits and considerations

**Benefits:** Understanding and preventing overfitting enables building production-ready models, dramatically improving ML investment ROI.

**Considerations:** Applying excessive overfitting prevention (strong regularization) causes "underfitting" where accuracy drops. Balance adjustment is difficult and requires extensive experimentation.

## Related terms

- **[Cross-Validation](Cross-Validation.md)** — Evaluates across multiple datasets, detecting overfitting—the standard technique
- **[Regularization](Regularization.md)** — Adds complexity penalties, preventing overfitting—mathematical technique
- **[Bias-Variance](Bias-Variance.md)** — Two error sources affecting model accuracy balance
- **[Hyperparameter Tuning](Hyperparameter-Tuning.md)** — Model setting optimization preventing overfitting
- **[Feature Selection](Feature-Selection.md)** — Data preprocessing removing unnecessary inputs, preventing overfitting

## Frequently asked questions

**Q: Why is training accuracy high while validation accuracy is low?**
A: Overfitting. The model is learning training data noise. Simplify the model, increase training data, or strengthen regularization.

**Q: Does collecting more data solve overfitting?**
A: Usually yes. More data training makes noise components less important relatively, focusing on true patterns.

**Q: How do we identify overfitting?**
A: Compare training versus test data error. Large gaps indicate high overfitting probability. Regularly evaluate validation sets.
