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

<strong>Analogy:</strong>Imagine a bookshelf that automatically shifts and spaces its books every time you add or remove one. Auto-Layout does the same for UI elements: no matter how many you insert or remove, your design stays organized and visually balanced.

<strong>Figma Official Guide:</strong>[Guide to auto layout – Figma Help Center](https://help.figma.com/hc/en-us/articles/360040451373-Guide-to-auto-layout)


## Why Use Auto-Layout?

<strong>Key Benefits:</strong>- <strong>Efficiency:</strong>Significantly reduces manual resizing and repositioning. Update content or components once, and the layout adapts everywhere.
- <strong>Responsive Design:</strong>Elements adapt to various screen sizes, making it ideal for multi-device design workflows.
- <strong>Consistency:</strong>Maintains uniform spacing, alignment, and proportions across entire projects.
- <strong>Collaboration:</strong>Designers and developers rely on the same set of rules, streamlining the handoff and minimizing miscommunication.

<strong>Use Cases:</strong>- Buttons that grow or shrink to fit their text  
- Dynamic lists or menus  
- Product galleries and dashboards  
- Adaptive website layouts

<strong>Further Reading:</strong>- [A Guide to Auto Layout: Best Practices, Tips & Tricks | Figma (YouTube)](https://www.youtube.com/watch?v=1odqpkfkDL8)
- [Figma Handbook: Advanced Auto Layout by Design+Code](https://designcode.io/figma-handbook-advanced-layout)


## How Auto-Layout Works

### Core Concepts

Auto-Layout uses layout rules, or <strong>constraints</strong>, to govern the spatial relationships of UI elements. Here’s how it operates:

- <strong>Constraints:</strong>Define rules between elements, e.g., "Button is always 16px below the label."
- <strong>Direction:</strong>The axis along which elements are arranged—horizontal, vertical, wrap, or grid.
- <strong>Resizing:</strong>Determines if containers and children hug content, fill space, or are fixed.
- <strong>Spacing & Padding:</strong>Sets gaps between elements and space inside containers.
- <strong>Alignment:</strong>Dictates position within the container—center, left, right, etc.
- <strong>Nesting:</strong>Place Auto-Layout frames within each other for sophisticated structures.

<strong>Example:</strong>A button whose width "hugs" its label will automatically resize as the text changes, maintaining consistent padding.

<strong>Official Documentation:</strong>- [Figma: Guide to auto layout](https://help.figma.com/hc/en-us/articles/360040451373-Guide-to-auto-layout)
- [Understanding Auto Layout – Apple Developer](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/AutolayoutPG/index.html#//apple_ref/doc/uid/TP40010853-CH7-SW1)

### Key Features

- <strong>Automatic Arrangement:</strong>No pixel-by-pixel adjustments; structure is handled automatically.
- <strong>Content-Driven Resizing:</strong>Elements grow/shrink to fit content or available space.
- <strong>Flexible Alignment:</strong>Align elements (left, center, right, top, bottom) or distribute them evenly.
- <strong>Nesting:</strong>Create complex layouts by combining multiple Auto-Layouts.
- <strong>Absolute Positioning:</strong>Exclude specific children from the Auto-Layout rules when needed.


## Platform Specifics: Auto-Layout in Figma

Figma’s Auto-Layout is one of the most powerful tools for interface design and prototyping.

### Adding and Removing Auto-Layout

- <strong>Add:</strong>Select layers → Press `Shift + A` or click <strong>Add auto layout</strong>in the sidebar.
- <strong>Remove:</strong>Select frame → Press `Option + Shift + A` (Mac) or `Alt + Shift + A` (Windows) or right-click and select <strong>Remove auto layout</strong>.

If you select objects not already in a frame, Figma creates a new frame with Auto-Layout applied.

[Official Figma Instructions](https://help.figma.com/hc/en-us/articles/360040451373-Guide-to-auto-layout)


### Direction: Horizontal, Vertical, Wrap, and Grid

- <strong>Horizontal:</strong>Arranges children in a row.
- <strong>Vertical:</strong>Arranges elements in a column.
- <strong>Wrap:</strong>Allows elements to continue onto new lines/columns when space is limited.
- <strong>Grid (Beta):</strong>Arranges elements in both rows and columns.

<strong>How to Switch:</strong>Use the Direction controls in Figma’s right panel.

<strong>Learn More:</strong>[Auto layout flow in Figma](https://help.figma.com/hc/en-us/articles/360040451373-Guide-to-auto-layout#flow)


### Spacing, Padding & Gaps

- <strong>Gap/Spacing:</strong>The space between items; set as a fixed value or “Auto.”
- <strong>Padding:</strong>The space inside the frame between the border and its children; can be set uniformly or for each side.

<strong>Adjustment:</strong>Set values in the right sidebar or drag handles on the canvas.

<strong>Example:</strong>A button with 16px horizontal and 8px vertical padding.

<strong>Deep Dive:</strong>[Advanced spacing and alignment – Figma Handbook](https://designcode.io/figma-handbook-advanced-layout)


### Resizing Options: Hug, Fill, Fixed, Min/Max

- <strong>Hug Contents:</strong>Frame resizes to fit its children.
- <strong>Fill Container:</strong>Child expands to fill available space in its parent.
- <strong>Fixed Size:</strong>Dimensions remain constant, regardless of content or parent size.
- <strong>Min/Max Constraints:</strong>Set the minimum/maximum size an element can shrink or grow to.

<strong>How to Set:</strong>Use the Width/Height dropdowns in Figma’s right panel.

<strong>Example:</strong>A button with width set to "Hug" and a minimum width of 100px prevents it from becoming too small.

[Resizing and constraints in Figma](https://help.figma.com/hc/en-us/articles/360040451373-Guide-to-auto-layout#resize)


### Nesting Auto-Layouts

<strong>Nesting</strong>allows one Auto-Layout frame inside another for modular and complex designs.

<strong>Example:</strong>A card component with vertical Auto-Layout, a header row (horizontal), and a content area (vertical).

<strong>Shortcut:</strong>`Ctrl + Shift + A` (Mac) or `Ctrl + Alt + Shift + A` (Windows) for “Suggest Auto-Layout.”

[Building complex layouts – Figma Help Center](https://help.figma.com/hc/en-us/articles/360040451373-Guide-to-auto-layout#nest)


### Alignment and Distribution

- <strong>Alignment:</strong>Controls position within the container.
- <strong>Distribution:</strong>Evenly spaces elements along the main axis.

<strong>How to Set:</strong>Use the alignment controls (the “gram cracker” icon) in the sidebar.

<strong>Troubleshooting:</strong>Alignment changes only have an effect when there’s space to align within; “hug” frames may show no visible change.

[Alignment and distribution in Figma](https://help.figma.com/hc/en-us/articles/360040451373-Guide-to-auto-layout#align)


### Ignoring Auto-Layout (Absolute Positioning)

<strong>Absolute Positioning</strong>(now called "Ignore Auto-Layout") lets you exclude an element from the layout flow for overlays like badges.

<strong>How to Use:</strong>Select the element → Design panel → Click “Ignore auto layout” or drag it while holding `Ctrl`.

<strong>Example:</strong>A notification badge positioned on the corner of an icon.

[Absolute positioning in Figma](https://help.figma.com/hc/en-us/articles/360040451373-Guide-to-auto-layout#absolute)


## Auto-Layout in Other Platforms

### iOS (SwiftUI & UIKit)

- <strong>UIKit Auto Layout:</strong>Uses constraints to define spatial relationships. Layouts adjust automatically to device orientation and size.
- <strong>SwiftUI:</strong>Uses HStack, VStack, ZStack, and Spacer for responsive arrangements.

<strong>Apple Documentation:</strong>- [Auto Layout Guide](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/AutolayoutPG/index.html)
- [Layout | Apple Developer Documentation](https://developer.apple.com/documentation/appkit/layout?language=objc)

<strong>Tips:</strong>- Use Interface Builder for visual constraint editing.
- Use “Safe Area” guides for layouts that adapt to notches and rounded corners.


### Android (Jetpack Compose, XML, ConstraintLayout)

- <strong>ConstraintLayout (XML):</strong>Defines constraints (top, bottom, baseline, etc.) for flexible layouts with a flat view hierarchy. No need for nested view groups.
- <strong>Jetpack Compose:</strong>Uses Row, Column, Box, and ConstraintLayout composables to build layouts programmatically.

<strong>Android Documentation:</strong>- [ConstraintLayout (XML) Guide](https://developer.android.com/develop/ui/views/layout/constraint-layout)
- [ConstraintLayout in Jetpack Compose](https://developer.android.com/develop/ui/compose/layouts/constraintlayout)

<strong>Best Practice:</strong>Use ConstraintLayout for complex, adaptive UIs and to avoid deep nesting.


### Web (CSS Flexbox, Grid)

- <strong>Flexbox:</strong>One-dimensional layout (row or column). Items grow/shrink to fit space.
- <strong>CSS Grid:</strong>Two-dimensional layout for rows and columns. Enables highly adaptive, responsive designs.

<strong>MDN Documentation:</strong>- [Basic concepts of flexbox – MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout/Basic_concepts)
- [Relationship of grid layout to other layout methods – MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/Relationship_with_other_layout_methods)

<strong>Example:</strong>- Flexbox for navigation bars and toolbars.
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

- <strong>Elements Overlap or Don’t Resize:</strong>Check resizing settings and ensure correct settings for parent/child.
- <strong>Alignment Not Working:</strong>Ensure there’s room for alignment; “hug” frames may limit visible alignment changes.
- <strong>Too Many Nested Frames:</strong>Simplify layout structure where possible.
- <strong>Badge/Overlay Not Positioning:</strong>Use “Ignore Auto-Layout.”
- <strong>Spacing Off After Applying Auto-Layout:</strong>Adjust padding and gap values manually.



## FAQ

<strong>What’s the difference between Hug, Fill, and Fixed in Figma Auto-Layout?</strong>- <strong>Hug:</strong>Container matches its children’s size.
- <strong>Fill:</strong>Child fills the parent’s available space.
- <strong>Fixed:</strong>Element stays the same size.

<strong>Can I combine horizontal and vertical Auto-Layouts?</strong>Yes, via nesting: e.g., vertical Auto-Layout for a card, horizontal for the card’s header.

<strong>How do I make an element ignore Auto-Layout rules?</strong>Use “Ignore Auto-Layout” (absolute positioning).

<strong>Does Auto-Layout work for responsive design?</strong>Yes, it’s designed for adaptive/responsive interfaces.

<strong>Why does my Auto-Layout frame shrink/expand unexpectedly?</strong>Figma sets initial padding based on content—adjust values in the right panel as needed.


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
