---
title: PageSpeed Insights
date: 2026-01-29
lastmod: 2026-04-02
translationKey: pagespeed-insights
description: Google's web performance analysis tool that measures Core Web Vitals and provides actionable recommendations for improving page speed.
keywords:
- PageSpeed Insights
- Core Web Vitals
- Web Performance
- Google Tool
- Page Speed
category: Data & Analytics
type: glossary
draft: false
url: /en/glossary/PageSpeed-Insights/
---

## What is PageSpeed Insights?

**PageSpeed Insights is a free web performance analysis tool developed by Google.** It evaluates web page load speed and user experience on both mobile and desktop devices. It combines real user data from Chrome User Experience Report (CrUX) with lab testing from Lighthouse to provide comprehensive performance perspective. It measures critical metrics like First Contentful Paint (FCP), Largest Contentful Paint (LCP), and Cumulative Layout Shift (CLS), providing specific page speed improvement recommendations.

> **In a nutshell:** A tool where Google tells you "how fast your website is and what to improve."

**Key points:**

- **What it does:** Evaluates page speed and experience quality on a 0-100 scale
- **Why it's needed:** Page speed affects user satisfaction and search rankings
- **Who uses it:** Web masters, developers, digital marketers

## Calculation method

PageSpeed Insights scores calculate from multiple metrics. **Core Web Vitals** (LCP, FID/INP, CLS) are most important, with other metrics (FCP, SI, TTI, etc.) also included. Scores range 0-100, where 90-100 is excellent (green), 50-89 needs improvement (orange), 0-49 is poor (red). Both actual user experience data (field data) and controlled-environment test results (lab data) appear.

## Targets and benchmarks

Good performance targets:

- **Largest Contentful Paint (LCP):** 2.5 seconds or better is good
- **First Input Delay (FID):** 100 milliseconds or better is good
- **Cumulative Layout Shift (CLS):** 0.1 or lower is good
- **Overall score:** 90 or above is excellent

Industry averages are 50-60 points, with mobile typically lower than desktop. E-commerce and heavy-content sites should aim for 60+ points, media sites for 70+.

## Why it matters

Page speed significantly impacts user experience — slow loading increases bounce rates. Search engines also use page speed as a ranking factor, making performance improvement a key SEO component. PageSpeed Insights shows specific improvements, allowing you to prioritize efficiently.

## How it works

PageSpeed Insights analyzes websites in two ways. **Field data** collects actual user experience from Chrome browsers over the past 28 days. **Lab data** simulates pages in standardized environments. Field data shows the real world; lab data provides diagnostics. Together they provide comprehensive performance pictures.

## Real-world use cases

**E-commerce optimization**
When product pages or checkout processes show low speed, prioritize image compression and code optimization. Post-improvement conversion rate increases.

**Content site improvement**
Third-party ads often become major bottlenecks on blogs and news sites. For poor LCP, consider delayed ad script loading.

**Mobile optimization**
For sites with mostly mobile users, prioritize mobile score improvement. Responsive images and font optimization are effective.

## Benefits and considerations

**Benefits:** PageSpeed Insights is simple to implement and free. Specific improvement suggestions help prioritization.

**Considerations:** Scores are relative — 90 points doesn't guarantee perfection. Monitoring actual user experience matters. Lab and field data sometimes diverge, requiring consultation of both.

## Related terms

- **Core Web Vitals** — The main metrics PageSpeed Insights measures
- **Lighthouse** — The diagnostic tool PageSpeed Insights uses
- **LCP** — The most critical Core Web Vitals metric
- **User Experience** — The experience quality page speed delivers
- **SEO** — Page speed as a ranking consideration
