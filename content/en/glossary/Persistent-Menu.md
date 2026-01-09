---
title: Persistent Menu
translationKey: persistent-menu
description: "A fixed menu that always stays visible in a chatbot, letting users quickly access important features like help or restart anytime without scrolling through messages."
keywords:
- Persistent Menu
- Chatbot
- Facebook Messenger
- Navigational Menu
- Menu Items
category: General
type: glossary
date: 2025-12-18
lastmod: 2025-12-18
draft: false
---

## What Is a Persistent Menu?

A Persistent Menu is an always-on, static menu interface embedded in a chatbot, providing continuous access to critical actions regardless of message context or conversation flow. The menu typically appears via a recognizable icon—often the hamburger menu—and lists essential actions such as restart, help, unsubscribe, or navigation shortcuts.

Unlike temporary buttons or quick replies that disappear after use, a Persistent Menu remains accessible throughout the entire user session. It serves as a constant navigational anchor, ensuring users can always access key functions without remembering commands or searching through conversation history. This architectural pattern has become a best practice in chatbot design, significantly improving user experience and reducing friction in conversational interfaces.

The Persistent Menu concept originated on messaging platforms like Facebook Messenger but has since been adopted across web chat widgets, mobile applications, and other conversational interfaces. Its persistent nature makes it ideal for both first-time users discovering bot capabilities and returning users seeking quick access to familiar features.

## Core Benefits

### Faster Navigation

Users reach frequently-needed features or information instantly without remembering commands or searching through conversation threads. This direct access reduces cognitive load and accelerates task completion.

### Friction Reduction

Prevents users from getting lost or frustrated by offering a direct escape route from confusing flows. Users always have a clear path back to main functionality or help resources.

### Feature Discovery

New and returning users see the bot's main capabilities at a glance. The menu serves as a feature catalog, increasing awareness of available functionality.

### Business Alignment

Promotes core actions such as product quizzes, contact support, or order tracking that drive business value. Strategic menu design guides users toward high-value interactions.

### Accessibility Enhancement

Users with accessibility needs benefit from clearly structured, always-available actions. Screen readers and assistive technologies can reliably access menu options.

## User Experience

### Access Pattern

The Persistent Menu is usually accessed by clicking or tapping a menu icon in the chat window. Its contents remain available at any conversation stage—during onboarding, mid-conversation, or after completing an action.

### Typical Actions

<strong>Restart Bot</strong>Resets conversation to the start or welcome step, useful when users want to begin fresh or encounter issues.

<strong>Access Help/FAQ</strong>Displays support resources or answers to common questions, providing self-service assistance.

<strong>Jump to Main Menu</strong>Returns users to primary navigation, offering a clear path back from specialized flows.

<strong>Unsubscribe</strong>Opts users out of future messages or interactions, respecting user preferences and privacy.

<strong>Open External URLs</strong>Launches web pages for additional resources, documentation, or related services.

<strong>Trigger Quizzes</strong>Initiates product recommendation or feedback quizzes, engaging users in interactive experiences.

## Platform Support and Limitations

| Platform | Support Level | Notes/Limitations |
|----------|--------------|-------------------|
| Facebook Messenger | Full | Max 3 top-level items; supports nested menus, user input control |
| Instagram | Supported (via API) | Similar to Messenger; check platform documentation for updates |
| Webchat Widgets | Full (most builders) | Button appearance, user input control, and nesting vary by vendor |
| WhatsApp, Telegram | Limited/Varies | Check each bot builder's documentation for support and limitations |

### Key Limitations

<strong>Button Limit</strong>Messenger supports up to 3 buttons per menu level. Exceeding this requires nesting or prioritization.

<strong>Appearance</strong>Menu icon and location may differ per channel. Consistent branding may require platform-specific customization.

<strong>Menu Scope</strong>Some platforms allow only a single menu per bot instance, requiring careful global design.

<strong>Input Control</strong>Disabling user input often applies globally, not per flow, requiring careful consideration of use cases.

## Menu Structure and Actions

### Button Action Types

<strong>Send Message</strong>Triggers a specific bot flow or sends a defined message, enabling programmatic conversation control.

<strong>Open URL</strong>Opens a specified web page, often in an in-app browser, for external resources or documentation.

<strong>Restart Bot</strong>Resets the conversation to the start or welcome step, providing a clean slate.

<strong>Unsubscribe</strong>Opts the user out of future messages or interactions, ensuring compliance with user preferences.

<strong>Take Quiz</strong>Launches a product or feedback quiz, engaging users in interactive experiences.

<strong>Help/FAQ</strong>Displays support or answers to common questions, enabling self-service resolution.

### Nested Menus

Some platforms like Messenger allow menu nesting, grouping related actions under one label. For example, "Account" might contain "Profile" and "Settings" submenus. However, not all platforms or builders support nested structures, requiring careful platform assessment.

### Example Menu Configurations

<strong>E-commerce Chatbot</strong>| Button | Action |
|--------|--------|
| 🛒 Shop | Open main shopping flow |
| 🚚 Track Order | Show order status |
| ❓ Help | FAQ or support flow |

<strong>Product Recommendation Quiz</strong>| Button | Action |
|--------|--------|
| 📝 Take Quiz | Start product quiz flow |
| 🔁 Restart Bot | Reset conversation |
| ❌ Unsubscribe | Opt-out of bot messages |

