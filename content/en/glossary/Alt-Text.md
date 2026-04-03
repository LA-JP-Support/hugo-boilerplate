---
title: Alt Text
date: 2025-12-19
lastmod: 2026-04-02
translationKey: alt-text
description: Text-based descriptions of images that display when images cannot be loaded, improving accessibility for visually impaired users and search engine optimization simultaneously.
keywords:
- alt text
- web accessibility
- image description
- SEO optimization
- screen reader
category: Web Development & Design
type: glossary
draft: false
url: /en/glossary/alt-text/
---

## What is Alt Text?

**Alt Text is a text description attached to images on web pages.** It communicates "what this image is" to people who cannot see images, when images fail to load, and to search engines.

Why is it necessary? Not everyone viewing the web can see images. Visually impaired users use screen readers—text-to-speech technology—but without Alt Text, screen readers only recognize an image as "image" without knowing its content. With Alt Text, screen readers read it aloud, giving visually impaired users the same information.

Search engines (Google, Bing) also reference Alt Text to understand image content. When someone searches for "coffee," if an image has Alt Text saying "morning coffee," that image appears more readily in search results.

> **In a nutshell:** Text descriptions that communicate image content to those who cannot see, and to search engines.

**Key points:**
- **What it does:** Describes image content in text
- **Why it matters:** Improves accessibility, SEO, and user experience
- **Who it serves:** Visually impaired users, slow internet users, search engines

## Why it matters

Web accessibility is a legal requirement. The US Americans with Disabilities Act (ADA), EU General Data Protection Regulation (GDPR), and Japan's public web accessibility standards all require "all users can access equally." Alt Text is the minimum measure meeting this requirement.

Moreover, SEO benefits are substantial. Search engines cannot directly "see" images, so they rely on Alt Text to judge image content. Strategically including keywords in Alt Text improves search rankings and increases organic traffic.

Additionally, when image loading is slow or fails, Alt Text displays instead, preventing users from losing meaningful information. This single practice simultaneously improves accessibility, SEO, and user experience.

## How it works

Alt Text is written within the HTML `<img>` tag:

```html
<img src="coffee.jpg" alt="Morning coffee at a modern cafe">
```

When a screen reader encounters this image, it reads aloud: "Morning coffee at a modern cafe." This allows visually impaired users to understand what the image shows.

Good Alt Text has **three elements**:

1. **Conciseness** — Aim for 50–125 characters. Screen readers better understand shorter descriptions.
2. **Context** — Don't repeat content already mentioned nearby. Avoid duplication.
3. **Accuracy** — State only objective facts without assumptions or emotion.

For example, with an image of "a child drinking coffee":
- Poor example: "Photo" (insufficient information)
- Poor example: "A lovely photo of a happy child enjoying coffee" (contains emotion)
- Good example: "Child holding a mug at a table" (concise, fact-based)

## Real-world use cases

**E-commerce (product images)**
A shoe online store. With Alt Text like "Navy leather business shoes, size 10," both visually impaired users and search engines understand the shoe's basic information.

**News sites (article illustrations)**
A political press conference photo with Alt Text "A politician at a podium in parliament chamber" helps visually impaired readers understand the situation and helps search engines grasp the article's topic more accurately.

**Social media posts**
On Instagram or Twitter, Alt Text like "Two people smiling before a birthday cake with a friend" lets visually impaired users enjoy the content. Many platforms now include Alt Text as standard.

## Benefits and considerations

**Benefits:** All users can equally access the web. SEO benefits increase search traffic. Improved user experience when image loading fails. Free to implement.

**Considerations:** Quality varies easily. With multiple writers, Alt Text detail differs by individual judgment. Additionally, "keyword stuffing" risks being flagged as spam, potentially reversing SEO benefits. Large sites face complex management.

## Related terms

- **[Web Accessibility](Web-Accessibility.md)** — Web design usable by everyone; Alt Text is part of this
- **[WCAG (Web Content Accessibility Guidelines)](WCAG.md)** — Global accessibility standards
- **[SEO (Search Engine Optimization)](SEO.md)** — Collective practices for improving search rankings
- **[Screen Reader](Screen-Reader.md)** — Software that reads screen content aloud
- **[User Experience (UX)](User-Experience.md)** — Usability of websites and apps

## Frequently asked questions

**Q: Does decorative imagery (design-only) need Alt Text?**
A: It needs Alt attribute but leave it empty. For decoration-only images, use `alt=""` so screen readers ignore it. Forced descriptions create noise.

**Q: Can I stuff Alt Text with SEO keywords?**
A: No. This "keyword stuffing" gets penalized by search engines. Alt Text is "description"; SEO is a "side effect." Priority matters.

**Q: For complex charts or diagrams, how long can Alt Text be?**
A: Complex diagrams may need paragraphs, not sentences. Recommended approach: concise Alt Text + detailed explanation in body text or separate page, using a layered strategy.

## References

1. World Wide Web Consortium (W3C). Web Content Accessibility Guidelines (WCAG) 2.1. 2024.
2. WebAIM. Alternative Text for Images. WebAIM, 2024.
3. Nielsen Norman Group. Alt Text for Images: Guidelines and Best Practices. NN/g Research.
4. Google Search Central. Image Best Practices for SEO. Google Developers.
5. Section 508 Guidelines. U.S. General Services Administration.
