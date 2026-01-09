---
title: MHaluBench
lastmod: 2025-12-18
date: 2025-12-18
translationKey: mhalubench
description: "A benchmark tool that evaluates whether image-and-text AI systems generate accurate information by breaking down responses into individual claims and checking each one for factual errors."
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

## What is MHaluBench?

MHaluBench is a comprehensive benchmark for evaluating and detecting hallucinations in Multimodal Large Language Models (MLLMs) at fine-grained, claim-level granularity. It provides standardized evaluation across both Image-to-Text (I2T) and Text-to-Image (T2I) tasks, enabling precise assessment of model reliability and accuracy in multimodal contexts.

Unlike previous benchmarks that operate at response or sentence level, MHaluBench decomposes model outputs into atomic factual claims, annotates each claim for hallucination type and category, and provides ground truth for meta-evaluation of detection systems. This granular approach enables targeted diagnosis of specific failure modes in multimodal AI systems.

The benchmark addresses critical challenges in deploying MLLMs for production use cases where accuracy and truthfulness are paramount—including medical imaging, autonomous systems, content moderation, and assistive technologies. By providing standardized evaluation methodology and high-quality annotations, MHaluBench accelerates research and development of more reliable multimodal AI systems.

## Understanding Hallucinations in Multimodal AI

Hallucination in MLLMs occurs when generated output content is syntactically plausible but semantically unfaithful to provided inputs or contradicts established world knowledge. This phenomenon manifests across visual, textual, and cross-modal outputs, presenting unique challenges compared to text-only language models.

### Hallucination Taxonomy

<strong>Faithfulness Hallucinations:</strong>Output contradicts direct input context. Example: Describing objects or attributes not present in input image, such as claiming "a dog is running" when only a cat appears in the image.

<strong>Factuality Hallucinations:</strong>Output conflicts with established external knowledge despite plausible appearance. Example: Asserting "Eiffel Tower is located in London" when generating captions or answering visual questions.

<strong>Modality-Conflicting Hallucinations:</strong>Direct contradictions between modalities in either input or output. Example: Text description states "red car" while associated image shows blue car, or T2I model generates image contradicting input text prompt.

<strong>Fact-Conflicting Hallucinations:</strong>Output appears reasonable but violates world knowledge or common sense. Example: Claiming person in historical photo is using smartphone, or dating building construction to impossible time period.

### Granularity Levels

<strong>Object-Level:</strong>Incorrect identification, omission, or fabrication of entities. Example: Detecting person where none exists, missing primary subject, or misidentifying object category.

<strong>Attribute-Level:</strong>Incorrect properties assigned to correctly identified objects. Example: Wrong colors, incorrect sizes, misattributed materials, or inaccurate spatial relationships.

<strong>Scene-Level:</strong>Misrepresentation of overall context, relationships, or events. Example: Describing indoor scene as outdoor, misidentifying activity or event, incorrect setting characterization.

<strong>Scene-Text:</strong>Errors in recognizing or generating text within images. Example: Misreading signage, fabricating text content, or generating incorrect written language in T2I outputs.

## Benchmark Structure

### Dataset Composition

MHaluBench comprises 620 carefully curated instances spanning three task categories, each annotated at both segment and claim levels for comprehensive evaluation.

<strong>Image Captioning (IC) - 200 samples:</strong>- Source: MS-COCO 2014 Validation dataset
- Outputs generated from: mPLUG, LLaVA, MiniGPT-4
- Annotation focus: Faithfulness to visual content, object/attribute accuracy

<strong>Visual Question Answering (VQA) - 200 samples:</strong>- Source: TextVQA test set
- Tasks: Scene text recognition, visual reasoning, attribute identification
- Annotation focus: Answer accuracy, scene-text hallucinations, reasoning correctness

<strong>Text-to-Image Generation (T2I) - 220 samples:</strong>- Source prompts: DrawBench, T2I-CompBench
- Models evaluated: DALL-E 2, DALL-E 3, Stable Diffusion variants
- Annotation focus: Prompt adherence, attribute fidelity, composition accuracy

Total coverage: 620 instances with dual-level annotation (segment and claim), providing 2,847 annotated claims across all categories.

### Annotation Methodology

<strong>Claim Extraction:</strong>- Automated extraction using GPT-4V and Gemini
- Manual verification and refinement by annotators
- Atomic factual assertions isolated from complex sentences
- Maintained semantic completeness while ensuring independence

<strong>Labeling Process:</strong>- Three graduate-level annotators independently label each claim
- Binary classification: hallucinatory vs. non-hallucinatory
- Category assignment: Object, Attribute, Scene-Text, Fact
- Disagreements resolved by majority vote
- Inter-annotator agreement: Fleiss's Kappa κ = 0.822 (strong agreement)

<strong>Propagation Rules:</strong>- Segment marked hallucinatory if any contained claim is hallucinatory
- Response marked hallucinatory if any segment is hallucinatory
- Preserves fine-grained analysis while enabling coarse-grained evaluation

### Data Schema

Each benchmark entry includes:

<strong>Identifiers:</strong>Unique ID, task type designation, source dataset reference

