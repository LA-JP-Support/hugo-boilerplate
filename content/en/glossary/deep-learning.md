---
title: "Deep Learning"
lastmod: 2025-12-18
date: 2025-12-18
translationKey: "deep-learning"
description: "A machine learning technology that uses multiple layers of artificial networks inspired by the human brain to automatically discover patterns and features from raw data, enabling computers to perform tasks like image recognition and language understanding."
keywords: ["deep learning", "neural networks", "machine learning", "artificial intelligence", "AI chatbots"]
category: "AI Chatbot & Automation"
type: "glossary"
draft: false
---

## What is Deep Learning?

Deep learning is a specialized branch of machine learning and artificial intelligence (AI) that uses multi-layered artificial neural networks to learn, extract, and model complex patterns from large and often unstructured datasets. The architecture of deep learning algorithms draws inspiration from the structure and functioning of the human brain, enabling computers to handle sophisticated tasks such as image recognition, natural language understanding, speech processing, autonomous decision-making, and creative content generation.

The term "deep" refers to the multiple layers of processing nodes (neurons) that transform input data through increasingly abstract representations. Unlike traditional machine learning approaches that require manual feature engineering—where human experts must identify and extract relevant characteristics from data—deep learning models automatically discover hierarchical features directly from raw data. This capability has revolutionized fields ranging from computer vision and natural language processing to robotics and drug discovery.

Deep learning represents a paradigm shift in how machines learn. Traditional programming involves writing explicit rules and logic to solve problems. Machine learning takes a step forward by learning patterns from examples. Deep learning extends this further by learning not just patterns but the optimal representations of data itself, discovering features that even human experts might not recognize as relevant. This automatic feature learning, combined with the ability to process massive datasets and leverage modern computational power, has made deep learning the foundation of contemporary AI breakthroughs.

The explosive growth of deep learning since the early 2010s stems from three converging factors: the availability of vast datasets for training (big data), dramatic increases in computational power particularly through GPUs (graphics processing units), and algorithmic innovations that enable effective training of very deep networks. These advances have transformed deep learning from a theoretical curiosity into a practical technology that powers everything from smartphone face recognition to autonomous vehicles to medical diagnosis systems.

## How Deep Learning Works

### Neural Networks: Architecture and Mechanisms

Artificial neural networks are computational structures inspired by biological neural networks in animal brains. Each network consists of interconnected layers of artificial neurons that process and transform information:

**Input Layer**Receives raw data in its original form—pixel values for images, word embeddings for text, or numerical features for structured data. The input layer passes this information forward without transformation, serving as the entry point for data into the network.

**Hidden Layers**Intermediate layers where the actual learning and feature extraction occurs. Each neuron in a hidden layer receives inputs from the previous layer, applies mathematical transformations through weights and activation functions, and passes results to the next layer. Multiple hidden layers enable the learning of increasingly complex and abstract representations. A network with many hidden layers is considered "deep," hence the name deep learning.

**Output Layer**Produces the final result—class probabilities for classification tasks, continuous values for regression, generated sequences for language models, or reconstructed data for autoencoders. The structure of the output layer depends on the specific task the network aims to solve.

### Layers and Hierarchical Feature Learning

The power of deep learning lies in hierarchical feature extraction across layers. Each layer builds upon representations learned by previous layers, progressively transforming raw input into increasingly abstract and meaningful representations.

For image recognition, early layers might detect simple features like edges, corners, and textures—basic building blocks of visual information. Middle layers combine these simple features into more complex shapes, parts of objects, and patterns. Deeper layers recognize complete objects, scenes, and contextual relationships. This hierarchical organization mirrors how visual processing works in biological brains, where information flows from simple visual features to complex object recognition.

In natural language processing, early layers might learn character or word-level patterns, middle layers capture syntactic structures and grammatical relationships, and deep layers understand semantic meaning, context, and pragmatic nuances. This automatic discovery of hierarchical representations eliminates the need for manual feature engineering and enables models to learn optimal representations for specific tasks.

### Weights, Biases, and Activation Functions

Neural networks learn through adjusting internal parameters:

**Weights**Numerical parameters that represent the strength and direction of connections between neurons. During training, weights are iteratively adjusted to minimize the difference between predicted and actual outputs. The specific values of millions or billions of weights in a network encode the learned patterns and knowledge.

**Biases**Additional parameters added to each neuron that provide flexibility in fitting data. Biases allow neurons to shift their activation functions, enabling better modeling of complex patterns.

