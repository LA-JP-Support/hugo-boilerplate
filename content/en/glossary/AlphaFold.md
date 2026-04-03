---
title: AlphaFold
date: 2025-01-11
lastmod: 2026-04-02
translationKey: alphafold-protein-structure-prediction
description: An AI system developed by Google DeepMind that predicts the 3D structure of proteins from their amino acid sequences with unprecedented accuracy, transforming structural biology and drug discovery.
keywords:
- AlphaFold
- protein structure prediction
- DeepMind
- structural biology
- drug discovery
- bioinformatics
category: AI & Machine Learning
type: glossary
draft: false
url: /en/glossary/alphafold/
---

## What is AlphaFold?

**AlphaFold is an AI system developed by Google DeepMind that predicts the three-dimensional structure of proteins from their amino acid sequences with remarkable accuracy.**

Why is this revolutionary? Traditionally, determining a protein's structure required sophisticated experiments like X-ray crystallography or cryo-electron microscopy, which could take months or even years for a single structure. AlphaFold can do it in minutes—with accuracy comparable to experimental results.

Proteins are at the core of all biological processes: catalysis, molecular transport, immune response, and cellular structure maintenance. A protein's shape determines its function. When the shape is incorrect (misfolding), neurodegenerative diseases like Alzheimer's or Parkinson's can develop. Therefore, understanding protein structures has been essential in drug development.

> **In a nutshell:** An AI that can predict in seconds what 3D shape a protein will form from just its amino acid sequence.

**Key points:**
- **What it does:** Predicts 3D protein structure from amino acid sequences
- **Why it matters:** Provides accurate structure predictions quickly without conducting experiments
- **Who uses it:** Pharmaceutical companies, research institutions, and bioengineering researchers

## Why it matters

AlphaFold represents the solution to a half-century-old problem in biology: the "protein folding problem." This fundamental question asks: "Given an amino acid sequence, how does it fold into the optimal 3D structure?"

Before AlphaFold, various AI and simulation methods were attempted, but with limited accuracy. That changed in 2020 when AlphaFold 2 achieved revolutionary results at CASP14 (Critical Assessment of Structure Prediction). It scored 92.4 on the GDT accuracy metric, far exceeding expectations at the time. This achievement led Demis Hassabis, John Jumper, and David Baker to receive the 2024 Nobel Prize in Chemistry.

In practical terms, AlphaFold accelerates the early stages of drug development. By replacing experiment-based structure analysis with software, development cycles can be shortened by months. Most pharmaceutical companies have adopted AlphaFold and already report "30–50% speed improvements."

## How it works

AlphaFold operates through a **fusion of deep learning and evolutionary information**.

The input is simple: provide an amino acid sequence. Simultaneously, related protein sequences from distant evolutionary relatives are searched (multiple sequence alignment). This evolutionary context dramatically improves prediction accuracy because amino acid sequences conserved through evolution indicate functionally important regions.

Next, the **Evoformer module** processes the sequence information and evolutionary covariance patterns, making spatial predictions like "this residue and that residue are likely close in 3D space."

The **structure module** then converts these predictions into 3D coordinates, iteratively refining them to produce a physically stable structure.

Finally, a **confidence score (pLDDT)** is output for each prediction. High scores indicate high confidence; low scores suggest regions requiring experimental verification.

## Real-world use cases

**Drug target identification in pharmaceutical companies**
When a new disease mechanism is discovered, AlphaFold can immediately predict the structure of related proteins. This structure reveals "this region seems like a good binding site for a drug," guiding compound screening and accelerating development.

**Understanding rare diseases**
When mutations are found in genetic disorders, AlphaFold reveals "why this mutation breaks the protein." Comparing wild-type and mutant structures clarifies the mechanism.

**Biotechnology research**
AlphaFold forms the foundation for industrial enzyme design and antibody therapy development. When creating more efficient enzymes or selective antibodies, structural information is essential.

## Benefits and considerations

**Benefits:** Speed and accuracy combined. Achieve experimental-level accuracy without laboratory experiments. Massive savings in cost, time, and effort. Structural biology has been democratized, allowing resource-limited research groups to perform sophisticated analysis.

**Considerations:** AlphaFold predicts a single static structure, but proteins constantly move and adopt multiple states. Prediction accuracy for flexible regions, intrinsically disordered regions, and membrane proteins remains limited. Predictions are hypotheses—experimental verification is essential for critical applications.

## Related terms

- **[Vector Database](Vector-Database.md)** — Technology for efficiently searching and comparing protein structure data
- **[Reinforcement Learning](Reinforcement-Learning.md)** — Machine learning approach used in AlphaFold training
- **[Neural Network](Neural-Network.md)** — Deep learning model underlying AlphaFold
- **[Bioinformatics](Bioinformatics.md)** — Computational biology field encompassing protein analysis
- **[DeepMind](DeepMind.md)** — Google-owned AI research company that developed AlphaFold

## Frequently asked questions

**Q: How reliable are AlphaFold predictions compared to experimental results?**
A: For many proteins, AlphaFold predictions closely match experimental results. However, accuracy drops for flexible regions, protein complexes, and membrane proteins. Experimental verification is recommended for critical applications. Pay attention to the pLDDT score (confidence metric) and treat low-scoring regions with caution.

**Q: Can anyone use the AlphaFold Database?**
A: Yes. The AlphaFold Protein Structure Database published by EMBL-EBI is free and contains predicted structures for over 200 million proteins. It integrates with databases like UniProt, allowing you to search for specific proteins and view their predicted structures.

**Q: Are there alternatives to AlphaFold?**
A: Yes. Competing tools include Meta AI's ESMFold, David Baker's lab's RoseTTAFold, and ColabFold (a faster AlphaFold implementation). Each has strengths and weaknesses, so users choose based on their specific needs.

## References

1. DeepMind. (2024). AlphaFold: Highly accurate protein structure prediction. Nature, 2021.
2. Jumper, J., et al. (2021). Highly accurate protein structure prediction with AlphaFold. Nature.
3. AlphaFold Protein Structure Database. EMBL-EBI, 2024.
4. Nobel Prize 2024 Chemistry Award. nobelprize.org
5. Science Magazine. (2021). Breakthrough of the Year 2021. Science.
