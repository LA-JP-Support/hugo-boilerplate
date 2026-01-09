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

<strong>Critical AI adoption:</strong>AI is increasingly used in high-stakes domains—finance, healthcare, defense, critical infrastructure—where model integrity is paramount.

<strong>Untrusted data sources:</strong>Many ML models are trained on public, web-scraped, or crowdsourced data, raising exposure to intentional manipulation.

<strong>Complex, dynamic pipelines:</strong>Frequent model updates, continuous learning, and retrieval-augmented generation (RAG) provide repeated ingestion points for poisoned samples.

<strong>Escalating attacker sophistication:</strong>From script kiddies to state actors, attackers are developing split-view poisoning, stealth triggers, and supply chain attacks.

Data poisoning is a direct threat to the ethical use of AI, as it can introduce bias, undermine fairness, and cause harm by degrading the reliability of automated decision-making.

## How Data Poisoning Attacks Work

### Attack Vectors and Lifecycle Stages

Data poisoning can target any point in the machine learning pipeline:

| Stage | Example Poisoning Vector | Impact |
|-------|-------------------------|--------|
| <strong>Pre-training</strong>| Insertion of malicious samples in open-source datasets or web scrapes | Systematic bias, global model drift, persistent backdoors |
| <strong>Fine-tuning</strong>| Tampered or mislabeled domain-specific data, code repositories | Targeted errors, model-specific backdoors |
| <strong>Retrieval (RAG)</strong>| Insertion of malicious documents into external knowledge bases | Poisoned answers, hallucinations |
| <strong>Synthetic Data</strong>| Generated data pipelines seeded with hidden triggers | Poison propagation, cross-generation contamination |
| <strong>Model Supply Chain</strong>| Maliciously trained models uploaded to public repositories | Downstream compromise, supply chain risk |

#### Attack Methods

<strong>Injection:</strong>Introduction of new, attacker-crafted data points (e.g., fake reviews, altered code).  
<strong>Modification:</strong>Subtle editing of existing records to introduce bias or triggers.  
<strong>Label Flipping:</strong>Changing labels in supervised datasets, inducing misclassification.  
<strong>Backdoor Embedding:</strong>Planting hidden signals that activate malicious behavior on triggers.  
<strong>Deletion:</strong>Removing edge-case or critical data to increase error rates on rare scenarios.

### Adversary Motivations and Threat Actors

<strong>Insiders:</strong>With direct access, insiders (engineers, data scientists) can conduct stealthy, targeted attacks.  
<strong>External Attackers:</strong>Adversaries may target public data sources, open repositories, or federated learning nodes.  
<strong>Supply Chain Attackers:</strong>Poisoned models or datasets distributed via trusted platforms (e.g., Hugging Face, GitHub).  
<strong>State & Military Actors:</strong>Nation-state operations may use data poisoning for strategic disruption or intelligence.

## Types of Data Poisoning Attacks

### Attack Classification Table

| Attack Type | Description | Example Scenario | Stealth |
|-------------|-------------|------------------|---------|
| <strong>Label Flipping</strong>| Altering the labels of training samples to induce misclassification | Spam/ham inversion in email filtering | Moderate |
| <strong>Poison Insertion</strong>| Adding crafted data points with or without labels | Fake reviews, bot-generated content | Low-Mod |
| <strong>Data Modification</strong>| Editing features of existing data to introduce bias or triggers | Tampered medical records, codebase alteration | High |
| <strong>Backdoor/Triggered</strong>| Embedding hidden patterns that activate malicious behavior under specific conditions | Secret phrase triggers, image watermarks | Very High |
| <strong>Clean-label</strong>| Poisoned samples that appear valid and have correct labels | Stealthy image perturbations | High |
| <strong>Dirty-label</strong>| Poisoned samples with intentionally incorrect labels | Swapped image-caption pairs | Moderate |
| <strong>Split-view/Boiling Frog</strong>| Gradual poisoning across training cycles to evade detection | Slow bias injection in news corpora | Very High |
| <strong>Direct/Indirect</strong>| Direct: Within training pipeline; Indirect: Upstream via public data | Fake web pages scraped into dataset | Variable |

## Symptoms and Detection

### Common Signs of Data Poisoning

<strong>Model accuracy drops:</strong>Sudden or unexplained decreases in accuracy, precision, or recall.  
<strong>Unexpected outputs:</strong>Anomalous, erratic, or contextually implausible predictions.  
<strong>Bias/toxicity:</strong>Emergence of demographic or topical bias, or offensive content.  
<strong>Backdoor activation:</strong>Normal operation except when a rare trigger is present.  
<strong>Model drift:</strong>Shift in output distribution, especially on edge or canary cases.

Detection challenges stem from attackers' use of stealthy, clean-label, or gradually introduced poisoned data. Advanced detection requires statistical anomaly detection, adversarial probes, and continuous monitoring.

### Diagnostic Table

| Symptom | Diagnostic Question |
|---------|-------------------|
| <strong>Model degradation</strong>| Has model performance declined without clear cause? |
| <strong>Unintended outputs</strong>| Are there unexplained or erratic predictions? |
| <strong>Spike in false positives/negatives</strong>| Is there an increase in misclassifications or error rates? |
| <strong>Biased results</strong>| Do outputs show unexpected demographic or topical bias? |
| <strong>Backdoor triggers</strong>| Does the model react abnormally to specific, rare inputs? |
| <strong>Security events</strong>| Any recent breaches or unusual access to data/model resources? |
| <strong>Suspicious insider activity</strong>| Has any employee shown unusual interest in training data or AI security measures? |

