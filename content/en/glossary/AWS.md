---
title: AWS
date: 2026-01-29
lastmod: 2026-04-02
translationKey: aws
description: Amazon Web Services (AWS) is a scalable cloud computing platform providing 200+ services, enabling global enterprises to build and operate IT infrastructure.
keywords:
- AWS
- Amazon Web Services
- Cloud Computing
- Cloud Infrastructure
- Cloud Platform
category: Enterprise & Platform
type: glossary
draft: false
url: /en/glossary/aws/
aliases:
- /en/glossary/AWS/
---

## What is AWS?

**AWS is Amazon's comprehensive cloud computing platform providing 200+ services—computing, storage, databases, networking, AI/machine learning—used globally by enterprises to build and operate IT infrastructure.** It eliminates on-premises server and data center building/management, enabling on-demand resource use. In 2024, AWS holds approximately 32% of the global cloud infrastructure market, leading the industry.

> **In a nutshell:** "Rental service for computing power." Instead of purchasing hardware, rent resources when needed and pay per usage—like paying monthly electricity bills.

**Key points:**

- **What it does:** Provides servers, storage, databases, networking, AI features—all IT infrastructure via internet
- **Why it matters:** Businesses skip capital infrastructure investment, respond rapidly to change, access world-class infrastructure
- **Who uses it:** Startups through enterprises, governments, educational institutions—all sizes and industries

## Why it matters

Traditionally, enterprises required massive capital investment in server hardware, network equipment, and security systems, plus ongoing specialist team maintenance. This burden prevented smaller companies from accessing world-class infrastructure.

AWS changed this. Netflix, Airbnb, Spotify, Pinterest—all-scale companies use identical infrastructure, leveling competitive ground regardless of size. With pay-per-use pricing, startups run cheaply initially and auto-scale as they grow. Regulatory compliance (HIPAA, PCI-DSS, GDPR) is pre-certified, dramatically reducing individual burden.

## How it works

AWS structures as regions (geographic areas) and availability zones (region's independent data centers). Users freely choose application location, data storage location, and backup location, meeting regulatory and latency requirements.

Users interact through three interfaces: AWS Management Console (web UI), AWS CLI (command-line), SDKs (language-specific libraries). All operations authenticate and authorize via IAM, strictly limiting user capabilities.

Real usage: launching EC2 (virtual server) means specifying instance type and region; automatic orchestration allocates physical servers, configures networking, applies security groups—typically completing in minutes. This contrasts traditional physical server ordering taking weeks/months.

## Real-world use cases

**Large web application operation**

Netflix and Uber Eats handle extreme traffic fluctuations using AWS Auto Scaling, auto-adjusting server counts matching access demand. Peaks run thousands of servers, maintaining stability.

**Data analytics and big data**

Airbnb and major banks analyze petabyte-scale customer data with AWS Redshift and EMR, leveraging real-time pricing and fraud detection. AWS Glue automates ETL across data sources.

**Machine learning development**

Healthcare and manufacturing develop diagnostic AI and quality inspection AI via Amazon SageMaker, deploying to production. Pre-trained models eliminate deep ML expertise requirements.

**Hybrid workload migration**

On-premises data center enterprises migrate to AWS via Migration Hub, reducing IT costs and accelerating global expansion.

## Benefits and considerations

**Benefits:** AWS excels in flexibility, scalability, and reliability. Companies eliminate capital IT spending; usage-based costs optimize naturally. Global regions enable local deployment worldwide.

**Considerations:** AWS's vast service catalog creates steep learning curves; proper architecture requires deep expertise. AWS dependency creates "vendor lock-in" risks, complicating migration. Pay-per-use pricing risks unexpected cost spikes if unoptimized.

## Related terms

- **[Amazon EC2](EC2.md)** — Virtual server service, AWS's computational foundation
- **[S3](S3.md)** — Object storage for video, images, documents
- **[RDS](RDS.md)** — Managed relational databases (PostgreSQL, MySQL, Oracle)
- **[Cloud Computing](Cloud-Computing.md)** — Internet-delivered computing resources; AWS is flagship example
- **[API Gateway](API-Gateway.md)** — API endpoint management for microservice and client-server communication

## Frequently asked questions

**Q: How do I optimize AWS costs?**

A: Regularly analyze usage via AWS Cost Explorer, use reserved instances for predictable loads, delete unnecessary resources, review auto-scaling settings. AWS Trusted Advisor auto-suggests optimizations.

**Q: How trustworthy is AWS security?**

A: AWS uses shared responsibility: AWS secures infrastructure, companies secure applications and data. AWS holds multiple certifications (SOC2, FedRAMP, HIPAA); underlying infrastructure is extremely robust.

**Q: Can I migrate from AWS to another cloud provider?**

A: Technically possible, but deep AWS dependency complicates migration significantly. Plan cloud-agnostic layers from implementation start if migration is anticipated.