<strong>Inputs:</strong>Original image (I2T tasks) or text prompt (T2I tasks)

<strong>Outputs:</strong>Generated text (I2T) or synthesized image (T2I)

<strong>Segments:</strong>Logical text divisions (sentences or clauses) with hallucination labels

<strong>Claims:</strong>Atomic factual assertions with detailed annotations including claim text, category classification, hallucination status, supporting rationale

<strong>Metadata:</strong>Model information, generation parameters, annotation timestamps

## UNIHD Detection Framework

Unified Hallucination Detection (UNIHD) represents state-of-the-art approach for automated hallucination detection, providing end-to-end pipeline from claim extraction to verification.

### Four-Stage Pipeline

<strong>Stage 1 - Essential Claim Extraction:</strong>- Decompose complex outputs into atomic factual claims
- Ensure claims are independently verifiable
- Maintain semantic relationships for context-dependent claims
- Filter non-factual content (opinions, questions, imperatives)

<strong>Stage 2 - Autonomous Tool Selection:</strong>- Analyze each claim for verification requirements
- Formulate targeted queries for validation
- Select appropriate verification tools from toolkit:
  - Object detectors (Grounding DINO, YOLO)
  - Attribute classifiers (color, size, material)
  - OCR systems (scene text recognition)
  - Knowledge bases (factual verification)

<strong>Stage 3 - Parallel Tool Execution:</strong>- Deploy selected tools concurrently for efficiency
- Retrieve verification evidence from multiple sources
- Handle tool failures and uncertain results gracefully
- Aggregate results maintaining provenance

<strong>Stage 4 - Hallucination Verification:</strong>- Compare claims against verification evidence
- Generate human-readable rationales for decisions
- Assign confidence scores to detections
- Produce final hallucinatory/non-hallucinatory labels

### Detection Approaches

<strong>Black-Box Methods:</strong>Evaluate models using only input-output pairs without internal access. Examples: FaithScore, GAVIE, HaELM. Advantages: Model-agnostic, deployable without architecture knowledge. Limitations: Cannot leverage internal states, limited explainability.

<strong>White-Box Methods:</strong>Exploit model internals (attention weights, hidden states, token probabilities). Examples: DHCP, OPERA, ContextualLens. Advantages: Direct access to uncertainty signals, detailed interpretability. Limitations: Model-specific implementation, requires architectural knowledge.

<strong>Tool-Augmented Methods:</strong>Leverage external verification tools for evidence-based detection. Examples: UNIHD, FactChecker, CutPaste & Find. Advantages: Grounded in external evidence, extensible with new tools. Limitations: Dependent on tool accuracy, potential scalability challenges.

<strong>Hybrid Approaches:</strong>Combine multiple detection paradigms for robust performance across scenarios and failure modes.

## Benchmark Positioning

### Comparison with Related Benchmarks

| Benchmark | Modalities | Tasks | Granularity | Categories | Annotation | Unique Features |
|-----------|-----------|-------|-------------|------------|------------|----------------|
| <strong>HaluEval</strong>| Text | QA, Summarization | Response | Factuality | Response-level | Large-scale text focus |
| <strong>POPE</strong>| Image+Text | Captioning | Response | Faithfulness | Response-level | Visual object presence |
| <strong>HalluCode</strong>| Code | Code generation | Token | Mapping, Naming, Logic | Token-level | Execution-based validation |
| <strong>CodeHalu</strong>| Code | Code generation | Span | Resource, Logic | Span-level | Comprehensive code analysis |
| <strong>Collu-Bench</strong>| Code | Gen & Repair | Token | Multiple | Token-level | Multi-LLM comparison |
| <strong>MHaluBench</strong>| Image+Text | I2T, T2I | Claim | Object, Attribute, Scene, Fact | Claim+Segment | Unified multimodal coverage |

<strong>Distinctive Advantages:</strong>- Only benchmark spanning both I2T and T2I tasks comprehensively
- Finest granularity with claim-level annotation enabling targeted analysis
- Explicit taxonomy distinguishing modality vs. fact conflicts
- Designed specifically for meta-evaluation of detection systems
- Balanced coverage across hallucination categories and task types

## Practical Applications

### Model Development

<strong>Targeted Improvement:</strong>Identify specific failure modes (e.g., attribute hallucinations in medical imaging) enabling focused model refinement.

<strong>Ablation Studies:</strong>Evaluate impact of architectural changes or training procedures on specific hallucination categories.

<strong>Comparison Analysis:</strong>Benchmark multiple model variants or architectures on standardized hallucination metrics.

### Detection System Evaluation

<strong>Meta-Evaluation:</strong>Assess detection systems against ground truth, measuring precision, recall, F1 across categories.

<strong>Robustness Testing:</strong>Evaluate detector performance across diverse scenarios, domains, and hallucination types.

<strong>Tool Development:</strong>Guide development of specialized detection tools for specific hallucination categories.

### Production Deployment

<strong>Quality Assurance:</strong>Establish thresholds and monitoring for acceptable hallucination rates in production systems.

