---
title: Hreflang
date: 2025-12-19
lastmod: 2026-04-02
translationKey: Hreflang
description: An HTML tag that tells search engines which language and region a page is intended for on multilingual websites, ensuring the correct language version reaches appropriate users.
keywords:
- hreflang
- international SEO
- multilingual websites
- language targeting
- regional SEO
category: Web Development & Design
type: glossary
draft: false
url: /en/glossary/hreflang/
---

## What is Hreflang?

**Hreflang is a tag that tells search engines "which language version is this page" on multilingual websites.** When both English and Japanese versions exist, correctly distinguishing them ensures that Japanese users see the Japanese version while American users see the English version. Introduced by Google in 2011, this mechanism has become an essential [SEO](SEO.md) strategy for websites operating globally.

> **In a nutshell:** A label that explains to search engines "this page is in Japanese" or "this one is in English (US)."

**Key points:**

- **What it does:** Explicitly specifies a page's language and region to search engines
- **Why it's needed:** Makes it easier for users of each language to find their language version
- **Who uses it:** Companies and media outlets operating sites in multiple languages

## Why it matters

In global business operations, language differences can damage user experience. Showing a user who doesn't understand Japanese a Japanese page is unfriendly. Search engines may also struggle to determine whether "this content is duplicated or meant for different markets." Hreflang resolves this confusion.

It also improves search results quality. When users easily find their language version, click-through rates to your website increase, potentially improving [rankings](Rankings.md) as a result. Additional international marketing benefits are also possible—for example, Japanese users can better understand product details in Japanese, making them more likely to purchase.

## How it works

Hreflang is a mechanism that defines relationships between pages. It consists of four key elements.

First is the language code. "ja" means Japanese, "en" means English, and "en-US" means US English, following ISO standards. Next, each language version creates mutual bidirectional references. For example, "the Japanese version links to the English and Chinese versions" while "the English version also links to the Japanese version."

Additionally, a special value "x-default" lets you specify a default page for users who don't match a specific language. Combined with [canonical URLs](Canonicalization.md), you can also specify page priorities more precisely.

## Real-world use cases

**Global e-commerce localization**
Online retailers sell the same products across multiple regions. With hreflang, French users automatically see the French version and Spanish users see the Spanish version, reducing cart abandonment rates.

**Multinational corporate websites**
When headquarters websites provide information about regional offices, hreflang lets you specify "show Japanese users information about the Japan office."

**Regional news distribution**
International news organizations often cover the same topic from different regional perspectives. Properly linking versions with hreflang makes it easier for users in each region to find news from their perspective.

## Benefits and considerations

Hreflang's biggest benefit is **improved user experience.** The correct language version displays automatically, reducing frustration from language barriers. You can also expect SEO benefits like improved rankings and increased traffic. You'll also avoid negative impacts from duplicate content detection.

However, complexity is a challenge. As language and region combinations increase, configuration becomes more complex. You must ensure mutual references between all versions, which requires maintenance time. Configuration errors can also worsen search results.

## Related terms

- **[Language Targeting](Language-Targeting.md)** — A technique for optimizing content for users of specific languages; hreflang is one implementation method
- **[International SEO](International-SEO.md)** — The general term for multilingual website optimization; hreflang is a key element
- **[Canonical URL](Canonicalization.md)** — A mechanism that specifies a page's preferred version, often used with hreflang
- **[XML Sitemap](XML-Sitemap.md)** — Hreflang can also be used within sitemaps
- **[Meta Tags](Meta-Tags.md)** — HTML tags like hreflang that communicate page information to search engines

## Frequently asked questions

**Q: Is hreflang necessary if the Japanese and English versions have identical content?**
A: Yes, it is. Even if content is simply translated, search engines see it as different pages. Properly specifying hreflang for each language version ensures the optimal version reaches each language's users.

**Q: What is the biggest mistake in hreflang implementation?**
A: Incomplete bidirectional linking is the most common error. If "the Japanese version links to English" but "the English version doesn't link to Japanese," the configuration may not work. Verify mutual references between all versions.

**Q: How long does it take for hreflang to take effect?**
A: Google usually reflects the configuration within several weeks to months. Change takes time, so patient monitoring is important. Regularly checking implementation status in Search Console is recommended.
