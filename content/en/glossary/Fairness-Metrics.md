---
title: Fairness Metrics
date: '2025-12-19'
lastmod: 2026-04-02
translationKey: fairness-metrics
description: Fairness Metrics are indicators that quantitatively measure and verify whether AI models treat different groups equally. Essential for bias detection and ensuring fairness.
keywords:
- fairness metrics
- bias detection
- AI ethics
- machine learning fairness
- algorithm evaluation
category: AI & Machine Learning
type: glossary
draft: false
url: "/en/glossary/fairness-metrics/"
---

## What is Fairness Metrics?

**Fairness Metrics are indicators that quantitatively measure whether AI systems treat demographic groups equally across attributes like gender and race.** In critical decision-making systems like hiring AI, lending systems, and medical diagnosis, fairness metrics detect unintended biases by converting them into numerical values. They serve as a tool that helps companies avoid legal risks while maintaining social responsibility.

> **In a nutshell:** "A fairness report card that checks whether applicants with the same test score receive different approval outcomes based on gender."

**Key points:**

- **What they do:** Quantify differences in prediction results between groups to identify unfairness
- **Why they're needed:** Overlooking bias leads to legal lawsuits and loss of trust
- **Who uses them:** AI developers, ethics committees, regulators, hiring/finance/healthcare organizations

## Calculation Methods

Representative metrics include the following:

**Demographic Parity** compares positive decision rates by group. If a hiring AI approves 60% of men and 55% of women, the difference is 5%. **Equalized Odds** restricts comparisons to qualified candidates for more accurate fairness measurement. **Equal Opportunity** checks both true positive rates and false positive rates for multidimensional evaluation.

In implementation, classification predictions for each group are collected from training data, and statistical differences are calculated. In a 1,000-person evaluation (600 men, 400 women) where men's approval rate is 50% and women's is 40%, the difference is 10%.

## Benchmarks and Targets

Acceptable bias differences are: 5% or less is excellent, 5-10% is warning level, 10-15% is critical level, and 15% or above carries legal risk. If women's pass rate is 15% lower in hiring AI, it constitutes indirect discrimination. Medical diagnosis requires 1% or less, security requires 0.5% or less.

## Why it Matters

Amazon discovered in 2016 that its hiring AI systematically discriminated against women and shut it down. Facial recognition has 35 times higher error rates for non-white individuals compared to white people; loan approval rates for minorities are 20% lower than for whites. These issues stem from biased training data and encoded unconscious bias. Without fairness metrics to detect these problems, significant [legal risk](Responsible-AI.md) and loss of social trust follow.

## How it Works

AI model predictions are broken down by demographic group, and result differences are measured using straightforward mechanisms. Prediction distributions by group are visualized, and statistical tests determine if significant differences exist. When differences are found, improvements are made through training data diversification, reducing weight on specific attributes, and adjusting decision thresholds.

However, simultaneously satisfying all metrics is difficult, and balance between [business requirements](Business-Strategy.md) and ethics is important. Improving one metric sometimes worsens another.

## Real-world Use Cases

**Bias testing in hiring AI**
Companies implement fairness testing on historical data before deployment. Pass rates by gender and race are compared, and if differences exceed 15%, training data is rebalanced before production launch.

**Loan review system audit**
Banks audit their AI systems per regulatory requirements. Approval rate differences across demographic groups are quantified to demonstrate the absence of discriminatory outcomes and achieve regulatory compliance.

**Fairness assurance in medical diagnosis AI**
Healthcare institutions test diagnosis AI across multiple racial groups. When accuracy differences are found, additional data for those groups is added to ensure equal accuracy for all.

## Benefits and Considerations

Benefits include objective bias evidence that avoids legal risk and builds trust. Bias removal also improves model performance. Considerations include multiple definitions of fairness and trade-offs where improving one metric worsens another. Monitoring multiple metrics in balance is important rather than focusing on a single metric.

## Related Terms

- **[Algorithm Bias](Algorithm-Bias.md)** — The tendency toward unfair judgment in AI
- **[Large Language Models (LLM)](LLM.md)** — Subject of fairness evaluation in text generation AI
- **[Responsible AI](Responsible-AI.md)** — Fairness is a core element
- **[Machine Learning](Machine-Learning.md)** — The application domain for fairness metrics
- **[Data Bias](Data-Bias.md)** — The root cause of bias

## Frequently Asked Questions

**Q: Does completely fair AI exist?**
A: No. Training data and algorithm design always involve choices, making perfect neutrality impossible. However, keeping it within acceptable ranges is possible.

**Q: Which takes priority—fairness or accuracy?**
A: Case by case. For critical decisions like hiring and lending, prioritize fairness. For medical diagnosis, balance is important.

**Q: What implementation tools exist?**
A: Major companies have open-sourced tools including Fairlearn (Microsoft), AIF360 (IBM), and Fairness Indicators (Google).
