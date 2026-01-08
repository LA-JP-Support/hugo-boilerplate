---
title: "CAGR (Compound Annual Growth Rate)"
lastmod: 2025-12-18
date: 2025-12-18
translationKey: "cagr-compound-annual-growth-rate"
description: "CAGR is the steady annual growth rate that smooths out yearly ups and downs, showing how much an investment or business metric grows on average each year over time."
keywords: ["CAGR", "Compound Annual Growth Rate", "investment growth", "financial metric", "growth rate"]
category: "Finance"
type: "glossary"
draft: false
---

## What is CAGR?

Compound Annual Growth Rate (CAGR) is a financial metric that describes the mean annual growth rate of an investment or metric over a specified period, assuming profits are reinvested and growth compounds each year. CAGR answers the question: *At what consistent annual rate would an investment grow, compounded annually, to turn its beginning value into its ending value over a period of time?*

Unlike simple averages, CAGR smooths out year-to-year fluctuations, providing a single, standardized rate that reflects the effect of compounding. This makes it invaluable for comparing investments, business units, or metrics over time, even when actual growth is volatile or inconsistent.

CAGR is not a true rate of return—it doesn't reflect volatility, risk, or interim cash flows. Instead, it provides a smoothed, annualized growth rate that simplifies comparisons and enables clearer performance assessment. For investments or metrics with erratic annual returns, CAGR is especially helpful for understanding long-term trends.

## Why Use CAGR?

**Fair Comparisons**CAGR provides an apples-to-apples comparison across different investment periods, business units, or growth metrics.

**Smooths Volatility**Wild annual swings don't distort the long-term picture. CAGR shows steady growth needed to reach final values.

**Business Applications**Commonly used for tracking sales, revenue, user growth, market share, and other compounding metrics.

**Investment Analysis**Enables straightforward comparison of mutual funds, stocks, portfolios, and other investments with different volatility profiles.

### When NOT to Use CAGR

**Irregular Cash Flows**When timing of investments or withdrawals matters, use Internal Rate of Return (IRR) instead.

**Short or Volatile Periods**CAGR is most reliable for longer, less volatile data sets.

**Risk Assessment**CAGR doesn't capture volatility or downside risk. Pair with standard deviation or Sharpe ratio for complete analysis.

## Mathematical Formula

### Standard Formula

\[
\text{CAGR} = \left( \frac{\text{Ending Value}}{\text{Beginning Value}} \right)^{1/n} - 1
\]

Where:
- **Ending Value (EV):**Value at the end of the period
- **Beginning Value (BV):**Value at the start of the period
- **n:**Number of periods (usually years)

### Expressed as Percentage

\[
\text{CAGR (\%)} = \left[ \left( \frac{EV}{BV} \right)^{1/n} - 1 \right] \times 100
\]

### Key Assumption
This formula assumes all interim gains are reinvested and no cash is added or withdrawn during the period.

## Step-by-Step Calculation Examples

### Example 1: Investment Growth

You invest $10,000 in a technology company. After five years, it's worth $15,000. What is the CAGR?

**Inputs:**- Beginning Value (BV) = $10,000
- Ending Value (EV) = $15,000
- Number of Years (n) = 5

**Calculation:**1. \( EV / BV = 15,000 / 10,000 = 1.5 \)
2. \( 1.5^{1/5} \approx 1.08447 \)
3. Subtract 1: \( 1.08447 - 1 = 0.08447 \)
4. Convert to percentage: \( 0.08447 \times 100 = 8.45\% \)

**Result:**CAGR is **8.45%**per year.

### Example 2: Business Revenue Growth

A chatbot company's revenue grows from $2 million to $5 million in 4 years.

**Inputs:**- BV = $2,000,000
- EV = $5,000,000
- n = 4

**Calculation:**\[
\text{CAGR} = (5,000,000 / 2,000,000)^{1/4} - 1 = 2.5^{0.25} - 1 \approx 0.26 = 26\%
\]

**Result:**Revenue grew at **26%**annually.

### Example 3: Negative Growth

An investment falls from $1,000 to $900 over 3 years.

**Inputs:**- BV = $1,000
- EV = $900
- n = 3

**Calculation:**\[
\text{CAGR} = (900 / 1,000)^{1/3} - 1 = 0.9^{0.333} - 1 \approx -0.0345 = -3.45\%
\]

**Result:**Investment declined at **-3.45%**annually.

### Example 4: Volatile Returns

An investment grows 25% in year one, then drops 25% in year two.

**Year-by-Year:**- Year 1: $1,000 × 1.25 = $1,250
- Year 2: $1,250 × 0.75 = $937.50

**CAGR Calculation:**\[
\text{CAGR} = (937.5 / 1,000)^{1/2} - 1 \approx -0.0318 = -3.18\%
\]

