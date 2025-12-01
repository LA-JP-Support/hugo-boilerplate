---
title: "Adaptive Cards"
translationKey: "adaptive-cards"
description: "Adaptive Cards are platform-agnostic, declarative UI snippets authored in JSON for exchanging and rendering rich, interactive content across various applications and services."
keywords: ["Adaptive Cards", "JSON", "Microsoft Teams", "Power Automate", "UI"]
category: "AI Chatbot & Automation"
type: "glossary"
draft: false
---


## **1. What Are Adaptive Cards?**

Adaptive Cards are a standardized, open-source, declarative framework for authoring UI cards using JSON. A card’s JSON describes the structure, content, styling, and interactivity (e.g., forms, buttons, images, text). When delivered to a host app, the card is rendered natively, adopting the host’s theme, fonts, interaction style, and accessibility features.

**Key Characteristics:**
- **Platform Agnostic:** Write once, use everywhere.
- **Declarative:** UI is described in JSON, not code.
- **Native Rendering:** Host apps render cards using their own controls and styles.
- **Interactivity:** Includes actionable elements (buttons, forms, inputs).

**Examples:**
- Task assignment cards in Microsoft Teams, featuring summary, description, and actionable buttons.
- Approval workflows in Outlook, where managers can approve or reject requests directly from their inbox.

**Why Use Adaptive Cards?**
- **Consistency:** Uniform user experience across platforms.
- **Efficiency:** Single card definition for multiple hosts.
- **Interactivity:** Enables actionable content and rich data collection.
- **Accessibility:** Supports adaptive styling for accessibility and dark mode.

