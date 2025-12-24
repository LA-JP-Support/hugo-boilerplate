---
title: Precision and Recall
translationKey: precision-and-recall
description: "Precision and Recall are two key metrics that measure how well a classification model performs. Precision shows how accurate the model's positive predictions are, while recall shows how many actual positives the model successfully identifies."
keywords:
- precision
- recall
- machine learning
- classification metrics
- confusion matrix
category: AI Chatbot & Automation
type: glossary
date: 2025-12-18
lastmod: 2025-12-18
draft: false
---

## What Are Precision and Recall?

Precision and recall are two of the most widely used evaluation metrics in supervised machine learning, particularly for classification and information retrieval tasks. Together, they provide complementary insights into model performance that accuracy alone cannot capture, especially when dealing with imbalanced datasets or scenarios where different types of errors carry different costs.

**Precision** measures the proportion of positive predictions that are actually correct. It answers: "Of all instances the model labeled as positive, how many were actually positive?" High precision means few false positives—when the model predicts something is positive, it's usually right.

**Recall** (also called sensitivity or true positive rate) measures the proportion of actual positives correctly identified by the model. It answers: "Of all true positives in the data, how many did the model catch?" High recall means few false negatives—the model finds most of the actual positive cases.

These metrics are vital for evaluating models when datasets are imbalanced, when costs of false positives and false negatives differ significantly, or when specific business requirements demand minimizing particular types of errors. Understanding and balancing precision and recall, alongside related measures such as F1 score and ROC-AUC, ensures robust, context-aware assessment and deployment of AI and automation systems.

## The Confusion Matrix Foundation

Precision and recall are both derived from the confusion matrix, which summarizes classification results in a 2x2 table:

|  | Predicted Positive | Predicted Negative |
|---|---|---|
| **Actual Positive** | True Positive (TP) | False Negative (FN) |
| **Actual Negative** | False Positive (FP) | True Negative (TN) |

**True Positive (TP):** Model correctly predicted a positive instance

**False Positive (FP):** Model incorrectly predicted positive (was actually negative)

**True Negative (TN):** Model correctly predicted a negative instance

**False Negative (FN):** Model incorrectly predicted negative (was actually positive)

The confusion matrix is the starting point for almost all classification evaluation metrics, including precision, recall, F1 score, accuracy, and specificity.

## Precision: Definition and Formula

### Definition

Precision measures the correctness of positive predictions. It quantifies what fraction of predicted positives are actually positive.

### Formula

```
Precision = TP / (TP + FP)
```

### Intuition

Precision is high when the model makes very few false positive errors. When it predicts "positive," it's usually correct.

**High Precision:** Few false alarms; most positive predictions are true

**Low Precision:** Many false alarms; positive predictions are often wrong

### When Precision Matters

Precision is especially important when the cost of a false positive is high:

- **Spam Detection:** High precision ensures legitimate emails are rarely marked as spam
- **Legal Document Review:** Incorrectly labeling non-relevant documents as relevant wastes expensive attorney time
- **Medical Screening:** False positives cause unnecessary stress, follow-up procedures, and costs

### Limitations

Over-optimizing for precision may cause the model to miss many true positives, reducing recall. If the model only predicts "positive" when very confident, it may rarely make positive predictions, leading to high precision but low recall.

## Recall: Definition and Formula

### Definition

Recall measures the ability of the model to find all actual positive instances. It quantifies what fraction of actual positives the model correctly identified.

### Formula

```
Recall = TP / (TP + FN)
```

### Intuition

Recall is high when the model misses very few actual positive cases.

**High Recall:** The model finds most of the positives (few false negatives)

**Low Recall:** The model misses many positives (many false negatives)

### When Recall Matters

Recall is crucial when missing a positive case has high costs:

- **Medical Diagnosis:** Missing a disease (false negative) can be fatal; high recall ensures most sick patients are found
- **Fraud Detection:** Missing a fraudulent transaction is costly
- **Safety-Critical Systems:** Failing to detect hazards can cause serious harm

### Limitations

Over-optimizing for recall may cause the model to make many false positive errors, reducing precision. If the model labels almost everything as positive, recall will be high but precision will suffer.

## Calculating Precision and Recall: Example

**Scenario:** Detecting fraudulent credit card transactions

- **Dataset:** 1,000 transactions; 50 are fraudulent (positive class), 950 are legitimate
- **Model predicts:** 40 transactions as fraud
  - 30 are truly fraudulent (TP = 30)
  - 10 are legitimate but flagged (FP = 10)
- Out of 50 actual frauds, 20 are missed (FN = 20)
- Model correctly identifies 940 as legitimate (TN = 940)

**Confusion Matrix:**

|  | Predicted Fraud | Predicted Legitimate |
|---|---|---|
| **Actual Fraud** | 30 (TP) | 20 (FN) |
| **Actual Legitimate** | 10 (FP) | 940 (TN) |

**Calculations:**

**Precision:** TP / (TP + FP) = 30 / (30 + 10) = 0.75 or 75%
- *Interpretation: 75% of transactions flagged as fraud were truly fraudulent*

**Recall:** TP / (TP + FN) = 30 / (30 + 20) = 0.60 or 60%
- *Interpretation: The model identified 60% of all fraud cases*

## Precision vs. Recall Trade-offs

