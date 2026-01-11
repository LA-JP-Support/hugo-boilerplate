---
title: "Auto-Layout"
lastmod: 2025-12-18
translationKey: "auto-layout"
description: "Auto-Layout is a design feature that automatically arranges and resizes UI elements based on rules you set, so your interface stays organized and balanced when content or screen size changes."
keywords: ["Auto-Layout", "Figma", "UI design", "Responsive design", "Constraints"]
category: "General"
type: "glossary"
date: 2025-12-18
draft: false
---

## What is Auto-Layout?

Auto-Layout is a design and development feature that arranges, aligns, and resizes interface elements automatically based on rules or constraints you define. When the content, screen size, or the number of elements changes, Auto-Layout recalculates and repositions elements, ensuring your interface remains clean, legible, and responsive.

Imagine a bookshelf that automatically shifts and spaces its books every time you add or remove one. Auto-Layout does the same for UI elements: no matter how many you insert or remove, your design stays organized and visually balanced.

## Why Use Auto-Layout?

**Key Benefits**

**Efficiency**
- Significantly reduces manual resizing and repositioning
- Update content or components once, and the layout adapts everywhere

**Responsive Design**
- Elements adapt to various screen sizes
- Ideal for multi-device design workflows

**Consistency**
- Maintains uniform spacing, alignment, and proportions across entire projects

**Collaboration**
- Designers and developers rely on the same set of rules
- Streamlines handoff and minimizes miscommunication

**Use Cases**
- Buttons that grow or shrink to fit their text
- Dynamic lists or menus
- Product galleries and dashboards
- Adaptive website layouts

## Core Concepts

**Constraints**
- Define rules between elements
- Example: "Button is always 16px below the label"

**Direction**
- The axis along which elements are arranged—horizontal, vertical, wrap, or grid

**Resizing**
- Determines if containers and children hug content, fill space, or are fixed

**Spacing & Padding**
- Sets gaps between elements and space inside containers

**Alignment**
- Dictates position within the container—center, left, right, etc.

**Nesting**
- Place Auto-Layout frames within each other for sophisticated structures

## Auto-Layout in Figma

**Adding and Removing Auto-Layout**
- Add: Select layers → Press `Shift + A` or click Add auto layout in sidebar
- Remove: Select frame → Press `Option + Shift + A` (Mac) or `Alt + Shift + A` (Windows)

**Direction Options**
- Horizontal: Arranges children in a row
- Vertical: Arranges elements in a column
- Wrap: Allows elements to continue onto new lines/columns when space is limited
- Grid (Beta): Arranges elements in both rows and columns

**Spacing, Padding & Gaps**
- Gap/Spacing: The space between items; set as a fixed value or "Auto"
- Padding: The space inside the frame between the border and its children
- Example: A button with 16px horizontal and 8px vertical padding

**Resizing Options**
- Hug Contents: Frame resizes to fit its children
- Fill Container: Child expands to fill available space in its parent
- Fixed Size: Dimensions remain constant
- Min/Max Constraints: Set minimum/maximum size an element can shrink or grow to

**Nesting Auto-Layouts**
- Nesting allows one Auto-Layout frame inside another for modular and complex designs
- Example: A card component with vertical Auto-Layout, a header row (horizontal), and a content area (vertical)

**Alignment and Distribution**
- Alignment: Controls position within the container
- Distribution: Evenly spaces elements along the main axis

**Ignoring Auto-Layout (Absolute Positioning)**
- Absolute Positioning (now called "Ignore Auto-Layout") lets you exclude an element from the layout flow
- Example: A notification badge positioned on the corner of an icon

## Auto-Layout in Other Platforms

**iOS (SwiftUI & UIKit)**
- UIKit Auto Layout: Uses constraints to define spatial relationships
- SwiftUI: Uses HStack, VStack, ZStack, and Spacer for responsive arrangements
- Tips: Use Interface Builder for visual constraint editing; use "Safe Area" guides for layouts that adapt to notches

**Android (Jetpack Compose, XML, ConstraintLayout)**
- ConstraintLayout (XML): Defines constraints for flexible layouts with flat view hierarchy
- Jetpack Compose: Uses Row, Column, Box, and ConstraintLayout composables
- Best Practice: Use ConstraintLayout for complex, adaptive UIs and to avoid deep nesting

**Web (CSS Flexbox, Grid)**
- Flexbox: One-dimensional layout (row or column); items grow/shrink to fit space
- CSS Grid: Two-dimensional layout for rows and columns
- Example: Flexbox for navigation bars; Grid for product listings and dashboards

## Common Use Cases

**Buttons That Expand with Text**
- Set the button container to "Hug contents" with fixed padding

**Responsive Lists and Menus**
- Use vertical Auto-Layout or a vertical stack so items reflow and spacing remains consistent

**Cards and Complex Components**
- Nest Auto-Layout frames for each region (header, content, actions)

**Notification Badges**
- Use "Ignore Auto-Layout" or absolute positioning for badges overlaying icons

**Adaptive Webpages**
- Use CSS Grid or Flexbox to make content reflow for different screen sizes

## Best Practices

**Start Small**
- Begin with small components (e.g., buttons) before scaling up

**Use Nesting**
- Create modular, reusable designs

**Apply Consistent Spacing**
- Use variables or tokens

**Document Layout Rules**
- For clarity and future maintenance

**Use Keyboard Shortcuts**
- For efficiency

## Troubleshooting

**Elements Overlap or Don't Resize**
- Check resizing settings and ensure correct settings for parent/child

**Alignment Not Working**
- Ensure there's room for alignment; "hug" frames may limit visible alignment changes

**Too Many Nested Frames**
- Simplify layout structure where possible

**Badge/Overlay Not Positioning**
- Use "Ignore Auto-Layout"

**Spacing Off After Applying Auto-Layout**
- Adjust padding and gap values manually

## Frequently Asked Questions

**What's the difference between Hug, Fill, and Fixed in Figma Auto-Layout?**
- Hug: Container matches its children's size
- Fill: Child fills the parent's available space
- Fixed: Element stays the same size

**Can I combine horizontal and vertical Auto-Layouts?**
- Yes, via nesting: e.g., vertical Auto-Layout for a card, horizontal for the card's header

**How do I make an element ignore Auto-Layout rules?**
- Use "Ignore Auto-Layout" (absolute positioning)

**Does Auto-Layout work for responsive design?**
- Yes, it's designed for adaptive/responsive interfaces

**Why does my Auto-Layout frame shrink/expand unexpectedly?**
- Figma sets initial padding based on content—adjust values in the right panel as needed

## References

- [Figma Auto-Layout YouTube Tutorial](https://www.youtube.com/watch?v=1odqpkfkDL8)
- [Figma Help Center – Guide to auto layout](https://help.figma.com/hc/en-us/articles/360040451373-Guide-to-auto-layout)
- [Figma Handbook – Advanced Auto Layout (Design+Code)](https://designcode.io/figma-handbook-advanced-layout)
- [CSS Flexbox Guide (MDN)](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout/Basic_concepts)
- [CSS Grid Guide (MDN)](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/Relationship_with_other_layout_methods)
- [Apple Auto Layout Documentation](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/AutolayoutPG/index.html)
- [Android ConstraintLayout Guide](https://developer.android.com/develop/ui/views/layout/constraint-layout)
- [ConstraintLayout in Jetpack Compose](https://developer.android.com/develop/ui/compose/layouts/constraintlayout)
- [Apple Developer: Layout](https://developer.apple.com/documentation/appkit/layout?language=objc)
