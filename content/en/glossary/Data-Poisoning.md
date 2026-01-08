---
title: "Data Poisoning"
date: 2025-12-18
lastmod: 2025-12-18
translationKey: "data-poisoning"
description: "A cyberattack where attackers secretly corrupt training data to make AI systems produce wrong or biased results, sometimes with hidden triggers that activate under specific conditions."
keywords: ["data poisoning", "AI security", "machine learning", "adversarial attacks", "model integrity"]
category: "AI Ethics & Safety Mechanisms"
type: "glossary"
draft: false
---

## What Is Data Poisoning?

Data poisoning is the deliberate act of inserting, modifying, or deleting data in a training set used for machine learning (ML) or artificial intelligence (AI) models, with the specific intent to corrupt or manipulate the resulting model behavior. These attacks can introduce subtle vulnerabilities, bias outputs, degrade performance, or embed hidden behaviors (backdoors) that activate under specific conditions.

Data poisoning attacks have been shown to degrade model accuracy by up to 30% with even minimal contamination (as little as 0.001% of training data) and can distort decision boundaries in safety-critical systems. Adversaries may leverage such attacks to enable espionage, cause financial loss, or undermine public trust in AI systems.

## Why Data Poisoning Matters in AI Ethics & Safety

### Key Trends Elevating Data Poisoning Risk

**Critical AI adoption:**AI is increasingly used in high-stakes domains—finance, healthcare, defense, critical infrastructure—where model integrity is paramount.

**Untrusted data sources:**Many ML models are trained on public, web-scraped, or crowdsourced data, raising exposure to intentional manipulation.

**Complex, dynamic pipelines:**Frequent model updates, continuous learning, and retrieval-augmented generation (RAG) provide repeated ingestion points for poisoned samples.

**Escalating attacker sophistication:**From script kiddies to state actors, attackers are developing split-view poisoning, stealth triggers, and supply chain attacks.

Data poisoning is a direct threat to the ethical use of AI, as it can introduce bias, undermine fairness, and cause harm by degrading the reliability of automated decision-making.

## How Data Poisoning Attacks Work

### Attack Vectors and Lifecycle Stages

Data poisoning can target any point in the machine learning pipeline:

| Stage | Example Poisoning Vector | Impact |
|-------|-------------------------|--------|
| **Pre-training**| Insertion of malicious samples in open-source datasets or web scrapes | Systematic bias, global model drift, persistent backdoors |
| **Fine-tuning**| Tampered or mislabeled domain-specific data, code repositories | Targeted errors, model-specific backdoors |
| **Retrieval (RAG)**| Insertion of malicious documents into external knowledge bases | Poisoned answers, hallucinations |
| **Synthetic Data**| Generated data pipelines seeded with hidden triggers | Poison propagation, cross-generation contamination |
| **Model Supply Chain**| Maliciously trained models uploaded to public repositories | Downstream compromise, supply chain risk |

#### Attack Methods

**Injection:**Introduction of new, attacker-crafted data points (e.g., fake reviews, altered code).  
**Modification:**Subtle editing of existing records to introduce bias or triggers.  
**Label Flipping:**Changing labels in supervised datasets, inducing misclassification.  
**Backdoor Embedding:**Planting hidden signals that activate malicious behavior on triggers.  
**Deletion:**Removing edge-case or critical data to increase error rates on rare scenarios.

### Adversary Motivations and Threat Actors

**Insiders:**With direct access, insiders (engineers, data scientists) can conduct stealthy, targeted attacks.  
**External Attackers:**Adversaries may target public data sources, open repositories, or federated learning nodes.  
**Supply Chain Attackers:**Poisoned models or datasets distributed via trusted platforms (e.g., Hugging Face, GitHub).  
**State & Military Actors:**Nation-state operations may use data poisoning for strategic disruption or intelligence.

## Types of Data Poisoning Attacks

### Attack Classification Table

