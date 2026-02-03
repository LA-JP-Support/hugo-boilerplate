---
title: "AI Learning Methods and Knowledge Sources"
date: 2026-02-03
lastmod: 2026-02-03
draft: false
translationKey: "ai-learning"
description: "SmartWeb's AI (chatbot and email response creation) learns information from FlowHunt's knowledge sources. It supports various formats including web crawling, Q&A, document uploads, and more."
keywords: ["AI learning", "knowledge sources", "FlowHunt", "web crawling", "FAQ", "RAG"]
category: "ai-fundamentals"
---

SmartWeb's AI chatbot and AI email response creation (AI Answer Composer) retrieve information from **FlowHunt's knowledge sources** and generate accurate responses using RAG (Retrieval-Augmented Generation) technology.

## Types of Knowledge Sources

FlowHunt allows you to manage three main types of knowledge sources:

| Knowledge Source | Description | Use Cases |
|------------------|-------------|-----------|
| **Schedules** | Regular web crawling of websites | Product information, FAQ, blogs |
| **Q&A** | Manually registered questions and answers | Frequently asked questions, important responses |
| **Documents** | File uploads | Manuals, PDFs, Excel files, etc. |

## Supported Content Formats

### File Upload Supported Formats

| Format | Description |
|--------|-------------|
| PDF | PDF documents |
| DOCX / DOC | Word documents |
| XLS / XLSX | Excel spreadsheets |
| TXT | Text files |
| RTF | Rich text format |
| CSV | Comma-separated values |
| Markdown | Markdown format |
| HTML | Web page format |
| YouTube videos | Video transcription |

### Types of Web Crawling

| Type | Description |
|------|-------------|
| Domain crawling | Automatically crawls entire specified domain |
| Single URL crawling | Retrieves only one specific page |
| Sitemap crawling | Crawls based on sitemap.xml |
| YouTube channel | Retrieves videos from channels |
| URL list crawling | Retrieves specified URL lists |
| XML product feed | Retrieves product data from e-commerce sites |

## Web Crawling Configuration

### Update Frequency Selection

| Update Frequency | Recommended Use Cases |
|------------------|----------------------|
| Daily | News sites, frequently updated FAQs |
| Weekly | Product information, blogs |
| Monthly | Manuals, company information |
| Yearly | Information with low change frequency |

*Half the credits are consumed even when there are no changes

### Advanced Configuration Options

| Option | Description |
|--------|-------------|
| Browser usage | For pages requiring JavaScript rendering (additional credits) |
| Link following | Retrieves linked pages as well |
| Screenshot capture | Saves page images (additional credits) |
| Proxy rotation | Crawls with changing IPs (additional credits) |
| Exclude URLs | Skips URLs with specified patterns |
| Target URL restriction | Retrieves only URLs with specified patterns |
| Custom headers | Adds HTTP headers for authentication, etc. |

## Q&A Management System

### Q&A Operation Features

- **Immediate reflection**: Manually added Q&As are immediately available
- **Priority settings**: Frequently asked questions are prioritized
- **Version management**: Manages change history of answers
- **Approval workflow**: Important information is reflected after approval

## Content Creation Guidelines for Better Responses

The accuracy of AI responses heavily depends on the quality of the content it learns from. Following these guidelines to organize your content will improve response accuracy.

### Basic Writing Rules

- **Keep sentences short** (15-20 words recommended)
- **Avoid technical jargon**
  - Example: "facilitate implementation of plans" → "help advance plans"
- **Avoid ambiguous expressions** (reduce use of "etc." and "may be the case")
- **Use active voice** (avoid passive voice)

### Content Structure Tips

- Separate content with headings
- Utilize bullet points
- Cover all frequently asked questions
- Include appropriate white space

### Pre-Implementation Preparation Checklist

- [ ] Verify FAQ and manual content is up-to-date
- [ ] Replace technical terms with plain language
- [ ] Optimize structure with headings, bullet points, and short paragraphs
- [ ] Check coverage of common question patterns
- [ ] Fix ambiguous expressions and insufficient explanations

**Tip**: We recommend reviewing existing FAQs and manuals once before implementation. Check for outdated information or ambiguous expressions.

## Benefits of Knowledge Base Sharing

The AI chatbot and AI email response creation **share the same knowledge base**:

- **One-time setup for both**: Register FAQs and manuals once, and they'll be utilized in both chat and email
- **Response consistency**: Provides the same quality responses across all channels
- **Maintenance efficiency**: Knowledge updates are immediately reflected in both systems

## Related Information

- [About RAG Technology](/ja/support/ai-fundamentals/rag-technology/) - Explanation of technology that enables high-precision responses
- [AI Provider Setup](/ja/support/ai-fundamentals/ai-provider-setup/) - FlowHunt configuration methods