**Activation Functions**Nonlinear functions applied to weighted sums of inputs, introducing the nonlinearity essential for modeling complex relationships. Common activation functions include:
- ReLU (Rectified Linear Unit): Most widely used, outputs zero for negative inputs and the input value for positive inputs
- Sigmoid: Squashes outputs to range 0-1, useful for probability outputs
- Tanh: Squashes outputs to range -1 to 1, often used in recurrent networks
- Softmax: Converts output values into probability distributions, used for multi-class classification

Without nonlinear activation functions, multiple layers would collapse into a single linear transformation, eliminating the benefit of depth.

### Forward Propagation and Prediction

During forward propagation, data flows from input through hidden layers to output:

1. Input data enters the network
2. Each layer applies linear transformations (weighted sums) followed by nonlinear activation functions
3. Information flows forward through all layers
4. The output layer produces predictions

This process happens very quickly even with millions of parameters, particularly when accelerated by specialized hardware like GPUs.

### Loss Functions and Error Measurement

Loss functions quantify how far predictions deviate from actual targets:

- **Mean Squared Error (MSE)**: For regression tasks, measures average squared differences
- **Cross-Entropy Loss**: For classification, measures difference between predicted and true probability distributions
- **Custom Loss Functions**: Designed for specific applications like object detection, semantic segmentation, or generative models

The choice of loss function profoundly impacts what the network learns and how it behaves.

### Backpropagation and Learning

Backpropagation is the algorithm that enables neural networks to learn from data:

1. **Forward Pass**: Input data flows through the network to generate predictions
2. **Loss Calculation**: The loss function measures prediction error
3. **Gradient Computation**: Backpropagation calculates how much each weight contributed to the error by computing gradients of the loss with respect to all parameters
4. **Parameter Update**: Optimization algorithms (typically variants of gradient descent) adjust weights to reduce the loss

This process repeats thousands or millions of times across many training examples, gradually improving the network's performance. Modern deep learning uses sophisticated optimization algorithms like Adam, RMSprop, or AdamW that adapt learning rates for different parameters and accelerate convergence.

The remarkable aspect of backpropagation is its efficiency—it calculates gradients for millions of parameters in reasonable time through clever application of the chain rule from calculus. This makes training very deep networks computationally feasible.

## Types of Neural Networks

Deep learning encompasses diverse neural network architectures, each designed for specific data types and tasks:

### 1. Feedforward Neural Networks (FNNs)

The simplest architecture where information flows in one direction from input to output without cycles. Fully connected layers connect every neuron in one layer to every neuron in the next. Used for basic classification and regression on structured, tabular data.

### 2. Multilayer Perceptrons (MLPs)

Feedforward networks with one or more hidden layers. Despite their simplicity, MLPs can approximate any continuous function given sufficient hidden units (universal approximation theorem). They serve as building blocks for more complex architectures.

### 3. Convolutional Neural Networks (CNNs)

Specifically designed for grid-structured data like images and video. CNNs use convolutional layers that apply filters to detect local patterns, pooling layers that downsample feature maps, and fully connected layers for final classification.

**Key Innovations:**- Local receptive fields capture spatial relationships
- Weight sharing across spatial locations reduces parameters
- Translation invariance recognizes patterns regardless of position
- Hierarchical feature learning from edges to complex objects

**Applications:**Image classification, object detection, facial recognition, medical image analysis, autonomous vehicle perception, video analysis.

**Notable Architectures:**LeNet, AlexNet, VGGNet, ResNet, Inception, EfficientNet, Vision Transformers.

### 4. Recurrent Neural Networks (RNNs)

Designed for sequential data where order matters. RNNs maintain internal hidden states that capture information from previous time steps, enabling processing of sequences of variable length.

**Characteristics:**- Loops in network architecture allow information persistence
- Share parameters across time steps
- Process one element at a time while maintaining memory

**Challenges:**Vanilla RNNs suffer from vanishing and exploding gradient problems when learning long-range dependencies.

**Applications:**Time series forecasting, speech recognition, music generation, video captioning, sequential decision-making.

### 5. Long Short-Term Memory (LSTM) Networks

Advanced RNN variant designed to address long-term dependency problems. LSTMs use gating mechanisms (input, forget, and output gates) to control information flow, enabling learning of relationships across long sequences.

**Advantages:**- Maintain information over long sequences
- Selectively forget irrelevant information
- Protect against vanishing gradients

