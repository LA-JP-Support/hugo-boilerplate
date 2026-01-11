---
title: "Utterance"
date: 2025-12-18
lastmod: 2025-12-18
translationKey: "utterance"
description: "An utterance is any message, question, or command a user sends to a chatbot—whether typed or spoken. It's the basic input that AI systems analyze to understand what the user wants and provide the right response."
keywords: ["utterance", "conversational AI", "chatbot", "NLU", "NLP"]
category: "AI Chatbot & Automation"
type: "glossary"
draft: false
---

## What is an Utterance in Conversational AI?

An utterance is any input, phrase, or statement that a user communicates to a chatbot or conversational AI during a conversation, either by typing or speaking. Each message or command—whether a sentence, question, or fragment—represents an utterance. Examples include:

- "What's my account balance?" (utterance)
- "Cancel my last order." (utterance)
- "Hi!" (utterance)

Utterances are the fundamental building blocks that conversational AI systems interpret to understand user needs and generate appropriate responses. They are core to systems that rely on natural language understanding (NLU) and natural language processing (NLP), serving as the primary data points for training and evaluating chatbot performance.

The quality and diversity of utterances in training data directly determine how well a conversational AI system can handle real-world user interactions. A chatbot trained on limited or homogeneous utterances will struggle with the natural variation in human communication, leading to misunderstandings, fallback responses, and user frustration.

## Utterance Examples Across Use Cases

Utterances vary significantly in complexity, length, and intent depending on the application domain and user context:

| Utterance Example | Possible Intent | Use Case |
|-------------------|-----------------|----------|
| "What's the weather like today?" | Weather Inquiry | Virtual assistant |
| "Book a flight to Paris for next week." | BookFlight | Travel booking |
| "Help!" | Request Assistance | Customer support |
| "Show me Italian restaurants nearby." | Restaurant Search | Local services |
| "I want to change my password." | Account Management | User settings |
| "Can you tell me a joke?" | Entertainment Request | Casual interaction |
| "Hi" | Greeting | Conversation opening |
| "Transfer $100 to savings." | Banking Transaction | Financial services |
| "Track my order." | Order Status | E-commerce |
| "I can't log in to my account." | Technical Support | IT help desk |

### Domain-Specific Utterance Patterns

**Banking Chatbots:**
- "How do I check my balance?"
- "Transfer $100 to savings."
- "When was my last transaction?"
- "Report a lost card."

**E-commerce Bots:**
- "Track my order."
- "I want to return these shoes."
- "Do you have this in size 10?"
- "When will my package arrive?"

**Customer Support:**
- "I can't log in to my account."
- "Reset my password."
- "How do I cancel my subscription?"
- "The app keeps crashing."

Each user input is an utterance that the chatbot must understand to fulfill the request. Capturing a wide range of utterances across different contexts, phrasings, and user types is vital for training effective conversational AI.

## Types and Categories of Utterances

Understanding utterance diversity is central to robust chatbot design and effective intent recognition. Utterances can be classified along multiple dimensions:

### Structural Categories

**Structured vs. Unstructured**
- Structured utterances follow clear, predictable formats (e.g., "Order status: #12345")
- Unstructured utterances use free-form, natural phrasing (e.g., "Can you tell me where my last order is?")

**Contextual vs. Non-Contextual**
- Contextual utterances depend on previous conversation or user data (e.g., "When will it arrive?" after discussing an order)
- Non-contextual utterances are independent and self-contained (e.g., "What are your store hours?")

**Positive vs. Negative**
- Positive utterances express satisfaction or agreement (e.g., "Thanks, that was helpful!")
- Negative utterances express dissatisfaction or complaint (e.g., "This isn't working for me.")

### Intent-Oriented Categories

**Direct Commands**  
Imperative statements requesting specific actions (e.g., "Cancel my appointment.")

**Polite Requests**  
Courteous phrasing of requests (e.g., "Could you please cancel my appointment?")

**Questions**  
Interrogative utterances seeking information (e.g., "How do I cancel my appointment?")

**Statements of Intent**  
Declarations of user goals (e.g., "I want to cancel my appointment.")

**Hypothetical Queries**  
Exploratory questions about consequences (e.g., "What if I cancel my appointment?")

**Partial/Fragmented**  
Abbreviated or incomplete input (e.g., "Cancel appointment")

