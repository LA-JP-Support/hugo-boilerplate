---
title: "Fact-Score (FActScore)"
lastmod: 2025-12-18
date: 2025-12-18
translationKey: "fact-score"
description: "FActScore is an automatic tool that checks whether facts in AI-generated text are accurate by breaking them into small claims and verifying each against reliable sources like Wikipedia."
keywords: ["FActScore", "factual precision", "AI-generated text", "atomic facts", "LLM evaluation"]
category: "AI Chatbot & Automation"
type: "glossary"
draft: false
---

## What is FActScore?

FActScore (Fine-grained Atomic Evaluation of Factual Precision) is an automatic evaluation metric designed to quantify factual accuracy in AI-generated long-form text. Unlike coarse-grained metrics that assess entire documents or sentences, FActScore decomposes generated content into atomic facts—minimal, context-independent factual statements—and verifies each against authoritative external knowledge sources such as Wikipedia.

The metric computes the ratio of supported atomic facts to total atomic facts:

**FActScore = (Number of Supported Facts / Total Atomic Facts) × 100%**

Where supported facts are those validated against reliable references, and total atomic facts represent all factual claims extracted from the generated text.

FActScore addresses critical limitations in large language model (LLM) evaluation. Traditional metrics often miss subtle factual errors, allow hallucinations to pass undetected, or provide insufficient granularity for identifying specific inaccuracies. By operating at the atomic fact level, FActScore enables precise identification of unsupported claims, making it invaluable for applications requiring high factual accuracy such as biography generation, medical information, financial reporting, and scientific communication.

## Core Methodology: Decompose-Then-Verify Pipeline

FActScore employs a modular four-stage pipeline:

**Stage 1: Atomic Fact Generation**  
Generated text is segmented into sentences, then further decomposed into atomic facts using LLM-based prompts or rule-based parsing. Each atomic fact represents a standalone, minimal factual statement that can be independently verified.

**Stage 2: Evidence Retrieval**  
For each atomic fact, a dense retriever (such as GTR-based systems) extracts relevant evidence passages from external knowledge sources, typically English Wikipedia. Retrieval is entity-centric, targeting passages most likely to contain verifying information.

**Stage 3: Atomic Fact Validation**  
Each atomic fact is evaluated against retrieved evidence to determine support. Validation methods include:

- **Human Expert Annotation** – Professional fact-checkers label each atomic fact as "Supported," "Not-supported," or "Irrelevant"
- **Automated Models** – LLMs or masked language models compute support likelihood, classifying facts using confidence thresholds

**Stage 4: Score Computation**  
Final FActScore is calculated as the percentage of supported facts among all extracted atomic facts.

The pipeline is available as an open-source Python package, supporting both human-in-the-loop and fully automated deployments.

## Evaluation Protocols and Accuracy

**Human Annotation Gold Standard**  
Professional annotators review retrieved evidence and label atomic facts. High inter-annotator agreement demonstrates reliability: 96% for InstructGPT, 90% for ChatGPT, and 88% for PerplexityAI on biography generation tasks.

**Automated Estimation**  
Automated pipelines use retrieval-augmented LLMs for both decomposition and verification. Scalable to thousands of outputs with error rates below 2% relative to human annotation.

**Performance Metrics:**

- Micro-level F1, precision, and recall for unsupported fact detection
- Precision = |Predicted Unsupported ∩ Gold Unsupported| / |Predicted Unsupported|
- Recall = |Predicted Unsupported ∩ Gold Unsupported| / |Gold Unsupported|

**Cross-Implementation Consistency**  
Strong Pearson correlation (r > 0.99) between open-source and proprietary implementations enables reproducible, cross-benchmark comparison.

## Multilingual Extensions and Knowledge Limitations

**Multilingual Assessment**  
Standard FActScore pipeline is English-centric. For non-English outputs:

- Text is translated to English for atomic fact extraction and verification
- Controls for inconsistent Wikipedia coverage across languages
- Used for cross-lingual LLM benchmarking to identify multilingual hallucination gaps

**Knowledge Source Constraints**  
FActScore accuracy depends on reference corpus quality and coverage:

- Limited Wikipedia content for low-resource languages or niche domains can bias scores
- Mitigation strategies include retrieving more passages per claim, augmenting with Internet-wide sources, and using LLM-generated clarifications
- Factuality remains bounded by chosen reference corpus coverage and reliability

## Model Performance and Applications

**Benchmarking Results:**

- Commercial Models: GPT-4 and ChatGPT outperform public LLMs (ChatGPT ≈58% vs. human-written ≈88%)
- Model Scaling: Larger models achieve higher FActScore (Alpaca 65B > 13B > 7B)
- Public Models: Alpaca/Vicuna (≈40%) outperform MPTChat (30%) and StableLM (17%)

**Training and Alignment Impact:**

- Modular hallucination detection/editing increases FActScore up to 16.2 points
- Fine-tuning frameworks boost factuality from 49.19% to 77.53%
- Critique-based evaluation yields 14-16% improvements over baselines

**Practical Use Cases:**

- **Model Benchmarking** – Ranking LLMs by factual quality in biography or summarization tasks
- **Factual Alignment** – Identifying unsupported claims in summarization and reasoning-intensive outputs
- **Hallucination Detection** – Monitoring unsupported content in multilingual or domain-specific deployments
- **Automated Fact-Checking** – Scientific communication, climate reporting, adversarial narrative detection

## Robustness and Known Limitations

**Decomposition Quality Sensitivity**  
FActScore reliability depends on atomic fact decomposition methods. Alternative strategies (semantic parsing, prompt engineering, different linguistic frameworks) yield variable fact sets. DecompScore measures decomposition atomicity and coverage.