**Applications:**Machine translation, speech recognition, handwriting recognition, language modeling, time series with long-term patterns.

### 6. Gated Recurrent Units (GRUs)

Simplified LSTM variant with fewer parameters. GRUs merge the forget and input gates into a single update gate, making them faster to train while maintaining similar performance to LSTMs for many tasks.

### 7. Transformer Networks

Revolutionary architecture that has become dominant for natural language processing and increasingly for other domains. Transformers use self-attention mechanisms to process entire sequences simultaneously rather than sequentially.

**Key Innovations:**- Self-attention mechanisms capture relationships between all positions
- Parallel processing enables training on massive datasets
- Positional encodings maintain sequence order information
- Multi-head attention captures different types of relationships

**Impact:**Transformers power modern large language models (GPT, BERT, Claude, etc.) and increasingly replace RNNs for sequential data processing.

**Applications:**Language translation, text generation, question answering, code generation, protein structure prediction, image generation (DALL-E).

### 8. Autoencoders

Unsupervised learning architecture that learns compressed representations of data. Autoencoders consist of an encoder that compresses input into a latent representation and a decoder that reconstructs the input from this representation.

**Types:**- Vanilla Autoencoders: Basic compression and reconstruction
- Variational Autoencoders (VAEs): Generate new samples by learning probability distributions
- Denoising Autoencoders: Learn robust representations by reconstructing corrupted inputs

**Applications:**Dimensionality reduction, anomaly detection, data denoising, feature learning, generative modeling.

### 9. Generative Adversarial Networks (GANs)

Consist of two networks in competition: a generator creates synthetic data, and a discriminator distinguishes real from generated data. Through adversarial training, the generator learns to create increasingly realistic outputs.

**Training Process:**- Generator creates fake samples
- Discriminator attempts to classify real vs. fake
- Both networks improve through competition
- Training reaches equilibrium when discriminator cannot distinguish real from fake

**Applications:**Image synthesis, style transfer, super-resolution, data augmentation, video generation, deepfake creation.

**Notable Variants:**DCGAN, StyleGAN, CycleGAN, Progressive GAN, Conditional GAN.

### 10. Graph Neural Networks (GNNs)

Process data structured as graphs (nodes and edges). GNNs aggregate information from neighboring nodes to learn representations that capture graph structure.

**Applications:**Social network analysis, molecular property prediction, recommendation systems, traffic forecasting, knowledge graphs.

### 11. Capsule Networks

Alternative architecture designed to better capture spatial hierarchies and viewpoint variations. Capsule networks use groups of neurons (capsules) to represent different properties of entities.

### 12. Residual Networks (ResNets)

Introduced skip connections that allow gradients to flow directly through network layers, enabling training of very deep networks (100+ layers). ResNets revolutionized image recognition by demonstrating that deeper networks could achieve better performance.

## Deep Learning vs. Machine Learning vs. AI

Understanding the relationship between these concepts clarifies their scope and applications:

| Aspect | Artificial Intelligence (AI) | Machine Learning (ML) | Deep Learning (DL) |
|--------|------------------------------|----------------------|-------------------|
| **Definition**| Broad field of creating intelligent systems | AI subset focused on learning from data | ML subset using deep neural networks |
| **Scope**| Encompasses all intelligent systems | Pattern recognition and prediction | Automatic feature learning from raw data |
| **Feature Engineering**| Varies by approach | Often requires manual feature extraction | Automatic feature learning |
| **Data Requirements**| Varies widely | Moderate datasets often sufficient | Requires large datasets for best performance |
| **Model Complexity**| Ranges from simple rules to complex systems | Moderate complexity | Highly complex with millions of parameters |
| **Hardware Requirements**| Varies by application | Standard CPUs often sufficient | Requires GPUs/TPUs for efficient training |
| **Interpretability**| Depends on approach | Generally interpretable | Often "black box" with limited interpretability |
| **Examples**| Expert systems, robotics, game playing | Spam filters, credit scoring, recommendation | Image recognition, language translation, speech synthesis |
| **Historical Development**| 1950s onwards | 1980s-1990s mainstream | 2010s breakthrough and rapid adoption |

**Hierarchy:**AI encompasses ML, which encompasses DL. Deep learning represents the current frontier of machine learning, achieving superhuman performance on many perceptual and cognitive tasks previously thought to require human intelligence.

## Applications and Real-World Use Cases

