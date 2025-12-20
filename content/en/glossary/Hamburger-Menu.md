---
title: "Hamburger Menu"
translationKey: "hamburger-menu"
description: "A menu icon with three stacked lines that opens hidden navigation options when clicked, commonly used on mobile apps and websites to save screen space."
keywords: ["hamburger menu", "UI/UX design", "mobile navigation", "progressive disclosure", "web accessibility"]
category: "General"
type: "glossary"
date: 2025-12-18
lastmod: 2025-12-18
draft: false
---

## What is a Hamburger Menu?

A hamburger menu is a graphical user interface (GUI) element represented by three stacked horizontal lines (the "hamburger icon"). When clicked or tapped, it reveals a hidden menu containing navigation options, settings, or additional features. In AI chatbots and automation platforms, the hamburger menu is frequently embedded within chat windows, providing access to persistent options—account settings, chat history, help, or bot switching—without overwhelming the primary conversation interface.

**Why "hamburger"?**  
The icon's three lines visually resemble a stylized hamburger: a patty between two buns. This metaphor is now near-universal for hidden navigation.

## Historical Origin

**First Appearance:**  
Created by designer Norm Cox in 1981 for the Xerox Star personal workstation to represent a list of options. The design was intentionally simple and memorable due to limited pixel space (16x16px or 13x13px).

**Early Adoption:**  
Used in Xerox Star and Windows 1.0 (1985), then faded from mainstream interfaces for decades.

**Mobile Resurgence:**  
The explosion of mobile apps in the late 2000s revived the hamburger menu. Twitter's 2008 mobile app and Apple's iOS used it to maximize screen space, followed by adoption in Facebook, Gmail, and Amazon apps.

**Current Status:**  
As recognizable as the search magnifying glass or gear icon for settings. Standard solution for mobile and responsive web navigation.

## Use Cases

**Mobile Apps and Responsive Websites:**  
Hide less-critical navigation on small screens, preserving visual space.

**AI Chatbots and Automation:**  
Chat interfaces use hamburger menus for user settings, chat history, bot switching, or help documentation.

**Desktop Applications:**  
Less common but sometimes used for secondary tools or preferences.

**Feature-Rich Web Apps:**  
Apps with many secondary options (Uber's payment settings, Gmail's folder structure) use hamburger menus to declutter core workflows.

**Examples in AI Chatbots:**

- **Chatbot Settings** – Tools like Intercom or Drift place user preferences, notifications, resources inside hamburger menu
- **Persistent Options** – Language switching, privacy controls, feedback forms
- **Multi-Bot Navigation** – Enterprise dashboards allow swapping between bots or channels

## Key UX Concepts

**Progressive Disclosure:**  
Design principle where only the most relevant information is shown by default, with extra options revealed as needed. The hamburger menu is a classic example—main actions stay visible; secondary options available on-demand.

- **Benefit** – Reduces visual clutter and cognitive overload
- **Drawback** – Risks hiding important options, lowering discoverability

**Interaction Cost:**  
Time, effort, and number of actions users need to achieve a goal. Hamburger menus raise interaction cost because users must perform an extra tap or click to access features.

- **High interaction cost** – Users may be less engaged and slower to complete tasks
- **Low interaction cost** – Improves efficiency but can increase visible clutter

## Pros and Cons

**Advantages:**

- **Simplifies Interface** – Creates cleaner, less cluttered interface
- **Enhances Mobile Usability** – Maximizes limited screen real estate
- **Accommodates Many Links** – Handles complex navigation structures
- **Supports Progressive Disclosure** – Keeps secondary features accessible but out of the way
- **Ubiquitous Icon** – Recognized by most users
- **Facilitates Consistency** – Unified navigation approach across platforms

**Disadvantages:**

- **Reduces Discoverability** – Hidden navigation decreases visibility of important sections
- **Slows Navigation** – Requires extra clicks/taps, frustrating users needing quick access
- **Can Overwhelm on Open** – Large menus present too many options
- **Less Familiar for Some** – Not all demographics recognize the hamburger icon
- **Not Always Appropriate** – Poor fit for simple sites or immediate action scenarios
- **Accessibility Barriers** – Without proper labels and keyboard support, hinders users with disabilities

## Design Best Practices

**Visual Design:**

- Use classic three-line icon—unadorned, equal length lines
- Place consistently (top-left for most languages; top-right for RTL or thumb-friendly layouts)
- Avoid unnecessary borders or embellishments
- Add "Menu" label for unfamiliar audiences
- Ensure clickability with hover states and cursor changes
- Provide adequate size and padding for easy tapping
- High contrast between icon and background
- Subtle animations (morphing to "X" on open) reinforce interactivity

**UX Guidelines:**

- Do not hide core features; use for secondary or infrequent actions
- Consider hybrid navigation—combine visible tabs/bars with hamburger for lesser-used items
- Monitor analytics for overlooked links or features
- User test icon recognition and accessibility
- Avoid icon confusion—don't place similar icons nearby
- Ensure fast, smooth menu opening

**Accessibility:**

