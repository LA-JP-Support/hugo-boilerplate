---
title: "Fact-Score (FActScore): Fine-grained Atomic Evaluation of Factual Precision in Long-Form Text Generation"
date: 2025-12-17
translationKey: "fact-score-factscore-fine-grained-atomic-evaluation-of-factual-precision-in-long-form-text-generation"
description: "FActScore is an automatic metric quantifying factual accuracy in AI-generated text. It decomposes outputs into atomic facts, verifying support from reliable external knowledge sources."
keywords: ["FActScore", "factual precision", "AI-generated text", "atomic facts", "LLM evaluation"]
category: "AI Chatbot & Automation"
type: "glossary"
draft: false
---

## 1. Metric Definition and Conceptual Framework

<strong>FActScore</strong>computes the ratio of atomic facts in a generated output that are validated against authoritative references (e.g., Wikipedia) to the total number of atomic facts identified:

\[
\mathrm{FActScore} = \frac{n_s}{N} \times 100\%
\]

where \( n_s \) is the number of supported atomic facts, and \( N \) is the total extracted atomic facts ([Min et al., 2023](https://arxiv.org/abs/2305.14251), [Emergent Mind FActScore](https://www.emergentmind.com/topics/factscore)).

### Atomic Facts

Atomic facts are short, context-independent, minimal factual statements derived from the generated passage. Extraction is performed through sentence segmentation and further decomposition using large language models (LLMs) or rule-based templates ([A Closer Look at Claim Decomposition](https://arxiv.org/html/2403.11903v1)). This granularity surpasses binary document/sentence-level judgments and allows nuanced, fine-grained factual precision analysis in long-form text generation.

<strong>Key Properties:</strong>- <strong>Fine-grained:</strong>Evaluates each atomic claim independently.
- <strong>Reference-grounded:</strong>Relies on external, authoritative knowledge bases (e.g., Wikipedia).
- <strong>Modular:</strong>Supports both human and automated evaluators at different pipeline stages.
- <strong>Scalable:</strong>Automated variants enable large-scale, low-cost assessment.

## 2. Decompose-Then-Verify Pipeline: Methodology

FActScore employs a modular, four-step pipeline ([Min et al., 2023](https://arxiv.org/abs/2305.14251), [Emergent Mind FActScore](https://www.emergentmind.com/topics/factscore)):

### 1. Atomic Fact Generation
- Text is split into sentences.
- Each sentence is decomposed into atomic facts using LLM-based prompts or rule-based parsing.
- Resulting atomic facts are standalone statements.

### 2. Evidence Retrieval
- For each atomic fact, a dense retriever (e.g., GTR-based retriever) extracts evidence from external sources (usually English Wikipedia).
- Retrieval is entity-centric, targeting passages most likely to contain verifying information.

### 3. Atomic Fact Validation
- Each atomic fact is evaluated against retrieved evidence to determine support.
- Validation can be:
  - <strong>Human Experts:</strong>Fact-checkers label each atomic fact as “Supported,” “Not-supported,” or “Irrelevant.”
  - <strong>Automated Models:</strong>LLMs or masked language models compute support likelihood, classifying with thresholds (e.g., 0.3).

### 4. Score Computation
- FActScore = (Number of Supported Facts / Total Number of Atomic Facts) × 100%.

<strong>Implementation:</strong>Available as an open-source package ([pip install factscore](https://pypi.org/project/factscore/)), supporting human-in-the-loop and fully automated deployments.

## 3. Human and Automated Evaluation Protocols

### 3.1 Human Annotation
- Used as the gold standard for calibration.
- Professional annotators label atomic facts after reviewing retrieved evidence.
- High inter-annotator agreement: 96% (InstructGPT), 90% (ChatGPT), 88% (PerplexityAI) on biography tasks ([Min et al., 2023](https://arxiv.org/abs/2305.14251), [Emergent Mind](https://www.emergentmind.com/topics/factscore)).

### 3.2 Automated Estimation
- Automated pipeline uses retrieval-augmented LLMs for both decomposition and verification.
- Scalable to thousands of outputs; error rate relative to human annotation <2%.
- Metrics: micro-level F1, precision, and recall:
  - <strong>Precision</strong>= |Predicted Unsupported ∩ Gold Unsupported| / |Predicted Unsupported|
  - <strong>Recall</strong>= |Predicted Unsupported ∩ Gold Unsupported| / |Gold Unsupported|
  - <strong>F1 (micro)</strong>= 2·P·R/(P+R)

### 3.3 Correlation and Consistency
- Strong Pearson correlation (r > 0.99) between open-source and proprietary implementations ([Emergent Mind](https://www.emergentmind.com/papers/2507.05965)).
- Enables reproducible, cross-benchmark comparison.

## 4. Multilingual Extensions and Knowledge Source Limitations

### 4.1 Multilingual Factuality Assessment
- Standard pipeline is English-centric.
- For non-English outputs:
  - Text is translated into English for atomic fact extraction and verification ([Multi-FAct](https://www.emergentmind.com/papers/2402.18045)).
  - Controls for inconsistent Wikipedia coverage across languages.
  - Used for cross-lingual LLM benchmarking ([Multilingual Hallucination Gaps](https://www.emergentmind.com/papers/2410.18270)).

### 4.2 Knowledge Source Constraints
- <strong>Coverage Gaps:</strong>Limited Wikipedia content for low-resource languages or niche domains can bias FActScore ([An Analysis of Multilingual FActScore](https://www.emergentmind.com/papers/2406.19415)).
- <strong>Mitigation Strategies:</strong>- Retrieve more passages per claim.
  - Augment with Internet-wide sources (e.g., Google API).
  - LLM-augmented knowledge (prompt GPT-4 for clarifications).
- <strong>Residual Limitation:</strong>Factuality is still bounded by the coverage and quality of the chosen reference corpus.

## 5. Robustness, Decomposition Quality, and Manipulation

### 5.1 Sensitivity to Decomposition
- FActScore’s reliability depends on the atomic fact decomposition method ([A Closer Look at Claim Decomposition](https://arxiv.org/html/2403.11903v1)).
- Alternative decomposition strategies (semantic parsing, prompt engineering, Russellian/Neo-Davidsonian frameworks) yield variable fact sets.
- <strong>DecompScore:</strong>Measures atomicity and coverage of decomposition; high DecompScore indicates better decomposition quality.

### 5.2 Vulnerabilities and Adversarial Manipulation
- Repetition or trivial/tautological facts can artificially inflate FActScore.
- <strong>MontageLie Benchmark:</strong>Demonstrates that reordering or montaging true statements into misleading narratives defeats both fine- and coarse-grained evaluators; AUC-ROC values fall below 65% ([Long-Form Information Alignment Evaluation Beyond Atomic Facts](https://arxiv.org/html/2505.15792v1)).
  - Example: All statements are true individually, but their order implies a false or misleading narrative, undetected by atomic-fact metrics.

### 5.3 Mitigation and Filtering
- Plug-and-play modules (e.g., <strong>Core</strong>) apply subclaim selection and informativeness weighting to suppress repetition and reward unique, informative facts ([Core: Robust Factual Precision](https://www.emergentmind.com/papers/2407.03572)).

## 6. Comparative Model Performance and Applications

### 6.1 Benchmarking Results
- <strong>Commercial Models:</strong>GPT-4 and ChatGPT outperform public LLMs (e.g., Alpaca, Vicuna) on FActScore (ChatGPT ≈ 58%; human-written ≈ 88%) ([Min et al., 2023](https://arxiv.org/abs/2305.14251)).
- <strong>Model Scaling:</strong>Larger models within a family achieve higher FActScore (e.g., Alpaca 65B > 13B > 7B).
- <strong>Public Models:</strong>Alpaca/Vicuna (≈40%) outperform MPTChat (30%) and StableLM (17%) among 7B LLMs.

### 6.2 Impact of Training and Alignment
- Modular hallucination detection/editing (e.g., PFME) increases FActScore by up to 16.2 points ([PFME: Fine-grained Hallucination Detection](https://www.emergentmind.com/papers/2407.00488)).
- Fine-tuning frameworks (Mask-DPO) leveraging sentence-level factuality masks boost factuality from 49.19% to 77.53% ([Mask-DPO: Factuality Alignment](https://www.emergentmind.com/papers/2503.02846)).
- Critique-based evaluation (FenCE) yields 14–16% increases over baselines ([Improving Model Factuality with Fine-grained Critique-based Evaluator](https://www.emergentmind.com/papers/2410.18359)).

### 6.3 Open-Source Implementations
- <strong>OpenFActScore:</strong>Supports any Hugging Face–compatible model, matches original FActScore benchmarks with similar BERTScore-F1 and error rates ([OpenFActScore](https://www.emergentmind.com/papers/2507.05965)).

### 6.4 Example Use Cases
- <strong>Model Benchmarking:</strong>Ranking LLMs by factual quality in biography or summarization ([TruthTorchLM](https://www.emergentmind.com/papers/2507.08203)).
- <strong>Fine-grained Alignment:</strong>Summarization, reasoning-intensive outputs ([Long-Form Information Alignment](https://www.emergentmind.com/papers/2505.15792)).
- <strong>Hallucination Detection:</strong>Monitoring unsupported content in multilingual or domain-specific deployments.
- <strong>Automated Fact-Checking:</strong>Used in scientific communication, climate reporting, adversarial narrative detection ([CLAImate](https://www.emergentmind.com/papers/2507.11677)).

## 7. Limitations and Open Challenges

- <strong>Compositional Factuality:</strong>FActScore does not detect manipulations involving reordering, montage, or selective omission of true statements (MontageLie benchmark).
- <strong>Reference Coverage:</strong>Limited by the breadth/depth of external knowledge sources.
- <strong>Decomposition Reliability:</strong>Fact extraction quality varies by domain and language; ongoing work aims to improve atomicity and coverage ([A Closer Look at Claim Decomposition](https://arxiv.org/html/2403.11903v1)).
- <strong>Gaming the Metric:</strong>Repetitive or trivial fact generation can inflate scores without improving true factuality.
- <strong>Scalability to Multimodal/Multilingual Tasks:</strong>Extending beyond English Wikipedia and text-only domains introduces retrieval and verification challenges.

## 8. Recent Advances and Future Directions

<strong>Emergent Trends:</strong>- <strong>Joint Factuality and Event-Ordering Metrics:</strong>DOVESCORE addresses both factual support and event-order consistency for improved robustness ([Long-Form Information Alignment Evaluation Beyond Atomic Facts](https://arxiv.org/html/2505.15792v1)).
- <strong>Modular Filtering and Informativeness Weighting:</strong>Core-type modules reward unique and informative claims ([Core: Robust Factual Precision](https://www.emergentmind.com/papers/2407.03572)).
- <strong>RL-based Online Alignment:</strong>Incorporates fact, detail, and answer relevance into RL reward signals for LLM alignment.
- <strong>Open-Source Pipelines:</strong>Tools like OpenFActScore democratize high-fidelity factuality evaluation ([OpenFActScore](https://www.emergentmind.com/papers/2507.05965)).

<strong>Future Research Directions:</strong>- Expansion to low-resource languages and multimodal content.
- Cross-domain factuality assessment (medical, legal, scientific).
- Real-time factuality monitoring in production LLMs.
- Enhanced robustness to adversarial attacks and compositional manipulations.

## 9. Practical Implementation and Access

- <strong>Availability:</strong>Open-source ([pip install factscore](https://pypi.org/project/factscore/)), research repositories ([GitHub](https://github.com/shmsw25/FActScore), [OpenFActScore](https://www.emergentmind.com/papers/2507.05965)).
- <strong>Integration:</strong>Supports human-in-the-loop annotation, fully automated evaluation, and third-party LLMs.
- <strong>Customization:</strong>Extensible to alternative knowledge sources, more languages, and domain-specific fact-checking.

## 10. Example Applications and Use Cases

### 10.1 Model Benchmarking

<strong>Scenario:</strong>An AI lab compares several LLMs’ factual precision on biography generation.
- Each model generates a biography.
- Outputs are processed via FActScore.
- Results: GPT-4/ChatGPT ≈58%, Alpaca/Vicuna ≈40%, human-written ≈88%.

### 10.2 Factual Alignment in Summarization

- Summaries are decomposed into atomic facts.
- Facts are checked against the source and Wikipedia.
- FActScore identifies unsupported claims for targeted refinement.

### 10.3 Multilingual Fact-Checking

- Responses in Spanish, Chinese, Arabic are translated to English.
- Fact extraction and validation performed using English Wikipedia.
- FActScore highlights gaps due to cross-lingual knowledge.

### 10.4 Hallucination Monitoring in Scientific Communication

- Climate science outreach tool generates explanations.
- Outputs are fact-checked against scientific literature and Wikipedia.
- FActScore quantifies hallucination rates, guiding retraining and prompt engineering.

## 11. Summary Table: Key Properties

| Property                               | Details                                                                                         |
|-----------------------------------------|-------------------------------------------------------------------------------------------------|
| <strong>Granularity</strong>| Atomic fact level (fine-grained)                                                                |
| <strong>Reference Source</strong>| Wikipedia (default), extensible to other corpora                                                |
| <strong>Evaluator</strong>| Human or automated (LLM, masked LM)                                                             |
| <strong>Supported Languages</strong>| English (default); multilingual via translation                                                 |
| <strong>Benchmark Coverage</strong>| Long-form generation (biographies, summaries, QA)                                               |
| <strong>Error Rate (Automated vs. Human)</strong>| <2%                                                                                             |
| <strong>Open-Source Availability</strong>| Yes ([pip install factscore](https://pypi.org/project/factscore/), [OpenFActScore](https://www.emergentmind.com/papers/2507.05965))   |
| <strong>Known Limitations</strong>| Compositionality, knowledge source coverage, decomposition variability, adversarial manipulation |

## 12. Glossary of Technical Terms

- <strong>Atomic Fact:</strong>Minimal, context-independent factual statement from generated text ([A Closer Look at Claim Decomposition](https://arxiv.org/html/2403.11903v1)).
- <strong>Retriever Model:</strong>Model that fetches relevant passages from a knowledge source for fact verification.
- <strong>Masked Language Modeling (MLM):</strong>Language modeling approach where tokens are masked and predicted, used in automated fact validation.
- <strong>Factual Precision:</strong>Proportion of supported atomic facts to total atomic facts in generated output.
- <strong>Hallucination:</strong>Unsupported or fabricated content generated by an AI model.
- <strong>Decomposition:</strong>Splitting text into atomic facts for granular evaluation.
- <strong>DecompScore:</strong>Metric for evaluating the quality and atomicity of fact decomposition.
- <strong>Core Module:</strong>Filtering mechanism to suppress repetitive or trivial subclaims during FActScore computation.
- <strong>MontageLie Benchmark:</strong>Adversarial benchmark where truthful statements are reordered to create misleading narratives ([Long-Form Information Alignment Evaluation Beyond Atomic Facts](https://arxiv.org/html/2505.15792v1)).
- <strong>DOVESCORE:</strong>Joint factuality and event-ordering metric to address compositional factuality ([Long-Form Information Alignment Evaluation Beyond Atomic Facts](https://arxiv.org/html/2505.15792v1)).

## References

1. Min, S., Krishna, K., Lyu, X., Lewis, M., Yih, W.-t., Koh, P. W., Iyyer, M., Zettlemoyer, L., & Hajishirzi, H. (2023). [FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation](https://arxiv.org/abs/2305.14251). EMNLP 2023.
2. [OpenFActScore: Open-Source Atomic Evaluation of Factuality in Text Generation](https://www.emergentmind.com/papers/2507.05965), 2025.
3. [Multi-FAct: Assessing Factuality of Multilingual LLMs using FActScore](https://www.emergentmind.com/papers/2402.18045), 2024.
4. [Multilingual Hallucination Gaps in Large Language Models](https://www.emergentmind.com/papers/2410.18270), 2024.
5. [An Analysis of Multilingual FActScore](https://www.emergentmind.com/papers/2406.19415), 2024.
6. [A Closer Look at Claim Decomposition](https://arxiv.org/html/2403.11903v1), 2024.
7. [Core: Robust Factual Precision with Informative Sub-Claim Identification](https://www.emergentmind.com/papers/2407.03572), 2024.
8. [PFME: A Modular Approach for Fine-grained Hallucination Detection and Editing of Large Language Models](https://www.emergentmind.com/papers/2407.00488), 2024.
9. [Mask-DPO: Generalizable Fine-grained Factuality Alignment of LLMs](https://www.emergentmind.com/papers/2503.02846), 2025.
10. [Improving Model Factuality with Fine-grained Critique-based Evaluator](https://www.emergentmind.com/papers/2410.18359), 2024.
11. [Learning to Reason for Factuality](https://www.emergentmind.com/papers/2508.05618), 2025.
12. [CLAImate: AI-Enabled Climate Change Communication through Personalized and Localized Narrative Visualizations](https://www.emergentmind.com/papers/2507.11677), 2025.
13. [Long-Form Information Alignment Evaluation Beyond Atomic Facts](https://arxiv.org/html/2505.15792v1), 2025.
14. [TruthTorchLM: A Comprehensive Library for Predicting Truthfulness in LLM Outputs](https://www.emergentmind.com/papers/2507.08203), 2025.
- [Emergent Mind: FActScore Topic Overview](https://www.emergentmind.com

