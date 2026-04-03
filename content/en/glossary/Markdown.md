---
title: Markdown
date: 2025-12-19
lastmod: 2026-04-02
translationKey: Markdown
description: Markdown is a lightweight markup language that formats text using simple symbols and converts to HTML, ideal for technical documentation.
keywords:
- Markdown syntax
- markup language
- text notation
- document creation
- technical writing
category: Data & Analytics
type: glossary
draft: false
url: /en/glossary/markdown/
---

## What is Markdown?

**Markdown is a lightweight markup language that formats text using simple symbols like `#` and `*`, enabling headings, lists, links, and code notation.** With lower learning cost than HTML and source files remaining readable, it is widely adopted in [GitHub](GitHub.md) README files, blog platforms, knowledge bases, and technical documentation. A single Markdown file converts to multiple formats (HTML, PDF, Word), making the writing-to-publication workflow extremely efficient.

> **In a nutshell:** Like writing "*emphasis*" in email and having text automatically format beautifully—that is how Markdown text notation works.

**Key points:**

- **What it does:** Format text with simple symbols and convert to multiple formats
- **Why it matters:** Simpler than HTML with perfect compatibility to version control (Git)
- **Who uses it:** Engineers, documentation authors, bloggers, technical writers

## Why it matters

Markdown is easier to learn than writing HTML by hand with fewer typos. Instead of `<h1>Title</h1>`, you write `# Title`. More importantly, Markdown files are plain text, making them perfectly compatible with [Git](Git.md) version control systems. This enables easy multi-person editing, change history tracking, and conflict resolution. Technical documentation can be managed at the same level as code, keeping documentation always current.

## How it works

Markdown's basic elements work as follows. **Headings use `#` for hierarchy** (`#`=H1, `##`=H2, etc.). **Emphasis uses `*` or `_`** (`*bold*`→**bold**, `_italic_`→_italic_). **Lists use hyphens or numbers** (`-` or `1.`) for hierarchy. **Links use brackets and parentheses** (`[display text](URL)`). **Code uses backticks** (`` `code` ``).

The execution flow is: ① create Markdown file (`README.md`) ② preview to verify headings, emphasis, lists format correctly ③ commit to version control ④ convert to HTML or PDF as needed ⑤ publish. Using conversion tools ([Pandoc](Pandoc.md), etc.) auto-generates multiple formats from single Markdown.

## Real-world use cases

**GitHub project README**
Document project description, installation, usage examples in Markdown. First document visitors read, defining first impressions.

**Technical documentation centralization**
Write API specs, setup guides, troubleshooting in Markdown, manage with Git. All engineers access latest information.

**Blog and knowledge base writing**
Blog platforms (Medium, Qiita) natively support Markdown. Write focused on content without HTML concerns.

## Benefits and considerations

**On the benefits side,** Markdown is simple to learn, more readable than HTML, and perfectly compatible with version control. Plain text works in any editor, remaining platform-independent. Multiple format conversion automates document management efficiency.

**As for considerations,** multiple Markdown "flavors" (GitHub Flavored Markdown, CommonMark) render differently across platforms. Complex layouts (intricate tables, image placement) exceed Markdown capabilities, requiring HTML. 

## Related terms

- **[Version Control](Version-Control.md)** — Track Markdown file changes
- **[Git](Git.md)** — Standard tool for managing Markdown files
- **[GitHub](GitHub.md)** — Standard-adopting Markdown platform
- **[HTML](HTML.md)** — Target conversion format for Markdown
- **[Technical Writing](Technical-Writing.md)** — Primary Markdown application field

## Frequently asked questions

**Q: Which Markdown flavor should I use on GitHub?**
A: GitHub Flavored Markdown (GFM) is standard, enabling extended features like tables and checklists.

**Q: Can Markdown achieve complex layouts?**
A: Possible but requires mixing HTML. For complex layouts, HTML or Word better suit your needs.

**Q: Can I convert Markdown to Word documents?**
A: Yes, using tools like Pandoc. However, complex layouts may be lost during conversion.