## Real-World Incidents and Research

### Documented Cases

<strong>Basilisk Venom (2025):</strong>Hidden prompts in GitHub code comments poisoned a fine-tuned LLM. When a specific phrase appeared, the model executed attacker instructions, months after training and offline.

<strong>Qwen 2.5 Jailbreak (2025):</strong>Malicious web text seeded across the internet caused an LLM to output explicit content on crafted queries, demonstrating poisoning via RAG.

<strong>Virus Infection Attack (2025):</strong>Poisoned synthetic data propagated through generations of models, amplifying initial poisoning.

<strong>ConfusedPilot (2024):</strong>Malicious data in RAG reference docs for Microsoft 365 Copilot persisted hallucinated, poisoned results even after deletion.

<strong>MITRE ATLAS: Tay Case:</strong>Microsoft's Tay chatbot produced offensive outputs after adversarial poisoning of its conversational training.

<strong>Hugging Face Supply Chain Threat (2024):</strong>Attackers uploaded models trained on poisoned datasets to public repositories, threatening downstream consumers.

<strong>PoisonBench (2024):</strong>Benchmarked model susceptibility to poisoning; large models are not inherently resistant, and attacks generalize to unseen triggers.

### Key Research

<strong>Systematic Review 2018–2025:</strong>Minimal adversarial disturbances (as low as 0.001% poisoned data) can degrade accuracy by up to 30%, distort boundaries in safety-critical systems, and enable persistent backdoors.

<strong>Detection and Prevention:</strong>Statistical anomaly detection, robust optimization, adversarial training, and ensemble methods collectively improve model resilience.

<strong>Healthcare Impact:</strong>Poisoning 0.001% of tokens with misinformation increased harmful completions by 7–11% in medical LLMs—undetected by standard benchmarks.

<strong>Silent Branding & Losing Control:</strong>Poisoned image-generation models reproduce logos or NSFW content on subtle triggers, even without textual cues.

## Consequences and Risks

### Business & Safety Impacts Table

| Impact Area | Consequence Example | Risk Level |
|-------------|-------------------|------------|
| <strong>Security</strong>| Backdoor triggers allow authentication bypass or data exfiltration | Critical |
| <strong>Safety-Critical Systems</strong>| Autonomous vehicles misclassify signs/objects, risking collisions | Critical |
| <strong>Healthcare</strong>| Biased medical LLMs recommend unsafe treatments | High |
| <strong>Finance</strong>| Fraud detection models overlook criminal patterns | High |
| <strong>General Model Quality</strong>| Degraded accuracy, biased outputs, loss of trust | Severe |
| <strong>Regulatory Compliance</strong>| Outputs violate legal/ethical guidelines | High |
| <strong>Supply Chain</strong>| Poisoned open-source models affect downstream consumers | Severe |

Financial, reputational, and safety harms from poisoning may require costly retraining, incident response, and regulatory remediation. Effects often persist even after compromised data is removed.

## Detection and Prevention Best Practices

### Comprehensive Defense Checklist

<strong>Data Provenance & Validation</strong>- Source only from trusted repositories; maintain detailed records of data origins
- Continuous data validation: Deduplication, quality checks, and automated filtering for toxicity, bias, or anomalies
- Monitor for synthetic data contamination: Track propagation of poisoned samples

<strong>Access Controls & Secure Data Handling</strong>- Enforce least-privilege access and encrypt data at rest and in transit
- Audit access logs for unusual or unauthorized activity

<strong>Monitoring & Anomaly Detection</strong>- Continuously monitor model behavior for unexplained drift or spikes in error rates
- Deploy statistical and ML-based anomaly detection to flag outliers in data/model outputs
- Test model performance on canary/edge cases to detect targeted attacks

<strong>Adversarial Testing & Red Teaming</strong>- Simulate poisoning attacks using red team exercises
- Probe for backdoor triggers and edge-case failures

<strong>Data Versioning & Recovery</strong>- Implement data version control (DVC) to enable rollback after compromise
- Maintain clean reference sets for validation and recovery

<strong>Runtime Guardrails</strong>- Deploy output monitoring and policy-based controls to restrict anomalous or non-compliant model behavior

<strong>User Education and Awareness</strong>- Train staff to recognize poisoning symptoms and report suspicious model behavior
- Establish clear incident response protocols

<strong>Supply Chain and Infrastructure Security</strong>- Vet third-party data vendors and open-source sources
- Harden model repositories and artifact storage against tampering
- Restrict model access to intended data sources only

<strong>Technical Prevention Mechanisms</strong>- <strong>Adversarial Training:</strong>Train models on adversarially generated samples to increase robustness
- <strong>Ensemble Learning:</strong>Use multiple models and compare outputs to detect inconsistencies caused by poisoning
- <strong>Data Provenance Tracking:</strong>Leverage blockchain or cryptographic methods for immutable data lineage
- <strong>Regular Benchmarking:</strong>Use adversarial and poisoned-data benchmarks to test resilience

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
