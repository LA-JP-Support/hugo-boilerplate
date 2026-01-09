---
title: "Utterance"
date: 2025-12-18
lastmod: 2025-12-18
translationKey: "utterance"
description: "An utterance is any message, question, or command a user sends to a chatbot—whether typed or spoken. It's the basic input that AI systems analyze to understand what the user wants."
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

<strong>Banking Chatbots:</strong>- "How do I check my balance?"
- "Transfer $100 to savings."
- "When was my last transaction?"
- "Report a lost card."

<strong>E-commerce Bots:</strong>- "Track my order."
- "I want to return these shoes."
- "Do you have this in size 10?"
- "When will my package arrive?"

<strong>Customer Support:</strong>- "I can't log in to my account."
- "Reset my password."
- "How do I cancel my subscription?"
- "The app keeps crashing."

Each user input is an utterance that the chatbot must understand to fulfill the request. Capturing a wide range of utterances across different contexts, phrasings, and user types is vital for training effective conversational AI.

## Types and Categories of Utterances

Understanding utterance diversity is central to robust chatbot design and effective intent recognition. Utterances can be classified along multiple dimensions:

### Structural Categories

<strong>Structured vs. Unstructured</strong>- Structured utterances follow clear, predictable formats (e.g., "Order status: #12345")
- Unstructured utterances use free-form, natural phrasing (e.g., "Can you tell me where my last order is?")

<strong>Contextual vs. Non-Contextual</strong>- Contextual utterances depend on previous conversation or user data (e.g., "When will it arrive?" after discussing an order)
- Non-contextual utterances are independent and self-contained (e.g., "What are your store hours?")

<strong>Positive vs. Negative</strong>- Positive utterances express satisfaction or agreement (e.g., "Thanks, that was helpful!")
- Negative utterances express dissatisfaction or complaint (e.g., "This isn't working for me.")

### Intent-Oriented Categories

<strong>Direct Commands</strong>Imperative statements requesting specific actions (e.g., "Cancel my appointment.")

<strong>Polite Requests</strong>Courteous phrasing of requests (e.g., "Could you please cancel my appointment?")

<strong>Questions</strong>Interrogative utterances seeking information (e.g., "How do I cancel my appointment?")

<strong>Statements of Intent</strong>Declarations of user goals (e.g., "I want to cancel my appointment.")

<strong>Hypothetical Queries</strong>Exploratory questions about consequences (e.g., "What if I cancel my appointment?")

<strong>Partial/Fragmented</strong>Abbreviated or incomplete input (e.g., "Cancel appointment")

<strong>Emotional Feedback</strong>Expressions of sentiment (e.g., "This is too slow." / "Great service!")

### Linguistic Variation

<strong>Formal vs. Informal</strong>- Formal: "I would like to inquire about..."
- Informal: "Wanna know about..."

<strong>Slang, Abbreviations, Typos</strong>- "U there?"
- "Plz help"
- "Cant log in"

## Utterance Processing Workflow

The chatbot workflow for processing utterances involves several coordinated steps:

<strong>1. User Input Capture</strong>The user types or speaks a message through the interface (web chat, mobile app, voice assistant).

<strong>2. Natural Language Processing</strong>The chatbot analyzes the utterance using multiple NLP techniques:
- <strong>Tokenization:</strong>Breaking down the utterance into words or tokens
- <strong>Stemming/Lemmatization:</strong>Reducing words to their base forms
- <strong>Part-of-Speech Tagging:</strong>Identifying grammatical roles
- <strong>Named Entity Recognition:</strong>Extracting key details like dates, locations, names
- <strong>Sentiment Analysis:</strong>Assessing emotional tone

<strong>3. Intent Classification</strong>Determining what the user wants to achieve based on the processed utterance. Example: "I want to book a flight to Tokyo." → Intent: BookFlight

<strong>4. Entity Extraction</strong>Pulling specific details from the utterance that are necessary for fulfilling the intent. Example: Destination = Tokyo, Action = Book, Service = Flight

<strong>5. Response Generation</strong>Using the identified intent, entities, and context to generate an appropriate reply, whether through template selection, dynamic generation, or API calls.

### Relationship Between Utterance, Intent, and Entity

| Component | Description | Example |
|-----------|-------------|---------|
| Utterance | What the user says | "Find me flights to Paris next weekend" |
| Intent | The goal or purpose behind the utterance | BookFlight |
| Entity | Key details within the utterance | Destination: Paris, Date: next weekend |

This relationship forms the foundation of conversational AI systems, with utterances serving as the input that gets processed into structured intent and entity information.

## Common Challenges in Handling Utterances

<strong>Linguistic Ambiguity</strong>Homonyms and homophones create confusion (e.g., "Book a table" vs. "Read a book"). Implicit intent requires contextual understanding (e.g., "It's too cold in here" implies adjusting temperature).

<strong>Slang, Abbreviations, and Informal Language</strong>Users employ informal expressions that may not appear in formal training data (e.g., "Wanna check balance", "Plz help").

<strong>Spelling and Typographical Errors</strong>Real-world input contains mistakes that systems must handle gracefully (e.g., "Cant login", "Tarnsfer funds").

<strong>Multilingual and Code-Switched Utterances</strong>Users may mix languages within a single utterance (e.g., "Quiero order pizza"), requiring multilingual understanding capabilities.