**Emotional Feedback**  
Expressions of sentiment (e.g., "This is too slow." / "Great service!")

### Linguistic Variation

**Formal vs. Informal**
- Formal: "I would like to inquire about..."
- Informal: "Wanna know about..."

**Slang, Abbreviations, Typos**
- "U there?"
- "Plz help"
- "Cant log in"

## Utterance Processing Workflow

The chatbot workflow for processing utterances involves several coordinated steps:

**1. User Input Capture**  
The user types or speaks a message through the interface (web chat, mobile app, voice assistant).

**2. Natural Language Processing**  
The chatbot analyzes the utterance using multiple NLP techniques:
- **Tokenization:** Breaking down the utterance into words or tokens
- **Stemming/Lemmatization:** Reducing words to their base forms
- **Part-of-Speech Tagging:** Identifying grammatical roles
- **Named Entity Recognition:** Extracting key details like dates, locations, names
- **Sentiment Analysis:** Assessing emotional tone

**3. Intent Classification**  
Determining what the user wants to achieve based on the processed utterance. Example: "I want to book a flight to Tokyo." → Intent: BookFlight

**4. Entity Extraction**  
Pulling specific details from the utterance that are necessary for fulfilling the intent. Example: Destination = Tokyo, Action = Book, Service = Flight

**5. Response Generation**  
Using the identified intent, entities, and context to generate an appropriate reply, whether through template selection, dynamic generation, or API calls.

### Relationship Between Utterance, Intent, and Entity

| Component | Description | Example |
|-----------|-------------|---------|
| Utterance | What the user says | "Find me flights to Paris next weekend" |
| Intent | The goal or purpose behind the utterance | BookFlight |
| Entity | Key details within the utterance | Destination: Paris, Date: next weekend |

This relationship forms the foundation of conversational AI systems, with utterances serving as the input that gets processed into structured intent and entity information.

## Common Challenges in Handling Utterances

**Linguistic Ambiguity**  
Homonyms and homophones create confusion (e.g., "Book a table" vs. "Read a book"). Implicit intent requires contextual understanding (e.g., "It's too cold in here" implies adjusting temperature).

**Slang, Abbreviations, and Informal Language**  
Users employ informal expressions that may not appear in formal training data (e.g., "Wanna check balance", "Plz help").

**Spelling and Typographical Errors**  
Real-world input contains mistakes that systems must handle gracefully (e.g., "Cant login", "Tarnsfer funds").

**Multilingual and Code-Switched Utterances**  
Users may mix languages within a single utterance (e.g., "Quiero order pizza"), requiring multilingual understanding capabilities.

**Context Dependence**  
Many utterances only make sense with reference to previous conversation turns (e.g., "How much is shipping?" after discussing a product).

**Overlapping Intents**  
Similar utterances may map to multiple intents, causing classification ambiguity and requiring disambiguation logic.

**Entity Variation**  
The same entity can be expressed in multiple ways (e.g., "NYC", "New York City", "The Big Apple"), requiring normalization and resolution.

## Best Practices for Utterance Design and Collection

**Collect Diverse, Representative Utterances**  
Use real user data from chat logs, support tickets, and actual conversations. Include brainstorming sessions and active learning from production data. Cover variations in phrasing, structure, and formality levels.

**Avoid Intent Overlap**  
Ensure utterances for different intents are distinct to prevent misclassification. Regularly review for redundancy or ambiguity. Test boundary cases where intents might overlap.

**Use Natural User Language**  
Prioritize how users actually speak or type, including slang, misspellings, and informal expressions. Avoid overly formal or artificial utterances that don't reflect real usage.

**Balance Utterance Counts Across Intents**  
Maintain similar numbers of utterances for each intent to avoid bias. Underrepresented intents lead to poor recognition accuracy for those user goals.

**Incorporate Contextual and Non-Contextual Variations**  
Train for both standalone queries and those that rely on prior conversation. Include utterances that reference previous context and those that don't.

**Regularly Update and Refine Utterance Libraries**  
Review live data continuously, add new utterances reflecting emerging patterns, and remove underperforming ones. Leverage AI tools to expand and validate utterances.

**Provide Coverage for Special Cases**  
Include greetings, farewells, help requests, complaints, and feedback. Account for fragmented or error-prone utterances that reflect real-world input quality.

