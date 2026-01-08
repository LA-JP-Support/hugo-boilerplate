---
title: "N-Gram"
translationKey: "n-gram"
description: "An N-gram is a contiguous sequence of n items (words, characters, or symbols) from text or speech, fundamental in NLP for language modeling and text analysis."
keywords: ["N-gram", "Natural Language Processing", "Language Modeling", "Text Analysis", "Speech Recognition"]
category: "AI Chatbot & Automation"
type: "glossary"
date: 2025-12-05
lastmod: 2025-12-05
draft: false
---
## Definition and Overview

An **N-gram**is a contiguous sequence of *n* items from a given sample of text or speech. In the context of [Natural Language Processing (NLP)](https://en.wikipedia.org/wiki/Natural_language_processing), N-grams are typically sequences of words, characters, or symbols. The value of *n* determines the length of each chunk:

- For *n=1*, the model uses **unigrams**(single words or tokens).
- For *n=2*, it uses **bigrams**(two-word sequences).
- For *n=3*, it uses **trigrams**(three-word sequences).
- Higher-order N-grams (*n > 3*) are also used in cases where larger context is necessary.

N-gram models are fundamental to computational linguistics, providing statistical frameworks for understanding, generating, and predicting language. They are the backbone of many classical NLP systems, including spell-checkers, predictive text, machine translation, and speech recognition.

A language model based on N-grams assigns a probability to sequences of tokens, using statistical information about the co-occurrence of items in a large corpus. This enables systems to automatically suggest likely next words, correct errors, or generate human-like text.

*Source: [Stanford Speech and Language Processing, N-gram Language Models (PDF)](https://web.stanford.edu/~jurafsky/slp3/3.pdf)*

## Historical Context and Development

N-grams have a rich history in both linguistics and information theory. The mathematical formalization of N-grams can be traced back to Andrey Markov, whose work on **Markov chains**in the early 20th century laid the foundation for sequence modeling. Markov's insight was that the probability of an event could depend on the previous event(s) in a chain, rather than the entire history (the "Markov property").

In the 1940s and 1950s, Claude Shannon applied Markov models to English text, introducing the concept of N-gram models for language. Shannon's experiments demonstrated that statistical models could generate surprisingly human-like text, laying the groundwork for computational linguistics.

By the 1980s and 1990s, with the rise of digital corpora and increased computational power, N-gram models became the standard approach for tasks such as speech recognition, optical character recognition (OCR), and early machine translation systems. Their simplicity, interpretability, and effectiveness made them a baseline in many NLP pipelines.

Today, while advanced neural architectures like [Transformers](https://www.geeksforgeeks.org/machine-learning/getting-started-with-transformers/) have surpassed N-gram models in many tasks, N-grams remain essential for feature engineering, baseline comparisons, and applications where efficiency and [transparency](/en/glossary/transparency/) are critical.

*Further reading: [Wikipedia: N-gram](https://en.wikipedia.org/wiki/N-gram)*

## Types of N-grams

### Unigrams

- **Definition:**Sequences of single items (usually words).
- **Example:**Text: "[Natural language processing](/en/glossary/natural-language-processing--nlp-/) is fun."  
  Unigrams: "Natural", "language", "processing", "is", "fun"
- **Use Cases:**Basic word frequency analysis, text classification, information retrieval.

### Bigrams

- **Definition:**Sequences of two consecutive items.
- **Example:**Text: "Natural language processing is fun."  
  Bigrams: "Natural language", "language processing", "processing is", "is fun"
- **Use Cases:**Phrase detection, [sentiment analysis](/en/glossary/sentiment-analysis/) ("not good"), speech recognition.

### Trigrams

- **Definition:**Sequences of three consecutive items.
- **Example:**Text: "Natural language processing is fun."  
  Trigrams: "Natural language processing", "language processing is", "processing is fun"
- **Use Cases:**Capturing broader context, autocomplete, spelling correction.

### Higher-order N-grams

- **Definition:**Sequences of four or more consecutive items (e.g., 4-grams, 5-grams).
- **Example:**For "Natural language processing is fun."  
  4-gram: "Natural language processing is", "language processing is fun"
- **Use Cases:**Domain-specific language modeling, plagiarism detection.
- **Considerations:**As *n* increases, the number of possible N-grams grows exponentially, leading to data sparsity and computational overhead.

*Source: [GeeksforGeeks: N-gram in NLP](https://www.geeksforgeeks.org/nlp/n-gram-in-nlp/)*

## How N-gram Models Work

### Probability Estimation

N-gram models estimate the probability of a word or token based on the preceding *n-1* items. The **chain rule of probability**expresses the joint probability of a sequence as a product of conditional probabilities:

\[
P(w_1, w_2, \ldots, w_n) = P(w_1) \cdot P(w_2|w_1) \cdot P(w_3|w_1, w_2) \cdots P(w_n|w_1, \ldots, w_{n-1})
\]

This formula is computationally expensive for long sequences. N-gram models simplify this by making the **Markov assumption**.

### Markov Assumption

The **Markov assumption**posits that the probability of a word depends only on the previous *n-1* words, not the entire preceding context. This is crucial for practical computation.

For a bigram (*n=2*):
\[
P(w_n | w_1, w_2, ..., w_{n-1}) \approx P(w_n | w_{n-1})
\]

For a trigram (*n=3*):
\[
P(w_n | w_1, ..., w_{n-1}) \approx P(w_n | w_{n-2}, w_{n-1})
\]

This assumption dramatically reduces the number of parameters and makes language modeling feasible on real-world data.

*Source: [Stanford Speech and Language Processing, N-gram Language Models (PDF)](https://web.stanford.edu/~jurafsky/slp3/3.pdf)*

### Maximum Likelihood Estimation (MLE)

MLE is used to estimate N-gram probabilities from observed data. The general formula for an N-gram model is:

\[
P(w_n | w_{n-N+1}, ..., w_{n-1}) = \frac{C(w_{n-N+1}, ..., w_n)}{C(w_{n-N+1}, ..., w_{n-1})}
\]

Where:
- \(C(w_{n-N+1}, ..., w_n)\): Count of the N-gram in the corpus.
- \(C(w_{n-N+1}, ..., w_{n-1})\): Count of the (N-1)-gram prefix.

For bigrams, this becomes:
\[
P(w_n | w_{n-1}) = \frac{C(w_{n-1}, w_n)}{C(w_{n-1})}
\]

**Example Calculation:**Given the corpus:
- "I am Sam"
- "Sam I am"
- "I do not like green eggs and ham"

To calculate \(P(am | I)\):
- Count of "I am": 2
- Count of "I": 3
- \(P(am | I) = 2/3\)

*See full calculation and mathematical derivation in [Stanford Speech and Language Processing, Chapter 3](https://web.stanford.edu/~jurafsky/slp3/3.pdf).*

### Smoothing Techniques

#### The Need for Smoothing

As *n* increases, many valid N-grams may not appear in the training data, resulting in zero probability estimates. This is called **data sparsity**. Smoothing techniques adjust probability estimates to account for unseen N-grams, improving generalization.

#### Laplace (Additive) Smoothing

Laplace smoothing simply adds a small constant (usually 1) to all N-gram counts:

\[
P_{Laplace}(w_n | w_{n-1}) = \frac{C(w_{n-1}, w_n) + 1}{C(w_{n-1}) + V}
\]

Where:
- \(V\) is the vocabulary size.

This ensures no N-gram has zero probability.

#### Advanced Smoothing: Good-Turing, Kneser-Ney

- **Good-Turing Smoothing:**Adjusts N-gram frequencies based on the number of N-grams seen once, twice, etc.
- **Kneser-Ney Smoothing:**State-of-the-art for language modeling, considers both the frequency and the distribution of contexts in which an N-gram appears.

*Detailed explanation: [Stanford PDF, Section 3.4](https://web.stanford.edu/~jurafsky/slp3/3.pdf)*

### Perplexity and Entropy

- **Perplexity**is a measure of how well a probability model predicts a sample. Lower perplexity indicates a better language model.
  \[
  Perplexity(P) = 2^{H(P)}
  \]
  where \(H(P)\) is the entropy of the probability distribution.
- **Entropy**measures the unpredictability of the text.

*More details: [Stanford PDF, Section 3.5](https://web.stanford.edu/~jurafsky/slp3/3.pdf)*

### Python Implementation Example

#### Basic N-gram Extraction

```python
def generate_ngrams(text, n):
    tokens = text.split()
    ngrams = [tuple(tokens[i:i + n]) for i in range(len(tokens) - n + 1)]
    return ngrams

text = "Geeks for Geeks Community"

unigrams = generate_ngrams(text, 1)
bigrams = generate_ngrams(text, 2)
trigrams = generate_ngrams(text, 3)

print("Unigrams:", unigrams)
print("Bigrams:", bigrams)
print("Trigrams:", trigrams)
```

#### Output
```
Unigrams: [('Geeks',), ('for',), ('Geeks',), ('Community',)]
Bigrams: [('Geeks', 'for'), ('for', 'Geeks'), ('Geeks', 'Community')]
Trigrams: [('Geeks', 'for', 'Geeks'), ('for', 'Geeks', 'Community')]
```

#### Laplace Smoothing Example

```python
from collections import Counter

def laplace_smoothing(ngrams, vocab_size):
    ngram_counts = Counter(ngrams)
    smoothed_ngrams = {ngram: (count + 1) / (len(ngrams) + vocab_size)
                       for ngram, count in ngram_counts.items()}
    return smoothed_ngrams

ngrams = [('Geeks', 'for'), ('for', 'Geeks'), ('Geeks', 'Community')]
vocab_size = 5

smoothed_ngrams = laplace_smoothing(ngrams, vocab_size)
print("Smoothed N-grams:", smoothed_ngrams)
```

**Output:**```
Smoothed N-grams: {('Geeks', 'for'): 0.25, ('for', 'Geeks'): 0.25, ('Geeks', 'Community'): 0.25}
```

#### NLTK Example

```python
import nltk
words = nltk.word_tokenize("I am going to the store")
bigrams = list(nltk.ngrams(words, 2))
trigrams = list(nltk.ngrams(words, 3))
print("Bigrams:", bigrams)
print("Trigrams:", trigrams)
```

## Feature Engineering with N-grams

N-gram features are widely used in NLP for machine learning models. They serve as the backbone for classical text classifiers, information retrieval, and more.

### Bag-of-N-grams Model

The **Bag-of-N-grams**approach represents a document as a sparse vector, where each dimension corresponds to an N-gram from the vocabulary. The value is usually the frequency of the N-gram in the document.

#### Example: Python with SciPy

```python
import scipy.sparse as sp
import numpy as np

def extract_ngrams(text, n):
    ngrams_list = []
    for i in range(len(text) - n + 1):
        ngrams_list.append(tuple(text[i:i + n]))
    return ngrams_list

def build_bag_of_ngrams(text, n, vocabulary):
    ngrams_list = extract_ngrams(text, n)
    ngrams_index = {ngram: i for i, ngram in enumerate(vocabulary)}
    col = [ngrams_index[ngram] for ngram in ngrams_list if ngram in ngrams_index]
    data = [1] * len(col)
    row = [0] * len(col)
    vector = sp.csr_matrix((data, (row, col)), shape=(1, len(vocabulary)))
    return vector
```

### Skip-grams and Subword N-grams

- **Skip-grams:**Non-contiguous N-grams (e.g., "I ... Sam" in "I am Sam"), useful for capturing longer-range dependencies.
- **Subword N-grams:**Character-level or syllable-based N-grams, essential for handling languages with rich morphology or noisy data (e.g., Twitter, OCR).

### Sequence Representation

Instead of a bag-of-N-grams, some models use sequence representations (ordered lists of N-grams) as input for sequential models such as [Hidden Markov Models](https://www.geeksforgeeks.org/machine-learning/hidden-markov-model-in-machine-learning/), [RNNs](https://www.geeksforgeeks.org/understanding-rnn-recurrent-neural-network/), or [Transformers](https://www.geeksforgeeks.org/machine-learning/getting-started-with-transformers/).

*Source: [A Comprehensive Guide To Feature Engineering with N-Grams For NLP](https://www.linkedin.com/pulse/comprehensive-guide-feature-engineering-n-grams-david-adamson-mbcs)*

## Applications of N-grams

N-grams are foundational in numerous NLP and AI automation tasks:

- **Language Modeling:**Predict the next word in a sentence, powering autocomplete, predictive typing, and chatbot responses.
- **Text Classification:**Feature extraction for categorizing documents (topics, sentiment). Bigrams like "not good" improve sentiment classifiers.
- **Speech Recognition:**Model word sequences to enhance transcription accuracy.
- **Spelling Correction:**Suggests corrections based on likely word sequences (e.g., "from" vs. "form").
- **Machine Translation:**Statistical translation systems use N-gram probabilities to construct target-language sentences.
- **Information Retrieval:**Search engines use N-grams for indexing and ranking documents.
- **Plagiarism Detection:**Detects overlapping sequences in documents.
- **Predictive Typing/Autocomplete:**Suggests next words as users type, using frequent N-gram sequences.

**Concrete Examples:**- In sentiment analysis, bigrams such as "very good" or "poor quality" strongly indicate positive or negative sentiment.
- Google search suggestions are powered by analyzing frequent trigrams: typing "how to" yields "how to cook", "how to code", based on N-gram frequency.

*Source: [GeeksforGeeks: N-gram in NLP](https://www.geeksforgeeks.org/nlp/n-gram-in-nlp/)*

## Advanced Topics

### Data Sparsity and Dimensionality

With higher values of *n*, the number of possible N-grams increases exponentially. For example, a vocabulary of 10,000 words yields:

- 10,000 unigrams
- 100,000,000 bigrams
- 1,000,000,000,000 trigrams

This causes:
- **Data sparsity:**Many N-grams never appear in the corpus.
- **High dimensionality:**Storage and computation become challenging.

### N-gram Backoff and Interpolation

**Backoff:**If a higher-order N-gram
