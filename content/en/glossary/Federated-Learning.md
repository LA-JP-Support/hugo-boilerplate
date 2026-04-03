---
title: Federated Learning
date: 2025-12-19
lastmod: 2026-04-02
translationKey: Federated-Learning
description: Federated learning trains distributed AI models across multiple devices and organizations without aggregating data, protecting privacy.
keywords:
- Federated Learning
- Distributed Machine Learning
- Privacy-Preserving AI
- Distributed Training
- Edge Computing
category: AI & Machine Learning
type: glossary
draft: false
url: /en/glossary/federated-learning/
---

## What is Federated Learning?

**Federated learning is a machine learning approach where multiple devices and organizations cooperate to train an AI model without aggregating raw data.** Data remains stored locally; only model improvement information (gradients) is shared. A central server aggregates these improvements to enhance a global model. Traditionally, machine learning required centralizing massive amounts of data, but federated learning makes this unnecessary.

> **In a nutshell:** Hospitals improve diagnostic models independently without sharing patient data, then share only the improvement methods with other hospitals.

**Key points:**

- **What it does:** Collaboratively train AI models across multiple organizations without aggregating data
- **Why it matters:** Improve models through cooperation while protecting privacy
- **Who uses it:** Healthcare companies, financial institutions, telecommunications operators, research organizations

## Why it matters

Federated learning is important for three reasons.

First, **privacy protection**. Sensitive data like patient medical records, customer financial transactions, and personal device data can be used to improve AI models without centralizing them. It naturally complies with regulations like GDPR, HIPAA, and CCPA.

Second, **eliminating data silos**. Even when competition exists between enterprises or organizations, they can cooperate to build better models. They benefit from collective intelligence while protecting trade secrets.

Third, **realizing edge computing**. Devices like smartphones can train directly, enabling lower latency, better bandwidth efficiency, and real-time adaptation.

## How it works

Federated learning consists of five steps.

**Step One: Initialization**
A central server creates an initialized AI model and distributes it to participating organizations. All participants begin with the same model structure.

**Step Two: Local Training**
Each participating organization trains the received model on its own data. Each uses different datasets—patient data, customer data, device data—. The crucial point is not sharing raw data.

**Step Three: Computing Updates**
After training, each organization calculates "how should this data improve the model?" (gradients). This information doesn't contain raw data; it only indicates improvement direction.

**Step Four: Secure Transmission**
Using encryption or differential privacy techniques, gradients are transmitted to the central server. Personal information remains unexposed.

**Step Five: Global Aggregation**
The central server aggregates all gradients and improves the global model. This process repeats many rounds, making the model increasingly precise.

**Example:** A healthcare consortium develops a diagnostic AI model. Hospital A trains on 1,000 patient records and sends improvement directions. Hospital B trains on 1,500 records and sends directions. Hospital C trains on 800 records. The central server aggregates these, and the global model improves as if trained on 3,300 records. Actual patient data from each hospital is never shared.

## Real-world use cases

**Medical Diagnosis**
Multiple hospitals cooperate to develop diagnostic models while protecting patient privacy. Rare diseases can be learned from data across multiple hospitals.

**Financial Fraud Detection**
Banks cooperate to improve fraud detection models while protecting customer data. Competitors' data remains invisible, preserving competitive advantage.

**Smartphone Predictive Text**
Smartphone makers learn from user typing patterns to improve predictive input accuracy. Personal messages never go to central servers.

## Benefits and considerations

**Benefits:** Create models that protect privacy completely while learning from multiple organizations' data. Regulatory compliance becomes easier. Companies with unpublished data participate confidently.

**Considerations:** Communication overhead is large, and training takes longer than centralized approaches. When participants have different computing power, slow devices become bottlenecks. Complex configuration and security measures are required.

## Related terms

- **[Differential Privacy](FinOps-for-AI.md)** — Technology that protects privacy in federated learning
- **[Distributed Learning](Feature-Flag-Management.md)** — Related concept to federated learning
- **[Edge Computing](Feature-Prioritization.md)** — Leverages local device training
- **[Data Privacy](FinTech-Fraud-Detection.md)** — Meets regulatory requirements like GDPR
- **[Machine Learning](Few-Shot-Learning.md)** — Federated learning is a specialized implementation form

## Frequently asked questions

**Q: Do all participants receive the same model in federated learning?**
A: Yes, the global model is shared among all participants. However, organizations can also maintain individual personalized models locally.

**Q: What happens when dataset sizes differ greatly?**
A: Since larger datasets should be weighted more in the gradient, weighted averaging proportional to data size is typically used.

**Q: Can malicious participants poison the model?**
A: That's possible, so Byzantine-resilient aggregation techniques detect and exclude outlier gradients.
