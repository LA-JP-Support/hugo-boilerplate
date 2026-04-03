---
title: Robots.txt
date: 2025-12-19
lastmod: 2026-04-02
translationKey: Robots-txt
description: Text file instructing search engine crawlers which site areas they can access, used for SEO optimization and server load management.
keywords:
- robots.txt
- Web Crawling
- SEO Optimization
- Crawler Control
- Website Management
category: Content & Marketing
type: glossary
draft: false
url: /en/glossary/Robots-txt/
---

## What is Robots.txt?

**Robots.txt is a text file instructing search engine crawlers which website sections they may access.** Located in the site root, crawler bots like Googlebot and Bingbot read this file first when visiting, confirming crawlable areas.

> **In a nutshell:** Website owner instructions to search engine bots: "see here," "don't see here."

**Key points:**

- **What it does:** Controls crawler access and crawl efficiency
- **Why it's needed:** Reduces server load; prevents inappropriate pages in search results
- **Who uses it:** Website administrators, SEO experts, web developers

## Why it matters

Search crawlers traverse countless pages daily. Without Robots.txt, internal test pages and admin interfaces get crawler discovery, appearing in results or wasting server resources. Efficient crawler-budget use (how deeply the crawler explores) ensures important content gets indexed reliably, improving SEO. Robots.txt optimizes SERP display and functions as fundamental SEO tool.

## How it works

Robots.txt uses simple "if-then" rules. Each line specifies "User-agent" (target crawler) and "Disallow" (forbidden paths). Example: "User-agent: *" targets all crawlers; "Disallow: /admin/" forbids admin pages.

Workflow: (1) Crawler visits site → (2) Requests "/robots.txt" → (3) Reads file, confirms rules → (4) Crawls following rules. Technically, robots.txt is just a "request"—malicious bots may ignore it. Truly sensitive pages need password protection.

## Real-world use cases

**Ecommerce site optimization**

Online stores exclude filtered search results (duplicate product list pages) via "Disallow: /?filter=", avoiding duplicate content while ensuring main product pages index.

**Blog admin interface protection**

Blogging platforms block post-login admin screens and drafts using robots.txt, preventing unpublished content appearance.

**Large site crawl efficiency**

News sites with millions of pages restrict crawler access to old archives via robots.txt, concentrating crawl power on latest articles.

## Benefits and considerations

Robots.txt's greatest benefit is reduced server load while improving SEO. However, important limits exist: robots.txt is publicly readable, exposing secret page locations. Real security needs password protection. Second, robots.txt is informal standard; crawler compliance is voluntary. Malicious bots ignore it. Third, syntax errors can mistakenly block important pages.

## Related terms

- **[SEO](SEO.md)** — Search optimization; robots.txt is critical component
- **[SERP](SERP.md)** — Search engine results pages; optimizable via robots.txt
- **[Meta Robots Tag](Meta-Robots-Tag.md)** — HTML tag controlling per-page crawler behavior
- **[XML Sitemap](XML-Sitemap.md)** — Helper tool signaling important pages to crawlers
- **[Crawl Budget](Crawl-Budget.md)** — Total crawler resources spent on site

## Frequently asked questions

**Q: Do robots.txt-blocked pages disappear from search results?**

A: Not necessarily. Pages discovered via external links may still appear despite robots.txt blocking. For guaranteed exclusion, use password protection or "noindex" meta tag.

**Q: Can the same robots.txt work across multiple domains?**

A: No. Each domain needs independent robots.txt. Subdomains can have different rules.

**Q: Do robots.txt changes take immediate effect?**

A: No. Takes effect when crawlers re-read robots.txt. Google Search Console can expedite updates.
