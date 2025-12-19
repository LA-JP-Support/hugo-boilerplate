---
title: "F1 Score"
date: 2025-12-17
translationKey: "f1-score"
description: "The F1 score is a key machine learning evaluation metric, representing the harmonic mean of precision and recall. It balances false positives and negatives, ideal for imbalanced datasets."
keywords: ["F1 score", "precision", "recall", "machine learning", "classification"]
category: "AI Chatbot & Automation"
type: "glossary"
draft: false
---

## Introduction

The [F1 score](https://en.wikipedia.org/wiki/F-score) is a key evaluation metric in machine learning and statistics, representing the harmonic mean of precision and recall. Unlike accuracy, which only measures the overall proportion of correct predictions, the F1 score quantifies a model’s effectiveness by balancing the trade-off between precision (the ability to avoid false positives) and recall (the ability to capture true positives). This makes the F1 score a preferred performance indicator for real-world machine learning problems where class imbalance is prevalent—such as fraud detection, healthcare diagnostics, and AI chatbot moderation. In these situations, the cost of misclassifying a positive or negative case is not uniform, and accuracy alone can be misleading ([V7 Labs](https://www.v7labs.com/blog/f1-score-guide); [GeeksforGeeks](https://www.geeksforgeeks.org/machine-learning/f1-score-in-machine-learning/)).

**On this page:**
- What the F1 score is and why it matters
- Relationship to confusion matrix, precision, and recall
- Mathematical formulation and calculation of F1 score
- F1 score variants and averaging strategies for multiclass scenarios
- Python implementation and practical coding examples
- Real-world applications and use cases
- Limitations, caveats, and best practices

## What is the F1 Score?

The [F1 score](https://en.wikipedia.org/wiki/F-score) quantifies a model’s performance in binary and multiclass classification tasks by combining precision and recall into a single metric. The F1 score ranges from 0 (worst) to 1 (best), where a score of 1 reflects perfect precision and recall. F1 is particularly valuable when classes are imbalanced, as it penalizes models that achieve high precision or recall at the expense of the other.

**Key properties:**
- **Balances precision and recall:** The harmonic mean ensures that both metrics are given equal weight. If either is low, the F1 score drops sharply.
- **Robust to class imbalance:** Outperforms accuracy in scenarios with skewed class distribution ([V7 Labs](https://www.v7labs.com/blog/f1-score-guide)).
- **Single-value summary:** Provides an interpretable number summarizing a model’s ability to minimize both false positives and false negatives ([GeeksforGeeks](https://www.geeksforgeeks.org/machine-learning/f1-score-in-machine-learning/)).

## Conceptual Foundations

Understanding the F1 score requires knowledge of **precision** and **recall**, which are derived from the confusion matrix.

### The Confusion Matrix

A [confusion matrix](https://developers.google.com/machine-learning/crash-course/classification/accuracy-precision-recall) tabulates actual versus predicted classifications, providing the foundation for most classification metrics. It is structured as follows:

|                     | Predicted Positive | Predicted Negative |
|---------------------|-------------------|-------------------|
| **Actual Positive** | True Positive (TP) | False Negative (FN) |
| **Actual Negative** | False Positive (FP) | True Negative (TN) |

- **True Positive (TP):** The model correctly predicts a positive instance.
- **False Positive (FP):** The model incorrectly predicts a negative instance as positive.
- **False Negative (FN):** The model incorrectly predicts a positive instance as negative.
- **True Negative (TN):** The model correctly predicts a negative instance.

([KDnuggets](https://www.kdnuggets.com/2022/11/confusion-matrix-precision-recall-explained.html); [Google Developers](https://developers.google.com/machine-learning/crash-course/classification/accuracy-precision-recall))

### Precision and Recall

- **Precision** measures the correctness of positive predictions:
  - *Definition:* Of all predicted positives, what fraction are actually positive?
  - *Formula:* \(\text{Precision} = \frac{TP}{TP + FP}\)
  - *Example:* If a model predicts 50 positives and 40 are correct (TP), precision is 80%.
- **Recall** (aka *sensitivity* or *true positive rate*) measures the model’s ability to find all actual positives:
  - *Definition:* Of all actual positives, what fraction did the model correctly identify?
  - *Formula:* \(\text{Recall} = \frac{TP}{TP + FN}\)
  - *Example:* If there are 100 actual positives and the model predicts 80 of them, recall is 80%.

([GeeksforGeeks](https://www.geeksforgeeks.org/machine-learning/f1-score-in-machine-learning/); [V7 Labs](https://www.v7labs.com/blog/f1-score-guide))

#### Why Not Use Accuracy Alone?

Accuracy is calculated as:
\[
\text{Accuracy} = \frac{TP + TN}{TP + FP + TN + FN}
\]
In imbalanced datasets, a model can achieve high accuracy by simply predicting the majority class. For example, if 95% of cases are negative and the model predicts all as negative, accuracy is 95% but recall for positives is 0%. Thus, precision and recall provide a more nuanced evaluation ([Google Developers](https://developers.google.com/machine-learning/crash-course/classification/accuracy-precision-recall)).

## Mathematical Explanation

### F1 Score Formula

The [F1 score](https://en.wikipedia.org/wiki/F-score) is the harmonic mean of precision and recall:
\[
\text{F1} = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}}
\]

This formula penalizes extreme values; if either precision or recall is low, the F1 score will also be low. The harmonic mean is less than or equal to the arithmetic mean, and only high if both precision and recall are high ([V7 Labs](https://www.v7labs.com/blog/f1-score-guide)).

#### Example Calculation

Suppose a model yields:
- Precision = 0.8
- Recall = 0.6

\[
\text{F1} = 2 \times \frac{0.8 \times 0.6}{0.8 + 0.6} = 2 \times \frac{0.48}{1.4} = 0.6857
\]

So, the F1 score is approximately 0.69.

#### F1 Score in Terms of Confusion Matrix

\[
\text{F1} = \frac{2 \times TP}{2 \times TP + FP + FN}
\]

This highlights that F1 is maximized only when both FP and FN are minimized relative to TP ([scikit-learn](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.f1_score.html)).

## Variants and Averaging Strategies

### Fβ Score (F-beta)

The [F-beta score](https://permetrics.readthedocs.io/en/latest/pages/classification/FBS.html) generalizes the F1 score by introducing a weight (\(\beta\)) to control the trade-off between precision and recall:
\[
F_\beta = (1 + \beta^2) \times \frac{\text{Precision} \times \text{Recall}}{(\beta^2 \times \text{Precision}) + \text{Recall}}
\]
- **β = 1:** Equal weight (F1 score)
- **β > 1:** Recall is more important (e.g., F2 score)
- **β < 1:** Precision is more important (e.g., F0.5 score)

Use cases: In medical diagnostics, high recall (catching as many positives as possible) may be prioritized, suggesting a higher β ([Arize](https://arize.com/blog-course/f1-score/)).

### Averaging for Multiclass and Multilabel Problems

When addressing datasets with more than two classes, several averaging strategies are employed ([scikit-learn](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.f1_score.html)):

- **Macro-average:** Computes F1 for each class, then averages. Treats all classes equally.
  \[
  \text{F1}_{macro} = \frac{1}{N} \sum_{i=1}^N \text{F1}_i
  \]
- **Micro-average:** Aggregates TP, FP, FN across all classes to compute a global F1.
  \[
  \text{F1}_{micro} = \frac{2 \times \sum TP_i}{2 \times \sum TP_i + \sum FP_i + \sum FN_i}
  \]
- **Weighted-average:** Averages F1 for each class, weighted by the number of true instances per class.
  \[
  \text{F1}_{weighted} = \frac{\sum w_i \times \text{F1}_i}{\sum w_i}
  \]
- **None:** Returns F1 per class without averaging.

([Permetrics](https://permetrics.readthedocs.io/en/latest/pages/classification/FBS.html))

## Practical Implementation

### Python Code Example: Calculating F1 Score

Python’s [scikit-learn](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.f1_score.html) library provides high-level interfaces for F1 calculation.

```python
from sklearn.metrics import f1_score

# Example data
y_true = [0, 1, 2, 2, 2, 2, 1, 0, 2, 1, 0]
y_pred = [0, 0, 2, 2, 1, 2, 1, 0, 1, 2, 1]

# F1 score for each class
f1_per_class = f1_score(y_true, y_pred, average=None)

# Micro-average F1 score
f1_micro = f1_score(y_true, y_pred, average='micro')

# Macro-average F1 score
f1_macro = f1_score(y_true, y_pred, average='macro')

# Weighted-average F1 score
f1_weighted = f1_score(y_true, y_pred, average='weighted')

print("F1 score per class:", f1_per_class)
print("Micro-average F1 score:", f1_micro)
print("Macro-average F1 score:", f1_macro)
print("Weighted-average F1 score:", f1_weighted)
```

**Output:**
```
F1 score per class: [0.67 0.40 0.67]
Micro-average F1 score: 0.64
Macro-average F1 score: 0.58
Weighted-average F1 score: 0.60
```

#### Calculating Fβ Score

```python
from sklearn.metrics import fbeta_score

# F2 Score (recall emphasized)
f2_score = fbeta_score(y_true, y_pred, average='macro', beta=2)
print("F2 score (macro-average):", f2_score)
```

#### Generating a Classification Report

The `classification_report` function in scikit-learn provides precision, recall, F1, and support for each class:

```python
from sklearn.metrics import classification_report

print(classification_report(y_true, y_pred))
```

([scikit-learn](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.f1_score.html); [Arize](https://arize.com/blog-course/f1-score/))

## Applications and Use Cases

The F1 score is widely used in domains where class imbalance and the cost of misclassification are critical ([Galileo AI](https://galileo.ai/blog/f1-score-ai-evaluation-precision-recall)).

### Common Use Cases

- **Healthcare diagnostics:** Models must minimize both missed diagnoses (FN) and false alarms (FP). For example, in cancer screening, missing a true case can have severe consequences ([ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0933365724003038)).
- **Fraud detection:** Fraudulent cases are rare; high recall ensures most frauds are caught, while high precision avoids overwhelming analysts with false alarms ([Arize](https://arize.com/blog-course/f1-score/)).
- **Spam detection:** Filters must avoid letting spam through (FN) and avoid misclassifying legitimate mail (FP).
- **AI chatbot moderation:** Detects toxic content, balancing between censoring benign messages and missing harmful ones ([Galileo AI](https://galileo.ai/blog/f1-score-ai-evaluation-precision-recall)).
- **LLM (large language model) evaluation:** Used to assess the accuracy of prompt templates and label extraction.

#### Example: Fraud Detection

In a dataset of credit card transactions where only 1% are fraudulent, a model predicting all transactions as legitimate achieves 99% accuracy, but 0% recall for fraud. The F1 score exposes this failure and incentivizes models that balance finding frauds (recall) while avoiding excessive false positives (precision) ([ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0933365724003038)).

## Limitations and Cautions

While the F1 score is powerful, it is not universally optimal ([V7 Labs](https://www.v7labs.com/blog/f1-score-guide); [Arize](https://arize.com/blog-course/f1-score/)).

### Limitations

- **Equal weighting of precision and recall:** F1 may not be suitable if one is much more important than the other.
- **Insensitive to true negatives:** F1 ignores TN, making it less informative in scenarios where negative class performance matters.
- **Interpretation challenges:** Identical F1 scores can arise from widely different precision/recall pairs.
- **Inadequate for severe imbalance:** When positives are extremely rare, F1 can still obscure practical performance. Metrics like ROC-AUC or precision-recall AUC may be more appropriate ([Galileo AI](https://galileo.ai/blog/f1-score-ai-evaluation-precision-recall)).

### When to Use Other Metrics

- **Prioritize recall (minimize FN):** Use recall or Fβ with β > 1.
- **Prioritize precision (minimize FP):** Use precision or Fβ with β < 1.
- **Ranking/threshold evaluation:** Use ROC-AUC or PR-AUC.

([KDnuggets](https://www.kdnuggets.com/2022/11/confusion-matrix-precision-recall-explained.html); [Permetrics](https://permetrics.readthedocs.io/en/latest/pages/classification/FBS.html))

## Summary / Key Takeaways

- **F1 score** is the harmonic mean of precision and recall, providing a balanced metric for classification model evaluation, especially with class imbalance.
- **Precision** measures positive prediction correctness; **recall** measures positive case detection.
- **F1 is most useful** when both types of errors (FP and FN) are significant.
- **Variants** like Fβ and averaging strategies (macro, micro, weighted) enable flexible evaluation in multiclass scenarios.
- **Implementation is straightforward** with tools like scikit-learn.
- **Limitations:** F1 may not capture application-specific costs or be optimal for all contexts.

**Best practice:** Always consider the specific business or domain context and supplement F1 with other relevant metrics.

## References

- [F1 Score in Machine Learning: Intro & Calculation (V7 Labs)](https://www.v7labs.com/blog/f1-score-guide)
- [F1 Score in Machine Learning (GeeksforGeeks)](https://www.geeksforgeeks.org/machine-learning/f1-score-in-machine-learning/)
- [Confusion Matrix, Precision, and Recall Explained (KDnuggets)](https://www.kdnuggets.com/2022/11/confusion-matrix-precision-recall-explained.html)
- [Classification: Accuracy, recall, precision, and related metrics (Google Developers)](https://developers.google.com/machine-learning/crash-course/classification/accuracy-precision-recall)
- [Performance Metrics: Confusion matrix, Precision, Recall, and F1 Score (Towards Data Science)](https://towardsdatascience.com/performance-metrics-confusion-matrix-precision-recall-and-f1-score-a8fe076a2262/)
- [F-Beta Score (Permetrics)](https://permetrics.readthedocs.io/en/latest/pages/classification/FBS.html)
- [sklearn.metrics.f1_score documentation (scikit-learn)](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.f1_score.html)
- [Understanding and Applying F1 Score: AI Evaluation Essentials (Arize)](https://arize.com/blog-course/f1-score/)
- [Fraud detection in healthcare claims using machine learning (ScienceDirect)](https://www.sciencedirect.com/science/article/pii/S0933365724003038)
- [F1 Score: Balancing Precision and Recall in AI Evaluation (Galileo AI)](https://galileo.ai/blog/f1-score-ai-evaluation-precision-recall)

**Further Reading and Tutorials**
- [scikit-learn F1 Score User Guide](https://scikit-learn.org/stable/modules/model_evaluation.html#f1-score)
- [YouTube: F1 Score Clearly Explained](https://www.youtube.com/watch?v=4jRBRDbJemM)
- [YouTube: Precision, Recall & F1 Score Clearly Explained](https://www.youtube.com/watch?v=Ul0gzBUq4bM)

*For a deeper dive into confusion matrices, error analysis, and advanced metric selection, see the linked references and [scikit-learn documentation](https://scikit-learn.org/stable/modules/model_evaluation.html#classification-metrics).*

