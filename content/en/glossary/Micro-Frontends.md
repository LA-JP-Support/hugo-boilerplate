---
title: "Micro-Frontends"
date: 2025-12-18
lastmod: 2025-12-18
translationKey: "micro-frontends"
description: "An architectural approach that divides a web application into smaller, independently managed frontend parts by different teams, enabling faster development and easier maintenance."
keywords: ["micro frontends", "frontend development", "micro frontend architecture", "web applications", "independent deployment"]
category: "AI Infrastructure & Deployment"
type: "glossary"
draft: false
---

## What Are Micro-Frontends?

Micro-Frontends is an architectural style where a single web application is decomposed into smaller, independently developed, tested, and deployed frontend applications—each owned by separate teams and composed together to create a seamless user experience. This approach extends the microservices paradigm to the frontend, bringing autonomy, scalability, and technology flexibility to web application development.

Each micro-frontend can be built with different frameworks, deployed on different schedules, and maintained by different organizational units—enabling teams to work independently while contributing to a unified application. The architecture addresses the challenge of scaling frontend development as applications grow in complexity and team size increases.

## Historical Context

As web applications increased in complexity, frontend codebases evolved into large monoliths that became difficult to scale and maintain. While microservices revolutionized backend development through independent services, frontend development often remained tightly coupled and monolithic.

The term "micro-frontends" was introduced in the ThoughtWorks Technology Radar in 2016 and subsequently popularized by Martin Fowler. The approach emerged from pain points including difficulty integrating new frameworks, challenges with parallel development for large teams, and high risk in modernizing legacy UIs.

As Single-Page Applications became standard, the need for frontend modularization grew, leading to adoption of micro-frontend patterns enabling team scalability and tech stack flexibility.

## Core Principles

### Domain-Based Decomposition

Micro-frontends typically represent vertical slices of functionality—features or business domains such as "Search," "Cart," or "Profile." Each is developed end-to-end by cross-functional teams responsible for specific business capabilities.

### Team Autonomy

Each micro-frontend team owns the complete software development lifecycle: development, testing, deployment, and maintenance. This autonomy accelerates delivery, reduces bottlenecks, and enables teams to make technology decisions appropriate for their domain.

### Independent Technology Choices

Teams may select different frameworks, libraries, or even programming languages for their micro-frontends. One team could use React, another Vue.js, and a third Angular—each optimized for specific requirements.

### Loose Coupling

Micro-frontends communicate through well-defined APIs and browser events, avoiding shared global state. This reduces accidental dependencies, simplifies integration, and enables independent evolution of components.

### Run-Time Composition

Individual micro-frontends compose into the overall application at runtime, creating seamless user experience. Composition can occur via server-side assembly, client-side integration, or hybrid approaches.

## Key Benefits

<strong>Incremental Modernization:</strong>Enable "strangler fig" pattern—incrementally replacing legacy sections with new micro-frontends, reducing migration risk compared to big-bang rewrites.

<strong>Simpler Codebases:</strong>Each micro-frontend is smaller and more focused, reducing cognitive load and error rates for developers. Easier to understand, test, and maintain.

<strong>Independent Deployment:</strong>Teams deploy micro-frontends independently, enabling faster release cycles and reduced coordination overhead. Fixes or features don't require global redeployment.

<strong>Team Scalability:</strong>Multiple teams develop and ship features in parallel, accelerating delivery and scaling development capacity—vital for large organizations with complex products.

<strong>Technology Flexibility:</strong>Teams can experiment with new frameworks or languages without impacting entire application. Easier to adopt emerging technologies incrementally.

<strong>Improved Resilience:</strong>Failure in one micro-frontend is isolated, minimizing user impact. Lazy loading improves initial load performance by delivering only required components per route.

## Challenges and Trade-offs

<strong>Operational Complexity:</strong>Managing multiple deployment pipelines, versioning, and monitoring introduces overhead. Coordinating cross-team changes can become complex.

<strong>Bundle Size Concerns:</strong>Different library versions can increase bundle size through dependency duplication, resulting in slower load times. Requires careful dependency management.

<strong>Governance Balance:</strong>Too much technology freedom can lead to "framework anarchy," making consistent user experience difficult and increasing maintenance costs. Need governance without excessive constraints.

<strong>CSS and Namespace Management:</strong>Without isolation (CSS modules, Shadow DOM, strict conventions), styles and global variables can leak between micro-frontends causing bugs and visual inconsistencies.

<strong>Communication Complexity:</strong>Defining robust, decoupled communication mechanisms between micro-frontends is non-trivial, especially for complex workflows requiring coordination.

<strong>Testing Requirements:</strong>Ensuring end-to-end quality when application assembles from independently deployed parts requires effective integration and regression testing strategies.

## Integration Patterns

### Server-Side Template Composition

Server assembles final HTML page from fragments served by each micro-frontend.

<strong>Advantages:</strong>Strong isolation, universal rendering, minimal client-side JavaScript.

<strong>Disadvantages:</strong>Limited interactivity, coarse updates, slower for dynamic UIs.

<strong>Example:</strong>Nginx SSI (Server Side Includes).

### Build-Time Integration

Micro-frontends published as libraries (npm packages) and imported by container application at build time.

<strong>Advantages:</strong>Deduplicated dependencies, optimized bundles.

<strong>Disadvantages:</strong>Loses independent deployment, requires coordinated releases.

### Run-Time Integration

<strong>Iframes:</strong>Each micro-frontend loads in iframe, with container managing visibility.
- Pros: Maximum isolation, security
- Cons: Clumsy navigation, poor communication, performance overhead

