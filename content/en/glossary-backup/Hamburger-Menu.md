---
title: "Hamburger Menu"
translationKey: "hamburger-menu"
description: "A hamburger menu is a GUI element with three stacked lines that reveals a hidden navigation menu when clicked. Essential for mobile and responsive web design."
keywords: ["hamburger menu", "UI/UX design", "mobile navigation", "progressive disclosure", "web accessibility"]
category: "General"
type: "glossary"
date: 2025-12-05
lastmod: 2025-12-05
draft: false
---
## What is a Hamburger Menu?

A <strong>hamburger menu</strong>is a graphical user interface (GUI) element, most often represented by three stacked horizontal lines (the "hamburger icon"). When clicked or tapped, it reveals a hidden menu containing navigation options, settings, or additional features.

In <strong>AI chatbots and automation platforms</strong>, the hamburger menu is frequently embedded within the chat window, providing access to persistent options—such as account settings, chat history, help, or switching between bots—without overwhelming the primary conversation interface.

<strong>Why the name?</strong>The icon’s three lines visually resemble a stylized hamburger: a patty between two buns. This metaphor is now near-universal for hidden navigation.

*Further Reading: [Interaction Design Foundation: Hamburger Menu Guide](https://www.interaction-design.org/literature/article/hamburger-menu-ux)*

## Historical Origin and Evolution

- <strong>First Appearance:</strong>The hamburger icon was created by designer Norm Cox in 1981 for the Xerox Star personal workstation to represent a list of options. Its design was intentionally simple and memorable due to limited pixel space (16x16px or 13x13px). [Read Cox’s interview](https://medium.com/readme-mic/a-conversation-with-norm-cox-creator-of-the-hamburger-menu-c913daea5f9e) and see [Interaction Design Foundation’s history](https://www.interaction-design.org/literature/article/hamburger-menu-ux).

- <strong>Early Adoption:</strong>After its use in Xerox Star and Windows 1.0 (1985), the hamburger menu faded from mainstream interfaces for decades.

- <strong>Resurgence in Mobile:</strong>The explosion of mobile apps in the late 2000s revived the hamburger menu. Twitter’s 2008 mobile app and Apple’s iOS used it to maximize screen space, followed by adoption in apps from Facebook, Gmail, and Amazon.

- <strong>Current Status:</strong>The hamburger menu is as recognizable as the search magnifying glass or gear icon for settings. It is a standard solution for mobile and responsive web navigation.

*Visual timeline: [Justinmind’s illustrated history](https://www.justinmind.com/ui-design/hamburger-menu), [NNG’s analysis](https://www.nngroup.com/articles/hamburger-menu-icon-recognizability/).*

## How and Where Hamburger Menus Are Used

### Typical Use Cases

- <strong>Mobile Apps & Responsive Websites:</strong>Hamburger menus are used to hide less-critical navigation on small screens, preserving visual space.

- <strong>AI Chatbots and Automation:</strong>In chat interfaces, the hamburger menu often contains user settings, chat history, bot switching, or help documentation.

- <strong>Desktop Applications:</strong>Less common but sometimes used for secondary tools or preferences.

- <strong>Feature-Rich Web Apps:</strong>Apps with many secondary options (e.g., Uber’s payment settings, Gmail’s folder structure) use hamburger menus to declutter core workflows.

*Source: [Interaction Design Foundation](https://www.interaction-design.org/literature/article/hamburger-menu-ux)*

### Examples in AI Chatbots & Automation

- <strong>Chatbot Settings:</strong>Tools like Intercom or Drift place user preferences, notifications, and resources inside the hamburger menu within the chat widget.

- <strong>Persistent Options:</strong>Language switching, privacy controls, or feedback forms are often accessed via the hamburger menu.

- <strong>Multi-Bot Navigation:</strong>On enterprise dashboards, users can swap between bots or channels using the hamburger menu.

## Key UX Concepts: Progressive Disclosure & Interaction Cost

### Progressive Disclosure

<strong>Progressive disclosure</strong>is a design principle where only the most relevant information is shown by default, with extra options revealed as needed. The hamburger menu is a classic example—main actions stay visible; secondary options are available on-demand.

- <strong>Benefit:</strong>Reduces visual clutter and cognitive overload, especially on mobile.
- <strong>Drawback:</strong>Risks hiding important options, which can lower discoverability.

*Deep dive: [Interaction Design Foundation: Progressive Disclosure](https://www.interaction-design.org/literature/topics/progressive-disclosure)*

### Interaction Cost

<strong>Interaction cost</strong>is the time, effort, and number of actions users need to achieve a goal. Hamburger menus raise interaction cost because users must perform an extra tap or click to access features.

- <strong>High interaction cost:</strong>Users may be less engaged and slower to complete tasks.
- <strong>Low interaction cost:</strong>Improves efficiency but can increase visible clutter.

*Further reading: [NNG: Interaction Cost Definition](https://www.nngroup.com/articles/interaction-cost-definition/)*

## Pros and Cons of Hamburger Menus

### Pros

- <strong>Simplifies the Interface:</strong>Hides navigation options to create a cleaner, less cluttered interface. Especially valuable in minimalist and mobile designs.
- <strong>Enhances Mobile Usability:</strong>Maximizes limited screen real estate and keeps actions accessible with a tap.
- <strong>Accommodates Many Links:</strong>Handles complex navigation structures without overwhelming users.
- <strong>Supports Progressive Disclosure:</strong>Keeps secondary features accessible but out of the way.
- <strong>Ubiquitous Icon:</strong>Recognized by most users, making it a reliable mental model.
- <strong>Facilitates Consistency:</strong>Offers a unified navigation approach across multiple platforms.

*Source: [Interaction Design Foundation](https://www.interaction-design.org/literature/article/hamburger-menu-ux)*

### Cons

- <strong>Reduces Discoverability:</strong>Hidden navigation decreases visibility of important sections and features.
- <strong>Slows Navigation:</strong>Requires extra clicks/taps, which can frustrate users needing quick access.
- <strong>Overwhelms on Open:</strong>Large menus can present too many options, overwhelming users.
- <strong>Less Familiar for Some Users:</strong>Not all demographics recognize the hamburger icon; older or less tech-savvy users may struggle.
- <strong>Not Always Appropriate:</strong>Poor fit for simple sites or scenarios requiring immediate action.
- <strong>Accessibility Barriers:</strong>If not implemented with proper labels and keyboard support, can hinder users with disabilities.

## Design Principles and Best Practices

### Visual Design Guidelines

- Use the classic three-line icon—unadorned, of equal length.
- Place consistently (top-left for most languages; top-right for RTL or thumb-friendly layouts).
- Avoid unnecessary borders or embellishments.
- Add a “Menu” label for unfamiliar audiences or unique contexts.
- Ensure clickability: use hover states and cursor changes.
- Provide adequate size and padding for easy tapping.
- High contrast between icon and background.
- Subtle animations (e.g., morphing to “X” on open) reinforce interactivity.

*Guidance: [NNG: Hamburger Icon Best Practices](https://www.nngroup.com/articles/hamburger-menu-icon-recognizability/), [Justinmind: Hamburger Menu Design Guide](https://www.justinmind.com/ui-design/hamburger-menu)*

### UX Guidelines

- Do not hide core features; use for secondary or infrequent actions.
- Consider hybrid navigation—combine visible tabs/bars with hamburger for lesser-used items.
- Monitor analytics for overlooked links or features.
- User test icon recognition and accessibility.
- Avoid icon confusion—don’t place similar icons nearby.
- Ensure fast, smooth menu opening.

### Accessibility Considerations

- Use semantic HTML: `<button>` elements for the menu trigger.
- Add `aria-label="Menu"` or similar for screen readers.
- Make menu accessible by keyboard (Tab to open, arrow keys for navigation).
- Provide visible focus states for all interactive elements.
- Ensure sufficient color contrast and large touch targets.

*Accessibility: [UXDesign.cc: Create an Accessible Hamburger Menu](https://uxdesign.cc/create-an-accessible-hamburger-menu-869b0301cfd7), [UserWay: Accessibility Navigation Best Practices](https://userway.org/blog/website-navigation/)*

## Real-World Examples

### Web and Mobile Applications

- <strong>Gmail (Android/iOS):</strong>Hamburger menu in the top-left reveals folders and account options.  
  [Gmail on Google Play](https://play.google.com/store/apps/details?id=com.google.android.gm)
- <strong>Uber:</strong>Hamburger menu is used for trip history, receipts, and settings.
- <strong>Amazon Mobile:</strong>Hamburger menu gives access to secondary navigation and preferences.
- <strong>Pipcorn:</strong>Mobile hamburger menu triggers a fold-out navigation panel.  
  [Pipsnacks.com](https://www.pipsnacks.com/)

### AI Chatbot Interfaces

- <strong>Enterprise Chatbot Widgets:</strong>Hamburger menu inside chat windows for profile, notification settings, chat history, and support.
- <strong>Customer Support Bots:</strong>Menu includes links to knowledge articles and escalation options.
- <strong>Multi-bot Platforms:</strong>Menu enables switching between bots or channels.

*Quoting Netwizard: “The hamburger menu is a great place for navigational buttons that don’t directly serve the main goal of your web page.” ([Netwizard Design](https://netwizarddesign.com.au/the-three-line-menu-option-called-hamburger-menu-what-are-the-pros-and-cons/))*

## Alternatives to the Hamburger Menu

Navigation patterns to consider instead of, or alongside, hamburger menus:

- <strong>Tab Bars:</strong>Visible row of navigation options. Best for 3-5 core sections (Instagram, Facebook).
- <strong>Bottom Navigation Bars:</strong>Mobile-friendly, keeps key actions within thumb’s reach.
- <strong>Visible Sidebars:</strong>For desktop or large screens; always-visible side menus.
- <strong>Dropdown Menus:</strong>Hover or click triggers a menu from the top bar (desktop).
- <strong>Floating Action Buttons (FAB):</strong>Prominent for a single primary action.

### Comparisons and When to Use Which Pattern

| Pattern        | Discoverability | Space Efficiency | Suitable For         |
| -------------- | -------------- | --------------- | -------------------- |
| Hamburger Menu | Low            | High            | Mobile, Secondary Nav|
| Tab Bar        | High           | Moderate        | Mobile, Core Nav     |
| Bottom Bar     | High           | Moderate        | Mobile, Frequent Nav |
| Sidebar        | High           | Low             | Desktop, Large Screens|

Choose the model that matches your users’ needs and the importance of the options you offer.

*Comparisons: [Justinmind: Navigation Patterns](https://www.justinmind.com/blog/navigation-design-almost-everything-you-need-to-know/)*

## When to Use or Avoid Hamburger Menus

<strong>Use a hamburger menu when:</strong>- Space is limited (mobile-first designs).
- Navigation options exceed visible interface space.
- Options are secondary or non-critical.
- Consistency across devices is vital.

<strong>Avoid or rethink the hamburger menu when:</strong>- Critical features would be hidden.
- Analytics show low engagement with hidden items.
- Target users are unfamiliar with the icon.
- The experience is already interaction-heavy.
- The interface has space for visible navigation.

*Details: [Interaction Design Foundation](https://www.interaction-design.org/literature/article/hamburger-menu-ux)*

## Implementation Notes & Practical Tips

### Simple Hamburger Menu in HTML/CSS

<strong>Static Icon Example:</strong>```html
<div class="hamburger-menu">
  <div></div>
  <div></div>
  <div></div>
</div>
```

```css
.hamburger-menu div {
  width: 35px;
  height: 5px;
  background-color: #333;
  margin: 6px 0;
}
```

**Accessible, Interactive Example:**```html
<button aria-label="Open menu" class="hamburger-menu" tabindex="0">
  <span></span>
  <span></span>
  <span></span>
</button>
```

- Use `<button>` for semantics and keyboard navigation.
- Add `aria-label` for screen readers.
- Ensure sufficient touch area and visible focus states.

*Demo: [CodePen Example](https://codepen.io/Danilo06/pen/PoNNvGm), [UXDesign: Accessible Hamburger Menu](https://uxdesign.cc/create-an-accessible-hamburger-menu-869b0301cfd7)*

### Tools & Resources

- <strong>No-code Builders:</strong>[Squarespace](https://www.squarespace.com/), [Webnode](https://us.webnode.com/), [Site123](https://www.site123.com/), [HubSpot CMS](https://www.hubspot.com/products/cms)
- <strong>Prototyping:</strong>[Justinmind Wireframe Tool](https://www.justinmind.com/free-wireframe-tool)
- <strong>UI Libraries:</strong>[Material UI AppBar](https://mui.com/components/app-bar/), [Bootstrap Navbar](https://getbootstrap.com/docs/5.0/components/navbar/)

## Summary Recommendations

- Use hamburger menus only when space is tight or options are secondary.
- Default to visible navigation when possible.
- Follow familiar icon patterns and placement.
- Label the menu where recognition is in doubt.
- Never hide critical features; keep key actions visible.
- Test usability and accessibility with real users.
- Ensure keyboard and screen reader support.

*Expert advice: [NNG: Hamburger Menu Icon Recognizability](https://www.nngroup.com/articles/hamburger-menu-icon-recognizability/)*

## Further Reading & Resources

- [Interaction Design Foundation: Hamburger Menu UX](https://www.interaction-design.org/literature/article/hamburger-menu-ux)
- [NNG: The Hamburger-Menu Icon Today: Is it Recognizable?](https://www.nngroup.com/articles/hamburger-menu-icon-recognizability/)
- [Justinmind: Guide to Hamburger Menu Design](https://www.justinmind.com/ui-design/hamburger-menu)
- [HubSpot: What is a Hamburger Button?](https://blog.hubspot.com/website/hamburger-button)
- [TechTarget: Hamburger Icon (slide drawer navigation)](https://www.techtarget.com/whatis/definition/hamburger-icon-slide-drawer-navigation)
- [NNG YouTube: Hamburger Menu Icon Update](https://www.youtube.com/watch?v=1au4Gff9cSo)
- [NNG: Hidden Navigation Hurts UX Metrics](https://www.nngroup.com/articles/hamburger-menus/)
- [Justinmind: Navigation Design Patterns](https://www.justinmind.com/blog/navigation-design-almost-everything-you-need-to-know/)
- [Netwizard: Hamburger Menu Pros and Cons](https://netwizarddesign.com.au/the-three-line-menu-option-called-hamburger-menu-what-are-the-pros-and-cons/)
- [UserWay: Website Navigation, UX, and Accessibility](https://userway.org/blog/website-navigation/)
- [UXDesign.cc: Create an Accessible Hamburger Menu](https://uxdesign.cc/create-an-accessible-hamburger-menu-869b0301cfd7)

<strong>Related Glossary Terms</strong>- [Navigation Options](#)
- [Progressive Disclosure](#)
- [Interaction Cost](#)
- [Mobile-Friendly Website](#)
- [Web Design](#)

- [Interaction Design Foundation: Hamburger Menu UX](https://www.interaction-design.org/literature/article/hamburger-menu-ux)
- [UXDesign.cc: Accessible Hamburger Menu Guide](https://uxdesign.cc/create-an-accessible-hamburger-menu-869b0301cfd7)
- [UserWay: Website Navigation Best Practices](https://userway.org/blog/website-navigation/)
- [NNG: Hamburger Menus Hurt UX Metrics](https://www.nngroup.com/articles/hamburger-menus/)
- [Justinmind: Hamburger Menu Design Guide](https://www.justinmind.com/ui-design/hamburger-menu)

For a deep dive into implementation, accessibility, and UX best practices, visit the recommended further reading links. This glossary consolidates the latest research and expert consensus on hamburger menus, their history, usage, best practices, and accessibility.
