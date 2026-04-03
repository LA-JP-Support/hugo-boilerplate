---
title: Core Web Vitals
date: 2025-12-19
lastmod: 2026-04-02
translationKey: Core-Web-Vitals
description: Three web experience metrics defined by Google. Measures page load speed, responsiveness, and stability, affecting SEO rankings.
category: Web Development & Design
type: glossary
draft: false
url: /en/glossary/core-web-vitals/
keywords:
- Core Web Vitals
- LCP
- FID
- CLS
- Page speed
---

## What is Core Web Vitals?

**Core Web Vitals are "three critical web user experience measurement metrics" defined by Google.** Specifically: "LCP (load speed)," "INP (responsiveness, formerly FID)," and "CLS (visual stability)."

These metrics quantify "how comfortable users find your site when using it." Since 2021, Google incorporates these metrics into search ranking algorithms, making them unavoidable for web creators.

> **In a nutshell:** Core Web Vitals is a "report card" showing "how comfortable your website is for users."

**Key points:**

- **What it does:** Measure web page user experience quality through three metrics
- **Why it's needed:** Directly impacts SEO rankings and user satisfaction
- **Who uses it:** Website operators, web developers, marketers

## Calculation methods and targets

Core Web Vitals comprises three metrics.

**LCP (Largest Contentful Paint)**

Calculation: Time from page load start until the largest visible element (text or image) fully loads.

Target: Below 2.5 seconds is "good," 4+ seconds requires improvement.

**INP (Interaction to Next Paint)**

Calculation: Time from user click/tap to next screen display.

Target: Below 200 milliseconds is "good," 500+ milliseconds requires improvement.

**CLS (Cumulative Layout Shift)**

Calculation: How much layout elements move during page load (ad insertion, image load delays, etc.).

Target: Below 0.1 is "good," 0.25+ requires improvement.

Google provides tools like "PageSpeed Insights" and "Search Console" to measure these metrics.

## Why it matters

Core Web Vitals are the only official metrics for quantifying [user experience](User-Experience.md) quality. Since they affect Google search rankings, they directly impact SEO and organic traffic.

For example, 4-second LCP "may lower search position" compared to 2.5 seconds, with major business impact. Additionally, user psychology dictates "slow page load = bad site," increasing bounce rate.

## How it works

Core Web Vitals measurement is based on actual user behavior data.

**Step 1 is data collection.** A JavaScript library (Web Vitals library) embedded on the site records user metrics while visitors use it.

**Step 2 is data transmission.** Collected data is sent to Google servers and aggregated, called CrUX (Chrome User Experience Report).

**Step 3 is analysis and improvement.** PageSpeed Insights and Search Console show "your site's score." Development teams improve failing items. Improvement examples: image optimization, JavaScript lazy loading, server response time reduction.

## Real-world use cases

**E-commerce conversion rate improvement**

A major fashion e-commerce site improved Core Web Vitals, reducing LCP from 4 to 2 seconds. Result: 20% bounce rate drop, 15% conversion rate increase. SEO ranking improved, organic traffic increased 30%.

**News site page views increase**

A news site focused on layout stability (CLS improvement) and load speed. Improved CLS from 0.5 to 0.08. Articles per user increased from 2.3 to 3.5 pages.

**Corporate site user satisfaction improvement**

A B2B company aligned Core Web Vitals scores to "good" levels, creating user psychology of "trustworthy site," improving inquiry rates.

## Benefits and considerations

Core Web Vitals' greatest benefit is **Google's official designation clarifies SEO priorities.** Clear direction on what to do; improvement effects are easily measured.

Quantifying user experience improvements helps convince development teams of needed improvements.

However, improvement requires technical knowledge. INP (responsiveness) improvement especially needs JavaScript optimization, often requiring expert help. Improvements take time with no immediate results, requiring long-term perspective.

## Related terms

- **[Page Speed](Page-Speed.md)** — General load speed term including Core Web Vitals (LCP).
- **[User Experience (UX)](User-Experience.md)** — Quality measured by Core Web Vitals.
- **[SEO](SEO.md)** — Core Web Vitals is one SEO ranking factor.
- **[PageSpeed Insights](PageSpeed-Insights.md)** — Google's official tool for measuring Core Web Vitals.
- **[CrUX](CrUX.md)** — Chrome User Experience Report; Core Web Vitals data source.

## Frequently asked questions

**Q: Does poor Core Web Vitals directly lower rankings?**

A: Possibly. Google explicitly states "Core Web Vitals affect search rankings." However, exceptional content quality may partially offset this.

**Q: Where should I start improving Core Web Vitals?**

A: Check PageSpeed Insights "needs improvement" items and prioritize. Image optimization typically has high impact and relative easy implementation.

**Q: Should mobile and desktop be improved separately?**

A: Yes. Different user environments produce different scores. Tools separate "mobile" from "desktop," requiring improvements on both.
