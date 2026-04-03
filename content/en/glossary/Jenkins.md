---
title: Jenkins
date: 2025-03-01
lastmod: 2026-04-02
description: An open-source CI/CD automation server that automatically executes code testing and deployment.
translationKey: jenkins
category: Knowledge & Collaboration
type: glossary
draft: false
url: /en/glossary/jenkins/
keywords:
  - Jenkins
  - CI/CD
  - automated testing
  - continuous integration
  - deployment automation
---

## What is Jenkins?

**Jenkins is an open-source CI/CD server that automates software development build, test, and deployment processes.** When developers submit code to a repository, it automatically executes tests, and if there are no problems, it can automatically deploy to production. With over 2,000 plugins, it integrates with numerous tools and is used widely from enterprises to personal projects.

> **In a nutshell:** Jenkins is an "automated factory" that automatically performs "run tests → quality checks → production release" whenever code changes occur.

**Key points:**

- **What it does:** Detects code changes and automatically executes build, test, and deploy
- **Why it's needed:** Prevents mistakes from manual testing/release and enables frequent updates safely
- **Who uses it:** DevOps engineers, software development teams, system administrators

## Why it matters

Traditionally in software development, developers wrote code, separate testers manually tested, and then release staff deployed to servers. This process was time-consuming and error-prone. With CI/CD tools like Jenkins, this entire workflow is automated. As a result, "adding new features to production multiple times daily" became possible, strengthening competitive advantage. Also, bugs are detected before reaching production, directly improving quality.

## How it works

Jenkins starts operation through "triggers"—the most common being "code updates to GitLab or GitHub." When developers submit code, Jenkins detects it and automatically executes a series of processes called a **Job** (job).

Job content is defined in configuration files, typically consisting of these steps: First, download the latest code from the repository. Next, **build** (compile and package) to make it executable. Then, **automated testing** verifies the code works as expected. If tests pass, **deployment** places the code in staging or production environments.

Jenkins records each step's results and notifies developers if problems occur. If tests fail, auto-deploy stops and production remains protected until developers fix it. This prevents "buggy code entering production"—the worst-case scenario.

Jenkins also has **distributed build capabilities**, executing multiple processes in parallel on multiple machines for high-speed processing even for large projects.

## Real-world use cases

**Startups requiring rapid development cycles** build Jenkins auto-release pipelines so features developed in the morning are in production by afternoon. Only code passing tests enters production, maintaining quality while releasing fast.

**Microservices environment batch updates** simultaneously test and deploy to multiple services. Even when services depend on each other, Jenkins executes updates in correct order, maintaining overall application integrity.

**Large-scale scheduled regular testing** automatically runs regression tests (checking past bugs haven't returned) nightly, with result reports delivered to the development team by morning. Quality is maintained without human effort.

## Benefits and considerations

Jenkins's greatest benefit is flexibility and extensibility. Over 2,000 plugins enable integration with almost all development tools with high customization freedom. Being open-source and free reduces adoption costs. Extensive use cases and knowledge from enterprises to individuals provide abundant expertise.

However, setup and maintenance require technical knowledge. With many plugins, choosing which ones is difficult. Outdated configuration methods exist, making learning resources fragmented. Some criticize the UI as complex, creating high barriers for beginners.

## Related terms

- **[GitLab](GitLab.md)** — Code management platform that triggers Jenkins execution. Can be used alongside GitLab CI
- **[Ansible](Ansible.md)** — After test execution in Jenkins, Ansible automates production server deployment
- **[Infrastructure as Code (IaC)](Infrastructure-as-Code--IaC-/)** — Jenkins runs IaC scripts to create/modify infrastructure
- **[API (Application Programming Interface)](APIs/)** — Jenkins REST API enables external tool control of jobs
- **[Microservices](Microservices/)** — Jenkins independently builds, tests, and deploys each microservice

## Frequently asked questions

**Q: Should I choose GitLab CI or Jenkins?**
A: GitLab CI has a gentler learning curve if you already use GitLab. Large customization needs or multiple tool integrations favor flexible Jenkins.

**Q: Self-hosted or cloud version?**
A: Self-hosted (on-premises) suits high security requirements. Cloud versions (CloudBees, etc.) reduce initial setup effort.

**Q: What happens when tests fail?**
A: Jenkins notifies developers via email/Slack and displays failure on dashboards. Auto-deploy stops, so production remains safe until developers fix it.
