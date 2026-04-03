---
title: "Content Front Matter"
date: 2025-12-19
lastmod: 2026-04-02
description: "Structured metadata section at the beginning of content files. Written in YAML format containing publication date, author, category, and other essential information"
translationKey: "Content-Front-Matter"
category: "Content & Marketing"
type: glossary
draft: false
url: /en/glossary/Content-Front-Matter/
keywords:
  - front matter
  - metadata
  - YAML
  - static site generators
  - content structure
---

## What is Content Front Matter?

**Content Front Matter is a structured metadata section placed at the beginning of content files, typically in YAML format, containing publication date, author, category, tags, and other critical information.** Static site generators (Hugo, Jekyll) and modern CMS platforms read this metadata to automatically organize and display content.

> **In a nutshell:** Like a book's table of contents or copyright page—structured information summarizing "what is this content" appears before the main text.

**Key points:**

- **What it does:** Embed content attribute information (dates, author, classification) in machine-readable format
- **Why it matters:** Enables website engines to automatically classify, organize, and display content
- **Who uses it:** Technical blogs, documentation sites, static site generator-based organizations

## How it works

Front matter consists of YAML-formatted data enclosed between separators (typically `---`).

**YAML advantages** include human readability alongside reliable machine parsing. Writing `title: Blog Article` enables the template engine to automatically display that title as page headers and search results.

**Key front matter items** include title, publication date, update date, description (displayed in search results), author, category, and tags. Custom fields can be added as needed.

**Processing flow** proceeds as: generator reads file → parses front matter → passes to template → generates HTML. Without front matter data, the site cannot determine how to treat each page.

## Real-world use cases

**Blog management** — Specifying post title, publication date, author, and category in front matter enables platforms to automatically generate "April 2026 posts" and "Marketing category" pages.

**Technical documentation** — API docs record version, related pages, and difficulty level in front matter, enabling consistent site-wide structure.

**Multilingual sites** — Front matter links language versions of identical content, using language codes and URLs to connect corresponding pages.

## Benefits and considerations

**Benefits** include managing content and structured information in a single file, easily tracking changes with version control, and simplifying automation.

**Considerations** include YAML complexity (indentation, special character escaping) creating barriers for non-technical contributors. Schema changes sometimes require updating entire file collections.

## Related terms

- **[Static Site Generators](Content-Hub.md)** — Technology processing front matter
- **[Metadata](Content-Inventory.md)** — Information front matter represents
- **[Content Management](Content-Governance.md)** — Metadata management implementation
- **[Templates](Content-Marketing.md)** — Systems using front matter information for rendering
- **[SEO Optimization](Content-Freshness.md)** — Meta descriptions in front matter appear in search results

## Frequently asked questions

**Q: Can formats other than YAML be used?**
A: YAML is most commonly supported, but JSON and TOML formats are also options. Follow your project's standards.

**Q: Who writes front matter?**
A: Content creators typically write it. Templates or presets reduce entry barriers for contributors.

**Q: What happens with incorrect front matter?**
A: Most generators either report errors or use default values. Build-time validation catches problems early.
