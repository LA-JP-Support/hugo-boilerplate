---
title: GitOps
date: 2025-12-19
lastmod: 2026-04-02
translationKey: gitops
description: GitOps is an operational framework that uses Git as the single source of truth and manages all infrastructure and application configurations through code, enabling safe and auditable automated deployments.
keywords:
- GitOps
- DevOps
- Infrastructure as Code
- Kubernetes
- Automated Deployment
category: Cloud & Infrastructure
type: glossary
draft: false
url: /en/glossary/gitops/
---

## What is GitOps?

**GitOps is an operational framework that uses Git repositories as the single source of truth and manages all infrastructure and application configurations declaratively.** Desired states are coded and stored in Git, and automatic tools (Argo CD, Flux, etc.) automatically adjust the current state to match the desired state.

> **In a nutshell:** GitOps is an approach to managing infrastructure "through Git pull requests." No direct SSH login is required.

**Key points:**

- **What it does:** Manage infrastructure configurations in Git and automatically reflect them in production environments
- **Why it's needed:** Safe change management, complete audit logs, rapid rollback, elimination of human error
- **Who uses it:** Organizations running Kubernetes, DevOps teams, microservices companies

## Why it matters

Traditionally, DevOps engineers directly logged into production servers via SSH to make configuration changes. This caused **drift** (deviation from desired state), making it difficult to identify failure causes. GitOps records the "desired state" in Git, ensuring environments always match Git. When problems occur, recovery is just reverting Git.

With complex infrastructure like Kubernetes, GitOps is practically essential to manage it.

## How it works

The GitOps workflow is simple:

**1. Define:** Write "I want to run 3 replicas" in Kubernetes manifest or Terraform and store in Git.

**2. Propose:** Suggest changes through pull request. Other team members review and approve.

**3. Merge:** When merged to main branch, automatically applies to production environment.

**4. Monitor:** GitOps agent (Argo CD, etc.) constantly compares Git state with current environment. Automatically fixes any drift.

This process ensures all change history is completely recorded in Git, making it clear "who changed what when." Security and compliance requirements are automatically satisfied.

## Real-world use cases

**Multi-cluster management**

Centrally manage multiple environments (AWS, Azure, on-premises) in one Git repository. Ensures consistency across environments.

**Production environment rollback**

Problem occurs → Revert previous commit in Git → Environment automatically recovers. Completes in seconds.

**Automated environment provisioning**

Need new staging environment → Create Git branch → Merge PR → Auto-construction complete. No manual work.

**Security policy enforcement**

Define Pod security policies and network policies in Git. Changes are reviewed and approved via PR before deployment.

## Benefits and considerations

GitOps's greatest advantage is **safety and visibility**. All changes are recorded in Git and visible to everyone. Additionally, **rollback is easy**. Simply revert Git when problems occur. Further, **human error decreases** and security vulnerabilities can be detected during PR review.

The challenge is **secret management complexity**. Database passwords can't be stored in Git, requiring Sealed Secrets or HashiCorp Vault. Also, **Git-only dependency risk** means if the Git server fails, environment changes become impossible. Backup and recovery plans are necessary.

## Related terms

- **[Infrastructure as Code](Infrastructure-as-Code.md)** — Philosophy of managing infrastructure through code. Foundation of GitOps
- **[Kubernetes](Kubernetes.md)** — Container orchestration where GitOps excels most
- **[CI/CD](CI-CD.md)** — GitOps is the evolution of CD (continuous deployment)
- **[Argo CD](Argo-CD.md)** — Most popular GitOps tool for Kubernetes
- **[DevOps](DevOps.md)** — Integration of development and operations. GitOps is its implementation method

## Frequently asked questions

**Q: What's the difference between GitOps and DevOps?**
A: DevOps is a general term for culture and automation. GitOps is a specific methodology and tool set using "Git as the single source of truth." GitOps is a means of implementing DevOps.

**Q: If a Pod is accidentally deleted, will GitOps recover it?**
A: Yes. Argo CD constantly monitors and automatically fixes any state differing from Git definition.

**Q: What if I directly SSH into a server and change configuration?**
A: That causes Git definition and environment to diverge, losing GitOps benefits. Basically prohibited. All changes should go through Git.
