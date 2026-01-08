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

A **Persistent Menu**is an always-on, static menu interface embedded in a chatbot, visible to users throughout their session. It provides immediate access to critical chatbot actions, regardless of message context or conversation flow. The menu typically appears via a recognizable icon (often a [hamburger menu](/en/glossary/hamburger-menu/)) and lists essential actions such as restart, help, unsubscribe, or navigation shortcuts.

- **Key Features:**- Always accessible—never disappears after a button is used.
  - Available at any step in the conversation or onboarding.
  - Presents a clear, consistent set of user options.
  - Ideal for both first-time and returning users.
## Why Use a Persistent Menu? (Core Benefits)

A well-configured Persistent Menu provides clear user value and supports business objectives:

- **Faster Navigation:**Users reach frequently-needed features or info instantly—no need to remember commands or search through conversation threads.
- **Reduces Friction:**Prevents users from getting lost or frustrated; offers a direct escape route from confusing flows.
- **Feature Discovery:**New and returning users see the bot’s main capabilities at a glance.
- **Business Alignment:**Promotes core actions (e.g., product quizzes, contact support, order tracking) that drive business value.
- **Accessibility:**Users with accessibility needs benefit from clearly structured, always-available actions.
## How is a Persistent Menu Used?

The Persistent Menu is usually accessed by clicking or tapping a menu icon (commonly the hamburger icon) in the chat window. Its contents are available at any time, regardless of conversation stage.

**User Experience Highlights:**- Users can open the menu in onboarding, mid-conversation, or after completing an action.
- Typical actions: restart bot, access help/FAQ, jump to a main menu, unsubscribe, open external URLs, or trigger quizzes.
## Supported Channels & Platform Limitations

Persistent Menus are supported on major messaging and web platforms, but features and limits vary:

| Platform              | Support Level           | Notes/Limitations                                                                            |
|-----------------------|------------------------|----------------------------------------------------------------------------------------------|
| Facebook Messenger    | Full                   | Max 3 top-level items; supports nested menus, user input control.                            |
| Instagram             | Supported (via API)    | Similar to Messenger; check platform-specific documentation for updates.                      |
| Webchat Widgets       | Full (most builders)   | Button appearance, user input control, and nesting vary by vendor.                            |
| WhatsApp, Telegram    | Limited/Varies         | Check each bot builder’s documentation for support and limitations.                           |

- **Button Limit:**Messenger supports up to 3 buttons per menu level.
- **Appearance:**Menu icon and location may differ per channel.
- **Menu Scope:**Some platforms only allow a single menu per bot instance.
- **Disabling Input:**Often applies globally, not per flow.
## Menu Item Types & Structure

### Button Actions

A Persistent Menu can include several types of actions:

- **Send Message:**Triggers a specific bot flow or sends a defined message.
- **Open URL:**Opens a specified web page, often in an in-app browser.
- **Restart Bot:**Resets the conversation to the start or welcome step.
- **Unsubscribe:**Opts the user out of future messages or interactions.
- **Take Quiz:**Launches a product or feedback quiz.
- **Help/FAQ:**Displays support or answers to common questions.

### Nested Menus

Some platforms (like Messenger) allow menu nesting, grouping related actions under one label. Example: “Account” → “Profile”, “Settings”.

- **Limitation:**Not all platforms or builders support nested (sub)menus.

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

1. **Log in to Your Bot Platform Dashboard**2. **Open Bot Settings or Flow Builder**- Find the “Persistent Menu”, “Menu”, or “Navigation” section.
3. **Create/Edit the Persistent Menu**- Usually via a “Create” or “Edit” button.
4. **Add Menu Items**- For each slot: Choose action type, label, and target (flow, URL, etc).
5. **Arrange Order**- Drag and drop to reorder; most important actions first.
6. **Advanced Options**- Localize menu, enable/disable user input, add submenus if supported.
7. **Save & Publish**- Click “Save”, “Publish”, or toggle menu live.
### Platform-Specific Instructions

#### **Facebook Messenger (via Chatfuel)**1. Go to [Chatfuel Dashboard](https://dashboard.chatfuel.com).
2. Open the Flow tab; create/select your flow.
3. Double-click canvas, select “Entry Points → Persistent Menu”.
4. Add up to 3 buttons (e.g., “Restart Bot”, “Help”, “Unsubscribe”).
5. Drag to reorder, enable menu with toggle.
6. For localization, click “Localization” to add translations.