Deep learning transforms industries through diverse applications:

### Computer Vision

**Image Classification**Categorizing images into predefined classes. Applications include medical diagnosis from X-rays and MRI scans, agricultural crop disease detection, wildlife monitoring, and quality control in manufacturing.

**Object Detection**Locating and classifying multiple objects within images or video streams. Powers autonomous vehicle perception, surveillance systems, retail checkout automation, and industrial robotics.

**Semantic Segmentation**Classifying every pixel in an image by category. Used for medical image analysis (tumor delineation), autonomous driving (road scene understanding), satellite imagery analysis, and augmented reality.

**Face Recognition**Identifying individuals by facial features. Applications include security systems, photo organization, authentication, and social media tagging.

**Image Generation**Creating new images from text descriptions or modifying existing images. Enables creative tools for artists, product visualization, virtual environments, and content creation.

### Natural Language Processing

**Machine Translation**Translating text between languages with increasing fluency and accuracy. Powers Google Translate, DeepL, and real-time conversation translation.

**Text Generation**Producing coherent, contextually appropriate text. Applications include content creation, code generation, automated report writing, creative writing assistance, and conversational AI.

**Sentiment Analysis**Determining emotional tone and opinion in text. Used for brand monitoring, customer feedback analysis, market research, and social media monitoring.

**Named Entity Recognition**Identifying and classifying named entities (people, organizations, locations) in text. Supports information extraction, knowledge graph construction, and document analysis.

**Question Answering**Providing direct answers to natural language questions. Powers virtual assistants, customer support automation, and information retrieval systems.

**Text Summarization**Generating concise summaries of longer documents. Applications include news aggregation, research paper summarization, and meeting notes generation.

### Speech and Audio

**Speech Recognition**Converting spoken language to text. Enables voice assistants (Siri, Alexa, Google Assistant), transcription services, voice-controlled interfaces, and accessibility tools.

**Text-to-Speech**Generating natural-sounding speech from text. Applications include audiobook narration, assistive technologies, virtual assistants, and voice user interfaces.

**Music Generation**Creating original musical compositions. Enables AI-composed background music, creative tools for musicians, and personalized music experiences.

**Audio Enhancement**Removing noise, enhancing quality, and restoring damaged audio. Used in telecommunications, media production, and hearing aids.

### Healthcare and Life Sciences

**Medical Image Analysis**Detecting diseases from X-rays, CT scans, MRI images, and pathology slides. Assists radiologists in diagnosis, screening programs, and treatment planning.

**Drug Discovery**Predicting molecular properties, identifying drug candidates, and optimizing compounds. Accelerates pharmaceutical research and reduces development costs.

**Genomics**Analyzing genetic sequences, predicting gene function, and identifying disease-causing mutations. Enables personalized medicine and genetic research.

**Prognosis Prediction**Forecasting patient outcomes and disease progression. Supports treatment planning and resource allocation.

### Autonomous Systems

**Self-Driving Vehicles**Perceiving environments, making driving decisions, and controlling vehicle operation. Combines computer vision, sensor fusion, and reinforcement learning.

**Robotics**Enabling robots to perceive environments, manipulate objects, and navigate spaces. Applications span manufacturing, logistics, agriculture, and service industries.

**Drones**Autonomous flight, obstacle avoidance, and mission execution. Used for delivery, inspection, surveillance, and search-and-rescue operations.

### Recommendation Systems

**Content Recommendations**Suggesting movies, music, articles, or products based on user preferences and behavior. Powers Netflix, Spotify, YouTube, and e-commerce platforms.

**Social Media Feeds**Curating personalized content feeds based on engagement patterns and interests. Core to Facebook, Instagram, TikTok, and Twitter.

### Finance

**Fraud Detection**Identifying suspicious transactions in real-time. Protects against credit card fraud, money laundering, and identity theft.

**Algorithmic Trading**Executing trades based on learned patterns and predictions. Enables high-frequency trading and quantitative investment strategies.

**Risk Assessment**Evaluating credit risk, insurance risk, and market risk. Improves underwriting accuracy and portfolio management.

### Manufacturing and Industry

**Predictive Maintenance**Forecasting equipment failures before they occur. Reduces downtime and maintenance costs in manufacturing, energy, and transportation.

**Quality Control**Detecting defects and anomalies in production. Ensures consistent product quality and reduces waste.

