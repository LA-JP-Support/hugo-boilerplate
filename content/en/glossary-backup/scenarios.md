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

A <strong>scenario</strong>(also known as a chatbot script, bot story, or conversation flow) is a pre-prepared, structured path of interactions between a user and an AI-powered automation system. It comprises a sequence of conversational steps, logic, and actions that define how the chatbot responds to user input, manages data, and executes operations to reach a desired outcome.

In practical terms, scenarios are constructed in visual or code-based workflow builders, where modular blocks (event listeners, actions, conditions, exits) are connected to form dynamic, interactive experiences. Scenarios are fundamental to the operation of modern AI chatbots and automation platforms, dictating the logic and responses that guide user interaction across digital channels.

- [What’s a chatbot script? (chatbot.com)](https://www.chatbot.com/blog/chatbot-script/)
- [Chatbot Architecture Explained (marutitech.com)](https://marutitech.com/chatbots-work-guide-chatbot-architecture/)

## Conceptual Overview

Scenarios are the backbone of chatbot automation, providing the logic and branching required for meaningful, context-aware conversations. They bridge the gap between static, FAQ-style bots and true conversational agents capable of simulating human-like interactions.

Scenarios are closely related to—but distinct from—user stories and use cases:

### Scenarios vs. User Stories vs. Use Cases

| Aspect         | Scenario                                                                                                            | User Story                                                                                  | Use Case                                                                                      |
|----------------|--------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| <strong>Definition</strong>| Predefined path (flow) of interactions between user and system, implemented in automation/chatbot                   | Short, simple description of a feature from the user's perspective (often in Agile)          | Technical specification of all possible interactions between role and system to achieve goal  |
| <strong>Format</strong>| Visual map or flowchart (blocks, branches, conditions, actions)                                                     | Text card: "As a [user], I want [goal], so that [outcome]."                                 | Stepwise text, includes main and alternate flows, error conditions                            |
| <strong>Detail</strong>| Step-by-step, including actions, conditions, data capture, and system responses                                     | Brief, high-level                                                                           | Comprehensive, covers all variations                                                          |
| <strong>Purpose</strong>| Guide actual automated conversation or process                                                                      | Capture a requirement or feature to implement                                               | Specify system requirements and responses                                                     |
| <strong>User Focus</strong>| Centered on user behavior and system automation, often tied to user personas or roles                               | User-centric, but abstract                                                                  | System-centric, technical                                                                     |

<strong>Example:</strong>- *Scenario:* Outlines the exact sequence by which a chatbot greets a visitor, requests their email, validates input, and routes the conversation.
- *User Story:* "As a new visitor, I want to get product support so that I can resolve my issue quickly."
- *Use Case:* Lists every possible interaction and error for product support, including invalid email handling and escalation paths.

Additional reading:
- [What are User Scenarios? (Interaction Design Foundation)](https://www.interaction-design.org/literature/topics/user-scenarios)
- [Design Scenarios – Communicating the Small Steps (Interaction Design Foundation)](https://www.interaction-design.org/literature/topics/scenarios)

## Structure of a Scenario

A scenario is composed of interconnected <strong>blocks</strong>, each representing a discrete function or step within the conversation flow. The main block types are:

### Entry Gate

- <strong>Purpose:</strong>Marks the starting point of the scenario. The first block after the Entry Gate typically determines the trigger (user message, event, etc.).
- <strong>Definition:</strong>Without an Entry Gate, a scenario cannot be activated or executed.

### Event Blocks

Event Blocks listen for specific triggers or events that pause or resume the scenario, including:

- <strong>New User Message:</strong>Detects any incoming message (text, image, file).
- <strong>User Message Matches:</strong>Detects messages matching keywords, phrases, or intent patterns.
- <strong>Button/Input Action:</strong>Detects user interactions with buttons, forms, or input fields.
- <strong>Conversation State Changed:</strong>Tracks changes in the chat’s status (pending, resolved, etc.).
- <strong>User Profile Updated:</strong>Triggers on updates to user data (email, name, phone).
- <strong>Custom Data Updated:</strong>Triggers when particular backend data fields change.
- <strong>Segments Updated:</strong>Listens for changes in user or conversation segments.
- <strong>URL Change Detected:</strong>Triggers when the user navigates to a specified link.
- <strong>New Crisp Event:</strong>Activates via programmatic event (e.g., SDK calls).
- <strong>Awaiting Operator:</strong>Triggers if a user message remains unread for a fixed interval.

<strong>Example:</strong>Use a "New User Message" event to begin a support flow when any message is received.

<strong>Further reading:</strong>[Chatbot Event Triggers – Chatbot.com Documentation](https://www.chatbot.com/help/)

### Action Blocks

Action Blocks execute operations within the scenario:

- <strong>Send Message:</strong>Outputs text, buttons, carousels, images, files, or notes.
    - *Types:* Text, Button Picker, Field Input, File Attachment, Animation (GIF), Carousel, Private Note.
- <strong>Update User:</strong>Modifies user data fields (name, email, phone, custom fields, segments).
- <strong>Internal Actions:</strong>Changes conversation state, assigns operators, blocks users, triggers webhooks.
- <strong>AI Actions:</strong>Integrates AI for intent analysis, knowledge base search, or dynamic replies.

<strong>Example:</strong>"Send Message > Button Picker" presents options; "Field Input" collects an email.
### Condition Blocks

Condition Blocks evaluate data or context to branch the flow:

- <strong>Conversation is New:</strong>Checks if the conversation is just starting.
- <strong>Time Passed Since:</strong>Evaluates the elapsed time from a specific event.
- <strong>Segments/Custom Data:</strong>Checks user/conversation data or segments.
- <strong>User Profile Checks:</strong>Evaluates if user email, name, or phone is set.
- <strong>User Metadata:</strong>Branches by location, language, hour, day.
- <strong>Conversation State/Channel/Inbox:</strong>Directs flow based on status or channel.
- <strong>Message Intent Matches:</strong>Uses AI to evaluate intent.
- <strong>HTTP Response Matches:</strong>Branches based on API/webhook responses.

<strong>Example:</strong>Use "User Email is Set" to check if email is available before proceeding.

### Exit Blocks

Exit Blocks end or hand off the scenario:

- <strong>Stop Scenario:</strong>Terminates the current flow.
- <strong>Run Scenario:</strong>Launches another scenario, enabling modular automation.

<strong>Note:</strong>Not every scenario requires an explicit exit block, but they are vital for organizing complex automation.

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

<strong>Purpose:</strong>Gather a user’s email during a chat.

<strong>Flow:</strong>1. Entry Gate
2. Send Message: "Welcome! To assist you, may I have your email address?"
3. Field Input (email), requiring a selection to continue
4. Button/Input Action: Listens for user response
5. Update User Email: Stores the email
6. Condition: Checks if email is set
7. Send Message: "Thank you! How may I assist you today?"

<strong>Tip:</strong>Always use an Event block after input to pause/resume and store values.

#### Example 2: FAQ Resolution Scenario

<strong>Purpose:</strong>Automate answers to common questions.

<strong>Flow:</strong>1. Entry Gate
2. User Message Matches Event: Detects patterns (e.g., "*refund*")
3. AI Action: Searches knowledge base for answer
4. Send Message: Delivers answer or escalation steps

<strong>Tip:</strong>Use wildcards for broad pattern matching.

#### Example 3: Multichannel Welcome Scenario

<strong>Purpose:</strong>Greet users differently by channel.

<strong>Flow:</strong>1. Entry Gate
2. New User Message: Detects channel
3. Condition: "Current Channel is WhatsApp"
    - If true: "Welcome, WhatsApp user!"
    - Else: "Welcome! How can we help you?"

<strong>More examples:</strong>[Chatbot Script Examples (chatbot.com)](https://www.chatbot.com/blog/chatbot-script/#chatbot-script-examples)

## Scenario Creation Process

### Step-by-Step Guide

1. <strong>Define Objective:</strong>State what the scenario should accomplish (e.g., collect user data, answer a FAQ).
2. <strong>Map User Flow:</strong>Outline the sequence of events, user actions, and system responses; use personas for realism.
3. <strong>Build with Blocks:</strong>- Start with Entry Gate.
    - Add Event Blocks to trigger the scenario.
    - Insert Action Blocks for outputs and operations.
    - Use Condition Blocks for branching.
    - Optionally, add Exit Blocks.
4. <strong>Configure Each Block:</strong>- Set triggers, patterns, and channels (Event Blocks).
    - Specify message types and variables (Action Blocks).
    - Define conditions and comparison ops (Condition Blocks).
    - Configure data collection and variable storage.
5. <strong>Test the Scenario:</strong>Simulate all branches and validate data capture, logic, and responses.
6. <strong>Iterate and Refine:</strong>Gather user/stakeholder feedback and improve flow, messages, and logic.

### Configuration Options

- <strong>Message Origins/Channels:</strong>Filter events by channel (web, email, WhatsApp, etc.).
- <strong>Pattern Matching:</strong>Use exact/wildcard matches to detect intent.
- <strong>Data Memorization:</strong>Store inputs in variables or fields.
- <strong>Localization:</strong>Present messages in multiple languages.
- <strong>Branching Logic:</strong>Personalize by user data or context.
- <strong>API/Webhook Integration:</strong>Trigger backend ops and resume scenarios on completion.

<strong>Warning:</strong>Chaining multiple "Awaiting Operator" blocks does not extend waiting period (fixed duration). Avoid redundant blocks to prevent logic errors.

## Best Practices

- <strong>User-Centric Design:</strong>Build flows around real user goals and behaviors; leverage personas.
- <strong>Clarity and Simplicity:</strong>Use clear, concise messaging; avoid jargon.
- <strong>Modularity:</strong>Split complex processes into reusable scenarios; use exit/run scenario blocks.
- <strong>Explicit Data Capture:</strong>Validate and confirm all user inputs before proceeding.
- <strong>Error Handling:</strong>Plan for invalid inputs, timeouts, and unexpected branches.
- <strong>Testing:</strong>Test across all supported channels and edge cases.
- <strong>Localization:</strong>Provide multi-language support as needed.

### Common Pitfalls and Warnings

- <strong>Neglecting Branches:</strong>Failing to handle all user responses can cause dead ends.
- <strong>Overcomplicating Flows:</strong>Excessive branching reduces maintainability.
- <strong>Missing Event Block After Input:</strong>Always pair inputs with event blocks to pause/resume and store values.
- <strong>Not Updating User Data:</strong>Ensure captured data is saved and used for personalization.
- <strong>Ignoring Privacy and Security:</strong>Avoid collecting sensitive data unless necessary; ensure compliance.

## Benefits of Scenarios

### For Users

- <strong>Consistent Experience:</strong>Predictable, reliable responses and journey.
- <strong>Personalization:</strong>Flows adapt to user data and context.
- <strong>Faster Resolution:</strong>Automation reduces wait times and accelerates solutions.

### For Businesses

- <strong>Scalability:</strong>Automate frequent tasks, reducing manual effort.
- <strong>Data Collection:</strong>Capture structured user data for CRM and analytics.
- <strong>Quality Assurance:</strong>Standardized flows ensure compliance and consistency.
- <strong>Continuous Improvement:</strong>Data/feedback enable ongoing optimization.

## Glossary of Key Terms

| Term                        | Definition                                                                                                 |
|-----------------------------|------------------------------------------------------------------------------------------------------------|
| <strong>Scenario</strong>| Pre-prepared conversation flow in a chatbot or automation system, built from modular blocks.               |
| <strong>Block</strong>| Discrete unit of logic/function within a scenario (Event, Action, Condition, Exit).                        |
| <strong>Entry Gate</strong>| Starting point of a scenario flow.                                                                         |
| <strong>Event Block</strong>| Triggers scenario progression based on user/system events.                                                 |
| <strong>Action Block</strong>| Executes actions (e.g., send message, update user data, call API).                                         |
| <strong>Condition Block</strong>| Evaluates data or state to branch scenario flow.                                                           |
| <strong>Exit Block</strong>| Ends or hands off scenario flow.                                                                           |
| <strong>User Scenario</strong>| Narrative describing user behavior, goals, and context within a system (often used for design/UX).         |
| <strong>User Story</strong>| Short, high-level requirement from user’s perspective (Agile development).                                 |
| <strong>Use Case</strong>| Formal description of all ways a user interacts with a system to achieve a goal.                           |
| <strong>Persona</strong>| Archetype representing a user segment, used to inform scenario design.                                     |
| <strong>Pattern Matching</strong>| Detecting keywords or phrases in user messages to trigger scenario logic.                                  |
| <strong>Memorization</strong>| Storing collected user data (e.g., email, name) within the scenario for later use.                         |

## References

1. [Chatbot.com: How to Write a Chatbot Script – Examples Included](https://www.chatbot.com/blog/chatbot-script/)
2. [Marutitech: How do Chatbots Work? A Guide to Chatbot Architecture](https://marutitech.com/chatbots-work-guide-chatbot-architecture/)
3. [Interaction Design Foundation: What are User Scenarios?](https://www.interaction-design.org/literature/topics/user-scenarios)
4. [Interaction Design Foundation: Design Scenarios – Communicating the Small Steps](https://www.interaction-design.org/literature/topics/scenarios)
5. [Make.com: Scenarios for AI agents – Help Center](https://www.make.com/en/help/scenarios)
6. [Zendesk: Was ist ein Chatbot? Funktionen & Vorteile im Überblick](https://www.zendesk.de/blog/chatbot-vorteile/)
7. Additional documentation and best practices from respective AI chatbot and automation platforms.

<strong>Further Reading & Resources:</strong>- [Chatbot.com Documentation](https://www.chatbot.com/help/)
- [OpenAI: Chatbot Best Practices](https://platform.openai.com/docs/guides/gpt)
- [YouTube: How to Create a Chatbot Flow](https://www.youtube.com/results?search_query=how+to+create+chatbot+flow)
- [Make.com: Scenarios Overview](https://www.make.com/en/help/scenarios)

This glossary provides a comprehensive, actionable reference for anyone designing, building, or maintaining AI chatbot and automation scenarios. For practical tutorials and in-depth guides, explore the referenced articles and documentation above.

