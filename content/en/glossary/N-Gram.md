---
title: "N-Gram"
translationKey: "n-gram"
description: "An N-gram is a sequence of consecutive words or characters used by computers to predict the next word you might type or to understand text patterns."
keywords: ["N-gram", "Natural Language Processing", "Language Modeling", "Text Analysis", "Speech Recognition"]
category: "AI Chatbot & Automation"
type: "glossary"
date: 2025-12-18
lastmod: 2025-12-18
draft: false
---

## What is an N-Gram?

An N-gram is a contiguous sequence of n items from a given sample of text or speech. In Natural Language Processing (NLP), N-grams are typically sequences of words, characters, or symbols. The value of n determines the length of each chunk—for n=1, the model uses unigrams (single words), for n=2, bigrams (two-word sequences), for n=3, trigrams (three-word sequences), and so forth.

N-gram models are fundamental to computational linguistics, providing statistical frameworks for understanding, generating, and predicting language. They are the backbone of many classical NLP systems including spell-checkers, predictive text, machine translation, and speech recognition.

A language model based on N-grams assigns probability to sequences of tokens, using statistical information about co-occurrence of items in large corpus. This enables systems to automatically suggest likely next words, correct errors, or generate human-like text.

## Historical Context

N-grams have rich history in both linguistics and information theory. Mathematical formalization can be traced back to Andrey Markov, whose work on Markov chains in early 20th century laid foundation for sequence modeling. Markov's insight was that probability of event could depend on previous event(s) in chain rather than entire history (the "Markov property").

In 1940s and 1950s, Claude Shannon applied Markov models to English text, introducing concept of N-gram models for language. Shannon's experiments demonstrated that statistical models could generate surprisingly human-like text, laying groundwork for computational linguistics.

By 1980s and 1990s, with rise of digital corpora and increased computational power, N-gram models became standard approach for tasks such as speech recognition, optical character recognition (OCR), and early machine translation systems. Their simplicity, interpretability, and effectiveness made them baseline in many NLP pipelines.

Today, while advanced neural architectures like Transformers have surpassed N-gram models in many tasks, N-grams remain essential for feature engineering, baseline comparisons, and applications where efficiency and transparency are critical.

## Types of N-Grams

### Unigrams

<strong>Definition:</strong>Sequences of single items (usually words).

<strong>Example:</strong>Text: "Natural language processing is fun."
Unigrams: "Natural", "language", "processing", "is", "fun"

<strong>Use Cases:</strong>Basic word frequency analysis, text classification, information retrieval.

### Bigrams

<strong>Definition:</strong>Sequences of two consecutive items.

<strong>Example:</strong>Text: "Natural language processing is fun."
Bigrams: "Natural language", "language processing", "processing is", "is fun"

<strong>Use Cases:</strong>Phrase detection, sentiment analysis ("not good"), speech recognition.

### Trigrams

<strong>Definition:</strong>Sequences of three consecutive items.

<strong>Example:</strong>Text: "Natural language processing is fun."
Trigrams: "Natural language processing", "language processing is", "processing is fun"

<strong>Use Cases:</strong>Capturing broader context, autocomplete, spelling correction.

### Higher-order N-grams

<strong>Definition:</strong>Sequences of four or more consecutive items (4-grams, 5-grams).

<strong>Example:</strong>For "Natural language processing is fun."
4-gram: "Natural language processing is", "language processing is fun"

<strong>Use Cases:</strong>Domain-specific language modeling, plagiarism detection.

<strong>Considerations:</strong>As n increases, number of possible N-grams grows exponentially, leading to data sparsity and computational overhead.

## How N-Gram Models Work

### Probability Estimation

N-gram models estimate probability of word or token based on preceding n-1 items. Chain rule of probability expresses joint probability of sequence as product of conditional probabilities.

This formula is computationally expensive for long sequences. N-gram models simplify this by making Markov assumption.

### Markov Assumption

Markov assumption posits that probability of word depends only on previous n-1 words, not entire preceding context. This is crucial for practical computation.

For bigram (n=2): P(wn | w1, w2, ..., wn-1) ≈ P(wn | wn-1)

For trigram (n=3): P(wn | w1, ..., wn-1) ≈ P(wn | wn-2, wn-1)

This assumption dramatically reduces number of parameters and makes language modeling feasible on real-world data.

### Maximum Likelihood Estimation

MLE is used to estimate N-gram probabilities from observed data. General formula for N-gram model is:

P(wn | wn-N+1, ..., wn-1) = C(wn-N+1, ..., wn) / C(wn-N+1, ..., wn-1)

Where:
- C(wn-N+1, ..., wn): Count of N-gram in corpus
- C(wn-N+1, ..., wn-1): Count of (N-1)-gram prefix

For bigrams: P(wn | wn-1) = C(wn-1, wn) / C(wn-1)

<strong>Example Calculation:</strong>Given corpus:
- "I am Sam"
- "Sam I am"
- "I do not like green eggs and ham"

To calculate P(am | I):
- Count of "I am": 2
- Count of "I": 3
- P(am | I) = 2/3

