---
title: "Spot Instances"
date: 2025-12-18
lastmod: 2025-12-18
translationKey: "spot-instances"
description: "Spot Instances are discounted cloud compute resources from AWS, Azure, and GCP, ideal for fault-tolerant workloads like batch processing, analytics, and ML training."
keywords: ["Spot Instances", "cloud compute", "AWS", "Azure", "GCP"]
category: "AI Infrastructure & Deployment"
type: "glossary"
draft: false
---

## What are Spot Instances?

Spot Instances are a purchasing model for cloud compute where users access spare capacity at discounts often reaching up to 90% off on-demand pricing. Major cloud providers offer Spot Instance programs with varying features and pricing mechanisms:

**Amazon Web Services (AWS) Spot Instances:** Users specify a maximum price and receive instances if the market price is below this threshold. Spot Instances are reclaimed with 2-minute notice when capacity is needed or price exceeds the maximum bid.

**Microsoft Azure Spot Virtual Machines (VMs):** Users set a maximum price; VMs are evicted when the market price exceeds this limit. Azure provides 30-second eviction notice.

**Google Cloud Spot VMs:** Offer similar discounts with fixed and substantial savings. Pricing is stable for up to a month. Google provides 30-second preemption notice.

Spot Instances are best suited for flexible, fault-tolerant applications. Providers can reclaim these instances with short notice, so resilience to interruptions is a crucial requirement.

## How Spot Instances Work

### Pricing Mechanism

**Dynamic, Supply/Demand Driven:** The spot price for each instance type and region fluctuates based on long-term trends in supply and demand, not real-time bidding.

**Max Price:** Users can set a maximum price they're willing to pay. As long as the current Spot price is below this, the instance runs.

**No Real-Time Bidding (Modern Model):** Early systems involved live bidding, but now most providers use a set-max-price model for simplicity.

**Billing Granularity:** AWS, Azure, and GCP bill per second, after a 1-minute minimum.

**Example:** On AWS, an `m5.large` On-Demand instance costs $0.096/hr, while the Spot price could be as low as $0.019/hr (an 80%+ saving).

### Availability & Interruption

**Capacity Pool:** Each Spot Instance draw comes from a pool defined by instance type and availability zone.

**Interruption Policy:** Providers may terminate or deallocate instances with short notice—2 minutes on AWS, 30 seconds on Azure and GCP—when they need the capacity or the spot price exceeds your max bid.

**Interruption Notification:**
- AWS: 2-minute warning
- Azure: 30-second notice
- GCP: 30-second notice

**Rebalancing:** AWS offers "rebalance recommendations," giving extra early warning that a Spot Instance is at elevated risk of interruption.

**Critical Point:** Applications must be architected to handle interruptions—statelessness, checkpointing, and auto-recovery are essential.

## Comparison: Spot vs On-Demand vs Reserved

| Feature | Spot Instances | On-Demand Instances | Reserved Instances |
|---------|----------------|---------------------|-------------------|
| **Pricing** | Variable, up to 90% less | Fixed, highest price | Discounted (up to 72%), fixed |
| **Availability** | Only if spare capacity exists | Always available | Guaranteed during reservation |
| **Interruptions** | Can be interrupted (2-min or 30-sec notice) | User decides when to terminate | Not interrupted during term |
| **Commitment** | No commitment | No commitment | 1 or 3 years required |
| **Use Cases** | Flexible, fault-tolerant, non-critical | All workloads, especially critical | Predictable, steady-state |
| **SLA** | No SLA | Standard SLA | Standard SLA |
| **Billing** | Per second (after 1st minute) | Per second | Per second |

## Cross-Cloud Provider Comparison

| Feature | AWS Spot | GCP Spot VMs | Azure Spot VMs |
|---------|----------|--------------|----------------|
| **Pricing Model** | Variable, supply/demand driven | Fixed discount (up to 91% off) | Variable, supply/demand driven |
| **Usage Time Limit** | No fixed limit | Max 24 hours | No fixed limit |
| **Interruption Notice** | 2 minutes | 30 seconds | 30 seconds |
| **Billing** | Per second (after 1 min) | Per second | Per second |
| **SLA** | No SLA | No SLA | No SLA |
| **Integration Tools** | Spot Fleet, ASG, Kubernetes | MIG, GKE | VM Scale Sets, AKS |
| **Best Use Cases** | Batch, CI/CD, ML, HPC, stateless | Batch, analytics, dev/test | Batch, stateless apps, CI/CD |
| **Unique Features** | Spot block (fixed-term interruption) | Sustained use discounts | Eviction policy customization |

