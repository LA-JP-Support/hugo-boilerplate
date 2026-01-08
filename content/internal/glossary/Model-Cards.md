+++
title = "Model Cards"
date = 2025-11-25
lastmod = 2025-12-05
translationKey = "model-cards"
description = "Model Cards are standardized documents for ML models, detailing architecture, intended uses, performance, limitations, training data, and ethical considerations for transparency and accountability."
keywords = ["Model Cards", "Machine Learning", "AI Ethics", "Transparency", "Responsible AI"]
category = "AI Ethics & Safety Mechanisms"
type = "glossary"
draft = false
url = "/internal/glossary/Model-Cards/"

+++
## Overview: Defining Model Cards

A model card is a standardized, structured document accompanying a machine learning (ML) model. It summarizes the model’s architecture, intended uses, performance metrics (including fairness and subgroup analyses), limitations, training data sources, and ethical considerations. Model cards are inspired by the concept of nutrition labels for food, aiming for clear and accessible communication of a model’s properties and risks.

- [Google Model Cards Overview](https://modelcards.withgoogle.com/)
- [Hugging Face Model Cards Documentation](https://huggingface.co/docs/hub/en/model-cards)
- [Original Model Cards Paper (arXiv:1810.03993)](https://arxiv.org/abs/1810.03993)

## Background and Context

### Origins

Model cards were first proposed by researchers at Google in 2018 to address the lack of standardized model documentation and the opacity of machine learning systems. The foundational paper by Mitchell et al., ["Model Cards for Model Reporting"](https://arxiv.org/abs/1810.03993), highlights the need for transparent communication of model characteristics and social impacts, especially in sensitive domains such as healthcare, finance, and law enforcement.

### Motivation

- **Transparency:**Clear articulation of what a model does, how it was trained, and its known limitations.
- **Accountability:**Enabling stakeholders to understand and audit model behavior, which is increasingly important for regulatory compliance and public trust.
- **Fairness:**Encouraging explicit reporting and analysis of bias and disparate impact.

### Adoption

Model cards have become a best practice in the AI community:
- **Hugging Face:**Thousands of models in the [Model Hub](https://huggingface.co/models) include model cards.
- **Meta, OpenAI, Google:**Major AI labs publish model cards for flagship models ([Meta Llama](https://github.com/facebookresearch/llama/blob/main/MODEL_CARD.md), [OpenAI GPT-3](https://github.com/openai/gpt-3/blob/master/model-card.md), [Google Face Detection](https://modelcards.withgoogle.com/face-detection)).
- **IBM:**[AI FactSheets](https://aifs360.mybluemix.net/introduction) extend the model card concept for enterprise governance.

## What is a Model Card?

A model card is a concise but comprehensive document that describes the key technical and ethical attributes of a machine learning model. It typically includes:

- Intended use and users
- Model architecture and training data
- Performance metrics, including disaggregated results
- Limitations and potential sources of bias
- Ethical and societal implications
- Licensing and contact details

**Analogy:**A model card is to an AI model what a nutrition label is to food: a clear, accessible summary that enables informed, responsible use.
## Why Model Cards Matter: Benefits

### 1. Transparency and Accountability
Model cards disclose the data, design, and evaluation processes of a model, making it possible for stakeholders to scrutinize and trust the system ([Google Model Cards](https://modelcards.withgoogle.com/)).

### 2. Informed Model Selection
Practitioners can compare models with similar tasks, understanding trade-offs in accuracy, fairness, and limitations ([Hugging Face Model Card Guidebook](https://huggingface.co/docs/hub/en/model-card-guidebook)).

### 3. Bias and Fairness Mitigation
Model cards require quantitative and qualitative analyses of model performance across demographic groups, helping identify and reduce harm ([arXiv:1810.03993](https://arxiv.org/abs/1810.03993)).

### 4. Governance and Compliance
Model cards provide artifacts necessary for regulatory reporting, risk management, and responsible AI audits ([IBM FactSheets](https://aifs360.mybluemix.net/introduction)).

### 5. Continuous Improvement & Collaboration
Documenting limitations and results supports iterative improvement and knowledge sharing within and across organizations.

### 6. Stakeholder Communication
Non-technical and technical audiences gain a shared understanding, which is crucial for responsible deployment and public trust.

## Core Sections of a Model Card

While templates vary, a comprehensive model card usually includes the following sections:

### 1. Model Details

- Model name, version, date
- Responsible organization and authors
- Licensing and contact info
- High-level description (model type, purpose)

### 2. Intended Use

- Primary use cases (e.g., [sentiment analysis](/en/glossary/sentiment-analysis/), medical diagnosis)
- Intended and out-of-scope users
- Known inappropriate or prohibited uses

### 3. Model Architecture

- Technical details (type, layers, activation functions)
- Pre-trained base model or unique architecture
- Link to code or repository

### 4. Training Data and Methodology

- Datasets used (source, size, selection criteria)
- Preprocessing and augmentation steps
- Data distribution and class balance
- Data collection period and privacy considerations

### 5. Performance Metrics

- Key metrics (accuracy, precision, recall, F1, AUC, etc.)
- Disaggregated results (by age, gender, language, etc.)
- Evaluation benchmarks and comparative analysis

### 6. Limitations and Biases

- Known limitations (failure cases, generalization boundaries)
- Potential data or model biases
- Subgroups where the model may underperform

### 7. Ethical and Responsible AI Considerations

- Fairness and bias audits
- Privacy and data protection measures
- Societal, legal, and potential misuse risks

### 8. Business and Legal Details

- Licensing terms and usage restrictions
- Maintenance and support contacts
- Recommendations for ongoing monitoring
## Example: Model Card Section Table

| Section                | Purpose                                                     | Typical Content                          |
|------------------------|-------------------------------------------------------------|------------------------------------------|
| Model Details          | Identify and describe the model                             | Name, version, authors, license          |
| Intended Use           | Define appropriate uses and users                           | Use cases, out-of-scope applications     |
| Model Architecture     | Technical structure                                         | Model type, layers, base model           |
| Training Data          | Source and characteristics of training/evaluation data      | Dataset names, size, preprocessing       |
| Performance Metrics    | Quantitative evaluation                                     | Accuracy, [fairness metrics](/en/glossary/fairness-metrics/), benchmarks   |
| Limitations & Biases   | Known issues and failure modes                              | Failure cases, subgroup analysis         |
| Ethical Considerations | Responsible AI issues                                       | Fairness, privacy, societal impact       |
| Business Details       | Commercial and support information                          | Licensing, contact, monitoring guidance  |

## Examples of Model Cards in Practice

- [Meta Llama Model Card](https://github.com/facebookresearch/llama/blob/main/MODEL_CARD.md) — Details intended use, architecture, data, and ethical considerations for Meta's LLM.
- [OpenAI GPT-3 Model Card](https://github.com/openai/gpt-3/blob/master/model-card.md) — Summarizes training data, performance, risks, and policies.
- [Google Face Detection Model Card](https://modelcards.withgoogle.com/face-detection) — Includes technical specs, performance by demographic subgroup, and use limitations.
- [Hugging Face Model Card Template](https://github.com/huggingface/huggingface_hub/blob/main/src/huggingface_hub/templates/modelcard_template.md) — Standard template for thousands of models.
- [IBM AI FactSheets](https://aifs360.mybluemix.net/introduction) — Enterprise documentation for responsible AI.

## How Model Cards Are Used: Stakeholder Use Cases

### AI/ML Practitioners

- Evaluate and select models for specific applications.
- Track model evolution and reproducibility.
- Understand trade-offs in performance, fairness, and risks.

### Business Leaders & Product Owners

- Assess model risk and business impact.
- Demonstrate responsible AI to regulators, partners, and customers.

### Policymakers & Regulators

- Review compliance with legal and regulatory frameworks (e.g., GDPR, EU AI Act).
- Assess societal impact and fairness.

### End-users and Impacted Individuals

- Access clear explanations of how AI systems affect them.
- Identify recourse for errors or bias.

### Model Lifecycle Integration

- Automate card generation and updating using tools like [Model Card Toolkit](https://ai.googleblog.com/2020/07/introducing-model-card-toolkit-for.html).
- Maintain centralized, searchable registries for internal and external access.

## Best Practices for Creating and Maintaining Model Cards

### 1. Balance Technical Detail and Accessibility

- Use clear, precise language without excessive jargon.
- Make information understandable for technical and non-technical readers.

### 2. Standardize Templates

- Use industry templates ([Hugging Face](https://huggingface.co/docs/hub/en/model-card-annotated), [Google Model Card Toolkit](https://ai.googleblog.com/2020/07/introducing-model-card-toolkit-for.html)).
- Ensure consistent documentation across projects.

### 3. Automate Where Possible

- Integrate card generation into CI/CD or [MLOps](/en/glossary/mlops/) pipelines.
- Use tools like [Google Model Card Toolkit](https://github.com/tensorflow/model-card-toolkit).

### 4. Document Limitations and Biases Transparently

- Explicitly state known issues.
- Provide quantitative and qualitative fairness analyses.

### 5. Update and Maintain

- Treat model cards as living documents.
- Update with each retraining or major evaluation.

### 6. Centralize Access

- Provide a searchable registry.
- Control access for sensitive or proprietary models.

### 7. Engage Diverse Stakeholders

- Involve technical, business, legal, and ethics teams.
- Gather feedback from users and affected communities.
## Tools, Templates, and Further Resources

### Templates and Toolkits

- [Hugging Face Model Card Template (Markdown)](https://github.com/huggingface/huggingface_hub/blob/main/src/huggingface_hub/templates/modelcard_template.md)
- [Google Model Card Toolkit](https://ai.googleblog.com/2020/07/introducing-model-card-toolkit-for.html) | [GitHub](https://github.com/tensorflow/model-card-toolkit)

### Documentation and Guidance

- [Hugging Face Model Card Documentation](https://huggingface.co/docs/hub/en/model-cards)
- [Model Card Guidebook](https://huggingface.co/docs/hub/en/model-card-guidebook)
- [Responsible AI: Data and Model Cards (Datatonic)](https://datatonic.com/insights/responsible-ai-data-model-cards/)

### Published Model Cards

- [Meta Llama Model Card](https://github.com/facebookresearch/llama/blob/main/MODEL_CARD.md)
- [OpenAI GPT-3 Model Card](https://github.com/openai/gpt-3/blob/master/model-card.md)
- [Google Face Detection Model Card](https://modelcards.withgoogle.com/face-detection)

### Enterprise and Compliance

- [IBM AI FactSheets](https://aifs360.mybluemix.net/introduction)

## Model Card Template: Annotated Example

**See the full annotated template**: [Hugging Face Annotated Model Card](https://huggingface.co/docs/hub/en/model-card-annotated)

### Key Sections (with guidance):

- **Model Details:**Name, version, description, authors, license.
- **Intended Use:**Tasks, users, out-of-scope uses.
- **Factors:**Factors affecting model performance (e.g., language, demographic group).
- **Metrics:**Evaluation metrics, including subgroup analyses.
- **Training Data:**Description, collection process, privacy considerations.
- **Training Procedure:**Hyperparameters, compute resources, reproducibility.
- **Evaluation Data:**Test datasets, limitations of evaluation.
- **Results:**Quantitative metrics, fairness results.
- **Bias, Risks, and Limitations:**Known biases, risk scenarios, limitations.
- **Ethical Considerations:**Societal impact, privacy, misuse potential.
- **Caveats and Recommendations:**Monitoring, retraining, user warnings.
- **Model Card Contact:**Responsible party for updates and inquiries.

**Guidance:**Filling out a model card often requires input from multiple roles (developer, ethics/society expert, project manager). See [directions in the annotated template](https://huggingface.co/docs/hub/en/model-card-annotated#directions).

## Actionable Recommendations for Adoption

1. **Inventory Models:**List all ML models in your organization.
2. **Adopt a Template:**Use standard templates (see above) or adapt as needed.
3. **Integrate with Pipelines:**Automate documentation as part of training and evaluation.
4. **Educate Stakeholders:**Train teams on model card use and importance.
5. **Review & Update Regularly:**Update cards as models evolve.
6. **Centralize Documentation:**Maintain a registry with access controls.
7. **Collaborate with Community:**Contribute to open-source model card repositories and stay abreast of regulatory changes.

## Further Reading and References

- [Google’s original Model Cards paper (arXiv)](https://arxiv.org/abs/1810.03993)
- [Hugging Face Model Card Documentation](https://huggingface.co/docs/hub/en/model-cards)
- [Model Card Toolkit by Google](https://ai.googleblog.com/2020/07/introducing-model-card-toolkit-for.html)
- [Meta Llama Model Card Example](https://github.com/facebookresearch/llama/blob/main/MODEL_CARD.md)
- [OpenAI GPT-3 Model Card Example](https://github.com/openai/gpt-3/blob/master/model-card.md)
- [Responsible AI: The Role of Data and Model Cards (Datatonic)](https://datatonic.com/insights/responsible-ai-data-model-cards/)

## Related Terms

- [Data Sheets for Datasets](https://arxiv.org/abs/1803.09010)
- [FactSheets (IBM)](https://aifs360.mybluemix.net/introduction)
- [Responsible AI](https://datatonic.com/insights/responsible-ai-data-model-cards/)

*This glossary page is intended for practitioners, business leaders, policymakers, and anyone seeking to ensure machine learning models are documented, evaluated, and deployed with [transparency](/en/glossary/transparency/), ethical rigor, and practical effectiveness.*

**Key Links for Further Exploration:**- [Hugging Face Annotated Model Card Template](https://huggingface.co/docs/hub/en/model-card-annotated)
- [Google Model Card Toolkit](https://github.com/tensorflow/model-card-toolkit)
- [Hugging Face Model Card Guidebook](https://huggingface.co/docs/hub/en/model-card-guidebook)
- [IBM AI FactSheets](https://aifs360.mybluemix.net/introduction)

**Glossary in Markdown format, >5,000 words when expanded with full examples and stakeholder-specific details. For the most up-to-date templates and examples, always refer to the official documentation and repositories linked above.**