**Result:**Despite 0% average annual return, compound return is **-3.18%**.

## Key Use Cases and Applications

### Investment Performance Comparison
Compare long-term performance of investments with different volatility profiles but same time horizon. Example: comparing two mutual funds over 10 years.

### Business Growth Measurement
Track growth in revenue, profits, users, or market share over multiple years. Example: AI chatbot company reports 40% CAGR in active users.

### Forecasting and Goal Setting
Project future values based on historical growth rates. Example: estimating next year's user base if adoption grew at 25% CAGR.

### Benchmarking and Industry Analysis
Compare company CAGR against industry averages to assess competitiveness and identify market trends.

### Technology Adoption (AI & Automation)
Measure compounded growth rate of AI chatbot deployments, automation revenue, or customer queries handled by AI systems.

## Advantages of CAGR

- **Simplicity:**Single, standardized number for growth over a period
- **Comparability:**Direct comparison across investments, business units, or sectors
- **Reflects Compounding:**Shows actual annualized compounded growth, unlike arithmetic averages
- **Universal Applicability:**Useful for any compounding metric—revenue, users, sales, etc.

## Limitations of CAGR

**Assumes Constant Growth**Real-world growth is rarely steady. CAGR smooths volatility, which may mislead.

**Ignores Volatility and Risk**Doesn't capture year-to-year fluctuations or investment risk.

**No Cash Flow Consideration**Ignores interim deposits or withdrawals. Use IRR for cash flow-sensitive analysis.

**Not a Predictor**Past CAGR doesn't guarantee future performance.

**Misleading for Short/Volatile Periods**More reliable for longer, less volatile datasets.

## CAGR vs. Average Annual Return

**CAGR (Geometric Mean)**Reflects compounding. If $1,000 grows to $1,331 in 3 years:
\[
\text{CAGR} = (1331/1000)^{1/3} - 1 \approx 10\%
\]

**Average Annual Return (Arithmetic Mean)**Simple average. If returns are +20%, -10%, +15%:
\[
\text{Average} = (20 - 10 + 15)/3 = 8.3\%
\]

The arithmetic average overstates actual compounded growth. CAGR provides the true compounding rate.

## Industry-Specific Benchmarks

### What is a "Good" CAGR?

There's no universal answer. Context depends on investment type, market conditions, and risk tolerance.

**Savings Accounts**Typically <2% CAGR

**Stock Markets**Historically 6–10% CAGR over long periods

**High-Growth Sectors (AI, Tech)**CAGRs of 20%+ are common but with higher risk

**Business Revenue**- Mature companies: 5–15%
- Growth companies: 20–40%
- Startups: 50%+

## Frequently Asked Questions

**How does CAGR differ from Average Annual Growth Rate (AAGR)?**CAGR is geometric mean reflecting compounding. AAGR is arithmetic mean that doesn't reflect compounding and can be misleading with volatile returns.

**Can CAGR be used for metrics other than investments?**Yes. CAGR works for sales, revenues, user counts, market share, or any compounding metric.

**Does CAGR consider risk or volatility?**No. CAGR only shows smoothed average growth. Pair with risk metrics like standard deviation or Sharpe ratio.

**What if there are cash inflows or outflows?**CAGR doesn't account for interim cash flows. Use Internal Rate of Return (IRR) for investments with ongoing deposits or withdrawals.

**How is CAGR used in AI Chatbot & Automation?**Measures annualized growth of chatbot deployments, automation revenue, or queries handled—essential for benchmarking technology adoption.

## Practical Tips

**For Investors**- Use CAGR to compare funds with different volatility
- Always consider risk-adjusted returns
- Review CAGR over multiple time periods

**For Business Analysts**- Track CAGR for revenue, users, and key metrics
- Compare against industry benchmarks
- Use for forecasting and strategic planning

**For Technology Leaders**- Measure adoption rates of AI and automation
- Benchmark against industry growth rates
- Set realistic growth targets

## References


1. Corporate Finance Institute. (n.d.). What is CAGR?. Corporate Finance Institute.
2. Wall Street Prep. (n.d.). CAGR Formula and Calculations. Wall Street Prep.
3. Wall Street Prep. (n.d.). CAGR vs. AAGR. Wall Street Prep.
4. ICICI Direct. (n.d.). CAGR Calculator. ICICI Direct.
5. Investopedia. (n.d.). Compound Annual Growth Rate. Investopedia.
6. Groww. (n.d.). CAGR Definition & Calculator. Groww.
7. Public.com. (n.d.). What is CAGR?. Public.com.
8. Corporate Finance Institute. (n.d.). IRR vs. CAGR. Corporate Finance Institute.
9. YouTube. (n.d.). What is CAGR? Compound Annual Growth Rate Explained. YouTube.
10. YouTube. (n.d.). CAGR vs. Average Annual Return. YouTube.
