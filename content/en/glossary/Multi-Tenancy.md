---
title: Multi-Tenancy
date: 2025-12-19
lastmod: 2026-04-02
translationKey: multi-tenancy
description: Multi-tenancy is an architecture where one application serves multiple customers while keeping their data completely isolated. It's how modern SaaS platforms efficiently serve millions of users.
keywords:
- Multi-tenancy
- SaaS
- Cloud computing
- Data isolation
- Software architecture
category: Business & Strategy
type: glossary
draft: false
url: /en/glossary/Multi-Tenancy/
---

## What is Multi-Tenancy?

**Multi-tenancy is an architecture where multiple customers (tenants) share one application and database while remaining completely isolated from each other.** It's the standard approach for cloud services and SaaS. For example, Salesforce serves millions of companies on the same platform—each company's data is logically separated by tenant ID and never visible to competitors.

> **In a nutshell:** Like an apartment building. Multiple households share building infrastructure and utilities while maintaining private independent spaces.

**Key points:**

- **What it does:** Serve multiple customers from shared infrastructure with isolated data
- **Why it's needed:** Dramatically reduce costs and operational efficiency
- **Who uses it:** SaaS companies, cloud service providers, large platforms

## Why it matters

Multi-tenancy is the efficiency foundation. If Salesforce maintained separate applications for each company, they couldn't serve 10+ million customers. It distributes infrastructure costs across customers, enabling flexible pricing from startups to enterprises. All customers use the same version, simplifying updates and maintaining unified security.

## How it works

Data isolation uses three approaches. **Tenant ID method** is simplest—add customer IDs to all rows, automatically filter on queries. **Schema separation** creates customer-specific schemas in one database for stronger isolation. **Database separation** dedicates databases per customer for maximum safety but increased operational costs.

At the application layer, users log in, system identifies their tenant, and automatically applies tenant ID filters to all queries. Developers write once; the same code serves all tenants.

## Real-world use cases

**Salesforce CRM** — Each company configures custom fields independently while running on the same platform. Updates reach all companies simultaneously.

**Cloud storage (Google Drive)** — Billions of users share infrastructure; only their own files are accessible. Efficiency and convenience combine.

**Project management tools (Asana, Notion)** — Multiple companies manage projects with complete data separation per organization.

## Benefits and considerations

**Benefits: Cost and efficiency** — Shared infrastructure means low per-customer costs with economy of scale. Single updates serve all customers.

**Considerations: Security risk** — Isolation failure risks exposing customer data. "Noisy neighbor" issues where heavy-resource tenants degrade others' performance.

## Related terms

- **[SaaS](SaaS.md)** — Delivery model enabled by multi-tenancy
- **[Cloud Computing](Cloud-Computing.md)** — Execution foundation
- **[Data Security](Data-Security.md)** — Multi-tenancy's greatest challenge
- **[Scalability](Scalability.md)** — Problem multi-tenancy solves

## Frequently asked questions

**Q: Is data truly isolated in multi-tenancy?**
A: Yes, if properly implemented. Bugs (like SQL injection) can breach isolation, so security audits are critical.

**Q: Can the "noisy neighbor" problem be prevented?**
A: Yes, through resource quotas and active monitoring. However, complete prevention is difficult; demanding tenants sometimes need physical isolation.
