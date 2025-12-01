---
title: "Active Learning"
translationKey: "active-learning"
description: "--- Active learning is a machine learning paradigm where an algorithm or model actively selects the most informative data points from an unlabeled..."
keywords: ['Active Learning', 'AI Chatbots', 'Automation']
category: "AI Chatbot & Automation"
type: "glossary"
draft: false
---

# Active Learning

## Definition

Active learning is a machine learning paradigm where an algorithm or model actively selects the most informative data points from an unlabeled dataset and queries a human annotator (the "oracle") to label those data points. This approach enables achieving higher accuracy with fewer labeled examples, reducing manual annotation costs and efforts. Active learning is a subset of supervised learning, optimized for scenarios where obtaining labeled data is expensive, time-consuming, or otherwise constrained.

**See also:**  
- [Active Learning in Machine Learning: Guide & Strategies | Encord](https://encord.com/blog/active-learning-machine-learning-guide/)  
- [ML | Active Learning - GeeksforGeeks](https://www.geeksforgeeks.org/machine-learning/ml-active-learning/)  
- [Key Terms for AI Governance | IAPP](https://iapp.org/resources/article/key-terms-for-ai-governance/#active-learning)  

---

## 1. What is Active Learning?

Active learning is not a passive process of consuming labeled data. Instead, it strategically requests labels for data points expected to yield the greatest model improvement. The model iteratively asks for help in areas of highest uncertainty or where new information would significantly affect predictions.

**Key characteristics:**
- **Human-in-the-loop:** Relies on a human or expert for labels when requested.
- **Iterative process:** Consists of repeated cycles of training, selection, annotation, and retraining.
- **Query strategy:** Core to active learning; the method for selecting which data points to label.

**Alternative terms:** Query learning, human-in-the-loop learning, selective sampling.

**Further reading:**  
- [Active Learning: Strategies, Tools, and Real-World Use Cases | Neptune.ai](https://neptune.ai/blog/active-learning-strategies-tools-use-cases)  
- [Optimal Experimental Design (Wikipedia)](https://en.wikipedia.org/wiki/Optimal_experimental_design)

---

## 2. How Active Learning Works

### 2.1. The Active Learning Workflow

Active learning is implemented as a loop:

1. **Initialization:** Start with a small labeled dataset to train the initial model.
2. **Model Training:** Train the model on current labeled data.
3. **Uncertainty/Query Assessment:** Use a query strategy to estimate which unlabeled data points would most improve the model if labeled.
4. **Querying the Oracle:** Request labels for selected data points from a human annotator or subject matter expert.
5. **Model Update:** Add new labeled data to the training set, retrain or fine-tune the model.
6. **Iteration:** Repeat until a performance threshold is achieved or annotation budget is exhausted.

**Diagram:**  
![Active learning cycle diagram](https://i0.wp.com/neptune.ai/wp-content/uploads/2022/10/Active-Learning.png?resize=646%2C514&ssl=1)

### 2.2. Query Strategies

The effectiveness of active learning depends on the **query strategy**—the method for choosing which unlabeled examples to annotate. Common strategies include:

#### a. Uncertainty Sampling
Selects data points for which the model's predictions have the lowest confidence (highest uncertainty).  
**Methods:** Least confident, margin sampling, entropy-based selection.  
**Example:** In binary classification, select samples with predicted probability closest to 0.5.

#### b. Query-by-Committee (QBC)
Trains multiple models ("the committee") and chooses data points where these models most disagree, indicating ambiguity.

#### c. Diversity Sampling
Selects samples that are both uncertain and diverse, to avoid redundancy and overfitting.  
**Approaches:** Clustering, core-set selection, distance-based metrics.

#### d. Expected Model Change
Selects samples expected to cause the greatest change in model parameters if labeled, directly optimizing for impactful updates.

#### e. Expected Error Reduction
Selects samples anticipated to reduce the model’s overall error the most after labeling. Computationally intensive, often approximated.

#### f. Query Synthesis
Generates new data points (possibly non-existent in the original dataset) for the oracle to label. Useful in sparse data scenarios.

**Detailed strategy breakdown:**  
- [Query Strategies | Encord Glossary](https://encord.com/glossary/query-strategies/)
- [Active Learning Query Strategies for Classification, Regression, and Clustering: A Survey | Springer](https://link.springer.com/article/10.1007/s11390-020-9487-4)
- [Active Learning in Classification — Query Strategies | Medium](https://medium.com/@rongqianhui/active-learning-in-classification-query-strategies-69cc9fe70938)

---

## 3. Real-World Use Cases and Industry Applications

Active learning is essential in domains with scarce labeled data or expensive labeling, yet large volumes of unlabeled data.

### 3.1. Computer Vision

- **Image Classification:** Actively selects ambiguous images for labeling.  
  Example: X-ray images where a diagnostic model is least certain.
- **Semantic Segmentation:** Annotators label only uncertain regions, reducing pixel-wise annotation costs.
- **Object Detection:** Focuses on edge cases—rare objects or ambiguous boundaries.

### 3.2. Natural Language Processing (NLP)

- **Text Classification:** Queries ambiguous sentences for sentiment or topic labels.
- **Named Entity Recognition (NER):** Focuses on sentences where entity boundaries are unclear.
- **Conversational AI:** Improves chatbot intent detection by labeling uncertain utterances.

### 3.3. Medical Imaging

Prioritizes complex or ambiguous scans for expert annotation, improving accuracy while limiting workload.

### 3.4. Autonomous Vehicles

Labels rare or hazardous driving scenarios from sensor data where the model is least confident.

### 3.5. Fraud Detection

Queries for labels on transactions with low-confidence classification (fraudulent vs. legitimate).

**Industry case study:**  
- [The Practical Challenges of Active Learning: A Case Study from Live Experimentation | Google Research](https://research.google/pubs/the-practical-challenges-of-active-learning-a-case-study-from-live-experimentation/)

---

## 4. Advanced Implementation Details

### 4.1. Practical Steps

1. **Dataset Preparation:** Split data into a small labeled set and a large unlabeled pool.
2. **Select a Model:** Choose a supervised learning algorithm (e.g., logistic regression, SVM, deep neural networks).
3. **Choose a Query Strategy:** Implement uncertainty sampling, QBC, or other methods.
4. **Iterative Loop:**
   - Train the model.
   - Apply the query strategy to select new samples from the unlabeled pool.
   - Obtain labels from the oracle.
   - Update the labeled set and retrain.
5. **Stopping Criteria:**  
   - When model performance plateaus, the budget is exhausted, or target accuracy is achieved.

### 4.2. Example: Active Learning with Logistic Regression

```python
import numpy as np
from sklearn.linear_model import LogisticRegression

# Assume: x_train (labeled), y_train (labels), x_unlabeled (unlabeled pool)

for iteration in range(max_iterations):
    # Train the model on currently labeled data
    model = LogisticRegression()
    model.fit(x_train, y_train)
    
    # Predict probabilities for unlabeled data
    probs = model.predict_proba(x_unlabeled)
    
    # Uncertainty sampling: select samples with probabilities closest to 0.5
    uncertainty = np.abs(probs[:, 1] - 0.5)
    query_indices = np.argsort(uncertainty)[:batch_size]
    
    # (Human) annotate selected samples and add to labeled set
    new_x, new_y = get_labels_from_oracle(x_unlabeled[query_indices])
    x_train = np.concatenate([x_train, new_x])
    y_train = np.concatenate([y_train, new_y])
    x_unlabeled = np.delete(x_unlabeled, query_indices, axis=0)
```
*For a full code example, see [ML | Active Learning - GeeksforGeeks](https://www.geeksforgeeks.org/machine-learning/ml-active-learning/).*

### 4.3. Libraries and Tools

- **modAL:** Modular active learning framework for Python, compatible with scikit-learn.  
  [modAL documentation](https://modal-python.readthedocs.io/en/latest/)
- **libact:** Python library for active learning.  
  [libact documentation](https://libact.readthedocs.io/en/latest/)
- **Encord Active:** Toolkit for computer vision active learning.  
  [Encord Active](https://encord.com/encord-active/)

**Further reading:**  
- [Top 6 Tools for Active Learning in Machine Learning | Encord](https://encord.com/blog/top-active-learning-tools-for-machine-learning/)

---

## 5. Mathematical Background and Performance Metrics

### 5.1. Generalization Error

Active learning aims to reduce generalization error—the difference between model performance on training and unseen data—by selecting informative samples.

### 5.2. Information Theory

Many query strategies are grounded in information theory, using entropy, mutual information, or expected information gain as criteria for selection. For example, **entropy-based uncertainty sampling** chooses samples with maximal output entropy.

### 5.3. Performance Metrics

Common metrics for evaluating active learning systems include:
- **Accuracy, Precision, Recall, F1-score:** Standard supervised learning metrics.
- **Learning Curve:** Plots model performance versus the number of labeled samples.
- **Label Efficiency:** Number of labels required to reach a certain level of performance.

**Reference:**  
- [Active Learning Query Strategies for Classification, Regression, and Clustering: A Survey | Springer](https://link.springer.com/article/10.1007/s11390-020-9487-4)

---

## 6. Advantages and Benefits

- **Reduced Labeling Cost:** Fewer labels needed for high accuracy.
- **Improved Model Accuracy:** Focus on ambiguous/informative samples.
- **Faster Convergence:** Achieves performance goals with fewer iterations and less data.
- **Better Generalization:** Avoids overfitting by selecting diverse, challenging examples.
- **Robustness:** Handles noise and edge cases by surfacing challenging data.

| Benefit                  | Description                                                                    |
|--------------------------|--------------------------------------------------------------------------------|
| Reduced Labeling Cost    | Fewer labels needed for similar or better accuracy                             |
| Improved Accuracy        | Focused learning on informative or ambiguous samples                           |
| Faster Convergence       | Model reaches target performance in fewer iterations                           |
| Better Generalization    | Encourages learning from diverse, representative, or challenging examples      |
| Robustness               | Decreases sensitivity to noise and outliers                                    |

---

## 7. Challenges and Limitations

- **Annotation Cost Remains:** Even with reductions, manual labeling is still required for complex/specialized tasks.
- **Continuous Retraining:** Each loop iteration requires model retraining, which can be computationally expensive for large models.
- **Query Strategy Complexity:** Poorly designed strategies may choose redundant or non-informative samples.
- **Imbalanced Data:** Risk of over-sampling certain classes if strategies are not carefully managed.
- **Oracle Limitations:** Humans may make mistakes, especially for ambiguous samples.
- **Scalability:** Difficult to scale for massive datasets or high-dimensional data.

**Case study on practical challenges:**  
- [The Practical Challenges of Active Learning: A Case Study from Live Experimentation | Google Research](https://research.google/pubs/the-practical-challenges-of-active-learning-a-case-study-from-live-experimentation/)

---

## 8. Comparison with Related Approaches

### 8.1. Active vs. Passive Learning

| Aspect               | Active Learning                             | Passive Learning                    |
|----------------------|---------------------------------------------|-------------------------------------|
| Data Selection       | Model selects which samples to label        | Random or predefined selection      |
| Labeling Cost        | Reduced                                     | High                                |
| Adaptability         | High (focuses on ambiguous examples)        | Low (may waste effort on easy cases)|
| Model Performance    | Higher for the same amount of labeled data  | Lower unless large label set        |
| Human-in-the-loop    | Required                                    | Not required                        |

### 8.2. Active Learning vs. Reinforcement Learning

| Aspect                  | Active Learning                                 | Reinforcement Learning            |
|-------------------------|-------------------------------------------------|-----------------------------------|
| Learning Mode           | Learns from selected labeled data               | Learns via trial-and-error        |
| Feedback                | Explicit labels from oracle                     | Reward/punishment signals         |
| Data Source             | Fixed dataset (label on request)                | Dynamic environment interaction   |
| Goal                    | Optimize model with minimal labeled data        | Maximize cumulative reward        |

---

## 9. Key Terms and Concepts

- **Active Learning Model:** A model employing active learning strategies.
- **Model Performance:** Measured in accuracy, precision, recall, F1-score, etc.
- **Uncertainty Sampling:** Query strategy focusing on least confident predictions.
- **Oracle:** The human or system providing ground-truth labels.
- **Training Dataset:** Collection of labeled data used to train the model.
- **Informative Samples:** Data points likely to contribute most to learning/improvement.

---

## 10. Further Reading and Resources

- [Active Learning in Machine Learning: Guide & Strategies | Encord](https://encord.com/blog/active-learning-machine-learning-guide/)
- [ML | Active Learning - GeeksforGeeks](https://www.geeksforgeeks.org/machine-learning/ml-active-learning/)
- [Active Learning: Strategies, Tools, and Real-World Use Cases | Neptune.ai](https://neptune.ai/blog/active-learning-strategies-tools-use-cases)
- [A Practical Guide to Active Learning for Computer Vision](https://encord.com/blog/a-practical-guide-to-active-learning-for-computer-vision/)
- [Active Learning Query Strategies for Classification, Regression, and Clustering: A Survey | Springer](https://link.springer.com/article/10.1007/s11390-020-9487-4)
- [YouTube: Uncertainty Sampling in Active Learning](https://youtu.be/DsdBe0-4-30)
- [modAL: Active Learning Framework for Python](https://modal-python.readthedocs.io/en/latest/)
- [libact: Python Library for Active Learning](https://libact.readthedocs.io/en/latest/)

---

## 11. Summary Table

| Concept                | Description                                                                                                     |
|------------------------|-----------------------------------------------------------------------------------------------------------------|
| Active Learning        | Model actively queries for labels on the most informative unlabeled instances                                   |
| Query Strategy         | Method for selecting which data points to query (uncertainty, diversity, committee, etc.)                      |
| Oracle                 | Human or system that provides true labels when requested                                                        |
| Pool-based Sampling    | Query samples from a pool of unlabeled data                                                                     |
| Stream-based Sampling  | Query samples from a continuous stream of data                                                                  |
| Query Synthesis        | Synthesize new unlabeled data points for querying                                                               |
| Applications           | Computer vision, NLP, medical imaging, fraud detection, autonomous vehicles                                     |
| Benefits               | Reduced labeling cost, improved generalization, better performance, robustness                                  |
| Challenges             | Annotation effort, retraining cost, strategy complexity, scalability, oracle errors                             |

---

## 12. Related Terms

- [Supervised Learning](https://www.geeksforgeeks.org/machine-learning/supervised-machine-learning/)
- [Unsupervised Learning](https://www.geeksforgeeks.org/machine-learning/unsupervised-learning/)
- [Human-in-the-Loop](https://iapp.org/resources/article/key-terms-for-ai-governance/#human-in-the-loop)
- [Model Performance](https://iapp.org/resources/article/key-terms-for-ai-governance/#accuracy)
- [Query Strategy](https://encord.com/glossary/query-strategies/)

---

**References:**
- [Encord: Active Learning in Machine Learning Guide](https://encord.com/blog/active-learning-machine-learning-guide/)
- [GeeksforGeeks: ML | Active Learning](https://www.geeksforgeeks.org/machine-learning/ml-active-learning/)
- [Active Learning: Strategies, Tools, and Real-World Use Cases | Neptune.ai](https://neptune.ai/blog/active-learning-strategies-tools-use-cases)
- [IEEE Teaching Excellence Hub: ACTIVE LEARNING IN MACHINE LEARNING: A STEP TOWARDS SMARTER MODELS](https://teaching.ieee.org/active-learning-in-machine-learning-a-step-towards-smarter-models/)
- [Key Terms for AI Governance | IAPP](https://iapp.org/resources/article/key-terms-for-ai-governance/#active-learning)
- [Active Learning Query Strategies for Classification, Regression, and Clustering: A Survey | Springer](https://link.springer.com/article/10.1007/s11390-020-9487-4)
- [The Practical Challenges of Active Learning: A Case Study from Live Experimentation | Google Research](https://research.google/pubs/the-practical-challenges-of-active-learning-a-case-study-from-live-experimentation/)

---

**Key Takeaway:**  
Active learning enables efficient, cost-effective training of machine learning models where labeled data is limited or expensive. By selecting the most informative data for labeling, it produces high-performance, robust models with minimal annotation effort. Its methods, challenges, and tools are critical for advancing AI across domains such as computer vision, NLP, healthcare, and more. For deeper technical exploration, refer to the sources above.
