---
title: Slot Filling
translationKey: slot-filling-the-definitive-glossary-for-conversational
description: Slot filling extracts specific parameters from user queries to complete
  tasks in conversational AI. Essential for gathering data, enabling natural interaction,
  and ensuring task completion.
keywords: ["Slot Filling", "Conversational AI", "Chatbot", "Entities", "Intents"]
category: AI Chatbot & Automation
type: glossary
date: 2025-12-03
draft: false
---
## What is Slot Filling?

Slot filling is a core technique in task-oriented dialog systems for [conversational AI](/en/glossary/conversational-ai/). It focuses on identifying and extracting required parameters—called slots—from user queries. These slots are necessary to fulfill a specific action, such as booking a flight, ordering food, or scheduling an appointment.

For example, in the query:

> “Book a flight from New York to London on July 20th.”

The conversational agent should extract:
- **Departure city:** New York
- **Destination city:** London
- **Date:** July 20th

Slot filling is the mechanism that allows the AI to parse this information, store it, and use it effectively to respond or take action on behalf of the user. If some information is missing, the system prompts the user to provide it, ensuring a complete data set for the task.

**Authoritative Sources:**  
- [Microsoft Copilot Studio: Use entities and slot filling in agents](https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced-entities-slot-filling)  
- [Dydu documentation: Slot filling](https://docs-en.dydu.ai/contents/knowledge/knowledge-types/slot-filling)  
- [Just AI Conversational Cloud: Slot filling](https://help.cloud.just-ai.com/en/jaicp/NLU_core/slot_filling)  

## Why is Slot Filling Important?

Slot filling is essential for enabling AI systems to:
- Gather all necessary data to complete a user’s request (e.g., booking, ordering, customer support).
- Allow users to provide information naturally, in any order and across multiple conversational turns.
- Reduce unnecessary back-and-forth by extracting maximum information from initial queries and prompting only for missing pieces.
- Ensure completeness and accuracy before executing any action, which minimizes errors and misunderstandings.

Slot filling is the backbone of any conversational interface that requires structured data extraction from free-form user input ([Microsoft Copilot Studio](https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced-entities-slot-filling), [Dydu](https://docs-en.dydu.ai/contents/knowledge/knowledge-types/slot-filling)).

## Key Concepts: Slots, Entities, and Intents

- **Intent:** The user’s goal or purpose (e.g., "Book a hotel," "Order pizza").
- **Slot:** A placeholder for a required or optional piece of information needed to fulfill the intent (e.g., “check-in date,” “pizza size”).
- **Entity:** The data type or category of information that a slot expects (e.g., city, date, number, item type).

**Relationship:**  
An intent defines the action, slots are parameters needed for that action, and entities describe the kind of data each slot expects ([Copilot Studio](https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced-entities-slot-filling), [Just AI](https://help.cloud.just-ai.com/en/jaicp/NLU_core/slot_filling)).

## Types of Entities Used in Slot Filling

Entities enable chatbots to recognize and extract relevant data from user input. Main categories:

### 1. Built-in/System Entities
Predefined by the conversational platform, these handle common data types such as:
- Dates and times
- Email addresses
- Phone numbers
- Cities and locations
- Colors, numbers, currency

[Microsoft Copilot Studio Prebuilt Entities](https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-variables-about#entities)

### 2. Custom Entities
Defined by developers to fit domain-specific needs.
- **Closed List Entities:** Enumerated set of acceptable values (e.g., pizza toppings, product SKUs).
- **Regular Expressions (RegEx):** Patterns for extracting structured data (e.g., ticket numbers like “INC000123”).

Custom entities expand the bot’s ability to handle specialized vocabulary and data types. ([Copilot Studio](https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced-entities-slot-filling#closed-list-entities), [Just AI entities guide](https://help.cloud.just-ai.com/en/jaicp/platform_ux/nlu_core/entities))

**Tip:**  
Use synonyms and fuzzy matching to broaden entity recognition (e.g., “NYC” as a synonym for “New York City”).

## Slot Filling Process: Step-by-Step

**1. Define Required Slots:**  
List all the pieces of information needed to accomplish a specific intent.

**2. Associate Entities with Each Slot:**  
Specify which data type or pattern each slot should accept.

**3. Extract Slot Values from User Input:**  
Use NLU (Natural Language Understanding) to identify and extract values for each slot.

**4. Prompt for Missing Slots:**  
If any required slot is unfilled, the bot asks questions to gather the missing information.

**5. Handle Multi-Turn Dialogs:**  
Allow users to fill slots over several messages and in any order.

**6. Confirm Collected Slot Values:**  
Optionally present gathered information to the user for confirmation before taking action.

**7. Execute the Task:**  
Proceed with the fulfillment (e.g., book, order, support) once all required slots are filled and confirmed.

**Visual Example (from Dydu):**

- User: "I want to order a pizza."
- Bot: "How many slices would you like?"
- User: "8"
- Bot: "What type of pizza do you want?"
- User: "Pepperoni"
- Bot: "You want an 8-slice Pepperoni pizza. Is that correct?"
- User: "Yes"
- Bot: "Order confirmed!"

([Dydu slot filling documentation, with images and full dialog flow](https://docs-en.dydu.ai/contents/knowledge/knowledge-types/slot-filling))

## Slot Configuration: Parameters & Options

When defining slots, configuration options include:

- **Name:** Identifier for the slot (e.g., `departure_city`).
- **Entity:** Data type expected—built-in or custom.
- **Required:** Is this slot mandatory for the task? If yes, the bot must prompt until filled or exit.
- **Is Array:** Should the slot accept multiple values (e.g., “Order two pizzas: one Margherita, one Pepperoni”)?
- **Clarifying Questions:** Prompts to use when requesting missing slot values.
- **Default Value:** Fallback value if the slot is optional and left unfilled.
- **Reset/Overwrite:** Should the slot’s value be overwritten if the user provides new information?
- **Max Retries / Garbage Count:** Maximum times to prompt for required information before abandoning the process.
- **Confirmation:** Option to confirm the slot values with the user before proceeding.

([Just AI Slot Parameter Details](https://help.cloud.just-ai.com/en/jaicp/NLU_core/slot_filling#slot-parameters), [Dydu Slot Options](https://docs-en.dydu.ai/contents/knowledge/knowledge-types/slot-filling#id-1-configuration-of-the-slots))

## Implementation Strategies & Technical Details

### General Workflow

1. **Intent Recognition:**  
   Use NLU models to detect the intent and identify which slots apply.

2. **Entity Extraction:**  
   Apply entity recognition to extract slot values from user input.

3. **Slot Tracking:**  
   Maintain the state of filled/unfilled slots throughout the conversation.

4. **Prompt Logic:**  
   Implement logic to prompt users for unfilled required slots and manage retries or interruptions.

5. **Script/Code Access:**  
   Access filled slots in conversation scripts or backend code.

6. **Completion & Confirmation:**  
   Once all required slots are filled, optionally confirm with the user before executing the backend action.

**Example: Slot Extraction in Code (Pseudocode)**
```python
if not slots['city']:
    prompt("Which city are you traveling to?")
elif not slots['date']:
    prompt("What date would you like to travel?")
else:
    confirm(f"Book a ticket to {slots['city']} on {slots['date']}. Is this correct?")
```

### Platform-Specific Details

- **Copilot Studio:**  
  - Use prebuilt and custom entities.
  - Enable “Smart Matching” for fuzzy matching and autocorrect.
  - Add synonyms to closed list entities.
  - Use regular expressions for structured data extraction.

([Copilot Studio Entity & Slot Documentation](https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced-entities-slot-filling))

- **Just AI Conversational Cloud:**  
  - Configure required/optional slots, array types, and retry/timeout logic in `chatbot.yaml`.
  - Access slots via `$parseTree` or related variables.

([Just AI Slot Filling Guide](https://help.cloud.just-ai.com/en/jaicp/NLU_core/slot_filling))

- **Dydu:**  
  - Define Slot knowledge types and configure the slot filling process visually.
  - Use introductory, confirmation, and end sentences to manage user flow.

([Dydu Slot Filling Setup Guide](https://docs-en.dydu.ai/contents/knowledge/knowledge-types/slot-filling#id-1-configuration-of-the-slots))

## Practical Examples and Dialog Snippets

### Example 1: Pizza Order (Dydu)
- **Required Slots:** Number of slices, Pizza type

```
User: "I want to order a pizza."
Bot: "How many slices would you like?"
User: "8"
Bot: "What type of pizza do you want?"
User: "Pepperoni"
Bot: "You want an 8-slice Pepperoni pizza. Is that correct?"
User: "Yes"
Bot: "Order confirmed!"
```
([Dydu slot filling example](https://docs-en.dydu.ai/contents/knowledge/knowledge-types/slot-filling#use-case-order-a-pizza))

### Example 2: Book a Train Ticket
- **Required Slots:** Destination city, Date

```
User: "I need to buy a train ticket to Paris."
Bot: "For which date do you want to travel?"
User: "Next Monday."
Bot: "Ticket to Paris on next Monday. Shall I proceed?"
```
([Dydu train ticket example](https://docs-en.dydu.ai/contents/knowledge/knowledge-types/slot-filling#use-case-buy-a-train-ticket))

### Example 3: Weather Inquiry (Just AI)
- **Slots:** City (required), Date (optional)

```
User: "What's the weather like in London today?"
Bot: "The weather in London for today is sunny with 20°C."
```
If the date is missing:
```
User: "What's the weather like in Paris?"
Bot: "For which date do you need the forecast?"
```
([Just AI slot filling example](https://help.cloud.just-ai.com/en/jaicp/NLU_core/slot_filling#slot-extraction))

## Best Practices in Slot Filling

1. **Use Built-in Entities When Possible:**  
   Leverage platform-provided entities for robust handling of common data types.

2. **Add Synonyms to Closed List Entities:**  
   Expand recognition with variations and related terms.

3. **Enable Smart or Fuzzy Matching:**  
   Allow for misspellings and similar terms to broaden entity recognition.

4. **Be Creative with Regular Expressions:**  
   Use RegEx for structured data formats, especially for codes and IDs.

5. **Confirm Critical Slot Values:**  
   Always confirm with the user before taking important actions.

6. **Set Maximum Retry/Prompt Limits:**  
   Prevent endless loops by limiting prompts for unfilled slots.

7. **Design for Interruptions:**  
   Allow users to exit slot filling flows or switch topics gracefully.

8. **Handle Arrays and Multiple Slot Values:**  
   Support scenarios where users provide several values for the same slot.

([Just AI Best Practices](https://help.cloud.just-ai.com/en/jaicp/NLU_core/slot_filling#interruption-of-slot-filling), [Microsoft Copilot Studio Best Practices](https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/slot-filling-best-practices))

## Common Pitfalls & How to Avoid Them

- **Missing Clarifying Questions:**  
  If no prompt is specified for a required slot, the intent may never be matched.

- **Overly Rigid Entity Definitions:**  
  Avoid restricting entities to a narrow list; use synonyms and smart matching.

- **Not Handling Slot Filling Interruptions:**  
  Always allow users a way to abandon or reset slot filling if stuck.

- **Ignoring Confirmation Steps:**  
  Failing to confirm slot values can lead to errors or user frustration.

- **Not Supporting Multi-Turn/Out-of-Order Filling:**  
  Users expect to give information in any order over several messages.

- **No Handling of Maximum Retries/Timeouts:**  
  Set sensible limits to avoid trapping users in endless clarification loops.

([Just AI Pitfalls](https://help.cloud.just-ai.com/en/jaicp/NLU_core/slot_filling#interruption-of-slot-filling), [Microsoft Copilot Studio Pitfalls](https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/slot-filling-best-practices))

## Advanced Approaches: BERT & Beyond

### Using BERT for Slot Filling

BERT (Bidirectional Encoder Representations from Transformers) has revolutionized slot filling by leveraging deep contextual language understanding:

- **Contextual Representations:** BERT captures context from the entire input, aiding in accurate slot boundary detection.
- **Ambiguity Resolution:** Handles ambiguous phrasing and abbreviations in user queries.
- **OOV Handling:** Subword tokenization supports extraction even when users use rare or misspelled terms.
- **Fine-Tuning:** Pre-trained BERT models can be fine-tuned on slot filling datasets for domain adaptation.

**Implementation Steps:**
1. **Data Preparation:** Create labeled datasets (tokens + slot labels).
2. **BERT Tokenization:** Convert text to tokens/subwords.
3. **Model Architecture:** Use BERT as encoder, with a slot classification layer.
4. **Fine-Tuning:** Train on slot-labeled data using cross-entropy loss.
5. **Inference:** Predict slot labels for each token in user input.

**Python Example ([Analytics Vidhya](https://www.analyticsvidhya.com/blog/2023/10/conversational-ai-with-bert/)):**
```python
from transformers import BertTokenizer, BertForTokenClassification

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertForTokenClassification.from_pretrained('bert-base-uncased', num_labels=num_labels)

# Tokenize and predict slots
inputs = tokenizer("Book a flight from New York to London", return_tensors='pt')
outputs = model(**inputs)
```

**Resources:**  
- [Enhancing Conversational AI with BERT: The Power of Slot Filling - Analytics Vidhya](https://www.analyticsvidhya.com/blog/2023/10/conversational-ai-with-bert/)

## Use Cases and Real-World Applications

Slot filling powers a broad range of conversational AI applications:

- **Travel Booking:** Departure/arrival cities, dates, passenger counts, class, etc.
- **E-commerce Orders:** Product types, quantities, sizes, colors, delivery addresses.
- **Customer Support:** Ticket numbers, account IDs, issue descriptions.
- **Restaurant Reservations:** Restaurant name, date, time, number of guests, special requests.
- **Smart Home/Utilities:** Device names, actions, schedules, settings.
- **Healthcare Chatbots:** Symptoms, appointment dates, doctor names, insurance information.

([Dydu Use Cases](https://docs-en.dydu.ai/contents/knowledge/knowledge-types/slot-filling), [Just AI Use Cases](https://help.cloud.just-ai.com/en/jaicp/NLU_core/slot_filling#slot-extraction))

## Key Takeaways

- Slot filling is fundamental to task-oriented conversational AI, enabling bots to collect all required data for intent fulfillment.
- It relies on defining intents, slots, and entities, with robust NLU for extraction.
- Multi-turn, flexible dialogs and confirmation steps boost usability and accuracy.
- Best practices include leveraging built-in entities, using synonyms and fuzzy matching, and setting sensible retry limits.
- State-of-the-art models like BERT enable advanced, high-accuracy slot extraction.

## Frequently Asked Questions (FAQ)

**Q1: What is the difference between a slot and an entity?**  
A slot is a placeholder for a specific piece of information required to complete a task (e.g., “date” in booking a ticket), while an entity is the data category or type (e.g., “city”, “number”, “date”) that can fill that slot.

**Q2: How does a chatbot know which slots to fill?**  
Each intent is associated with a set of required and optional slots. The chatbot tracks which have been filled and prompts for missing ones, based on user input and dialog state.

**Q3: What happens if the user does not provide all required slot values?**  
The chatbot will prompt with clarifying questions for missing required slots, up to a maximum retry limit or until the user abandons the process.

**Q4: Can users fill multiple slots in one message?**

