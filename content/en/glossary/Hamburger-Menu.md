---
title: "Hamburger Menu"
translationKey: "hamburger-menu"
description: "A menu icon with three stacked lines that reveals hidden navigation options when clicked, commonly used on mobile apps and websites to save screen space."
keywords: ["hamburger menu", "UI/UX design", "mobile navigation", "progressive disclosure", "web accessibility"]
category: "General"
type: "glossary"
date: 2025-12-18
lastmod: 2025-12-18
draft: false
---

## What is a Hamburger Menu?

A hamburger menu is a graphical user interface (GUI) element represented by three stacked horizontal lines (the "hamburger icon"). When clicked or tapped, it reveals a hidden menu containing navigation options, settings, or additional features. In AI chatbots and automation platforms, the hamburger menu is frequently embedded within chat windows, providing access to persistent options—account settings, chat history, help, or bot switching—without overwhelming the primary conversation interface.

<strong>Why "hamburger"?</strong>The icon's three lines visually resemble a stylized hamburger: a patty between two buns. This metaphor is now near-universal for hidden navigation.

## Historical Origin

<strong>First Appearance:</strong>Created by designer Norm Cox in 1981 for the Xerox Star personal workstation to represent a list of options. The design was intentionally simple and memorable due to limited pixel space (16x16px or 13x13px).

<strong>Early Adoption:</strong>Used in Xerox Star and Windows 1.0 (1985), then faded from mainstream interfaces for decades.

<strong>Mobile Resurgence:</strong>The explosion of mobile apps in the late 2000s revived the hamburger menu. Twitter's 2008 mobile app and Apple's iOS used it to maximize screen space, followed by adoption in Facebook, Gmail, and Amazon apps.

<strong>Current Status:</strong>As recognizable as the search magnifying glass or gear icon for settings. Standard solution for mobile and responsive web navigation.

## Use Cases

<strong>Mobile Apps and Responsive Websites:</strong>Hide less-critical navigation on small screens, preserving visual space.

<strong>AI Chatbots and Automation:</strong>Chat interfaces use hamburger menus for user settings, chat history, bot switching, or help documentation.

<strong>Desktop Applications:</strong>Less common but sometimes used for secondary tools or preferences.

<strong>Feature-Rich Web Apps:</strong>Apps with many secondary options (Uber's payment settings, Gmail's folder structure) use hamburger menus to declutter core workflows.

<strong>Examples in AI Chatbots:</strong>- <strong>Chatbot Settings</strong>– Tools like Intercom or Drift place user preferences, notifications, resources inside hamburger menu
- <strong>Persistent Options</strong>– Language switching, privacy controls, feedback forms
- <strong>Multi-Bot Navigation</strong>– Enterprise dashboards allow swapping between bots or channels

## Key UX Concepts

<strong>Progressive Disclosure:</strong>Design principle where only the most relevant information is shown by default, with extra options revealed as needed. The hamburger menu is a classic example—main actions stay visible; secondary options available on-demand.

- <strong>Benefit</strong>– Reduces visual clutter and cognitive overload
- <strong>Drawback</strong>– Risks hiding important options, lowering discoverability

<strong>Interaction Cost:</strong>Time, effort, and number of actions users need to achieve a goal. Hamburger menus raise interaction cost because users must perform an extra tap or click to access features.

- <strong>High interaction cost</strong>– Users may be less engaged and slower to complete tasks
- <strong>Low interaction cost</strong>– Improves efficiency but can increase visible clutter

## Pros and Cons

<strong>Advantages:</strong>- <strong>Simplifies Interface</strong>– Creates cleaner, less cluttered interface
- <strong>Enhances Mobile Usability</strong>– Maximizes limited screen real estate
- <strong>Accommodates Many Links</strong>– Handles complex navigation structures
- <strong>Supports Progressive Disclosure</strong>– Keeps secondary features accessible but out of the way
- <strong>Ubiquitous Icon</strong>– Recognized by most users
- <strong>Facilitates Consistency</strong>– Unified navigation approach across platforms

<strong>Disadvantages:</strong>- <strong>Reduces Discoverability</strong>– Hidden navigation decreases visibility of important sections
- <strong>Slows Navigation</strong>– Requires extra clicks/taps, frustrating users needing quick access
- <strong>Can Overwhelm on Open</strong>– Large menus present too many options
- <strong>Less Familiar for Some</strong>– Not all demographics recognize the hamburger icon
- <strong>Not Always Appropriate</strong>– Poor fit for simple sites or immediate action scenarios
- <strong>Accessibility Barriers</strong>– Without proper labels and keyboard support, hinders users with disabilities

## Design Best Practices

<strong>Visual Design:</strong>- Use classic three-line icon—unadorned, equal length lines
- Place consistently (top-left for most languages; top-right for RTL or thumb-friendly layouts)
- Avoid unnecessary borders or embellishments
- Add "Menu" label for unfamiliar audiences
- Ensure clickability with hover states and cursor changes
- Provide adequate size and padding for easy tapping
- High contrast between icon and background
- Subtle animations (morphing to "X" on open) reinforce interactivity