**Process Optimization**Optimizing manufacturing parameters for efficiency and quality. Improves yield and reduces energy consumption.

## Advantages of Deep Learning

Deep learning offers compelling benefits that drive its widespread adoption:

**Automatic Feature Learning**Eliminates manual feature engineering by learning optimal representations directly from raw data. This reduces development time and often discovers features human experts wouldn't identify.

**Superior Performance**Achieves state-of-the-art results on complex tasks like image recognition, speech processing, and natural language understanding. Performance often improves with more data and larger models.

**Scalability**Benefits from increased data volumes and computational resources. Larger models trained on more data generally achieve better performance, following empirical scaling laws.

**Versatility**Handles diverse data types including images, text, audio, video, time series, and structured data. Single models can process multiple modalities simultaneously (multimodal learning).

**End-to-End Learning**Maps inputs directly to outputs without requiring intermediate processing steps or hand-crafted pipelines. Simplifies system design and optimization.

**Transfer Learning**Pre-trained models can be fine-tuned for new tasks with limited data. Reduces training time and data requirements for specialized applications.

**Continuous Improvement**Models improve as more data becomes available and computational resources increase. Systems can be updated with new knowledge without complete retraining.

## Challenges and Limitations

Despite impressive capabilities, deep learning faces significant challenges:

**Large Data Requirements**Training effective deep learning models typically requires thousands to millions of labeled examples. Acquiring and labeling large datasets is expensive and time-consuming. Some domains (medical imaging, rare events) inherently have limited data availability.

**Computational Demands**Training large models requires expensive specialized hardware (GPUs, TPUs) and substantial energy consumption. Training times can range from hours to weeks or months. Inference costs for deployed models can be significant at scale.

**Black Box Nature**Deep neural networks operate as "black boxes" with limited interpretability. Understanding why a model makes specific predictions proves challenging, particularly for networks with millions of parameters. This opacity raises concerns in high-stakes applications like healthcare and criminal justice.

**Overfitting Risk**Models may memorize training data rather than learning generalizable patterns, resulting in poor performance on new data. Requires careful regularization, validation strategies, and monitoring.

**Adversarial Vulnerability**Small, carefully crafted perturbations to inputs can cause dramatic misclassifications. This vulnerability raises security concerns for deployed systems.

**Bias and Fairness**Models learn and amplify biases present in training data. Can produce discriminatory outcomes when trained on biased datasets or when certain groups are underrepresented.

**Limited Reasoning**Current deep learning excels at pattern recognition but struggles with logical reasoning, common-sense understanding, and causal inference. Models lack genuine understanding of concepts they manipulate.

**Brittleness**Models trained for specific tasks perform poorly when conditions change. Lack the robustness and adaptability of human intelligence.

**Resource Constraints**Deploying large models on resource-constrained devices (smartphones, IoT devices) requires model compression techniques and hardware optimization.

## Best Practices for Deep Learning Projects

Successfully implementing deep learning requires attention to several key practices:

**Data Preparation**Collect diverse, representative training data. Implement robust data augmentation to increase effective dataset size. Carefully split data into training, validation, and test sets. Address class imbalance issues.

**Model Selection**Start with proven architectures appropriate for your task. Consider transfer learning from pre-trained models. Balance model complexity with available data and computational resources.

**Training Strategies**Use appropriate loss functions and optimization algorithms. Implement early stopping to prevent overfitting. Monitor training and validation metrics closely. Use techniques like learning rate scheduling and gradient clipping.

**Regularization**Apply dropout, weight decay, or other regularization techniques to prevent overfitting. Use data augmentation to increase training set diversity. Implement batch normalization for training stability.

**Validation and Testing**Maintain strictly separated validation and test sets. Use cross-validation for small datasets. Test models on diverse real-world examples beyond the test set.

**Deployment Considerations**Optimize models for inference speed and resource efficiency. Implement monitoring for model performance in production. Plan for model updates and retraining. Consider edge cases and failure modes.

**Ethical Considerations**Test for biases across demographic groups. Implement fairness metrics and constraints. Provide appropriate documentation and transparency. Consider societal impacts of deployments.

## Frequently Asked Questions

**What is the difference between deep learning and machine learning?**Machine learning encompasses all algorithms that learn from data. Deep learning is a subset using neural networks with multiple layers. Deep learning automatically learns features from raw data, while traditional machine learning often requires manual feature engineering.

