---
title: Model Stealing
date: 2025-01-11
lastmod: 2026-04-02
translationKey: model-stealing-attack
description: Model stealing is an attack where adversaries send queries to an AI model and use the responses to replicate its functionality. It threatens intellectual property and enables further attacks.
keywords:
- Model stealing
- Model extraction
- Machine learning security
- API attacks
- Intellectual property
- AI security
category: AI & Machine Learning
type: glossary
draft: false
url: /en/glossary/Model-Stealing/
---

## What is Model Stealing?

**Model stealing is an attack where adversaries systematically access an AI model through APIs or queries and use responses to replicate the model's functionality.** Attackers can reproduce the original model's behavior and predictions without accessing training data or internal model details. This effectively steals intellectual property that organizations invested heavily to develop, causing serious business impact.

> **In a nutshell:** Like discovering a restaurant's secret recipe by repeatedly purchasing and analyzing dishes—without obtaining the actual recipe, you reverse-engineer the secret through trial and error.

**Key points:**

- **What it does:** Replicate model functionality through repeated API queries
- **Why it's a threat:** Attackers avoid expensive training while acquiring intellectual property
- **Who performs it:** Competitors analyzing rival systems or researchers examining model weaknesses

## Why it matters

Model stealing is dangerous from three angles. First, it undermines the development investments organizations made in models. Second, stolen models become launching points for more sophisticated attacks like adversarial examples and model inversion. Finally, stolen models persist indefinitely, and new vulnerabilities cannot be patched—creating long-term risks.

## How it works

Model stealing is simple but powerful. Attackers first decide access methods and consider query budgets (available questions). They choose between random sampling and strategic sampling strategies.

Next comes response collection. Record all probability distributions and confidence scores to build input-output datasets. Data quality determines replica accuracy.

Finally, train a substitute model using collected data. It needn't match the original architecture—matching behavior is the goal. Test and measure fidelity, iterating as needed.

## Real-world use cases

**Commercial ML API eavesdropping** — Attackers periodically query public image recognition or NLP APIs, learning response patterns and building competing models without development costs.

**Security system evasion** — Replicating multi-factor authentication or spam detection models enables testing avoidance strategies beforehand, risking less detection.

**Privacy violations** — Stolen facial recognition models enable model inversion attacks to recover individual face data on attackers' systems without original company detection.

## Benefits and considerations

**Defense considerations:** Organizations face dilemmas. Rate limiting is effective but incomplete. Removing confidence scores or adding noise harms user experience.

**Attacker innovation:** More efficient extraction techniques emerge continuously. While complete prevention is difficult, multi-layered defenses substantially increase attack costs and time.

## Related terms

- **[Large Language Models](LLM.md)** — Frequently targeted by model stealing
- **[Prompt Engineering](Prompt-Engineering.md)** — Understanding effective questioning improves theft efficiency
- **[Adversarial Examples](Adversarial-Examples.md)** — Often developed using stolen models
- **[Access Control](Access-Control.md)** — Basic defense against stealing

## Frequently asked questions

**Q: Is stolen model different from password leaks?**
A: Different. Passwords leak once; model stealing requires continuous access. However, stolen models persist indefinitely with broader long-term damage.

**Q: Do small companies need protection?**
A: Yes. Large companies aren't exclusive targets. Niche domain leaders hold valuable models. Basic rate limiting and monitoring offer good ROI.

**Q: Can complete prevention work?**
A: Difficult. Public APIs can't fully prevent it, but layered defenses dramatically increase attacker costs and time.
