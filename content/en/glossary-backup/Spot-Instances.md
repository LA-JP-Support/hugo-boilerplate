---
title: "Spot Instances"
date: 2025-11-25
lastmod: 2025-12-05
translationKey: "spot-instances"
description: "Spot Instances are discounted cloud compute resources from AWS, Azure, and GCP, ideal for fault-tolerant workloads like batch processing, analytics, and ML training."
keywords: ["Spot Instances", "cloud compute", "AWS", "Azure", "GCP"]
category: "AI Infrastructure & Deployment"
type: "glossary"
draft: false
---
## What Are Spot Instances?

Spot Instances are a purchasing model for cloud compute where users access spare resources at discounts often reaching <strong>up to 90% off</strong>on-demand pricing. Major providers include:

- <strong>Amazon Web Services (AWS) Spot Instances:</strong>Users specify a maximum price and receive instances if the market price is below this threshold. [AWS Spot Instances Documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances.html)
- <strong>Microsoft Azure Spot Virtual Machines (VMs):</strong>Users set a max price; VMs are evicted when the market price exceeds this. [Azure Spot VMs Guide](https://spot.io/resources/azure-pricing/the-complete-guide/what-are-azure-spot-virtual-machines/)
- <strong>Google Cloud Spot VMs:</strong>Offer similar discounts, with fixed and substantial savings, and pricing is stable for up to a month. [Google Cloud Spot VMs](https://cloud.google.com/compute/docs/instances/spot)

Spot Instances are best suited for <strong>flexible, fault-tolerant applications</strong>. Providers can reclaim these instances with short notice, so resilience to interruptions is a crucial requirement.  

## How Spot Instances Work

### Pricing Mechanism

- <strong>Dynamic, Supply/Demand Driven:</strong>The spot price for each instance type and region fluctuates based on long-term trends in supply and demand, not real-time bidding. [AWS Pricing](https://aws.amazon.com/ec2/spot/pricing/)
- <strong>Max Price:</strong>Users can set a maximum price they’re willing to pay. As long as the current Spot price is below this, the instance runs.
- <strong>No Real-Time Bidding (Modern Model):</strong>Early systems involved live bidding, but now most providers use a set-max-price model for simplicity. Users no longer compete in real-time auctions. [Spot.io: Spot vs On-Demand](https://spot.io/resources/spot-instances/spot-instances-vs-on-demand-instances-pros-and-cons/)
- <strong>Billing Granularity:</strong>AWS, Azure, and GCP bill per second, after a 1-minute minimum. [Google Cloud Pricing](https://cloud.google.com/compute/pricing)

> <strong>Example:</strong>On AWS, an `m5.large` On-Demand instance costs $0.096/hr, while the Spot price could be as low as $0.019/hr (an 80%+ saving).  
> See [AWS Spot Pricing](https://aws.amazon.com/ec2/spot/pricing/)

### Availability & Interruption

- <strong>Capacity Pool:</strong>Each Spot Instance draw comes from a pool defined by instance type and availability zone.
- <strong>Interruption Policy:</strong>Providers may terminate or deallocate instances with short notice—2 minutes on AWS, 30 seconds on Azure and GCP—when they need the capacity or the spot price exceeds your max bid.
- <strong>Interruption Notification:</strong>AWS sends a 2-minute warning, while Azure and GCP provide a 30-second notice.  
  - [AWS Spot Interruptions](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-interruptions.html)
  - [Azure Spot VMs](https://learn.microsoft.com/en-us/azure/virtual-machines/spot-vms)
  - [GCP Spot VMs](https://cloud.google.com/compute/docs/instances/spot#preemption)
- <strong>Rebalancing:</strong>AWS offers "rebalance recommendations," giving extra early warning that a Spot Instance is at elevated risk of interruption.  
  - [AWS Rebalance Recommendations](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-interruptions.html#instance-rebalance-recommendations)
  
> <strong>Key Point:</strong>Applications <strong>must</strong>be architected to handle interruptions—statelessness, checkpointing, and auto-recovery are essential.

## Spot Instances vs. On-Demand vs. Reserved Instances

| Feature                    | <strong>Spot Instances</strong>| <strong>On-Demand Instances</strong>| <strong>Reserved Instances</strong>|
|----------------------------|---------------------------------------------------------------|---------------------------------------------------|----------------------------------------------|
| <strong>Pricing</strong>| Variable, up to 90% less than On-Demand                      | Fixed, highest price                              | Discounted (up to 72%), fixed                |
| <strong>Availability</strong>| Only if spare capacity exists                                 | Always available (if capacity exists)             | Guaranteed during reservation period          |
| <strong>Interruptions</strong>| Can be interrupted at any time (2-min or 30-sec notice)       | User decides when to terminate                     | Not interrupted during term                   |
| <strong>Commitment</strong>| No commitment                                                 | No commitment                                     | 1 or 3 years (commitment required)            |
| <strong>Use Cases</strong>| Flexible, fault-tolerant, non-critical                        | All workloads, especially critical                 | Predictable, steady-state workloads           |
| <strong>SLA</strong>| No SLA                                                        | Standard SLA                                      | Standard SLA                                 |
| <strong>Billing Granularity</strong>| Per second (after 1st minute)                                 | Per second                                        | Per second                                   |

- <strong>Further reading:</strong>[AWS Billing & Purchasing Options](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-purchasing-options.html)

## Cross-Cloud Provider Comparison

| Feature                 | <strong>AWS Spot Instances</strong>| <strong>GCP Spot VMs</strong>| <strong>Azure Spot VMs</strong>|
|-------------------------|-----------------------------------------|--------------------------------------|------------------------------------|
| <strong>Pricing Model</strong>| Variable, supply/demand driven          | Fixed discount (up to 91% off)       | Variable, supply/demand driven     |
| <strong>Usage Time Limit</strong>| No fixed limit                          | Max 24 hours                         | No fixed limit                     |
| <strong>Interruption Notice</strong>| 2 minutes                               | 30 seconds                           | 30 seconds                         |
| <strong>Billing</strong>| Per second (after 1 min)                | Per second                           | Per second                         |
| <strong>SLA</strong>| No SLA                                  | No SLA                               | No SLA                             |
| <strong>Integration Tools</strong>| Spot Fleet, ASG, Kubernetes             | MIG, GKE                             | VM Scale Sets, AKS                 |
| <strong>Best Use Cases</strong>| Batch, CI/CD, ML, HPC, stateless apps   | Batch, analytics, dev/test           | Batch, stateless apps, CI/CD       |
| <strong>Unique Features</strong>| Spot block (fixed-term interruption)    | Sustained use discounts              | Eviction policy customization      |

- [Spot.io Provider Comparison](https://spot.io/resources/spot-instances/spot-instances-aws-azure-google-cloud/)

## Core Concepts

### Spot Capacity Pool

A group of unused virtual machines of the same instance type in the same availability zone. Each pool operates independently, and capacity/price can vary between pools. [AWS Spot Pools](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances.html)

### Spot Instance Request

A user-initiated request to allocate a Spot Instance. Requests can be:
- <strong>One-time:</strong>Provisioned once if capacity is available.
- <strong>Persistent:</strong>Automatically resubmitted if interrupted (useful for jobs that must eventually finish).

### Rebalance Recommendation (AWS)

AWS issues a rebalance recommendation before the standard interruption notice if a Spot Instance is at increased risk of termination, allowing workloads to proactively migrate or checkpoint. [AWS Instance Rebalance Recommendations](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-interruptions.html#instance-rebalance-recommendations)

## Use Cases and Practical Examples

Spot Instances excel in scenarios where <strong>interruption is manageable</strong>and costs need to be minimized. Top use cases include:

### Ideal Use Cases

- <strong>Batch Processing:</strong>Data analytics, video transcoding, rendering, ETL jobs.
  - *Example:* Researchers running Monte Carlo simulations for climate data, saving 80%+ on compute.
- <strong>Big Data Analytics:</strong>Hadoop/Spark clusters, log/data analysis at scale.
  - *Example:* Media businesses processing petabytes of logs nightly on AWS EMR with Spot Instances.
- <strong>CI/CD Pipelines:</strong>Short-lived build and test environments.
  - *Example:* SaaS providers using Spot Instances as Jenkins build agents for cost-effective, parallelized CI.
- <strong>Machine Learning Training:</strong>Deep learning, hyperparameter tuning, checkpointed training on GPUs.
  - *Example:* Teams training neural networks on Spot GPU instances with autosave for interruption recovery.
- <strong>Containers and Microservices:</strong>Stateless services orchestrated by Kubernetes or Docker Swarm.
- <strong>Dev/Test Environments:</strong>Non-production workloads where interruption is acceptable.
- <strong>High-Performance Computing (HPC):</strong>Genomic sequencing, financial modeling, scientific simulations.

- [AWS Spot Use Cases](https://aws.amazon.com/ec2/spot/use-cases/)

### Non-Ideal Use Cases

- <strong>Mission-Critical Applications:</strong>Where high-availability and minimal downtime are paramount.
- <strong>Stateful Apps Without Resilience:</strong>Apps that cannot checkpoint state or recover from sudden termination.

- [Spot.io: Suitable Use Cases](https://spot.io/resources/spot-instances/spot-instances-aws-azure-google-cloud/#Suitable-Use-Cases-for-Spot-Instances)

## Risks, Challenges, and Mitigation Strategies

### Key Risks

- <strong>Interruption Risk:</strong>Instances can be terminated or deallocated with as little as 30 seconds’ notice.
- <strong>Capacity Volatility:</strong>Spot capacity can disappear unpredictably, depending on region, type, and market demand.
- <strong>Pricing Fluctuations:</strong>Spot prices can spike, especially for popular instance types during busy periods.
- <strong>No SLA:</strong>Providers do not guarantee uptime or availability for Spot Instances.

- [AWS Spot Interruptions](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-interruptions.html)
- [Spot.io: Risks & Strategies](https://spot.io/resources/spot-instances/spot-instances-aws-azure-google-cloud/#Strategies-to-Optimize-the-Use-of-Spot-Instances)

### Mitigation Strategies

- <strong>Automation:</strong>- Use orchestration systems (e.g., Kubernetes, AWS Auto Scaling) to reschedule and replace interrupted workloads.
  - Blend Spot with On-Demand and Reserved Instances for resilience.
  - Employ automation platforms (e.g., [Cast AI](https://cast.ai/blog/reduce-cloud-costs-with-spot-instances/), [Spot.io](https://spot.io/products/eco/)) that manage lifecycles and fallback.
- <strong>Application Design:</strong>- Architect services as stateless and leverage external storage.
  - Implement checkpointing to resume jobs after interruption.
  - Use loose coupling to tolerate node failures.
- <strong>Proactive Monitoring:</strong>- Monitor interruption rates by region/type using tools like [AWS Spot Instance Advisor](https://aws.amazon.com/ec2/spot/instance-advisor/).
  - Act on [rebalance recommendations](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-interruptions.html#instance-rebalance-recommendations) to migrate workloads early.
- <strong>Diversification:</strong>- Use a mix of instance types and regions to avoid “herd” interruptions.
  - Set sensible max bids to reduce risk of sudden eviction.

- [Cast AI Spot Guide](https://cast.ai/blog/reduce-cloud-costs-with-spot-instances/)

## Best Practices for Using Spot Instances

1. <strong>Start with Non-Critical Workloads:</strong>Validate your interruption-handling strategies.
2. <strong>Diversify:</strong>Use multiple instance types and availability zones for higher reliability.
3. <strong>Automate:</strong>Employ [AWS Spot Fleet](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Fleets.html), Auto Scaling Groups, or Kubernetes autoscalers.
4. <strong>Monitor Trends:</strong>Use [AWS Spot Price History](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances-history.html) and [Spot Instance Advisor](https://aws.amazon.com/ec2/spot/instance-advisor/).
5. <strong>Set Max Prices:</strong>Cap your bid at or below the On-Demand price.
6. <strong>Plan for Interruption:</strong>Architect for fast recovery and zero data loss.
7. <strong>Leverage Third-Party Tools:</strong>Try [Cast AI](https://cast.ai/blog/reduce-cloud-costs-with-spot-instances/) or [CloudZero](https://www.cloudzero.com/blog/spot-instances/) for optimization and automation.
8. <strong>Use Tags:</strong>Track usage and savings by team/project.
9. <strong>Regularly Review:</strong>Update your mix and strategies based on usage reports.

- [AWS Spot Best Practices](https://aws.amazon.com/blogs/compute/best-practices-to-optimize-your-amazon-ec2-spot-instances-usage/)
- [CloudZero Spot Guide](https://www.cloudzero.com/blog/spot-instances/)

## Billing and Pricing Details

- <strong>Spot Price:</strong>Set by the provider, fluctuates with market demand and supply.
- <strong>Billing Granularity:</strong>Per second after the first minute (AWS, Azure, GCP).
- <strong>Termination Billing:</strong>Generally, if AWS interrupts, you are not charged for the last partial hour; if you terminate, you pay for seconds used. [AWS Billing Details](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/billing-for-interrupted-spot-instances.html)
- <strong>Savings Tracking:</strong>Use provider dashboards, [AWS Spot Fleet savings reports](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-savings.html), or third-party tools (e.g., [Cast AI](https://cast.ai/blog/reduce-cloud-costs-with-spot-instances/), [Infracost](https://www.infracost.io/glossary/spot-instances/)).
- <strong>No Overlap with Savings Plans:</strong>Spot usage does not contribute to AWS Savings Plans commitments.

- [AWS EC2 Spot Pricing](https://aws.amazon.com/ec2/spot/pricing/)
- [GCP Spot Pricing](https://cloud.google.com/compute/pricing)
- [Azure Spot Pricing](https://azure.microsoft.com/en-us/pricing/details/virtual-machines/spot/)

## Example Scenario

<strong>Research Team Running Simulations</strong>A university research group needs to run thousands of Monte Carlo simulations for climate modeling. By using Spot Instances orchestrated by Kubernetes, they cut compute costs by 85% compared to On-Demand pricing. Checkpoints are saved to persistent storage before interruption, so jobs resume without loss.

- [AWS Spot HPC Use Case](https://aws.amazon.com/ec2/spot/use-cases/hpc/)
- [Milvus AI Quick Reference: Spot Instances](https://milvus.io/ai-quick-reference/what-are-spot-instances-in-cloud-computing)

## Frequently Asked Questions (FAQ)

<strong>Q: Can I use Spot Instances for production workloads?</strong>A: Yes, if your application is resilient to interruptions. Many organizations blend Spot with On-Demand or Reserved Instances for critical workloads.  
- [AWS Spot FAQ](https://aws.amazon.com/ec2/spot/faqs/)

<strong>Q: How much can I save with Spot Instances?</strong>A: Typically 70–90% compared to On-Demand, depending on region, type, and demand.  
- [AWS Spot Savings](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-savings.html)

<strong>Q: What happens when a Spot Instance is interrupted?</strong>A: You receive a short interruption notice (2 minutes on AWS, 30 seconds on Azure/GCP). The instance is then terminated, stopped, or hibernated as per provider policy.  
- [AWS Spot Interruptions](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-interruptions.html)

<strong>Q: How do I request a Spot Instance?</strong>A: Use the cloud provider’s console, CLI, or API. Specify instance type, max price, and duration as needed.  
- [AWS Spot Requests](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-requests.html)

<strong>Q: Can Spot Instances be used with Kubernetes?</strong>A: Yes, container orchestrators like Kubernetes can reschedule pods when a Spot Instance is interrupted.  
- [Kubernetes with Spot Instances](https://cast.ai/blog/reduce-cloud-costs-with-spot-instances/)

<strong>Q: Is there any SLA for Spot Instances?</strong>A: No. Providers do not guarantee uptime or availability for Spot Instances.

## Authoritative Resources & Further Reading

- [AWS Spot Instances Documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances.html)
- [AWS EC2 Spot Pricing](https://aws.amazon.com/ec2/spot/pricing/)
- [CloudZero Spot Instances Guide](https://www.cloudzero.com/blog/spot-instances/)
- [Infracost Spot Instances Glossary](https://www.infracost.io/glossary/spot-instances/)
- [Cast AI Spot Instances Guide](https://cast.ai/blog/reduce-cloud-costs-with-spot-instances/)
- [Milvus AI Quick Reference: Spot Instances](https://milvus.io/ai-quick-reference/what-are-spot-instances-in-cloud-computing)
- [Amazon EC2 Spot Fleet](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Fleets.html)
- [AWS Spot Instance Advisor](https://aws.amazon.com/ec2/spot/instance-advisor/)
- [Spot.io Ultimate Guide](https://spot.io/resources/spot-instances/spot-instances-aws-azure-google-cloud/)
- [AWS Spot FAQ](https://aws.amazon.com/ec2/spot/faqs/)

## Related Terms

- [On-Demand Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-on-demand-instances.html)
- [Reserved Instances](https://docs.aws.amazon.com/AWSEC2/latest
