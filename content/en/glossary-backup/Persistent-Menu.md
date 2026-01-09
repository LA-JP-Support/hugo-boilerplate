---
title: Persistent Menu
translationKey: persistent-menu
description: 'Learn about Persistent Menus in chatbots: what they are, why use them,
  how to implement them, and best practices for enhancing user navigation and experience.'
keywords:
- Persistent Menu
- Chatbot
- Facebook Messenger
- Navigational Menu
- Menu Items
category: General
type: glossary
date: 2025-12-05
lastmod: 2025-12-05
draft: false
---
## What is a Persistent Menu?

A <strong>Persistent Menu</strong>is an always-on, static menu interface embedded in a chatbot, visible to users throughout their session. It provides immediate access to critical chatbot actions, regardless of message context or conversation flow. The menu typically appears via a recognizable icon (often a hamburger menu) and lists essential actions such as restart, help, unsubscribe, or navigation shortcuts.

- <strong>Key Features:</strong>- Always accessible—never disappears after a button is used.
  - Available at any step in the conversation or onboarding.
  - Presents a clear, consistent set of user options.
  - Ideal for both first-time and returning users.
## Why Use a Persistent Menu? (Core Benefits)

A well-configured Persistent Menu provides clear user value and supports business objectives:

- <strong>Faster Navigation:</strong>Users reach frequently-needed features or info instantly—no need to remember commands or search through conversation threads.
- <strong>Reduces Friction:</strong>Prevents users from getting lost or frustrated; offers a direct escape route from confusing flows.
- <strong>Feature Discovery:</strong>New and returning users see the bot’s main capabilities at a glance.
- <strong>Business Alignment:</strong>Promotes core actions (e.g., product quizzes, contact support, order tracking) that drive business value.
- <strong>Accessibility:</strong>Users with accessibility needs benefit from clearly structured, always-available actions.
## How is a Persistent Menu Used?

The Persistent Menu is usually accessed by clicking or tapping a menu icon (commonly the hamburger icon) in the chat window. Its contents are available at any time, regardless of conversation stage.

<strong>User Experience Highlights:</strong>- Users can open the menu in onboarding, mid-conversation, or after completing an action.
- Typical actions: restart bot, access help/FAQ, jump to a main menu, unsubscribe, open external URLs, or trigger quizzes.
## Supported Channels & Platform Limitations

Persistent Menus are supported on major messaging and web platforms, but features and limits vary:

| Platform              | Support Level           | Notes/Limitations                                                                            |
|-----------------------|------------------------|----------------------------------------------------------------------------------------------|
| Facebook Messenger    | Full                   | Max 3 top-level items; supports nested menus, user input control.                            |
| Instagram             | Supported (via API)    | Similar to Messenger; check platform-specific documentation for updates.                      |
| Webchat Widgets       | Full (most builders)   | Button appearance, user input control, and nesting vary by vendor.                            |
| WhatsApp, Telegram    | Limited/Varies         | Check each bot builder’s documentation for support and limitations.                           |

- <strong>Button Limit:</strong>Messenger supports up to 3 buttons per menu level.
- <strong>Appearance:</strong>Menu icon and location may differ per channel.
- <strong>Menu Scope:</strong>Some platforms only allow a single menu per bot instance.
- <strong>Disabling Input:</strong>Often applies globally, not per flow.
## Menu Item Types & Structure

### Button Actions

A Persistent Menu can include several types of actions:

- <strong>Send Message:</strong>Triggers a specific bot flow or sends a defined message.
- <strong>Open URL:</strong>Opens a specified web page, often in an in-app browser.
- <strong>Restart Bot:</strong>Resets the conversation to the start or welcome step.
- <strong>Unsubscribe:</strong>Opts the user out of future messages or interactions.
- <strong>Take Quiz:</strong>Launches a product or feedback quiz.
- <strong>Help/FAQ:</strong>Displays support or answers to common questions.

### Nested Menus

Some platforms (like Messenger) allow menu nesting, grouping related actions under one label. Example: “Account” → “Profile”, “Settings”.

- <strong>Limitation:</strong>Not all platforms or builders support nested (sub)menus.

### Menu Item Examples