### Smoothing Techniques

<strong>The Need for Smoothing:</strong>As n increases, many valid N-grams may not appear in training data, resulting in zero probability estimates. This is called data sparsity. Smoothing techniques adjust probability estimates to account for unseen N-grams, improving generalization.

<strong>Laplace (Additive) Smoothing:</strong>Simply adds small constant (usually 1) to all N-gram counts:

P_Laplace(wn | wn-1) = (C(wn-1, wn) + 1) / (C(wn-1) + V)

Where V is vocabulary size. This ensures no N-gram has zero probability.

<strong>Advanced Smoothing:</strong>Good-Turing and Kneser-Ney smoothing adjust frequencies based on distribution of contexts and are state-of-the-art for language modeling.

### Perplexity and Entropy

<strong>Perplexity</strong>measures how well probability model predicts sample. Lower perplexity indicates better language model.

<strong>Entropy</strong>measures unpredictability of text.

## Python Implementation

### Basic N-gram Extraction

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

Output:
```
Unigrams: [('Geeks',), ('for',), ('Geeks',), ('Community',)]
Bigrams: [('Geeks', 'for'), ('for', 'Geeks'), ('Geeks', 'Community')]
Trigrams: [('Geeks', 'for', 'Geeks'), ('for', 'Geeks', 'Community')]
```

### Laplace Smoothing Example

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

### NLTK Example

```python
import nltk
words = nltk.word_tokenize("I am going to the store")
bigrams = list(nltk.ngrams(words, 2))
trigrams = list(nltk.ngrams(words, 3))
print("Bigrams:", bigrams)
print("Trigrams:", trigrams)
```

## Feature Engineering

### Bag-of-N-grams Model

Bag-of-N-grams approach represents document as sparse vector where each dimension corresponds to N-gram from vocabulary. Value is usually frequency of N-gram in document.

### Skip-grams and Subword N-grams

<strong>Skip-grams:</strong>Non-contiguous N-grams (e.g., "I ... Sam" in "I am Sam"), useful for capturing longer-range dependencies.

<strong>Subword N-grams:</strong>Character-level or syllable-based N-grams, essential for handling languages with rich morphology or noisy data (Twitter, OCR).

### Sequence Representation

Some models use sequence representations (ordered lists of N-grams) as input for sequential models such as Hidden Markov Models, RNNs, or Transformers.

## Applications

<strong>Language Modeling:</strong>Predict next word in sentence, powering autocomplete, predictive typing, and chatbot responses.

<strong>Text Classification:</strong>Feature extraction for categorizing documents (topics, sentiment). Bigrams like "not good" improve sentiment classifiers.

<strong>Speech Recognition:</strong>Model word sequences to enhance transcription accuracy.

<strong>Spelling Correction:</strong>Suggests corrections based on likely word sequences (e.g., "from" vs. "form").

<strong>Machine Translation:</strong>Statistical translation systems use N-gram probabilities to construct target-language sentences.

<strong>Information Retrieval:</strong>Search engines use N-grams for indexing and ranking documents.

<strong>Plagiarism Detection:</strong>Detects overlapping sequences in documents.

<strong>Predictive Typing/Autocomplete:</strong>Suggests next words as users type using frequent N-gram sequences.

## Advanced Topics

### Data Sparsity and Dimensionality

With higher values of n, number of possible N-grams increases exponentially. For example, vocabulary of 10,000 words yields:
- 10,000 unigrams
- 100,000,000 bigrams
- 1,000,000,000,000 trigrams

This causes data sparsity (many N-grams never appear in corpus) and high dimensionality (storage and computation become challenging).

### Backoff and Interpolation

<strong>Backoff:</strong>If higher-order N-gram is not found, back off to lower-order N-gram.

<strong>Interpolation:</strong>Combine probabilities from multiple N-gram orders, weighted by their reliability.

## Limitations

<strong>Fixed Context:</strong>Cannot capture dependencies beyond n-1 previous words.

<strong>Data Sparsity:</strong>Many valid N-grams may not appear in training corpus.

<strong>No Semantic Understanding:</strong>Treats words as discrete symbols without understanding meaning or synonyms.

<strong>Computational Complexity:</strong>Higher-order N-grams require exponentially more storage and computation.

## References


1. Jurafsky, D., & Martin, J. H. (n.d.). Stanford Speech and Language Processing: N-gram Language Models. Stanford University.

2. Wikipedia. (n.d.). N-gram. Wikipedia.

3. GeeksforGeeks. (n.d.). N-gram in NLP. GeeksforGeeks.

4. Adamson, D. (n.d.). Comprehensive Guide to Feature Engineering with N-Grams. LinkedIn.

5. GeeksforGeeks. (n.d.). Getting Started with Transformers. GeeksforGeeks.

6. GeeksforGeeks. (n.d.). Hidden Markov Model in Machine Learning. GeeksforGeeks.

7. GeeksforGeeks. (n.d.). Understanding RNN (Recurrent Neural Network). GeeksforGeeks.
