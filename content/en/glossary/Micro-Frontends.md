---
title: Micro-Frontends
date: 2025-12-19
lastmod: 2026-04-02
translationKey: micro-frontends
description: An architectural approach that breaks down web applications into smaller, independently developed and deployed frontend applications, enabling scalable and autonomous team operations.
keywords:
- Micro-Frontends
- Frontend Development
- Web Applications
- Independent Deployment
- Team Autonomy
category: Web Development & Design
type: glossary
draft: false
url: /en/glossary/Micro-Frontends/
---

## What are Micro-Frontends?

**Micro-frontends are an architectural style that decomposes web applications into independently developed and deployable small frontend applications.** Each frontend can be owned by a different team and implemented using different frameworks or technologies, while still delivering a unified, seamless user experience.

> **In a nutshell:** Micro-frontends are like splitting a large website into multiple independent smaller websites and combining them. While each team moves at its own pace, the overall experience remains unified.

**Key points:**

- **What it does:** Modularizes frontends and enables independent development and deployment.
- **Why it matters:** Accelerates parallel development across large teams and increases technological flexibility.
- **Who uses it:** Enterprises developing large-scale web applications across multiple teams.

## Why it matters

Traditional monolithic frontend architectures pack all functionality into a single codebase, causing conflicts when multiple teams work simultaneously. Micro-frontends allow teams to work independently, eliminating deployment synchronization.

Teams can also select optimal technologies per unit, enabling gradual migration to new frameworks. Failure impact is limited, improving overall system reliability.

## How it works

Micro-frontend implementation has multiple patterns. **Server-side integration** has servers combine HTML fragments from multiple frontends to create the final page. **Build-time integration** publishes each frontend as an npm package, which container applications import during builds. **Runtime integration** dynamically loads each frontend in the browser using iFrame, JavaScript entry points, or Web Components.

Web Components are recommended as a standard browser technology with high portability. Module Federation enables dynamic code sharing between applications, optimizing bundle sizes.

## Real-world use cases

**E-commerce platforms**
Product search, shopping cart, and checkout were split into independent micro-frontends, allowing feature teams to improve at their own pace.

**SaaS administration dashboards**
Implementing dashboards, user management, and billing as separate micro-frontends enabled multiple teams to develop features in parallel.

**Enterprise portals**
Different business units with different technology stacks integrated their features into a single portal, maintaining consistency while enabling departmental innovation.

## Benefits and considerations

Micro-frontends enable development parallelization, shortened release cycles, and increased technical freedom. However, managing multiple build pipelines increases complexity, and version differences between frameworks can introduce bugs. Style conflicts and global variable collisions require mitigation.

## Related terms

- **[Microservices](Microservices.md)** — The backend equivalent of micro-frontends.
- **[Web Components](Web-Components.md)** — Standard technology for micro-frontend integration.
- **[Module Federation](Module-Federation.md)** — Code sharing mechanism in Webpack 5.
- **[API Gateway](API-Gateway.md)** — Supporting backend concept.
- **[DevOps](DevOps.md)** — Independent deployment strategy is important.

## Frequently asked questions

**Q: Do small teams need micro-frontends?**
A: With 1-2 teams, the complexity often outweighs benefits. Consider adoption when team size reaches 3+ for serious parallel development.

**Q: Doesn't this hurt performance?**
A: Properly implemented, lazy loading improves initial load times. Bundle size optimization often improves.

**Q: Can we migrate from existing monolithic apps?**
A: The Strangler pattern enables gradual replacement with new micro-frontends—lower risk than complete rewrites.