**References:**
- [Official Adaptive Cards Documentation Hub](https://adaptivecards.microsoft.com/)
- [Adaptive Cards Overview - Microsoft Learn](https://learn.microsoft.com/en-us/adaptive-cards/)

## **2. Architecture: How Adaptive Cards Work**

### **2.1. Authoring**
- **Card Author:** Creates cards using the standardized JSON schema, defining layout, content, and available actions.
- **Schema:** Supports a wide range of elements, such as TextBlock, Image, FactSet, Input.Text, Input.ChoiceSet, and action types like Action.OpenUrl, Action.Submit, Action.Execute.

**Example JSON:**
```json
{
  "type": "AdaptiveCard",
  "version": "1.5",
  "body": [
    { "type": "TextBlock", "text": "Task Assigned", "weight": "Bolder", "size": "Medium" },
    { "type": "TextBlock", "text": "You have a new task: Review Q2 Report." }
  ],
  "actions": [
    { "type": "Action.OpenUrl", "title": "View Task", "url": "https://contoso.com/tasks/123" }
  ]
}
```
- See the [Adaptive Cards Schema Explorer](https://adaptivecards.io/explorer/) for a complete list of supported elements.

### **2.2. Delivery and Hosting**
- **Host Application:** Receives the card JSON, parses it, and renders it natively.
- **Supported Hosts:** Microsoft Teams, Outlook, Power Automate, Windows Timeline, web/mobile apps, and the Microsoft Bot Framework.
- **Rendering:** The host interprets the card JSON, applies its own visual language (colors, fonts, spacings), and displays the card as part of its UI.

**Reference:**  
- [Adaptive Cards: How it Works](https://adaptivecards.io/)

### **2.3. Adaptation**
- **Automatic Styling:** Cards automatically adapt to the host’s style, including dark mode and accessibility settings.
- **Native Controls:** Inputs and buttons use the host’s native UI elements for a seamless experience.

### **2.4. Interactivity**
- **Actions:** Cards support various interactive actions:
  - Action.OpenUrl: Open a link.
  - Action.Submit: Submit data (form inputs).
  - Action.Execute (Universal Actions): Unified handling across Teams and Outlook.
- **Data Collection:** User input is processed by bots, Power Automate flows, or custom app handlers.  
  - See [Universal Actions for Adaptive Cards](https://learn.microsoft.com/en-us/microsoftteams/platform/task-modules-and-cards/cards/universal-actions-for-adaptive-cards/overview).

**Diagram Description:**  
A bot sends a card’s JSON to Teams. Teams renders it as a native card, styled like Teams, and users interact directly in the app. Actions trigger backend processes or update the card.

## **3. Key Features and Design Principles**

### **3.1. Core Features**
- **Portability:** One card definition for all platforms (Teams, Outlook, web, mobile, etc.).
- **Declarative:** Entire UI and interaction described in JSON.
- **Open Source:** Community-driven with SDKs for major platforms ([GitHub](https://github.com/microsoft/AdaptiveCards/)).
- **Reusable:** Same card payload can be reused and templated.
- **Expressive:** Supports text, images, media, complex layouts, inputs, and multiple action types.
- **Safe:** No executable code or scripting is allowed in cards.
- **Consistent Experience:** Host controls look and feel for native integration.

### **3.2. Design Principles**
- **Content Ownership:** Card authors define content; hosts control appearance.
- **Semantic Layout:** Focus on logical information structure over pixel-perfect layouts.
- **Simplicity:** Avoid unnecessary complexity; emphasize clarity and purpose.
- **Extensibility:** Developers can extend with custom elements as needed, but should prefer standard schema for cross-platform consistency.
- **Universal Schema:** One JSON format for all supported hosts.

**Feature Table:**
| Feature         | Description                                                                                   |
|-----------------|----------------------------------------------------------------------------------------------|
| Portability     | Cards work on Teams, Outlook, web, mobile, and more.                                         |
| Declarative     | JSON-based, no code for UI logic.                                                            |
| Openness        | Open-source SDKs, community templates, transparent roadmap.                                  |
| Consistency     | Host apps control visual style, ensuring a native feel.                                      |
| Interactivity   | Supports input fields, buttons, and inline actions.                                          |
| Reusability     | Same card can be used in multiple flows and platforms.                                       |
| Security        | Declarative only, no scripting or unsafe markup.                                             |

**References:**  
- [Designing Adaptive Cards for Teams](https://learn.microsoft.com/en-us/microsoftteams/platform/task-modules-and-cards/cards/design-effective-cards)  
- [Adaptive Cards Design Best Practices](https://adaptivecards.microsoft.com/?topic=design-best-practices)

## **4. Core Use Cases and Examples**

Adaptive Cards are pivotal in business process automation, conversational AI bots, actionable messaging, workflow approvals, and custom app dashboards.

### **4.1. Business Process Automation**
**Scenario:**  
A CRM creates a new sales lead. Power Automate triggers a card in the Teams Sales channel, showing lead info and action buttons (“Assign”, “Contact”). A sales manager clicks “Assign”, submits the card, and the CRM is updated via the flow.

**References:**  
- [Adaptive Cards in Power Automate](https://learn.microsoft.com/en-us/power-automate/overview-adaptive-cards)

### **4.2. AI Chatbots**
**Scenario:**  
A helpdesk bot presents an Adaptive Card with an issue submission form in Teams or web chat. User fills in details, submits, and the bot processes the input, responding with a confirmation card.

**References:**  
- [Bot Framework Adaptive Cards Reference](https://docs.microsoft.com/microsoftteams/platform/concepts/cards/cards-reference#adaptive-card)

### **4.3. Actionable Emails in Outlook**
**Scenario:**  
Managers receive expense approval cards in Outlook. The card displays expense details and action buttons (Approve/Reject). The manager acts directly from their email.

**References:**  
- [Adaptive Cards for Outlook Actionable Messages](https://learn.microsoft.com/en-us/outlook/actionable-messages/adaptive-card)

### **4.4. Automating Workflows with Power Automate**
**Scenario:**  
Adaptive Cards are posted in Teams channels for feedback. The flow waits until a response is received, then processes the input and continues.

### **4.5. Additional Use Cases**
- **Notifications:** System events, escalations, deadlines.
- **Surveys and Polls:** Structured user feedback.
- **Status Updates:** Task, delivery, or incident status.
- **Third-party Integrations:** Bringing external data into Teams/Outlook.

**Reference:**  
- [Adaptive Cards Use Cases](https://adaptivecards.io/)

## **5. Implementation: Authoring and Deploying Adaptive Cards**

### **5.1. Designing Cards**
- Use the [Adaptive Cards Designer](https://adaptivecards.io/designer) for drag-and-drop card creation, JSON preview, and data binding.
- Preview how cards render in Teams, Outlook, Web, and other hosts.
- Access [templates and samples](https://github.com/OfficeDev/Microsoft-Teams-Adaptive-Card-Samples/tree/main) for rapid development.

### **5.2. Authoring JSON**
- Manually craft JSON or use the designer to export it.
- Leverage [templating](https://adaptivecards.io/designer/#templating) for dynamic data binding.

### **5.3. Deploying Cards**
- **Power Automate:**  
  - Use actions such as “Post adaptive card and wait for response”.
  - Cards can be sent to users or channels; workflow continues after response.
  - [Overview of Adaptive Cards in Power Automate](https://learn.microsoft.com/en-us/power-automate/overview-adaptive-cards)

- **Bot Framework:**  
  - Bots send and process Adaptive Cards in conversations.
  - Adaptive Cards support updates, refreshes, and sequential workflows.

- **Outlook Actionable Messages:**  
  - Send Adaptive Cards in emails for embedded approval, notification, or survey actions.
  - [Outlook Adaptive Cards](https://docs.microsoft.com/outlook/actionable-messages/adaptive-card)

- **Custom Apps:**  
  - Use SDKs for JavaScript, .NET, Android, iOS, and React Native to render cards in any app.
  - [SDKs and Platform Integrations](https://adaptivecards.io/#platforms)

## **6. Integration with Microsoft Teams, Power Automate, Outlook, and More**

### **6.1. Microsoft Teams**
- Cards can be sent as bots or via Power Automate to users, chats, or channels.
- Supports light/dark themes, accessibility, and native styling.
- [Designing Effective Cards for Teams](https://learn.microsoft.com/en-us/microsoftteams/platform/task-modules-and-cards/cards/design-effective-cards)

### **6.2. Power Automate**
- Actions for posting cards to users/channels, waiting for responses, collecting input, and driving workflows.
- Dynamic content from flows can be inserted in cards.
- [Power Automate Adaptive Cards Guide](https://learn.microsoft.com/en-us/power-automate/overview-adaptive-cards)

### **6.3. Outlook**
- Actionable Messages powered by Adaptive Cards.
- Users can approve/reject, provide feedback, or trigger flows from their inbox.
- [Outlook Actionable Messages](https://docs.microsoft.com/outlook/actionable-messages/adaptive-card)

### **6.4. Bot Framework**
- Bots can send Adaptive Cards interactively in Teams, web chat, and other channels.
- [Bot Framework Adaptive Cards](https://docs.microsoft.com/microsoftteams/platform/concepts/cards/cards-reference#adaptive-card)

### **6.5. Web and Custom Apps**
- SDKs for [JavaScript](https://docs.microsoft.com/adaptive-cards/sdk/rendering-cards/javascript/getting-started), [.NET](https://docs.microsoft.com/adaptive-cards/sdk/rendering-cards/net-html/getting-started), [Android](https://docs.microsoft.com/adaptive-cards/sdk/rendering-cards/android/getting-started), and [iOS](https://docs.microsoft.com/adaptive-cards/sdk/rendering-cards/ios/getting-started).
- Embed cards in any dashboard, portal, or UI.

## **7. Developer Tools and SDKs**

- **Visual Designer:** [Adaptive Cards Designer](https://adaptivecards.io/designer)
- **SDKs:**
  - [JavaScript](https://docs.microsoft.com/adaptive-cards/sdk/rendering-cards/javascript/getting-started)
  - [.NET / ASP.NET / WPF](https://docs.microsoft.com/adaptive-cards/sdk/rendering-cards/net-html/getting-started)
  - [Android](https://docs.microsoft.com/adaptive-cards/sdk/rendering-cards/android/getting-started)
  - [iOS](https://docs.microsoft.com/adaptive-cards/sdk/rendering-cards/ios/getting-started)
  - [React Native](https://docs.microsoft.com/adaptive-cards/sdk/rendering-cards/react-native/getting-started)
- **Templating Service:** Separate data from layout for reusable cards.
- **REST APIs:** Deliver cards/templates from backend services.
- **Open Source Repository:** [AdaptiveCards on GitHub](https://github.com/microsoft/AdaptiveCards/)

## **8. Known Limitations**

- **Host Capabilities:** Some hosts may not support all schema features (e.g., certain input types or actions).
- **Data Submission:** Action.Submit can only be used in “wait for response” flows in Power Automate.
- **Single Submission:** Cards in “wait for response” mode are single-use; after submission, further attempts are ignored unless updated.
- **Update Message Requirement:** Prevent duplicate submissions by updating the card post-submission.
- **No Custom JavaScript/CSS:** Hosts control all styling and scripting; custom code is disallowed.
- **DoD Environment:** Adaptive Cards are not available in some government (Department of Defense) environments.
- **Refresh Constraints:** Inconsistent refresh behavior for anonymous users or certain hosts ([source](https://learn.microsoft.com/en-us/answers/questions/2281334/inconsistent-adaptive-card-refresh-behavior-for-an)).
- **Universal Actions Model:** Not every scenario is compatible with Action.Execute; some messaging extension scenarios require Action.Submit ([Universal Actions for Adaptive Cards](https://learn.microsoft.com/en-us/microsoftteams/platform/task-modules-and-cards/cards/universal-actions-for-adaptive-cards/overview)).

## **9. Best Practices**

- **Design for Host Adaptation:** Avoid pixel-perfect layouts; embrace host-controlled styling.
- **Use Update Messages:** Configure “replacement” messages after submission to prevent duplicate actions.
- **Prefer Universal Actions:** Use Action.Execute for broadest compatibility in Teams and Outlook.
- **Keep Cards Simple:** Include only essential information and actions; avoid overcrowding.
- **Test Across Hosts:** Use the Designer to preview cards for all intended platforms.
- **Secure Data Handling:** Never include sensitive information directly in cards; host apps may log or cache data.
- **Accessibility:** Use semantic elements and text alternatives for screen reader compatibility.
- **Leverage Templates and UI Kits:** Use the [Microsoft Teams UI Kit (Figma)](https://www.figma.com/community/file/916836509871353159) and the [Adaptive Card templates](https://github.com/OfficeDev/Microsoft-Teams-Adaptive-Card-Samples/tree/main) for rapid, accessible card design.

## **10. Related Concepts and Terms**

- **JSON Object:** The data structure used to describe Adaptive Cards.
- **Host Application:** Teams, Outlook, or any app rendering the card.
- **Bot Framework:** SDK for building conversational bots delivering cards.
- **Power Automate:** Platform for triggering and posting Adaptive Cards as part of workflows.
- **Rendering:** Host-side process of parsing and displaying the card from JSON.
- **Templating:** Separating card structure from dynamic data for reusability.
- **Actionable Content:** UI elements (buttons, forms) enabling user interaction.
- **Universal Action Model:** Unified action handling across hosts using Action.Execute.

## **11. Frequently Asked Questions**

**Q: What is an Adaptive Card?**  
A: A JSON-defined UI card rendered natively by host applications, delivering interactive experiences across platforms.

**Q: Where can Adaptive Cards be used?**  
A: Microsoft Teams, Outlook, Power Automate, Bot Framework, web apps, mobile apps, and any app supporting the SDK.

**Q: How do I create an Adaptive Card?**  
A: Use the [Adaptive Cards Designer](https://adaptivecards.io/designer) or author JSON manually.

**Q: Can I collect input from users?**  
A: Yes, cards support input fields, choice sets, and toggles. Submissions are processed by bots, flows, or handlers.

**Q: Are Adaptive Cards secure?**  
A: Yes; they are declarative with no custom scripts, reducing attack surfaces.

**Q: Can cards be updated or refreshed?**  
A: Yes, use update messages or refresh actions to update card content after submission.

**Q: What are common limitations?**  
A: Feature support varies by host; data submission and styling are host-controlled; no custom code is allowed.

## **12. Related Resources**

- [Official Adaptive Cards Documentation Hub](https://adaptivecards.microsoft.com/)
- [Adaptive Cards Designer](https://adaptivecards.io/designer)
- [Microsoft Learn: Adaptive Cards Overview](https://learn.microsoft.com/en-us/adaptive-cards/)
- [Power Automate Adaptive Cards](https://learn.microsoft

