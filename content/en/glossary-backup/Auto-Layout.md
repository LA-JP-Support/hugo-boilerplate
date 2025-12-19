---
title: "Auto-Layout"
translationKey: "auto-layout"
description: "Master Auto-Layout, a design feature for automatically arranging and resizing UI elements. Covers core concepts, benefits, and implementation in Figma, iOS, Android, and Web."
keywords: ["Auto-Layout", "Figma", "UI design", "Responsive design", "Constraints"]
category: "General"
type: "glossary"
date: 2025-12-02
draft: false
---
## What is Auto-Layout?

Auto-Layout is a design and development feature that arranges, aligns, and resizes interface elements automatically based on rules or constraints you define. When the content, screen size, or the number of elements changes, Auto-Layout recalculates and repositions elements, ensuring your interface remains clean, legible, and responsive.

**Analogy:**  
Imagine a bookshelf that automatically shifts and spaces its books every time you add or remove one. Auto-Layout does the same for UI elements: no matter how many you insert or remove, your design stays organized and visually balanced.

**Figma Official Guide:**  
[Guide to auto layout – Figma Help Center](https://help.figma.com/hc/en-us/articles/360040451373-Guide-to-auto-layout)


## Why Use Auto-Layout?

**Key Benefits:**

- **Efficiency:** Significantly reduces manual resizing and repositioning. Update content or components once, and the layout adapts everywhere.
- **Responsive Design:** Elements adapt to various screen sizes, making it ideal for multi-device design workflows.
- **Consistency:** Maintains uniform spacing, alignment, and proportions across entire projects.
- **Collaboration:** Designers and developers rely on the same set of rules, streamlining the handoff and minimizing miscommunication.

**Use Cases:**  
- Buttons that grow or shrink to fit their text  
- Dynamic lists or menus  
- Product galleries and dashboards  
- Adaptive website layouts

**Further Reading:**  
- [A Guide to Auto Layout: Best Practices, Tips & Tricks | Figma (YouTube)](https://www.youtube.com/watch?v=1odqpkfkDL8)
- [Figma Handbook: Advanced Auto Layout by Design+Code](https://designcode.io/figma-handbook-advanced-layout)


## How Auto-Layout Works

### Core Concepts

Auto-Layout uses layout rules, or **constraints**, to govern the spatial relationships of UI elements. Here’s how it operates:

- **Constraints:** Define rules between elements, e.g., "Button is always 16px below the label."
- **Direction:** The axis along which elements are arranged—horizontal, vertical, wrap, or grid.
- **Resizing:** Determines if containers and children hug content, fill space, or are fixed.
- **Spacing & Padding:** Sets gaps between elements and space inside containers.
- **Alignment:** Dictates position within the container—center, left, right, etc.
- **Nesting:** Place Auto-Layout frames within each other for sophisticated structures.

**Example:**  
A button whose width "hugs" its label will automatically resize as the text changes, maintaining consistent padding.

**Official Documentation:**  
- [Figma: Guide to auto layout](https://help.figma.com/hc/en-us/articles/360040451373-Guide-to-auto-layout)
- [Understanding Auto Layout – Apple Developer](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/AutolayoutPG/index.html#//apple_ref/doc/uid/TP40010853-CH7-SW1)

### Key Features

- **Automatic Arrangement:** No pixel-by-pixel adjustments; structure is handled automatically.
- **Content-Driven Resizing:** Elements grow/shrink to fit content or available space.
- **Flexible Alignment:** Align elements (left, center, right, top, bottom) or distribute them evenly.
- **Nesting:** Create complex layouts by combining multiple Auto-Layouts.
- **Absolute Positioning:** Exclude specific children from the Auto-Layout rules when needed.


## Platform Specifics: Auto-Layout in Figma

Figma’s Auto-Layout is one of the most powerful tools for interface design and prototyping.

### Adding and Removing Auto-Layout

- **Add:** Select layers → Press `Shift + A` or click **Add auto layout** in the sidebar.
- **Remove:** Select frame → Press `Option + Shift + A` (Mac) or `Alt + Shift + A` (Windows) or right-click and select **Remove auto layout**.

If you select objects not already in a frame, Figma creates a new frame with Auto-Layout applied.

[Official Figma Instructions](https://help.figma.com/hc/en-us/articles/360040451373-Guide-to-auto-layout)


### Direction: Horizontal, Vertical, Wrap, and Grid

- **Horizontal:** Arranges children in a row.
- **Vertical:** Arranges elements in a column.
- **Wrap:** Allows elements to continue onto new lines/columns when space is limited.
- **Grid (Beta):** Arranges elements in both rows and columns.

**How to Switch:**  
Use the Direction controls in Figma’s right panel.

**Learn More:**  
[Auto layout flow in Figma](https://help.figma.com/hc/en-us/articles/360040451373-Guide-to-auto-layout#flow)


### Spacing, Padding & Gaps

- **Gap/Spacing:** The space between items; set as a fixed value or “Auto.”
- **Padding:** The space inside the frame between the border and its children; can be set uniformly or for each side.

**Adjustment:**  
Set values in the right sidebar or drag handles on the canvas.

**Example:**  
A button with 16px horizontal and 8px vertical padding.

**Deep Dive:**  
[Advanced spacing and alignment – Figma Handbook](https://designcode.io/figma-handbook-advanced-layout)


### Resizing Options: Hug, Fill, Fixed, Min/Max

- **Hug Contents:** Frame resizes to fit its children.
- **Fill Container:** Child expands to fill available space in its parent.
- **Fixed Size:** Dimensions remain constant, regardless of content or parent size.
- **Min/Max Constraints:** Set the minimum/maximum size an element can shrink or grow to.

**How to Set:**  
Use the Width/Height dropdowns in Figma’s right panel.

**Example:**  
A button with width set to "Hug" and a minimum width of 100px prevents it from becoming too small.

[Resizing and constraints in Figma](https://help.figma.com/hc/en-us/articles/360040451373-Guide-to-auto-layout#resize)


### Nesting Auto-Layouts

**Nesting** allows one Auto-Layout frame inside another for modular and complex designs.

**Example:**  
A card component with vertical Auto-Layout, a header row (horizontal), and a content area (vertical).

**Shortcut:**  
`Ctrl + Shift + A` (Mac) or `Ctrl + Alt + Shift + A` (Windows) for “Suggest Auto-Layout.”

[Building complex layouts – Figma Help Center](https://help.figma.com/hc/en-us/articles/360040451373-Guide-to-auto-layout#nest)


### Alignment and Distribution

- **Alignment:** Controls position within the container.
- **Distribution:** Evenly spaces elements along the main axis.

**How to Set:**  
Use the alignment controls (the “gram cracker” icon) in the sidebar.

**Troubleshooting:**  
Alignment changes only have an effect when there’s space to align within; “hug” frames may show no visible change.

[Alignment and distribution in Figma](https://help.figma.com/hc/en-us/articles/360040451373-Guide-to-auto-layout#align)


### Ignoring Auto-Layout (Absolute Positioning)

**Absolute Positioning** (now called "Ignore Auto-Layout") lets you exclude an element from the layout flow for overlays like badges.

**How to Use:**  
Select the element → Design panel → Click “Ignore auto layout” or drag it while holding `Ctrl`.

**Example:**  
A notification badge positioned on the corner of an icon.

[Absolute positioning in Figma](https://help.figma.com/hc/en-us/articles/360040451373-Guide-to-auto-layout#absolute)


## Auto-Layout in Other Platforms

### iOS (SwiftUI & UIKit)

- **UIKit Auto Layout:** Uses constraints to define spatial relationships. Layouts adjust automatically to device orientation and size.
- **SwiftUI:** Uses HStack, VStack, ZStack, and Spacer for responsive arrangements.

**Apple Documentation:**
- [Auto Layout Guide](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/AutolayoutPG/index.html)
- [Layout | Apple Developer Documentation](https://developer.apple.com/documentation/appkit/layout?language=objc)

**Tips:**  
- Use Interface Builder for visual constraint editing.
- Use “Safe Area” guides for layouts that adapt to notches and rounded corners.


### Android (Jetpack Compose, XML, ConstraintLayout)

- **ConstraintLayout (XML):** Defines constraints (top, bottom, baseline, etc.) for flexible layouts with a flat view hierarchy. No need for nested view groups.
- **Jetpack Compose:** Uses Row, Column, Box, and ConstraintLayout composables to build layouts programmatically.

**Android Documentation:**
- [ConstraintLayout (XML) Guide](https://developer.android.com/develop/ui/views/layout/constraint-layout)
- [ConstraintLayout in Jetpack Compose](https://developer.android.com/develop/ui/compose/layouts/constraintlayout)

**Best Practice:**  
Use ConstraintLayout for complex, adaptive UIs and to avoid deep nesting.


### Web (CSS Flexbox, Grid)

- **Flexbox:** One-dimensional layout (row or column). Items grow/shrink to fit space.
- **CSS Grid:** Two-dimensional layout for rows and columns. Enables highly adaptive, responsive designs.

**MDN Documentation:**
- [Basic concepts of flexbox – MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout/Basic_concepts)
- [Relationship of grid layout to other layout methods – MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/Relationship_with_other_layout_methods)

**Example:**  
- Flexbox for navigation bars and toolbars.
- Grid for product listings and dashboards.


## Common Use Cases and Examples

### Buttons That Expand with Text

Set the button container to “Hug contents” with fixed padding, so the button always fits its label—no clipping or excessive whitespace.

### Responsive Lists and Menus

Use vertical Auto-Layout or a vertical stack (SwiftUI/Jetpack Compose) so items reflow and spacing remains consistent.

### Cards and Complex Components

Nest Auto-Layout frames for each region (header, content, actions) to maintain structure and flexibility.

### Notification Badges

Use “Ignore Auto-Layout” or absolute positioning for badges overlaying icons or buttons.

### Adaptive Webpages

Use CSS Grid or Flexbox to make content reflow for different screen sizes, keeping layouts fluid and responsive.


## Best Practices and Troubleshooting

### Best Practices

- Start with small components (e.g., buttons) before scaling up.
- Use nesting for modular, reusable designs.
- Apply consistent spacing and padding, ideally as variables or tokens.
- Document layout rules for clarity and future maintenance.
- Use keyboard shortcuts for efficiency.

### Troubleshooting

- **Elements Overlap or Don’t Resize:** Check resizing settings and ensure correct settings for parent/child.
- **Alignment Not Working:** Ensure there’s room for alignment; “hug” frames may limit visible alignment changes.
- **Too Many Nested Frames:** Simplify layout structure where possible.
- **Badge/Overlay Not Positioning:** Use “Ignore Auto-Layout.”
- **Spacing Off After Applying Auto-Layout:** Adjust padding and gap values manually.



## FAQ

**What’s the difference between Hug, Fill, and Fixed in Figma Auto-Layout?**  
- **Hug:** Container matches its children’s size.
- **Fill:** Child fills the parent’s available space.
- **Fixed:** Element stays the same size.

**Can I combine horizontal and vertical Auto-Layouts?**  
Yes, via nesting: e.g., vertical Auto-Layout for a card, horizontal for the card’s header.

**How do I make an element ignore Auto-Layout rules?**  
Use “Ignore Auto-Layout” (absolute positioning).

**Does Auto-Layout work for responsive design?**  
Yes, it’s designed for adaptive/responsive interfaces.

**Why does my Auto-Layout frame shrink/expand unexpectedly?**  
Figma sets initial padding based on content—adjust values in the right panel as needed.


## Further Resources

- [Figma Auto-Layout YouTube Tutorial](https://www.youtube.com/watch?v=1odqpkfkDL8)
- [Figma Help Center – Guide to auto layout](https://help.figma.com/hc/en-us/articles/360040451373-Guide-to-auto-layout)
- [Figma Handbook – Advanced Auto Layout (Design+Code)](https://designcode.io/figma-handbook-advanced-layout)
- [CSS Flexbox Guide (MDN)](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout/Basic_concepts)
- [CSS Grid Guide (MDN)](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/Relationship_with_other_layout_methods)
- [Apple Auto Layout Documentation](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/AutolayoutPG/index.html)
- [Android ConstraintLayout Guide](https://developer.android.com/develop/ui/views/layout/constraint-layout)
- [ConstraintLayout in Jetpack Compose](https://developer.android.com/develop/ui/compose/layouts/constraintlayout)


This glossary incorporates detailed, authoritative information for Auto-Layout across Figma, iOS, Android, and Web, with direct links to official documentation and advanced tutorials for deep learning and troubleshooting.
