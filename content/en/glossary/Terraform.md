---
title: Terraform
date: 2025-03-01
lastmod: 2026-04-02
description: HashiCorp's Infrastructure-as-Code tool that defines and manages cloud resources across multiple providers using code.
translationKey: Terraform
category: Knowledge & Collaboration
type: glossary
draft: false
url: /en/glossary/Terraform/
keywords:
- Terraform
- Infrastructure
- IaC
- HashiCorp
---

## What is Terraform?

**Terraform is an Infrastructure-as-Code (IaC) tool developed by HashiCorp that allows you to define and manage resources (servers, networks, storage) across multiple cloud providers like AWS, Azure, and GCP using a unified code language.** Using Terraform's dedicated "HCL (HashiCorp Configuration Language)," you write your infrastructure configuration in text files and deploy with a single `terraform apply` command. The same code can be executed to reproduce identical environments.

> **In a nutshell:** Instead of using the AWS console clicking buttons, you write code describing "I want this server in this AWS location," then one button press automatically builds it. Running the same code recreates the same environment.

**Key points:**

- **What it does:** Multi-cloud Infrastructure-as-Code tool
- **Why it's needed:** Automate cloud infrastructure building and changes safely and efficiently
- **Who uses it:** DevOps engineers, infrastructure engineers, software development teams

## Why it matters

Before Terraform, cloud infrastructure was built manually through AWS console (web UI) with point-and-click steps and manual value entry. Complex environments took days to build with high risk of human error.

Terraform enables:

Automated building and reproducibility. Running the same code completely reproduces the environment. "Development and production environments have slightly different configurations" problems disappear.

Multi-cloud support. Terraform supports AWS, Azure, GCP, and more. Changing providers means only updating the provider code portion—the same resources deploy in different clouds. This dramatically reduces vendor lock-in.

Infrastructure change transparency. All configuration changes are committed to version control, recording "who changed what and when." Pull requests enable code review before production deployment.

Easy scaling. Changing from three to five servers is simply updating code parameters and running `terraform apply`.

## How it works

Terraform's basic workflow follows these steps:

**1. Code writing**

First, write infrastructure configuration in HCL (Terraform's language). For example:

```hcl
provider "aws" {
  region = "ap-northeast-1"
}

resource "aws_instance" "web_server" {
  ami           = "ami-12345678"
  instance_type = "t2.micro"
}
```

This code means "create one t2.micro server in AWS's Tokyo region."

**2. Plan (planning)**

Running `terraform plan` calculates differences between current and code-specified states, showing what will be added, changed, or deleted.

You can confirm before executing, preventing unexpected changes.

**3. Apply (application)**

Running `terraform apply` executes the planned resource changes. API calls to cloud providers automatically create or update servers and network settings.

**4. State management**

Terraform records current infrastructure state in `terraform.tfstate`. On the next plan, it determines "what changed" by comparing this file to the code.

**Terraform's characteristics:**

- **Multi-cloud support**: Works with AWS, Azure, GCP, and 100+ other providers
- **Declarative**: Describes desired state, enabling high readability
- **Rich provider ecosystem**: Supports Kubernetes, Docker, GitHub, DataDog, and countless infrastructure services
- **Modularity**: Reusable common configurations

## Real-world use cases

**New SaaS service launches**

Startups launching new web services define infrastructure in Terraform: "5 web servers, 1 database, load balancer, CDN." Production environment launches in minutes, automating a week-long manual process.

**Multi-region deployments**

Global services deploying to multiple regions (Tokyo, London, Singapore) simply change region parameters and rerun code—identical environments deploy in different locations.

**Development/staging/production synchronization**

Parameterize environments so "development is compact, production is highly available" by changing `terraform.tfvars` per environment.

**Cloud vendor migration**

"Reduce AWS dependency" becomes possible by changing provider code and rerunning—Tencent can handle the same resources on different clouds, greatly reducing vendor lock-in.

## Benefits and considerations

Terraform's greatest benefit is automating complex infrastructure and making it reproducible. Multi-cloud support reduces vendor dependency.

Version control through Git enables "infrastructure as code culture" in organizations.

The `plan` command confirms changes before execution, preventing unexpected side effects.

Learning curves are important. HCL syntax is relatively simple, but you need both "Terraform concepts" (providers, resources, state management) and cloud provider knowledge (AWS VPC, security groups, etc.).

State file (terraform.tfstate) management is critical. This file may contain sensitive information (passwords, API keys) requiring secure storage and backup.

Terraform version management is also necessary. New versions can change code syntax, requiring version compatibility attention.

Complex branching logic or multi-tool integration sometimes can't be expressed in Terraform alone. In those cases, combining with Ansible is common.

## Related terms

- **[Infrastructure-as-Code (IaC)](Infrastructure-as-Code-IaC.md)** — Technology approach that Terraform enables
- **[Git](Git.md)** — Version control foundation for Terraform code and change tracking
- **[Continuous Integration](Continuous-Integration-CI.md)** — Process that validates Terraform code syntax and implementation
- **[Continuous Deployment](Continuous-Deployment-CD.md)** — Automatic infrastructure deployment via Terraform
- **[Configuration Management](Configuration-Management.md)** — Practice coordinating with Terraform for unified infrastructure management

## Frequently asked questions

**Q: Should we use Terraform or CloudFormation (AWS native)?**

A: "AWS-only organizations" might choose CloudFormation, but "multi-cloud planning organizations" should choose Terraform. Terraform offers better general-purpose capabilities with more future-proof learning investments.

**Q: Where should state files be stored?**

A: Local disk is dangerous. Use Terraform Cloud or encrypted S3 for remote state storage. This enables team-wide state sharing and safe concurrent operations.

**Q: If using Terraform, is Ansible unnecessary?**

A: Different purposes. Terraform manages infrastructure resources (servers themselves). Ansible manages server software configuration. Complex systems typically use "Terraform to create servers → Ansible to configure."

**Q: What are large-scale environment management challenges?**

A: Hundreds or thousands of resources cause Terraform files to grow and become complex. Modularity and workspace (environment separation) strategies maintain manageability. Remote state is essential to avoid state conflicts.
