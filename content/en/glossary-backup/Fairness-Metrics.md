---
title: "Fairness Metrics"
date: 2025-11-25
lastmod: 2025-12-05
translationKey: "fairness-metrics"
description: "Fairness metrics are mathematical and statistical tools used to quantify, evaluate, and monitor bias in AI/ML systems, ensuring equitable treatment across groups."
keywords: ["fairness metrics", "AI bias", "algorithmic bias", "responsible AI", "machine learning fairness"]
category: "AI Ethics & Safety Mechanisms"
type: "glossary"
draft: false
---
## **What Are Fairness Metrics?**

Fairness metrics are mathematical and statistical tools designed to quantify, evaluate, and monitor bias in artificial intelligence (AI) and machine learning (ML) systems. These metrics provide structured ways to assess whether an AI model treats individuals or groups equitably, or if it unfairly disadvantages anyone based on sensitive attributes such as race, gender, age, or socioeconomic status.

Fairness metrics are central to responsible AI development. They enable organizations to identify, measure, and mitigate algorithmic bias—key for building trustworthy AI, ensuring compliance with regulations, and fostering societal acceptance.

## **Why Are Fairness Metrics Used?**

AI models increasingly influence decisions in hiring, healthcare, law enforcement, finance, and education. Without safeguards, these models can:

- Perpetuate or amplify existing biases in training data.
- Unfairly disadvantage certain individuals or groups (e.g., lower loan approval rates for minorities).
- Create reputational, ethical, and legal risks.

**Fairness metrics are used to:**

