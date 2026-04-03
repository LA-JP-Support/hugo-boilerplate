---
title: Market Basket Analysis
date: 2025-12-19
lastmod: 2026-04-02
translationKey: market-basket-analysis
description: Market Basket Analysis identifies product purchase patterns, discovering which products customers buy together to identify cross-sell opportunities using mathematical methods.
keywords:
- Market Basket Analysis
- association analysis
- cross-sell
- purchase patterns
- recommendation
category: Data & Analytics
type: glossary
draft: false
url: /en/glossary/market-basket-analysis/
---

## What is Market Basket Analysis?

**Market Basket Analysis discovers co-purchase patterns from transaction data like "customers buying product A also tend to buy product B" and applies findings to store layout, cross-selling, and bundle sales.** Algorithms like Apriori mechanically extract frequently co-purchased product sets, forming the basis for marketing initiatives. Originating in retail, it now applies across e-commerce, finance, healthcare, and other sectors.

> **In a nutshell:** The technique of mathematically discovering patterns like "beer buyers also buy potato chips" and leveraging this for sales growth.

**Key points:**

- **What it does:** Discover inter-product relationships from purchase patterns
- **Why it matters:** Present complementary products at right times and places to increase sales
- **Who uses it:** Retailers, e-commerce companies, marketing analysts

## Why it matters

Research shows that displaying "butter" where customers buy "bread" increases impulse purchase rate to 70%. Market Basket Analysis discovering such relationships enables store layout optimization increasing sales. Additionally, Amazon's "customers who purchased this also bought" feature applies Market Basket Analysis, reportedly generating 20-30% of total revenue.

## How it works

The process follows four steps. First, **data collection** accumulates all transactions (customer ID, purchased items, timing) into a database. Next, **algorithm application** runs the Apriori algorithm extracting all frequent itemsets (like "bread+butter" and "beer+chips"). Then, **rule generation** creates rules like "bread→butter" (70% confidence), calculating their strength ([Lift](Lift.md) values). Finally, **implementation** translates findings into actions like "position butter prominently in bread section to increase butter sales 20%."

## Real-world use cases

**Grocery store sales improvement**
Analysis discovered "bread→butter" (70% confidence, 2.5 lift=2.5x normal purchases) → positioned butter prominently in bread section → achieved 15% butter sales increase, 8% increase in average customer purchase.

**Online store recommendations**
Analysis discovered "65% of laptop buyers also purchase mice" → added "frequently bought together" section to product pages → achieved 12% conversion improvement.

**Financial product cross-selling**
Analysis discovered "40% of account openers apply for credit cards within 3 months" → implemented gradual card benefit promotion in post-opening emails → achieved 35% application rate improvement.

## Benefits and considerations

**On the benefits side,** discovered relationships are data-driven with higher effectiveness than intuition-based initiatives. Large datasets enable automatic discovery of complex patterns humans miss. Multi-industry applicability means with expertise, findings apply across sectors.

**As for considerations,** discovered relationships don't necessarily mean causation ("bread+butter" is causal, but "beer+diapers" may be coincidental timing). Rare, high-value products may be filtered out for insufficient frequency. Dynamic adaptation to seasonal variations and trend changes is essential.

## Related terms

- **[Data Mining](Data-Mining.md)** — Foundation technology for Market Basket Analysis
- **[Cross-Sell](Cross-Sell.md)** — Application scenario for analysis findings
- **[Recommendation](Recommendation.md)** — Feature leveraging analysis results
- **[Apriori Algorithm](Apriori.md)** — Most common implementation algorithm
- **[Conversion Rate](Conversion-Rate.md)** — Effectiveness measurement metric for analysis

## Frequently asked questions

**Q: How much data is needed?**
A: Generally, 10,000+ transactions enable reliable pattern extraction. Amount varies by industry and product count.

**Q: Can I discover patterns for new products?**
A: No, new products lack history for discovering relationships with existing products. Start with manual classification or hypothesis-driven assumptions.

**Q: How do you handle seasonal variations?**
A: Rerun analysis regularly (monthly) and monitor pattern changes. Applying different rules by season is effective.
