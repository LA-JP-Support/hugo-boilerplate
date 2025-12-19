---
title: "Named Entity Recognition (NER)"
translationKey: "named-entity-recognition-ner"
description: "Named Entity Recognition (NER) identifies and classifies real-world entities (people, organizations, locations, etc.) in text, transforming raw data into structured information."
keywords: ["Named Entity Recognition", "NER", "Natural Language Processing", "NLP", "Entity Extraction"]
category: "AI Chatbot & Automation"
type: "glossary"
date: 2025-12-05
lastmod: 2025-12-05
draft: false
---
## What is Named Entity Recognition (NER)?

[Named Entity Recognition (NER)](https://en.wikipedia.org/wiki/Named-entity_recognition) is a core task in [Natural Language Processing (NLP)](https://www.ibm.com/think/topics/natural-language-processing), focused on automatically identifying and classifying real-world entities in unstructured text. Entities include names of people, organizations, locations, dates, quantities, monetary values, and more. NER transforms raw text into structured, machine-readable data by locating relevant substrings (entity mentions) and assigning them to predefined categories.

In practical terms, NER models process textual data to extract and annotate key information, enabling downstream applications such as search, question answering, content recommendation, and document automation.

**Example:**  
*"Apple is looking at buying U.K. startup for $1 billion."*  
NER output:  
- "Apple" → Organization (ORG)
- "U.K." → Geopolitical entity (GPE)
- "$1 billion" → Money (MONEY)

For a visual example and further explanation, see [Encord’s NER guide](https://encord.com/blog/named-entity-recognition/).

## Why is NER Important?

Most digital content is unstructured—emails, articles, customer chats, social media posts, medical records, legal documents, and more. NER enables machines to extract factual meaning from this data, supporting a broad spectrum of applications:

- **Search:** Enhances result relevance by indexing named entities.
- **Recommendation:** Suggests content based on recognized people, places, or products.
- **Automation:** Extracts structured data from invoices, contracts, and forms.
- **Compliance:** Identifies and redacts personally identifiable information (PII).
- **Knowledge Graphs:** Structures information for analytics and AI.

**Ambiguity Handling Example:**  
NER models analyze context to resolve ambiguous names:
- *"Lincoln"* can refer to "Abraham Lincoln" (Person), "Lincoln Motor Company" (Organization), or "Lincoln, Nebraska" (Location).

For additional use cases, see the [AltexSoft NER overview](https://www.altexsoft.com/blog/named-entity-recognition/).

## Key Concepts and Terminology

### Named Entity (NE)
A unique, real-world object denoted by a proper noun or a fixed reference.  
**Examples:** “Michelle Obama” (Person), “London” (Location), “Google” (Organization), “$500” (Money).

### Entity Type / Label / Tag
The category assigned to an entity span, such as PER (Person), ORG (Organization), LOC (Location), DATE, MONEY, etc.

### Entity Boundary Detection
The process of detecting the start and end indices of entity mentions in the text, crucial for multi-word names and complex entities.
- Example: Correctly extracting “The George Washington University Hospital” as a single entity.

### Tagging Schemes
NER models often use tagging schemes to mark entity boundaries:
- **BIO** (Begin, Inside, Outside): B-ORG, I-ORG, O
- **IOBES** (Inside, Outside, Begin, End, Single): B-ORG, I-ORG, E-ORG, S-ORG, O

**Tagging examples and visuals:**  
[Encord: NER Tagging Schemes](https://encord.com/blog/named-entity-recognition/)

### Part-of-Speech (POS) Tagging
Assigns words their grammatical roles (noun, verb, adjective, etc.), often used as features for NER models.

### Chunking
Groups words into meaningful units (e.g., noun phrases), making it easier to identify entity boundaries.

### Word Embeddings
Transforms words into dense numeric vectors (using models like Word2Vec, GloVe, or contextual models like BERT) that capture semantic and syntactic relationships for machine learning.

### Gazetteers (Lexicons)
Dictionaries of known entity names used for rule-based or hybrid NER approaches.

### Corpus
A large, annotated collection of texts used to train and evaluate NER systems.

## How NER Works: Detailed Workflow

The NER process comprises several sequential stages:

### 1. Text Input and Preprocessing
- **Tokenization:** Splitting raw text into words, punctuation, and symbols (tokens).
- **Sentence Segmentation:** Identifying sentence boundaries.
- **Normalization:** Lowercasing, stemming, or lemmatization to reduce word forms.

### 2. Feature Extraction
NER models extract features to inform entity boundaries and classification:
- **Morphological:** Word shapes, prefixes, suffixes, capitalization.
- **Syntactic:** POS tags, phrase structure.
- **Semantic:** Contextual meaning, neighbors.
- **External:** Gazetteer matches, regular expression patterns.

### 3. Entity Boundary Detection
Locate candidate spans that may represent entities, using contextual and syntactic cues.

### 4. Entity Classification
Assign each detected candidate the most probable label (e.g., Person, Location, Organization), using either hand-crafted rules, statistical models, or deep learning.

### 5. Post-processing
- **Overlapping/Nested Entities:** Resolve when entities overlap or nest (e.g., “University of California, Berkeley”).
- **Ambiguity Resolution:** Leverage context to disambiguate polysemous names.
- **Consistency Enforcement:** Ensure consistent labeling within and across documents.

### 6. Output Generation
Return structured results, typically as annotated text, JSON, or XML.

**Sample JSON:**  
```json
[
  { "text": "Steve Jobs", "type": "PERSON", "startOffset": 0, "endOffset": 10 },
  { "text": "Apple", "type": "ORG", "startOffset": 22, "endOffset": 27 }
]
```

**Further reading:**  
- [Encord NER Guide](https://encord.com/blog/named-entity-recognition/)
- [IBM: What Is Named Entity Recognition?](https://www.ibm.com/think/topics/named-entity-recognition)

## Label Types and Tagging Schemes in NER

### Common Entity Labels

| Label        | Description                                      | Example                        |
|--------------|--------------------------------------------------|--------------------------------|
| PER          | Person (individuals, fictional characters)       | “Marie Curie”, “Sherlock Holmes” |
| ORG          | Organization (companies, agencies, groups)       | “Google”, “United Nations”     |
| LOC          | Location (mountains, rivers, cities, etc.)       | “Mount Everest”, “Nile River”  |
| GPE          | Geopolitical Entity (countries, cities, states)  | “Tokyo”, “United States”       |
| DATE         | Calendar dates or periods                        | “January 1, 2022”, “19th century” |
| TIME         | Specific times or durations                      | “5 PM”, “two hours”            |
| MONEY        | Monetary values                                  | “$100”, “€50 million”          |
| PERCENT      | Percentages                                      | “50%”, “half”                  |
| FAC          | Facilities (buildings, airports, highways)       | “JFK Airport”, “Golden Gate Bridge” |
| PRODUCT      | Products, vehicles, software                     | “iPhone”, “Boeing 747”         |
| EVENT        | Named events (wars, sports, disasters)           | “Olympics”, “Hurricane Katrina”|
| WORK_OF_ART  | Books, movies, paintings                         | “Mona Lisa”, “Star Wars”       |
| LANGUAGE     | Languages                                        | “English”, “Mandarin”          |
| LAW          | Legal documents, treaties                        | “Treaty of Versailles”         |
| NORP         | Nationalities, religious, or political groups    | “American”, “Democrat”         |

**For visuals and more detail:**  
[Encord: NER Labels Table](https://encord.com/blog/named-entity-recognition/)

### Tagging Schemes

- **BIO (Begin, Inside, Outside):**
  - B-ORG: Beginning of an organization
  - I-ORG: Inside organization
  - O: Outside any entity

- **IOBES/IOB2:**  
  Expands BIO with E (End) and S (Single) for finer boundary control.

- **Nested/Overlapping Tagging:**  
  Some advanced NER systems support nested entity recognition, crucial for biomedical and legal texts.

**Visuals and examples:**  
[Encord: Tagging Schemes](https://encord.com/blog/named-entity-recognition/)

## Methods and Approaches

### 1. Rule-Based (Pattern-Based / Lexicon-Based)
- Uses dictionaries (gazetteers), regular expressions, and linguistic rules.
- Fast and interpretable, but brittle—requires manual updating for new entities or domains.
- Effective for fixed formats (phone numbers, dates, known PII).
### 2. Traditional Machine Learning
- Learns from annotated datasets using engineered features (word shapes, POS, context).
- Popular algorithms: Conditional Random Fields (CRF), Hidden Markov Models (HMM), Support Vector Machines (SVM), Decision Trees.
- Can generalize to unseen examples but needs labeled data and feature engineering.
- **Further reading:** [Stanford NLP CRFClassifier](https://nlp.stanford.edu/software/CRF-NER.html)

### 3. Deep Learning Approaches

#### a. Recurrent Neural Networks (RNN, LSTM)
- Learns sequential dependencies; popular before transformers.
- Bidirectional LSTMs capture context from both left and right.

#### b. Transformer-Based Models (BERT, RoBERTa, GPT, etc.)
- Use self-attention to model complex dependencies in context.
- Pretrained on massive corpora, fine-tuned with labeled NER data.
- Handle ambiguity, context, long-range dependencies, subword units, and nested entities.
- **BERT for NER:**  
  - Context-aware, bidirectional, supports transfer learning.
  - Supports IOB tagging for multi-word entities.
  - Outperforms previous models on standard benchmarks.
  - [How to Do NER with BERT: Machine Learning Mastery](https://machinelearningmastery.com/how-to-do-named-entity-recognition-ner-with-a-bert-model/)
  - [Recent Advances in NER: arXiv Survey](https://arxiv.org/html/2401.10825v3)
- **Code Example:**  
  ```python
  from transformers import pipeline
  ner_pipeline = pipeline("ner", model="dbmdz/bert-large-cased-finetuned-conll03-english", aggregation_strategy="simple")
  text = "Apple CEO Tim Cook announced new iPhone models in California yesterday."
  entities = ner_pipeline(text)
  for entity in entities:
      print(entity)
  ```

#### c. Large Language Models (LLMs)
- General-purpose LLMs like GPT-4, PaLM, and Claude can perform NER via zero-shot or few-shot prompting.
- Less labeled data required, but may lack fine control or domain specificity.

#### d. Domain Adaptation & Transfer Learning
- Fine-tuning pretrained models on custom corpora (e.g., medical, legal) yields domain-specific NER.

#### e. Reinforcement Learning & Graph-Based NER
- Reinforcement learning can optimize NER pipelines.
- Graph-based approaches model relationships between entities for improved accuracy.
- [Recent Advances: arXiv NER Survey](https://arxiv.org/html/2401.10825v3)

## Challenges in NER

NER remains a hard problem in NLP due to:

- **Ambiguity & Polysemy:** Words can have multiple entity types (“Amazon”: company or river).
- **Boundary Detection:** Multi-word and nested entity names (“Martin Luther King Jr.”, “University of California, Berkeley”).
- **Domain Adaptation:** New or rare entities in specialized domains (biomedicine, law).
- **Evolving Language:** New terms, brands, slang, or acronyms.
- **Multilingual NER:** Handling code-switching, different scripts, or language-specific entity types.
- **Scarce Labeled Data:** Annotating large corpora is expensive and time-consuming.
- **Nested/Overlapping Entities:** Entities within entities (especially in biomedical or legal text).
- **Noise and Informality:** Social media, OCR, and speech transcripts introduce errors and informal language.

**For more challenges, see:**  
[Encord: Challenges in NER](https://encord.com/blog/named-entity-recognition/)  
[arXiv: Recent Advances in NER](https://arxiv.org/html/2401.10825v3)

## NER Use Cases and Applications

### 1. Search and Information Retrieval
NER tags articles and content, improving search relevance by distinguishing entities like “Apple” (company vs. fruit).

### 2. Recommendation Engines
Streaming services recommend content based on extracted entities (actors, genres).

### 3. Document Automation & RPA
Extracts names, dates, and amounts from invoices, contracts, and forms for automated processing.

### 4. Knowledge Graph Construction
Creates structured graphs of entities and relationships from unstructured documents, powering analytics and AI.

### 5. Compliance & Privacy
Identifies and redacts PII in sensitive documents for GDPR, HIPAA, and other regulatory compliance.

  **Redaction Example:**  
  “Steve Jobs founded Apple in Cupertino.”  
  → “[PERSON] founded [ORG] in [LOCATION].”

### 6. Sentiment Analysis Enhancement
Associates sentiment with specific entities (e.g., “breakfast buffet” is negative, “room” is positive in hotel reviews).

### 7. Customer Support Automation
Routes tickets by extracting product names, course titles, or complaint subjects.

### 8. Domain-Specific NER
Biomedical (genes, proteins, diseases), legal (cases, statutes), financial (tickers, instruments), and more.

**Case Studies and Examples:**  
- [AltexSoft NER Applications](https://www.altexsoft.com/blog/named-entity-recognition/)
- [GeeksforGeeks: NER Applications](https://www.geeksforgeeks.org/nlp/named-entity-recognition/)

## Practical Implementation: Step-by-Step Example with spaCy

### Step 1: Install Required Libraries
```bash
pip install spacy
python -m spacy download en_core_web_sm
```

### Step 2: Load the spaCy Model
```python
import spacy
nlp = spacy.load("en_core_web_sm")
```

### Step 3: Process Text and Extract Entities
```python
content = "Steve Jobs and Steve Wozniak founded Apple on April 1, 1976 in Cupertino, California."
doc = nlp(content)
for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)
```

**Sample Output:**
```
Steve Jobs 0 10 PERSON
Steve Wozniak 15 29 PERSON
Apple 39 44 ORG
April 1, 1976 48 61 DATE
Cupertino 65 74 GPE
California 76 86 GPE
```

### Step 4: Visualize Entities
```python
from spacy import displacy
displacy.render(doc, style="ent")
```
![NER visualization with spaCy](https://www.altexsoft.com/static/blog-post/2024/3/afb1c9bf-f08e-4ad7-a4ec-ad9745dda06d.jpg)

### Step 5: Convert Entities to Structured Data
```python
import pandas as pd
entities = [(ent.text, ent.label_) for ent in doc.ents]
df = pd.DataFrame(entities, columns=['Entity', 'Type'])
print(df)
```

**Result:**

| Entity           | Type   |
|------------------|--------|
| Steve Jobs       | PERSON |
| Steve Wozniak    | PERSON |
| Apple            | ORG    |
| April 1, 1976    | DATE   |
| Cupertino        | GPE    |
| California       | GPE    |

**For further tutorials and code samples:**  
- [spaCy Named Entities Documentation](https://spacy.io/usage/linguistic-features#named-entities)
- [MachineLearningMastery: How to Do NER with BERT](https://machinelearningmastery.com/how-to-do-named-entity-recognition-ner-with-a-bert-model/)

## Leading NER Tools, Libraries, and APIs

| Tool/Library                   | Highlights / Best For                                               | Language(s)    | Reference |
|------------------------------- |---------------------------------------------------------------------|----------------|-----------|
| [spaCy](https://spacy.io/)     | Fast, production-ready, customizable, pre-trained models            | Python         | [spaCy Docs](https://spacy.io/usage/linguistic-features#named-entities) |
| [NLTK](https://www.nltk.org/)  | Educational, basic NER, linguistic analysis                         | Python         | [NLTK Docs](https://www.nltk.org/) |
| [Stanford CoreNLP](https://stanfordnlp.github.io/CoreNLP/) | Academic gold standard, RegexNER for rules, multi-language support | Java, Python   | [Stanford CoreNLP](https://stanfordnlp.github.io/CoreNLP/) |
| [Tonic Textual](https://www.tonic.ai/products/textual) | Enterprise NER, redaction, synthesis, custom models                | API, Python SDK| [Tonic Textual](https://www.tonic.ai/products/textual) |
| [DeepPavlov](https://deeppavlov.ai/) | Deep learning, pre-trained models, domain adaptation                | Python         | [DeepPavlov](https://deeppavlov.ai/) |
| [Google Cloud NLP](https://cloud.google.com/natural-language)
