---
title: "Data Cleaning"
date: 2025-03-01
lastmod: 2026-04-02
description: "The process of identifying and correcting missing values, duplicates, and inconsistencies to improve data quality for analysis."
translationKey: "data-cleaning"
category: "Data & Analytics"
type: glossary
draft: false
url: /en/glossary/Data-Cleaning/
keywords:
  - Data Quality
  - Missing Value Handling
  - Data Preparation
  - Preprocessing
---

## What is Data Cleaning?

**Data cleaning is the process of detecting and correcting missing values, duplicate records, format errors, and inconsistencies in collected data to prepare it for analysis.** Real-world data always exists in "dirty" states. Data entry typos, system integration gaps, measurement errors, and outdated information mixing create problems. Without data cleaning, analysis results are based on flawed data—"garbage in, garbage out."

> **In a nutshell:** Finding and fixing errors and defects in data to make it usable and clean.

**Key points:**

- **What it does:** Fix missing values, eliminate duplicates, unify formats, and correct anomalies
- **Why it's needed:** Ensure data quality and increase analysis reliability
- **Who uses it:** Data engineers, data scientists, business analysts

## Why it matters

Data quality and analysis accuracy are directly correlated. A famous statistics saying—"Garbage In, Garbage Out"—is absolutely true. Training statistical models on data with missing values produces biased pattern learning, reducing accuracy. When the same customer appears as both "Yamada Taro" and "Yamada  Taro" (spacing difference), analysis misidentifies the same customer as multiple people, leading to incorrect customer value assessment.

Data cleaning investment dramatically affects final analysis quality. Typically, 50–70% of data analysis project hours go to data cleaning and [normalization](Data-Normalization.md). This is not wasted effort—high-quality data makes subsequent analysis exponentially more efficient, producing more trustworthy results.

## How it works

Data cleaning involves multiple sequential steps.

**Missing value detection and handling** is the first important step. When data cells lack values, missing calculations error. Analyzing absence patterns is critical. "Fewer than 5% missing overall" justifies imputation (filling missing values via average, neighboring values, etc.). "Entire columns missing" may require column exclusion. Determining if absence is "random distribution" or "concentrated in specific segments" (e.g., pre-2020 data) changes approaches.

**Duplicate record elimination** identifies and removes multiple registrations of the same entity. Exact matches (all columns identical) are easily detected, but subtle differences (spacing, spelling variations) require distance metrics and fuzzy matching. [Outlier detection](Outlier-Detection.md) techniques help identify statistically equivalent duplicates.

**Format unification and anomaly correction** ensure data consistency. When dates exist as "2024-01-01," "01/01/2024," and "January 1, 2024," converting to unified format is necessary. Phone numbers as "090-xxxx-yyyy" and "0120-xxxx-xxxx" formats require standardization. [Outlier detection](Outlier-Detection.md) identifies statistically anomalous values (age 999, negative prices) for correction or exclusion.

**Validity validation** applies business rule checks. "Customer withdrawal date before registration date," "negative product prices," or "transaction amounts 100x normal" represent logical contradictions needing detection.

## Real-world Use Cases

**CRM implementation data unification**

When organizations implement CRM systems, existing customer data from multiple tools (spreadsheets, legacy systems) requires migration. Data cleaning detects "same customer in multiple records," "inconsistent postal formats," and "missing telephone numbers," enabling accurate CRM migration.

**Real estate price analysis anomaly handling**

When real estate sites analyze nationwide property data, input errors create "Tokyo single-family house 10,000 yen" entries. Applying [outlier detection](Outlier-Detection.md) identifies statistically anomalous prices, improving market analysis accuracy.

**Medical record data quality improvement**

Hospital electronic record systems experience physician input inconsistency—"patient height recorded in cm or mm." Converting to unified format improves nutritional status accuracy and BMI calculation precision.

## Benefits and Considerations

**Maximum benefit** comes from analysis result trustworthiness and reproducibility substantially improving. High-quality data enables more accurate, sustainable decision-making. [Data discovery](Data-Discovery.md) and [predictive analytics](Predictive-Analytics.md) efficiency increase, directing more time to meaningful pattern finding.

**However, data cleaning requires enormous time and effort.** For large datasets, automation tools are essential, but humans must address problems tools miss (logical contradictions, business rule violations). Missing value filling and anomaly handling require domain knowledge, demanding data scientist and business department cooperation. Cleaning decisions ("is this anomaly real or error?") risk introducing bias affecting results.

## Related terms

- **[Outlier Detection](Outlier-Detection.md)** — Automatically detecting statistically anomalous values, key data cleaning element
- **[Data Normalization](Data-Normalization.md)** — The next step after cleaning, unifying different-scale data
- **[ETL](ETL-Extract-Transform-Load.md)** — Data cleaning is the "transform" stage of [ETL](ETL-Extract-Transform-Load.md) processes
- **[Data Integration](Data-Integration.md)** — Cleaning is prerequisite when combining multiple data sources
- **[Data Discovery](Data-Discovery.md)** — High-quality cleaned data improves discovery efficiency

## Frequently asked questions

**Q: What is the best missing value imputation method?**

A: It depends on absence mechanism and extent. When absence is under 5% randomly distributed, mean/median imputation works. When absence shows patterns (e.g., specific timeframe sensor failure), interpolation or model-based imputation works better. Always record imputation methods and verify sensitivity to imputation choices.

**Q: How much time does data cleaning take?**

A: Depends on dataset size and problem complexity, but typically occupies 50–70% of total project time. 1 million row CSVs require days to weeks; multi-system data integration requires months. Automation pipelines require initial time investment but make subsequent runs efficient.

**Q: How much automation can data cleaning tools provide?**

A: Tools (Apache Spark, Trifacta, OpenRefine) can automate roughly 70–80%, but complete automation is difficult. Business rule decisions ("is this value error or real data?") and complex pattern matching (similar record merging) require human involvement. Tool and human cooperation is most effective.