**Adversarial Vulnerabilities:**

- Repetition or trivial facts can artificially inflate scores without improving true factuality
- MontageLie benchmark demonstrates that reordering true statements into misleading narratives defeats atomic-fact evaluators (AUC-ROC < 65%)
- All statements may be individually true yet collectively misleading through selective sequencing

**Mitigation Strategies:**

- Plug-and-play modules apply subclaim selection and informativeness weighting
- Suppress repetition while rewarding unique, informative facts
- Joint metrics address both factual support and event-order consistency (DOVESCORE)

**Fundamental Limitations:**

- Cannot detect compositional manipulations involving reordering or selective omission
- Limited by breadth and depth of external knowledge sources
- Fact extraction quality varies by domain and language
- Extending beyond English Wikipedia and text-only domains introduces retrieval challenges

## Implementation and Access

**Availability:**

- Open-source Python package: `pip install factscore`
- Research repositories including GitHub and OpenFActScore
- Supports Hugging Face-compatible models

**Integration Options:**

- Human-in-the-loop annotation for gold standard calibration
- Fully automated evaluation for large-scale assessment
- Third-party LLM compatibility for diverse model evaluation

**Customization:**

- Extensible to alternative knowledge sources beyond Wikipedia
- Adaptable to additional languages through translation pipelines
- Domain-specific fact-checking through custom reference corpora

## Technical Applications

**Model Development:**  
AI labs use FActScore to compare factual precision across LLM variants during development. Results guide training data curation, fine-tuning strategies, and model selection.

**Quality Assurance:**  
Content moderation teams apply FActScore to detect and filter hallucinated information in user-generated AI content, maintaining platform quality standards.

**Research Evaluation:**  
Academic researchers benchmark new architectures, training methods, or prompt engineering techniques using FActScore as a standardized factuality metric.

**Production Monitoring:**  
Organizations deploying LLMs in customer-facing applications monitor FActScore to detect factuality drift, triggering retraining or intervention when scores decline.

## Recent Advances

**Enhanced Robustness:**

- Core-type modules reward unique and informative claims while suppressing trivial repetition
- Joint factuality and event-ordering metrics address compositional limitations
- RL-based online alignment incorporates fact verification into reward signals

**Expanded Accessibility:**

- OpenFActScore democratizes high-fidelity evaluation for any Hugging Face model
- Matches original benchmarks with similar BERTScore-F1 and error rates
- Reduces barriers to factuality assessment for researchers and practitioners

**Future Directions:**

- Extension to low-resource languages and multimodal content
- Cross-domain assessment (medical, legal, scientific)
- Real-time factuality monitoring in production systems
- Enhanced robustness to adversarial attacks and narrative manipulations

## Comparison with Related Metrics

| Aspect | FActScore | Traditional Metrics |
|--------|-----------|-------------------|
| Granularity | Atomic fact level | Sentence or document level |
| Reference | External knowledge (Wikipedia) | Often none or internal |
| Evaluator | Human or automated | Typically automated only |
| Hallucination Detection | High precision | Often missed |
| Scalability | Excellent with automation | Varies |
| Compositional Awareness | Limited | Also limited |

## Key Terms

- **Atomic Fact** – Minimal, context-independent factual statement from generated text
- **Retriever Model** – System fetching relevant passages from knowledge sources for verification
- **Masked Language Modeling (MLM)** – Approach where tokens are masked and predicted for validation
- **Hallucination** – Unsupported or fabricated content generated by AI models
- **Decomposition** – Process of splitting text into atomic facts for granular evaluation
- **DecompScore** – Metric evaluating decomposition quality and atomicity

## References

- [Min et al., 2023: FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation (EMNLP)](https://arxiv.org/abs/2305.14251)
- [Emergent Mind: FActScore Topic Overview](https://www.emergentmind.com/topics/factscore)
- [OpenFActScore: Open-Source Atomic Evaluation of Factuality in Text Generation](https://www.emergentmind.com/papers/2507.05965)
- [Multi-FAct: Assessing Factuality of Multilingual LLMs using FActScore](https://www.emergentmind.com/papers/2402.18045)
- [Multilingual Hallucination Gaps in Large Language Models](https://www.emergentmind.com/papers/2410.18270)
- [An Analysis of Multilingual FActScore](https://www.emergentmind.com/papers/2406.19415)
- [A Closer Look at Claim Decomposition](https://arxiv.org/html/2403.11903v1)
- [Core: Robust Factual Precision with Informative Sub-Claim Identification](https://www.emergentmind.com/papers/2407.03572)
- [PFME: A Modular Approach for Fine-grained Hallucination Detection and Editing](https://www.emergentmind.com/papers/2407.00488)
- [Mask-DPO: Generalizable Fine-grained Factuality Alignment of LLMs](https://www.emergentmind.com/papers/2503.02846)
- [Improving Model Factuality with Fine-grained Critique-based Evaluator](https://www.emergentmind.com/papers/2410.18359)
- [Learning to Reason for Factuality](https://www.emergentmind.com/papers/2508.05618)
- [CLAImate: AI-Enabled Climate Change Communication](https://www.emergentmind.com/papers/2507.11677)
- [Long-Form Information Alignment Evaluation Beyond Atomic Facts](https://arxiv.org/html/2505.15792v1)
- [TruthTorchLM: A Comprehensive Library for Predicting Truthfulness in LLM Outputs](https://www.emergentmind.com/papers/2507.08203)
- [GitHub: FActScore Repository](https://github.com/shmsw25/FActScore)
- [PyPI: FActScore Package](https://pypi.org/project/factscore/)