<strong>UX Guidelines:</strong>- Do not hide core features; use for secondary or infrequent actions
- Consider hybrid navigation—combine visible tabs/bars with hamburger for lesser-used items
- Monitor analytics for overlooked links or features
- User test icon recognition and accessibility
- Avoid icon confusion—don't place similar icons nearby
- Ensure fast, smooth menu opening

<strong>Accessibility:</strong>- Use semantic HTML: `<button>` elements for menu trigger
- Add `aria-label="Menu"` or similar for screen readers
- Make menu accessible by keyboard (Tab to open, arrow keys for navigation)
- Provide visible focus states for all interactive elements
- Ensure sufficient color contrast and large touch targets

## Real-World Examples

<strong>Web and Mobile Applications:</strong>- <strong>Gmail (Android/iOS)</strong>– Hamburger menu in top-left reveals folders and account options
- <strong>Uber</strong>– Used for trip history, receipts, and settings
- <strong>Amazon Mobile</strong>– Gives access to secondary navigation and preferences

<strong>AI Chatbot Interfaces:</strong>- <strong>Enterprise Chatbot Widgets</strong>– Hamburger menu inside chat windows for profile, notification settings, chat history, support
- <strong>Customer Support Bots</strong>– Menu includes links to knowledge articles and escalation options
- <strong>Multi-bot Platforms</strong>– Menu enables switching between bots or channels

## Alternatives to Hamburger Menu

<strong>Tab Bars:</strong>Visible row of navigation options. Best for 3-5 core sections (Instagram, Facebook).

<strong>Bottom Navigation Bars:</strong>Mobile-friendly, keeps key actions within thumb's reach.

<strong>Visible Sidebars:</strong>For desktop or large screens; always-visible side menus.

<strong>Dropdown Menus:</strong>Hover or click triggers menu from top bar (desktop).

<strong>Floating Action Buttons (FAB):</strong>Prominent for a single primary action.

<strong>Comparison:</strong>| Pattern | Discoverability | Space Efficiency | Suitable For |
|---------|----------------|------------------|--------------|
| Hamburger Menu | Low | High | Mobile, Secondary Nav |
| Tab Bar | High | Moderate | Mobile, Core Nav |
| Bottom Bar | High | Moderate | Mobile, Frequent Nav |
| Sidebar | High | Low | Desktop, Large Screens |

## When to Use or Avoid

<strong>Use a hamburger menu when:</strong>- Space is limited (mobile-first designs)
- Navigation options exceed visible interface space
- Options are secondary or non-critical
- Consistency across devices is vital

<strong>Avoid or rethink when:</strong>- Critical features would be hidden
- Analytics show low engagement with hidden items
- Target users are unfamiliar with the icon
- The experience is already interaction-heavy
- The interface has space for visible navigation

## Implementation

<strong>Simple HTML/CSS Example:</strong>```html
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

**Key Points:**- Use `<button>` for semantics and keyboard navigation
- Add `aria-label` for screen readers
- Ensure sufficient touch area and visible focus states

**Tools and Resources:**- **No-code Builders**– Squarespace, Webnode, Site123, HubSpot CMS
- **Prototyping**– Justinmind Wireframe Tool
- **UI Libraries**– Material UI AppBar, Bootstrap Navbar

## References


1. Interaction Design Foundation. (n.d.). Hamburger Menu UX. Interaction Design Foundation.
2. Nielsen Norman Group (NNG). (n.d.). The Hamburger-Menu Icon Today. Nielsen Norman Group.
3. Justinmind. (n.d.). Guide to Hamburger Menu Design. Justinmind.
4. HubSpot. (n.d.). What is a Hamburger Button?. HubSpot Blog.
5. TechTarget. (n.d.). Hamburger Icon Definition. TechTarget.
6. Nielsen Norman Group (NNG). (n.d.). Hamburger Menu Icon Update. YouTube.
7. Nielsen Norman Group (NNG). (n.d.). Hidden Navigation Hurts UX Metrics. Nielsen Norman Group.
8. Justinmind. (n.d.). Navigation Design Patterns. Justinmind Blog.
9. Netwizard. (n.d.). Hamburger Menu Pros and Cons. Netwizard Design.
10. UserWay. (n.d.). Website Navigation Best Practices. UserWay.
11. UXDesign.cc. (n.d.). Create an Accessible Hamburger Menu. UXDesign.cc.
12. Medium. (n.d.). A Conversation with Norm Cox. Medium.
13. Interaction Design Foundation. (n.d.). Progressive Disclosure. Interaction Design Foundation.
14. Nielsen Norman Group (NNG). (n.d.). Interaction Cost Definition. Nielsen Norman Group.
15. CodePen. Hamburger Menu Example. URL: https://codepen.io/Danilo06/pen/PoNNvGm
16. Squarespace. Website Builder Platform. URL: https://www.squarespace.com/
17. HubSpot CMS. Content Management System. URL: https://www.hubspot.com/products/cms
18. Material UI AppBar. UI Component Library. URL: https://mui.com/components/app-bar/
19. Bootstrap Navbar. UI Component Library. URL: https://getbootstrap.com/docs/5.0/components/navbar/
