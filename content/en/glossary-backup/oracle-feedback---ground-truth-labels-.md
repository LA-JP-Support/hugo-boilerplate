---
title: Oracle Feedback (Ground-Truth Labels)
date: 2025-12-17
translationKey: oracle-feedback-ground-truth-labels
description: Explore Oracle feedback and ground-truth labels in AI/ML. Learn how Oracle
  Select AI and HCM Cloud use authoritative data for model training, evaluation, and
  continuous improvement.
keywords:
- Oracle feedback
- ground-truth labels
- AI
- machine learning
- Select AI
category: AI
type: glossary
draft: false
---

## Introduction

Oracle feedback—referred to as “oracle feedback (ground-truth labels)”—is the system of providing authoritative, correct answers for AI and machine learning (ML) model training, evaluation, and continual improvement. In Oracle’s AI ecosystem, particularly with products like [Oracle Select AI](https://docs.oracle.com/en/cloud/paas/autonomous-database/serverless/adbsb/select-ai-feedback.html) and [Oracle HCM Cloud](https://docs.oracle.com/en/cloud/saas/readiness/hcm/24a/tama-24a/24A-talent-mgmt-wn-f31188.htm), oracle feedback forms the backbone of supervised learning, prompt tuning, and adaptive automation. An "oracle" is any trusted authority—typically a human or a gold-standard process—that provides these ground-truth labels for reference, validation, and iterative model improvement.

## Glossary & Core Definitions

### Oracle Feedback

Oracle feedback is the process in which correct answers (ground-truth labels) are provided to an AI/ML system. These answers are created or validated by subject-matter experts or trusted annotation methods and serve as the reference for model training, validation, and improvement.

#### Key Points:
- Used primarily in supervised machine learning where each input is paired with a known, correct output.
- Enables AI systems to learn the mappings between inputs and desired outputs by example.
- In Oracle platforms, feedback can be provided via user interfaces, APIs, or specific procedures.

**Links:**
- [Oracle ML Fundamentals](https://www.oracle.com/artificial-intelligence/machine-learning/what-is-machine-learning/)
- [Labeling Data for ML (LabelYourData)](https://labelyourdata.com/articles/label-data-for-machine-learning)
- [OCI Data Labeling](https://www.oracle.com/artificial-intelligence/data-labeling/)

### Ground-Truth Labels

Ground-truth labels are the set of correct answers for a given dataset, established by an authoritative process or expert annotation. These labels are the gold standard for training, validating, and evaluating AI models.

- **In NLP:** The correct SQL query for a natural language prompt.
- **In Computer Vision:** The correct class, bounding box, or segmentation mask for an image.
- **In Classification:** The correct class or category for a data point.

### Oracle (Authority)

An oracle, in AI/ML, refers to a reliable source providing definitive feedback or validation of what the correct output should be. Often this is a human expert, but it may also be a trusted automated system or process.

## How Oracle Feedback Works in Oracle AI and Automation

### 1. Data Labeling and Collection

The process begins with data labeling—the act of assigning correct answers to data samples. Oracle’s [OCI Data Labeling](https://www.oracle.com/artificial-intelligence/data-labeling/) provides a robust service for assembling and annotating datasets, critical for training AI models.

#### Steps:
- Data is uploaded (text, image, documents).
- Annotators label each data item with its correct output.
- The labeled data can be exported in JSON for direct integration with Oracle AI and data science services.

**Features:**  
- Custom templates and annotation formats.
- GUI and API-based annotation.
- Integration with OCI Vision and OCI Language for seamless model training.
### 2. Model Training (Supervised Learning)

The labeled data is used for supervised learning, where the model is explicitly shown the correct answer for each example.

- **Algorithm Examples:** Neural Networks, Decision Trees, SVMs.
- **Process:** Each input is paired with its label; the model adjusts its internal parameters to minimize the error between predicted and correct outputs.
### 3. Model Evaluation and Validation

After training, the model is tested on new, labeled data. The outputs are compared to the ground-truth labels to compute metrics such as accuracy, precision, recall, and F1 score.

- **Purpose:** Identify where AI predictions diverge from ground truth, enabling focused improvement.
- **Best Practice:** Use a separate test set with reliable, oracle-provided labels.

### 4. Feedback Mechanisms in Oracle Platforms

#### **Oracle Select AI (NL2SQL) Feedback Loop**

[Select AI](https://docs.oracle.com/en/cloud/paas/autonomous-database/serverless/adbsb/select-ai-feedback.html) allows users to provide direct feedback on AI-generated SQL queries, improving natural language to SQL performance.

- **Process:**
  - User issues a natural language prompt.
  - AI generates an SQL query.
  - User reviews the SQL:
    - If correct, positive feedback is given.
    - If incorrect, user provides the corrected SQL or descriptive feedback.
  - Feedback is recorded in a vector index (e.g., `<profile_name>_FEEDBACK_VECINDEX`).

- **Technical Interface:**
  - Feedback can be given through a UI or by calling the `DBMS_CLOUD_AI.FEEDBACK` procedure.
    - [DBMS_CLOUD_AI Package Reference](https://docs.oracle.com/en-us/iaas/autonomous-database-serverless/doc/dbms-cloud-ai-package.html)
  - The feedback is used as a reference for future prompts, enhancing the LLM’s contextual understanding and accuracy.

- **Example:**
```sql
-- Positive feedback for correct SQL
EXEC DBMS_CLOUD_AI.FEEDBACK(
    ai_profile    => 'my_profile',
    prompt        => 'Show me all sales from last quarter',
    feedback_type => 'positive',
    feedback      => 'The generated SQL is correct.'
);

-- Negative feedback with correct SQL
EXEC DBMS_CLOUD_AI.FEEDBACK(
    ai_profile    => 'my_profile',
    prompt        => 'Show me all sales from last quarter',
    feedback_type => 'negative',
    feedback      => 'The SQL should include date filtering for last quarter.',
    correct_sql   => 'SELECT * FROM sales WHERE sale_date BETWEEN :start AND :end;'
);
```

- **Underlying Mechanism:**  
  The vector index stores feedback, allowing Select AI to retrieve and use contextually relevant feedback for new, similar prompts, thereby improving output over time.
#### **Oracle HCM Cloud: AI-Assisted Feedback**

Oracle HCM Cloud’s [AI Assistance for Giving Feedback](https://docs.oracle.com/en/cloud/saas/readiness/hcm/24a/tama-24a/24A-talent-mgmt-wn-f31188.htm) feature leverages generative AI to help users write effective feedback for colleagues or direct reports.

- **Workflow:**
  - User types the initial feedback.
  - Clicks the AI Assist icon; the system generates a draft based on the initial text.
  - User reviews, edits, and submits the feedback.
  - The finalized, human-reviewed feedback is stored as ground truth, refining future AI-generated drafts.

- **Configuration Steps:**
  - Enable Redwood Anytime Feedback and Visual Builder Studio features as described in the documentation.
  - Use profile options (e.g., `ORA_HCM_VBCS_PWA_ENABLED`, `ORA_HRT_ANYTIME_FEEDBACK_REDWOOD_ENABLED`) to activate features.
  - [Set Profile Option Values](https://docs.oracle.com/pls/topic/lookup?ctx=fa-latest&id=s20052787)
  - [Visual Builder Studio Overview](https://docs.oracle.com/pls/topic/lookup?ctx=fa-latest&id=s20072861)

- **Benefits:**
  - Accelerates the feedback process.
  - Ensures feedback quality and consistency.
  - System adapts to organizational and managerial style over time.
### 5. Feedback Loop and Continuous Improvement

Oracle’s feedback systems support a closed feedback loop:  
- New feedback is continuously incorporated into the system.
- Stored feedback contextualizes and tunes future model outputs.
- Models adapt to evolving user needs and domain-specific requirements without requiring full retraining.

## Benefits of Oracle Feedback & Ground-Truth Labels

- **Accuracy:** Models learn directly from correct examples, leading to more reliable outputs.
- **Transparency:** Human-validated answers provide traceability and accountability.
- **Adaptive Learning:** Systems evolve by incorporating new feedback, supporting prompt tuning and ongoing accuracy.
- **Efficient Evaluation:** Objective measurement against ground-truth benchmarks enables robust model assessment.
- **Personalization:** User feedback refines AI behavior for organizational or domain-specific requirements.
- **Bias Reduction:** Diverse, well-labeled datasets help counteract unwanted model biases.
- **Scalable Automation:** Feedback loops support continuous improvement and deployment without full retraining.

## Examples & Use Cases

### Oracle Select AI: NL2SQL Feedback Loop

- User asks for a report in natural language.
- Select AI generates an SQL query.
- User confirms or corrects the SQL.
- Corrected SQL is stored as ground-truth.
- System uses stored feedback to improve future SQL generation.

**Documentation:**  
[Select AI Feedback](https://docs.oracle.com/en/cloud/paas/autonomous-database/serverless/adbsb/select-ai-feedback.html)

### Oracle HCM Cloud: AI-Generated Employee Feedback

- HR manager writes initial comments for an employee review.
- AI Assist generates a draft.
- Manager reviews/edits and submits.
- Human-reviewed feedback becomes part of the ground-truth corpus for future AI suggestions.

**Documentation:**  
[AI Assistance for Giving Feedback](https://docs.oracle.com/en/cloud/saas/readiness/hcm/24a/tama-24a/24A-talent-mgmt-wn-f31188.htm)

### Supervised Learning in Computer Vision

- Human annotators label images (e.g., “defective” vs. “non-defective” products).
- Model trained on these labels can detect defects in new images.
### Spam Detection

- Annotators label emails as “spam” or “not spam.”
- Model learns to classify new emails based on these oracle-provided labels.

## Best Practices & Implementation Tips

- **Use domain experts or robust annotation guidelines for ground-truth creation.**
- **Leverage tools like OCI Data Labeling for scalable annotation.**
- **Incorporate feedback continuously to adapt to evolving requirements.**
- **Use separate validation and test sets to prevent overfitting to feedback.**
- **Document feedback and annotation processes for traceability and reproducibility.**

## Technical Deep Dive: Select AI Feedback & DBMS_CLOUD_AI.FEEDBACK

**Feedback Mechanism:**
- Available only on Oracle AI Database 26ai.
- Used alongside Select AI actions: `runsql`, `showsql`, `explainsql`.
- Feedback action or `DBMS_CLOUD_AI.FEEDBACK` procedure records user responses.
- Creates a default vector index (`<profile_name>_FEEDBACK_VECINDEX`) to store feedback references.

**DBMS_CLOUD_AI.FEEDBACK Syntax and Usage:**
- Used when LLM-generated SQL is incorrect or needs refinement.
- Allows for both positive (confirmation) and negative (correction) feedback.
- Feedback is used as a reference for similar future queries.

**Documentation:**  
[DBMS_CLOUD_AI Package Reference](https://docs.oracle.com/en-us/iaas/autonomous-database-serverless/doc/dbms-cloud-ai-package.html)

## References & Further Reading

1. [Oracle Documentation – Select AI Feedback](https://docs.oracle.com/en/cloud/paas/autonomous-database/serverless/adbsb/select-ai-feedback.html)
2. [Oracle Documentation – DBMS_CLOUD_AI.FEEDBACK Procedure](https://docs.oracle.com/en-us/iaas/autonomous-database-serverless/doc/dbms-cloud-ai-package.html)
3. [OCI Data Labeling](https://www.oracle.com/artificial-intelligence/data-labeling/)
4. [AI Assistance for Giving Feedback – Oracle HCM Cloud](https://docs.oracle.com/en/cloud/saas/readiness/hcm/24a/tama-24a/24A-talent-mgmt-wn-f31188.htm)
5. [What is Machine Learning? (Oracle)](https://www.oracle.com/artificial-intelligence/machine-learning/what-is-machine-learning/)
6. [Labeling Data for Machine Learning (LabelYourData)](https://labelyourdata.com/articles/label-data-for-machine-learning)
7. [Supervised vs Unsupervised Learning (Viso.ai)](https://viso.ai/deep-learning/supervised-vs-unsupervised-learning/)

## Appendix: Related Oracle Documentation

- [Select AI Overview](https://docs.oracle.com/en-us/iaas/autonomous-database-serverless/doc/select-ai.html)
- [Autonomous AI Database Supplied Package Reference](https://docs.oracle.com/en-us/iaas/autonomous-database-serverless/doc/dbmscloud-reference.html)
- [Oracle Cloud HCM: Implementing Generative AI](https://blogs.oracle.com/fusionhcmcoe/implementing-generative-ai-oracle-cloud-hcm)

**This glossary provides comprehensive, technically detailed coverage of Oracle feedback and ground-truth labeling, with direct links to Oracle and industry documentation for further exploration and implementation.**