- Quantify and monitor disparate outcomes across demographic groups.
- Identify and address algorithmic bias during model development and deployment.
- Guide corrective actions such as adjusting data, refining algorithms, or revising decision thresholds.
- Demonstrate [transparency](/en/glossary/transparency/) and accountability to stakeholders, regulators, and the public.
- Ensure compliance with regulations, including:
  - [EU AI Act](https://www.europarl.europa.eu/topics/en/article/20230601STO93804/eu-ai-act-first-regulation-on-artificial-intelligence)
  - [Fair Credit Reporting Act](https://www.ftc.gov/legal-library/browse/statutes/fair-credit-reporting-act)
  - [Equal Credit Opportunity Act](https://www.consumerfinance.gov/compliance/compliance-resources/other-applicable-requirements/equal-credit-opportunity-act/)
  - [Algorithmic Accountability Act (US)](https://www.congress.gov/bill/117th-congress/house-bill/6580/text)
  - [GDPR](https://gdpr.eu/)

## **How Are Fairness Metrics Used in Practice?**

**Workflow for Using Fairness Metrics:**

1. **Data Collection & Preparation**
   - Collect demographic and sensitive attribute data (e.g., gender, race, age).
   - Ensure representative data for all relevant groups.
2. **Model Training & Evaluation**
   - Train models on labeled datasets.
   - Evaluate model outputs across groups using fairness metrics.
3. **Bias Assessment**
   - Apply one or more fairness metrics to measure disparities in outcomes.
   - Analyze specific subgroups to identify where unfairness occurs.

4. **Mitigation & Iteration**
   - Use actionable insights from fairness metrics to modify data, algorithms, or thresholds.
   - Re-evaluate and iterate until acceptable fairness levels are achieved.
5. **Monitoring & Reporting**
   - Continuously monitor fairness metrics post-deployment.
   - Document findings and mitigation efforts for audits and compliance.
**Integration with Model Lifecycle:**

- **Pre-processing:** Address bias in data before training (e.g., reweighting, data augmentation).
- **In-processing:** Apply fairness constraints or regularization during model training.
- **Post-processing:** Adjust model predictions or thresholds after training for fairer outcomes.

## **Key Types of Fairness Metrics**

### **1. Demographic Parity (Statistical Parity / Group Fairness)**

- **Definition:** Ensures individuals from different demographic groups have the same probability of receiving a positive outcome (e.g., job offer, loan approval).
- **Mathematical Formula:**  
  P(Outcome = 1 | Group A) = P(Outcome = 1 | Group B)
- **Use Cases:**
  - Hiring algorithms: Ensuring equal selection rates for men and women.
  - Loan approval: Equal approval rates across ethnicities.
- **Limitations:**
  - Does not account for group qualification differences.
  - Strict enforcement can lead to "reverse discrimination" or reduced utility.
### **2. Equal Opportunity**

- **Definition:** Qualified individuals from different groups have the same probability of receiving a positive outcome.
- **Formula:**  
  P(Outcome = 1 | Qualified = 1, Group A) = P(Outcome = 1 | Qualified = 1, Group B)
- **Use Cases:**
  - University admissions: Equally qualified students from all backgrounds have equal admission rates.
  - Internal promotions: Equal promotion chances for equally qualified employees.
- **Limitations:**
  - Relies on accurate, unbiased measurement of "qualification."
### **3. Equalized Odds (Equality of Odds)**

- **Definition:** True positive and [false positive](/en/glossary/false-positive/) rates are equal across groups.
- **Formula:**  
  - TPR: P(Outcome = 1 | Actual = 1, Group A) = P(Outcome = 1 | Actual = 1, Group B)
  - FPR: P(Outcome = 1 | Actual = 0, Group A) = P(Outcome = 1 | Actual = 0, Group B)
- **Use Cases:**
  - Criminal justice risk assessments: Equal correct and incorrect prediction rates for all races.
  - Medical diagnosis: Equal diagnostic error rates across genders.
- **Limitations:**
  - Difficult to achieve; may conflict with other metrics or model accuracy.
### **4. Predictive Parity (Predictive Equality / Predictive Value Parity)**

- **Definition:** Precision (positive predictive value) is equal across groups.
- **Formula:**  
  P(Actual = 1 | Outcome = 1, Group A) = P(Actual = 1 | Outcome = 1, Group B)
- **Use Cases:**
  - Loan default prediction: Equal likelihood that approved applicants will repay across demographics.
  - Healthcare treatment recommendations: Equal precision in predicting treatment success for all patient groups.
- **Limitations:**
  - Can conflict with equal opportunity or equalized odds.
### **5. Treatment Equality**

- **Definition:** The ratio of false positives to false negatives is equal across groups.
- **Formula:**  
  P(Outcome = 1 | Actual = 0, Group A) / P(Outcome = 0 | Actual = 1, Group A) =  
  P(Outcome = 1 | Actual = 0, Group B) / P(Outcome = 0 | Actual = 1, Group B)
- **Use Cases:**
  - Predictive policing: Balancing false arrest and missed crime rates.
  - Fraud detection: Equalizing false alarms and missed frauds for customer segments.
- **Limitations:**
  - Complex to interpret and implement.
### **6. Individual Fairness**

- **Definition:** Similar individuals should receive similar outcomes from the AI system.
- **Measurement:** Requires a task-specific similarity metric and analysis of model consistency for similar input cases.
- **Use Cases:**
  - Loan approval: Individuals with similar financial profiles receive similar decisions.
  - Healthcare triage: Comparable patients receive consistent recommendations.
- **Limitations:**
  - Defining "similarity" is subjective and context-dependent.
### **7. Counterfactual Fairness**

- **Definition:** A model’s prediction remains the same if a sensitive attribute (e.g., race, gender) is changed, holding all else constant.
- **Measurement:** Compare predicted outcomes for real vs. counterfactual (altered) inputs.
- **Use Cases:**
  - Loan application: Would the decision change if the applicant’s gender were different but all else remained equal?
  - Job screening: Ensuring decisions are not impacted by protected attributes.
- **Limitations:**
  - Requires causal modeling and counterfactual data generation.
## **Real-World Examples and Use Cases**

### **Hiring Algorithms**
- **Problem:** Resume screening tool favors candidates from a specific gender or ethnicity.
- **Metric Applied:** Demographic parity, equal opportunity.
- **Mitigation:** Adjust training data, apply fairness constraints, monitor selection rates.
### **Facial Recognition Systems**
- **Problem:** Higher error rates for underrepresented groups (e.g., people of color).
- **Metric Applied:** Equalized odds.
- **Mitigation:** Diversify training data, retrain model, audit for performance disparities.
### **Loan Approval**
- **Problem:** Lower approval rates for minority applicants due to historical bias.
- **Metric Applied:** Predictive parity, counterfactual fairness.
- **Mitigation:** Apply debiasing, adjust thresholds, ensure regulatory compliance.
### **Healthcare Diagnosis**
- **Problem:** Diagnostic tools less accurate for certain demographic groups.
- **Metric Applied:** Equalized odds, treatment equality.
- **Mitigation:** Augment training data, monitor fairness metrics, engage domain experts.
## **Open-Source Fairness Metric Libraries & Tools**

- **[Fairlearn](https://fairlearn.org/):** Python library for evaluating and improving model fairness. Features metrics, mitigation algorithms, and visualizations.
- **[AIF360 (AI Fairness 360)](https://aif360.res.ibm.com/):** IBM toolkit with a broad set of fairness metrics and [bias mitigation](/en/glossary/bias-mitigation/) techniques.
- **[Fairness Indicators](https://www.tensorflow.org/tfx/guide/fairness_indicators):** Google's tool for evaluating and visualizing fairness metrics, especially for TensorFlow models.
- **[FairComp](https://www.faircomp.io/):** Library for comparing fairness interventions and benchmarking different metrics.
- **[FairML](https://github.com/adebayoj/fairml):** Tool for auditing model fairness and identifying sources of bias.
- **[Aequitas](https://github.com/dssg/aequitas):** Auditing tool for analyzing model impact on demographic groups.
- **[Themis](https://github.com/LASER-UMASS/Themis) & [Themis-ML](https://github.com/cosmicBboy/themis-ml):** Libraries focused on individual fairness.

## **Best Practices for Using Fairness Metrics**

1. **Use Multiple Metrics:**  
   Combine several metrics for a holistic view of fairness.
2. **Consider Context:**  
   Tailor metric selection and interpretation to the real-world impact.

3. **Engage Stakeholders:**  
   Involve impacted groups, domain experts, and decision makers.

4. **Regular Audits:**  
   Continuously monitor fairness metrics post-deployment.

5. **Document & Report:**  
   Maintain transparency by recording fairness analyses, decisions, and remediation steps.

6. **Balance Fairness and Accuracy:**  
   Improving fairness may reduce accuracy; use multi-objective optimization and make informed trade-offs.

## **Common Pitfalls and How to Avoid Them**

- **Relying on a Single Metric:**  
  One metric rarely provides the full picture.
- **Ignoring Social Context:**  
  Interpret metrics within the relevant social and ethical framework.
- **Static Evaluation:**  
  Regularly reassess as data, models, and populations shift.
- **Confusing Correlation with Causation:**  
  Disparities may reflect real-world inequalities, not just model bias.
- **Neglecting Transparency:**  
  Failure to document can lead to compliance issues and loss of trust.

## **Compliance, Regulation, and Industry Standards**

**Legal & Regulatory Frameworks:**

- **[EU AI Act](https://www.europarl.europa.eu/topics/en/article/20230601STO93804/eu-ai-act-first-regulation-on-artificial-intelligence):** Sets requirements for transparency, accountability, and fairness; mandates risk assessments and documentation.
- **[Fair Credit Reporting Act (FCRA)](https://www.ftc.gov/legal-library/browse/statutes/fair-credit-reporting-act):** Governs credit data use, prohibits discrimination in automated credit decisions.
- **[Equal Credit Opportunity Act (ECOA)](https://www.consumerfinance.gov/compliance/compliance-resources/other-applicable-requirements/equal-credit-opportunity-act/):** Prohibits discrimination in lending decisions.
- **[GDPR](https://gdpr.eu/):** Mandates transparency and “right to explanation” for automated decisions in the EU.
- **[Algorithmic Accountability Act (US)](https://www.congress.gov/bill/117th-congress/house-bill/6580/text):** (Proposed) Requires algorithmic bias assessment and reporting.

**Industry Guidelines:**

- **Ethics Boards and Responsible AI Committees:** Organizational oversight on fairness and bias.
- **Documentation Standards:** Model cards and data sheets record fairness checks and risks.
## **Glossary: Key Terms**

- **Bias (AI):** Systematic error in AI outputs caused by prejudiced data, flawed algorithms, or skewed training.
- **Sensitive Attribute:** Demographic feature (race, gender, age) that may lead to discrimination if used in decision-making.
- **Disparate Impact:** Model predictions disproportionately harm a protected group, even if sensitive attributes are not explicitly used.
- **Transparency:** Degree to which AI decisions and processes can be understood, audited, and explained.
- **Accountability:** Obligation to justify and be answerable for AI system outcomes, especially regarding fairness.

## **Further Reading & Resources**

- [Shelf.io: Fairness Metrics in AI](https://shelf.io/blog/fairness-metrics-in-ai/)
- [Forbes: AI & Fairness Metrics](https://councils.forbes.com/blog/ai-and-fairness-metrics)
- [Google ML Fairness Guide](https://developers.google.com/machine-learning/crash-course/fairness/evaluating-for-bias)
- [AI Evaluation Metrics – Bias & Fairness](https://www.francescatabor.com/articles/2025/7/10/ai-evaluation-metrics-bias-amp-fairness)
- [Fairlearn documentation](https://fairlearn.org/)
- [AIF360 documentation](https://aif360.res.ibm.com/)
- [EU AI Act summary](https://www.europarl.europa.eu/topics/en/article/20230601STO93804/eu-ai-act-first-regulation-on-artificial-intelligence)

**Videos:**
- [YouTube: ML Fairness (Google Crash Course)](https://www.youtube.com/watch?v=59bMh59JQDo)
- [YouTube: Responsible AI—Fairness and Bias](https://www.youtube.com/watch?v=F03lK5q6ohM)

## **Summary Table: Common Fairness Metrics**

| Metric                | What It Measures                                           | Formula (Simplified)                                      | Example Use Case                        |
|-----------------------|-----------------------------------------------------------|-----------------------------------------------------------|-----------------------------------------|
| Demographic Parity    | Equal positive rates across groups                        | P(Y=1|A=a) = P(Y=1|A=b)                                   | Hiring, Loan Approval                   |
| Equal Opportunity     | Equal TPR for qualified individuals                       | P(Y=1|Y*=1, A=a) = P(Y=1|Y*=1, A=b)                       | University Admissions                   |
| Equalized Odds        | Equal TPR and FPR across groups                           | TPR_a = TPR_b; FPR_a = FPR_b                              | Criminal Justice, Healthcare Diagnosis  |
| Predictive Parity     | Equal precision (PPV) across groups                       | P(Y*=1|Y=1, A=a) = P(Y*=1|Y=1, A=b)                       | Loan Default Prediction                 |
| Treatment Equality    | Equal FP/FN ratio across groups                           | FP/FN ratio_a = FP/FN ratio_b                             | Predictive Policing, Fraud Detection    |
| Individual Fairness   | Similar individuals get similar outcomes                  | Distance(Y(x), Y