Precision and recall typically trade off against each other:

| Metric | Optimize When | Risk If Maximized Alone | Example Application |
|--------|---------------|------------------------|---------------------|
| Precision | False positives are costly | Misses true positives (low recall) | Spam detection, legal review |
| Recall | False negatives are costly | Many false positives (low precision) | Medical screening, fraud detection |

### The Precision-Recall Balance

**High precision, low recall:** Model rarely makes positive predictions but they are mostly correct

**High recall, low precision:** Model finds most positives but also incorrectly labels many negatives as positives

### Threshold Dependence

The balance between precision and recall can be adjusted using the model's decision threshold:

- **Lowering the threshold** increases recall but reduces precision
- **Raising the threshold** increases precision but reduces recall

Precision-recall curves plot precision vs. recall at various thresholds, helping identify optimal operating points.

## When to Use Precision, Recall, or Both

**Focus on Precision When:**
- False positives have high costs (e.g., marking important emails as spam)
- Resources for investigating predictions are limited
- User trust depends on prediction accuracy

**Focus on Recall When:**
- False negatives have high costs (e.g., missing cancer diagnosis)
- Finding all positive cases is critical regardless of false alarms
- Follow-up processes can filter false positives efficiently

**Balance Both When:**
- Most real-world problems require considering both metrics
- Both false positives and false negatives have consequences
- Use F1 score or precision-recall curves for optimization

## Related Metrics

### F1 Score

The F1 score is the harmonic mean of precision and recall:

```
F1 = 2 × (Precision × Recall) / (Precision + Recall)
```

Use when you need a single metric that balances precision and recall, especially for imbalanced datasets.

### Accuracy

```
Accuracy = (TP + TN) / (TP + FP + TN + FN)
```

**Limitation:** Can be misleading when classes are imbalanced. A model predicting all negatives in a 99:1 imbalanced dataset achieves 99% accuracy but 0% recall.

### ROC-AUC

**ROC Curve:** Plots true positive rate (recall) vs. false positive rate at different thresholds

**AUC:** Area under the ROC curve; measures model's ability to distinguish between classes across all thresholds

Useful for comparing models and visualizing trade-offs.

### Specificity

```
Specificity = TN / (TN + FP)
```

Measures the proportion of actual negatives correctly identified. Especially relevant in medical diagnostics, often used alongside recall (sensitivity).

## Best Practices

**Evaluate Both Metrics**

Report both precision and recall, not just accuracy. Single metrics can hide critical weaknesses.

**Use Confusion Matrix**

Understand model errors through the confusion matrix before optimizing metrics.

**Report F1 Score as Summary**

Include F1 score but always show precision and recall separately for complete understanding.

**Visualize Performance**

Use precision-recall curves and ROC curves to understand performance across thresholds.

**Adjust Thresholds**

Set decision thresholds to meet business or safety requirements rather than default values.

**Choose Metrics Based on Costs**

Select optimization targets based on real-world costs of different error types in your application.

**Complement with Additional Metrics**

For thorough evaluation, include specificity, ROC-AUC, and mean average precision.

## Common Pitfalls

**Ignoring Class Imbalance**

High accuracy can mask poor performance on rare classes; precision and recall provide better insight.

**Reporting Only One Metric**

Can hide critical weaknesses; always report both precision and recall.

**Threshold Sensitivity**

Precision and recall values depend on the decision threshold; evaluate across multiple thresholds or use curves.

**Undefined Values**

If there are no positive predictions (TP + FP = 0), precision is undefined. Handle edge cases appropriately.

## Use Case Examples

| Domain | Use Case | Priority | Reason |
|--------|----------|----------|---------|
| Medical Diagnosis | Disease screening | Recall | Missing a sick patient is highly consequential |
| Spam Detection | Email filtering | Precision | Marking real email as spam is disruptive |
| Fraud Detection | Transaction monitoring | Recall | Missing fraud is costly |
| Search Engines | Document retrieval | Both | Users want all relevant and few irrelevant results |
| Image Recognition | Object detection | Contextual | Depends on cost of missed or extra detections |

## References


1. Google. (n.d.). ML Crash Course: Accuracy, Precision, Recall. Google Developers.

2. EvidentlyAI. (n.d.). Accuracy vs Precision vs Recall. EvidentlyAI Blog.

3. EvidentlyAI. (n.d.). Confusion Matrix Explained. EvidentlyAI Blog.

4. EvidentlyAI. (n.d.). Classification Metrics Guide. EvidentlyAI Blog.

5. GeeksforGeeks. (n.d.). Precision and Recall in Machine Learning. GeeksforGeeks.

6. DeepAI. (n.d.). Precision and Recall. DeepAI Machine Learning Glossary.

7. DeepAI. (n.d.). ROC Curve. DeepAI Machine Learning Glossary.

8. BuiltIn. (n.d.). Precision and Recall. BuiltIn.

9. BuiltIn. (n.d.). F1 Score and Advanced Metrics. BuiltIn.

10. Lyzr. (n.d.). Glossary - Precision and Recall. Lyzr.

11. scikit-learn. (n.d.). Precision-Recall Curves. scikit-learn Documentation.

12. StatQuest. (n.d.). Precision and Recall Clearly Explained. YouTube.

13. Corey Schafer. (n.d.). Precision and Recall Explained. YouTube.
