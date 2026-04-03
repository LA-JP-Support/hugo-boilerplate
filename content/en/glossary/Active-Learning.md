---
title: Active Learning
date: 2025-12-19
lastmod: 2026-04-02
translationKey: Active-Learning
description: A machine learning strategy where the algorithm actively selects the most valuable data to learn from, dramatically reducing annotation costs while maintaining model accuracy.
keywords:
  - Active learning
  - Machine learning
  - Data annotation
  - Uncertainty sampling
  - Query strategy
category: AI & Machine Learning
type: glossary
draft: false
url: /en/glossary/active-learning/
aliases:
  - /en/glossary/Active-Learning/
---

## What is Active Learning?

**Active Learning is a machine learning strategy where the algorithm actively selects the most valuable data to learn from, requiring labels for only the most informative examples, dramatically reducing annotation costs while maintaining model accuracy.** Traditional supervised learning requires a fully pre-labeled dataset. Active Learning shifts this by having the algorithm decide which data needs labeling next, achieving high-accuracy models with 10-20% of the annotation budget typically required.

> **In a nutshell:** "A student asking a teacher 'Can you explain this part I don't understand?' focuses learning on difficult areas. Similarly, AI asking 'Which data should we label next?' learns efficiently by focusing on uncertain areas."

**Key points:**

- **What it does:** The algorithm selects the most informative unlabeled examples for human annotation, minimizing labeling budget needs
- **Why it matters:** In high-cost annotation domains (medical images, legal documents), 60-80% cost reduction combined with high accuracy is achievable
- **Who uses it:** ML engineers, data scientists, annotation managers, organizations handling large datasets

## Why it matters

Traditional ML requires upfront labeling of entire datasets. Medical image diagnosis costs radiologists hundreds of dollars per image; legal document review costs lawyers days per document. This represents massive economic burden.

Active Learning eliminates this waste. Research shows 10-20% of the normally required labels achieves equivalent model accuracy. A $1 million annotation budget that would have labeled 1 million samples with traditional approaches yields 100,000-200,000 strategically selected samples with Active Learning. Google and Facebook report millions in cost savings.

Additionally, models understand "what they don't know," allowing annotators to focus on complex, valuable cases rather than easy ones. Result: improved annotation quality and model robustness.

## How it works

Active Learning starts with a small seed of labeled data. The model trained on this seed has low initial accuracy but provides uncertainty estimates. Next, unlabeled examples from a large pool are identified—specifically those the model is "least confident about."

Multiple uncertainty measurement methods exist. **Uncertainty sampling** (most common) prioritizes examples where prediction confidence is near 50% (can't decide between classes). **Query-by-committee** uses multiple models voting; examples where votes most disagree are selected. Annotators then focus on these high-value cases.

New labels are integrated with existing labeled data and the model is retrained. This cycle repeats, with each round adding more valuable examples. When stopping conditions are met (target accuracy, budget exhausted, accuracy plateau), the final model is complete.

## Calculation method

Active Learning efficiency is measured by comparing required data:

**Cost Reduction Rate = ((Traditional Required Labels - AL Required Labels) / Traditional Required Labels) × 100**

Example: Traditional approach needs 1,000 labels for 85% accuracy. AL achieves same accuracy with 150-200 labels. Reduction rate: 80-85%.

Uncertainty score example (classification):

**Uncertainty = 1 - max(P(y₁), P(y₂), ..., P(yₖ))**

Where P(yᵢ) is class i prediction probability. Maximum probability near 50% (uncertainty near 50%) indicates highest candidate value.

## Benchmarks

Typical cost reduction by domain:

- **80-90% reduction:** Medical image diagnosis, radiology—high-cost expert annotation
- **60-75% reduction:** Text classification, NLP, entity extraction—language tasks
- **40-60% reduction:** Object detection, semantic segmentation—computer vision
- **20-40% reduction:** Low-cost annotation or well-balanced datasets

Learning curve by implementation phase:

- **Early stage (0-20% data):** Peak AL effectiveness, 60-80% reduction
- **Growth stage (20-60%):** Steady 60-70% reduction, complex sample selection strategy important
- **Maturity stage (60-100%):** Diminishing returns, 30-50% reduction

## Related terms

- **[Machine Learning (ML)](/en/glossary/Machine-Learning/)** – Automatic pattern learning from data; AL is an ML efficiency technique
- **[Semi-Supervised Learning](/en/glossary/Semi-Supervised-Learning/)** – Mixing labeled and unlabeled data; similar goal to AL
- **[Data Annotation](/en/glossary/Data-Annotation/)** – Labeling raw data; AL directly optimizes this cost
- **[Uncertainty Estimation](/en/glossary/Uncertainty-Estimation/)** – Quantifying model prediction confidence; the foundation of AL query strategies
- **[Transfer Learning](/en/glossary/Transfer-Learning/)** – Reusing knowledge from other tasks; useful for AL seed set construction

## Frequently asked questions

**Q: Can AL really achieve 80% cost reduction?**
A: Case-by-case. Medical imaging and expert-labeled tasks report 80-90% reductions. Well-balanced open datasets achieve 30-40% reductions. Domain complexity, initial model quality, and annotator expertise greatly affect results.

**Q: Doesn't AL extend training time?**
A: Yes, short-term. Iterative retraining takes longer than one-time bulk annotation. However, total cost (money + time combined) shows significant savings.

**Q: Which query strategy is best?**
A: Task-dependent. Uncertainty sampling is simplest and most common. Diversity-aware hybrid strategies often achieve best practical results. Pilot multiple strategies on your data and optimize.
