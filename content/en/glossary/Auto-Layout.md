---
title: Auto-Layout
date: 2026-04-02
lastmod: 2026-04-02
translationKey: auto-layout
description: A design feature automatically positioning and resizing UI elements. Implemented in Figma, iOS, Android, and CSS as the foundation of responsive design.
keywords:
- auto-layout
- Figma
- responsive design
- UI design
- constraint
category: Web Development & Design
type: glossary
draft: false
url: /en/glossary/auto-layout/
---

## What is Auto-Layout?

**Auto-Layout is a feature automatically positioning and resizing UI elements based on designer-defined rules.** When content changes, layouts adjust automatically, efficiently creating responsive interfaces handling different text lengths and device sizes. Implemented across Figma, iOS, Android, and CSS, it's a modern UI design fundamental.

> **In a nutshell:** Like a bookshelf—adding or removing books automatically closes gaps or spreads spacing.

**Key points:**

- **What it does:** Automatically align and resize UI elements following defined rules
- **Why it's needed:** Eliminate repetitive manual adjustments for content and device changes
- **Who uses it:** UI designers, UX designers, front-end developers

## Why it matters

Traditionally, when button text increased, designers manually resized the button, adjusted internal spacing, and repositioned elements for layout changes. This repetitive work consumed time and introduced errors. Auto-Layout automates this, letting designers focus on creative decisions.

Data shows enterprises adopting Auto-Layout reduce responsive design time by 60% average. This accelerates all design phases—from prototyping to final implementation.

## How it works

Auto-Layout consists of three major elements. First, **direction**—arrange horizontally (row), vertically (column), or grid format. Second, **spacing**—gaps between elements and internal padding. Third, **resize behavior**—when parent container changes, do elements match content size, fill parent space, or stay fixed?

Workflow: First set Auto-Layout on basic units like buttons and cards. Next add settings to containers holding multiple elements. Finally, when text increases, icons add, or device width changes, the system automatically recalculates positioning.

## Real-world use cases

**Button text auto-adjustment**
When "Confirm" becomes "Confirm now," buttons automatically expand and internal spacing self-adjusts. Designers continue without manual resizing.

**Multi-device support**
Same component automatically generates optimal layout for smartphone (320px width) and tablet (768px width).

**Dynamic list generation**
E-commerce product lists whether 100 or 1000 items automatically align correctly, minimizing developer work.

## Benefits and considerations

Auto-Layout's biggest benefit is design-development efficiency. Designers correctly defining rules lets developers implement nearly identically using auto-generated code. Content changes become simple—modifications are easy, brand consistency is maintained.

However, initial setup is complex. Wrong parent padding ripples to all children. Very complex layouts (overlaps, conditionals) may exceed Auto-Layout capabilities, requiring manual adjustment. Settings errors cascade failures.

## Related terms

- **Responsive Design** — Design principles auto-adapting to different device sizes
- **CSS Flexbox** — One-dimensional layout specification for web
- **CSS Grid** — Two-dimensional grid layout for web
- **Component Design** — Design methodology for reusable UI units
- **Constraint** — Relative positioning rules between UI elements

## Frequently asked questions

**Q: How to add Auto-Layout in Figma?**
A: Select element, click "Add Auto-Layout" in right panel (or Shift+A). Set direction (horizontal/vertical), spacing, padding. Takes seconds with practice.

**Q: Different layouts needed for mobile vs. desktop?**
A: Difficult with Auto-Layout alone—needs multiple layout rule sets. Figma: create multiple components with device-width switching. CSS: use @media queries for conditional rules.

**Q: Positioning components ignoring Auto-Layout?**
A: Badges and tooltips overlaying others use "ignore Auto-Layout." This positions absolutely. But overuse obscures layout intent—limit to specific cases.