**Test and Validate Thoroughly**  
Simulate real conversations and iterate based on user feedback and chatbot logs. Use A/B testing to compare utterance sets and measure impact on performance.

**Handle Multilingual and Regional Variations**  
Include utterances in all supported languages and dialects for global audiences. Account for cultural differences in expression and communication style.

**Protect User Privacy**  
Ensure utterance data does not contain personal or confidential information. Anonymize and sanitize training data appropriately.

## Utterance Quality Checklist

| Best Practice | Implementation |
|---------------|----------------|
| Vary structure and length | Include short, medium, and long utterances |
| Use synonyms and different wording | "Book" / "Reserve" / "Schedule" |
| Avoid intent overlap | Distinct utterances for each intent |
| Use real user data | Authentic language patterns and typos |
| Update regularly | Incorporate live user feedback |
| Balance utterance count per intent | Prevent model bias |
| Cover special cases | Greetings, farewells, error handling |
| Include negative examples | Utterances similar but not matching intent |
| Test across demographics | Different age groups, backgrounds |
| Document sources | Track where utterances originated |

## Utterance Training Guidelines

**Recommended Quantities**  
Industry guidance suggests 10-20 well-chosen utterances per intent as a starting point. Too many utterances can cause confusion and overlap; too few limit the model's ability to generalize.

**Quality Over Quantity**  
Focus on representative, diverse utterances rather than simply maximizing count. Ten thoughtfully selected utterances often outperform twenty repetitive or similar ones.

**Iterative Expansion**  
Start with core utterances, deploy to limited users, analyze misunderstandings, and expand based on actual confusion patterns observed in production.

**Negative Examples**  
Include utterances that are close to an intent but don't match it, helping the model learn precise boundaries between similar intents.

## Frequently Asked Questions

**Why are multiple utterances needed for chatbot training?**  
Users express the same intent in countless ways. Training on diverse utterances enables chatbots to recognize intent despite variation in phrasing, improving accuracy and user experience.

**How do I collect utterances for a new chatbot?**  
Use historical chat logs, user surveys, brainstorming sessions with domain experts, and active learning from real conversations. Start with employee or beta tester interactions if launching a new service.

**How many utterances per intent are recommended?**  
Start with 10-20 well-chosen utterances per intent. Monitor performance and expand based on misclassification patterns observed in production.

**Should I include misspellings and slang?**  
Yes. Include common typos, abbreviations, and slang to improve robustness in real-world conditions where users don't always type or speak perfectly.

**Can utterances contain multiple intents?**  
Some user messages express more than one intent. Design your chatbot to handle multi-intent utterances through prioritization, clarification dialogs, or sequential processing.

**How often should utterance libraries be updated?**  
Continuously. Regularly review live interactions (weekly or monthly), add new utterances reflecting emerging patterns, and remove outdated examples as language and user behavior evolve.

**Are utterances only user inputs?**  
Primarily yes, but some advanced systems also model bot utterances and system responses for comprehensive dialogue management and response optimization.

**What tools can help manage utterances?**  
Major platforms like Microsoft LUIS, IBM Watson, Emplifi, and Dialogflow provide utterance management features including AI-assisted generation, validation, and performance analytics.

## References

- [Microsoft LUIS: Utterances](https://learn.microsoft.com/en-us/azure/ai-services/luis/concepts/utterances)
- [SiteSpeakAI: What is an Utterance?](https://sitespeak.ai/ai-chatbot-terms/utterance)
- [Emplifi: AI Utterances Documentation](https://docs.emplifi.io/platform/latest/home/ai-utterances)
- [LinkedIn: What is Utterance, Intent & Entity in Conversational AI](https://www.linkedin.com/pulse/what-utterance-intent-entity-conversational-ai-paul-blocchi)
- [CogniTech: Intents, Entities, Synonyms in Natural Language Understanding](https://www.cognitech.systems/blog/artificial-intelligence/entry/intents-entities-synonyms-retrieval-natural-language-understanding)
- [BotPenguin: Utterance - Types and Challenges](https://botpenguin.com/glossary/utterance)
- [IBM Cloud: Conversational AI Videos](https://www.youtube.com/results?search_query=ibm+cloud+conversational+ai)
- [Microsoft Azure AI: NLP and Chatbots](https://www.youtube.com/results?search_query=microsoft+azure+ai+chatbot)