![Persistent Menu Example in Chatfuel](https://storage.googleapis.com/chatfuel-cms-staging/pic/original_persistent_menu_0_8a23ef77c3/original_persistent_menu_0_8a23ef77c3.webp)

- [Chatfuel: Persistent Menu Docs](https://chatfuel.com/blog/persistent-menu)

#### **ChatbotBuilder.ai**1. Go to Settings → Channels → Facebook Messenger/Instagram → Persistent Menu.
2. Click “Edit” to open setup wizard.
3. Add menu items as needed.
4. To disable user input, uncheck “Allow Keyboard Input”.
5. Save and publish.

- [ChatbotBuilder.ai: Persistent Menu](https://docs.chatbotbuilder.ai/support/solutions/articles/150000166613-persistent-menu)

#### **Certainly**1. Open [Bot Settings](https://support.certainly.io/knowledge/Individualize-your-chatbot-in-Bot-Settings).
2. Select the Persistent Menu tab.
3. Add items (Open URL, Send message, Nested).
4. Save your changes.

- [Certainly Knowledge Base: Add a Persistent Menu](https://support.certainly.io/knowledge/add-a-persistent-menu-to-your-chat)

#### **Webchat Widgets (BotSailor Example)**1. Log in to BotSailor dashboard.
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

**Best Practice:**Only localize if your bot supports those languages throughout the user journey.

### Disabling User Input

- Disable free text input to restrict users to menu/[quick replies](/en/glossary/quick-replies/) only.
- Useful for strict flows (e.g., quizzes, forms) but beware: this usually disables input globally.
- To collect open responses (emails, addresses), leave user input enabled.

### Menu Appearance & Order

- Menu is usually bottom-right (Messenger), but varies per platform.
- Order matters: Place most critical actions at the top.
- Use descriptive, short labels (30-character limit is common).
- Emojis can aid recognition, but keep usage professional.
- Buttons can open URLs or trigger bot flows.

## Best Practices for Persistent Menus

- **Keep it Simple:**Limit to 2–3 primary actions; avoid menu clutter.
- **Prioritize Critical Functions:**“Restart”, “Help”, “Unsubscribe” should be easily accessible.
- **Clear Labels:**Use terms like “Restart Bot” over vague terms like “Again”.
- **Mix Action Types:**Combine links, flows, and submenus as needed.
- **Test Thoroughly:**Check on all channels and devices.
- **Maintain Accessibility:**Use readable fonts and clear contrast.
- **Update Regularly:**Adjust menu based on analytics and user feedback.
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

- **Menu Not Showing:**Confirm menu is enabled and published; check channel support.
- **User Input Disabled Unintentionally:**Remember disabling input often applies to the whole bot.
- **Localization Issues:**Make sure language settings are correct; only button text is localized.
- **Too Many Buttons:**Respect platform limits (e.g., Messenger = 3 per menu level); use nesting if supported.
- **Testing:**Test on all target channels and devices for visibility and function.
## Further Resources & Next Steps

- [Chatfuel Blog: Persistent Menu](https://chatfuel.com/blog/persistent-menu)
- [ChatbotBuilder.ai Documentation](https://docs.chatbotbuilder.ai/support/solutions/articles/150000166613-persistent-menu)
- [Certainly Knowledge Base: Add a Persistent Menu](https://support.certainly.io/knowledge/add-a-persistent-menu-to-your-chat)
- [Messenger Platform API: persistent_menu](https://developers.facebook.com/docs/messenger-platform/reference/messenger-profile-api/persistent-menu/)
- [YouTube: Persistent Menu in Website Chatbot](https://www.youtube.com/watch?v=4kAlBEgCvwM)
- [YouTube: Using Persistent Menu Entry Point in Chatfuel](https://www.youtube.com/watch?v=DWovaAjFOOk)

## Try It Yourself!

**Add a Persistent Menu to your chatbot:**- Log in to your chatbot builder.
- Follow the setup instructions for your platform.
- Test and iterate based on user feedback.

**Need help?**Explore the documentation and video tutorials linked above, or reach out to your platform’s support team.

## Related Keywords

add persistent menu, button persistent menu, persistent menu add, creating persistent menu, navigational menu, disable user input, recommendation quiz, facebook messenger, restart bot, chat bot, menu items, add buttons, menu users, main menu

**Comprehensive Deep-Dive**This glossary consolidates platform documentation, best practices, and implementation details. For official technical API details, see [Meta’s persistent_menu API reference](https://developers.facebook.com/docs/messenger-platform/reference/messenger-profile-api/persistent-menu/).  

For visual and step-by-step tutorials, watch:  
- [How to Setup Persistent Menu In Website Chatbot (YouTube)](https://www.youtube.com/watch?v=4kAlBEgCvwM)  
- [How to Use the Persistent Menu Entry Point in Chatfuel (YouTube)](https://www.youtube.com/watch?v=DWovaAjFOOk)

For further reading on customization and advanced use, visit:  
- [ChatbotBuilder.ai Documentation](https://docs.chatbotbuilder.ai/support/solutions/articles/150000166613-persistent-menu)  
- [Certainly Knowledge Base](https://support.certainly.io/knowledge/add-a-persistent-menu-to-your-chat)

**Enhance your chatbot now by leveraging these resources and building a Persistent Menu that fits your users’ needs and your business goals.**
