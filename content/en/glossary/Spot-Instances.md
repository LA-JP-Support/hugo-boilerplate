---
title: "Spot Instances"
date: 2025-12-18
lastmod: 2025-12-18
translationKey: "spot-instances"
description: "Discounted cloud computing resources that use spare server capacity at up to 90% off regular prices, ideal for flexible tasks that can tolerate brief interruptions."
keywords: ["Spot Instances", "cloud compute", "AWS", "Azure", "GCP"]
category: "AI Infrastructure & Deployment"
type: "glossary"
draft: false
---

## What are Spot Instances?

Spot Instances are a purchasing model for cloud compute where users access spare capacity at discounts often reaching up to 90% off on-demand pricing. Major cloud providers offer Spot Instance programs with varying features and pricing mechanisms:

<strong>Amazon Web Services (AWS) Spot Instances:</strong>Users specify a maximum price and receive instances if the market price is below this threshold. Spot Instances are reclaimed with 2-minute notice when capacity is needed or price exceeds the maximum bid.

<strong>Microsoft Azure Spot Virtual Machines (VMs):</strong>Users set a maximum price; VMs are evicted when the market price exceeds this limit. Azure provides 30-second eviction notice.

<strong>Google Cloud Spot VMs:</strong>Offer similar discounts with fixed and substantial savings. Pricing is stable for up to a month. Google provides 30-second preemption notice.

Spot Instances are best suited for flexible, fault-tolerant applications. Providers can reclaim these instances with short notice, so resilience to interruptions is a crucial requirement.

## How Spot Instances Work

### Pricing Mechanism

<strong>Dynamic, Supply/Demand Driven:</strong>The spot price for each instance type and region fluctuates based on long-term trends in supply and demand, not real-time bidding.

<strong>Max Price:</strong>Users can set a maximum price they're willing to pay. As long as the current Spot price is below this, the instance runs.

<strong>No Real-Time Bidding (Modern Model):</strong>Early systems involved live bidding, but now most providers use a set-max-price model for simplicity.

<strong>Billing Granularity:</strong>AWS, Azure, and GCP bill per second, after a 1-minute minimum.

<strong>Example:</strong>On AWS, an `m5.large` On-Demand instance costs $0.096/hr, while the Spot price could be as low as $0.019/hr (an 80%+ saving).

### Availability & Interruption

<strong>Capacity Pool:</strong>Each Spot Instance draw comes from a pool defined by instance type and availability zone.

<strong>Interruption Policy:</strong>Providers may terminate or deallocate instances with short notice—2 minutes on AWS, 30 seconds on Azure and GCP—when they need the capacity or the spot price exceeds your max bid.

<strong>Interruption Notification:</strong>- AWS: 2-minute warning
- Azure: 30-second notice
- GCP: 30-second notice

<strong>Rebalancing:</strong>AWS offers "rebalance recommendations," giving extra early warning that a Spot Instance is at elevated risk of interruption.

<strong>Critical Point:</strong>Applications must be architected to handle interruptions—statelessness, checkpointing, and auto-recovery are essential.

## Comparison: Spot vs On-Demand vs Reserved

| Feature | Spot Instances | On-Demand Instances | Reserved Instances |
|---------|----------------|---------------------|-------------------|
| <strong>Pricing</strong>| Variable, up to 90% less | Fixed, highest price | Discounted (up to 72%), fixed |
| <strong>Availability</strong>| Only if spare capacity exists | Always available | Guaranteed during reservation |
| <strong>Interruptions</strong>| Can be interrupted (2-min or 30-sec notice) | User decides when to terminate | Not interrupted during term |
| <strong>Commitment</strong>| No commitment | No commitment | 1 or 3 years required |
| <strong>Use Cases</strong>| Flexible, fault-tolerant, non-critical | All workloads, especially critical | Predictable, steady-state |
| <strong>SLA</strong>| No SLA | Standard SLA | Standard SLA |
| <strong>Billing</strong>| Per second (after 1st minute) | Per second | Per second |

## Cross-Cloud Provider Comparison

| Feature | AWS Spot | GCP Spot VMs | Azure Spot VMs |
|---------|----------|--------------|----------------|
| <strong>Pricing Model</strong>| Variable, supply/demand driven | Fixed discount (up to 91% off) | Variable, supply/demand driven |
| <strong>Usage Time Limit</strong>| No fixed limit | Max 24 hours | No fixed limit |
| <strong>Interruption Notice</strong>| 2 minutes | 30 seconds | 30 seconds |
| <strong>Billing</strong>| Per second (after 1 min) | Per second | Per second |
| <strong>SLA</strong>| No SLA | No SLA | No SLA |
| <strong>Integration Tools</strong>| Spot Fleet, ASG, Kubernetes | MIG, GKE | VM Scale Sets, AKS |
| <strong>Best Use Cases</strong>| Batch, CI/CD, ML, HPC, stateless | Batch, analytics, dev/test | Batch, stateless apps, CI/CD |
| <strong>Unique Features</strong>| Spot block (fixed-term interruption) | Sustained use discounts | Eviction policy customization |

