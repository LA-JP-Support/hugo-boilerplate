---
title: Jamstack
date: 2025-12-19
lastmod: 2026-04-02
translationKey: Jamstack
description: JavaScript and API are leveraged to pre-generate HTML and serve it, a modern and high-speed web construction method.
keywords:
- jamstack
- static site generation
- web development
- performance
- CDN
category: Web Development & Design
type: glossary
draft: false
url: /en/glossary/jamstack/
---

## What is Jamstack?

**Jamstack is a modern web construction method combining JavaScript + API + Markup (HTML).** Unlike traditional server-type websites, pages are pre-generated as HTML and stored, then delivered at high speed from a [CDN](CDN.md). Instead of "creating the page" every time a visitor accesses it, you "deliver the pre-created HTML," resulting in remarkably fast loading speeds and low security risks.

> **In a nutshell:** Instead of creating pages "on demand," you "create them ahead of time and deliver" them. That's why it's super fast and secure.

**Key points:**

- **What it does:** Pre-generates HTML and delivers static files using a CDN
- **Why it's beneficial:** Pages load super fast and security risks are low
- **Target audience:** Web developers, performance-focused companies, startups

## Why it matters

Modern users abandon "slow sites" in 0.1 seconds. Page speed significantly impacts purchase and application rates ([conversion](Conversion.md) rates). Jamstack solves this problem fundamentally.

Traditional [WordPress](WordPress.md) and similar platforms have servers "assemble the page" every time a user accesses. Database access and complex calculations are necessary, so it takes time. Jamstack delivers already-completed HTML from fast [CDN](CDN.md), so users receive pages instantly. Simultaneously, server complexity decreases and security threats are greatly reduced.

## How it works

The Jamstack development/operation process divides into three stages.

**Stage 1: Build (Pre-generate pages)**
Content for blog articles and pages is prepared, and a [static site generator](Static-Site-Generator.md) (Gatsby, Next.js, etc.) automatically converts it to HTML. This "build" process runs when developers make changes.

**Stage 2: Deploy (Preparation for delivery)**
Generated HTML files are uploaded to [CDN](CDN.md). [CDN](CDN.md) copies files to servers (edge servers) worldwide.

**Stage 3: Delivery and Interaction**
When users access the site, HTML is delivered super fast from the nearest edge server. After page display, JavaScript calls APIs in response to user actions, providing dynamic features (search, form submission, etc.).

With this method, once files are built, they're "complete products," so no additional server processing is needed as visitor numbers increase.

## Implementation best practices

**Leverage headless CMS**
Using API-type CMS like [Contentful](Contentful.md) or [Notion](Notion.md), when content editors create articles in a browser, the build automatically starts and the site updates.

**Caching strategy**
Set [CDN](CDN.md) cache duration appropriately. "Daily-updated pages: 1-day cache," "Rarely-changed pages: 1-month cache"—adjust based on update frequency to balance speed and freshness.

**Incremental build**
Full site rebuilds take time, so use "incremental build" features to rebuild only changed parts.

**Error handling**
Since relying on external APIs, prepare fallback alternatives when APIs fail.

## Related terms

- **[Static Site Generation (SSG)](Static-Site-Generation.md)** — Jamstack's core. The process of pre-generating HTML
- **[Headless CMS](Headless-CMS.md)** — Content management method widely used with Jamstack. Supplies content via API
- **[CDN](CDN.md)** — Global distribution network. The foundation supporting Jamstack's speed
- **[Serverless Functions](Serverless.md)** — Execute processing without managing servers. Provides dynamic features for Jamstack
- **[NextJS](NextJS.md)** — Standard Jamstack development framework. React-based

## Frequently asked questions

**Q: Jamstack for blogs, WordPress for complex apps?**
A: Correct. Jamstack is optimal for blogs, portfolios, marketing sites—static content. If complex dynamic features (member systems, comments) are needed, traditional options should be considered.

**Q: Is real-time updating possible?**
A: Yes. After page display, JavaScript calls APIs to fetch and display real-time data. Supports chat, rankings, inventory information, etc.

**Q: Can I migrate from existing WordPress?**
A: Easy for simple blogs. Complex features (member systems, comments) require adjustments.
