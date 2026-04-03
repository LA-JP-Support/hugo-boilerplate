---
title: Carousel (UI Component)
date: 2025-12-19
lastmod: 2026-04-02
translationKey: carousel-ui-component
description: A carousel is a UI component that displays multiple images or cards in a single view, allowing users to browse by swiping or clicking.
keywords:
- carousel
- UI component
- web design
- UX design
- interaction
category: Web Development & Design
type: glossary
draft: false
url: /en/glossary/carousel/
---

## What is a Carousel?

**A carousel is a UI component that displays multiple images or cards sequentially in a single area, allowing users to browse through them one by one using arrows or swipes.** Named after the rotating carousel horses at amusement parks, the content appears to rotate. Carousels are used in many scenarios: product galleries on e-commerce sites, header images on news sites, and onboarding on mobile apps. While it has the advantage of displaying multiple pieces of content in limited screen space, many users view little beyond the first slide, which is a known challenge.

> **In a nutshell:** A carousel is like flipping through magazine covers one at a time. You can focus on one piece of information at a time, but you easily miss the pages deeper in the stack.

**Key points:**

- **What it does:** Displays multiple items sequentially in one space with navigation features for browsing
- **Why it's needed:** To present multiple pieces of information in limited screen space while focusing attention on one item
- **Who uses it:** E-commerce companies, news sites, mobile app developers

## Why it matters

Web page screen space is limited. Displaying many products or news articles in a grid divides user attention more than a carousel showing "one at a time." Animation effects also capture attention. However, usability research shows "the vast majority of users view nothing beyond the first slide," requiring careful design consideration.

## How it works

A carousel contains multiple elements (slides) in a container with the display area restricted to show only one at a time. Clicking arrow buttons or dot pagination, or swiping on mobile, displays the next slide. Optionally, it can rotate automatically, though allowing user control is better for accessibility. Keyboard navigation and screen reader support are also important.

## Real-world use cases

**Product gallery** E-commerce sites show products from multiple angles.

**News carousel** Homepage headers display rotating images at the top.

**Onboarding** Apps explain features to new users across multiple carousel steps.

**Recommended products corner** Limited smartphone screen space shows recommended products one at a time in sequence.

## Benefits and considerations

Benefits include presenting much information in limited space and capturing attention visually. It also works well for mobile adaptation.

A key consideration is that usability research shows "most users view only the first slide and not the second onward." Hiding important information in later slides misses opportunities. Auto-rotating carousels also suffer from banner blindness (ignored like advertisements).

## Design best practices

Three to five slides are ideal. More than that, users won't realize "there's more." Include all important information in the first slide. Arrows and dots must be clear; touch devices require sufficient sizing. User-controlled carousels are preferable to auto-rotating. Pay attention to accessibility (keyboard control, screen reader support).

## Alternative approaches

Grid display (showing multiple items simultaneously) takes more space but has higher discoverability. Tab format lets you view multiple pages at once and switch quickly. Infinite scroll (more appear as you scroll down) works well for mobile. Depending on the situation, consider alternatives to carousels.

## Frequently asked questions

**Q: Can carousel negatively impact user experience?**
A: Yes. Research shows 84% of users don't view slides after the first one. Important information shouldn't be hidden in carousels; displaying multiple items simultaneously is often better.

**Q: Should it auto-rotate?**
A: Avoid it on mobile. Even on desktop, user-controlled carousels are preferred. If auto-rotating, always include a pause button.

**Q: How do I ensure accessibility?**
A: Allow keyboard navigation with arrow keys and Tab. Add ARIA labels for screen reader support. Image descriptions (alt text) are essential.

## References

- [Nielsen Norman Group: Carousel Design](https://www.nngroup.com/articles/designing-effective-carousels/)
- [W3C: Carousel Accessibility](https://www.w3.org/WAI/tutorials/carousels/)
- [Smashing Magazine: UI Design Patterns](https://www.smashingmagazine.com/)
- [A List Apart: User Experience](https://alistapart.com/)
- [UX Collective: Design Patterns](https://uxdesign.cc/)
- [Interaction Design Foundation: UX](https://www.interaction-design.org/)
- [Material Design: Carousel Components](https://material.io/)
- [Ant Design: Component Library](https://ant.design/)
