---
title: React
date: 2025-03-01
lastmod: 2026-04-02
translationKey: react
description: A JavaScript library developed by Facebook. Efficiently builds dynamic UIs. Standardizing web development.
keywords:
  - JavaScript
  - Frontend
  - UI framework
  - Components
  - Virtual DOM
category: Web Development & Design
type: glossary
draft: false
url: /en/glossary/React/
---

## What is React?

**React is a JavaScript library developed by Facebook for efficiently building dynamic, interactive user interfaces (UI).** React uses "components," reusable UI building blocks as its foundation, constructing complex UIs. When data changes, React automatically updates UI elements efficiently using "virtual DOM" technology, letting developers focus simply on UI logic while maintaining optimal performance. Since its 2013 release, it's become the de facto standard for web application development, adopted by enterprises worldwide.

> **In a nutshell:** Like building complex websites from LEGO blocks—combining small UI pieces (buttons, text boxes)—React efficiently constructs complex web pages.

**Key points:**

- **What it does:** Define UI components in JavaScript, automatically updating UI when data changes
- **Why it's needed:** Develop large, complex web applications maintainably and efficiently
- **Who uses it:** Frontend developers, web application companies, startups

## Why it matters

React matters because it systematized and scaled web application development. Traditional JavaScript development required direct DOM manipulation; complex applications had many bugs and difficult maintenance. Updating entire DOM each data change degraded performance.

React solved these problems. Component orientation enables independent UI development and testing, improving code reusability and reducing bugs. Virtual DOM technology minimizes actual DOM updates, keeping applications fast. JSX syntax—writing HTML-like UI and JavaScript logic together—dramatically improves development efficiency.

Currently, Netflix, Uber, Airbnb, and Facebook itself use React, making it web application development's standard.

## How it works

React's mechanism comprises three elements: "components," "state management," and "virtual DOM."

Components are React's smallest units. JavaScript functions or classes represent UI portions (buttons, forms, lists). A "user info card" component displays username, email, profile image. Importantly, components contain other components, expressing complex UI through small combined pieces.

State management means handling application state data—"user-entered text," "login status." React manages this through "state" concept. State changes trigger automatic related component re-rendering. Developers need not explicitly write "when data changes, do this"—simply declaring "this UI displays based on this data" suffices.

Virtual DOM is React's high-performance secret. Normal web applications have JavaScript directly manipulate DOM, with browsers re-rendering. Frequent DOM manipulation is slow, heavily burdening browsers. React instead creates virtual DOM—memory JavaScript objects representing UI—when data changes. Comparing previous and current virtual DOM ("diffing"), only changed portions are reflected in actual DOM. This minimizes DOM operations, making applications fast.

JSX is syntax writing HTML-like markup inside JavaScript. For example, component definition:

```jsx
function Greeting({ name }) {
  return <h1>Hello, {name}!</h1>;
}
```

This looks like HTML but is JavaScript. Compilation converts it to JavaScript function calls. This syntax makes UI and logic visually clear.

## Real-world use cases

**Social media platforms**

Facebook, Instagram, Twitter are extremely dynamic applications loading new content as users scroll, with likes/comments reflecting in real-time. React efficiently manages complex state changes, maintaining high performance—ideal for these platforms.

**E-commerce platforms**

Amazon, Shopify have product filtering, cart management, checkout flows—multiple interrelated UI elements. React's component orientation enables independent feature development, easing maintenance.

**Collaboration tools**

Google Docs, Figma enable multiple users real-time co-editing, requiring immediate response to user input and reflecting other users' changes. React's performance and state management handle these complex requirements.

## Benefits and considerations

React's greatest benefits combine development efficiency and application performance. Component orientation modularizes UI development, improving reusability. Virtual DOM provides speed for complex applications. Ecosystem is rich—routing, state management, UI libraries are abundant.

Considerations include learning curves requiring JavaScript and web fundamentals knowledge. Small projects might find React setup complex. SEO requires server-side rendering and other workarounds.

## Related terms

- **Vue.js** — Similar component-oriented framework to React
- **Angular** — Heavier full-stack framework than React
- **JavaScript** — Programming language underlying React
- **Node.js** — Used for React application building and server implementation

## Frequently asked questions

**Q: Is React a library or framework?**
A: React is precisely a library. It specializes in UI rendering; routing and state management require separate libraries. Angular is a full-stack framework including all these.

**Q: Can React develop mobile apps?**
A: Yes. Using "React Native" enables developing iOS and Android native apps using same React component logic.

**Q: Should small projects use React?**
A: Small projects might find React setup excessive. HTML and vanilla JavaScript may suffice. However, if future expansion is possible, starting with React provides later advantages.
