---
title: Web Components
date: 2025-03-01
lastmod: 2026-04-02
description: A standard technology for creating and integrating reusable UI components using native browser capabilities
translationKey: web-components
category: Web Development & Design
type: glossary
draft: false
url: /en/glossary/web-components/
keywords:
  - Web Components
  - Custom Elements
  - Shadow DOM
  - Templates
  - frontend
---

## What is Web Components?

**Web Components is a technology that uses standard browser APIs (Custom Elements, Shadow DOM, HTML Templates, etc.) to create and integrate reusable, independent UI components.** Without relying on frameworks like React or Vue, you can implement encapsulated components using only native browser features. Once created, these components can be reused across different projects and frameworks, achieving true reusability.

> **In a nutshell:** Web Components are "UI building blocks like LEGO" that follow browser-native standards, making them compatible across any project.

**Key points:**

- **What it does:** Define encapsulated components using browser standards and reuse them as you would HTML tags
- **Why it matters:** Framework-independent reusability, maintainability, and style isolation enable efficient management of large, complex UIs
- **Who uses it:** Front-end developers, design system architects, enterprise application developers

## Why it matters

Traditionally, UI components were locked within specific frameworks like React or Vue. A button component created in React couldn't be used in a Vue project, requiring duplicate implementations across frameworks. Since Web Components is a browser standard, it works across framework boundaries, making integration of legacy and new systems much easier.

In large organizations, multiple teams develop different products using different frameworks. By adopting Web Components as a [design system](Design-System.md), the entire organization can share unified UI components. Additionally, since styles are encapsulated through Shadow DOM, global CSS settings don't affect components, and internal component styles are protected. This dramatically reduces the complexity of managing large stylesheets.

## How it works

Web Components comprises four technologies. First, "Custom Elements" allows you to define custom HTML tags (like `<my-button>`) with behavior implemented in JavaScript classes. Next, "Shadow DOM" creates an isolated DOM area within the component, protecting it from external CSS and JavaScript. "HTML Templates" use the `<template>` tag to store markup blueprints that can be cloned and reused as needed. Finally, "ES Modules" enable distributing and managing components as independent JavaScript modules.

For example, to create a custom button, you define a class with `class MyButton extends HTMLElement`, create Shadow DOM within `connectedCallback()`, and write markup in HTML Templates. Then users can embed a fully encapsulated button with simple HTML like `<my-button>Click me</my-button>`. The button's internal styles and JavaScript don't affect anything outside, and multiple components coexist without style conflicts.

Communication between components happens through data attributes and properties. Data is passed dynamically through "properties," and information is returned to parent components through "events." This architecture enables complex component composition even without a framework.

## Real-world use cases

**Enterprise-wide design systems**

Large tech and media companies develop websites and dashboards using different frameworks (React, Angular, Vue) across business units. Building a [design system](Design-System.md) with Web Components provides framework-neutral, company-wide UI components (buttons, forms, cards, modals, etc.), enabling consistent appearance and behavior across all products.

**Micro-frontend architecture**

In large SaaS platforms where multiple teams develop and deploy independent feature modules, Web Components serve as the ideal unit. Teams can use different technology stacks while combining modules through Web Components, enabling scalable, independent development.

**Adding features to legacy systems**

When adding new features to systems built with older jQuery or vanilla JavaScript, Web Components allow modern development techniques without framework introduction. You can integrate new components simply by embedding them as HTML tags without major legacy code modifications.

## Benefits and considerations

Web Components' greatest benefit is "standardization." Being framework-agnostic, they offer high reusability across teams and projects with easier long-term maintenance. Shadow DOM's style encapsulation eliminates CSS conflicts and global pollution concerns, reducing complexity in large applications. Performance is also excellent with no framework overhead, making them lightweight.

However, while browser support is well established, IE11 is not supported. Additionally, integration with React can be somewhat complex regarding refs and dynamic properties. Debugging and testing tools and knowledge are not as mature as React or Vue. Furthermore, high design freedom can create different patterns per project, making knowledge sharing between teams essential.

## Related terms

- **[Design System](Design-System.md)** — A systematic approach to managing UI elements, with Web Components serving as an implementation foundation
- **[Shadow DOM](Shadow-DOM.md)** — Core Web Components technology that encapsulates styles and DOM structure
- **[Custom Elements](Custom-Elements.md)** — Specification for defining custom HTML tags, a key Web Components feature
- **[Micro-Frontend](Micro-Frontend.md)** — Architecture combining multiple independent front-end modules, with Web Components as the optimal integration unit
- **[Framework-Agnostic Development](Framework-Agnostic.md)** — Development approach independent of frameworks, with Web Components as the realization method

## Frequently asked questions

**Q: Can I develop using only Web Components instead of React or Vue?**

A: Yes. However, for complex state management or routing, code volume increases without a framework. They work well for small to medium component libraries, but for managing entire SPAs, frameworks are often more efficient.

**Q: How should I choose between Web Components and React components?**

A: Web Components excel at "reusability" and "framework independence." React components excel at "high productivity within the framework." Choose Web Components for organization-wide unified UI systems, and React for efficiency in individual projects.

**Q: How much browser support is there?**

A: Modern browsers like Chrome, Firefox, Safari, and Edge have near-complete support. Polyfills enable older browser compatibility, though IE11 has limited functionality. If IE support is required, consider transpilation or polyfill implementation.