<strong>JavaScript Entry Points:</strong>Each micro-frontend exposes global render function called by container.
- Pros: Flexible, independent deployments
- Cons: Namespace collisions, dependency management challenges

<strong>Web Components:</strong>Distributed as custom HTML elements leveraging Shadow DOM for encapsulation.
- Pros: Strong encapsulation, tech stack agnostic, native browser support
- Cons: Advanced communication complexity

<strong>Module Federation (Webpack 5+):</strong>Runtime loading and sharing of code between separately built applications.
- Pros: Dynamic loading, fine-grained sharing
- Cons: Requires careful configuration and operational discipline

## Implementation Example

### Food Delivery Application Architecture

<strong>Domain Decomposition:</strong>- Browse Restaurants: Search and filter functionality
- Order Page: Menu selection, customization, checkout
- User Profile: Account settings, order history

<strong>Team Structure:</strong>Each page is a micro-frontend owned by dedicated team.

<strong>Integration:</strong>Container app provides global layout, navigation, shared services. Micro-frontends load dynamically as users navigate.

<strong>Web Components Implementation:</strong>```javascript
class BrowseRestaurants extends HTMLElement {
  connectedCallback() {
    this.innerHTML = '<div>Restaurant browsing interface</div>';
  }
}
window.customElements.define('browse-restaurants', BrowseRestaurants);

class OrderFood extends HTMLElement {
  connectedCallback() {
    this.innerHTML = '<div>Order management interface</div>';
  }
}
window.customElements.define('order-food', OrderFood);
```

**Container Composition:**```html
<div id="main">
  <browse-restaurants></browse-restaurants>
  <!-- Dynamically swap components based on routing -->
</div>
```

<strong>Communication:</strong>Use browser-native CustomEvent, local storage, or event bus for cross-micro-frontend interactions maintaining decoupling.

## Best Practices

<strong>Technology Agnosticism:</strong>Enable teams to choose and upgrade stacks independently. Use browser standards (Custom Elements) for integration boundaries.

<strong>Code Isolation:</strong>Avoid shared globals and runtime dependencies. Namespace CSS, events, and storage preventing collisions.

<strong>Robustness:</strong>Support universal/server-side rendering and progressive enhancement for resilience and performance.

<strong>Communication Patterns:</strong>Favor native browser events over custom APIs for decoupled communication between micro-frontends.

<strong>Shared Component Libraries:</strong>Use central libraries for visual consistency, but ensure encapsulation preventing conflicts.

<strong>Framework Governance:</strong>Align on minimal set of frameworks and conventions avoiding fragmentation, while supporting team flexibility.

<strong>Performance Monitoring:</strong>Track bundle sizes, loading times, and runtime performance across micro-frontends identifying optimization opportunities.

## Repository Organization

<strong>Monorepo:</strong>All micro-frontends in single repository.
- Pros: Easier code sharing, atomic commits, unified CI/CD
- Cons: Can become unwieldy, risk of coupling, slower builds

<strong>Multirepo:</strong>Each micro-frontend in own repository.
- Pros: Strong autonomy, independent pipelines
- Cons: Harder to share code, coordinate cross-repo changes

<strong>Metarepo:</strong>Hybrid approach with multiple repos plus meta-repo for coordination.
- Pros: Balance of autonomy and shared governance
- Cons: Requires additional tooling and coordination

## When to Use

<strong>Appropriate Scenarios:</strong>- Large, complex web apps with distinct business domains
- Multiple teams needing independent delivery cycles
- Incremental migration from legacy monoliths
- Long-term maintainability and feature evolution requirements

<strong>Inappropriate Scenarios:</strong>- Small or single-team applications
- Unstable or rapidly evolving business domains
- Organizational overhead outweighs modularity benefits
- Rapid prototyping or startups with shifting requirements

## Use Cases

<strong>E-Commerce:</strong>Product catalog, cart, and account as separate micro-frontends enabling specialized teams for each domain.

<strong>Food Delivery:</strong>Browsing, ordering, user profile as individual micro-frontends optimized for specific workflows.

<strong>Enterprise Portals:</strong>Dashboard, analytics, admin modules built and deployed independently supporting different release cycles.

<strong>SaaS Platforms:</strong>Integrating independently developed features into single product while maintaining team autonomy.

## Architecture Comparison

| Aspect | Monolithic Frontend | Micro-Frontend Architecture |
|--------|--------------------|-----------------------------|
| <strong>Codebase</strong>| Single, large, tightly coupled | Multiple, smaller, decoupled |
| <strong>Deployment</strong>| All-or-nothing releases | Independent, incremental releases |
| <strong>Team Structure</strong>| Centralized, cross-team coupling | Decentralized, vertical ownership |
| <strong>Tech Stack</strong>| One stack for all | Flexible per micro-frontend |
| <strong>Scaling</strong>| Difficult for teams/features | Teams/features scale independently |
| <strong>Migration</strong>| High risk, hard | Incremental, low risk |

## References


1. Fowler, M. (n.d.). Micro Frontends. Martin Fowler.

2. Micro-Frontends.org. (n.d.). Micro Frontends. Micro-Frontends.org.

3. Wikipedia. (n.d.). Micro Frontend. Wikipedia.

4. ThoughtWorks. (n.d.). Micro Frontends. ThoughtWorks Technology Radar.

5. Webpack. (n.d.). Module Federation. Webpack Documentation.

6. Google. (n.d.). Custom Elements. Google Web Fundamentals.

7. Nginx. (n.d.). Server Side Includes Module. Nginx Documentation.

8. Mozilla. (n.d.). CustomEvent. MDN Web Docs.

9. YouTube. (n.d.). Edge-Side Includes. YouTube Video.