## Core Concepts

### Spot Capacity Pool

A group of unused virtual machines of the same instance type in the same availability zone. Each pool operates independently, and capacity/price can vary between pools.

### Spot Instance Request

A user-initiated request to allocate a Spot Instance:
- **One-time:** Provisioned once if capacity is available
- **Persistent:** Automatically resubmitted if interrupted (useful for jobs that must eventually finish)

### Rebalance Recommendation (AWS)

AWS issues a rebalance recommendation before the standard interruption notice if a Spot Instance is at increased risk of termination, allowing workloads to proactively migrate or checkpoint.

## Use Cases and Examples

### Ideal Use Cases

**Batch Processing:** Data analytics, video transcoding, rendering, ETL jobs  
*Example:* Researchers running Monte Carlo simulations for climate data, saving 80%+ on compute.

**Big Data Analytics:** Hadoop/Spark clusters, log/data analysis at scale  
*Example:* Media businesses processing petabytes of logs nightly on AWS EMR with Spot Instances.

**CI/CD Pipelines:** Short-lived build and test environments  
*Example:* SaaS providers using Spot Instances as Jenkins build agents for cost-effective, parallelized CI.

**Machine Learning Training:** Deep learning, hyperparameter tuning, checkpointed training on GPUs  
*Example:* Teams training neural networks on Spot GPU instances with autosave for interruption recovery.

**Containers and Microservices:** Stateless services orchestrated by Kubernetes or Docker Swarm

**Dev/Test Environments:** Non-production workloads where interruption is acceptable

**High-Performance Computing (HPC):** Genomic sequencing, financial modeling, scientific simulations

### Non-Ideal Use Cases

**Mission-Critical Applications:** Where high-availability and minimal downtime are paramount

**Stateful Apps Without Resilience:** Apps that cannot checkpoint state or recover from sudden termination

## Risks and Mitigation Strategies

### Key Risks

**Interruption Risk:** Instances can be terminated with as little as 30 seconds' notice

**Capacity Volatility:** Spot capacity can disappear unpredictably

**Pricing Fluctuations:** Spot prices can spike, especially for popular instance types

**No SLA:** Providers do not guarantee uptime or availability

### Mitigation Strategies

**Automation:**
- Use orchestration systems (Kubernetes, AWS Auto Scaling) to reschedule and replace interrupted workloads
- Blend Spot with On-Demand and Reserved Instances for resilience
- Employ automation platforms that manage lifecycles and fallback

**Application Design:**
- Architect services as stateless and leverage external storage
- Implement checkpointing to resume jobs after interruption
- Use loose coupling to tolerate node failures

**Proactive Monitoring:**
- Monitor interruption rates by region/type using tools like AWS Spot Instance Advisor
- Act on rebalance recommendations to migrate workloads early

**Diversification:**
- Use mix of instance types and regions to avoid "herd" interruptions
- Set sensible max bids to reduce risk of sudden eviction

## Best Practices

**1. Start with Non-Critical Workloads**  
Validate your interruption-handling strategies before moving critical workloads.

**2. Diversify**  
Use multiple instance types and availability zones for higher reliability.

**3. Automate**  
Employ AWS Spot Fleet, Auto Scaling Groups, or Kubernetes autoscalers.

**4. Monitor Trends**  
Use AWS Spot Price History and Spot Instance Advisor.

**5. Set Max Prices**  
Cap your bid at or below the On-Demand price.

**6. Plan for Interruption**  
Architect for fast recovery and zero data loss.

**7. Leverage Third-Party Tools**  
Try Cast AI or CloudZero for optimization and automation.

**8. Use Tags**  
Track usage and savings by team/project.

**9. Regularly Review**  
Update your mix and strategies based on usage reports.

## Billing and Pricing

**Spot Price:** Set by provider, fluctuates with market demand and supply

**Billing Granularity:** Per second after first minute (AWS, Azure, GCP)

**Termination Billing:** Generally, if AWS interrupts, you are not charged for the last partial hour; if you terminate, you pay for seconds used.

**Savings Tracking:** Use provider dashboards, AWS Spot Fleet savings reports, or third-party tools

**No Overlap with Savings Plans:** Spot usage does not contribute to AWS Savings Plans commitments

## Example Scenario

**Research Team Running Simulations**

