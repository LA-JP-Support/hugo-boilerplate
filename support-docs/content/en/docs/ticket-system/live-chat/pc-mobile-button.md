---
title: "Displaying Different Chat Buttons for PC/Mobile Sites"
date: 2026-01-30
lastmod: 2026-01-30
draft: false
translationKey: "pc-mobile-button"
description: "You can switch the display of chat buttons between PC sites and mobile sites."
keywords: ["chat", "mobile", "about", "LiveAgent", "live chat"]
category: "ticket-system/live-chat"
---
## Chat Button Display Settings Overview

Chat buttons can be configured differently for PC sites and mobile sites. This explains methods for achieving device-optimized display.

## LiveAgent Chat Button Display Settings

### Mobile Environment Appearance Settings

In "Settings" - "Chat" - "Chat Buttons" - (click the relevant button name) "Online Button" page, you can customize the display for mobile environments.

#### Display Size Adjustment Examples
- "No change"
- "Scale down"
- Text portion only display

#### Design Customization
- Use of original images
- Adjustable to match site design
  - Design
  - Display method
  - Position
  - Size

## Method for Displaying Different Buttons on PC/Mobile Sites

### Implementation Steps

1. Set up buttons in LiveAgent
   - PC chat button
   - Mobile chat button

2. Paste source code into website

### Display Control with CSS

#### Settings for Smartphone Size
- Hide PC chat button
- Display mobile chat button

#### Settings for Tablet/PC Size
- Display PC chat button
- Hide mobile chat button

### Implementation Code Examples

#### Class Specification in HTML
```html
<div class="livechat_pc">
  <!-- PC chat button source code -->
</div>

<div class="livechat_mobile">
  <!-- Mobile chat button source code -->
</div>
```

#### Display Control with CSS
```css
@media only screen and (max-width: 679px) {
  .livechat_pc { display: none; }
  .livechat_mobile { display: block; }
}

@media only screen and (min-width: 679px) {
  .livechat_pc { display: block; }
  .livechat_mobile { display: none; }
}
```