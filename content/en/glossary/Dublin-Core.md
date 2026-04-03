---
title: Dublin Core
date: 2025-12-19
lastmod: 2026-04-02
translationKey: Dublin-Core
description: Dublin Core is an international standard metadata schema for describing digital resources, enabling interoperability between libraries and databases.
keywords:
- Dublin Core
- metadata standards
- digital libraries
- resource description
- interoperability
category: Data & Analytics
type: glossary
draft: false
url: /en/glossary/dublin-core/
---

## What is Dublin Core?

**Dublin Core is an international standard defining 15 basic elements for uniformly describing digital resources (webpages, e-books, datasets).** Named after a metadata workshop held in Dublin, Ireland in 1995, it standardizes information like "Title," "Creator," "Subject," "Description," "Publisher," etc. This standard enables information sharing across different libraries and databases. In the digital age where [metadata](Dublin-Core.md) management is critical, Dublin Core is essential.

> **In a nutshell:** "A standard way all libraries record 'Title,' 'Creator,' 'Description' and other information about digital books and documents in the same format."

**Key points:**

- **What it does:** Describes digital resource information in standard format
- **Why it's needed:** Enables information exchange across different systems
- **Who uses it:** Librarians, data managers, digital archive operators

## Why it matters

Dublin Core is important for three reasons. First, it enables "interoperability"—the same format allows searching across different libraries and databases. Second, it's simple and easy to implement—only 15 elements are needed for basic description, unlike complex metadata standards. Third, as an internationally recognized standard (ISO 15836), it offers long-term reliability. With the development of [semantic web](Docker.md), Dublin Core has been integrated into RDF (Resource Description Framework).

## How it works

Dublin Core's mechanism is straightforward. When describing a digital resource (e.g., a PDF), you add metadata like "Title," "Creator," "Creation Date." These are stored in XML or RDF format. Next, this metadata is exchanged across systems. Using OAI-PMH (Open Archives Initiative Protocol for Metadata Harvesting), multiple libraries automatically collect metadata.

For example, if University A's digital repository and University B's digital repository both describe data in Dublin Core format, federated search finds content from both.

## Real-world use cases

**Digital archives** Historical documents and old photos are digitized, described in Dublin Core, and published online.

**University thesis repositories** Graduate theses are registered in Dublin Core format and shared with other universities.

**Museum collections databases** Artwork information (title, creator, creation year, materials) is managed in Dublin Core.

## Benefits and considerations

**Benefits:** Simple and easy to learn. No cost (open standard), widely supported by tools. Easy data exchange between organizations.

**Considerations:** 15 basic elements may not adequately describe complex resources. Quality control is important but challenging for large collections. Different organizations may interpret elements differently.

## Related terms

- **[Metadata](Dublin-Core.md)** — data about data
- **[RDF](Dublin-Core.md)** — Resource Description Framework
- **[Interoperability](Dublin-Core.md)** — connecting different systems
- **[Digital libraries](Document-Loader.md)** — primary field using Dublin Core
- **[Semantic web](Docker.md)** — web where machines understand meaning

## Frequently asked questions

**Q: Must all 15 elements be used?**
A: No. Use only necessary elements based on resource type. Minimum is just "Title."

**Q: Can qualified Dublin Core extensions be used?**
A: Yes. For detailed description needs, qualified elements can be used.

**Q: How to ensure interoperability with other libraries?**
A: Use harvesting protocols like OAI-PMH to regularly exchange metadata.