<strong>Context Dependence</strong>Many utterances only make sense with reference to previous conversation turns (e.g., "How much is shipping?" after discussing a product).

<strong>Overlapping Intents</strong>Similar utterances may map to multiple intents, causing classification ambiguity and requiring disambiguation logic.

<strong>Entity Variation</strong>The same entity can be expressed in multiple ways (e.g., "NYC", "New York City", "The Big Apple"), requiring normalization and resolution.

## Best Practices for Utterance Design and Collection

<strong>Collect Diverse, Representative Utterances</strong>Use real user data from chat logs, support tickets, and actual conversations. Include brainstorming sessions and active learning from production data. Cover variations in phrasing, structure, and formality levels.

<strong>Avoid Intent Overlap</strong>Ensure utterances for different intents are distinct to prevent misclassification. Regularly review for redundancy or ambiguity. Test boundary cases where intents might overlap.

<strong>Use Natural User Language</strong>Prioritize how users actually speak or type, including slang, misspellings, and informal expressions. Avoid overly formal or artificial utterances that don't reflect real usage.

<strong>Balance Utterance Counts Across Intents</strong>Maintain similar numbers of utterances for each intent to avoid bias. Underrepresented intents lead to poor recognition accuracy for those user goals.

<strong>Incorporate Contextual and Non-Contextual Variations</strong>Train for both standalone queries and those that rely on prior conversation. Include utterances that reference previous context and those that don't.

<strong>Regularly Update and Refine Utterance Libraries</strong>Review live data continuously, add new utterances reflecting emerging patterns, and remove underperforming ones. Leverage AI tools to expand and validate utterances.

<strong>Provide Coverage for Special Cases</strong>Include greetings, farewells, help requests, complaints, and feedback. Account for fragmented or error-prone utterances that reflect real-world input quality.

<strong>Test and Validate Thoroughly</strong>Simulate real conversations and iterate based on user feedback and chatbot logs. Use A/B testing to compare utterance sets and measure impact on performance.

<strong>Handle Multilingual and Regional Variations</strong>Include utterances in all supported languages and dialects for global audiences. Account for cultural differences in expression and communication style.

<strong>Protect User Privacy</strong>Ensure utterance data does not contain personal or confidential information. Anonymize and sanitize training data appropriately.

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

<strong>Recommended Quantities</strong>Industry guidance suggests 10-20 well-chosen utterances per intent as a starting point. Too many utterances can cause confusion and overlap; too few limit the model's ability to generalize.

<strong>Quality Over Quantity</strong>Focus on representative, diverse utterances rather than simply maximizing count. Ten thoughtfully selected utterances often outperform twenty repetitive or similar ones.

<strong>Iterative Expansion</strong>Start with core utterances, deploy to limited users, analyze misunderstandings, and expand based on actual confusion patterns observed in production.

<strong>Negative Examples</strong>Include utterances that are close to an intent but don't match it, helping the model learn precise boundaries between similar intents.

## Frequently Asked Questions

<strong>Why are multiple utterances needed for chatbot training?</strong>Users express the same intent in countless ways. Training on diverse utterances enables chatbots to recognize intent despite variation in phrasing, improving accuracy and user experience.

<strong>How do I collect utterances for a new chatbot?</strong>Use historical chat logs, user surveys, brainstorming sessions with domain experts, and active learning from real conversations. Start with employee or beta tester interactions if launching a new service.

<strong>How many utterances per intent are recommended?</strong>Start with 10-20 well-chosen utterances per intent. Monitor performance and expand based on misclassification patterns observed in production.

<strong>Should I include misspellings and slang?</strong>Yes. Include common typos, abbreviations, and slang to improve robustness in real-world conditions where users don't always type or speak perfectly.

<strong>Can utterances contain multiple intents?</strong>Some user messages express more than one intent. Design your chatbot to handle multi-intent utterances through prioritization, clarification dialogs, or sequential processing.

<strong>How often should utterance libraries be updated?</strong>Continuously. Regularly review live interactions (weekly or monthly), add new utterances reflecting emerging patterns, and remove outdated examples as language and user behavior evolve.

<strong>Are utterances only user inputs?</strong>Primarily yes, but some advanced systems also model bot utterances and system responses for comprehensive dialogue management and response optimization.

<strong>What tools can help manage utterances?</strong>Major platforms like Microsoft LUIS, IBM Watson, Emplifi, and Dialogflow provide utterance management features including AI-assisted generation, validation, and performance analytics.

## References


1. Microsoft. (n.d.). LUIS: Utterances. Microsoft Learn.

2. SiteSpeakAI. (n.d.). What is an Utterance?. SiteSpeakAI Glossary.

3. Emplifi. (n.d.). AI Utterances Documentation. Emplifi Documentation.

4. Blocchi, P. (n.d.). What is Utterance, Intent & Entity in Conversational AI. LinkedIn.

5. CogniTech. (n.d.). Intents, Entities, Synonyms in Natural Language Understanding. CogniTech Blog.

6. BotPenguin. (n.d.). Utterance - Types and Challenges. BotPenguin Glossary.

7. IBM. (n.d.). Conversational AI Videos. YouTube.

8. Microsoft. (n.d.). Azure AI: NLP and Chatbots. YouTube.