- Use semantic HTML: `<button>` elements for menu trigger
- Add `aria-label="Menu"` or similar for screen readers
- Make menu accessible by keyboard (Tab to open, arrow keys for navigation)
- Provide visible focus states for all interactive elements
- Ensure sufficient color contrast and large touch targets

## Real-World Examples

**Web and Mobile Applications:**

- **Gmail (Android/iOS)** – Hamburger menu in top-left reveals folders and account options
- **Uber** – Used for trip history, receipts, and settings
- **Amazon Mobile** – Gives access to secondary navigation and preferences

**AI Chatbot Interfaces:**

- **Enterprise Chatbot Widgets** – Hamburger menu inside chat windows for profile, notification settings, chat history, support
- **Customer Support Bots** – Menu includes links to knowledge articles and escalation options
- **Multi-bot Platforms** – Menu enables switching between bots or channels

## Alternatives to Hamburger Menu

**Tab Bars:**  
Visible row of navigation options. Best for 3-5 core sections (Instagram, Facebook).

**Bottom Navigation Bars:**  
Mobile-friendly, keeps key actions within thumb's reach.

**Visible Sidebars:**  
For desktop or large screens; always-visible side menus.

**Dropdown Menus:**  
Hover or click triggers menu from top bar (desktop).

**Floating Action Buttons (FAB):**  
Prominent for a single primary action.

**Comparison:**

| Pattern | Discoverability | Space Efficiency | Suitable For |
|---------|----------------|------------------|--------------|
| Hamburger Menu | Low | High | Mobile, Secondary Nav |
| Tab Bar | High | Moderate | Mobile, Core Nav |
| Bottom Bar | High | Moderate | Mobile, Frequent Nav |
| Sidebar | High | Low | Desktop, Large Screens |

## When to Use or Avoid

**Use a hamburger menu when:**

- Space is limited (mobile-first designs)
- Navigation options exceed visible interface space
- Options are secondary or non-critical
- Consistency across devices is vital

**Avoid or rethink when:**

- Critical features would be hidden
- Analytics show low engagement with hidden items
- Target users are unfamiliar with the icon
- The experience is already interaction-heavy
- The interface has space for visible navigation

## Implementation

**Simple HTML/CSS Example:**

```html
<button aria-label="Open menu" class="hamburger-menu" tabindex="0">
  <span></span>
  <span></span>
  <span></span>
</button>
```

```css
.hamburger-menu span {
  display: block;
  width: 35px;
  height: 5px;
  background-color: #333;
  margin: 6px 0;
}
```

**Key Points:**

- Use `<button>` for semantics and keyboard navigation
- Add `aria-label` for screen readers
- Ensure sufficient touch area and visible focus states

**Tools and Resources:**

- **No-code Builders** – Squarespace, Webnode, Site123, HubSpot CMS
- **Prototyping** – Justinmind Wireframe Tool
- **UI Libraries** – Material UI AppBar, Bootstrap Navbar

## References

- [Interaction Design Foundation: Hamburger Menu UX](https://www.interaction-design.org/literature/article/hamburger-menu-ux)
- [NNG: The Hamburger-Menu Icon Today](https://www.nngroup.com/articles/hamburger-menu-icon-recognizability/)
- [Justinmind: Guide to Hamburger Menu Design](https://www.justinmind.com/ui-design/hamburger-menu)
- [HubSpot: What is a Hamburger Button?](https://blog.hubspot.com/website/hamburger-button)
- [TechTarget: Hamburger Icon Definition](https://www.techtarget.com/whatis/definition/hamburger-icon-slide-drawer-navigation)
- [NNG YouTube: Hamburger Menu Icon Update](https://www.youtube.com/watch?v=1au4Gff9cSo)
- [NNG: Hidden Navigation Hurts UX Metrics](https://www.nngroup.com/articles/hamburger-menus/)
- [Justinmind: Navigation Design Patterns](https://www.justinmind.com/blog/navigation-design-almost-everything-you-need-to-know/)
- [Netwizard: Hamburger Menu Pros and Cons](https://netwizarddesign.com.au/the-three-line-menu-option-called-hamburger-menu-what-are-the-pros-and-cons/)
- [UserWay: Website Navigation Best Practices](https://userway.org/blog/website-navigation/)
- [UXDesign.cc: Create an Accessible Hamburger Menu](https://uxdesign.cc/create-an-accessible-hamburger-menu-869b0301cfd7)
- [Medium: A Conversation with Norm Cox](https://medium.com/readme-mic/a-conversation-with-norm-cox-creator-of-the-hamburger-menu-c913daea5f9e)
- [Interaction Design Foundation: Progressive Disclosure](https://www.interaction-design.org/literature/topics/progressive-disclosure)
- [NNG: Interaction Cost Definition](https://www.nngroup.com/articles/interaction-cost-definition/)
- [CodePen Example](https://codepen.io/Danilo06/pen/PoNNvGm)
- [Squarespace](https://www.squarespace.com/)
- [HubSpot CMS](https://www.hubspot.com/products/cms)
- [Material UI AppBar](https://mui.com/components/app-bar/)
- [Bootstrap Navbar](https://getbootstrap.com/docs/5.0/components/navbar/)
