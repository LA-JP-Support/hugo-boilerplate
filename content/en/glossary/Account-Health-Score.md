---
title: Account Health Score
date: 2025-12-19
lastmod: 2026-04-02
translationKey: Account-Health-Score
description: A composite metric measuring the overall health and sustainability of a customer account, used to predict churn and identify expansion opportunities.
keywords:
  - Account health score
  - Customer success metrics
  - Churn prediction
  - Account management
  - Customer retention
category: Data & Analytics
type: glossary
draft: false
url: /en/glossary/account-health-score/
aliases:
  - /en/glossary/Account-Health-Score/
---

## What is Account Health Score?

**Account Health Score is a composite metric that quantifies the overall health and sustainability of a customer account, used for early churn risk detection and expansion opportunity identification.** It integrates multiple data points—product usage patterns, support ticket frequency, payment history, engagement level—into a score from 0-100 or color-coded categories (red/yellow/green). Higher scores indicate healthier accounts with better sustainability and greater expansion potential.

> **In a nutshell:** "Like a patient health checkup. Just as doctors combine blood pressure, weight, and cholesterol readings to assess overall health, Account Health Score combines multiple customer activity signals to answer: 'Is this customer healthy right now?'"

**Key points:**

- **What it does:** Processes multiple behavioral indicators algorithmically to visualize account continuation risk and expansion opportunities
- **Why it matters:** Optimally allocates limited customer success resources, enables proactive intervention to prevent churn, and maximizes lifetime value
- **Who uses it:** Customer success managers, sales managers, executives, SaaS and subscription companies

## Why it matters

SaaS companies historically faced 30-40% annual customer churn as industry standard. However, churn rarely happens suddenly—warning signs appear months in advance: declining usage frequency, increased support tickets, key personnel changes. These leading indicators allow intervention before it's too late.

Traditional approaches become apparent only at churn notification—too late to prevent. Account Health Score automatically detects these early indicators, creating intervention time. Research shows accounts with health scores below 60 have 80%+ churn probability—proof that the score has predictive power.

Higher-scored accounts (80+) enable efficient upsell targeting. Expansion deals to already-satisfied customers close at 3-5x the rate of new sales.

## How it works

Account Health Score operates across multiple layers. First, **data collection** gathers signals from CRM, product analytics, support systems, and billing systems. Next, **normalization** converts different units (user count, login frequency, dollar payments) to a common comparable scale.

Then **weighting** is applied. Product usage frequency might receive 30% weight (high predictive power), support tickets 20%, payment reliability 25%, etc. Machine learning models calculate optimal weights from historical data.

Weighted indicators feed into a **score calculation algorithm**, producing composite scores from simple linear addition to complex ML models. Generated scores trigger **automated alerts**—scores below 60 flag for immediate review; below 40 require escalation. Finally, **dashboard visualization** enables customer success managers to intuitively understand risk and opportunity.

## Calculation method

Example weighted average model:

Score = (Product Usage × 0.30) + (Engagement × 0.25) + (Support Satisfaction × 0.20) + (Payment Reliability × 0.15) + (Contract Value Trend × 0.10)

Each element normalizes to 0-100 values. More sophisticated models consider element interactions (for example, declining usage despite continued payment).

## Benchmarks

- **80-100: Very Healthy** – Expansion targets, minimal churn risk
- **60-79: Healthy** – Standard support, improvement opportunities
- **40-59: At Risk** – Manager engagement, deep diagnostic needed
- **0-39: Critical** – Executive involvement, recovery plan required

## Related terms

- **[Churn (Customer Attrition)](/en/glossary/Churn/)** – Customers not renewing or canceling; the score predicts this
- **[Customer Success](/en/glossary/Customer-Success/)** – Supporting customers to achieve goals; the score prioritizes efforts
- **[Customer Lifetime Value (CLV)](/en/glossary/Customer-Lifetime-Value/)** – Total customer value over time; healthy accounts have higher CLV
- **[SaaS Metrics (MRR, ARR)](/en/glossary/SaaS-Metrics/)** – Monthly/annual recurring revenue tracked; part of score input data
- **[Predictive Analytics](/en/glossary/Predictive-Analytics/)** – Forecasting future trends from historical data; the score is an application

## Frequently asked questions

**Q: Which data points matter most in score calculation?**
A: Product usage (login frequency, feature adoption) typically has highest predictive power, followed by payment reliability. However, optimal metrics vary by business model and industry—validation on your own data is essential.

**Q: How should we respond to low-scoring accounts?**
A: Below 60: Schedule a "business review" meeting. Below 40: Assemble a response team including sales and leadership. Listen to root causes and present solutions.

**Q: Can we automate actions based on score (like auto-emails)?**
A: Full automation is not recommended. Use score declines to trigger human review, assess customer context, then apply personalized approaches.
