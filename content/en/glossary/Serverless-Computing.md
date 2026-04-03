---
title: Serverless Computing
translationKey: serverless-computing
description: Serverless computing is an execution model where infrastructure management is delegated to cloud providers, allowing developers to focus on code.
keywords:
- serverless computing
- cloud computing
- FaaS
- AWS Lambda
- event-driven
category: Cloud & Infrastructure
type: glossary
date: 2026-04-02
lastmod: 2026-04-02
draft: false
url: "/en/glossary/Serverless-Computing/"
---

## What is Serverless Computing?

**Serverless computing is a cloud execution model where the cloud provider handles all server management, allowing developers to focus on code execution.** Physical servers exist in the background, but developers don't need to be aware of them. Despite the name, servers don't "not exist"—rather, their management is "invisible."

> **In a nutshell:** Computing where you use only what you need and pay only for what you use, like water or electricity.

**Key points:**

- **What it does:** Executes functions in response to events and automatically scales
- **Why it's needed:** Eliminates infrastructure management complexity and increases development speed
- **Who uses it:** Startups to large enterprises, IoT, data processing, and many other use cases

## Why it matters

Traditional server management is complex and costly. Provisioning, scaling, patching, and backing up servers consumed time beyond development itself. With serverless models, all of this is automated.

Furthermore, pay-as-you-go pricing means you only pay for actual usage. With zero idle costs, unpredictable traffic fluctuations are easier to handle.

## How it works

Serverless architecture operates on an event-driven model. When users send requests, those events trigger function execution.

**Execution flow:** HTTP request arrives → cloud provider automatically starts container → executes function → returns result → unused containers stop

Multiple [FaaS (Function as a Service)](FaaS.md) platforms exist, such as [AWS Lambda](AWS-Lambda.md) and Google Cloud Functions. These can process millions of requests simultaneously with minimal latency.

## Real-world use cases

**Automated image processing**
When files are uploaded to S3, functions automatically start to generate and optimize thumbnails.

**Real-time data processing**
IoT device data is received via [Kafka](Kafka.md) and real-time analysis is executed by serverless functions.

**Web API backend**
Multiple serverless functions are exposed via API Gateway to build a scalable backend.

## Benefits and considerations

**Benefits:** Low cost, zero operational burden, automatic scaling, and fast deployment.

**Considerations:** "Cold start" latency can occur on first execution. Additionally, vendor lock-in risks exist and execution time limits apply. It's not suitable for long-running or complex workflows.

## Related terms

- **[Cloud Computing](Cloud-Computing.md)** — parent concept of serverless
- **[FaaS](FaaS.md)** — function-based execution model
- **[AWS Lambda](AWS-Lambda.md)** — representative serverless platform
- **[Microservices](Microservices.md)** — often implemented with serverless
- **[Auto-Scaling](Auto-Scaling.md)** — key feature of serverless

## Frequently asked questions

**Q: Is it really okay to not manage servers?**
A: Yes. Security patches and scaling are all handled by the provider. You can focus on function code.

**Q: Can it be used for all processing?**
A: It's designed for short-duration processing. Complex image processing or time-consuming tasks are better served by other models.
