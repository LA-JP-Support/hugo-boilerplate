---
title: Data Preprocessing
date: 2025-12-19
lastmod: 2026-04-02
translationKey: data-preprocessing
description: Data Preprocessing is the process of transforming raw data into a format suitable for machine learning and analysis. Critical for quality improvement and model performance.
keywords:
- Data Preprocessing
- Data Cleaning
- Feature Engineering
- Data Transformation
- Machine Learning Preparation
category: Data & Analytics
type: glossary
draft: false
url: /en/glossary/Data-Preprocessing/
---

## What is Data Preprocessing?

**Data Preprocessing transforms raw, incomplete data into clean, structured formats suitable for machine learning and analysis.** It includes filling missing values, removing duplicates, handling anomalies, and standardizing data types. Data scientists spend 60-80% of practical time on this critical phase that heavily influences model performance.

> **In a nutshell:** Like cooking preparation—washing vegetables, peeling, cutting. Sloppy preparation ruins excellent ingredients.

**Key points:**

- **What it does:** Cleans raw data, preparing it for analysis
- **Why it's needed:** Directly improves model accuracy and reduces errors
- **Who uses it:** Data scientists, analysis engineers, data engineers primarily

## Why it matters

Real-world data is always incomplete. Missing values (unenteredinfo), outliers (abnormal values), format inconsistencies (inconsistent date formats), duplicate records (customers registered twice) are common.

Providing these problems to models causes inaccurate learning and reduced prediction accuracy. For example, "999" as customer age completely distorts average age calculation. Preprocessing corrects problems pre-model, allowing accurate pattern learning and reliable predictions.

## How it works

Preprocessing consists of five major steps.

**Data Exploration** establishes overall dataset understanding—column count, row count, data types, missing value percentage, statistical characteristics. **Data Cleaning** removes duplicates and corrects obvious errors. For example, "2025-13-45" date becomes deleted or set to NULL.

**Missing Value Handling** deletes data with many missing values or supplements with mean/median for sparse missing data. **Outlier Handling** uses statistical methods (z-score analysis) identifying anomalies, choosing deletion or transformation. **Feature Engineering** creates new information from existing columns. For example, calculating "age" or "generation" from birthdate adds business-useful features.

Finally, [standardization and normalization](Normalization.md) unify numerical scales. Age (0-100) and income (0-10 million) differ vastly, preventing proper algorithm learning.

## Real-world use cases

**Credit Card Fraud Detection**

Banks building fraud-detection models encounter unprocessed transactions (NULL values) and system errors causing anomalies. Preprocessing removes outliers, fills missing data appropriately, adds time-of-day and weekday features enabling models to recognize fraud patterns more accurately.

**Customer Churn Prediction**

Telecom companies predict customer cancellation using profile data (with missing values), monthly fees, and support contact counts. Preprocessing fills missing data, identifies anomalies, creates "average monthly expense" and "support contact frequency" features dramatically improving prediction accuracy.

## Benefits and considerations

Maximum benefit: **improved model accuracy**. Clean data enables more accurate model learning. **Improved computational efficiency** matters—removing unnecessary columns reduces memory usage and shortens learning time. **Enhanced interpretability** helps—properly processed data makes result explanations easier.

Considerations: **information loss from over-processing**. Deleting all outliers removes valuable information (e.g., new fraud patterns). **[Privacy](Data-Privacy.md) balance** is important—removing personal identifiers while retaining analysis-necessary information requires care. **Reproducibility** is challenging—unclear preprocessing documentation prevents identical treatment of new data.

## Related terms

- **[Data Cleaning](Data-Cleaning.md)** — First preprocessing stage
- **[Feature Engineering](Feature-Engineering.md)** — New feature creation
- **[Data Profiling](Data-Profiling.md)** — Pre-preprocessing analysis
- **[Outlier Detection](Outlier-Detection.md)** — Anomaly identification
- **[Normalization](Normalization.md)** — Data scale unification

## Frequently asked questions

**Q: What missing data percentage warrants column deletion?**

A: Generally 50% missing justifies deletion consideration. However, if business-critical, supplementation is worth trying. Domain knowledge and business requirements guide judgment.

**Q: Should we delete all outliers?**

A: No. Outliers sometimes contain crucial information. For fraud detection, unusual transactions (outliers) are important. Recording outliers and investigating causes matters more.

**Q: Should training and test data use identical preprocessing?**

A: Yes, critically important. Use training data statistics (mean, minimum) to transform test data identically. This enables fair evaluation.