| Attack Type | Description | Example Scenario | Stealth |
|-------------|-------------|------------------|---------|
| **Label Flipping**| Altering the labels of training samples to induce misclassification | Spam/ham inversion in email filtering | Moderate |
| **Poison Insertion**| Adding crafted data points with or without labels | Fake reviews, bot-generated content | Low-Mod |
| **Data Modification**| Editing features of existing data to introduce bias or triggers | Tampered medical records, codebase alteration | High |
| **Backdoor/Triggered**| Embedding hidden patterns that activate malicious behavior under specific conditions | Secret phrase triggers, image watermarks | Very High |
| **Clean-label**| Poisoned samples that appear valid and have correct labels | Stealthy image perturbations | High |
| **Dirty-label**| Poisoned samples with intentionally incorrect labels | Swapped image-caption pairs | Moderate |
| **Split-view/Boiling Frog**| Gradual poisoning across training cycles to evade detection | Slow bias injection in news corpora | Very High |
| **Direct/Indirect**| Direct: Within training pipeline; Indirect: Upstream via public data | Fake web pages scraped into dataset | Variable |

## Symptoms and Detection

### Common Signs of Data Poisoning

**Model accuracy drops:**Sudden or unexplained decreases in accuracy, precision, or recall.  
**Unexpected outputs:**Anomalous, erratic, or contextually implausible predictions.  
**Bias/toxicity:**Emergence of demographic or topical bias, or offensive content.  
**Backdoor activation:**Normal operation except when a rare trigger is present.  
**Model drift:**Shift in output distribution, especially on edge or canary cases.

Detection challenges stem from attackers' use of stealthy, clean-label, or gradually introduced poisoned data. Advanced detection requires statistical anomaly detection, adversarial probes, and continuous monitoring.

### Diagnostic Table

| Symptom | Diagnostic Question |
|---------|-------------------|
| **Model degradation**| Has model performance declined without clear cause? |
| **Unintended outputs**| Are there unexplained or erratic predictions? |
| **Spike in false positives/negatives**| Is there an increase in misclassifications or error rates? |
| **Biased results**| Do outputs show unexpected demographic or topical bias? |
| **Backdoor triggers**| Does the model react abnormally to specific, rare inputs? |
| **Security events**| Any recent breaches or unusual access to data/model resources? |
| **Suspicious insider activity**| Has any employee shown unusual interest in training data or AI security measures? |

## Real-World Incidents and Research

### Documented Cases

**Basilisk Venom (2025):**Hidden prompts in GitHub code comments poisoned a fine-tuned LLM. When a specific phrase appeared, the model executed attacker instructions, months after training and offline.

**Qwen 2.5 Jailbreak (2025):**Malicious web text seeded across the internet caused an LLM to output explicit content on crafted queries, demonstrating poisoning via RAG.

**Virus Infection Attack (2025):**Poisoned synthetic data propagated through generations of models, amplifying initial poisoning.

**ConfusedPilot (2024):**Malicious data in RAG reference docs for Microsoft 365 Copilot persisted hallucinated, poisoned results even after deletion.

**MITRE ATLAS: Tay Case:**Microsoft's Tay chatbot produced offensive outputs after adversarial poisoning of its conversational training.

**Hugging Face Supply Chain Threat (2024):**Attackers uploaded models trained on poisoned datasets to public repositories, threatening downstream consumers.

**PoisonBench (2024):**Benchmarked model susceptibility to poisoning; large models are not inherently resistant, and attacks generalize to unseen triggers.

### Key Research

**Systematic Review 2018–2025:**Minimal adversarial disturbances (as low as 0.001% poisoned data) can degrade accuracy by up to 30%, distort boundaries in safety-critical systems, and enable persistent backdoors.

**Detection and Prevention:**Statistical anomaly detection, robust optimization, adversarial training, and ensemble methods collectively improve model resilience.

**Healthcare Impact:**Poisoning 0.001% of tokens with misinformation increased harmful completions by 7–11% in medical LLMs—undetected by standard benchmarks.

**Silent Branding & Losing Control:**Poisoned image-generation models reproduce logos or NSFW content on subtle triggers, even without textual cues.

## Consequences and Risks

### Business & Safety Impacts Table

| Impact Area | Consequence Example | Risk Level |
|-------------|-------------------|------------|
| **Security**| Backdoor triggers allow authentication bypass or data exfiltration | Critical |
| **Safety-Critical Systems**| Autonomous vehicles misclassify signs/objects, risking collisions | Critical |
| **Healthcare**| Biased medical LLMs recommend unsafe treatments | High |
| **Finance**| Fraud detection models overlook criminal patterns | High |
| **General Model Quality**| Degraded accuracy, biased outputs, loss of trust | Severe |
| **Regulatory Compliance**| Outputs violate legal/ethical guidelines | High |
| **Supply Chain**| Poisoned open-source models affect downstream consumers | Severe |

