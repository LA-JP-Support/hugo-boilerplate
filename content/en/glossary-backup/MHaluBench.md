---
title: MHaluBench
date: 2025-12-17
translationKey: mhalubench
description: MHaluBench is a meta-evaluation and annotation benchmark for fine-grained,
  claim-level hallucination detection in multimodal large language models (MLLMs)
  across I2T and T2I tasks.
keywords:
- MHaluBench
- hallucination detection
- multimodal LLMs
- AI benchmark
- I2T T2I
category: Multimodal AI
type: glossary
draft: false
---

## Glossary and Conceptual Expansion

### Hallucination in Multimodal AI

<strong>Definition:</strong>In MLLMs, hallucination is the generation of output content that is syntactically plausible but semantically unfaithful to the provided input(s) or contradicts established world knowledge. This can occur in visual, textual, or cross-modal outputs.
### Taxonomy and Definitions

#### Faithfulness vs. Factuality Hallucinations

- <strong>Faithfulness Hallucination:</strong>Output contradicts the direct input context. Example: Describing an object not present in the input image.  
  [Related: Taxonomy summary, arXiv survey, Section 2.1](https://arxiv.org/html/2507.19024v1)
- <strong>Factuality Hallucination:</strong>Output conflicts with established external knowledge, not the input context. Example: Assigning the wrong name to a famous landmark.

#### Modality-Conflicting vs. Fact-Conflicting Hallucinations

- <strong>Modality-Conflicting:</strong>Direct contradiction between modalities (e.g., visual vs. textual).  
  Example: Text says “red car,” image shows blue car.
- <strong>Fact-Conflicting:</strong>Output is plausible but incorrect by world knowledge.  
  Example: “Eiffel Tower is in London.”

#### Granularity: Object-Level, Attribute-Level, Scene-Level

- <strong>Object-Level:</strong>Incorrect identification or hallucination of entities.  
  Example: Citing a dog when only a cat is present.
- <strong>Attribute-Level:</strong>Incorrect properties assigned (color, shape, etc.).
- <strong>Scene-Level:</strong>Misrepresentation of relationships or events.
- <strong>Scene-Text:</strong>Errors in text recognition or generation within images.

#### Task Modalities

- <strong>Image-to-Text (I2T):</strong>Captioning, VQA, visual reasoning. [MS-COCO](https://cocodataset.org/#home), [TextVQA](https://textvqa.org/)
- <strong>Text-to-Image (T2I):</strong>DALL-E, Stable Diffusion, etc. [DrawBench](https://arxiv.org/abs/2206.01714), [T2I-CompBench](https://arxiv.org/abs/2307.10021)

#### Annotation Levels

- <strong>Segment-Level:</strong>Sentence or logical text segment.
- <strong>Claim-Level:</strong>Atomic factual assertion within a segment.

### Benchmark Construction

#### Dataset Composition

MHaluBench covers:
- <strong>Image Captioning (IC):</strong>200 samples from [MS-COCO 2014 Validation](https://cocodataset.org/#download), generated from diverse MLLMs.
- <strong>Visual Question Answering (VQA):</strong>200 samples from [TextVQA test set](https://textvqa.org/download.html).
- <strong>Text-to-Image Generation:</strong>220 samples based on [DrawBench](https://arxiv.org/abs/2206.01714) and [T2I-CompBench](https://arxiv.org/abs/2307.10021).

<strong>Total:</strong>620 instances, each annotated at both segment and claim levels.  
*Source: [MHaluBench Dataset Card on HuggingFace](https://huggingface.co/datasets/OpenKG/MHaluBench)*

#### Data Generation and Model Coverage

- I2T outputs: [mPLUG](https://github.com/X-PLUG/mPLUG), [LLaVA](https://llava-vl.github.io/), [MiniGPT-4](https://minigpt-4.github.io/)
- T2I outputs: [DALL-E2](https://openai.com/research/dall-e), [DALL-E3](https://openai.com/blog/dall-e-3), and related diffusion models.

#### Annotation Protocol

- <strong>Claim Extraction:</strong>Automated using advanced LLMs ([GPT-4V](https://platform.openai.com/docs/guides/vision), [Gemini](https://deepmind.google/technologies/gemini/)), then manually verified.
- <strong>Labeling:</strong>- Claims labeled hallucinatory/non-hallucinatory.
  - Segment is hallucinatory if any claim within is hallucinatory.
  - Response is hallucinatory if any segment is hallucinatory.
- <strong>Category Labels:</strong>| Category      | Definition | Example |
  |---------------|------------|---------|
  | Object        | Incorrect/omitted entity | “A dog is running” when only a cat is present |
  | Attribute     | Incorrect property | “The car is red” (but it’s blue) |
  | Scene-Text    | Transcription/factual error in text | “Sign says ‘Open’” (but says ‘Closed’) |
  | Fact          | Contradiction to external knowledge | “Eiffel Tower is in London” |

- <strong>Human Annotation:</strong>Three graduate-level annotators independently label; disagreements resolved by majority vote.  
  Inter-annotator agreement: Fleiss’s Kappa κ = 0.822.  
  *See [MHaluBench paper, Section 4.2, Table 5](https://aclanthology.org/2024.acl-long.178.pdf)*

#### Dataset Schema

Each entry includes:
- Unique ID, task type, input (image/text), output (text/image)
- Segments and claims (with text, category, hallucination label, etc.)

### Methodological Approaches: Detection Frameworks

#### Unified Hallucination Detection (UNIHD)

UNIHD decomposes hallucination detection into four stages:
1. <strong>Essential Claim Extraction:</strong>Identify atomic factual claims ([MHaluBench, Section 3.1](https://aclanthology.org/2024.acl-long.178/)).
2. <strong>Autonomous Tool Selection:</strong>Formulate targeted queries and select validation tools (object, attribute, scene-text, fact).
3. <strong>Parallel Tool Execution:</strong>Deploy detectors/classifiers (e.g., [Grounding DINO](https://github.com/IDEA-Research/GroundingDINO) for objects, OCR for scene-text).
4. <strong>Hallucination Verification:</strong>Aggregate results, generate rationales, and assign final labels.

<strong>Supported Detection Approaches:</strong>| Approach           | Description | Examples |
|--------------------|-------------|----------|
| Black-Box          | Input/output only | [FaithScore](https://arxiv.org/abs/2309.00906), GAVIE, HaELM |
| White-Box          | Uses model internals | DHCP, OPERA, ContextualLens |
| Tool-Augmented     | Uses external tools | UNIHD, FactCheXcker, CutPaste & Find |
| Hybrid             | Combines above | Multi-stage frameworks |

*See [A Survey of Multimodal Hallucination Evaluation and Detection, Table 1](https://arxiv.org/html/2507.19024v1#table.1)*

### Benchmark Comparison and Positioning

| Benchmark      | Modalities   | Tasks              | Granularity         | Categories Covered           | Annotation Level | Unique Features                          |
|----------------|-------------|--------------------|---------------------|------------------------------|------------------|-------------------------------------------|
| HaluEval       | Text only   | QA, Summarization  | Sentence/Response   | Factuality                   | Response         | Large-scale, text-centric                 |
| POPE           | Image/text  | Captioning         | Sentence/Response   | Faithfulness                 | Response         | Visual focus                              |
| HalluCode      | Code        | Code generation    | Code span/token     | Mapping, Naming, Logic       | Token            | Execution-based, code-specific            |
| CodeHalu       | Code        | Code generation    | Code span           | Resource, Logic              | Span             | Execution-based evaluation pipeline       |
| Collu-Bench    | Code        | Code gen & repair  | Token               | Multiple code categories     | Token            | Per-token localization, multi-LLM         |
| MHaluBench     | Image/Text  | Captioning, VQA, T2I| Segment/Claim      | Object, Attribute, Scene, Fact| Claim/Segment    | Unified, fine-grained, cross-modal        |

- <strong>Distinctive aspects of MHaluBench:</strong>- Covers both I2T and T2I tasks.
  - Fine-grained, claim-level annotation scheme.
  - Explicitly distinguishes modality- and fact-conflicting hallucinations.
  - Structured for meta-evaluation of detectors.

<strong>Further reading:</strong>- [OpenKG MHaluBench Dataset on HuggingFace](https://huggingface.co/datasets/OpenKG/MHaluBench)
- [MMHal-Bench: Modality Misalignment Evaluation (Emergent Mind)](https://www.emergentmind.com/topics/mmhal-bench)

### Illustrative Examples

<strong>Image-to-Text (I2T):</strong>- *Input*: Soccer match with a blue-uniformed athlete on the right.
- *Output*: “The athlete on the right side, wearing the red uniform, belongs to Club América.”
- *Extracted Claims*:  
  1. Athlete on right wears red uniform. *(Hallucinatory: Attribute-level, Modality-conflicting)*
  2. Athlete belongs to Club América. *(Fact-level, requires external check)*

<strong>Text-to-Image (T2I):</strong>- *Input*: “A yellow school bus parked in front of the Eiffel Tower in Paris.”
- *Output*: Image showing a red bus in front of an unidentified landmark.
- *Extracted Claims*:  
  1. There is a yellow school bus. *(Hallucinatory: Object/Attribute, Modality-conflicting)*
  2. Bus is in front of Eiffel Tower in Paris. *(Hallucinatory: Fact-level, Modality-conflicting)*

### Use Cases

- <strong>Benchmarking:</strong>Standardized testbed for evaluating hallucination detectors ([UNIHD](https://aclanthology.org/2024.acl-long.178/), black-box, etc.).
- <strong>Model Diagnostics:</strong>Enables granular, claim-level error analysis for targeted improvement.
- <strong>Unified Detection Pipeline Prototyping:</strong>Data structure supports integration/testing of tool-augmented pipelines (object detectors, OCR, fact-checkers).

### Limitations and Future Directions

- <strong>Dataset Size:</strong>Currently 620 instances—smaller than large-scale text benchmarks. Plans for expansion and inclusion of more modalities (audio, video) and domains.
- <strong>Annotation Scalability:</strong>Human annotation is resource-intensive; future iterations may use semi-automatic or consensus-driven approaches.
- <strong>Tool Dependency:</strong>Frameworks like UNIHD depend on external tool accuracy (object detectors, OCR, knowledge bases).
- <strong>Dynamic Evaluation:</strong>Most data is static; open-domain or real-time deployment evaluation remains an open challenge.
- <strong>From Detection to Mitigation:</strong>MHaluBench is for detection/diagnostics; future directions include integrating with correction/mitigation systems.

### References & Further Links

1. [Unified Hallucination Detection for Multimodal Large Language Models (ACL 2024)](https://aclanthology.org/2024.acl-long.178/)
2. [A Survey of Multimodal Hallucination Evaluation and Detection (arXiv 2024)](https://arxiv.org/abs/2507.19024)
3. [MHaluBench HuggingFace Dataset Card](https://huggingface.co/datasets/OpenKG/MHaluBench)
4. [HaluEval Paper](https://arxiv.org/abs/2306.05645)
5. [HalluCode Benchmark](https://arxiv.org/abs/2402.09901)
6. [CodeHalu Benchmark](https://arxiv.org/abs/2402.09901)
7. [Collu-Bench Benchmark](https://arxiv.org/abs/2405.14451)
8. [mPLUG](https://github.com/X-PLUG/mPLUG)
9. [LLaVA](https://llava-vl.github.io/)
10. [MiniGPT-4](https://minigpt-4.github.io/)
11. [DALL-E2](https://openai.com/research/dall-e)
12. [DALL-E3](https://openai.com/blog/dall-e-3)
13. [DrawBench Dataset](https://arxiv.org/abs/2206.01714)
14. [T2I-CompBench Dataset](https://arxiv.org/abs/2307.10021)
15. [Grounding DINO Object Detector](https://github.com/IDEA-Research/GroundingDINO)
16. [GPT-4V (Vision)](https://platform.openai.com/docs/guides/vision)
17. [Gemini Multimodal Model](https://deepmind.google/technologies/gemini/)
18. [MMHal-Bench (Emergent Mind)](https://www.emergentmind.com/topics/mmhal-bench)

For a complete deep dive, consult the [MHaluBench dataset](https://huggingface.co/datasets/OpenKG/MHaluBench), the [ACL 2024 paper](https://aclanthology.org/2024.acl-long.178/), and the [arXiv survey](https://arxiv.org/abs/2507.19024). These resources provide foundational theory, taxonomy, practical annotation protocols, benchmark construction, and links to all referenced source datasets and models.

