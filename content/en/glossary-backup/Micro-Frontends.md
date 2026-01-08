---
title: "Micro-Frontends"
date: 2025-11-25
lastmod: 2025-12-05
translationKey: "micro-frontends"
description: "Micro-Frontends is an architectural style decomposing web applications into smaller, independently developed and deployed frontend apps for scalable, autonomous teams."
keywords: ["micro frontends", "frontend development", "micro frontend architecture", "web applications", "independent deployment"]
category: "AI Infrastructure & Deployment"
type: "glossary"
draft: false
---
## Definition

**Micro-Frontends**is an architectural style for web development where a single application is decomposed into smaller, independently developed, tested, and deployed frontend applications—each called a *micro-frontend*. These microapps are owned by separate teams and are composed together to create a seamless user experience.

> “An architectural style where independently deliverable frontend applications are composed into a greater whole.” ([martinfowler.com](https://martinfowler.com/articles/micro-frontends.html))

This concept extends the microservices paradigm, bringing its autonomy and scalability benefits to the frontend. Each micro-frontend can be built with different technologies, deployed on different schedules, and even maintained by different organizational units.
## Background and Evolution

As web applications increased in complexity, frontend codebases grew into large monoliths that became difficult to scale and maintain. While microservices revolutionized backend development by allowing teams to work on independent services, frontend development often remained tightly coupled and monolithic.

The term "micro-frontends" was introduced in the [ThoughtWorks Technology Radar in 2016](https://www.thoughtworks.com/radar/techniques/micro-frontends) and popularized by [Martin Fowler](https://martinfowler.com/articles/micro-frontends.html). The need arose from pain points such as:

- Difficulty integrating new frameworks or features
- Challenges with parallel development for large teams
- High risk and cost in modernizing legacy UIs

As Single-Page Applications (SPAs) became the standard, the need for frontend modularization grew, leading to the adoption of micro-frontend patterns to enable team scalability and tech stack flexibility.

## Core Concepts

### Decomposition by Business Domain

A micro-frontend typically represents a vertical slice of the application—a feature or business domain such as “Search”, “Cart”, or “Profile.” Each is developed end-to-end by a cross-functional team ([micro-frontends.org](https://micro-frontends.org/)).

### Team Autonomy

Each micro-frontend team is responsible for the full software development lifecycle: development, testing, deployment, and maintenance. This autonomy accelerates delivery and reduces bottlenecks.

### Independent Technology Choices

Teams may select different frameworks, libraries, and even programming languages for their micro-frontends. For example, one team could use React, another Vue.js, and a third Angular.

### Loose Coupling, Clear Contracts

Micro-frontends communicate through well-defined APIs and browser events, avoiding shared global state. This reduces accidental dependencies and simplifies integration ([martinfowler.com](https://martinfowler.com/articles/micro-frontends.html#Cross-applicationCommunication)).

### Run-time Composition

Individual micro-frontends are composed into the overall application at runtime, creating a seamless user experience. This can be achieved via server-side assembly, client-side integration, or a hybrid approach.
## Benefits of Micro-Frontends

### Incremental Upgrades and Migration

Migrating a large, monolithic frontend is risky and time-consuming. Micro-frontends enable “strangler fig” modernization—incrementally replacing legacy sections with new micro-frontends, reducing migration risk ([martinfowler.com](https://martinfowler.com/articles/micro-frontends.html#IncrementalUpgrades)).

### Simpler, Decoupled Codebases

Each micro-frontend is smaller and more focused, making the codebase easier to understand, test, and maintain. This reduces cognitive load and error rates for developers.

### Independent Deployment

Teams deploy their micro-frontends independently, allowing faster release cycles and reduced coordination overhead. A fix or feature in one micro-frontend doesn’t require a global redeploy.

### Team Autonomy and Scalability

Multiple teams can develop and ship features in parallel, accelerating delivery and scaling development capacity. This is vital for large organizations with complex products.

### Reusability and Flexibility

Micro-frontends can be reused across different applications or products. Teams can experiment with new frameworks or languages without impacting the whole application.

### Improved Resilience and Performance

A failure in one micro-frontend is isolated, minimizing user impact. Lazy loading of micro-frontends can improve initial load performance by delivering only what’s needed per route.
## Challenges and Downsides

### Increased Operational Complexity

Managing multiple deployment pipelines, versioning, and monitoring for each micro-frontend introduces operational overhead. Coordinating cross-team changes can become complex.

### Bundle Size and Duplication

If teams use different versions of the same library, dependency duplication can increase bundle size, resulting in slower load times ([martinfowler.com](https://martinfowler.com/articles/micro-frontends.html#PayloadSize)).

### Governance and Consistency

Too much freedom in technology choices can lead to “framework anarchy,” making it hard to maintain a consistent user experience and increasing maintenance costs.

### CSS and Global Namespace Conflicts

Without careful isolation (e.g., using CSS modules, Shadow DOM, or strict naming conventions), styles and [global variables](/en/glossary/global-variables/) can leak between micro-frontends, causing bugs and visual inconsistencies.

### Cross-Application Communication

Defining robust, decoupled communication mechanisms between micro-frontends is non-trivial, especially for complex workflows.

### Testing and Quality Assurance

Ensuring end-to-end quality when the application is assembled from independently deployed parts requires effective integration and regression testing strategies.
## Architectural Patterns and Integration Approaches

Micro-frontends can be composed in several ways, each with unique pros and cons.

### 1. Server-Side Template Composition

The server assembles the final HTML page from fragments or partials served by each micro-frontend.  
- **Example:**[Nginx SSI](https://nginx.org/en/docs/http/ngx_http_ssi_module.html)  
- **Pros:**Strong isolation, universal rendering, minimal client-side JS  
- **Cons:**Limited interactivity, coarse updates, slower for dynamic UIs  
### 2. Build-Time Integration

Micro-frontends are published as libraries (npm packages) and imported by a “container” application at build time.  
- **Pros:**Deduplicated dependencies, optimized bundles  
- **Cons:**Loses independent deployment; requires coordinated releases  
### 3. Run-Time Integration

**a. Iframes**Each micro-frontend is loaded in an iframe, with the container application managing which iframe is visible.  
- **Pros:**Maximum isolation, security  
- **Cons:**Clumsy navigation, poor communication, performance overhead  
**b. JavaScript Entry Points**Each micro-frontend exposes a global render function. The container app loads the bundle and calls the function to mount the micro-frontend.  
- **Pros:**Flexible, independent deployments  
- **Cons:**Namespace collisions, dependency management  
**c. Web Components (Custom Elements)**Micro-frontends are distributed as custom HTML elements, leveraging Shadow DOM for encapsulation.  
- **Pros:**Strong encapsulation, tech stack agnostic, native browser support  
- **Cons:**Browser compatibility (modern browsers are fine), advanced communication can be complex  
**d. Module Federation (Webpack 5+)**Allows runtime loading and sharing of code between separately built and deployed applications.  
- **Pros:**Dynamic loading, fine-grained sharing  
- **Cons:**Requires careful configuration and operational discipline  
## Technical Deep Dive & Example

### Example: Food Delivery Application

**Pages:**- *Browse Restaurants*: Search and filter options  
- *Order Page*: Select menu items, customize orders, checkout  
- *User Profile*: Manage account settings, order history  

**Team Structure:**Each page is a micro-frontend, owned and operated by a dedicated team.

**Integration:**A container app provides global layout, navigation, and shared services. Micro-frontends are loaded dynamically as the user navigates.

**Web Components Code Example:**```js
class BrowseRestaurants extends HTMLElement { /* ... */ }
window.customElements.define('browse-restaurants', BrowseRestaurants);

class OrderFood extends HTMLElement { /* ... */ }
window.customElements.define('order-food', OrderFood);

class UserProfile extends HTMLElement { /* ... */ }
window.customElements.define('user-profile', UserProfile);
```

**Composition in Container:**```html
<div id="main">
  <browse-restaurants></browse-restaurants>
  <!-- or dynamically insert <order-food> or <user-profile> as needed -->
</div>
```

**Communication:**Use browser-native [CustomEvent](https://developer.mozilla.org/en-US/docs/Web/API/CustomEvent), local storage, or an event bus for cross-micro-frontend interactions.
## Best Practices & Design Principles

- **Technology Agnosticism:**Teams should be able to choose and upgrade their stack independently. Use browser standards (Custom Elements) for integration boundaries ([micro-frontends.org](https://micro-frontends.org/#core-ideas-behind-micro-frontends)).
- **Team/Code Isolation:**Avoid shared globals and runtime dependencies. Namespace CSS, events, and storage to prevent collisions.
- **Robustness:**Support universal/server-side rendering and progressive enhancement for resilience and performance.
- **Communication Patterns:**Favor native browser events over custom APIs for decoupled communication.
- **Shared Component Libraries:**Use central libraries for visual consistency, but ensure encapsulation to prevent conflicts.
- **Framework Governance:**Align on a minimal set of frameworks and conventions to avoid fragmentation, while supporting team flexibility.
## Types of Micro-Frontend Organization

### Monorepo

All micro-frontends in a single repository.  
- **Pros:**Easier code sharing, atomic commits, unified CI/CD  
- **Cons:**Can become unwieldy, risk of coupling, slower builds

### Multirepo

Each micro-frontend in its own repository.  
- **Pros:**Strong autonomy, independent pipelines  
- **Cons:**Harder to share code and coordinate cross-repo changes

### Metarepo

Hybrid approach: multiple micro-frontend repos with a meta-repo for coordination.  
- **Pros:**Balance of autonomy and shared governance  
- **Cons:**Requires additional tooling and coordination
## When to Use (and When Not To)

### When to Use

- Large, complex web apps with distinct business domains
- Multiple teams needing independent delivery cycles
- Incremental migration from legacy monoliths
- Long-term maintainability and feature evolution

### When *Not* to Use

- Small or single-team applications
- Unstable or rapidly evolving business domains
- Organizational overhead outweighs modularity benefits
- Rapid prototyping/startups with shifting requirements
## Use Cases and Examples

- **E-commerce:**Product catalog, cart, and account as separate micro-frontends
- **Food Delivery:**Browsing, ordering, user profile as individual micro-frontends
- **Enterprise Portals:**Dashboard, analytics, admin modules built/deployed independently
- **SaaS Platforms:**Integrating independently developed features into a single product
## Summary Table: Monolithic vs. Micro-Frontend Architectures

| Aspect               | Monolithic Frontend                | Micro-Frontend Architecture          |
|----------------------|------------------------------------|-------------------------------------|
| **Codebase**| Single, large, tightly coupled     | Multiple, smaller, decoupled        |
| **Deployment**| All-or-nothing, global releases    | Independent, incremental releases   |
| **Team Structure**| Centralized, cross-team coupling   | Decentralized, vertical ownership   |
| **Tech Stack**| One stack for all                  | Flexible, per-micro-frontend        |
| **Scaling**| Difficult for teams and features   | Teams/features scale independently  |
| **Migration**| Hard, high risk                    | Incremental, low risk               |


## References & Further Reading

- [Martin Fowler: Micro Frontends](https://martinfowler.com/articles/micro-frontends.html)
- [Micro-Frontends.org](https://micro-frontends.org/)
- [Wikipedia: Micro Frontend](https://en.wikipedia.org/wiki/Micro_frontend)
- [ThoughtWorks Technology Radar: Micro Frontends](https://www.thoughtworks.com/radar/techniques/micro-frontends)
- [Webpack: Module Federation](https://webpack.js.org/concepts/module-federation/)
- [Custom Elements - Google Developers](https://developers.google.com/web/fundamentals/web-components/customelements)
- [YouTube: Edge-Side Includes explained (from 7:22)](https://youtu.be/A3n1n5QRmF0?t=442)

## Related Terms

Microservices, Single-Page Application (SPA), Web Components, Shadow DOM, Progressive Enhancement, Universal Rendering, Vertical Slices, Monolithic Frontends, Module Federation

*For practical patterns and implementation details, see [martinfowler.com/articles/micro-frontends.html](https://martinfowler.com/articles/micro-frontends.html) and [micro-frontends.org](https://micro-frontends.org/).*

**This glossary provides a comprehensive, detail-rich, and reference-linked overview of micro-frontends, their rationale, patterns, and best practices. For deeper technical dives and real-world case studies, always consult the [Martin Fowler article](https://martinfowler.com/articles/micro-frontends.html) and [Micro-Frontends.org](https://micro-frontends.org/).**