**How much data do I need for deep learning?**Requirements vary by task complexity and model size. Simple tasks might need thousands of examples, while complex tasks often require millions. Transfer learning can reduce data requirements by leveraging pre-trained models.

**Why is deep learning called "deep"?**The "deep" refers to the multiple layers of processing in the neural network. More layers enable learning of more abstract and complex representations.

**Can deep learning models explain their decisions?**Standard deep learning models have limited interpretability. Research into explainable AI aims to make models more transparent, but fundamental trade-offs exist between performance and interpretability.

**Do I need GPUs for deep learning?**GPUs dramatically accelerate training and enable working with larger models. While CPUs can train small models, GPUs are practically essential for serious deep learning work. Cloud services provide GPU access without hardware investment.

**How long does it take to train a deep learning model?**Training time varies from minutes to weeks depending on model size, dataset size, hardware, and task complexity. Small models on modest datasets train in hours. Large language models require weeks on massive GPU clusters.

**Is deep learning better than traditional machine learning?**Deep learning excels when large datasets are available and automatic feature learning is beneficial (images, speech, text). Traditional machine learning often performs better on small structured datasets where interpretability matters. The best approach depends on the specific problem, data availability, and requirements.

## References


1. AWS. (n.d.). What is Deep Learning?. URL: https://aws.amazon.com/what-is/deep-learning/

2. GeeksforGeeks. (n.d.). Introduction to Deep Learning. URL: https://www.geeksforgeeks.org/deep-learning/introduction-deep-learning/

3. Analytics Vidhya. (2020). 12 Types of Neural Networks. URL: https://www.analyticsvidhya.com/blog/2020/02/cnn-vs-rnn-vs-mlp-analyzing-3-types-of-neural-networks-in-deep-learning/

4. TechTarget. (n.d.). What is Deep Learning?. URL: https://www.techtarget.com/searchenterpriseai/definition/deep-learning

5. Columbia University. (n.d.). AI vs. Machine Learning. URL: https://datascience.columbia.edu/about-us/news/artificial-intelligence-ai-vs-machine-learning/

6. GeeksforGeeks. (n.d.). Neural Networks Guide. URL: https://www.geeksforgeeks.org/machine-learning/neural-networks-a-beginners-guide/

7. Analytics Vidhya. (2020). How Neural Networks Work. URL: https://www.analyticsvidhya.com/blog/2020/02/cnn-vs-rnn-vs-mlp-analyzing-3-types-of-neural-networks-in-deep-learning/

8. Analytics Vidhya. (2021). Perceptron. URL: https://www.analyticsvidhya.com/blog/2021/10/perceptron-building-block-of-artificial-neural-network/

9. Analytics Vidhya. (2022). CNN Basics. URL: https://www.analyticsvidhya.com/blog/2022/03/basics-of-cnn-in-deep-learning/

10. GeeksforGeeks. (n.d.). Convolutional Neural Networks. URL: https://www.geeksforgeeks.org/machine-learning/introduction-convolution-neural-network/

11. Analytics Vidhya. (2022). RNNs Overview. URL: https://www.analyticsvidhya.com/blog/2022/03/a-brief-overview-of-recurrent-neural-networks-rnn/

12. GeeksforGeeks. (n.d.). Recurrent Neural Networks. URL: https://www.geeksforgeeks.org/machine-learning/introduction-to-recurrent-neural-network/

13. Analytics Vidhya. (2021). LSTM Introduction. URL: https://www.analyticsvidhya.com/blog/2021/03/introduction-to-long-short-term-memory-lstm/

14. Analytics Vidhya. (2024). Understanding Transformers. URL: https://www.analyticsvidhya.com/blog/2024/04/understanding-transformers-a-deep-dive-into-nlps-core-technology/

15. GeeksforGeeks. (n.d.). Getting Started with Transformers. URL: https://www.geeksforgeeks.org/machine-learning/getting-started-with-transformers/

16. GeeksforGeeks. (n.d.). Auto-Encoders. URL: https://www.geeksforgeeks.org/machine-learning/auto-encoders/

17. GeeksforGeeks. (n.d.). Generative Adversarial Networks. URL: https://www.geeksforgeeks.org/deep-learning/generative-adversarial-network-gan/

18. Wikipedia. (n.d.). Types of Artificial Neural Networks. URL: https://en.wikipedia.org/wiki/Types_of_artificial_neural_networks

19. IBM. (n.d.). What is Deep Learning?. URL: https://www.ibm.com/topics/deep-learning