| Button Label       | Action                         | Description                                      |
|--------------------|-------------------------------|--------------------------------------------------|
| 🏠 Main Menu       | Go to main menu flow           | Returns user to main navigation                   |
| 🔁 Restart         | Reset conversation             | Lets user start over                             |
| ❌ Unsubscribe     | Opt-out action                 | Ends further messages to the user                |
| 📝 Take Quiz       | Launch recommendation/quiz     | Collects info, provides personalized suggestions |
| ❓ Help            | Show FAQ/contact options        | Offers instant support                           |
| 📦 Order Status    | Check order                    | For e-commerce bots                              |
| 💬 Contact Support | Open support flow/email         | Human agent or further help                      |

*You may mix different action types within one menu.*
## Step-by-Step: How to Add a Persistent Menu

The process depends on your chatbot builder/platform. Here’s a generalized guide, followed by specific instructions for popular platforms.

### General Steps

1. <strong>Log in to Your Bot Platform Dashboard</strong>2. <strong>Open Bot Settings or Flow Builder</strong>- Find the “Persistent Menu”, “Menu”, or “Navigation” section.
3. <strong>Create/Edit the Persistent Menu</strong>- Usually via a “Create” or “Edit” button.
4. <strong>Add Menu Items</strong>- For each slot: Choose action type, label, and target (flow, URL, etc).
5. <strong>Arrange Order</strong>- Drag and drop to reorder; most important actions first.
6. <strong>Advanced Options</strong>- Localize menu, enable/disable user input, add submenus if supported.
7. <strong>Save & Publish</strong>- Click “Save”, “Publish”, or toggle menu live.
### Platform-Specific Instructions

#### <strong>Facebook Messenger (via Chatfuel)</strong>1. Go to [Chatfuel Dashboard](https://dashboard.chatfuel.com).
2. Open the Flow tab; create/select your flow.
3. Double-click canvas, select “Entry Points → Persistent Menu”.
4. Add up to 3 buttons (e.g., “Restart Bot”, “Help”, “Unsubscribe”).
5. Drag to reorder, enable menu with toggle.
6. For localization, click “Localization” to add translations.