<strong>User Trust:</strong>Provide evidence-based reliability metrics informing deployment decisions and user expectations.

<strong>Risk Mitigation:</strong>Identify high-risk scenarios requiring human oversight or additional verification.

## Illustrative Examples

### Image-to-Text Hallucination

<strong>Input:</strong>Soccer match photograph showing athlete in blue uniform on right side

<strong>Model Output:</strong>"The athlete on the right side, wearing the red uniform, belongs to Club América."

<strong>Extracted Claims:</strong>1. "Athlete on right wears red uniform" - HALLUCINATORY (Attribute-level, Modality-conflicting: Image shows blue uniform)
2. "Athlete belongs to Club América" - REQUIRES FACT-CHECK (Fact-level: Needs external verification of team membership)

<strong>Detection Process:</strong>Object detector confirms athlete presence and location, attribute classifier identifies blue uniform contradicting claim 1, knowledge base query verifies team information for claim 2.

### Text-to-Image Hallucination

<strong>Input Prompt:</strong>"A yellow school bus parked in front of the Eiffel Tower in Paris"

<strong>Generated Image:</strong>Red bus in front of unidentified landmark

<strong>Extracted Claims:</strong>1. "Image contains yellow school bus" - HALLUCINATORY (Object/Attribute-level, Modality-conflicting: Image shows red bus)
2. "Bus positioned in front of Eiffel Tower" - HALLUCINATORY (Fact-level, Modality-conflicting: Landmark not identifiable as Eiffel Tower)

<strong>Detection Process:</strong>Object detection identifies bus but wrong color, landmark recognition fails to confirm Eiffel Tower, attribute verification contradicts yellow color claim.

## Limitations and Future Directions

<strong>Scale Constraints:</strong>Current 620 instances smaller than large-scale text benchmarks. Expansion planned to thousands of instances across more domains and modalities.

<strong>Annotation Costs:</strong>Human annotation resource-intensive limiting rapid scaling. Future work explores semi-automatic annotation with human verification.

<strong>Modality Coverage:</strong>Currently limited to image-text pairs. Extension to video, audio, 3D, and sensor data modalities under consideration.

<strong>Tool Dependency:</strong>Detection performance bounded by external tool accuracy. Improving tool reliability and developing specialized verification systems ongoing.

<strong>Dynamic Evaluation:</strong>Static benchmark may not reflect real-world deployment challenges. Development of dynamic evaluation protocols for live systems needed.

<strong>Cultural and Linguistic Diversity:</strong>Current focus on English and common image domains. Expansion to multilingual settings and diverse cultural contexts planned.

<strong>Mitigation Integration:</strong>Benchmark focuses on detection; integration with correction and mitigation systems represents future direction.

## Implementation Resources

<strong>Dataset Access:</strong>Available on HuggingFace Datasets platform with comprehensive documentation, evaluation scripts, and baseline results.

<strong>Evaluation Tools:</strong>Python toolkit for computing detection metrics, analyzing error patterns, and generating detailed reports.

<strong>Baseline Implementations:</strong>Reference implementations of UNIHD and other detection approaches for reproduction and extension.

<strong>Community Contributions:</strong>Open invitation for submission of detection systems to public leaderboard, expanding benchmark coverage.

## References


1. Shi, W., et al. (2024). Unified Hallucination Detection. ACL 2024 Proceedings.

2. Anonymous. (2024). Multimodal Hallucination Survey. arXiv.

3. OpenKG. (n.d.). MHaluBench Dataset. HuggingFace.

4. COCO Consortium. (n.d.). MS-COCO Dataset. COCO Dataset.

5. TextVQA Team. (n.d.). TextVQA Dataset. TextVQA.

6. Anonymous. (2022). DrawBench Benchmark. arXiv.

7. Anonymous. (2023). T2I-CompBench. arXiv.

8. Anonymous. (2023). HaluEval Paper. arXiv.

9. Anonymous. (2024). HalluCode Benchmark. arXiv.

10. Anonymous. (2024). CodeHalu Benchmark. arXiv.

11. Anonymous. (2024). Collu-Bench. arXiv.

12. mPLUG. (n.d.). mPLUG Framework. URL: https://github.com/X-PLUG/mPLUG

13. LLaVA. (n.d.). LLaVA Model. URL: https://llava-vl.github.io/

14. MiniGPT-4. (n.d.). MiniGPT-4. URL: https://minigpt-4.github.io/

15. OpenAI. (n.d.). DALL-E 2. URL: https://openai.com/research/dall-e

16. OpenAI. (n.d.). DALL-E 3. URL: https://openai.com/blog/dall-e-3

17. IDEA Research. (n.d.). Grounding DINO. URL: https://github.com/IDEA-Research/GroundingDINO

18. OpenAI. (n.d.). GPT-4V Vision. URL: https://platform.openai.com/docs/guides/vision

19. Google DeepMind. (n.d.). Gemini Multimodal. URL: https://deepmind.google/technologies/gemini/

20. Emergent Mind. (n.d.). MMHal-Bench. URL: https://www.emergentmind.com/topics/mmhal-bench
