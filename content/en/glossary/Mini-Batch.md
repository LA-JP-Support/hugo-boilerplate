---
title: Mini-Batch
date: 2025-12-19
lastmod: 2026-04-02
translationKey: Mini-Batch
description: An optimization technique used in machine learning that divides training data into small groups to process sequentially when training neural networks.
keywords:
- mini-batch processing
- batch gradient descent
- machine learning optimization
- neural network training
- deep learning
category: AI & Machine Learning
type: glossary
draft: false
url: /en/glossary/Mini-Batch/
---

## What is Mini-Batch?

**Mini-batch is a technique in neural network training where the entire dataset is not processed at once, but is instead divided into small subsets (typically 16-512 samples) and processed incrementally.** Even with large datasets, this approach allows efficient training with limited memory while maintaining stable learning—an essential technique in modern deep learning.

> **In a nutshell:** It's like counting all products in a supermarket not all at once, but aisle by aisle.

**Key points:**

- **What it does:** Divides training data into smaller chunks and updates model weights progressively
- **Why it's needed:** Reduces memory usage and balances computational efficiency with learning stability
- **Who uses it:** Researchers and developers training deep learning models

## Why it matters

Without mini-batch processing, training large-scale neural networks would be impractical. For example, loading a million images all at once into memory typically causes GPU memory exhaustion. Using mini-batches allows you to leverage the parallel processing power of GPUs or TPUs while learning from all data progressively.

Additionally, the noise introduced by mini-batches helps the model escape local minima, making optimization easier. This means training becomes more stable and efficient compared to updating with the entire dataset just once.

## How it works

Mini-batch training repeats through these steps:

1. **Data division** - Split the training dataset into equally-sized mini-batches
2. **Forward pass** - Pass the mini-batch through the model to compute predictions
3. **Loss calculation** - Compute the error between predictions and ground truth
4. **Backward pass** - Calculate gradients based on that error to update model weights
5. **Weight update** - Adjust model weights slightly using the computed gradients
6. **Next batch** - Repeat this process for all mini-batches

Mini-batch size (the number of samples processed at once) is an important choice. If too small, training becomes unstable; if too large, you may run out of memory or lose computational efficiency. In practice, powers of two (32, 64, 128, etc.) are commonly used.

## Real-world use cases

**Training image recognition models**

When a data scientist trains a dog recognition model on a million dog photos, they cannot load all images into memory. Instead, with a mini-batch size of 64, each computation handles 64 images, and the entire dataset is learned through 15,600 update steps. Due to GPU parallelization, this is hundreds of times faster than training one sample at a time.

**Fine-tuning large language models**

When fine-tuning a large language model for a specific task, mini-batch processing allows learning from millions of text strings with limited memory. Gradient averaging stabilizes training and improves performance.

**Updating recommendation systems**

When updating recommendation algorithms from user behavior data, computing all user history at once is impractical. Processing mini-batches allows improving the model at near-real-time frequencies.

## Benefits and considerations

**Benefits:** Mini-batch processing enables training on large datasets with limited hardware resources, improving computational efficiency. Noise from batches provides a regularization effect that prevents overfitting, resulting in more generalizable models. Training progress can be monitored batch-by-batch, allowing early problem detection.

**Considerations:** Mini-batch size selection significantly impacts training success. The optimal size varies by model and dataset, typically requiring experimentation. When changing batch size, you must also adjust the learning rate. If batch variance is too small, training can become unstable.

## Related terms

- **[Stochastic Gradient Descent (SGD)](Stochastic-Gradient-Descent.md)** — Updates with mini-batch size 1, calculating gradients from each sample
- **[Batch Gradient Descent](Batch-Gradient-Descent.md)** — Computes gradients from the entire dataset and updates once
- **[Learning Rate](Learning-Rate.md)** — The multiplier determining how much to adjust weights based on mini-batch gradients
- **[Neural Network](Neural-Network.md)** — The base model trained with mini-batches
- **[GPU](GPU.md)** — Hardware that accelerates mini-batch parallel processing

## Frequently asked questions

**Q: Is a larger mini-batch size always better?**
A: Not necessarily. Larger sizes consume more memory and reduce regularization effects from noise. Smaller sizes cause training instability. Usually, you experiment in the 32-256 range to find the optimal size.

**Q: Should I change the learning rate when changing mini-batch size?**
A: Yes, generally important. Larger batch sizes produce more stable gradient estimates, allowing larger learning rates. The inverse also applies.

**Q: What do we call going through the entire dataset once?**
A: That's called one epoch. Training typically repeats for several to hundreds of epochs.