<strong>Restaurant Reservation Bot</strong>| Button | Action |
|--------|--------|
| 📅 Book Table | Start reservation flow |
| 📖 Menu | Open menu URL |
| 🏠 Main Menu | Return to home flow |

## Implementation Guide

### General Steps

1. <strong>Log in to Your Bot Platform Dashboard</strong>2. <strong>Open Bot Settings or Flow Builder</strong>- Find the "Persistent Menu", "Menu", or "Navigation" section
3. <strong>Create/Edit the Persistent Menu</strong>- Usually via a "Create" or "Edit" button
4. <strong>Add Menu Items</strong>- For each slot: Choose action type, label, and target (flow, URL, etc)
5. <strong>Arrange Order</strong>- Drag and drop to reorder; most important actions first
6. <strong>Advanced Options</strong>- Localize menu, enable/disable user input, add submenus if supported
7. <strong>Save & Publish</strong>- Click "Save", "Publish", or toggle menu live

### Platform-Specific Instructions

<strong>Facebook Messenger (via Chatfuel)</strong>1. Go to Chatfuel Dashboard
2. Open the Flow tab; create/select your flow
3. Double-click canvas, select "Entry Points → Persistent Menu"
4. Add up to 3 buttons (e.g., "Restart Bot", "Help", "Unsubscribe")
5. Drag to reorder, enable menu with toggle
6. For localization, click "Localization" to add translations

<strong>ChatbotBuilder.ai</strong>1. Go to Settings → Channels → Facebook Messenger/Instagram → Persistent Menu
2. Click "Edit" to open setup wizard
3. Add menu items as needed
4. To disable user input, uncheck "Allow Keyboard Input"
5. Save and publish

<strong>Certainly</strong>1. Open Bot Settings
2. Select the Persistent Menu tab
3. Add items (Open URL, Send message, Nested)
4. Save your changes

<strong>Webchat Widgets</strong>1. Log in to bot platform dashboard
2. Go to web chatbot manager
3. Click on "Persistent Menu"
4. Click "Create", configure menu in the popup
5. You can disable user input entirely if needed
6. Save and test your web chat widget

## Customization Options

### Localization (Multiple Languages)

Add translations via a "Localization" or "Add Language" button. Select target language and enter translated button labels. Note that only menu button text is localized, not full conversation flows.

<strong>Best Practice:</strong>Only localize if your bot supports those languages throughout the user journey to maintain consistency.

### Disabling User Input

Disable free text input to restrict users to menu and quick replies only. This is useful for strict flows such as quizzes or forms, but be aware that this usually disables input globally. To collect open responses like emails or addresses, leave user input enabled.

### Menu Appearance and Order

<strong>Location</strong>Menu is usually bottom-right in Messenger, but varies per platform.

<strong>Order</strong>Place most critical actions at the top as order matters for user attention and accessibility.

<strong>Labels</strong>Use descriptive, short labels (30-character limit is common). Clear, action-oriented language improves usability.

<strong>Emojis</strong>Can aid recognition and visual appeal, but keep usage professional and accessible.

<strong>Buttons</strong>Can open URLs or trigger bot flows, providing flexible functionality.

## Best Practices

<strong>Keep it Simple</strong>Limit to 2-3 primary actions to avoid menu clutter and decision paralysis.

<strong>Prioritize Critical Functions</strong>"Restart", "Help", and "Unsubscribe" should be easily accessible for user control and compliance.

<strong>Clear Labels</strong>Use terms like "Restart Bot" over vague terms like "Again" for clarity.

<strong>Mix Action Types</strong>Combine links, flows, and submenus as needed to provide comprehensive functionality.

<strong>Test Thoroughly</strong>Check on all channels and devices to ensure visibility and proper function.

<strong>Maintain Accessibility</strong>Use readable fonts and clear contrast. Ensure screen reader compatibility.

<strong>Update Regularly</strong>Adjust menu based on analytics and user feedback to maintain relevance.

## Troubleshooting

<strong>Menu Not Showing</strong>Confirm menu is enabled and published. Check channel support and configuration settings.

<strong>User Input Disabled Unintentionally</strong>Remember disabling input often applies to the whole bot, not individual flows.

<strong>Localization Issues</strong>Verify language settings are correct. Only button text is localized, not conversation flows.

<strong>Too Many Buttons</strong>Respect platform limits (e.g., Messenger = 3 per menu level). Use nesting if supported or prioritize most important actions.

<strong>Testing</strong>Test on all target channels and devices for visibility and function before full deployment.

## References


1. Chatfuel. (n.d.). Persistent Menu. Chatfuel Blog.
2. ChatbotBuilder.ai. (n.d.). Persistent Menu Documentation. ChatbotBuilder.ai Documentation.
3. Certainly. (n.d.). Add a Persistent Menu. Certainly Knowledge Base.
4. Facebook. (n.d.). Persistent Menu. Messenger Platform API.
5. Unknown. (n.d.). Persistent Menu in Website Chatbot. YouTube.
6. Unknown. (n.d.). Using Persistent Menu Entry Point in Chatfuel. YouTube.
7. Certainly. (n.d.). Bot Settings. Certainly Bot Settings.
