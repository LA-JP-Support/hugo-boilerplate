---
title: Docker
date: 2025-12-19
lastmod: 2026-04-02
translationKey: docker
description: Docker is an open-source platform that packages applications into isolated environments called containers, enabling them to operate identically across any environment.
keywords:
- Docker
- Containers
- Containerization
- Microservices
- Kubernetes
category: Cloud & Infrastructure
type: glossary
draft: false
url: /en/glossary/docker/
---

## What is Docker?

**Docker is an open-source platform that packages applications into small isolated boxes called containers, enabling them to operate identically on any computer.** Traditionally, "works in development but not in production" problems plagued teams. Docker solves this by packaging all dependencies into containers, so development machines, servers, and clouds all run identically.

> **In a nutshell:** A box containing everything applications need (code, libraries, configuration) that runs identically everywhere.

**Key points:**

- **What it does:** Packages applications and dependencies together
- **Why it matters:** Eliminates environment inconsistencies; simplifies deployment
- **Who uses it:** Software companies, development teams, DevOps engineers

## Why it matters

Docker matters for three reasons. First, application development accelerates—environments taking hours to set up now take seconds. Second, [cloud](Kubernetes.md) operations simplify; scaling becomes easy. Third, it enables microservices architecture, running multiple small applications independently.

## How it works

Docker operations resemble cooking recipes. A Dockerfile text file contains recipes: "Start from this OS, install these libraries, copy this code, launch with this command." This recipe creates "images"—templates. Finally, images launch "containers"—running instances.

Crucially, in [microservices](Kubernetes.md) scenarios, each service runs in independent containers, enabling separate updates, scaling, and stopping.

## Real-world use cases

**Web application development** Using identical containers in development and production prevents "works in my environment" problems.

**Continuous deployment** CI/CD pipelines automate testing and deployment, maintaining code quality while releasing rapidly.

**Microservices** Multiple small applications (frontend, API, database) operate in separate containers.

## Benefits and considerations

**Benefits:** Identical development and production environments reduce bugs. Simple setup enables new team members fast starts. Efficient resource use—more applications per physical machine.

**Considerations:** Docker mastery requires learning time. Incorrect security settings risk container processes affecting others. Storage and [network](Kubernetes.md) management complexity increases.

## Related terms

- **[Kubernetes](Kubernetes.md)** — Container orchestration tool managing Docker at scale
- **[Images](Document-Loader.md)** — Container template file sets
- **[Registry](Duplicate-Content.md)** — Image storage and distribution
- **[Containerization](Docker.md)** — Process of converting applications to containers
- **[Microservices](Drupal.md)** — Combinations of multiple small services

## Frequently asked questions

**Q: What's the difference between Docker and virtual machines?**
A: Docker shares OS kernels—lightweight and fast. Virtual machines copy entire OSs—heavy resource use.

**Q: What should beginners do first?**
A: Study Docker's official tutorials, learning basic commands (run, build, push).

**Q: My container won't start. What do I check?**
A: Dockerfile syntax errors, missing files, port conflicts. Logs are critical.
