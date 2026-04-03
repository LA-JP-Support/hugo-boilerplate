---
title: Nofollow Link
date: 2025-12-19
lastmod: 2026-04-02
translationKey: nofollow-link
description: A nofollow link is an HTML attribute that tells search engines not to count it as endorsement of the destination website.
keywords:
- nofollow link
- link attribute
- SEO optimization
- link equity
- search engine
category: Web Development & Design
type: glossary
draft: false
url: /en/glossary/Nofollow-Link/
---

## What is a Nofollow Link?

**A nofollow link is an HTML link containing the rel="nofollow" attribute, telling search engines "I don't endorse this link destination."** This prevents SEO value from being passed to the linked site, preventing spam and pagerank manipulation.

> **In a nutshell:** A way to link somewhere while saying "I'm not endorsing this."

**Key points:**

- **What it does:** Use HTML rel attributes to instruct search engines not to pass link value
- **Why it matters:** Prevent spam, avoid losing link value to irrelevant sites, comply with SEO guidelines
- **Who uses it:** Blog operators, forum administrators, CMS users, news sites

## Why it matters

Historically, the web operated on trust. High-quality sites linking to something signaled that the destination was valuable—essentially a vote. However, this was exploited for spam. Mass spam link posting in comments and paid links to unrelated sites proliferated. Nofollow was introduced by Google in 2005 as a defense mechanism.

Today, proper nofollow use is considered basic SEO etiquette. Additionally, the FTC (U.S. Federal Trade Commission) recommends nofollow for paid links, making it important from legal and ethical perspectives.

## How it works

In HTML, nofollow is written like this: `<a href="https://example.com" rel="nofollow">link text</a>`

When search engine crawlers find this tag, they don't follow the link or include it in ranking calculations. However, users can still click and access the link. Nofollow is only an instruction to search engines, not affecting user experience.

Today, beyond basic nofollow, more detailed attributes like rel="sponsored" (paid links) or rel="ugc" (user-generated content) are also available. These provide search engines with "why aren't you endorsing this?" information, helping more accurate ranking calculations.

## Real-world use cases

**Blog comments** — Automatically nofollow user comment links, preventing comment spam.

**Affiliate links** — Apply nofollow to paid referral links, showing "product recommendation" rather than company endorsement.

**User posting forums** — Apply blanket nofollow to links from untrusted users, preventing spam.

**External references** — Apply nofollow to external sites you reference but don't fully endorse.

## Benefits and considerations

**Benefits** — Effectively prevent spam and comply with search engine guidelines. Demonstrate intentional non-transfer of SEO value in paid link agreements.

**Considerations** — Excessive nofollow use can reduce overall site SEO value. Even nofollowing internal links stops intentional value flow to important pages, backfiring. Excessive nofollow makes site structure appear unnatural.

## Related terms

- **[SEO](SEO.md)** — Nofollow is part of on-page SEO.
- **[Link Building](Link-Building.md)** — Understanding nofollow is essential for high-quality link building.
- **[Domain Authority](Domain-Authority.md)** — Link value forms domain authority.
- **[Crawler](Crawler.md)** — Nofollow is an HTML signal controlling crawler behavior.
- **[PageRank](PageRank.md)** — Google's link value ranking algorithm.

## Frequently asked questions

**Q: Can you click nofollow links?**
A: Yes. Nofollow is only an instruction to search engines, and user clicks work normally.

**Q: Should internal links use nofollow?**
A: Usually not. Internal links indicate site structure, so nofollowing them increases value leakage and backfires.

**Q: Do paid links always require nofollow?**
A: FTC guidelines recommend nofollow or rel="sponsored" for paid links or advertising.