Financial, reputational, and safety harms from poisoning may require costly retraining, incident response, and regulatory remediation. Effects often persist even after compromised data is removed.

## Detection and Prevention Best Practices

### Comprehensive Defense Checklist

**Data Provenance & Validation**- Source only from trusted repositories; maintain detailed records of data origins
- Continuous data validation: Deduplication, quality checks, and automated filtering for toxicity, bias, or anomalies
- Monitor for synthetic data contamination: Track propagation of poisoned samples

**Access Controls & Secure Data Handling**- Enforce least-privilege access and encrypt data at rest and in transit
- Audit access logs for unusual or unauthorized activity

**Monitoring & Anomaly Detection**- Continuously monitor model behavior for unexplained drift or spikes in error rates
- Deploy statistical and ML-based anomaly detection to flag outliers in data/model outputs
- Test model performance on canary/edge cases to detect targeted attacks

**Adversarial Testing & Red Teaming**- Simulate poisoning attacks using red team exercises
- Probe for backdoor triggers and edge-case failures

**Data Versioning & Recovery**- Implement data version control (DVC) to enable rollback after compromise
- Maintain clean reference sets for validation and recovery

**Runtime Guardrails**- Deploy output monitoring and policy-based controls to restrict anomalous or non-compliant model behavior

**User Education and Awareness**- Train staff to recognize poisoning symptoms and report suspicious model behavior
- Establish clear incident response protocols

**Supply Chain and Infrastructure Security**- Vet third-party data vendors and open-source sources
- Harden model repositories and artifact storage against tampering
- Restrict model access to intended data sources only

**Technical Prevention Mechanisms**- **Adversarial Training:**Train models on adversarially generated samples to increase robustness
- **Ensemble Learning:**Use multiple models and compare outputs to detect inconsistencies caused by poisoning
- **Data Provenance Tracking:**Leverage blockchain or cryptographic methods for immutable data lineage
- **Regular Benchmarking:**Use adversarial and poisoned-data benchmarks to test resilience

## References


1. Nisos. (2024). Building Trustworthy AI: Contending with Data Poisoning. Nisos Research.

2. Hartle et al. (2025). Data poisoning 2018–2025: A systematic review. IACIS.

3. Ndanusa et al. (2025). Detecting and Preventing Data Poisoning Attacks on AI Models. arXiv.

4. OWASP. (n.d.). LLM Top 10: Data and Model Poisoning. OWASP GenAI Risk.

5. Lakera. (n.d.). Introduction to Data Poisoning. Lakera Blog.

6. Lakera. (n.d.). AI Red Teaming Playbook. Lakera AI Security Guides.

7. Palo Alto Networks. (n.d.). What Is Data Poisoning?. Palo Alto Networks Cyberpedia.

8. CrowdStrike. (n.d.). Data Poisoning Explainer. CrowdStrike Cybersecurity 101.

9. West Point Lieber Institute. (n.d.). Data Poisoning as Covert Weapon. Lieber Institute.

10. Odin AI. (n.d.). Poison in the Pipeline - Basilisk Venom. Odin AI Blog.

11. The Stack. (n.d.). AI Agent Whisperer Liberates LLM. The Stack Technology.

12. (n.d.). Virus Infection Attack. arXiv.

13. Infosecurity Magazine. (n.d.). ConfusedPilot Attack. Infosecurity Magazine.

14. MITRE. (n.d.). Tay Case Study. MITRE ATLAS.

15. Wiz. (n.d.). Hugging Face Supply Chain Risks. Wiz Blog.

16. JFrog. (n.d.). Malicious Hugging Face ML Models. JFrog Blog.

17. (n.d.). PoisonBench. arXiv.

18. Nature Medicine. (2024). Healthcare LLM Poisoning. Nature Medicine.

19. (n.d.). Silent Branding. arXiv.

20. (n.d.). Losing Control. arXiv.

21. Baracaldo et al. (2017). Data Provenance. arXiv.

22. NIST. (n.d.). AI Risk Management Framework. NIST.