![Persistent Menu Example in Chatfuel](https://storage.googleapis.com/chatfuel-cms-staging/pic/original_persistent_menu_0_8a23ef77c3/original_persistent_menu_0_8a23ef77c3.webp)

- [Chatfuel: Persistent Menu Docs](https://chatfuel.com/blog/persistent-menu)

#### <strong>ChatbotBuilder.ai</strong>1. Go to Settings → Channels → Facebook Messenger/Instagram → Persistent Menu.
2. Click “Edit” to open setup wizard.
3. Add menu items as needed.
4. To disable user input, uncheck “Allow Keyboard Input”.
5. Save and publish.

- [ChatbotBuilder.ai: Persistent Menu](https://docs.chatbotbuilder.ai/support/solutions/articles/150000166613-persistent-menu)

#### <strong>Certainly</strong>1. Open [Bot Settings](https://support.certainly.io/knowledge/Individualize-your-chatbot-in-Bot-Settings).
2. Select the Persistent Menu tab.
3. Add items (Open URL, Send message, Nested).
4. Save your changes.

- [Certainly Knowledge Base: Add a Persistent Menu](https://support.certainly.io/knowledge/add-a-persistent-menu-to-your-chat)

#### <strong>Webchat Widgets (BotSailor Example)</strong>1. Log in to BotSailor dashboard.
2. Go to your web chatbot manager.
3. Click on “Persistent Menu”.
4. Click “Create”, configure menu in the popup.
5. You can disable user input entirely if needed.
6. Save and test your web chat widget.

- [YouTube Tutorial: Persistent Menu in Website Chatbot](https://www.youtube.com/watch?v=4kAlBEgCvwM)

## Customizing the Persistent Menu

### Localization (Multiple Languages)

- Add translations via a “Localization” or “Add Language” button.
- Select target language, enter translated button labels.
- Only menu button text is localized, not full conversation flows.

<strong>Best Practice:</strong>Only localize if your bot supports those languages throughout the user journey.

### Disabling User Input

- Disable free text input to restrict users to menu/quick replies only.
- Useful for strict flows (e.g., quizzes, forms) but beware: this usually disables input globally.
- To collect open responses (emails, addresses), leave user input enabled.

### Menu Appearance & Order

- Menu is usually bottom-right (Messenger), but varies per platform.
- Order matters: Place most critical actions at the top.
- Use descriptive, short labels (30-character limit is common).
- Emojis can aid recognition, but keep usage professional.
- Buttons can open URLs or trigger bot flows.

## Best Practices for Persistent Menus

- <strong>Keep it Simple:</strong>Limit to 2–3 primary actions; avoid menu clutter.
- <strong>Prioritize Critical Functions:</strong>“Restart”, “Help”, “Unsubscribe” should be easily accessible.
- <strong>Clear Labels:</strong>Use terms like “Restart Bot” over vague terms like “Again”.
- <strong>Mix Action Types:</strong>Combine links, flows, and submenus as needed.
- <strong>Test Thoroughly:</strong>Check on all channels and devices.
- <strong>Maintain Accessibility:</strong>Use readable fonts and clear contrast.
- <strong>Update Regularly:</strong>Adjust menu based on analytics and user feedback.
## Common Use Cases & Examples

### E-commerce Chatbot Menu

| Button         | Action                 |
|----------------|-----------------------|
| 🛒 Shop        | Open main shopping flow|
| 🚚 Track Order | Show order status      |
| ❓ Help        | FAQ or support flow    |

### Product Recommendation Quiz

| Button           | Action                        |
|------------------|------------------------------|
| 📝 Take Quiz     | Start product quiz flow       |
| 🔁 Restart Bot   | Reset conversation            |
| ❌ Unsubscribe   | Opt-out of bot messages       |

### Restaurant Reservation Bot

| Button          | Action                    |
|-----------------|--------------------------|
| 📅 Book Table   | Start reservation flow    |
| 📖 Menu        | Open menu URL             |
| 🏠 Main Menu   | Return to home flow       |

## Troubleshooting & Considerations

- <strong>Menu Not Showing:</strong>Confirm menu is enabled and published; check channel support.
- <strong>User Input Disabled Unintentionally:</strong>Remember disabling input often applies to the whole bot.
- <strong>Localization Issues:</strong>Make sure language settings are correct; only button text is localized.
- <strong>Too Many Buttons:</strong>Respect platform limits (e.g., Messenger = 3 per menu level); use nesting if supported.
- <strong>Testing:</strong>Test on all target channels and devices for visibility and function.
## Further Resources & Next Steps

- [Chatfuel Blog: Persistent Menu](https://chatfuel.com/blog/persistent-menu)
- [ChatbotBuilder.ai Documentation](https://docs.chatbotbuilder.ai/support/solutions/articles/150000166613-persistent-menu)
- [Certainly Knowledge Base: Add a Persistent Menu](https://support.certainly.io/knowledge/add-a-persistent-menu-to-your-chat)
- [Messenger Platform API: persistent_menu](https://developers.facebook.com/docs/messenger-platform/reference/messenger-profile-api/persistent-menu/)
- [YouTube: Persistent Menu in Website Chatbot](https://www.youtube.com/watch?v=4kAlBEgCvwM)
- [YouTube: Using Persistent Menu Entry Point in Chatfuel](https://www.youtube.com/watch?v=DWovaAjFOOk)

## Try It Yourself!

<strong>Add a Persistent Menu to your chatbot:</strong>- Log in to your chatbot builder.
- Follow the setup instructions for your platform.
- Test and iterate based on user feedback.

<strong>Need help?</strong>Explore the documentation and video tutorials linked above, or reach out to your platform’s support team.

## Related Keywords

add persistent menu, button persistent menu, persistent menu add, creating persistent menu, navigational menu, disable user input, recommendation quiz, facebook messenger, restart bot, chat bot, menu items, add buttons, menu users, main menu

<strong>Comprehensive Deep-Dive</strong>This glossary consolidates platform documentation, best practices, and implementation details. For official technical API details, see [Meta’s persistent_menu API reference](https://developers.facebook.com/docs/messenger-platform/reference/messenger-profile-api/persistent-menu/).  

For visual and step-by-step tutorials, watch:  
- [How to Setup Persistent Menu In Website Chatbot (YouTube)](https://www.youtube.com/watch?v=4kAlBEgCvwM)  
- [How to Use the Persistent Menu Entry Point in Chatfuel (YouTube)](https://www.youtube.com/watch?v=DWovaAjFOOk)

For further reading on customization and advanced use, visit:  
- [ChatbotBuilder.ai Documentation](https://docs.chatbotbuilder.ai/support/solutions/articles/150000166613-persistent-menu)  
- [Certainly Knowledge Base](https://support.certainly.io/knowledge/add-a-persistent-menu-to-your-chat)

<strong>Enhance your chatbot now by leveraging these resources and building a Persistent Menu that fits your users’ needs and your business goals.</strong>
