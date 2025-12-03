---
title: Precision and Recall
translationKey: precision-and-recall-glossary-and
description: Precision and recall are core metrics for evaluating classification and
  information retrieval systems. Precision measures correct positive predictions,
  recall finds all actual positives.
keywords:
- precision
- recall
- machine learning
- classification metrics
- confusion matrix
category: AI Chatbot & Automation
type: glossary
date: 2025-12-03
draft: false
---

## Category: AI Chatbot & Automation

**Definition:**  
Precision and recall are core metrics used to evaluate the performance of classification and information retrieval systems. Precision quantifies a model’s ability to correctly identify positive predictions, while recall measures the ability to find all actual positives. Both metrics are essential for understanding the strengths and weaknesses of models, especially in scenarios with imbalanced classes or when specific types of errors carry different costs.

## TL;DR (Quick Summary)

- **Precision:** Proportion of positive predictions that are actually correct.
- **Recall (Sensitivity/True Positive Rate):** Proportion of actual positives correctly identified by the model.
- These metrics are vital for evaluating models, particularly with imbalanced datasets or differing costs of false positives vs. false negatives.
- Precision and recall typically exhibit a trade-off: improving one can reduce the other.
- Use precision to minimize false positives and recall to minimize false negatives.
- Always report both metrics (and often the F1 score) for a balanced view of model performance.

## What Are Precision and Recall?

Precision and recall are two of the most widely used evaluation metrics in supervised machine learning, particularly for classification and information retrieval tasks.  
- **Precision:** Out of all instances that the model predicted as positive, what fraction were truly positive?
- **Recall:** Out of all actual positive instances in the dataset, how many did the model correctly identify?

Their importance increases when:
- The dataset is imbalanced (one class is much rarer than the other).
- The costs of false positives and false negatives are not the same.

