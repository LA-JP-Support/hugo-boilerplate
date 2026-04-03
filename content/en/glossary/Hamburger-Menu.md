---
title: Hamburger Menu
date: 2025-12-19
lastmod: 2026-04-02
translationKey: hamburger-menu
description: A hamburger menu is a UI icon with three horizontal lines that displays navigation menus when clicked. It's an essential element in mobile and responsive design.
keywords:
  - Hamburger Menu
  - UI/UX Design
  - Mobile Navigation
  - Progressive Disclosure
  - Web Accessibility
category: Web Development & Design
type: glossary
draft: false
url: /en/glossary/hamburger-menu/
---

## What is Hamburger Menu?

**A hamburger menu is a UI element—three horizontal lines stacked—that displays navigation menus when clicked.** It's widely adopted in mobile devices and responsive websites to efficiently use limited screen space while offering numerous navigation options.

> **In a nutshell:** A button hiding menus to keep screens simple, expanding to show "three lines" when needed.

**Key points:**

- **What it does:** Toggle button showing/hiding hidden menus on click
- **Why it's needed:** Accommodate many navigation items on small screens while avoiding visual clutter
- **Who uses it:** Mobile app, responsive website, smartwatch app developers

## Why it matters

The hamburger menu is important in mobile-first design. Smartphone screens limit displaying all navigation items simultaneously. Through hamburger menus, designers follow [progressive disclosure](Progressive-Disclosure.md) principles, prioritizing primary content while ensuring secondary access. Additionally, this icon is nearly universally recognized globally, enabling intuitive user experience.

## How it works

The hamburger menu is HTML, CSS, JavaScript interaction. When users click/tap the three-line icon, JavaScript changes the `display` property, showing hidden navigation elements. Designers implement this as semantic `<button>` elements so [accessibility](Accessibility.md) technologies like screen readers interpret correctly.

Visually, animation enables sophisticated interaction. Adding "X" shape animation on click emphasizes open state visually. Such subtle feedback helps users immediately understand menu status.

## Real-world use cases

**Mobile e-commerce sites**

While browsing products, hamburger menus provide category, filter, account access while maximizing product image space.

**News applications**

Links to different sections (politics, economics, technology) stored in menus enable article content focus.

**Enterprise dashboards**

Multi-section admin screens let users access necessary functions while keeping work areas wide.

## Benefits and considerations

Hamburger menus efficiently use screen space but have drawbacks. Hidden menus have low "discoverability"—new users may miss features. Additional steps to open menus suit infrequent access; frequent features require different approaches. Designers should conduct user testing, including only necessary navigation items.

From [accessibility](Accessibility.md) perspective, keyboard menu operation and screen reader compatibility are essential. Adding `aria-label="Menu"` enables non-visual users understanding icon purpose.

## Related terms

- **[Progressive Disclosure](Progressive-Disclosure.md)** — Design pattern for staged information display
- **[Responsive Design](Responsive-Design.md)** — Web design auto-adapting to screen sizes
- **[UI/UX Design](UI-UX-Design.md)** — Creating user-friendly, enjoyable interfaces
- **[Web Accessibility](Web-Accessibility.md)** — Ensuring all users can access websites
- **[Customer Experience](Customer-Experience.md)** — Overall service interaction experience

## Frequently asked questions

**Q: Do users really understand hamburger menus?**

A: Yes, nearly universally recognized now. Adding "Menu" label further clarifies for new or older users.

**Q: Are there hamburger menu alternatives?**

A: Yes—tab bars, bottom navigation bars, sidebars, dropdowns, etc. Optimal patterns vary by use case and content.

**Q: Should hamburger menus always appear on mobile?**

A: Frequently accessed navigation appears in bottom bars; supplementary functions go in hamburger menus—a hybrid approach is effective.
