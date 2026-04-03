---
title: Model Serving
date: 2025-12-19
lastmod: 2026-04-02
translationKey: Model-Serving
description: Model serving is the technology for providing trained AI models in a usable state to applications and continuously processing prediction requests. It's essential for production operation.
keywords:
- Model serving
- Model deployment
- Real-time predictions
- Batch processing
- API
category: AI & Machine Learning
type: glossary
draft: false
url: /en/glossary/Model-Serving/
---

## What is Model Serving?

**Model serving is the process of providing trained AI models in a usable state to applications and continuously processing prediction requests.** It aims to efficiently execute and scale models from development to production.

> **In a nutshell:** Like a kitchen completing dishes and a waiter delivering them to customers—models need an efficient delivery mechanism.

**Key points:**

- **What it does:** Make AI models available for applications to use
- **Why it's needed:** Integrate model predictions into business systems
- **Who uses it:** MLOps engineers, backend developers, infrastructure engineers

## Why it matters

Great models become worthless if production can't execute them efficiently. Multi-second predictions frustrate users who abandon applications. Model serving creates fast prediction returns.

Scalability is equally important. Peak traffic brings thousands of requests per second. Serving frameworks must handle this efficiently.

## How it works

Model serving has several approaches:

**Real-time APIs** respond immediately to user requests. REST APIs or gRPC implementations demand millisecond-level latency. TensorFlow Serving, KServe, and Seldon are popular frameworks.

**Batch processing** handles large data sets together. Useful when immediate responses aren't required (daily sales reports). Simpler to implement with good computational efficiency.

**Streaming** processes continuous data streams. Used for real-time analytics, often combined with systems like Kafka.

**Edge serving** runs models on smartphones and IoT devices. TensorFlow Lite and ONNX Runtime are common.

Serving frameworks manage multiple model versions, A/B testing, auto-scaling, health checks, and logging.

## Real-world use cases

**E-commerce recommendations** — Return recommendations in tens of milliseconds when users view pages. Fast serving is essential.

**Real-time fraud detection** — Return fraud judgments instantly during credit card transactions. Even slight delays matter.

**Chatbots** — Return answers within seconds. Chains multiple models (text processing, response generation).

## Benefits and considerations

**Benefits** — Fast predictions, scalability, efficient multi-model management, A/B testing support.

**Considerations** — Framework selection, setup, and operational costs. Model version management becomes complex.

## Related terms

- **[Model Deployment](Model-Deployment.md)** — Entire process leading to serving
- **[API Design](API-Design.md)** — Foundation for real-time serving
- **[Caching](Caching.md)** — Serving performance optimization
- **[Load Balancing](Load-Balancing.md)** — Scalability realization
- **[A/B Testing](AB-Testing.md)** — Model comparison in serving environments

## Frequently asked questions

**Q: What's the difference between serving and deployment?**
A: Deployment asks "how do we get models to production?" Serving asks "how do we efficiently keep them running?" Serving is the main job after deployment.

**Q: When to use real-time vs. batch?**
A: Use real-time if users wait (web apps, chatbots). Use batch if they don't (report generation, recommendation emails).

**Q: What's the main bottleneck?**
A: Usually I/O and networking, not model inference itself. Optimize with caching, batching, and async processing.
