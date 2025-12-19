---
title: "Serverless Computing"
date: 2025-11-25
lastmod: 2025-12-05
translationKey: "serverless-computing"
description: "Serverless computing is a cloud execution model where providers manage infrastructure, allowing developers to build and deploy applications without provisioning or scaling servers."
keywords: ["serverless computing", "cloud computing", "FaaS", "BaaS", "AWS Lambda"]
category: "AI Infrastructure & Deployment"
type: "glossary"
draft: false
---
## 1. Introductory Definition

Serverless computing is a cloud execution model in which cloud providers (like AWS, Google Cloud, Azure, IBM Cloud, and others) automatically manage the infrastructure required to run application code. This model enables developers to build and deploy applications without provisioning, operating, or scaling servers themselves. Despite the term, physical servers are always involved; "serverless" refers to the abstraction of server management, shifting operational responsibilities to the vendor. Developers focus exclusively on writing business logic, while the underlying compute, networking, scaling, patching, and fault tolerance are handled by the provider. ([AWS](https://aws.amazon.com/what-is/serverless-computing/), [Google Cloud](https://cloud.google.com/discover/what-is-serverless-computing), [IBM](https://www.ibm.com/think/topics/serverless), [Alpacked](https://alpacked.io/blog/what-is-serverless-computing/))

## 2. What is Serverless Computing?

Serverless computing is a paradigm where application owners are relieved from the responsibility of provisioning, scaling, and managing servers. All applications ultimately run on servers, but in serverless, these resources are managed, orchestrated, and scaled dynamically by the cloud provider. This approach allows developers to focus on the core business logic and application code, deploying it as discrete functions or microservices that respond to specific events.

**Key characteristics:**
- **Infrastructure abstraction:** Developers never interact directly with compute resources. The cloud provider handles all server lifecycle management and scaling.
- **Event-driven execution:** Code is deployed as functions that are triggered by events (HTTP requests, file uploads, database changes, scheduled tasks).
- **Pay-per-use pricing:** Billing is based solely on execution metrics—such as the number of requests, execution duration, and resources consumed—resulting in no charges for idle or unused capacity.
- **Short-lived, stateless functions:** Serverless functions are typically designed for short, atomic execution. Any state is stored externally, such as in databases or object storage.
- **Rapid deployments:** Deployment involves uploading code to the cloud, with updates requiring only code replacement and redeployment.

**Analogy:** Serverless computing can be compared to using a utility like water or electricity: as a user, you simply turn the tap or flip a switch, consuming only what you need and paying accordingly, with no concern for the underlying infrastructure. ([Google Cloud](https://cloud.google.com/discover/what-is-serverless-computing))

## 3. How Does Serverless Work?

Serverless architectures operate on an event-driven model. Functions—discrete, stateless units of logic—are invoked in response to external or internal triggers. The lifecycle of a serverless function typically follows these steps:

1. **Trigger:** An event, such as an HTTP request, file upload, message queue update, or scheduled timer, initiates the execution of a function.
2. **Provisioning:** The provider allocates necessary compute resources (CPU, memory, networking) within milliseconds, often using [containerization](/en/glossary/containerization/) technology under the hood.
3. **Execution:** The function runs, processes the event, and returns a result. Execution environments are ephemeral.
4. **Scaling & Termination:** The provider can instantly scale to handle multiple concurrent events by running multiple instances in parallel. When there are no more events, resources are deallocated, and the environment can "scale to zero."

**Key features:**
- **Autoscaling:** Instantly scales from zero to millions of requests, without manual intervention or configuration.
- **Statelessness:** Each execution is isolated. Persistent state, if needed, must be managed through external storage (e.g., cloud databases, distributed caches).
- **Short-lived tasks:** Functions are optimized for quick execution, commonly with upper limits on runtime (e.g., AWS Lambda has a 15-minute limit).

**Example:**  
A user uploads an image to a cloud storage bucket. The upload event triggers a serverless function that resizes the image and stores different variants back into the bucket for use in different contexts (thumbnails, previews, etc.).

**Further reading:**  
- [Alpacked: What is Serverless Computing](https://alpacked.io/blog/what-is-serverless-computing/)
- [TechTarget: Top benefits and disadvantages](https://www.techtarget.com/searchcloudcomputing/tip/Top-benefits-and-disadvantages-of-serverless-computing)
- [Okta: Uses, Advantages, Disadvantages](https://www.okta.com/identity-101/serverless-computing/)

## 4. Serverless vs. Other Cloud Models

| Attribute             | Serverless          | PaaS                | Containers           | VMs                  |
|-----------------------|--------------------|---------------------|----------------------|----------------------|
| **Admin Burden**      | Minimal            | Medium              | Medium–High          | High                 |
| **Cost Model**        | Pay-per-use        | Pay-per-instance    | Pay-per-container    | Pay-per-VM           |
| **Maintenance**       | None               | Low                 | Medium               | High                 |
| **Scalability**       | Automatic, instant | Manual/Auto         | Manual/Auto          | Manual/Auto          |
| **Statelessness**     | Typically stateless| Stateful/stateless  | Stateful/stateless   | Stateful/stateless   |
| **Provisioning Time** | Milliseconds       | Minutes             | Minutes              | Minutes–Hours        |
| **Idle Cost**         | $0                 | Incurred            | Incurred             | Incurred             |

- **Serverless** abstracts nearly all infrastructure management and scales seamlessly to demand, billing only for actual usage.
- **PaaS** reduces some operational overhead but typically requires manual scaling and incurs costs for running instances, even when idle.
- **Containers** provide portability and flexibility but require orchestration, scaling, and lifecycle management.
- **VMs** offer full control but place administrative responsibility and scaling on the user.

**Further reading:**  
- [Google Cloud comparison](https://cloud.google.com/discover/what-is-serverless-computing)
- [IBM Serverless](https://www.ibm.com/think/topics/serverless)
- [Alpacked: Serverless vs Containers](https://alpacked.io/blog/what-is-serverless-computing/#Serverless%20VS%20containers)

## 5. Types of Serverless Architecture

### Function as a Service (FaaS)

**Definition:**  
FaaS allows developers to deploy individual functions or code snippets that are executed in response to events. The platform handles the orchestration, scaling, and lifecycle of these functions.

**Key characteristics:**  
- Event-driven
- Stateless
- Short-lived executions
- Automatic scaling

**Examples:**  
- [AWS Lambda](https://aws.amazon.com/lambda/)
- [Google Cloud Functions](https://cloud.google.com/functions)
- [Azure Functions](https://azure.microsoft.com/en-us/products/functions/)
- [IBM Cloud Code Engine](https://cloud.ibm.com/codeengine)

### Backend as a Service (BaaS)

**Definition:**  
BaaS offers managed backend services such as databases, authentication, messaging, and storage through APIs, eliminating the need for custom backend code or infrastructure.

**Examples:**  
- [Firebase](https://firebase.google.com/)
- [AWS Amplify](https://aws.amazon.com/amplify/)
- [Auth0](https://auth0.com/)

### Other Serverless Forms

- **Serverless Databases:** Automatically scale database capacity (e.g., [Amazon Aurora Serverless](https://aws.amazon.com/rds/aurora/serverless/)).
- **Serverless Containers:** Run containers without managing servers (e.g., [AWS Fargate](https://aws.amazon.com/fargate/), [Google Cloud Run](https://cloud.google.com/run)).
- **Serverless Edge Computing:** Executes functions closer to end-users for lower [latency](/en/glossary/latency/) ([Cloudflare Workers](https://workers.cloudflare.com/)).
- **Serverless Event Streaming:** Managed event pipelines ([Azure Event Grid](https://azure.microsoft.com/en-us/products/event-grid/), [AWS EventBridge](https://aws.amazon.com/eventbridge/)).

**Further reading:**  
- [Alpacked: Serverless application components](https://alpacked.io/blog/what-is-serverless-computing/#How%20does%20serverless%20computing%20work?)
- [Red Hat: What is FaaS?](https://www.redhat.com/en/topics/cloud-native-apps/what-is-faas)

## 6. Advantages and Disadvantages of Serverless Computing

### Advantages

**Cost Efficiency:**  
Billing is strictly based on actual compute consumption—no costs for idle capacity or pre-provisioned infrastructure. This is particularly cost-effective for variable workloads. ([TechTarget](https://www.techtarget.com/searchcloudcomputing/tip/Top-benefits-and-disadvantages-of-serverless-computing), [Alpacked](https://alpacked.io/blog/what-is-serverless-computing/))

**Operational Efficiency:**  
Cloud providers handle server provisioning, patching, updates, and scaling, freeing developers from infrastructure management and accelerating deployment cycles.

**Automatic & Infinite Scalability:**  
Serverless functions scale seamlessly to accommodate unpredictable or fluctuating workloads, ensuring applications remain responsive regardless of demand spikes.

**Accelerated Development Velocity:**  
Developers focus on business logic and feature development, resulting in faster time-to-market and improved product quality.

**Simplified Backend Code:**  
Serverless architectures promote modular, microservices-oriented design, which enhances maintainability and supports rapid iteration.

**Integrated Ecosystem:**  
Major cloud providers offer integrated services (e.g., databases, AI/machine learning, messaging) that work natively with serverless platforms.

### Disadvantages

**Cold Start Latency:**  
Functions may experience additional startup latency, known as "cold starts," when invoked after periods of inactivity. This can impact user experience in latency-sensitive applications.

**Vendor Lock-In:**  
Migrating serverless workloads between cloud providers can be complex, as proprietary APIs, configurations, and runtimes may not be portable. ([Okta](https://www.okta.com/identity-101/serverless-computing/))

**Limited Control:**  
Developers have less visibility and fewer customization options for the runtime environment, networking, and security controls compared to traditional models.

**Suitability Constraints:**  
Serverless is less ideal for long-running or stateful applications, as most platforms impose execution time limits and require external state management.

**Debugging and Monitoring Complexity:**  
Abstraction of infrastructure can hinder deep troubleshooting, log aggregation, and system tracing.

**Potential Higher Cost for Long-Running Processes:**  
For compute-intensive, long-duration tasks, serverless pricing may exceed that of reserved or dedicated infrastructure.

**Security Considerations:**  
Each function can be a potential attack entry point, increasing the attack surface if not properly secured. ([TechTarget](https://www.techtarget.com/searchcloudcomputing/tip/Top-benefits-and-disadvantages-of-serverless-computing))

**Further reading:**  
- [Okta: Serverless Computing: Uses, Advantages, and Disadvantages](https://www.okta.com/identity-101/serverless-computing/)
- [TechTarget: Top benefits and disadvantages](https://www.techtarget.com/searchcloudcomputing/tip/Top-benefits-and-disadvantages-of-serverless-computing)
- [Alpacked: Benefits and Limitations](https://alpacked.io/blog/what-is-serverless-computing/#Benefits%20of%20the%20serverless%20architecture)

## 7. Common and Emerging Use Cases

Serverless computing is used across a range of industries and technical domains, with particular suitability for event-driven, stateless, or highly scalable applications.

### API Backends
- Build scalable APIs using serverless functions as endpoints.
- *Example:* [Coca-Cola Freestyle](https://aws.amazon.com/solutions/case-studies/coca-cola-freestyle/) uses AWS Lambda for mobile app backend.

### Real-Time Data Processing and Analytics
- Process streaming data from IoT, user activity, or logs for immediate insights.
- *Example:* [Genentech](https://aws.amazon.com/solutions/case-studies/genentech1/) utilizes AWS Lambda for rapid clinical data analysis.

### Batch Processing
- Perform high-volume ETL, data backups, or reporting jobs.
- *Example:* [Liberty Mutual](https://aws.amazon.com/solutions/case-studies/liberty-mutual-case-study/) processes 100 million global financial transactions using serverless workflows.

### Business Process Automation
- Automate workflows, data pipelines, and system integrations.
- *Example:* [Taco Bell](https://aws.amazon.com/solutions/case-studies/taco-bell/) delivers real-time menu data to partners using serverless.

### Image and Video Processing
- Automatically generate image thumbnails, optimize video streams, or convert file formats upon upload.

### AI Inference & Applications
- Host scalable AI endpoints for real-time inference, chatbots, or recommendation engines.
- *Example:* [Google Cloud Run](https://cloud.google.com/run) integrates serverless with AI model deployment.

### IoT and Event-Driven Apps
- Respond to unpredictable device events or sensor data.

### DevOps & CI/CD Automation
- Automate build, testing, and deployment pipelines using serverless triggers.

### Third-Party Integrations and Scheduled Tasks
- Sync data between SaaS tools, generate scheduled reports, or run periodic jobs without dedicated infrastructure.

**Further reading:**  
- [AWS: What are the use cases?](https://aws.amazon.com/what-is/serverless-computing/#what-are-the-use-cases-of-serverless-computing--15dcg8p)
- [Google Cloud: Use Cases](https://cloud.google.com/discover/what-is-serverless-computing)
- [IBM: Common Applications](https://www.ibm.com/think/topics/serverless)

## 8. Security & Operations

### Shared Responsibility Model

- **Cloud Provider Responsibilities:**  
  Secure the infrastructure, virtualization, OS patching, and managed backend services.
- **Customer Responsibilities:**  
  Secure application code, manage identity and access (IAM policies), validate inputs, and protect API endpoints.

### Best Practices for Securing Serverless Applications

- **Principle of Least Privilege:** Assign minimal permissions to functions and services.
- **Input Validation:** Sanitize and validate all incoming data to prevent injection and other attacks.
- **Monitoring and Logging:** Use integrated tools (AWS CloudWatch, Google Cloud Monitoring, IBM Log Analysis) for real-time monitoring, anomaly detection, and troubleshooting.
- **API Security:** Protect endpoints with authentication, authorization, and rate limiting (e.g., API Gateway).
- **Dependency Management:** Regularly update and audit third-party packages to reduce vulnerabilities.
- **Network Controls:** Restrict function network access, using VPC integration or firewall rules where available.

**Further reading:**  
- [AWS: Security in Serverless](https://aws.amazon.com/what-is/serverless-computing/#is-serverless-architecture-secure--15dcg8p)
- [IBM: Serverless Security](https://www.ibm.com/think/topics/serverless)
- [TechTarget: Serverless security risks](https://www.techtarget.com/searchcloudcomputing/tip/Top-benefits-and-disadvantages-of-serverless-computing)

## 9. Getting Started / Next Steps

### Try Serverless Services
- [AWS Lambda](https://aws.amazon.com/lambda/)
- [Google Cloud Functions](https://cloud.google.com/functions)
- [IBM Cloud Code Engine](https://cloud.ibm.com/codeengine)
- [Azure Functions](https://azure.microsoft.com/en-us/products/functions/)
- [Red Hat OpenShift Serverless](https://www.redhat.com/en/technologies/cloud-computing/openshift/serverless)

### Tutorials & Hands-On Labs
- [IBM Cloud Code Engine “Hello World”](https://cloud.ibm.com/docs/codeengine?topic=codeengine-application-workloads)
- [AWS Serverless Getting Started](https://aws.amazon.com/getting-started/hands-on/run-serverless-code/)
- [Google Cloud Run Quickstart](https://cloud.google.com/run/docs/quickstarts)

### In-Depth Learning
- [Serverless Essentials by Google Cloud (YouTube, 8:20)](https://www.youtube.com/watch?v=PBw9vD_BO5A)
- [Red Hat: What is Serverless?](https://www.redhat.com/en/topics/cloud-native-apps/what-is-serverless)
- [IBM: What is Serverless Computing?](https://www.ibm.com/think/topics/serverless)

**Start building your first serverless application today.**  
[Sign up for a free AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html), get [Google Cloud credits](https://console.cloud.google.com/freetrial), or try the [IBM Cloud free tier](https://cloud.ibm.com/registration).

## 10. References & Further Reading

- [AWS: What is Serverless Computing?](https://aws.amazon.com/what-is/serverless-computing/)
- [Google Cloud: What is Serverless Computing?](https://cloud.google.com/discover/what-is-serverless-computing)
- [Red Hat: What is Serverless?](https://www.redhat.com/en/topics/cloud-native-apps/what-is-serverless)
- [IBM: What is Serverless Computing?](https://www.ibm.com/think/topics/serverless)
- [ALPACKED: Full Guide to Serverless](https://alpacked.io/blog/what-is-serverless-computing/)
- [TechTarget: Top benefits and disadvantages](https://www.techtarget.com/searchcloudcomputing/tip/Top-benefits-and-disadvantages-of-serverless-computing)
- [Okta: Serverless Computing](https://www.okta.com/identity-101/serverless-computing/)
- [YouTube: Serverless Essentials by Google Cloud](https://www.youtube.com/watch?v=PBw9vD_BO5A)
- [OpenShift Serverless](https://www.redhat.com/en/technologies/cloud-computing/openshift/serverless)
- [Knative: Serverless on Kubernetes](https://knative.dev/)
- [Cloudflare Workers: Serverless at the Edge](https://workers.cloudflare.com/)

## Related Glossary Entries

- [Function as a Service (FaaS)](https://www.redhat.com/en/topics/cloud-native-apps/what-is-faas)
- [Backend as a Service (BaaS)](https://firebase.google.com/)
-
