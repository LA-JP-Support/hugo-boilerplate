---
title: Kubernetes (K8s)
date: 2025-03-01
lastmod: 2026-04-02
translationKey: kubernetes-k8s
description: An orchestration platform for automatically managing and operating multiple containers across clusters.
keywords:
- Kubernetes
- K8s
- Container management
- Orchestration
- Cloud infrastructure
category: Cloud & Infrastructure
type: glossary
draft: false
url: /en/glossary/kubernetes-k8s/
---

## What is Kubernetes (K8s)?

**Kubernetes (K8s) is an orchestration platform for automatically managing and operating multiple [containers](Container.md) in a cluster (collection of multiple machines).** Developed by Google and currently managed by CNCF (Cloud Native Computing Foundation), it has become the de facto industry standard. It automates complex operational tasks including container startup, shutdown, restart, network connection, storage management, and load balancing, allowing developers to focus on application development.

> **In a nutshell:** Kubernetes is "the conductor of an orchestra," where multiple instruments (containers) automatically follow the conductor, timing their performances harmoniously.

**Key points:**

- **What it does:** Automatically manages multiple containers across multiple servers, performing scaling per load, failure recovery, rolling updates based on requirements
- **Why it's needed:** Manual operations are complex, low-quality, and expensive, but Kubernetes enables automation, robustness, and efficiency simultaneously
- **Who uses it:** DevOps engineers, SREs (Site Reliability Engineers), cloud infrastructure teams, companies building scalable systems

## Why it matters

[Container](Container.md) technology solved environment consistency from development to production, but manually managing multiple containers remains difficult. For systems with five web server containers and two database containers, manually scaling "increase web servers to 10" during traffic surges isn't realistic. Additionally, if one server crashes, "automatically restart on another machine," and when deploying new versions, "replace old containers sequentially without downtime" operations are impossible without automation.

Kubernetes automates all these tasks, dramatically reducing operational burden and human error. System reliability improves and feature release cycles shorten. Large tech companies like Netflix, Airbnb, and Uber safely execute massive daily deployments enabled by Kubernetes automation.

## How it works

Kubernetes architecture comprises "master nodes" and "worker nodes." Master nodes are Kubernetes' brain—receiving user instructions ("Launch 20 web server containers") and planning their realization. Worker nodes follow master instructions, actually starting and managing containers on server groups.

The smallest unit Kubernetes manages is the "Pod," containing one or more containers. Pods run together on the same machine, sharing network namespace, enabling localhost communication. Defining Pod collections as "Deployments" specifies replication requirements like "this application should always run with 5 Pods." Kubernetes controllers continuously compare "current state" to "desired state," automatically correcting differences.

Load balancing is realized through "Services." Configuring a Service with five running web server Pods distributes incoming requests equally among all five. If a Pod fails, Deployment automatically starts a new Pod and Service begins distributing to it, avoiding downtime.

Scaling is automated through "HPA (Horizontal Pod Autoscaler)." Defining rules like "increase Pod count when CPU exceeds 80%" enables automatic scaling during traffic spikes. Updates use "rolling updates," sequentially replacing old Pods with new ones, enabling new version deployment without service stoppage.

## Real-world use cases

**Microservices infrastructure construction**

Financial institutions and e-commerce companies operate tens to hundreds of microservices. Each service runs in independent Pods with Kubernetes automatically managing them, efficiently operating the whole while managing inter-service dependencies.

**Automatic traffic fluctuation response**

Consider e-commerce sale events with 10x traffic increases. Kubernetes auto-scaling detects load and launches additional Pods in seconds, handling the surge without service stoppage. Post-event, Pods automatically reduce as load decreases.

**Safe deployment through rolling updates**

Organizations requiring multiple daily deployments can continuously replace old versions with new through Kubernetes rolling updates, maintaining service continuity.

## Benefits and considerations

Kubernetes' greatest merit is "automation." Scaling, failure recovery, rolling updates, and resource optimization happen automatically, dramatically reducing operations engineer burden while improving reliability. Supporting different cloud providers prevents vendor lock-in, enabling same platforms for both on-premises and cloud. Multiple teams sharing Kubernetes clusters improve resource efficiency.

Conversely, Kubernetes has a steep learning curve. Numerous concepts (Pod, Deployment, Service, Ingress) and complex configuration require substantial engineering time and operations knowledge. Kubernetes cluster management itself (version updates, security patches) creates overhead. Small, simple systems may experience unnecessary complexity, and managed services (EKS, GKE) still incur significant costs.

## Related terms

- **[Container](Container.md)** — Container technology managed by Kubernetes
- **[Docker](Docker.md)** — Container image creation/execution tool, standard combination with Kubernetes
- **[Microservices](Microservices.md)** — Splitting systems into small services architecture with Kubernetes as ideal implementation platform
- **[DevOps](DevOps.md)** — Development and operations integration concept, significantly advanced by Kubernetes
- **[Infrastructure as Code (IaC)](Infrastructure-as-Code.md)** — Infrastructure definition as code, exemplified by Kubernetes manifest files

## Frequently asked questions

**Q: What should be done before Kubernetes adoption?**

A: First, [containerized](Container.md) applications and basic Docker understanding are essential. Additionally, microservices architecture migration is often a prerequisite, making current architecture evaluation important. Small teams should consider managed services like AWS EKS, Google GKE, or Azure AKS rather than complete self-management.

**Q: Is Kubernetes necessary for small applications (few containers)?**

A: Not essential. Complexity increases without commensurate benefits. For simple few-container operations, simpler platforms like Docker Compose or Heroku suffice. Kubernetes delivers value with multiple teams, multiple services, and complex operational requirements.

**Q: What skills are required to become a Kubernetes cluster administrator?**

A: Broad IT infrastructure knowledge including Linux system administration, networking, storage, and security is necessary. Kubernetes-specific concepts (resource definition, RBAC, network policies) must also be learned. Using managed services like AWS or Google Cloud automates cluster management itself, enabling focus on application layers.
