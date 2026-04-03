---
title: Hugo Taxonomy
date: 2025-12-19
lastmod: 2026-04-02
translationKey: hugo-taxonomy
description: Hugo's system for classifying content using tags and categories, automatically generating related content pages.
keywords:
- Hugo taxonomy
- static site generator
- content organization
- tags and categories
- website classification
category: Web Development & Design
type: glossary
draft: false
url: /en/glossary/hugo-taxonomy/
---

## What is Hugo Taxonomy?

**Hugo Taxonomy is a system that classifies content using tags and categories, and displays related content together.** When you add "Python" and "machine learning" tags to a blog article, Hugo automatically generates a tag page listing other articles with the same tags. Traditional blog systems require manually creating category pages, but Hugo automates this.

> **In a nutshell:** Like a library's card catalog system where indices by author and theme are automatically created.

**Key points:**

- **What it does:** Classifies content with tags, auto-generating related pages
- **Why it's needed:** Users find content matching their interests more easily
- **Who uses it:** Blog and documentation site operators

## Why it matters

Without [taxonomy](Taxonomy.md), users struggle finding articles they're interested in. Hugo Taxonomy means simply writing `tags: [Python, machine learning]` in Front Matter generates related article pages automatically. This helps [SEO](SEO.md), as aggregate pages for topics like "Python machine learning" help search engines understand site structure. [User experience](User-Experience.md) improves—visitors can navigate to related articles and deepen their learning.

## How it works

Hugo Taxonomy has a two-level structure. **Taxonomy** refers to "tags" or "categories"—high-level classifications defined in configuration. **Term** refers to specific labels like "Python" or "web development." Processing has four stages. First, **content reading** analyzes all articles and extracts tags. Next, **auto-page generation** creates list pages for each tag. Then, **template application** applies design. Finally, **internal link building** cross-references article and tag pages.

For example, if ten articles have the "Python" tag, a "Python" tag page automatically generates, listing those ten articles.

## Real-world use cases

**Technical blog post classification**
Set multiple taxonomies like "language," "framework," and "difficulty level." Readers easily find articles matching criteria like "Python for beginners."

**E-commerce product classification**
Assign taxonomies like "category," "brand," and "price range." Customers can search "Nike shoes under 5000 yen," improving purchasing experience.

**Documentation site navigation**
Tag API documentation with "authentication," "data retrieval," and "error handling." Users progressively learn related APIs.

## Benefits and considerations

Hugo Taxonomy's biggest benefit is **automation.** Pages don't need manual creation—tags automatically generate related pages. It scales well; more articles aren't a problem. Multiple combined taxonomies enable flexible classification. However, too many taxonomies complicate navigation, risking user confusion. Inconsistent tag naming causes problems—"Python" and "python" become separate pages.

## Related terms

- **[Hugo](Hugo.md)** — The static site generator with this taxonomy feature
- **[Taxonomy](Taxonomy.md)** — The general term for classification systems
- **[Front Matter](Front-Matter.md)** — Content taxonomies are specified here
- **[SEO](SEO.md)** — Taxonomy pages benefit SEO
- **[Navigation Design](Navigation-Design.md)** — Effective taxonomies improve navigation

## Frequently asked questions

**Q: How should I differentiate between tags and categories?**
A: Categories follow the one-per-article rule, used for broad classifications ("blog," "documentation"). Tags allow multiple assignments, used for specific themes ("Python," "asynchronous processing"). This distinction is typical.

**Q: How many taxonomies can I create?**
A: No technical limit, but 3-5 is recommended for usability. Too many confuses visitors.

**Q: Can I change or merge existing tags later?**
A: Yes, but Front Matter requires manual editing. For large changes, automation scripts help.
