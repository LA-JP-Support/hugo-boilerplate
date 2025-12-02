---
title: "Active Learning"
translationKey: "active-learning"
description: "Active learning is a machine learning process where the model interactively queries a human to label uncertain data, optimizing learning efficiency and reducing annotation costs."
keywords: ["Active Learning", "Machine Learning", "Data Annotation", "Query Strategy", "Model Uncertainty"]
category: "AI Chatbot & Automation"
type: "glossary"
draft: false
---

## What is Active Learning?

Active learning is a focused approach in supervised machine learning that enables a model to select and request labels for data points it finds most informative or uncertain. Instead of passively consuming all available labeled data, the model actively identifies which unlabeled instances would most improve its predictive power if annotated.  
This approach is especially valuable when labeling large datasets is expensive, time-consuming, or requires domain experts.

> **Authoritative Definition:**  
> Active learning is a supervised machine learning process in which the model interactively queries a human (or other external oracle) to label data points it is uncertain about, thereby optimizing learning efficiency while minimizing the amount of required labeled data.  
> — [Encord Guide on Active Learning](https://encord.com/blog/active-learning-machine-learning-guide/), [V7 Labs Guide](https://www.v7labs.com/blog/active-learning-guide)

The model’s ability to “query” for new labels based on a strategic selection is why this paradigm is also referred to as *query learning*.

## Key Concepts and Definitions

- **Oracle:** The person or system (usually a human expert) providing ground truth labels upon request.
- **Unlabeled Data Pool:** The dataset containing instances for which the true labels are not yet known.
- **Query Strategy:** The method or algorithm the model uses to select which data points to query for labels.
- **Model Uncertainty:** A quantitative measure of the model’s confidence in its predictions for specific data points.
- **Iteration:** The repeated cycle of training, querying, annotating, and retraining as part of the active learning process.
- **Stopping Condition:** The rule (such as a labeling budget, accuracy threshold, or convergence) that determines when to end the active learning cycle.

For more, see:  
- [Encord: Active Learning Key Concepts](https://encord.com/blog/active-learning-machine-learning-guide/)  
- [V7 Labs: Active Learning Glossary](https://www.v7labs.com/blog/active-learning-guide)

## How Active Learning is Used in Machine Learning

Data annotation is often the bottleneck in developing accurate AI systems, as it can be expensive and slow, particularly for complex domains. Active learning addresses this by directing labeling efforts where they have the highest impact on model performance.

In a typical scenario, suppose you are building an email spam classifier. Instead of labeling thousands of emails at random, active learning lets the model request human input only on those emails it finds ambiguous, streamlining the annotation process and maximizing model improvement per labeled instance.

Active learning’s selective approach is increasingly significant in areas where annotated data is rare or costly, such as medical imaging, autonomous vehicles, and legal document analysis ([V7 Labs Guide](https://www.v7labs.com/blog/active-learning-guide), [Encord Guide](https://encord.com/blog/active-learning-machine-learning-guide/)).

## Active Learning Workflow: Step-by-Step

Active learning operates through a systematic, iterative cycle. Each iteration aims to refine the model using carefully selected new data. The standard workflow includes:

1. **Initialization:**  
   Begin with a small, labeled dataset to train the initial model.
2. **Model Training:**  
   Train the model on the labeled data.
3. **Query Strategy Application:**  
   Use a query strategy to identify unlabeled instances where the model has the least confidence or expects the most benefit from labeling.
4. **Annotation:**  
   Request labels for these selected instances from a human annotator (oracle).
5. **Model Update:**  
   Add the newly labeled data to the training set and retrain the model.
6. **Iteration:**  
   Repeat steps 3–5 until a stopping condition (such as a labeling budget or target accuracy) is reached.

**Analogy:**  
Think of active learning as a junior analyst who handles tasks independently but consults a senior expert only when encountering uncertainty.

**Visual Workflow:**  
Model Training → Uncertainty Estimation → Query → Human Annotation → Retraining → (repeat)

- See [Encord Guide: Workflow Visualization](https://encord.com/blog/active-learning-machine-learning-guide/)
- [V7 Labs: Workflow Example](https://www.v7labs.com/blog/active-learning-guide#what-is-active-learning)

## Core Strategies in Active Learning

The effectiveness of active learning hinges on the selection strategy used to choose which data points to label. The most prominent query strategies include:

### 1. Uncertainty Sampling
- **How it works:** Selects examples where the model’s confidence in its prediction is lowest (e.g., softmax probabilities close to 0.5 in binary classification).
- **When to use:** Rapidly reduce model uncertainty, especially in classification problems.
- **Example:** In a cat vs. dog classifier, images where the model predicts 51% cat and 49% dog are prioritized for labeling.
- [V7 Labs: Uncertainty Sampling](https://www.v7labs.com/blog/active-learning-guide#uncertainty-sampling)
- [YouTube: Uncertainty Sampling Explained](https://youtu.be/DsdBe0-4-30)

### 2. Query-by-Committee (QBC)
- **How it works:** Uses an ensemble (“committee”) of models, selecting samples with the highest prediction disagreement.
- **When to use:** When ensemble methods are available, increasing robustness by capturing diverse model opinions.
- **Example:** If three models predict “cat,” “dog,” and “rabbit” for the same image, that image is highly informative.
- [Encord: QBC Explanation](https://encord.com/blog/active-learning-machine-learning-guide/)

### 3. Diversity Sampling
- **How it works:** Selects samples that are most different from already-labeled data, ensuring comprehensive coverage of the data space.
- **When to use:** To prevent overfitting and ensure generalization, especially in datasets with high variance.
- **Example:** Choosing images that are visually distinct from previously labeled examples.
- [V7 Labs: Diversity Sampling](https://www.v7labs.com/blog/active-learning-guide#diversity-sampling)

### 4. Expected Model Change
- **How it works:** Selects samples that, if labeled, are expected to most change the current model’s parameters.
- **When to use:** When optimizing for rapid improvement with minimal labels.

### 5. Density-Weighted Sampling
- **How it works:** Balances informativeness (uncertainty) and representativeness (density) by selecting uncertain data points in dense regions of the data space.
- **When to use:** Avoids focusing only on outliers, emphasizes common but ambiguous cases.
- [V7 Labs: Density Sampling](https://www.v7labs.com/blog/active-learning-guide#density-weighted-sampling)

### 6. Stream-Based vs. Pool-Based Sampling
- **Stream-Based:** Model evaluates each incoming data point in real-time, deciding instantly whether to query a label.
- **Pool-Based:** Model selects the most informative samples from a static pool of unlabeled data.
- [V7 Labs: Stream-Based Sampling](https://www.v7labs.com/blog/active-learning-guide#stream-based-selective-sampling)

### 7. Query Synthesis
- **How it works:** Model generates new synthetic data points to query when natural data is scarce.
- **Example:** Generating artificial images or sentences and requesting human annotation.

Academic resource: [Policy-based Active Learning (PAL)](https://arxiv.org/pdf/1708.02383.pdf)

## Benefits of Active Learning

Implementing active learning offers substantial advantages:

- **Reduced Labeling Costs:**  
  By labeling only the most informative data points, overall annotation costs are minimized.
- **Faster Model Convergence:**  
  The model learns efficiently, reaching high accuracy with fewer labeled examples.
- **Improved Accuracy and Generalization:**  
  Focusing on edge cases and ambiguous data enhances model robustness.
- **Efficient Use of Expert Resources:**  
  Human experts focus on the most valuable data points, maximizing their impact.
- **Adaptability to Imbalanced Data or New Distributions:**  
  The model can shift its focus as new data types emerge or rare events are encountered.

> **Example:** In medical imaging, active learning reduces the workload on radiologists by prioritizing annotation of ambiguous scans.
> — [Encord: Active Learning Advantages](https://encord.com/blog/active-learning-machine-learning-guide/), [V7 Labs: Benefits](https://www.v7labs.com/blog/active-learning-guide#advantages-of-active-learning)

## Challenges and Limitations

Despite its strengths, active learning presents several practical challenges:

- **Cost of Expert Annotation:**  
  Complex data types (e.g., legal or medical) still require costly expert labeling.
- **Computational Overhead:**  
  Retraining the model frequently as new labels are added increases computational demands.
- **Potential for Bias and Imbalanced Data:**  
  Poorly designed query strategies may oversample certain data regions, leading to bias or neglect of rare classes.
- **Annotation Difficulty:**  
  In query synthesis, synthetic data may be difficult for humans to label accurately.

**Mitigation Strategies:**
- Combine multiple query strategies (e.g., uncertainty + diversity).
- Monitor and balance label distribution across classes.
- Use AI-assisted labeling to automate simple annotation tasks.
- Define clear stopping criteria for active learning loops.

References:  
- [V7 Labs: Limitations](https://www.v7labs.com/blog/active-learning-guide#limitations-of-active-learning)
- [Encord: Challenges](https://encord.com/blog/active-learning-machine-learning-guide/)

## Practical Examples and Use Cases

Active learning is applied in diverse domains where labeled data is difficult or expensive to obtain:

### 1. **Medical Imaging**
   - Prioritizes ambiguous scans (e.g., X-rays, MRIs), reducing radiologist workload and improving diagnostic models.
   - Case: Active learning can cut annotation volumes by up to 80% in large-scale radiology projects.
   - [Encord: Medical Imaging Case Study](https://encord.com/blog/active-learning-machine-learning-guide/)

### 2. **Natural Language Processing (NLP)**
   - Selects difficult examples for sentiment analysis, entity recognition, or spam detection, improving language model performance.

### 3. **Autonomous Vehicles**
   - Focuses annotation on rare or complex driving scenarios, enhancing object detection and decision-making AI.

### 4. **Fraud Detection**
   - Targets financial transactions the model finds suspicious but cannot confidently classify, refining fraud detection.

### 5. **Document Understanding and Automation**
   - Accelerates training of document classifiers (e.g., invoice vs. contract recognition), reducing manual review time.
   - Example: UiPath reports up to 80% faster model training using active learning in business automation pipelines ([UiPath Blog](https://www.uipath.com/blog/ai/what-is-active-learning)).

Additional use cases:  
- Robotics (exploration and navigation)
- Retail (customer intent classification)
- Industrial quality control (anomaly detection)

## Comparison with Related Machine Learning Paradigms

Active learning differs from, but relates to, several other machine learning approaches:

| Approach                      | Data Labeling         | Data Selection           | Human Role           | Typical Use Case           |
|-------------------------------|-----------------------|--------------------------|----------------------|----------------------------|
| **Active Learning**           | Selective, iterative  | Model-driven (query)     | Label only queried   | Expensive annotation       |
| **Passive Learning**          | All data upfront      | Random or all            | Label all data       | Large, cheap datasets      |
| **Reinforcement Learning**    | Learns from rewards   | Environment exploration  | Defines reward rules | Robotics, games            |
| **Semi-Supervised Learning**  | Few labels + unlabeled| Uses both                | Label a small set    | Abundant unlabeled data    |
| **Self-Supervised Learning**  | No human labels       | Generates own labels     | No labeling          | Pretraining, language models|

### Key Differences

- **Active vs. Passive Learning:**  
  Active learning queries labels only for selected data; passive learning labels all available data.
- **Active vs. Reinforcement Learning:**  
  Active learning queries for labels; reinforcement learning learns by interacting with an environment and receiving feedback.
- **Active vs. Semi/Self-Supervised Learning:**  
  Semi-supervised learning combines a small labeled set with a large unlabeled set; self-supervised learning generates its own training signals.

References:  
- [V7 Labs: Paradigm Comparison](https://www.v7labs.com/blog/active-learning-guide#active-learning-vs-passive-learning)  
- [Encord: Related Approaches](https://encord.com/blog/active-learning-machine-learning-guide/)

## Implementation and Tools

Active learning can be implemented using open-source libraries and commercial platforms. Typical workflow:

1. **Setup:**  
   Divide your dataset into labeled and unlabeled pools.
2. **Training:**  
   Train a base model on the labeled data.
3. **Query:**  
   Use a query strategy (e.g., uncertainty sampling) to select data points from the unlabeled pool.
4. **Annotation:**  
   Request human labels for selected points.
5. **Retrain:**  
   Add new labels to the training set and retrain the model.
6. **Repeat:**  
   Continue until your stopping condition is met.

### Popular Libraries

- **scikit-learn:**  
  Classic machine learning library; active learning via extensions.
  - [scikit-learn](https://scikit-learn.org/stable/)
- **modAL:**  
  Modular active learning framework built on top of scikit-learn.
  - [modAL Documentation](https://modal-python.readthedocs.io/en/latest/)
- **Encord:**  
  Platform for data curation, annotation, and active learning workflows.
  - [Encord Platform](https://encord.com/explore-product/)
- **V7 Labs:**  
  Provides active learning integrated with data annotation and curation.
  - [V7 Go Platform](https://www.v7labs.com/)
- **UiPath:**  
  Integrates active learning into document understanding and business automation.
  - [UiPath Overview](https://www.uipath.com/blog/ai/what-is-active-learning)

### Sample Code Snippet (Python with modAL)

```python
from modAL.models import ActiveLearner
from sklearn.ensemble import RandomForestClassifier

learner = ActiveLearner(
    estimator=RandomForestClassifier(),
    X_training=initial_X, y_training=initial_y
)

for i in range(num_iterations):
    query_idx, query_instance = learner.query(unlabeled_X)
    label = oracle_label(query_instance)
    learner.teach(X=query_instance, y=label)
```

More implementation details:  
- [Encord: Tools for Active Learning](https://encord.com/blog/active-learning-machine-learning-guide/#tools-to-use-for-active-learning)
- [V7 Labs: Implementation Guide](https://www.v7labs.com/blog/active-learning-guide#how-to-implement-active-learning)

## Further Reading and References

- [GeeksforGeeks: ML | Active Learning](https://www.geeksforgeeks.org/machine-learning/ml-active-learning/)
- [Encord: Active Learning in Machine Learning Guide](https://encord.com/blog/active-learning-machine-learning-guide/)
- [V7 Labs: Active Learning in Machine Learning Guide](https://www.v7labs.com/blog/active-learning-guide)
- [UiPath: Active Learning Overview](https://www.uipath.com/blog/ai/what-is-active-learning)
- [IEEE: ACTIVE LEARNING IN MACHINE LEARNING: A STEP TOWARDS SMARTER MODELS](https://teaching.ieee.org/active-learning-in-machine-learning-a-step-towards-smarter-models/)
- [IAPP: AI Governance Key Terms – Active learning](https://iapp.org/resources/article/key-terms-for-ai-governance/#active-learning)
- [YouTube: Uncertainty Sampling Explained](https://youtu.be/DsdBe0-4-30)
- [Policy-based Active Learning (PAL) Paper](https://arxiv.org/pdf/1708.02383.pdf)

## Glossary Box: Related Terms

- **Supervised Learning:** Training an AI model using labeled data to predict outcomes for new data.
- **Unsupervised Learning:** Learning patterns from unlabeled data without explicit labels.
- **Semi-Supervised Learning:** Combines a small amount of labeled data with a large amount of unlabeled data.
- **Self-Supervised Learning:** The model generates its own supervisory signals from the data.
- **Reinforcement Learning:** An agent learns to make decisions by receiving feedback in the form of rewards or penalties.
- **Data Annotation:** The process of labeling data with ground truth, crucial for supervised and active learning.
- **Model Uncertainty:** A measure of how unsure a model is about its predictions, used to guide querying in active learning.
- **Oracle:** The human or system providing ground truth labels upon request.
- **Query Synthesis:** Generating synthetic data points for labeling when the natural data pool is small.
- **Pool-Based Sampling:** Selecting samples from a fixed pool of unlabeled data.
- **Stream-Based Sampling:** Selecting samples from a continuous stream of incoming data.
- **Informative Sample:** A data point that, if labeled, is expected to provide significant value to the model.
- **Generalization

