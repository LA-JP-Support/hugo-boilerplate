---
title: "Auto-Layout"
lastmod: 2025-12-18
translationKey: "auto-layout"
description: "Auto-Layout is a design feature that automatically arranges and resizes UI elements based on rules you set, keeping your interface organized and balanced when content or screen size changes."
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

<strong>Key Benefits</strong>

<strong>Efficiency</strong>- Significantly reduces manual resizing and repositioning
- Update content or components once, and the layout adapts everywhere

<strong>Responsive Design</strong>- Elements adapt to various screen sizes
- Ideal for multi-device design workflows

<strong>Consistency</strong>- Maintains uniform spacing, alignment, and proportions across entire projects

<strong>Collaboration</strong>- Designers and developers rely on the same set of rules
- Streamlines handoff and minimizes miscommunication

<strong>Use Cases</strong>- Buttons that grow or shrink to fit their text
- Dynamic lists or menus
- Product galleries and dashboards
- Adaptive website layouts

## Core Concepts

<strong>Constraints</strong>- Define rules between elements
- Example: "Button is always 16px below the label"

<strong>Direction</strong>- The axis along which elements are arranged—horizontal, vertical, wrap, or grid

<strong>Resizing</strong>- Determines if containers and children hug content, fill space, or are fixed

<strong>Spacing & Padding</strong>- Sets gaps between elements and space inside containers

<strong>Alignment</strong>- Dictates position within the container—center, left, right, etc.

<strong>Nesting</strong>- Place Auto-Layout frames within each other for sophisticated structures

## Auto-Layout in Figma

<strong>Adding and Removing Auto-Layout</strong>- Add: Select layers → Press `Shift + A` or click Add auto layout in sidebar
- Remove: Select frame → Press `Option + Shift + A` (Mac) or `Alt + Shift + A` (Windows)

<strong>Direction Options</strong>- Horizontal: Arranges children in a row
- Vertical: Arranges elements in a column
- Wrap: Allows elements to continue onto new lines/columns when space is limited
- Grid (Beta): Arranges elements in both rows and columns

<strong>Spacing, Padding & Gaps</strong>- Gap/Spacing: The space between items; set as a fixed value or "Auto"
- Padding: The space inside the frame between the border and its children
- Example: A button with 16px horizontal and 8px vertical padding

<strong>Resizing Options</strong>- Hug Contents: Frame resizes to fit its children
- Fill Container: Child expands to fill available space in its parent
- Fixed Size: Dimensions remain constant
- Min/Max Constraints: Set minimum/maximum size an element can shrink or grow to

<strong>Nesting Auto-Layouts</strong>- Nesting allows one Auto-Layout frame inside another for modular and complex designs
- Example: A card component with vertical Auto-Layout, a header row (horizontal), and a content area (vertical)

<strong>Alignment and Distribution</strong>- Alignment: Controls position within the container
- Distribution: Evenly spaces elements along the main axis

<strong>Ignoring Auto-Layout (Absolute Positioning)</strong>- Absolute Positioning (now called "Ignore Auto-Layout") lets you exclude an element from the layout flow
- Example: A notification badge positioned on the corner of an icon

## Auto-Layout in Other Platforms

<strong>iOS (SwiftUI & UIKit)</strong>- UIKit Auto Layout: Uses constraints to define spatial relationships
- SwiftUI: Uses HStack, VStack, ZStack, and Spacer for responsive arrangements
- Tips: Use Interface Builder for visual constraint editing; use "Safe Area" guides for layouts that adapt to notches

<strong>Android (Jetpack Compose, XML, ConstraintLayout)</strong>- ConstraintLayout (XML): Defines constraints for flexible layouts with flat view hierarchy
- Jetpack Compose: Uses Row, Column, Box, and ConstraintLayout composables
- Best Practice: Use ConstraintLayout for complex, adaptive UIs and to avoid deep nesting

<strong>Web (CSS Flexbox, Grid)</strong>- Flexbox: One-dimensional layout (row or column); items grow/shrink to fit space
- CSS Grid: Two-dimensional layout for rows and columns
- Example: Flexbox for navigation bars; Grid for product listings and dashboards

## Common Use Cases

<strong>Buttons That Expand with Text</strong>- Set the button container to "Hug contents" with fixed padding

<strong>Responsive Lists and Menus</strong>- Use vertical Auto-Layout or a vertical stack so items reflow and spacing remains consistent

<strong>Cards and Complex Components</strong>- Nest Auto-Layout frames for each region (header, content, actions)

<strong>Notification Badges</strong>- Use "Ignore Auto-Layout" or absolute positioning for badges overlaying icons

<strong>Adaptive Webpages</strong>- Use CSS Grid or Flexbox to make content reflow for different screen sizes

## Best Practices

<strong>Start Small</strong>- Begin with small components (e.g., buttons) before scaling up

<strong>Use Nesting</strong>- Create modular, reusable designs

<strong>Apply Consistent Spacing</strong>- Use variables or tokens

<strong>Document Layout Rules</strong>- For clarity and future maintenance

<strong>Use Keyboard Shortcuts</strong>- For efficiency

## Troubleshooting

<strong>Elements Overlap or Don't Resize</strong>- Check resizing settings and ensure correct settings for parent/child

<strong>Alignment Not Working</strong>- Ensure there's room for alignment; "hug" frames may limit visible alignment changes

<strong>Too Many Nested Frames</strong>- Simplify layout structure where possible

<strong>Badge/Overlay Not Positioning</strong>- Use "Ignore Auto-Layout"

<strong>Spacing Off After Applying Auto-Layout</strong>- Adjust padding and gap values manually

## Frequently Asked Questions

<strong>What's the difference between Hug, Fill, and Fixed in Figma Auto-Layout?</strong>- Hug: Container matches its children's size
- Fill: Child fills the parent's available space
- Fixed: Element stays the same size

<strong>Can I combine horizontal and vertical Auto-Layouts?</strong>- Yes, via nesting: e.g., vertical Auto-Layout for a card, horizontal for the card's header

<strong>How do I make an element ignore Auto-Layout rules?</strong>- Use "Ignore Auto-Layout" (absolute positioning)

<strong>Does Auto-Layout work for responsive design?</strong>- Yes, it's designed for adaptive/responsive interfaces

<strong>Why does my Auto-Layout frame shrink/expand unexpectedly?</strong>- Figma sets initial padding based on content—adjust values in the right panel as needed

## References


1. Figma. (n.d.). Auto-Layout YouTube Tutorial. YouTube.

2. Figma. (n.d.). Guide to auto layout. Figma Help Center.

3. Design+Code. (n.d.). Figma Handbook – Advanced Auto Layout. Design+Code.

4. MDN. (n.d.). CSS Flexbox Guide. Mozilla Developer Network.

5. MDN. (n.d.). CSS Grid Guide. Mozilla Developer Network.

6. Apple. (n.d.). Auto Layout Documentation. Apple Developer Library.

7. Google. (n.d.). Android ConstraintLayout Guide. Android Developers.

8. Google. (n.d.). ConstraintLayout in Jetpack Compose. Android Developers.

9. Apple. (n.d.). Developer: Layout. Apple Developer Documentation.