## Core Concepts

### Spot Capacity Pool

A group of unused virtual machines of the same instance type in the same availability zone. Each pool operates independently, and capacity/price can vary between pools.

### Spot Instance Request

A user-initiated request to allocate a Spot Instance:
- <strong>One-time:</strong>Provisioned once if capacity is available
- <strong>Persistent:</strong>Automatically resubmitted if interrupted (useful for jobs that must eventually finish)

### Rebalance Recommendation (AWS)

AWS issues a rebalance recommendation before the standard interruption notice if a Spot Instance is at increased risk of termination, allowing workloads to proactively migrate or checkpoint.

## Use Cases and Examples

### Ideal Use Cases

<strong>Batch Processing:</strong>Data analytics, video transcoding, rendering, ETL jobs  
*Example:* Researchers running Monte Carlo simulations for climate data, saving 80%+ on compute.

<strong>Big Data Analytics:</strong>Hadoop/Spark clusters, log/data analysis at scale  
*Example:* Media businesses processing petabytes of logs nightly on AWS EMR with Spot Instances.

<strong>CI/CD Pipelines:</strong>Short-lived build and test environments  
*Example:* SaaS providers using Spot Instances as Jenkins build agents for cost-effective, parallelized CI.

<strong>Machine Learning Training:</strong>Deep learning, hyperparameter tuning, checkpointed training on GPUs  
*Example:* Teams training neural networks on Spot GPU instances with autosave for interruption recovery.

<strong>Containers and Microservices:</strong>Stateless services orchestrated by Kubernetes or Docker Swarm

<strong>Dev/Test Environments:</strong>Non-production workloads where interruption is acceptable

<strong>High-Performance Computing (HPC):</strong>Genomic sequencing, financial modeling, scientific simulations

### Non-Ideal Use Cases

<strong>Mission-Critical Applications:</strong>Where high-availability and minimal downtime are paramount

<strong>Stateful Apps Without Resilience:</strong>Apps that cannot checkpoint state or recover from sudden termination

## Risks and Mitigation Strategies

### Key Risks

<strong>Interruption Risk:</strong>Instances can be terminated with as little as 30 seconds' notice

<strong>Capacity Volatility:</strong>Spot capacity can disappear unpredictably

<strong>Pricing Fluctuations:</strong>Spot prices can spike, especially for popular instance types

<strong>No SLA:</strong>Providers do not guarantee uptime or availability

### Mitigation Strategies

<strong>Automation:</strong>- Use orchestration systems (Kubernetes, AWS Auto Scaling) to reschedule and replace interrupted workloads
- Blend Spot with On-Demand and Reserved Instances for resilience
- Employ automation platforms that manage lifecycles and fallback

<strong>Application Design:</strong>- Architect services as stateless and leverage external storage
- Implement checkpointing to resume jobs after interruption
- Use loose coupling to tolerate node failures

<strong>Proactive Monitoring:</strong>- Monitor interruption rates by region/type using tools like AWS Spot Instance Advisor
- Act on rebalance recommendations to migrate workloads early

<strong>Diversification:</strong>- Use mix of instance types and regions to avoid "herd" interruptions
- Set sensible max bids to reduce risk of sudden eviction

## Best Practices

<strong>1. Start with Non-Critical Workloads</strong>Validate your interruption-handling strategies before moving critical workloads.

<strong>2. Diversify</strong>Use multiple instance types and availability zones for higher reliability.

<strong>3. Automate</strong>Employ AWS Spot Fleet, Auto Scaling Groups, or Kubernetes autoscalers.

<strong>4. Monitor Trends</strong>Use AWS Spot Price History and Spot Instance Advisor.

<strong>5. Set Max Prices</strong>Cap your bid at or below the On-Demand price.

<strong>6. Plan for Interruption</strong>Architect for fast recovery and zero data loss.

<strong>7. Leverage Third-Party Tools</strong>Try Cast AI or CloudZero for optimization and automation.

<strong>8. Use Tags</strong>Track usage and savings by team/project.

<strong>9. Regularly Review</strong>Update your mix and strategies based on usage reports.

## Billing and Pricing

<strong>Spot Price:</strong>Set by provider, fluctuates with market demand and supply

<strong>Billing Granularity:</strong>Per second after first minute (AWS, Azure, GCP)

<strong>Termination Billing:</strong>Generally, if AWS interrupts, you are not charged for the last partial hour; if you terminate, you pay for seconds used.

