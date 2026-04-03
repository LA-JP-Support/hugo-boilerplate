---
title: Model Compression
date: 2025-12-19
lastmod: 2026-04-02
translationKey: Model-Compression
description: Techniques that reduce machine learning model size while maintaining performance. Essential for deployment on mobile and edge devices.
keywords:
- model compression
- quantization
- pruning
- knowledge distillation
- edge AI
category: AI & Machine Learning
type: glossary
draft: false
url: /en/glossary/Model-Compression/
---

## What is Model Compression?

**Model compression is a set of techniques that reduce AI model size while maintaining prediction accuracy.** Modern AI models contain hundreds of billions to trillions of parameters, consuming massive memory and computational resources. Compression allows these models to run on resource-limited devices like smartphones and IoT equipment.

> **In a nutshell:** Like packing a suitcase full of books into a more compact space without losing the contents.

**Key points:**

- **What it does:** Reduces model size and computational requirements
- **Why it's needed:** To enable AI on mobile and edge devices
- **Who uses it:** ML engineers, embedded systems developers, mobile app developers

## Why it matters

Large language models and computer vision models work perfectly in the cloud but can't run on smartphones or edge devices. Compression enables powerful AI with low power consumption.

Energy efficiency matters too. Compressed models use less battery power, reducing data center operating costs. Plus, local processing protects privacy.

## How it works

Model compression uses four main techniques.

**Quantization** converts model parameters from 32-bit floating-point to 8-bit integers. Just as reducing photo color depth barely affects appearance, neural networks maintain accuracy with low-bit representation.

**Pruning** removes unimportant weights (connections). Like removing unused books from a library, it streamlines the network. Structured pruning removes entire neuron layers; unstructured pruning removes individual weights.

**Knowledge Distillation** transfers knowledge from a large "teacher model" to a small "student model." The student learns the teacher's prediction patterns and achieves similar accuracy despite being much smaller.

**Low-Rank Approximation** approximates complex calculations with simpler mathematics.

## Real-world use cases

**Smartphone image recognition** — Compressed computer vision models enable real-time object detection and face recognition on iPhones and Androids. Faster downloads and offline functionality.

**Autonomous vehicle perception** — Vehicles need millisecond decisions with limited compute. Compressed models enable low-latency, safe perception.

**IoT sensor devices** — Smart home and factory sensors often can't maintain internet connections. Compressed models run locally, sending only alerts to the cloud.

## Benefits and considerations

**Benefits** — Enables mobile deployment, reduces battery consumption, improves privacy (local processing), reduces latency.

**Considerations** — Compression may cause slight accuracy loss. Compressed models don't run optimally on all hardware. Quantization might speed up one processor but slow another.

## Related terms

- **Model Evaluation** — Methods for measuring performance before and after compression
- **Quantization** — The most common compression technique
- **Model Deployment** — Placing compressed models in production
- **Model Serving** — Efficiently running compressed models
- **Edge AI** — Running AI on edge devices

## Frequently asked questions

**Q: How much smaller do compressed models get?**
A: It varies. Quantization achieves 2–4x reduction, knowledge distillation can achieve 5–50x. You can adjust based on accuracy requirements.

**Q: Does compression always reduce accuracy?**
A: Some accuracy loss is nearly unavoidable, but proper techniques keep it negligible. You can often recover it through fine-tuning afterward.

**Q: Which compression technique should I choose?**
A: It depends. For smartphones, consider quantization. For extreme resource constraints needing high accuracy, try knowledge distillation. For general optimization, consider pruning.
