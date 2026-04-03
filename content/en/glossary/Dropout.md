---
title: Dropout
date: 2025-12-19
lastmod: 2026-04-02
translationKey: Dropout
description: Dropout is a regularization technique in neural networks that randomly deactivates neurons during training to prevent overfitting and improve model generalization.
keywords:
- dropout regularization
- neural network overfitting
- machine learning techniques
- deep learning optimization
- model generalization
category: AI & Machine Learning
type: glossary
draft: false
url: /en/glossary/dropout/
---

## What is Dropout?

**Dropout is a technique where a neural network randomly deactivates (sets to zero) a fraction of neurons during training.** This prevents overfitting—the problem where a model adapts too closely to training data—and improves its ability to generalize to new data. Proposed by Geoffrey Hinton in 2012, this technique has been transformative for deep learning. For example, complex models like [LLMs](Document-Loader.md) (large language models) become robust against both training data and unseen data when using dropout.

> **In a nutshell:** "During training, randomly 'turning off' neurons (like brain cells) prevents the model from memorizing training data too closely."

**Key points:**

- **What it does:** Randomly deactivates a portion of neurons during training
- **Why it's needed:** Prevents models from over-adapting to training data alone
- **Who uses it:** Deep learning engineers, data scientists, AI researchers

## Why it matters

Dropout is crucial because it addresses a fundamental challenge in neural networks. As networks grow more complex, they tend to "overfit"—adapting perfectly to training data while performing poorly on new data. Dropout prevents this. Additionally, dropout achieves the effect of training multiple models (ensemble learning) within a single model, reducing computational costs. Its effectiveness has been validated across all fields, from [image recognition](Dropout.md) to [natural language processing](Dropout.md).

## How it works

Dropout's mechanism is intuitive. During each training step, each neuron is "dropped" with probability p (typically 0.5)—its output is set to zero. The remaining neurons are rescaled by 1/(1-p) to maintain expected values. This process destroys "co-adaptation" between neurons—preventing the network from relying too heavily on specific neuron pairs.

At test time, all neurons are used, but outputs are adjusted to account for training-time scaling. This maintains consistency between training and inference.

## Real-world use cases

**Image classification models** When training on large datasets like ImageNet, applying dropout of 0.5 to hidden layers prevents overfitting.

**Text analysis** In training [LLMs](Document-Loader.md) and sentiment analysis models, dropout rates of 0.3–0.5 are applied to fully connected layers to reduce dependence on training data.

**Medical image diagnosis** For training robust models on limited medical imaging datasets, dropout is used aggressively.

## Benefits and considerations

**Benefits:** Training computation cost remains nearly unchanged. Implementation is straightforward and supported by nearly all deep learning frameworks. In most cases, model generalization performance improves by 5–15%.

**Considerations:** Excessive dropout (too high a probability) can impair the model's learning ability. Interactions with other regularization techniques like [batch normalization](Dropout.md) must be considered. Optimal dropout rates vary by layer, requiring hyperparameter tuning.

## Related terms

- **[Overfitting](Dropout.md)** — the primary problem dropout addresses
- **[Neural networks](Dropout.md)** — where dropout is applied
- **[Regularization](Dropout.md)** — dropout's classification
- **[Batch normalization](Dropout.md)** — a technique with similar effects
- **[Deep learning](Document-Loader.md)** — the field where dropout is applied

## Frequently asked questions

**Q: Should dropout be applied to all layers?**
A: No. Generally, the output layer is excluded. Hidden layers typically use 0.2–0.5.

**Q: Is a higher dropout rate always better?**
A: No. Above 0.5, models may fail to learn. Typically, 0.3–0.5 is optimal.

**Q: Should dropout be used during testing?**
A: No. During testing, dropout is disabled; only the training-time expected value scaling is applied.