<strong>Savings Tracking:</strong>Use provider dashboards, AWS Spot Fleet savings reports, or third-party tools

<strong>No Overlap with Savings Plans:</strong>Spot usage does not contribute to AWS Savings Plans commitments

## Example Scenario

<strong>Research Team Running Simulations</strong>A university research group needs to run thousands of Monte Carlo simulations for climate modeling. By using Spot Instances orchestrated by Kubernetes, they cut compute costs by 85% compared to On-Demand pricing. Checkpoints are saved to persistent storage before interruption, so jobs resume without loss.

## Frequently Asked Questions

<strong>Q: Can I use Spot Instances for production workloads?</strong>A: Yes, if your application is resilient to interruptions. Many organizations blend Spot with On-Demand or Reserved Instances for critical workloads.

<strong>Q: How much can I save with Spot Instances?</strong>A: Typically 70–90% compared to On-Demand, depending on region, type, and demand.

<strong>Q: What happens when a Spot Instance is interrupted?</strong>A: You receive a short interruption notice (2 minutes on AWS, 30 seconds on Azure/GCP). The instance is then terminated, stopped, or hibernated.

<strong>Q: How do I request a Spot Instance?</strong>A: Use the cloud provider's console, CLI, or API. Specify instance type, max price, and duration as needed.

<strong>Q: Can Spot Instances be used with Kubernetes?</strong>A: Yes, container orchestrators like Kubernetes can reschedule pods when a Spot Instance is interrupted.

<strong>Q: Is there any SLA for Spot Instances?</strong>A: No. Providers do not guarantee uptime or availability for Spot Instances.

## References


1. Amazon Web Services (AWS). (n.d.). AWS Spot Instances Documentation. AWS EC2 User Guide.
2. Amazon Web Services (AWS). (n.d.). AWS EC2 Spot Pricing. AWS Pricing.
3. Amazon Web Services (AWS). (n.d.). AWS Spot Interruptions. AWS EC2 User Guide.
4. Amazon Web Services (AWS). (n.d.). AWS Instance Rebalance Recommendations. AWS EC2 User Guide.
5. Amazon Web Services (AWS). (n.d.). AWS Spot Use Cases. AWS Website.
6. Amazon Web Services (AWS). (n.d.). AWS Spot HPC Use Case. AWS Website.
7. Amazon Web Services (AWS). (n.d.). AWS Billing & Purchasing Options. AWS EC2 User Guide.
8. Amazon Web Services (AWS). (n.d.). AWS Spot Price History. AWS EC2 User Guide.
9. Amazon Web Services (AWS). (n.d.). AWS Spot Instance Advisor. AWS Website.
10. Amazon Web Services (AWS). (n.d.). AWS EC2 Spot Fleet. AWS EC2 User Guide.
11. Amazon Web Services (AWS). (n.d.). AWS Spot Requests. AWS EC2 User Guide.
12. Amazon Web Services (AWS). (n.d.). AWS Spot Savings. AWS EC2 User Guide.
13. Amazon Web Services (AWS). (n.d.). AWS Billing for Interrupted Spot Instances. AWS EC2 User Guide.
14. Amazon Web Services (AWS). (n.d.). AWS Spot Best Practices. AWS Compute Blog.
15. Amazon Web Services (AWS). (n.d.). AWS Spot FAQ. AWS Website.
16. Google Cloud. (n.d.). Google Cloud Spot VMs. Google Cloud Documentation.
17. Google Cloud. (n.d.). Google Cloud Spot Preemption. Google Cloud Documentation.
18. Google Cloud. (n.d.). Google Cloud Pricing. Google Cloud Website.
19. Microsoft Azure. (n.d.). Azure Spot Virtual Machines. Microsoft Learn.
20. Microsoft Azure. (n.d.). Azure Spot Pricing. Azure Website.
21. Spot.io. (n.d.). Azure Spot VMs Guide. Spot.io Resources.
22. Spot.io. (n.d.). Spot vs On-Demand. Spot.io Resources.
23. Spot.io. (n.d.). Provider Comparison. Spot.io Resources.
24. Spot.io. (n.d.). Suitable Use Cases. Spot.io Resources.
25. Spot.io. (n.d.). Risks & Strategies. Spot.io Resources.
26. Spot.io. (n.d.). Ultimate Guide. Spot.io Resources.
27. Spot.io. (n.d.). Spot.io Eco. Spot.io Products.
28. CloudZero. (n.d.). Spot Instances Guide. CloudZero Blog.
29. Infracost. (n.d.). Spot Instances Glossary. Infracost Website.
30. Cast AI. (n.d.). Spot Guide. Cast AI Blog.
31. Milvus AI. (n.d.). Spot Instances Quick Reference. Milvus AI Reference.
