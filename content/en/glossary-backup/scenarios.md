---
title: Scenarios (Pre-Prepared Conversation Flows)
date: 2025-12-17
translationKey: scenarios-pre-prepared-conversation-flows
description: Explore scenarios (chatbot scripts) in AI chatbot and automation systems.
  Learn their definition, structure (blocks, events, actions), creation process, and
  benefits for businesses.
keywords:
- scenario
- chatbot
- automation
- conversation flow
- AI
category: AI Chatbot & Automation
type: glossary
draft: false
---

## Definition of Scenarios

A **scenario** (also known as a chatbot script, bot story, or conversation flow) is a pre-prepared, structured path of interactions between a user and an AI-powered automation system. It comprises a sequence of conversational steps, logic, and actions that define how the chatbot responds to user input, manages data, and executes operations to reach a desired outcome.

In practical terms, scenarios are constructed in visual or code-based workflow builders, where modular blocks (event listeners, actions, conditions, exits) are connected to form dynamic, interactive experiences. Scenarios are fundamental to the operation of modern AI chatbots and automation platforms, dictating the logic and responses that guide user interaction across digital channels.

- [What’s a chatbot script? (chatbot.com)](https://www.chatbot.com/blog/chatbot-script/)
- [Chatbot Architecture Explained (marutitech.com)](https://marutitech.com/chatbots-work-guide-chatbot-architecture/)

## Conceptual Overview

Scenarios are the backbone of chatbot automation, providing the logic and branching required for meaningful, context-aware conversations. They bridge the gap between static, FAQ-style bots and true conversational agents capable of simulating human-like interactions.

Scenarios are closely related to—but distinct from—user stories and use cases:

### Scenarios vs. User Stories vs. Use Cases

| Aspect         | Scenario                                                                                                            | User Story                                                                                  | Use Case                                                                                      |
|----------------|--------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| **Definition** | Predefined path (flow) of interactions between user and system, implemented in automation/chatbot                   | Short, simple description of a feature from the user's perspective (often in Agile)          | Technical specification of all possible interactions between role and system to achieve goal  |
| **Format**     | Visual map or flowchart (blocks, branches, conditions, actions)                                                     | Text card: "As a [user], I want [goal], so that [outcome]."                                 | Stepwise text, includes main and alternate flows, error conditions                            |
| **Detail**     | Step-by-step, including actions, conditions, data capture, and system responses                                     | Brief, high-level                                                                           | Comprehensive, covers all variations                                                          |
| **Purpose**    | Guide actual automated conversation or process                                                                      | Capture a requirement or feature to implement                                               | Specify system requirements and responses                                                     |
| **User Focus** | Centered on user behavior and system automation, often tied to user personas or roles                               | User-centric, but abstract                                                                  | System-centric, technical                                                                     |

**Example:**
- *Scenario:* Outlines the exact sequence by which a chatbot greets a visitor, requests their email, validates input, and routes the conversation.
- *User Story:* "As a new visitor, I want to get product support so that I can resolve my issue quickly."
- *Use Case:* Lists every possible interaction and error for product support, including invalid email handling and escalation paths.

Additional reading:
- [What are User Scenarios? (Interaction Design Foundation)](https://www.interaction-design.org/literature/topics/user-scenarios)
- [Design Scenarios – Communicating the Small Steps (Interaction Design Foundation)](https://www.interaction-design.org/literature/topics/scenarios)

## Structure of a Scenario

A scenario is composed of interconnected **blocks**, each representing a discrete function or step within the conversation flow. The main block types are:

### Entry Gate

- **Purpose:** Marks the starting point of the scenario. The first block after the Entry Gate typically determines the trigger (user message, event, etc.).
- **Definition:** Without an Entry Gate, a scenario cannot be activated or executed.

### Event Blocks

Event Blocks listen for specific triggers or events that pause or resume the scenario, including:

- **New User Message:** Detects any incoming message (text, image, file).
- **User Message Matches:** Detects messages matching keywords, phrases, or intent patterns.
- **Button/Input Action:** Detects user interactions with buttons, forms, or input fields.
- **Conversation State Changed:** Tracks changes in the chat’s status (pending, resolved, etc.).
- **User Profile Updated:** Triggers on updates to user data (email, name, phone).
- **Custom Data Updated:** Triggers when particular backend data fields change.
- **Segments Updated:** Listens for changes in user or conversation segments.
- **URL Change Detected:** Triggers when the user navigates to a specified link.
- **New Crisp Event:** Activates via programmatic event (e.g., SDK calls).
- **Awaiting Operator:** Triggers if a user message remains unread for a fixed interval.

**Example:** Use a "New User Message" event to begin a support flow when any message is received.

**Further reading:** [Chatbot Event Triggers – Chatbot.com Documentation](https://www.chatbot.com/help/)

### Action Blocks

Action Blocks execute operations within the scenario:

- **Send Message:** Outputs text, buttons, carousels, images, files, or notes.
    - *Types:* Text, Button Picker, Field Input, File Attachment, Animation (GIF), Carousel, Private Note.
- **Update User:** Modifies user data fields (name, email, phone, custom fields, segments).
- **Internal Actions:** Changes conversation state, assigns operators, blocks users, triggers webhooks.
- **AI Actions:** Integrates AI for intent analysis, knowledge base search, or dynamic replies.

**Example:** "Send Message > Button Picker" presents options; "Field Input" collects an email.
### Condition Blocks

Condition Blocks evaluate data or context to branch the flow:

- **Conversation is New:** Checks if the conversation is just starting.
- **Time Passed Since:** Evaluates the elapsed time from a specific event.
- **Segments/Custom Data:** Checks user/conversation data or segments.
- **User Profile Checks:** Evaluates if user email, name, or phone is set.
- **User Metadata:** Branches by location, language, hour, day.
- **Conversation State/Channel/Inbox:** Directs flow based on status or channel.
- **Message Intent Matches:** Uses AI to evaluate intent.
- **HTTP Response Matches:** Branches based on API/webhook responses.

**Example:** Use "User Email is Set" to check if email is available before proceeding.

### Exit Blocks

Exit Blocks end or hand off the scenario:

- **Stop Scenario:** Terminates the current flow.
- **Run Scenario:** Launches another scenario, enabling modular automation.

**Note:** Not every scenario requires an explicit exit block, but they are vital for organizing complex automation.

## How Scenarios Are Used

Scenarios orchestrate automation across use cases:

- Customer support and ticketing
- Lead generation and qualification
- Information gathering and customer onboarding
- Automated troubleshooting and FAQ resolution
- Order tracking and notifications
- Employee self-service, HR workflows

Scenarios are executed via web chat, email, messaging apps (WhatsApp, Telegram), and mobile. They are also used for backend automation, such as updating CRM records or triggering notifications.

### Scenario Examples and Use Cases

#### Example 1: Email Collection Scenario

**Purpose:** Gather a user’s email during a chat.

**Flow:**
1. Entry Gate
2. Send Message: "Welcome! To assist you, may I have your email address?"
3. Field Input (email), requiring a selection to continue
4. Button/Input Action: Listens for user response
5. Update User Email: Stores the email
6. Condition: Checks if email is set
7. Send Message: "Thank you! How may I assist you today?"

**Tip:** Always use an Event block after input to pause/resume and store values.

#### Example 2: FAQ Resolution Scenario

**Purpose:** Automate answers to common questions.

**Flow:**
1. Entry Gate
2. User Message Matches Event: Detects patterns (e.g., "*refund*")
3. AI Action: Searches knowledge base for answer
4. Send Message: Delivers answer or escalation steps

**Tip:** Use wildcards for broad pattern matching.

#### Example 3: Multichannel Welcome Scenario

**Purpose:** Greet users differently by channel.

**Flow:**
1. Entry Gate
2. New User Message: Detects channel
3. Condition: "Current Channel is WhatsApp"
    - If true: "Welcome, WhatsApp user!"
    - Else: "Welcome! How can we help you?"

**More examples:** [Chatbot Script Examples (chatbot.com)](https://www.chatbot.com/blog/chatbot-script/#chatbot-script-examples)

## Scenario Creation Process

### Step-by-Step Guide

1. **Define Objective:** State what the scenario should accomplish (e.g., collect user data, answer a FAQ).
2. **Map User Flow:** Outline the sequence of events, user actions, and system responses; use personas for realism.
3. **Build with Blocks:**
    - Start with Entry Gate.
    - Add Event Blocks to trigger the scenario.
    - Insert Action Blocks for outputs and operations.
    - Use Condition Blocks for branching.
    - Optionally, add Exit Blocks.
4. **Configure Each Block:**
    - Set triggers, patterns, and channels (Event Blocks).
    - Specify message types and variables (Action Blocks).
    - Define conditions and comparison ops (Condition Blocks).
    - Configure data collection and variable storage.
5. **Test the Scenario:** Simulate all branches and validate data capture, logic, and responses.
6. **Iterate and Refine:** Gather user/stakeholder feedback and improve flow, messages, and logic.

### Configuration Options

- **Message Origins/Channels:** Filter events by channel (web, email, WhatsApp, etc.).
- **Pattern Matching:** Use exact/wildcard matches to detect intent.
- **Data Memorization:** Store inputs in variables or fields.
- **Localization:** Present messages in multiple languages.
- **Branching Logic:** Personalize by user data or context.
- **API/Webhook Integration:** Trigger backend ops and resume scenarios on completion.

**Warning:** Chaining multiple "Awaiting Operator" blocks does not extend waiting period (fixed duration). Avoid redundant blocks to prevent logic errors.

## Best Practices

- **User-Centric Design:** Build flows around real user goals and behaviors; leverage personas.
- **Clarity and Simplicity:** Use clear, concise messaging; avoid jargon.
- **Modularity:** Split complex processes into reusable scenarios; use exit/run scenario blocks.
- **Explicit Data Capture:** Validate and confirm all user inputs before proceeding.
- **Error Handling:** Plan for invalid inputs, timeouts, and unexpected branches.
- **Testing:** Test across all supported channels and edge cases.
- **Localization:** Provide multi-language support as needed.

### Common Pitfalls and Warnings

- **Neglecting Branches:** Failing to handle all user responses can cause dead ends.
- **Overcomplicating Flows:** Excessive branching reduces maintainability.
- **Missing Event Block After Input:** Always pair inputs with event blocks to pause/resume and store values.
- **Not Updating User Data:** Ensure captured data is saved and used for personalization.
- **Ignoring Privacy and Security:** Avoid collecting sensitive data unless necessary; ensure compliance.

## Benefits of Scenarios

### For Users

- **Consistent Experience:** Predictable, reliable responses and journey.
- **Personalization:** Flows adapt to user data and context.
- **Faster Resolution:** Automation reduces wait times and accelerates solutions.

### For Businesses

- **Scalability:** Automate frequent tasks, reducing manual effort.
- **Data Collection:** Capture structured user data for CRM and analytics.
- **Quality Assurance:** Standardized flows ensure compliance and consistency.
- **Continuous Improvement:** Data/feedback enable ongoing optimization.

## Glossary of Key Terms

| Term                        | Definition                                                                                                 |
|-----------------------------|------------------------------------------------------------------------------------------------------------|
| **Scenario**                | Pre-prepared conversation flow in a chatbot or automation system, built from modular blocks.               |
| **Block**                   | Discrete unit of logic/function within a scenario (Event, Action, Condition, Exit).                        |
| **Entry Gate**              | Starting point of a scenario flow.                                                                         |
| **Event Block**             | Triggers scenario progression based on user/system events.                                                 |
| **Action Block**            | Executes actions (e.g., send message, update user data, call API).                                         |
| **Condition Block**         | Evaluates data or state to branch scenario flow.                                                           |
| **Exit Block**              | Ends or hands off scenario flow.                                                                           |
| **User Scenario**           | Narrative describing user behavior, goals, and context within a system (often used for design/UX).         |
| **User Story**              | Short, high-level requirement from user’s perspective (Agile development).                                 |
| **Use Case**                | Formal description of all ways a user interacts with a system to achieve a goal.                           |
| **Persona**                 | Archetype representing a user segment, used to inform scenario design.                                     |
| **Pattern Matching**        | Detecting keywords or phrases in user messages to trigger scenario logic.                                  |
| **Memorization**            | Storing collected user data (e.g., email, name) within the scenario for later use.                         |

## References

1. [Chatbot.com: How to Write a Chatbot Script – Examples Included](https://www.chatbot.com/blog/chatbot-script/)
2. [Marutitech: How do Chatbots Work? A Guide to Chatbot Architecture](https://marutitech.com/chatbots-work-guide-chatbot-architecture/)
3. [Interaction Design Foundation: What are User Scenarios?](https://www.interaction-design.org/literature/topics/user-scenarios)
4. [Interaction Design Foundation: Design Scenarios – Communicating the Small Steps](https://www.interaction-design.org/literature/topics/scenarios)
5. [Make.com: Scenarios for AI agents – Help Center](https://www.make.com/en/help/scenarios)
6. [Zendesk: Was ist ein Chatbot? Funktionen & Vorteile im Überblick](https://www.zendesk.de/blog/chatbot-vorteile/)
7. Additional documentation and best practices from respective AI chatbot and automation platforms.

**Further Reading & Resources:**

- [Chatbot.com Documentation](https://www.chatbot.com/help/)
- [OpenAI: Chatbot Best Practices](https://platform.openai.com/docs/guides/gpt)
- [YouTube: How to Create a Chatbot Flow](https://www.youtube.com/results?search_query=how+to+create+chatbot+flow)
- [Make.com: Scenarios Overview](https://www.make.com/en/help/scenarios)

This glossary provides a comprehensive, actionable reference for anyone designing, building, or maintaining AI chatbot and automation scenarios. For practical tutorials and in-depth guides, explore the referenced articles and documentation above.

