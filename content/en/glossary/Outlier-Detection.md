---
title: Outlier Detection
date: 2025-03-01
lastmod: 2026-04-02
translationKey: outlier-detection
description: Outlier detection is a technology that automatically identifies statistically abnormal values in a dataset to ensure data quality.
keywords:
- Anomaly Detection
- Data Quality
- Statistical Analysis
- Machine Learning
category: Data & Analytics
type: glossary
draft: false
url: /en/glossary/Outlier-Detection/
---

## What is Outlier Detection?

**Outlier detection is a technology that automatically identifies values in a dataset that are statistically far removed from the vast majority.** Every dataset contains a certain percentage of "unusual" values. Sales data typically ranges 1-2 million yen monthly but might suddenly show 5 million yen. Customer age typically ranges 20-70, but values like "999" or "-50" sometimes appear as clear errors. These outliers stem from data entry errors, equipment failures, or unusual business events (like major contract wins). Outlier detection systematically identifies them to ensure data quality and discover anomalous business events.

> **In a nutshell:** Statistically detecting values that feel "different" in data and systematically confirming them.

**Key points:**

- **What it does:** Identify statistically abnormal values within datasets
- **Why it's needed:** Ensure data quality and discover hidden problems and opportunities
- **Who uses it:** Data engineers, data scientists, quality assurance managers

## Why it matters

Outliers significantly impact analysis results. Consider salary data: "100M, 200M, 150M, 180M, 1000M yen" for five employees averages 530M yen. But the 1000M might be executive compensation. As a representative value for regular employees, the average is useless. Excluding the outlier yields 158M yen, properly reflecting the situation.

Additionally, outliers sometimes hide critically important business information. In banking fraud detection, "100 times normal international wire transfer amount" is an outlier that signals money laundering. Missing such outliers means fraud goes undetected. Outlier detection thus serves two purposes: "removing data noise" and "discovering anomalous business events."

## How it works

Outlier detection approaches vary based on data characteristics and detection goals.

**Statistical outlier detection** assumes normal distribution and flags values beyond three standard deviations from mean. For example, mean 100 with standard deviation 10: range 70-130 is "normal," beyond that is outliers. Simple and intuitive but lacks robustness since outliers distort distribution shape. Robust statistical methods using median and interquartile range solve this.

**Distance-based detection** evaluates how far each data point is from others. The k-Nearest Neighbors algorithm calculates average distance to the five nearest points and flags values exceeding a threshold. This effectively handles multivariate data by considering multiple variables simultaneously.

**Machine learning-based detection** uses algorithms like Isolation Forest or One-Class SVM. These leverage the property that "anomalies are rare with different patterns" to detect outliers through unsupervised learning. Particularly effective for complex multivariate or nonlinear data.

## Real-world use cases

**Credit Card Fraud Detection**

Card companies process millions of daily transactions, using anomaly detection to identify outliers. Patterns like "same-day use in Japan and USA (physically impossible)" trigger alerts, and companies verify with cardholders.

**Medical Data Quality Assurance**

Hospital patient databases contain critical lab values and measurements. Outlier detection flags clearly wrong values like "patient height 500cm" or "glucose 1000mg/dL (exceeding device limits)," alerting physicians.

**Website Traffic Anomaly Detection**

Website operators detect anomalies in access logs. Normal hourly traffic is 1,000 accesses; sudden 1-million-access outliers indicate either DDoS attacks or viral content spread. Different responses are needed, making detection critical.

## Benefits and considerations

Major benefits include systematically identifying data quality issues and automatically detecting important anomalies. Manual data review misses outliers; automation ensures reliable detection. Additionally, investigating outlier causes reveals data collection process problems like sensor failures.

Challenges include context-dependency in defining "anomalies." A 10x sales increase is statistically abnormal but a business "opportunity," not noise to remove in data cleaning. Multivariate outliers (combinations unusual even if individual values aren't) get missed by univariate detection. For example, "age 40, income 2M yen" individually seem normal but the combination might be statistically unusual. Additionally, anomaly definitions change over time—pandemic-era online shop traffic might be 3x normal, establishing a new baseline.

## Related terms

- **[Data Cleaning](Data-Cleaning.md)** — Outlier detection is a key part, identifying and correcting invalid data
- **[Correlation Analysis](Correlation-Analysis.md)** — Outliers significantly change correlation coefficients; pre-analysis removal is important
- **[Data Normalization](Data-Normalization.md)** — Scaling with outliers becomes dominated by them; robust normalization is effective
- **[Data Discovery](Data-Discovery.md)** — Outliers often contain hidden business opportunities or problems
- **[Predictive Analytics](Predictive-Analytics.md)** — Models trained on data with outliers have lower accuracy; pre-processing removal is crucial

## Frequently asked questions

**Q: Should all outliers be excluded?**
A: No. Exclude "data entry errors" but retain "business-critical events." Distinguishing is difficult and requires [data cleaning](Data-Cleaning.md) teams collaborating with business units. Statistics should report both with and without outliers.

**Q: How should outlier thresholds be set?**
A: Industry standard uses three standard deviations (97.7% of data falls within), but it's not absolute. Stricter detection uses 2x (95% within), looser uses 3.5x. Important is basing thresholds on business requirements, not arbitrarily.

**Q: How do we detect multivariate outliers?**
A: Univariate detection (evaluating each variable independently) misses anomalies in variable combinations. Solutions include using multivariate algorithms like Isolation Forest or One-Class SVM, or performing principal component analysis on multiple variables then detecting outliers in that space.
