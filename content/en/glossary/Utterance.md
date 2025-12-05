---
title: "Utterance"
date: 2025-11-25
translationKey: "utterance"
description: "Learn what an utterance is in conversational AI, its role in NLU/NLP, types, workflow, challenges, and best practices for training chatbots effectively."
keywords: ["utterance", "conversational AI", "chatbot", "NLU", "NLP"]
category: "AI Chatbot & Automation"
type: "glossary"
draft: false
---
## What is an Utterance in Conversational AI?

An **utterance** is any input, phrase, or statement that a user communicates to a chatbot or [conversational AI](/en/glossary/conversational-ai/) during a conversation, either by typing or speaking. Each message or command—whether a sentence, question, or fragment—is an utterance. For example:

- User: “What’s my account balance?” *(utterance)*
- User: “Cancel my last order.” *(utterance)*
- User: “Hi!” *(utterance)*

Utterances are the building blocks that conversational AI systems interpret to understand user needs and generate appropriate responses. They are core to systems that rely on **natural language understanding (NLU)** and **natural language processing (NLP)**.

**Authoritative Reference:**  
- [SiteSpeakAI: What is an Utterance?](https://sitespeak.ai/ai-chatbot-terms/utterance)
- [Emplifi: AI Utterances Documentation](https://docs.emplifi.io/platform/latest/home/ai-utterances)
- [LinkedIn: Utterance, Intent & Entity in Conversational AI](https://www.linkedin.com/pulse/what-utterance-intent-entity-conversational-ai-paul-blocchi)

## Deep Dive: Practical Examples of Utterances

Utterances can vary in complexity, length, and intent. They range from brief greetings to specific commands or open-ended questions. Some common examples:

| Utterance Example                        | Possible Intent             |
|-------------------------------------------|-----------------------------|
| "What's the weather like today?"          | Weather Inquiry             |
| "Book a flight to Paris for next week."   | BookFlight                  |
| "Help!"                                  | Request Assistance          |
| "Show me Italian restaurants nearby."     | Restaurant Search           |
| "I want to change my password."           | Account Management          |
| "Can you tell me a joke?"                 | Entertainment Request       |
| "Hi"                                     | Greeting                    |

### Real-World Use Cases

- **Banking Chatbots:**  
  - “How do I check my balance?”
  - “Transfer $100 to savings.”

- **E-commerce Bots:**  
  - “Track my order.”
  - “I want to return these shoes.”

- **Customer Support:**  
  - “I can’t log in to my account.”
  - “Reset my password.”

Each user input is an utterance that the chatbot must understand to fulfill the request. Capturing a wide range of utterances is vital for training conversational AI effectively. ([SiteSpeakAI](https://sitespeak.ai/ai-chatbot-terms/utterance))

## Types and Categories of Utterances

Understanding utterance diversity is central to robust chatbot design and effective [intent recognition](/en/glossary/intent-recognition/).

### 1. Structured vs. Unstructured Utterances

- **Structured:** Clear, predictable format.
  - Example: “Order status: #12345”
- **Unstructured:** Free-form, natural phrasing.
  - Example: “Can you tell me where my last order is?”

### 2. Contextual vs. Non-Contextual Utterances

- **Contextual:** Dependent on previous conversation or user data.
  - Example: “When will it arrive?” (after discussing an order)
- **Non-Contextual:** Independent, can be understood alone.
  - Example: “What are your store hours?”

### 3. Positive vs. Negative Utterances

- **Positive:** Satisfaction or agreement.
  - “Thanks, that was helpful!”
- **Negative:** Dissatisfaction or complaint.
  - “This isn’t working for me.”

### 4. Intent-Oriented Categories

- **Direct Commands:** “Cancel my appointment.”
- **Polite Requests:** “Could you please cancel my appointment?”
- **Questions:** “How do I cancel my appointment?”
- **Statements of Intent:** “I want to cancel my appointment.”
- **Hypotheticals:** “What if I cancel my appointment?”
- **Partial/Fragmented:** “Cancel appointment”
- **Emotion or Feedback:** “This is too slow.” / “Great service!”

### 5. Linguistic Variation

- **Formal vs. Informal:** “I would like to…” vs. “Wanna…”
- **Slang, Abbreviations, Typos:** “U there?” “Plz help” “Cant log in”

#### Category Table

| Category                | Example(s)                                 | Use Case                        |
|-------------------------|--------------------------------------------|----------------------------------|
| Direct Command          | “Delete account”                           | Action requests                  |
| Polite Request          | “Could you remove my profile?”             | Courteous users                  |
| Question                | “How do I reset my password?”              | Seeking guidance                 |
| Statement of Intent     | “I want to change my email address”        | Explicit user goal               |
| Partial/Fragment        | “Password reset”                           | Abbreviated input                |
| Hypothetical            | “What if I delete my account?”             | Exploring consequences           |
| Feedback (Positive)     | “Thanks for your help!”                    | Expressing gratitude             |
| Feedback (Negative)     | “This isn’t working”                       | Expressing frustration           |
| Greeting/Farewell       | “Hello!” / “Goodbye”                       | Conversation flow                |

## Utterances in the Chatbot Workflow

The chatbot workflow for processing utterances involves several steps:

1. **User submits an utterance:** The user types or speaks a message.
2. **Natural Language Processing (NLP):** The chatbot analyzes the utterance using:
   - **Tokenization:** Breaking down the utterance into words or tokens.
   - **Stemming/Lemmatization:** Reducing words to their base forms.
   - **Part-of-speech tagging:** Identifying grammatical roles.
   - **Named Entity Recognition (NER):** Extracting key details (like dates, locations).
   - **Sentiment Analysis:** Assessing emotional tone.
3. **Intent Classification:** Determining what the user wants to achieve.
   - Example: “I want to book a flight to Tokyo.” → Intent: BookFlight
4. **Entity Extraction:** Pulling specific details from the utterance.
   - Example: Destination = Tokyo
5. **Response Generation:** Using the identified intent, entities, and context to generate a reply.

### Relationship: Utterance, Intent, and Entity

| Term       | Description                                                        | Example                                 |
|------------|--------------------------------------------------------------------|-----------------------------------------|
| Utterance  | What the user says                                                 | “Find me flights to Paris next weekend” |
| Intent     | The goal or purpose behind the utterance                           | BookFlight                              |
| Entity     | Key details within the utterance                                   | Destination: Paris, Date: next weekend  |

**Further Reading:**  
- [Microsoft LUIS: Utterances](https://learn.microsoft.com/en-us/azure/ai-services/luis/concepts/utterances)  
- [IBM Watson: Intents and Entities](https://www.ibm.com/cloud/learn/natural-language-processing)  
- [LinkedIn: What is Utterance, Intent & Entity?](https://www.linkedin.com/pulse/what-utterance-intent-entity-conversational-ai-paul-blocchi)

## Challenges in Handling Utterances

### 1. Linguistic Ambiguity

- **Homonyms and Homophones:**  
  - “Book a table” (reserve) vs. “Read a book” (object)
- **Implicit Intent:**  
  - “It’s too cold in here” (implied: turn up the heat)

### 2. Slang, Abbreviations, and Informal Language

- “Wanna check balance”
- “Plz help”

### 3. Spelling and Typographical Errors

- “Cant login”
- “Tarnsfer funds”

### 4. Multilingual and Code-Switched Utterances

- “Quiero order pizza” (Mix of Spanish and English)

### 5. Context Dependence

- “How much is shipping?” (after discussing an item)

### 6. Overlapping Intents

- Similar utterances may map to multiple intents, causing confusion.

### 7. Entity Variation

- “NYC”, “New York City”, “The Big Apple” (same destination)

**Source:**  
- [SiteSpeakAI: Utterance FAQ](https://sitespeak.ai/ai-chatbot-terms/utterance)
- [LinkedIn: Utterance, Intent & Entity](https://www.linkedin.com/pulse/what-utterance-intent-entity-conversational-ai-paul-blocchi)

## Best Practices for Designing and Collecting Utterances

### 1. Collect Diverse, Representative Utterances

Use real user data, chat logs, brainstorming, and active learning from actual conversations. Include variations in phrasing, structure, and formality.

### 2. Avoid Overlap Between Intents

Ensure utterances for different intents are distinct to prevent misclassification. Regularly review for redundancy or ambiguity.

### 3. Use Natural User Language

Prioritize how users actually speak or type, including slang, misspellings, and informal expressions.

### 4. Balance Utterance Counts Across Intents

Avoid bias by maintaining a similar number of utterances for each intent.

### 5. Incorporate Contextual and Non-Contextual Variations

Train for both standalone queries and those that rely on prior conversation.

### 6. Regularly Update and Refine Utterance Libraries

Review live data, add new utterances, and remove underperforming ones. Leverage AI tools (e.g., Emplifi, Microsoft LUIS, IBM Watson) to expand and validate utterances.

### 7. Provide Coverage for Special Cases

Include greetings, farewells, help requests, complaints, and feedback. Account for fragmented or error-prone utterances.

### 8. Test and Validate

Simulate real conversations and iterate based on user feedback and chatbot logs.

### 9. Handle Multilingual and Regional Variations

Include utterances in all supported languages and dialects for global audiences.

### 10. Avoid Confidential or Sensitive Information

Ensure utterance data does not contain personal or confidential information.

#### Sample Best Practices Checklist

| Practice                                 | Description                                  |
|-------------------------------------------|----------------------------------------------|
| Vary structure and length                 | Short, medium, long utterances               |
| Use synonyms and different wording        | “Book” / “Reserve” / “Schedule”              |
| Avoid intent overlap                      | Distinct utterances for each intent          |
| Use real user data                        | Authentic language and typos                 |
| Update regularly                          | Incorporate live user feedback               |
| Balance utterance count per intent        | Prevent bias                                 |
| Cover special cases                       | Greetings, farewells, error handling         |

**References:**  
- [Emplifi: AI Utterances - How To](https://docs.emplifi.io/platform/latest/home/ai-utterances)
- [Microsoft LUIS: Best Practices](https://learn.microsoft.com/en-us/azure/ai-services/luis/concepts/utterances)

## Utterance Types, Challenges, and Solutions

| Category            | Example                           | Challenge Addressed             | Solution/Best Practice                     |
|---------------------|-----------------------------------|-------------------------------|--------------------------------------------|
| Structured          | “Order status: #12345”            | Format adherence               | Include both structured/unstructured forms |
| Unstructured        | “Where’s my pizza?”               | Phrasing variation             | Gather real, informal utterances           |
| Fragmented          | “Cancel acc”                      | Partial input                  | Train with incomplete phrases              |
| Spelling Errors     | “Cant log in”                     | Typos/misspellings             | Use spell correction or train with errors  |
| Multilingual        | “Bonjour, je veux un café”        | Language diversity             | Multilingual utterance sets                |
| Contextual          | “How long will it take?”          | Context dependence             | Context-aware NLU engines                  |
| Negative Feedback   | “Not working”                     | Sentiment, support escalation  | [Sentiment analysis](/en/glossary/sentiment-analysis/), escalation triggers    |

**Further Reading:**  
- [IBM Watson: NLP in Chatbots](https://www.ibm.com/cloud/learn/natural-language-processing)
- [CogniTech: Intents, Entities, Synonyms](https://www.cognitech.systems/blog/artificial-intelligence/entry/intents-entities-synonyms-retrieval-natural-language-understanding)
- [BotPenguin: Utterance Glossary](https://botpenguin.com/glossary/utterance)

## Frequently Asked Questions (FAQ) about Utterances

**Q: Why are multiple utterances needed for chatbot training?**  
A: Users express the same intent in many ways. Training on diverse utterances enables chatbots to recognize a wide variety of phrasings, improving accuracy and the user experience. ([SiteSpeakAI FAQ](https://sitespeak.ai/ai-chatbot-terms/utterance))

**Q: How do I collect utterances for a new chatbot?**  
A: Use historical chat logs, user surveys, brainstorming, and active learning from real conversations.

**Q: How many utterances per intent are recommended?**  
A: Industry guidance (e.g., Microsoft LUIS, Emplifi) suggests 10–20 well-chosen utterances per intent. Too many can cause confusion; too few can limit accuracy. ([Emplifi Utterance Guide](https://docs.emplifi.io/platform/latest/home/ai-utterances))

**Q: Should I include misspellings and slang?**  
A: Yes. Include common typos, abbreviations, and slang to improve robustness.

**Q: Can utterances contain multiple intents?**  
A: Some user messages may express more than one intent. Design your chatbot to prioritize, clarify, or handle multi-intent utterances.

**Q: How often should utterance libraries be updated?**  
A: Continuously. Regularly review live interactions, add new utterances, and remove outdated examples.

**Q: Are utterances only user inputs?**  
A: Primarily, yes, but some systems also model bot/system utterances for advanced [dialogue management](/en/glossary/dialogue-management/).

## Further Reading and Resources

- [Microsoft LUIS: Utterances](https://learn.microsoft.com/en-us/azure/ai-services/luis/concepts/utterances)
- [IBM Cloud: What is Conversational AI? (YouTube Search)](https://www.youtube.com/results?search_query=ibm+cloud+conversational+ai)
- [SiteSpeakAI: What is an Utterance?](https://sitespeak.ai/ai-chatbot-terms/utterance)
- [Emplifi: AI Utterances Documentation](https://docs.emplifi.io/platform/latest/home/ai-utterances)
- [LinkedIn: What is Utterance, Intent & Entity?](https://www.linkedin.com/pulse/what-utterance-intent-entity-conversational-ai-paul-blocchi)
- [CogniTech: Intents, Entities, Synonyms](https://www.cognitech.systems/blog/artificial-intelligence/entry/intents-entities-synonyms-retrieval-natural-language-understanding)
- [BotPenguin: Utterance—Types and Challenges](https://botpenguin.com/glossary/utterance)

## Key Takeaways

- An **utterance** is any user input (text or speech) provided to a chatbot or conversational AI.
- Utterances drive the process of understanding user intent and extracting entities for meaningful responses.
- Capturing diverse, natural, and representative utterances is critical for building effective conversational AI.
- Regularly review and update utterance libraries, avoid intent overlap, and reflect real user language.
- Handling variations—such as slang, typos, context, and multilingual inputs—improves chatbot robustness and user satisfaction.

## Video Resources

For visual learning and demonstrations, explore:
- [YouTube: IBM Cloud Conversational AI](https://www.youtube.com/results?search_query=ibm+cloud+conversational+ai)
- [Microsoft Azure AI: NLP and Chatbots](https://www.youtube.com/results?search_query=microsoft+azure+ai+chatbot)

*Category: AI Chatbot & Automation*

