---
title: "Zero-Shot Learning (ZSL)"
date: 2025-12-17
translationKey: "zero-shot-learning-zsl"
description: "Zero-shot learning (ZSL) is a machine learning paradigm enabling models to classify instances from unseen classes by leveraging auxiliary information like semantic descriptions or embeddings, reducing the need for extensive labeled data."
keywords: ["zero-shot learning", "machine learning", "unseen classes", "auxiliary information", "embedding-based methods"]
category: "Machine Learning"
type: "glossary"
draft: false
---

## Definition

**Zero-shot learning (ZSL)**is a machine learning paradigm in which a model is able to recognize or classify instances from classes that were not represented in its training data. Rather than relying solely on labeled examples, zero-shot learning enables a model to generalize knowledge by leveraging auxiliary information such as semantic descriptions, attribute vectors, or embeddings, and to apply this generalization to make predictions on previously unseen classes ([IBM](https://www.ibm.com/think/topics/zero-shot-learning), [Lightly AI](https://www.lightly.ai/blog/zero-shot-learning)).

ZSL is particularly impactful in domains where the number of possible classes or categories is large, open-ended, or ever-expanding, making it infeasible to collect labeled data for every class.

## How Zero-Shot Learning Works

### Knowledge Transfer via Auxiliary Information

The core idea of ZSL is to bridge the gap between **seen classes**(those with labeled training data) and **unseen classes**(those with no labeled examples) using auxiliary knowledge. This auxiliary information can take various forms:

- **Semantic Descriptions**: Natural language explanations or definitions of classes.
- **Attribute Vectors**: Explicitly defined features such as color, shape, or function.
- **Embeddings**: Learned high-dimensional vectors representing classes, often derived from large language or vision models.

### Typical Workflow

1. **Model Pre-training**- The model is trained on a large dataset containing many classes (the "seen" classes).
   - During this phase, general representations are learned (using self-supervised or supervised techniques).
   - Example: A vision model trained on ImageNet learns representations for thousands of objects.

2. **Auxiliary Information Acquisition**- For each unseen class, semantic descriptions or attribute vectors are provided.
   - Example: If "zebra" is unseen, an attribute vector might specify "has stripes, is a mammal, is four-legged."

3. **Embedding to a Shared Semantic Space**- Both inputs (e.g., images or text) and class descriptions are mapped to a common embedding space.
   - This is often achieved using neural networks (transformers for text, CNNs for images).
   - The distance or similarity in this space is used for classification.

4. **Similarity-Based Classification**- When presented with a new input, the model computes its embedding and compares it to the embeddings of candidate classes (based on auxiliary info).
   - The class whose embedding is most similar (via cosine similarity, Euclidean distance, etc.) is selected.

5. **Prediction**- The model outputs the class label for the input, even if it has never seen labeled data for that class during training.

([Lightly AI Guide](https://www.lightly.ai/blog/zero-shot-learning))

## Examples

### Computer Vision

- **Animal Recognition**: A model trained on "horses" but not "zebras" is told a "zebra looks like a horse with stripes." Using the concept of "horse" and the new attribute "striped," it can identify zebras in images.
- **Object Detection**: Identifying rare or new objects in surveillance or medical images based on attribute descriptions.

### Natural Language Processing (NLP)

- **Text Classification**: Using a pre-trained language model (like BERT or GPT), a system can classify text into categories it has never seen directly, using label descriptions.
- **Sentiment Analysis**: A model can infer sentiment by understanding the semantics of "positive" and "negative" without explicit training on labeled sentiment data.
- **Intent Detection in Chatbots**: Answering user queries about new topics by matching the query's meaning to documentation or knowledge base entries.

([Lightly AI Guide](https://www.lightly.ai/blog/zero-shot-learning), [IBM](https://www.ibm.com/think/topics/zero-shot-learning))

## Key Technical Methods

### Attribute-Based Methods

- **Attributes**are human-defined characteristics that describe classes (e.g., "has feathers," "can fly").
- During training, the model learns to recognize these attributes.
- At inference, unseen classes are described solely by their attributes.
- **Example**: Classifying "penguin" by "has feathers, cannot fly" even if there are no penguin images in the training set.

#### Steps:
1. Define a set of attributes relevant to the domain.
2. Train the model to predict attributes from input data.
3. Encode each class as an attribute vector.
4. At inference, match the inferred attribute vector of an input to the attribute profile of each class.

**Pros**: Intuitive, interpretable.
**Cons**: Requires comprehensive and discriminative attributes, which can be costly to annotate.

([Lightly AI Guide](https://www.lightly.ai/blog/zero-shot-learning))

### Embedding-Based Methods

- Both inputs and class descriptions are mapped to a high-dimensional embedding space.
- Embeddings are obtained from pre-trained models (e.g., BERT for text, ResNet for images).
- The class whose embedding is most similar to the input's embedding is selected.

#### Steps:
1. Use a pre-trained model to embed both data and class labels/descriptions.
2. Normalize and compare embeddings in a shared space.
3. Assign the input to the class with the highest similarity.

**Pros**: Scalable to large label spaces, effective for multi-modal data.
**Cons**: Relies on the quality of embedding models and the semantic richness of class descriptions.

([Lightly AI Guide](https://www.lightly.ai/blog/zero-shot-learning))

### Joint Embedding Space

- ZSL often employs a **joint embedding space**for heterogeneous data (e.g., images and text).
- Models are trained so that semantically similar items from different modalities are close in the embedding space.
- Used for tasks like image-text retrieval, cross-modal classification, and more.

([Towards AI Deep Dive](https://towardsai.net/p/l/zero-shot-learning-deep-dive-how-to-select-one-and-present-day-challenges))

### Pretrained Foundation Models

- Large foundation models like BERT, GPT (for NLP), ResNet, or Vision Transformers (for vision) are commonly used.
- These models internalize semantic relationships and can generalize to tasks or classes not seen during training.
- **Example**: GPT-3 answering novel factual questions, CLIP matching text to images.

([Lightly AI Guide](https://www.lightly.ai/blog/zero-shot-learning), [IBM](https://www.ibm.com/think/topics/zero-shot-learning))

## Mathematical Formulation

Let:
- \( x \) denote an input example (image, text, etc.).
- \( y \) denote a class label.
- \( \mathcal{Y}_S \) be the set of seen classes.
- \( \mathcal{Y}_U \) be the set of unseen classes (at inference).

The model learns a function \( f(x, a(y)) \) where \( a(y) \) is the auxiliary information (attributes, embedding) for class \( y \). At inference, given \( x \) and auxiliary information for all \( y \in \mathcal{Y}_U \), the model predicts:

\[
\hat{y} = \arg\max_{y \in \mathcal{Y}_U} \text{Similarity}(g(x), h(a(y)))
\]

Where:
- \( g(x) \) is the embedding of input \( x \).
- \( h(a(y)) \) is the embedding of auxiliary information for \( y \).
- Similarity is often cosine similarity or dot product in the embedding space.

([Lightly AI Guide](https://www.lightly.ai/blog/zero-shot-learning))

## Applications

### Computer Vision

- **Object Recognition**: Recognizing new objects without labeled images ([IBM](https://www.ibm.com/think/topics/zero-shot-learning)).
- **Medical Imaging**: Diagnosing rare diseases from images based on attribute profiles.
- **Surveillance**: Identifying suspicious objects or behaviors not seen during training.

### Natural Language Processing

- **Intent Classification**: Extending chatbots to new topics or intents.
- **Topic Segmentation**: Assigning documents to new categories as they emerge.
- **Multilingual Translation**: Translating to/from languages with little or no parallel data.

### Recommendation Systems

- **Cold Start**: Recommending new items or to new users using metadata or descriptions.

### Healthcare & Bioinformatics

- **Rare Disease Detection**: Inferring properties of diseases with limited data using textual/structural descriptions.

([Lightly AI Guide](https://www.lightly.ai/blog/zero-shot-learning), [IBM](https://www.ibm.com/think/topics/zero-shot-learning))

## Advantages

- **Scalability**: No need for labeled data for every class.
- **Flexibility**: New classes can be added simply by providing their descriptions or attributes.
- **Cost-Efficiency**: Reduces annotation cost, especially for rare or emerging categories.
- **Generalization**: Models can handle a much broader range of tasks and concepts.

([Lightly AI Guide](https://www.lightly.ai/blog/zero-shot-learning), [IBM](https://www.ibm.com/think/topics/zero-shot-learning))

## Challenges and Limitations

### Semantic Gap

- If class descriptions or attributes are ambiguous, incomplete, or not discriminative, model performance drops.
- The quality and relevance of auxiliary information is critical.

### Attribute Annotation Cost

- Defining discriminative attribute sets can be subjective and time-consuming.

### Bias Toward Seen Classes

- In **Generalized Zero-Shot Learning (GZSL)**, models often favor seen classes at inference, leading to poor performance on truly unseen classes.

### Representation Limitations

- Embedding methods assume that all classes (seen and unseen) are adequately represented in the embedding space, which may not hold for out-of-distribution or novel concepts.

### Evaluation

- Standard accuracy metrics may not reflect ZSL's generalization ability.
- Requires benchmarks and protocols specifically designed for ZSL.

### Domain Shift

- Discrepancies between the distribution of seen and unseen classes can degrade performance.

([Lightly AI Guide](https://www.lightly.ai/blog/zero-shot-learning), [Towards AI Deep Dive](https://towardsai.net/p/l/zero-shot-learning-deep-dive-how-to-select-one-and-present-day-challenges))

## Related Concepts

| Concept | Description | Example Use Case |
|---|---|---|
| **Zero-Shot Learning (ZSL)**| Model predicts classes with no labeled examples, using auxiliary information | Chatbots answering novel questions |
| **Attribute-Based ZSL**| Uses predefined attributes to describe and infer class membership | Vision models classifying unseen animals |
| **Embedding-Based ZSL**| Represents data and classes as vectors in a shared space | Text classification for new topics |
| **Generalized ZSL (GZSL)**| Handles both seen and unseen classes at inference | Product categorization as catalogs update |
| **Few-Shot Learning**| Recognizes new classes from a handful of labeled examples | Disease diagnosis for rare conditions |
| **Transfer Learning**| Adapts pre-trained models for new tasks | Adapting vision models to new domains |

([Lightly AI Guide](https://www.lightly.ai/blog/zero-shot-learning))

## Further Reading and Resources

- [IBM: What Is Zero-Shot Learning?](https://www.ibm.com/think/topics/zero-shot-learning)
- [Lightly AI: Zero-Shot Learning: A Practical Guide](https://www.lightly.ai/blog/zero-shot-learning)
- [Towards AI: Zero-shot Learning Deep Dive: How to Select One and Present-day Challenges](https://towardsai.net/p/l/zero-shot-learning-deep-dive-how-to-select-one-and-present-day-challenges)
- [Google AI Blog: Zero-shot Learning](https://ai.googleblog.com/2021/06/zero-shot-learning-for-visual.html)
- [Hugging Face Transformers: Zero-shot Classification](https://huggingface.co/docs/transformers/main_classes/pipelines#transformers.ZeroShotClassificationPipeline)
- [Arxiv: A Survey on Zero-Shot Learning](https://arxiv.org/abs/1904.01198)

## Summary

Zero-shot learning is a transformative approach in machine learning that pushes the boundaries of what AI systems can do, particularly in terms of scalability, adaptability, and cost-efficiency. By leveraging auxiliary information and shared semantic spaces, ZSL enables models to generalize to new tasks and classes without direct supervision. However, its effectiveness depends on the quality of auxiliary information, the power of pre-trained models, and the design of the underlying embedding spaces.

*For more technical details, practical guides, and updates, refer to:*
- [IBM ZSL Overview](https://www.ibm.com/think/topics/zero-shot-learning)
- [Lightly AI: Zero-Shot Learning Guide](https://www.lightly.ai/blog/zero-shot-learning)
- [Towards AI: Deep Dive](https://towardsai.net/p/l/zero-shot-learning-deep-dive-how-to-select-one-and-present-day-challenges)
- [Hugging Face Zero-Shot Pipeline](https://huggingface.co/docs/transformers/main_classes/pipelines#transformers.ZeroShotClassificationPipeline)

**This glossary incorporates and cites information from authoritative technical sources, including IBM, Lightly AI, and Towards AI. For further exploration, consult the linked articles and resources.**

