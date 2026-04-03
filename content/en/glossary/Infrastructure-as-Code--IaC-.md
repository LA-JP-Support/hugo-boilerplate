---
title: Infrastructure as Code (IaC)
date: 2025-12-19
lastmod: 2026-04-02
translationKey: infrastructure-as-code-iac
description: Infrastructure as Code (IaC) is a method of defining and managing IT infrastructure through code, enabling automation and reproducibility for efficient cloud operations.
keywords:
- Infrastructure as Code
- IaC
- DevOps
- automation
- cloud infrastructure
category: Cloud & Infrastructure
type: glossary
draft: false
url: /en/glossary/infrastructure-as-code--iac-/
---

## What is Infrastructure as Code (IaC)?

**Infrastructure as Code (IaC) is the practice of defining and managing IT infrastructure—servers, networks, and databases—through code files rather than manual commands.** Traditionally, network engineers manually stood up servers and configured firewalls. IaC expresses the entire process as "code," which tools then automatically execute, eliminating human error and ensuring repeatable results every time.

> **In a nutshell:** Write infrastructure design as code and have machines automatically execute it.

**Key points:**

- **What it does:** Defines infrastructure resources (servers, DBs, networks) in text code and auto-deploys
- **Why it matters:** Eliminates manual work, ensures reproducibility, enables version control, automates scaling
- **Primary users:** DevOps engineers, cloud architects, infrastructure operators

## Why it matters

In the cloud era, infrastructure resource demands change rapidly. Scaling hundreds of servers in minutes during traffic spikes, then reducing during low traffic—human labor can't handle this. With IaC, complex infrastructure can be built or destroyed in seconds.

Reproducibility is critically important. Development environments often differ from production, causing problems. With IaC, both environments are built from identical code, preventing environment-difference bugs.

Furthermore, changes can be tracked in version control systems like Git. "Who changed what, when, and why" is all logged. Production incidents can be quickly traced to their cause, enabling rapid rollbacks if needed. From a security compliance perspective, infrastructure change audit trails are invaluable.

## How it works

IaC comes in two main approaches: **declarative** and **imperative**. Declarative (Terraform, CloudFormation) expresses desired end-state, and tools determine how to reach it. Imperative (Bash, Ansible) explicitly describes step-by-step procedures. Modern practice favors declarative approaches because they offer superior reproducibility, maintainability, and idempotency (same command run multiple times yields identical results).

Example Terraform code:
```
resource "aws_instance" "web" {
  ami           = "ami-123"
  instance_type = "t2.micro"
}
```

Running `terraform apply` auto-creates the specified AWS instance. Modifying configuration and re-running only updates differences.

Major tools include Terraform (multi-cloud), AWS CloudFormation, Google Cloud Deployment Manager, Azure Resource Manager (cloud-vendor-specific), Ansible, and Chef (configuration management). Large systems combine these, incrementally building infrastructure.

## Real-world use cases

**Startup Scaling**
Early stages work with small servers; as user volume grows, auto-scaling configurations are added to IaC code, automatically responding to traffic increases.

**Multi-Cloud Strategy**
Using both AWS and GCP? Terraform's common code manages both, preventing vendor lock-in.

**CI/CD Pipeline Automation**
Code changes trigger auto test environment construction, test execution, and production deployment—all automated through IaC.

**Disaster Recovery**
When primary regions fail, re-running IaC in alternate regions reconstructs complete infrastructure in minutes.

**Development and Production Environment Alignment**
Teams build with identical IaC code, eliminating environment-based issues.

## Benefits and considerations

IaC's greatest merit is infrastructure automation and consistency. However, the learning curve is steep. Teams need significant time and training to understand IaC concepts, tools, and best practices.

State management becomes complex. Terraform's state files record resource current states. Corrupting or losing state files can be catastrophic. Proper backup and centralized state file management are essential.

Infrastructure drift (manual changes outside IaC) creates inconsistency between code and reality, causing mysterious production-only failures. Regular drift detection and correction are crucial.

## Related terms

- **[DevOps](DevOps.md)** — IaC is DevOps culture's technical foundation
- **[CI/CD](CI-CD.md)** — Combined with IaC, enables complete automated deployment
- **[Cloud Computing](Cloud-Computing.md)** — IaC reaches peak value in the cloud era
- **[Version Control](Version-Control.md)** — IaC code is version-controlled via Git
- **[Agile Development](Agile-Development.md)** — IaC enables development cycle acceleration

## Frequently asked questions

**Q: Can legacy systems be IaC-ified?**
A: Yes, but phased approach is advised. Start with new resources, gradually migrate existing ones—this is more practical.

**Q: What investment does IaC adoption require?**
A: Initial learning costs are high, but most cases achieve ROI in 6-12 months. Frequently-scaled systems show particularly striking benefits.

**Q: Are some infrastructure elements unmanageable through IaC?**
A: Physical servers, hardware configurations, and some legacy cloud services lack IaC support. Manual management or wrapper tools may be necessary.
