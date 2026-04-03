---
title: Page Bundle
date: 2025-12-19
lastmod: 2026-04-02
translationKey: page-bundle
description: A method of managing content with static site generators (like Hugo) where a webpage and all its related files (images, documents) are organized together in one folder.
keywords:
- Page Bundle
- Hugo
- Static Site Generator
- Content Management
- Resource Organization
category: Knowledge & Collaboration
type: glossary
draft: false
url: "/en/glossary/Page-Bundle/"
---

## What is Page Bundle?

**A Page Bundle is a method for organizing a single webpage and all its related assets (images, documents, etc.) together in one folder when building websites with static site generators like Hugo.** Traditionally, pages and assets were scattered across different directories, and moving files broke links. Bundle organization solves this problem, creating more portable content structures.

> **In a nutshell:** Organizing a blog post and its images together in "one folder."

**Key points:**

- **What it does:** Keeps a page and its assets together in one folder
- **Why it's needed:** Prevents broken links, simplifies management, improves portability
- **Types:** Leaf bundles (pages) and branch bundles (sections)

## Why it matters

Large websites struggle with content and asset management complexity. When blog articles and their ten images live in separate folders, updating page structure means fixing link references constantly.

Page Bundles eliminate this complexity by physically co-locating related files. Version control with Git becomes more efficient — tracking who changed which image for which page is easier.

## How it works

Page Bundles are expressed through folder structure. Each page gets a dedicated folder containing `index.md` (main content) and all related files.

```
content/
├── posts/
│   ├── article-1/
│   │   ├── index.md
│   │   ├── featured.jpg
│   │   └── diagram.png
│   └── article-2/
│       ├── index.md
│       └── data.csv
```

Generators like Hugo recognize this directory structure and process all files as a single unit. Image references use simple relative paths (`./featured.jpg`), eliminating manual work when moving pages.

**Leaf bundles** represent individual pages (blog articles) with no child pages. **Branch bundles** represent sections/categories containing multiple child pages.

## Real-world use cases

**Running a tech blog**
Tech writers writing tutorial articles with five screenshots, code examples, and downloadable samples use bundle organization to keep everything in one folder, letting readers easily find related files.

**Large SaaS product documentation site**
Managing 1,000+ pages of documentation, page bundles keep each feature-explanation page bundled with its images, videos, and PDF files. Adding features simplifies management.

**Publisher archive management**
Magazine digital editions where each article has its related images, supplementary materials, and interactive elements in one bundle simplify back-issue and archive searching.

## Benefits and considerations

**Benefits:** Automated link management drastically reduces errors. Version management becomes efficient and team collaboration easier. Site-wide rebuilds simplify.

**Considerations:** Growing bundle directories complicate tree structure. File searching and navigation require careful planning. When wanting to share images/resources across bundles, bundle independence becomes a constraint.

## Related terms

- **Hugo** — The representative static site generator with page bundle capabilities
- **Static Site Generator** — General term for tools adopting page bundle concepts
- **Asset Management** — Optimizing image and video handling within page bundles
- **Frontmatter** — Metadata definition format within page bundles
- **Content Organization** — Efficient information architecture through bundle structure

## Frequently asked questions

**Q: Using page bundle organization, can multiple pages share the same image?**
A: Yes, but the bundle approach's benefits diminish. Place frequently-shared resources in a global assets folder and reference from outside bundles — this is recommended.

**Q: Can I migrate existing site structures to bundle format?**
A: Yes. Gradual migration is recommended. Create new pages using bundle format and migrate existing pages as needed.

**Q: Are there bundle size limits?**
A: No. Bundles can contain tens of megabytes (including video). However, build time may be affected, requiring optimization in some cases.