**Authority references:**  
- [Google ML Crash Course: Precision & Recall](https://developers.google.com/machine-learning/crash-course/classification/accuracy-precision-recall)  
- [EvidentlyAI: Accuracy vs Precision vs Recall](https://www.evidentlyai.com/classification-metrics/accuracy-precision-recall)  

## Confusion Matrix: The Foundation

Precision and recall are both derived from the **confusion matrix**, which summarizes the results of a classification algorithm.

|                       | **Predicted Positive** | **Predicted Negative** |
|-----------------------|-----------------------|-----------------------|
| **Actual Positive**   | True Positive (TP)    | False Negative (FN)   |
| **Actual Negative**   | False Positive (FP)   | True Negative (TN)    |

- **True Positive (TP):** Model correctly predicted a positive instance.
- **False Positive (FP):** Model incorrectly predicted a positive (was actually negative).
- **True Negative (TN):** Model correctly predicted a negative instance.
- **False Negative (FN):** Model incorrectly predicted a negative (was actually positive).

The confusion matrix is the starting point for almost all classification evaluation metrics, including precision, recall, F1 score, accuracy, specificity, and more.

**Resource:**  
- [EvidentlyAI: Confusion Matrix Explained](https://www.evidentlyai.com/classification-metrics/confusion-matrix)

## Precision: Definition, Formula, and Intuition

### Definition

Precision measures the correctness of positive predictions. It answers: *"Of all instances the model labeled as positive, how many were actually positive?"*

### Formula

\[
\text{Precision} = \frac{\text{True Positives (TP)}}{\text{True Positives (TP)} + \text{False Positives (FP)}}
\]

### Intuition

Precision is high when the model makes very few false positive errors. In other words, when it predicts “positive,” it’s usually correct.  
- **High precision:** Few false alarms; most positive predictions are true.
- **Low precision:** Many false alarms; positive predictions are often wrong.

### When is Precision Important?

Precision is especially important when the cost of a false positive is high.  
**Examples:**
- **Spam detection:** High precision ensures that legitimate emails are rarely marked as spam. ([GeeksforGeeks: Precision and Recall](https://www.geeksforgeeks.org/machine-learning/precision-and-recall-in-machine-learning/))
- **Legal document review:** Incorrectly labeling a non-relevant document as relevant is expensive.

### Limitations

- Over-optimizing for precision may cause the model to miss many true positives (reduce recall).
- If the model only predicts "positive" when very confident, it may rarely make positive predictions, leading to high precision but low recall.

## Recall: Definition, Formula, and Intuition

### Definition

Recall (also called sensitivity or true positive rate) measures the ability of the model to find all actual positive instances. It answers: *"Of all true positives in the data, how many did the model catch?"*

### Formula

\[
\text{Recall} = \frac{\text{True Positives (TP)}}{\text{True Positives (TP)} + \text{False Negatives (FN)}}
\]

### Intuition

Recall is high when the model misses very few actual positive cases.  
- **High recall:** The model finds most of the positives (few false negatives).
- **Low recall:** The model misses many positives (many false negatives).

### When is Recall Important?

Recall is crucial when missing a positive case has a high cost.  
**Examples:**
- **Medical diagnosis:** Missing a disease (false negative) can be fatal. High recall ensures most sick patients are found.
- **Fraud detection:** Missing a fraudulent transaction is costly.

### Limitations

- Over-optimizing for recall may cause the model to make many false positive errors (reduce precision).
- If the model labels almost everything as positive, recall will be high but precision will suffer.

## Calculating Precision and Recall: Step-by-Step Example

**Case Study:** Detecting fraudulent credit card transactions.

- **Dataset:** 1,000 transactions; 50 are fraudulent (positive class), 950 are non-fraudulent.
- **Model predicts:** 40 transactions as fraud.
    - 30 are truly fraudulent (**TP=30**)
    - 10 are not fraudulent (**FP=10**)
- Out of 50 actual frauds, 20 are missed by the model (**FN=20**)
- The model correctly identifies 940 as non-fraudulent (**TN=940**)

**Confusion Matrix:**

|                       | **Predicted Fraud** | **Predicted Not Fraud** |
|-----------------------|--------------------|------------------------|
| **Actual Fraud**      | 30 (TP)            | 20 (FN)                |
| **Actual Not Fraud**  | 10 (FP)            | 940 (TN)               |

**Calculations:**

- **Precision:**  
  \[
  \text{Precision} = \frac{TP}{TP + FP} = \frac{30}{30+10} = 0.75
  \]  
  *Interpretation: 75% of the transactions flagged as fraud were truly fraudulent.*

- **Recall:**  
  \[
  \text{Recall} = \frac{TP}{TP + FN} = \frac{30}{30+20} = 0.60
  \]  
  *Interpretation: The model identified 60% of all fraud cases.*

**Visual Reference:**  
- [GeeksforGeeks: Precision and Recall Example](https://www.geeksforgeeks.org/machine-learning/precision-and-recall-in-machine-learning/)

## Precision vs. Recall: Trade-offs and Use-Cases

Precision and recall usually trade off against each other:

| **Metric**   | **Optimize When**                 | **Risk If Maximized Alone**     | **Example Application**          |
|--------------|-----------------------------------|---------------------------------|----------------------------------|
| Precision    | False positives are costly        | Misses true positives (low recall) | Spam detection, legal review     |
| Recall       | False negatives are costly/dangerous | Many false positives (low precision) | Medical screening, fraud detection |

**Precision-Recall Trade-off:**  
- **High precision, low recall:** Model rarely makes positive predictions but they are mostly correct.
- **High recall, low precision:** Model finds most positives but also incorrectly labels many negatives as positives.

**Threshold Dependence:**  
The balance between precision and recall can be adjusted using the model’s decision threshold:  
- Lowering the threshold increases recall but reduces precision.
- Raising the threshold increases precision but reduces recall.

**Visualizations and Curves:**
- **Precision-Recall Curve:** Plots precision vs. recall at various thresholds. ([scikit-learn documentation](https://scikit-learn.org/stable/auto_examples/model_selection/plot_precision_recall.html))
- **ROC Curve:** Plots true positive rate (recall) vs. false positive rate.

## When to Use Precision, Recall, or Both

- **Precision:** Focus when false positives have high costs (e.g., marking important emails as spam).
- **Recall:** Focus when false negatives have high costs (e.g., missing cancer diagnosis).
- **Both:** Most real-world problems require balancing both metrics since both false positives and false negatives have consequences.

**Resource:**  
- [EvidentlyAI: When to Use Precision vs Recall](https://www.evidentlyai.com/classification-metrics/accuracy-precision-recall)

## Related Metrics: F1 Score, Accuracy, ROC-AUC, Specificity

### F1 Score

The F1 score is the harmonic mean of precision and recall:

\[
\text{F1} = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}}
\]

- **Use when:** You need a single metric that balances precision and recall, especially for imbalanced datasets.

### Accuracy

\[
\text{Accuracy} = \frac{TP + TN}{TP + FP + TN + FN}
\]

- **Limitation:** Can be misleading when classes are imbalanced.  
  ([Google ML Crash Course: Accuracy vs Precision vs Recall](https://developers.google.com/machine-learning/crash-course/classification/accuracy-precision-recall))

### ROC-AUC (Receiver Operating Characteristic - Area Under Curve)

- **ROC Curve:** Plots true positive rate (recall) vs. false positive rate at different thresholds.
- **AUC:** Area under the ROC curve; measures model’s ability to distinguish between classes across all thresholds.
- Useful for comparing models and visualizing trade-offs.  
  ([DeepAI: ROC Curve](https://deepai.org/machine-learning-glossary-and-terms/receiver-operating-characteristic-curve))

### Specificity

\[
\text{Specificity} = \frac{TN}{TN + FP}
\]

- Measures the proportion of actual negatives correctly identified.
- Especially relevant in medical diagnostics, often used alongside recall (sensitivity).

## Common Pitfalls and Limitations

- **Ignoring Class Imbalance:** High accuracy can mask poor performance on rare classes; precision and recall provide more insight.
- **Reporting Only One Metric:** Can hide critical weaknesses; always report both precision and recall.
- **Threshold Sensitivity:** Precision and recall values depend on the decision threshold; evaluate across multiple thresholds or use curves.
- **Undefined (NaN) Values:** If there are no positive predictions (TP + FP = 0), precision is undefined (NaN).  
  ([Google ML Crash Course: Precision & Recall](https://developers.google.com/machine-learning/crash-course/classification/accuracy-precision-recall))

## Best Practices for Using Precision and Recall

- Evaluate and report both metrics, not just accuracy.
- Use the confusion matrix to understand model errors.
- Report F1 score as a summary, but always include precision and recall.
- Visualize performance with precision-recall and ROC curves.
- Adjust decision thresholds to meet business or safety requirements.
- Choose metrics based on real-world costs of errors in your application.
- For thorough evaluation, complement with additional metrics like specificity, ROC-AUC, and mean average precision.

**Resource:**  
- [EvidentlyAI: Classification Metrics Guide](https://www.evidentlyai.com/classification-metrics)

## Example Use-Cases for Precision and Recall

| **Domain**        | **Use-Case**           | **Priority** | **Reason**                                         |
|-------------------|-----------------------|--------------|----------------------------------------------------|
| Medical Diagnosis | Disease screening     | Recall       | Missing a sick patient is highly consequential     |
| Spam Detection    | Email filtering       | Precision    | Marking a real email as spam is disruptive         |
| Fraud Detection   | Transaction monitoring| Recall       | Missing a fraud is costly                          |
| Search Engines    | Relevant document retrieval | Both   | Users want all relevant and few irrelevant results |
| Image Recognition | Object detection      | Both (contextual) | Depends on cost of missed or extra detections |

## Summary Table: Precision vs. Recall

| **Aspect**             | **Precision**                        | **Recall**                         |
|------------------------|--------------------------------------|------------------------------------|
| Definition             | TP / (TP + FP)                       | TP / (TP + FN)                     |
| Focus                  | Correctness of positive predictions  | Coverage of actual positives       |
| High Value Means       | Few false positives                  | Few false negatives                |
| Use When               | False positives are costly           | False negatives are costly         |
| Example Application    | Spam filter (minimize lost legit emails) | Disease screening (find all sick cases) |

## References and Further Reading

- [Google ML Crash Course: Accuracy, Precision, Recall](https://developers.google.com/machine-learning/crash-course/classification/accuracy-precision-recall)
- [EvidentlyAI: Accuracy vs Precision vs Recall](https://www.evidentlyai.com/classification-metrics/accuracy-precision-recall)
- [GeeksforGeeks: Precision and Recall](https://www.geeksforgeeks.org/machine-learning/precision-and-recall-in-machine-learning/)
- [DeepAI: Precision and Recall](https://deepai.org/machine-learning-glossary-and-terms/precision-and-recall)
- [BuiltIn: Precision and Recall](https://builtin.com/data-science/precision-and-recall)
- [Lyzr: Glossary - Precision and Recall](https://www.lyzr.ai/glossaries/precision-and-recall/)

## Glossary: Key Terms

- **True Positive (TP):** Correctly predicted positive instance.
- **False Positive (FP):** Incorrectly predicted positive instance.
- **False Negative (FN):** Actual positive missed by the model.
- **True Negative (TN):** Correctly predicted negative instance.
- **Confusion Matrix:** Table summarizing TP, FP, TN, FN.
- **Threshold:** Value above which a model predicts positive; adjusting this changes precision and recall.
- **Class Imbalance:** When one class is much more frequent than the other(s).
- **F1 Score:** Harmonic mean of precision and recall.

## Further Learning

- [EvidentlyAI: Confusion Matrix Explained](https://www.evidentlyai.com/classification-metrics/confusion-matrix)
- [DeepAI: ROC Curve and AUC](https://deepai.org/machine-learning-glossary-and-terms/receiver-operating-characteristic-curve)
- [BuiltIn: F1 Score and Advanced Metrics](https://builtin.com/data-science/f1-score)
- [scikit-learn: Precision-Recall Curves](https://scikit-learn.org/stable/auto_examples/model_selection/plot_precision_recall.html)

## Video Guides

- [StatQuest: Precision and Recall, Clearly Explained (YouTube)](https://www.youtube.com/watch?v=0pP4EwWJgIU)
- [Corey Schafer: Precision and Recall Explained (YouTube)](https://www.youtube.com/watch?v=Kdsp6soqA7o)

**Summary:**  
Precision and recall are foundational for evaluating classification model performance—especially when simple accuracy fails to capture real-world costs or class imbalance. Understanding and balancing these metrics, alongside related measures such as F1 score and ROC-AUC, ensures robust, context-aware assessment and deployment of AI and automation systems.

**For more details, advanced tutorials, and live examples, visit these trusted resources:**

- [Google ML Crash Course: Precision & Recall](https://developers.google.com/machine-learning/crash-course/classification/accuracy-precision-recall)
- [EvidentlyAI: Accuracy vs Precision vs Recall](https://www.evidentlyai.com/classification-metrics/accuracy-precision-recall)
- [GeeksforGeeks: Precision and Recall](https://www.geeksforgeeks.org/machine-learning/precision-and-recall-in-machine-learning/)
- [scikit-learn: Precision-Recall Curves](https://scikit-learn.org/stable/auto_examples/model_selection/plot_precision_recall.html)

