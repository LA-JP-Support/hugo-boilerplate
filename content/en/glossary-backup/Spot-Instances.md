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

Spot Instances are a purchasing model for cloud compute where users access spare resources at discounts often reaching **up to 90% off** on-demand pricing. Major providers include:

- **Amazon Web Services (AWS) Spot Instances:** Users specify a maximum price and receive instances if the market price is below this threshold. [AWS Spot Instances Documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances.html)
- **Microsoft Azure Spot Virtual Machines (VMs):** Users set a max price; VMs are evicted when the market price exceeds this. [Azure Spot VMs Guide](https://spot.io/resources/azure-pricing/the-complete-guide/what-are-azure-spot-virtual-machines/)
- **Google Cloud Spot VMs:** Offer similar discounts, with fixed and substantial savings, and pricing is stable for up to a month. [Google Cloud Spot VMs](https://cloud.google.com/compute/docs/instances/spot)

Spot Instances are best suited for **flexible, fault-tolerant applications**. Providers can reclaim these instances with short notice, so resilience to interruptions is a crucial requirement.  

## How Spot Instances Work

### Pricing Mechanism

- **Dynamic, Supply/Demand Driven:** The spot price for each instance type and region fluctuates based on long-term trends in supply and demand, not real-time bidding. [AWS Pricing](https://aws.amazon.com/ec2/spot/pricing/)
- **Max Price:** Users can set a maximum price they’re willing to pay. As long as the current Spot price is below this, the instance runs.
- **No Real-Time Bidding (Modern Model):** Early systems involved live bidding, but now most providers use a set-max-price model for simplicity. Users no longer compete in real-time auctions. [Spot.io: Spot vs On-Demand](https://spot.io/resources/spot-instances/spot-instances-vs-on-demand-instances-pros-and-cons/)
- **Billing Granularity:** AWS, Azure, and GCP bill per second, after a 1-minute minimum. [Google Cloud Pricing](https://cloud.google.com/compute/pricing)

> **Example:** On AWS, an `m5.large` On-Demand instance costs $0.096/hr, while the Spot price could be as low as $0.019/hr (an 80%+ saving).  
> See [AWS Spot Pricing](https://aws.amazon.com/ec2/spot/pricing/)

### Availability & Interruption

- **Capacity Pool:** Each Spot Instance draw comes from a pool defined by instance type and availability zone.
- **Interruption Policy:** Providers may terminate or deallocate instances with short notice—2 minutes on AWS, 30 seconds on Azure and GCP—when they need the capacity or the spot price exceeds your max bid.
- **Interruption Notification:** AWS sends a 2-minute warning, while Azure and GCP provide a 30-second notice.  
  - [AWS Spot Interruptions](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-interruptions.html)
  - [Azure Spot VMs](https://learn.microsoft.com/en-us/azure/virtual-machines/spot-vms)
  - [GCP Spot VMs](https://cloud.google.com/compute/docs/instances/spot#preemption)
- **Rebalancing:** AWS offers "rebalance recommendations," giving extra early warning that a Spot Instance is at elevated risk of interruption.  
  - [AWS Rebalance Recommendations](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-interruptions.html#instance-rebalance-recommendations)
  
> **Key Point:** Applications **must** be architected to handle interruptions—statelessness, checkpointing, and auto-recovery are essential.

## Spot Instances vs. On-Demand vs. Reserved Instances

| Feature                    | **Spot Instances**                                             | **On-Demand Instances**                           | **Reserved Instances**                       |
|----------------------------|---------------------------------------------------------------|---------------------------------------------------|----------------------------------------------|
| **Pricing**                | Variable, up to 90% less than On-Demand                      | Fixed, highest price                              | Discounted (up to 72%), fixed                |
| **Availability**           | Only if spare capacity exists                                 | Always available (if capacity exists)             | Guaranteed during reservation period          |
| **Interruptions**          | Can be interrupted at any time (2-min or 30-sec notice)       | User decides when to terminate                     | Not interrupted during term                   |
| **Commitment**             | No commitment                                                 | No commitment                                     | 1 or 3 years (commitment required)            |
| **Use Cases**              | Flexible, fault-tolerant, non-critical                        | All workloads, especially critical                 | Predictable, steady-state workloads           |
| **SLA**                    | No SLA                                                        | Standard SLA                                      | Standard SLA                                 |
| **Billing Granularity**    | Per second (after 1st minute)                                 | Per second                                        | Per second                                   |

- **Further reading:** [AWS Billing & Purchasing Options](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-purchasing-options.html)

## Cross-Cloud Provider Comparison

| Feature                 | **AWS Spot Instances**                  | **GCP Spot VMs**                     | **Azure Spot VMs**                 |
|-------------------------|-----------------------------------------|--------------------------------------|------------------------------------|
| **Pricing Model**       | Variable, supply/demand driven          | Fixed discount (up to 91% off)       | Variable, supply/demand driven     |
| **Usage Time Limit**    | No fixed limit                          | Max 24 hours                         | No fixed limit                     |
| **Interruption Notice** | 2 minutes                               | 30 seconds                           | 30 seconds                         |
| **Billing**             | Per second (after 1 min)                | Per second                           | Per second                         |
| **SLA**                 | No SLA                                  | No SLA                               | No SLA                             |
| **Integration Tools**   | Spot Fleet, ASG, Kubernetes             | MIG, GKE                             | VM Scale Sets, AKS                 |
| **Best Use Cases**      | Batch, CI/CD, ML, HPC, stateless apps   | Batch, analytics, dev/test           | Batch, stateless apps, CI/CD       |
| **Unique Features**     | Spot block (fixed-term interruption)    | Sustained use discounts              | Eviction policy customization      |

- [Spot.io Provider Comparison](https://spot.io/resources/spot-instances/spot-instances-aws-azure-google-cloud/)

## Core Concepts

### Spot Capacity Pool

A group of unused virtual machines of the same instance type in the same availability zone. Each pool operates independently, and capacity/price can vary between pools. [AWS Spot Pools](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances.html)

### Spot Instance Request

A user-initiated request to allocate a Spot Instance. Requests can be:
- **One-time:** Provisioned once if capacity is available.
- **Persistent:** Automatically resubmitted if interrupted (useful for jobs that must eventually finish).

### Rebalance Recommendation (AWS)

AWS issues a rebalance recommendation before the standard interruption notice if a Spot Instance is at increased risk of termination, allowing workloads to proactively migrate or checkpoint. [AWS Instance Rebalance Recommendations](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-interruptions.html#instance-rebalance-recommendations)

## Use Cases and Practical Examples

Spot Instances excel in scenarios where **interruption is manageable** and costs need to be minimized. Top use cases include:

### Ideal Use Cases

- **Batch Processing:** Data analytics, video transcoding, rendering, ETL jobs.
  - *Example:* Researchers running Monte Carlo simulations for climate data, saving 80%+ on compute.
- **Big Data Analytics:** Hadoop/Spark clusters, log/data analysis at scale.
  - *Example:* Media businesses processing petabytes of logs nightly on AWS EMR with Spot Instances.
- **CI/CD Pipelines:** Short-lived build and test environments.
  - *Example:* SaaS providers using Spot Instances as Jenkins build agents for cost-effective, parallelized CI.
- **Machine Learning Training:** Deep learning, hyperparameter tuning, checkpointed training on GPUs.
  - *Example:* Teams training neural networks on Spot GPU instances with autosave for interruption recovery.
- **Containers and Microservices:** Stateless services orchestrated by Kubernetes or [Docker](/en/glossary/docker/) Swarm.
- **Dev/Test Environments:** Non-production workloads where interruption is acceptable.
- **High-Performance Computing (HPC):** Genomic sequencing, financial modeling, scientific simulations.

- [AWS Spot Use Cases](https://aws.amazon.com/ec2/spot/use-cases/)

### Non-Ideal Use Cases

- **Mission-Critical Applications:** Where high-availability and minimal downtime are paramount.
- **Stateful Apps Without Resilience:** Apps that cannot checkpoint state or recover from sudden termination.

- [Spot.io: Suitable Use Cases](https://spot.io/resources/spot-instances/spot-instances-aws-azure-google-cloud/#Suitable-Use-Cases-for-Spot-Instances)

## Risks, Challenges, and Mitigation Strategies

### Key Risks

- **Interruption Risk:** Instances can be terminated or deallocated with as little as 30 seconds’ notice.
- **Capacity Volatility:** Spot capacity can disappear unpredictably, depending on region, type, and market demand.
- **Pricing Fluctuations:** Spot prices can spike, especially for popular instance types during busy periods.
- **No SLA:** Providers do not guarantee uptime or availability for Spot Instances.

- [AWS Spot Interruptions](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-interruptions.html)
- [Spot.io: Risks & Strategies](https://spot.io/resources/spot-instances/spot-instances-aws-azure-google-cloud/#Strategies-to-Optimize-the-Use-of-Spot-Instances)

### Mitigation Strategies

- **Automation:**
  - Use orchestration systems (e.g., Kubernetes, AWS Auto Scaling) to reschedule and replace interrupted workloads.
  - Blend Spot with On-Demand and Reserved Instances for resilience.
  - Employ automation platforms (e.g., [Cast AI](https://cast.ai/blog/reduce-cloud-costs-with-spot-instances/), [Spot.io](https://spot.io/products/eco/)) that manage lifecycles and fallback.
- **Application Design:**
  - Architect services as stateless and leverage external storage.
  - Implement checkpointing to resume jobs after interruption.
  - Use loose coupling to tolerate node failures.
- **Proactive Monitoring:**
  - Monitor interruption rates by region/type using tools like [AWS Spot Instance Advisor](https://aws.amazon.com/ec2/spot/instance-advisor/).
  - Act on [rebalance recommendations](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-interruptions.html#instance-rebalance-recommendations) to migrate workloads early.
- **Diversification:**
  - Use a mix of instance types and regions to avoid “herd” interruptions.
  - Set sensible max bids to reduce risk of sudden eviction.

- [Cast AI Spot Guide](https://cast.ai/blog/reduce-cloud-costs-with-spot-instances/)

## Best Practices for Using Spot Instances

1. **Start with Non-Critical Workloads:** Validate your interruption-handling strategies.
2. **Diversify:** Use multiple instance types and availability zones for higher reliability.
3. **Automate:** Employ [AWS Spot Fleet](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Fleets.html), Auto Scaling Groups, or Kubernetes autoscalers.
4. **Monitor Trends:** Use [AWS Spot Price History](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances-history.html) and [Spot Instance Advisor](https://aws.amazon.com/ec2/spot/instance-advisor/).
5. **Set Max Prices:** Cap your bid at or below the On-Demand price.
6. **Plan for Interruption:** Architect for fast recovery and zero data loss.
7. **Leverage Third-Party Tools:** Try [Cast AI](https://cast.ai/blog/reduce-cloud-costs-with-spot-instances/) or [CloudZero](https://www.cloudzero.com/blog/spot-instances/) for optimization and automation.
8. **Use Tags:** Track usage and savings by team/project.
9. **Regularly Review:** Update your mix and strategies based on usage reports.

- [AWS Spot Best Practices](https://aws.amazon.com/blogs/compute/best-practices-to-optimize-your-amazon-ec2-spot-instances-usage/)
- [CloudZero Spot Guide](https://www.cloudzero.com/blog/spot-instances/)

## Billing and Pricing Details

- **Spot Price:** Set by the provider, fluctuates with market demand and supply.
- **Billing Granularity:** Per second after the first minute (AWS, Azure, GCP).
- **Termination Billing:** Generally, if AWS interrupts, you are not charged for the last partial hour; if you terminate, you pay for seconds used. [AWS Billing Details](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/billing-for-interrupted-spot-instances.html)
- **Savings Tracking:** Use provider dashboards, [AWS Spot Fleet savings reports](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-savings.html), or third-party tools (e.g., [Cast AI](https://cast.ai/blog/reduce-cloud-costs-with-spot-instances/), [Infracost](https://www.infracost.io/glossary/spot-instances/)).
- **No Overlap with Savings Plans:** Spot usage does not contribute to AWS Savings Plans commitments.

- [AWS EC2 Spot Pricing](https://aws.amazon.com/ec2/spot/pricing/)
- [GCP Spot Pricing](https://cloud.google.com/compute/pricing)
- [Azure Spot Pricing](https://azure.microsoft.com/en-us/pricing/details/virtual-machines/spot/)

## Example Scenario

**Research Team Running Simulations**

A university research group needs to run thousands of Monte Carlo simulations for climate modeling. By using Spot Instances orchestrated by Kubernetes, they cut compute costs by 85% compared to On-Demand pricing. Checkpoints are saved to persistent storage before interruption, so jobs resume without loss.

- [AWS Spot HPC Use Case](https://aws.amazon.com/ec2/spot/use-cases/hpc/)
- [Milvus AI Quick Reference: Spot Instances](https://milvus.io/ai-quick-reference/what-are-spot-instances-in-cloud-computing)

## Frequently Asked Questions (FAQ)

**Q: Can I use Spot Instances for production workloads?**  
A: Yes, if your application is resilient to interruptions. Many organizations blend Spot with On-Demand or Reserved Instances for critical workloads.  
- [AWS Spot FAQ](https://aws.amazon.com/ec2/spot/faqs/)

**Q: How much can I save with Spot Instances?**  
A: Typically 70–90% compared to On-Demand, depending on region, type, and demand.  
- [AWS Spot Savings](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-savings.html)

**Q: What happens when a Spot Instance is interrupted?**  
A: You receive a short interruption notice (2 minutes on AWS, 30 seconds on Azure/GCP). The instance is then terminated, stopped, or hibernated as per provider policy.  
- [AWS Spot Interruptions](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-interruptions.html)

**Q: How do I request a Spot Instance?**  
A: Use the cloud provider’s console, CLI, or API. Specify instance type, max price, and duration as needed.  
- [AWS Spot Requests](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-requests.html)

**Q: Can Spot Instances be used with Kubernetes?**  
A: Yes, container orchestrators like Kubernetes can reschedule pods when a Spot Instance is interrupted.  
- [Kubernetes with Spot Instances](https://cast.ai/blog/reduce-cloud-costs-with-spot-instances/)

**Q: Is there any SLA for Spot Instances?**  
A: No. Providers do not guarantee uptime or availability for Spot Instances.

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