A university research group needs to run thousands of Monte Carlo simulations for climate modeling. By using Spot Instances orchestrated by Kubernetes, they cut compute costs by 85% compared to On-Demand pricing. Checkpoints are saved to persistent storage before interruption, so jobs resume without loss.

## Frequently Asked Questions

**Q: Can I use Spot Instances for production workloads?**  
A: Yes, if your application is resilient to interruptions. Many organizations blend Spot with On-Demand or Reserved Instances for critical workloads.

**Q: How much can I save with Spot Instances?**  
A: Typically 70–90% compared to On-Demand, depending on region, type, and demand.

**Q: What happens when a Spot Instance is interrupted?**  
A: You receive a short interruption notice (2 minutes on AWS, 30 seconds on Azure/GCP). The instance is then terminated, stopped, or hibernated.

**Q: How do I request a Spot Instance?**  
A: Use the cloud provider's console, CLI, or API. Specify instance type, max price, and duration as needed.

**Q: Can Spot Instances be used with Kubernetes?**  
A: Yes, container orchestrators like Kubernetes can reschedule pods when a Spot Instance is interrupted.

**Q: Is there any SLA for Spot Instances?**  
A: No. Providers do not guarantee uptime or availability for Spot Instances.

## References

- [AWS Spot Instances Documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances.html)
- [AWS EC2 Spot Pricing](https://aws.amazon.com/ec2/spot/pricing/)
- [AWS Spot Interruptions](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-interruptions.html)
- [AWS Instance Rebalance Recommendations](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-interruptions.html#instance-rebalance-recommendations)
- [AWS Spot Use Cases](https://aws.amazon.com/ec2/spot/use-cases/)
- [AWS Spot HPC Use Case](https://aws.amazon.com/ec2/spot/use-cases/hpc/)
- [AWS Billing & Purchasing Options](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-purchasing-options.html)
- [AWS Spot Price History](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances-history.html)
- [AWS Spot Instance Advisor](https://aws.amazon.com/ec2/spot/instance-advisor/)
- [AWS EC2 Spot Fleet](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Fleets.html)
- [AWS Spot Requests](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-requests.html)
- [AWS Spot Savings](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-savings.html)
- [AWS Billing for Interrupted Spot Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/billing-for-interrupted-spot-instances.html)
- [AWS Spot Best Practices](https://aws.amazon.com/blogs/compute/best-practices-to-optimize-your-amazon-ec2-spot-instances-usage/)
- [AWS Spot FAQ](https://aws.amazon.com/ec2/spot/faqs/)
- [Google Cloud Spot VMs](https://cloud.google.com/compute/docs/instances/spot)
- [Google Cloud Spot Preemption](https://cloud.google.com/compute/docs/instances/spot#preemption)
- [Google Cloud Pricing](https://cloud.google.com/compute/pricing)
- [Azure Spot Virtual Machines](https://learn.microsoft.com/en-us/azure/virtual-machines/spot-vms)
- [Azure Spot Pricing](https://azure.microsoft.com/en-us/pricing/details/virtual-machines/spot/)
- [Spot.io: Azure Spot VMs Guide](https://spot.io/resources/azure-pricing/the-complete-guide/what-are-azure-spot-virtual-machines/)
- [Spot.io: Spot vs On-Demand](https://spot.io/resources/spot-instances/spot-instances-vs-on-demand-instances-pros-and-cons/)
- [Spot.io: Provider Comparison](https://spot.io/resources/spot-instances/spot-instances-aws-azure-google-cloud/)
- [Spot.io: Suitable Use Cases](https://spot.io/resources/spot-instances/spot-instances-aws-azure-google-cloud/#Suitable-Use-Cases-for-Spot-Instances)
- [Spot.io: Risks & Strategies](https://spot.io/resources/spot-instances/spot-instances-aws-azure-google-cloud/#Strategies-to-Optimize-the-Use-of-Spot-Instances)
- [Spot.io Ultimate Guide](https://spot.io/resources/spot-instances/spot-instances-aws-azure-google-cloud/)
- [Spot.io Eco](https://spot.io/products/eco/)
- [CloudZero Spot Instances Guide](https://www.cloudzero.com/blog/spot-instances/)
- [Infracost Spot Instances Glossary](https://www.infracost.io/glossary/spot-instances/)
- [Cast AI Spot Guide](https://cast.ai/blog/reduce-cloud-costs-with-spot-instances/)
- [Milvus AI Quick Reference: Spot Instances](https://milvus.io/ai-quick-reference/what-are-spot-instances-in-cloud-computing)
