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

<strong>Zero-shot learning (ZSL)</strong>is a machine learning paradigm in which a model is able to recognize or classify instances from classes that were not represented in its training data. Rather than relying solely on labeled examples, zero-shot learning enables a model to generalize knowledge by leveraging auxiliary information such as semantic descriptions, attribute vectors, or embeddings, and to apply this generalization to make predictions on previously unseen classes ([IBM](https://www.ibm.com/think/topics/zero-shot-learning), [Lightly AI](https://www.lightly.ai/blog/zero-shot-learning)).

ZSL is particularly impactful in domains where the number of possible classes or categories is large, open-ended, or ever-expanding, making it infeasible to collect labeled data for every class.

## How Zero-Shot Learning Works

### Knowledge Transfer via Auxiliary Information

The core idea of ZSL is to bridge the gap between <strong>seen classes</strong>(those with labeled training data) and <strong>unseen classes</strong>(those with no labeled examples) using auxiliary knowledge. This auxiliary information can take various forms:

- <strong>Semantic Descriptions</strong>: Natural language explanations or definitions of classes.
- <strong>Attribute Vectors</strong>: Explicitly defined features such as color, shape, or function.
- <strong>Embeddings</strong>: Learned high-dimensional vectors representing classes, often derived from large language or vision models.

### Typical Workflow

1. <strong>Model Pre-training</strong>- The model is trained on a large dataset containing many classes (the "seen" classes).
   - During this phase, general representations are learned (using self-supervised or supervised techniques).
   - Example: A vision model trained on ImageNet learns representations for thousands of objects.

2. <strong>Auxiliary Information Acquisition</strong>- For each unseen class, semantic descriptions or attribute vectors are provided.
   - Example: If "zebra" is unseen, an attribute vector might specify "has stripes, is a mammal, is four-legged."

3. <strong>Embedding to a Shared Semantic Space</strong>- Both inputs (e.g., images or text) and class descriptions are mapped to a common embedding space.
   - This is often achieved using neural networks (transformers for text, CNNs for images).
   - The distance or similarity in this space is used for classification.

4. <strong>Similarity-Based Classification</strong>- When presented with a new input, the model computes its embedding and compares it to the embeddings of candidate classes (based on auxiliary info).
   - The class whose embedding is most similar (via cosine similarity, Euclidean distance, etc.) is selected.

5. <strong>Prediction</strong>- The model outputs the class label for the input, even if it has never seen labeled data for that class during training.

([Lightly AI Guide](https://www.lightly.ai/blog/zero-shot-learning))

## Examples

### Computer Vision

- <strong>Animal Recognition</strong>: A model trained on "horses" but not "zebras" is told a "zebra looks like a horse with stripes." Using the concept of "horse" and the new attribute "striped," it can identify zebras in images.
- <strong>Object Detection</strong>: Identifying rare or new objects in surveillance or medical images based on attribute descriptions.

### Natural Language Processing (NLP)

- <strong>Text Classification</strong>: Using a pre-trained language model (like BERT or GPT), a system can classify text into categories it has never seen directly, using label descriptions.
- <strong>Sentiment Analysis</strong>: A model can infer sentiment by understanding the semantics of "positive" and "negative" without explicit training on labeled sentiment data.
- <strong>Intent Detection in Chatbots</strong>: Answering user queries about new topics by matching the query's meaning to documentation or knowledge base entries.

([Lightly AI Guide](https://www.lightly.ai/blog/zero-shot-learning), [IBM](https://www.ibm.com/think/topics/zero-shot-learning))

## Key Technical Methods

### Attribute-Based Methods

- <strong>Attributes</strong>are human-defined characteristics that describe classes (e.g., "has feathers," "can fly").
- During training, the model learns to recognize these attributes.
- At inference, unseen classes are described solely by their attributes.
- <strong>Example</strong>: Classifying "penguin" by "has feathers, cannot fly" even if there are no penguin images in the training set.

#### Steps:
1. Define a set of attributes relevant to the domain.
2. Train the model to predict attributes from input data.
3. Encode each class as an attribute vector.
4. At inference, match the inferred attribute vector of an input to the attribute profile of each class.

<strong>Pros</strong>: Intuitive, interpretable.
<strong>Cons</strong>: Requires comprehensive and discriminative attributes, which can be costly to annotate.

([Lightly AI Guide](https://www.lightly.ai/blog/zero-shot-learning))

### Embedding-Based Methods

- Both inputs and class descriptions are mapped to a high-dimensional embedding space.
- Embeddings are obtained from pre-trained models (e.g., BERT for text, ResNet for images).
- The class whose embedding is most similar to the input's embedding is selected.

#### Steps:
1. Use a pre-trained model to embed both data and class labels/descriptions.
2. Normalize and compare embeddings in a shared space.
3. Assign the input to the class with the highest similarity.

<strong>Pros</strong>: Scalable to large label spaces, effective for multi-modal data.
<strong>Cons</strong>: Relies on the quality of embedding models and the semantic richness of class descriptions.

([Lightly AI Guide](https://www.lightly.ai/blog/zero-shot-learning))

### Joint Embedding Space

- ZSL often employs a <strong>joint embedding space</strong>for heterogeneous data (e.g., images and text).
- Models are trained so that semantically similar items from different modalities are close in the embedding space.
- Used for tasks like image-text retrieval, cross-modal classification, and more.

([Towards AI Deep Dive](https://towardsai.net/p/l/zero-shot-learning-deep-dive-how-to-select-one-and-present-day-challenges))

### Pretrained Foundation Models

- Large foundation models like BERT, GPT (for NLP), ResNet, or Vision Transformers (for vision) are commonly used.
- These models internalize semantic relationships and can generalize to tasks or classes not seen during training.
- <strong>Example</strong>: GPT-3 answering novel factual questions, CLIP matching text to images.

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

- <strong>Object Recognition</strong>: Recognizing new objects without labeled images ([IBM](https://www.ibm.com/think/topics/zero-shot-learning)).
- <strong>Medical Imaging</strong>: Diagnosing rare diseases from images based on attribute profiles.
- <strong>Surveillance</strong>: Identifying suspicious objects or behaviors not seen during training.

### Natural Language Processing

- <strong>Intent Classification</strong>: Extending chatbots to new topics or intents.
- <strong>Topic Segmentation</strong>: Assigning documents to new categories as they emerge.
- <strong>Multilingual Translation</strong>: Translating to/from languages with little or no parallel data.

### Recommendation Systems

- <strong>Cold Start</strong>: Recommending new items or to new users using metadata or descriptions.

### Healthcare & Bioinformatics

- <strong>Rare Disease Detection</strong>: Inferring properties of diseases with limited data using textual/structural descriptions.

([Lightly AI Guide](https://www.lightly.ai/blog/zero-shot-learning), [IBM](https://www.ibm.com/think/topics/zero-shot-learning))

## Advantages

- <strong>Scalability</strong>: No need for labeled data for every class.
- <strong>Flexibility</strong>: New classes can be added simply by providing their descriptions or attributes.
- <strong>Cost-Efficiency</strong>: Reduces annotation cost, especially for rare or emerging categories.
- <strong>Generalization</strong>: Models can handle a much broader range of tasks and concepts.

([Lightly AI Guide](https://www.lightly.ai/blog/zero-shot-learning), [IBM](https://www.ibm.com/think/topics/zero-shot-learning))

## Challenges and Limitations

### Semantic Gap

- If class descriptions or attributes are ambiguous, incomplete, or not discriminative, model performance drops.
- The quality and relevance of auxiliary information is critical.

### Attribute Annotation Cost

- Defining discriminative attribute sets can be subjective and time-consuming.

### Bias Toward Seen Classes

- In <strong>Generalized Zero-Shot Learning (GZSL)</strong>, models often favor seen classes at inference, leading to poor performance on truly unseen classes.

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
| <strong>Zero-Shot Learning (ZSL)</strong>| Model predicts classes with no labeled examples, using auxiliary information | Chatbots answering novel questions |
| <strong>Attribute-Based ZSL</strong>| Uses predefined attributes to describe and infer class membership | Vision models classifying unseen animals |
| <strong>Embedding-Based ZSL</strong>| Represents data and classes as vectors in a shared space | Text classification for new topics |
| <strong>Generalized ZSL (GZSL)</strong>| Handles both seen and unseen classes at inference | Product categorization as catalogs update |
| <strong>Few-Shot Learning</strong>| Recognizes new classes from a handful of labeled examples | Disease diagnosis for rare conditions |
| <strong>Transfer Learning</strong>| Adapts pre-trained models for new tasks | Adapting vision models to new domains |

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

<strong>This glossary incorporates and cites information from authoritative technical sources, including IBM, Lightly AI, and Towards AI. For further exploration, consult the linked articles and resources.</strong>

