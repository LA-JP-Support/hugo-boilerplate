---
title: "Adaptive Cards – Glossary & Technical Reference"
translationKey: "adaptive-cards-glossary-technical-reference"
description: "--- **Keyword:** Adaptive Cards **Definition:** A platform-agnostic UI framework allowing developers to exchange rich content cards (images, text,..."
keywords: ['Adaptive Cards – Glossary & Technical Reference', 'AI Chatbots', 'Automation']
category: "AI Chatbot & Automation"
type: "glossary"
draft: false
---

---

# Adaptive Cards – Glossary & Technical Reference

**Keyword:** Adaptive Cards  
**Definition:** A platform-agnostic UI framework allowing developers to exchange rich content cards (images, text, forms) in a common format.  
## Table of Contents

1. [What Are Adaptive Cards?](#what-are-adaptive-cards)
2. [Core Concepts](#core-concepts)
    - [JSON Schema](#json-schema)
    - [Platform-Agnostic Rendering](#platform-agnostic-rendering)
    - [Host Applications](#host-applications)
3. [Key Features and Principles](#key-features-and-principles)
    - [Portability](#portability)
    - [Declarative Authoring](#declarative-authoring)
    - [Open Source and Extensibility](#open-source-and-extensibility)
    - [Native Performance](#native-performance)
    - [Dynamic and Interactive Content](#dynamic-and-interactive-content)
4. [How Adaptive Cards Are Used](#how-adaptive-cards-are-used)
    - [Authoring and Design](#authoring-and-design)
    - [Rendering and Display](#rendering-and-display)
    - [User Input and Actions](#user-input-and-actions)
5. [Typical Use Cases](#typical-use-cases)
    - [AI Chatbots](#ai-chatbots)
    - [Business Process Automation](#business-process-automation)
    - [Enterprise Messaging](#enterprise-messaging)
    - [Web and Mobile Applications](#web-and-mobile-applications)
6. [Integration Examples](#integration-examples)
    - [Microsoft Teams](#microsoft-teams)
    - [Microsoft Outlook Actionable Messages](#microsoft-outlook-actionable-messages)
    - [Bot Framework](#bot-framework)
    - [Custom Apps and Web Portals](#custom-apps-and-web-portals)
7. [Implementation Steps](#implementation-steps)
    - [Creating an Adaptive Card](#creating-an-adaptive-card)
    - [Integrating with Microsoft Teams via Power Automate](#integrating-with-microsoft-teams-via-power-automate)
    - [Custom Integration (SDKs)](#custom-integration-sdks)
8. [Best Practices](#best-practices)
9. [Known Limitations](#known-limitations)
10. [Tooling & Ecosystem](#tooling--ecosystem)
11. [Quotes & Testimonials](#quotes--testimonials)
12. [Visual Aids: Examples & JSON Snippets](#visual-aids-examples--json-snippets)
13. [Further Reading & References](#further-reading--references)

---

## What Are Adaptive Cards?

Adaptive Cards are a platform-agnostic, open card exchange format that enables developers to exchange UI content in a common and consistent way. Authored in JSON, Adaptive Cards encapsulate structured data—such as text, images, inputs, containers, and actions—into a portable payload. This payload, when delivered to a host application (such as Microsoft Teams, Outlook, Windows Timeline, or a custom web app), is transformed into native UI that adopts the style and behavior of the host environment.

The Adaptive Cards framework is open source and designed to work across all major platforms and UI frameworks. Its declarative approach separates content and presentation, promoting reusability and easy maintenance. Adaptive Cards are integral to AI chatbots, business process automation, and cross-platform messaging due to their consistent, interactive, and lightweight user experience.

- [Adaptive Cards Official Site](https://adaptivecards.io/)
- [Adaptive Cards Overview – Microsoft Learn](https://learn.microsoft.com/en-us/adaptive-cards/)

---

## Core Concepts

### JSON Schema

Adaptive Cards are defined by a declarative JSON schema that specifies the structure and content of each card. The schema supports a wide range of elements, including `TextBlock`, `Image`, `Input`, `Container`, `FactSet`, and more. Actions such as `Action.OpenUrl` or `Action.Submit` allow user interactivity. The schema is both human-readable and machine-processable.

**Example: Basic Adaptive Card JSON**
```json
{
  "type": "AdaptiveCard",
  "version": "1.4",
  "body": [
    {
      "type": "TextBlock",
      "text": "Welcome to Adaptive Cards!",
      "weight": "Bolder",
      "size": "Medium"
    },
    {
      "type": "Image",
      "url": "https://adaptivecards.io/content/cats/1.png"
    }
  ],
  "actions": [
    {
      "type": "Action.OpenUrl",
      "title": "Learn More",
      "url": "https://adaptivecards.io"
    }
  ]
}
```
- [Adaptive Cards Schema Reference](https://adaptivecards.io/explorer/)
- [JSON Schema Specification](https://learn.microsoft.com/en-us/adaptive-cards/authoring-cards/card-schema)

### Platform-Agnostic Rendering

Adaptive Cards are rendered natively by any host application that supports the Adaptive Cards framework. The host application parses the card's JSON and automatically adapts its appearance and controls to match the host's design guidelines and accessibility requirements. This ensures a consistent and integrated user experience across platforms.

- [Rendering Cards – Getting Started](https://learn.microsoft.com/en-us/adaptive-cards/rendering-cards/getting-started)

### Host Applications

A host application is any service or platform that can receive, parse, and render Adaptive Cards. Notable hosts include:
- Microsoft Teams
- Outlook (Actionable Messages)
- Windows Timeline
- Web applications
- Bots built on Microsoft Bot Framework

The host application controls the final look and feel, ensuring that Adaptive Cards blend seamlessly into the native user interface.

- [Host Applications Overview](https://learn.microsoft.com/en-us/adaptive-cards/rendering-cards/getting-started)
- [Teams Design Best Practices](https://learn.microsoft.com/en-us/microsoftteams/platform/task-modules-and-cards/cards/design-effective-cards)

---

## Key Features and Principles

### Portability

Adaptive Cards are designed to work across any app, device, or UI framework. The "write once, render anywhere" paradigm eliminates the need for custom markup or repeated development for different platforms.

- [Portable UI Integration](https://learn.microsoft.com/en-us/adaptive-cards/)

### Declarative Authoring

Authors define card UI in JSON, specifying the structure, content, and actions without imperative programming. Basic interactivity and dynamic layouts are supported natively through the schema.

- [Authoring Cards – Getting Started](https://learn.microsoft.com/en-us/adaptive-cards/authoring-cards/getting-started)

### Open Source and Extensibility

The Adaptive Cards framework is open source, with libraries and schemas available for extension and customization. Developers can add custom elements, actions, or templates to meet specialized needs.

- [GitHub Repository](https://github.com/microsoft/AdaptiveCards/)

### Native Performance

Host applications render cards using native controls, ensuring that performance, accessibility, and styling are consistent with the host's ecosystem.

- [Native UI Rendering Details](https://adaptivecards.io/)

### Dynamic and Interactive Content

Adaptive Cards support input controls (text, date, toggles, choice sets) and actions (submit, open URL, custom actions). Dynamic data binding and templating allow cards to reflect real-time data and personalized content.

- [Adaptive Cards Templating Language](https://learn.microsoft.com/en-us/adaptive-cards/templating/language)

---

## How Adaptive Cards Are Used

### Authoring and Design

Card authors define layouts, content, and actions using the Adaptive Cards JSON schema. Authoring can be done manually or through visual design tools such as the [Adaptive Card Designer](https://adaptivecards.microsoft.com/designer.html).

- [Adaptive Card Designer](https://adaptivecards.microsoft.com/designer.html)
- [Design Best Practices](https://adaptivecards.microsoft.com/?topic=design-best-practices)

### Rendering and Display

Upon delivery to a host, the card's JSON is parsed and rendered as native UI. The host application determines final styling, ensuring cards match the look and feel of the environment.

- [Rendering Cards](https://learn.microsoft.com/en-us/adaptive-cards/rendering-cards/getting-started)

### User Input and Actions

Cards can collect data from users through input fields and support actions such as submit, open URL, or custom host-defined actions. User submissions are processed by bots, workflows, or application logic.

- [Input Controls Reference](https://adaptivecards.io/explorer/Input.Text.html)

---

## Typical Use Cases

### AI Chatbots

Adaptive Cards allow chatbots to present structured information, collect input, and guide conversational workflows within chat clients or web channels.

**Example:**  
A support bot presents a troubleshooting guide with images, steps, and feedback buttons.

- [Bot Framework Integration](https://docs.microsoft.com/en-us/microsoftteams/platform/concepts/cards/cards-reference#adaptive-card)

### Business Process Automation

Cards streamline business processes by embedding forms, approvals, and actionable content into users' preferred applications (e.g., Teams, Outlook).

**Example:**  
An employee receives a leave approval request as an Adaptive Card in Teams and can approve/reject it inline.

- [Actionable Messages in Outlook](https://docs.microsoft.com/outlook/actionable-messages/adaptive-card)

### Enterprise Messaging

Adaptive Cards enable delivery of interactive messages, surveys, notifications, and reports in enterprise communication tools.

**Example:**  
A survey card is sent via Outlook Actionable Message, and users can submit responses directly from their inbox.

### Web and Mobile Applications

Developers use Adaptive Cards to inject consistent, dynamic UI components across web, desktop, and mobile platforms without needing custom code for each.

**Example:**  
A CRM system displays customer details and allows quick updates via Adaptive Cards embedded in the dashboard.

- [SDKs for Major Platforms](https://learn.microsoft.com/en-us/adaptive-cards/sdk/rendering-cards/getting-started)

---

## Integration Examples

### Microsoft Teams

Adaptive Cards are deeply integrated into [Microsoft Teams](https://learn.microsoft.com/en-us/power-automate/overview-adaptive-cards), enabling actionable messages in channels, chats, and notifications. Cards can be posted by bots or automated workflows and support real-time updates and input collection.

**Typical Workflow:**  
1. A Power Automate flow posts an Adaptive Card to a Teams user or channel.
2. The card collects user input (e.g., approval, comments).
3. The workflow processes the response and continues based on user input.

- [Teams Integration Guide](https://learn.microsoft.com/en-us/power-automate/overview-adaptive-cards)

### Microsoft Outlook Actionable Messages

Outlook uses Adaptive Cards for [Actionable Messages](https://docs.microsoft.com/outlook/actionable-messages/adaptive-card), enabling users to complete tasks directly within an email (e.g., approve expenses, respond to surveys).

> “User engagement on surveys is always a challenge, but after utilizing Outlook Actionable Messages, our return rate surged from 10-12% to a 3 month average of 35%!”  
> — Richard Greenfield, Executive Support Services

- [Outlook Actionable Messages Documentation](https://docs.microsoft.com/outlook/actionable-messages/adaptive-card)

### Bot Framework

Bots built with the [Microsoft Bot Framework](https://dev.botframework.com/) use Adaptive Cards for rich, interactive messaging across web chat, Teams, and other supported channels.

- [Bot Framework Integration Documentation](https://docs.microsoft.com/en-us/microsoftteams/platform/concepts/cards/cards-reference#adaptive-card)

### Custom Apps and Web Portals

Adaptive Cards can be rendered in custom web or desktop applications using official SDKs:
- [Android](https://learn.microsoft.com/adaptive-cards/sdk/rendering-cards/android/getting-started)
- [iOS](https://learn.microsoft.com/adaptive-cards/sdk/rendering-cards/ios/getting-started)
- [JavaScript](https://learn.microsoft.com/adaptive-cards/sdk/rendering-cards/javascript/getting-started)
- [.NET](https://learn.microsoft.com/adaptive-cards/sdk/rendering-cards/net-html/getting-started)
- [React Native](https://learn.microsoft.com/adaptive-cards/sdk/rendering-cards/react-native/getting-started)

For advanced scenarios, developers can extend rendering logic or customize the schema.

- [Rendering SDKs – Getting Started](https://learn.microsoft.com/en-us/adaptive-cards/sdk/rendering-cards/getting-started)

---

## Implementation Steps

### Creating an Adaptive Card

1. **Define the Card Structure:**  
   Use the [Adaptive Card Designer](https://adaptivecards.microsoft.com/designer.html) or author JSON directly. Specify elements like `TextBlock`, `Image`, `Input`, etc.
2. **Validate the Card:**  
   Preview and validate your card using the visualizer in the designer.
3. **Integrate with the Target Host:**  
   Use the relevant SDK or follow platform-specific guides.

- [Adaptive Card Designer](https://adaptivecards.microsoft.com/designer.html)
- [Card Schema Reference](https://adaptivecards.io/explorer/)

### Integrating with Microsoft Teams via Power Automate

1. Create a new flow in Power Automate.
2. Add a trigger (e.g., new email, form submission).
3. Use the action “Post an Adaptive Card to a Teams user/channel and wait for a response.”
4. Paste or author the card JSON.
5. Map responses to subsequent actions in your flow.

- [Power Automate Integration](https://learn.microsoft.com/en-us/power-automate/overview-adaptive-cards)

### Custom Integration (SDKs)

Use official SDKs for:
- [Android](https://learn.microsoft.com/adaptive-cards/sdk/rendering-cards/android/getting-started)
- [iOS](https://learn.microsoft.com/adaptive-cards/sdk/rendering-cards/ios/getting-started)
- [JavaScript](https://learn.microsoft.com/adaptive-cards/sdk/rendering-cards/javascript/getting-started)
- [.NET](https://learn.microsoft.com/adaptive-cards/sdk/rendering-cards/net-html/getting-started)
- [React Native](https://learn.microsoft.com/adaptive-cards/sdk/rendering-cards/react-native/getting-started)

Parse and render Adaptive Cards in your app, or extend the schema/renderer for custom requirements.

- [SDKs for Rendering Cards](https://learn.microsoft.com/en-us/adaptive-cards/sdk/rendering-cards/getting-started)

---

## Best Practices

- **Use Templating:**  
  Utilize the [Adaptive Cards Templating Language](https://learn.microsoft.com/en-us/adaptive-cards/templating/language) to separate data from presentation.
- **Design for Adaptability:**  
  Avoid hardcoding visual details; let the host control styles.
- **Update Cards on Submission:**  
  Provide feedback and prevent duplicate submissions by updating cards post-interaction.
- **Validate User Input:**  
  Configure input fields and actions to capture and validate data effectively.
- **Test Across Hosts:**  
  Preview cards in all target environments for user experience consistency.

- [Design Best Practices](https://adaptivecards.microsoft.com/?topic=design-best-practices)

---

## Known Limitations

- Cards without "wait for a response" actions can only capture user input via URL clicks.
- Submit buttons on such cards error; only `OpenUrl` actions function.
- "Wait for a response" cards can be submitted once per instance.
- Only one container per card is allowed; multiple selection not supported.
- Some features (e.g., property translation prevention) require specific platform versions.
- Adaptive Cards may not be available in certain environments (e.g., DoD tenant in Power Automate).

- [Limitations & Host Support](https://adaptivecards.io/samples/)

---

## Tooling & Ecosystem

- **Designer:** [Adaptive Cards Designer](https://adaptivecards.microsoft.com/designer.html)
- **SDKs:** [SDKs for Major Platforms](https://learn.microsoft.com/en-us/adaptive-cards/sdk/rendering-cards/getting-started)
- **Template Service:** [Template Discovery and Exchange](https://learn.microsoft.com/en-us/adaptive-cards/templating)
- **Card Editor (DRUID):** [Adaptive Cards Editor](https://docs.druidai.com/1385954/Content/4_Flows/Adaptive%20Cards%20Steps.htm#Adaptive_Card_Editor)
- **GitHub:** [Adaptive Cards GitHub](https://github.com/microsoft/AdaptiveCards/)
- **Documentation Hub:** [Adaptive Cards Documentation Hub](https://adaptivecards.microsoft.com)
- **Community & Examples:** [Adaptive Cards Official Site](https://adaptivecards.io/)

---

## Quotes & Testimonials

> “Microsoft Teams is only as powerful as the third-party services that integrate with it. Adaptive Cards allows any developer to plug into the richness of the Teams platform in a native way.”  
> — Bill Bliss, Platform Architect

> “AtBot helps anyone write a bot without having to write code. By embedding the Adaptive Card designer directly into our web-based portal, our customers can create rich, data-bound cards right from the browser.”  
> — Joe Herres, Co-CEO

> “User engagement on surveys is always a challenge, but after utilizing Outlook Actionable Messages, our return rate surged from 10-12% to a 3 month average of 35%!”  
> — Richard Greenfield, Executive Support Services

---

## Visual Aids: Examples & JSON Snippets

### Example 1: Simple Welcome Card
```json
{
  "type": "AdaptiveCard",
  "version": "1.4",
  "body": [
    {
      "type": "TextBlock",
      "text": "Welcome, John!",
      "weight": "Bolder",
      "size": "Large"
    },
    {
      "type": "Image",
      "url": "https://adaptivecards.io/content/cats/2.png",
      "size": "Medium"
    }
  ],
  "actions": [
    {
      "type": "Action.OpenUrl",
      "title": "View Dashboard",
      "url": "https://contoso.com/dashboard"
    }
  ]
}
```

### Example 2: Collect User Feedback
```json
{
  "type": "AdaptiveCard",
  "version": "1.4",
  "body": [
    {
      "type": "TextBlock",
      "text": "Please rate your recent experience:",
      "wrap": true
