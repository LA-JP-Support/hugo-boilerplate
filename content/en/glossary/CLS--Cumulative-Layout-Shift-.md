---
title: CLS (Cumulative Layout Shift)
date: 2025-12-19
lastmod: 2026-04-02
translationKey: CLS--Cumulative-Layout-Shift-
description: CLS measures how much page elements unexpectedly shift during loading, expressed as a value between 0 and 1. Lower scores are better.
keywords:
- CLS
- Cumulative Layout Shift
- Web performance
- Visual stability
- Core Web Vitals
category: Web Development & Design
type: glossary
draft: false
url: /en/glossary/cls--cumulative-layout-shift-/
---

## What is CLS (Cumulative Layout Shift)?

**CLS measures how much page elements unexpectedly shift during loading, expressed as a value between 0 and 1. Lower values mean the page is more stable.** Have you ever opened a webpage and suddenly an ad appeared, pushing the entire page down? Or a button moved and you clicked the wrong thing? This is called "layout shift," and it frustrates users. Google recognized this problem and created the CLS metric to measure it, incorporating it into SEO rankings.

> **In a nutshell:** CLS measures how much elements move on your page during loading. Less movement means a lower score (which is good).

**Key points:**
- **What it does:** Measures web page visual stability with a number between 0 and 1
- **Why it matters:** Unexpected element movement causes accidental clicks and harms user experience and business results
- **Who cares:** Web designers, front-end developers, marketing managers

## How It's Calculated

CLS is calculated by multiplying two values: (1) Impact fraction—what percentage of the page's visible area does the shifted element occupy, and (2) Distance fraction—how much does the element move relative to the viewport. For example, if 50% of the page shifts by 25%, the CLS score is 0.5 × 0.25 = 0.125.

Layout shifts only count if they happen unexpectedly. When a user clicks a button and the display changes, that shift isn't counted.

## Benchmarks and Targets

**Below 0.1: "Good"** — Virtually no unexpected shifts; the page is smooth. **0.1–0.25: "Needs improvement"** — Noticeable shifts that should be fixed. **0.25 and above: "Poor"** — Serious problems requiring immediate action. Google targets 0.1 or below, so aim for that number.

## Why It Matters

In 2020, Google added "page experience" alongside page speed as a SEO ranking factor. Sites with good CLS scores rank higher in search results and get more organic traffic. Poor CLS scores lower your ranking and hurt business. From a usability perspective, shifting pages frustrate users and increase bounce rates.

## Real Improvement Examples

**Specify Image Dimensions** — When images load without width and height specified, layout shifts happen. Using HTML width/height attributes or CSS aspect ratio reserves space in advance and prevents shifts.

**Reserve Space for Ads** — Pre-allocate space for ads that load later so article content doesn't get pushed down.

**Optimize Font Loading** — Use the font-display property to control loading order so shifts don't occur while web fonts load.

## Related Terms

- **[Web Vitals](Web-Vitals.md)** — Google's three-metric set measuring web site health
- **[LCP (Largest Contentful Paint)](LCP.md)** — Time until the largest content element appears
- **[FID (First Input Delay)](FID.md)** — Time from user click to page response
- **[SEO](SEO.md)** — Optimizing to rank higher in search engines
- **[User Experience](User-Experience.md)** — Overall user satisfaction with websites

## Frequently Asked Questions

**Q: My CLS score exceeds 0.1. Do I need to fix it immediately?**
A: Yes, improve it as soon as possible. Especially on e-commerce sites, unexpected shifts can cause accidental purchases and costly mistakes.

**Q: Why does my mobile CLS differ from my desktop CLS?**
A: Screen sizes differ, changing impact measurements. Mobile screens are smaller, so the same pixel movement looks proportionally larger.

**Q: Do shifts from user actions (like clicking a button) count toward CLS?**
A: No. CLS only counts "unexpected" shifts. Changes resulting from user interaction aren't counted.
