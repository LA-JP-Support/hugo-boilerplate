---
title: Lazy Loading
date: 2025-12-19
lastmod: 2026-04-02
translationKey: Lazy-Loading
description: A technique that delays content loading until needed. Improves page speed and conserves bandwidth through performance optimization.
keywords:
- Lazy Loading
- Deferred Loading
- Performance Optimization
- Web Development
- Image Loading
category: Web Development & Design
type: glossary
draft: false
url: /en/glossary/Lazy-Loading/
---

## What is Lazy Loading?

**Lazy loading is a performance optimization technique that loads page content only when users actually view it.** Rather than loading all images, videos, and scripts on page access, they load only when users scroll near them. This dramatically improves initial display speed.

> **In a nutshell:** Like borrowing only needed books from a library instead of reading everything on the shelf.

**Key points:**

- **What it does:** Defer content loading until needed
- **Why it matters:** Improves page speed and resource efficiency
- **Who uses it:** Web engineers, frontend developers

## Why it matters

Page speed directly impacts user experience and business outcomes. Google research shows over 40% of users abandon pages taking 3+ seconds. Image-heavy sites using traditional approaches take 10+ seconds. Lazy loading can reduce initial display to under 2 seconds, dramatically improving user satisfaction and [conversion rates](Conversion-Rate.md). Mobile users face bandwidth limits, so sending only necessary content is critical.

## How it works

Lazy loading follows a phased loading strategy. When users access the page, only first-view content loads. Intended scroll areas display grayed placeholders or skeleton screens signaling content presence. Intersection Observer API or scroll listeners continuously monitor when elements enter the viewport. As users scroll near elements, those resources begin loading. Upon completion, placeholders replace with actual content. This process is fully automatic.

Phased loading efficiently uses network and memory resources. Since non-visible content doesn't require preloading, server load reduces too. Mobile environments particularly benefit, where limited bandwidth prioritizes important content.

## How it's measured

Lazy loading effectiveness is measured by load time reduction. If traditional loading took 10 seconds for all content, achieving 2-second initial display represents 80% user experience improvement. In practice, [Core Web Vitals](Core-Web-Vitals.md) metric "Largest Contentful Paint (LCP)" measures this, targeting 2.5 seconds or below.

Data transmission reduction also matters. On 100MB image-heavy pages where users average 30% viewing, 70MB unnecessary transfer is eliminated.

## Benchmarks

| Scenario | Reduction Rate | Impact |
|----------|----------------|--------|
| Image-heavy sites | 50-70% | Major initial load improvement |
| E-commerce | 40-60% | Lower cart abandonment |
| News sites | 30-50% | Better bounce rate |
| Mobile | 20-40% | Reduced data usage |

Example: initial load 10 seconds → 2 seconds (80% reduction), data 150MB → 50MB (67% reduction).

## Real-world use cases

**E-commerce Product Lists**

With dozens of product images, loading only visible ones means 1-second initial display. Prevents bounce of users ready to purchase.

**Long Blog Articles**

With many illustrations and embedded videos, first 200 characters display in 0.5 seconds. Media loads during reading time.

**Infinite Scroll Search Results**

New results load as users scroll down. Maintains memory efficiency while engaging users.

## Benefits and considerations

Lazy loading dramatically improves initial speed and data efficiency. However, implementation requires attention. JavaScript-disabled environments need fallback functionality. Unset placeholder sizes cause layout shifts (CLS degradation) on completion. Screenreader compatibility needs proper ARIA attributes on hidden content.

## Related terms

- **[Core Web Vitals](Core-Web-Vitals.md)** — International page speed standard
- **[Intersection Observer API](Intersection-Observer.md)** — Essential implementation API
- **[CDN](Content-Delivery-Network.md)** — Technology further improving delivery speed
- **[Code Splitting](Code-Splitting.md)** — JavaScript deferred loading
- **[Service Worker](Service-Worker.md)** — Advanced offline support technique

## Frequently asked questions

**Q: Does lazy loading hurt SEO?**

A: No impact if properly implemented. Send first-view content immediately from server and add schema markup to additional content for proper search engine indexing.

**Q: Works on old browsers?**

A: Intersection Observer API unsupported on IE 11. Use polyfills or scroll event listener alternatives.

**Q: Apply to all elements?**

A: No. Load important first-view content immediately. Limit to secondary scroll-area content.
