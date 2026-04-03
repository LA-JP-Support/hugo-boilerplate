---
title: "Lambda"
date: 2025-03-01
lastmod: 2026-04-02
description: "AWS's Function as a Service product. Execute code without server management"
translationKey: "lambda"
category: "Cloud & Infrastructure"
type: glossary
draft: false
url: /en/glossary/Lambda/
keywords:
  - AWS Lambda
  - Serverless
  - Cloud Functions
  - FaaS
  - Amazon Web Services
---

## Basic Information

| Item | Details |
|------|---------|
| Parent Company | Amazon Web Services (AWS) |
| Service Launch | 2014 |
| Service Type | Function as a Service (FaaS) |
| Supported Languages | Python, Node.js, Java, Go, C#, Ruby, custom runtimes |
| Execution Time Limit | Maximum 15 minutes |

## Key Features and Services

**AWS Lambda is a service specialized in code execution.** Developers write code in Python or JavaScript and upload it to the AWS Lambda management console, where it runs on the internet. It supports multiple language runtimes, with the latest versions (Python 3.11, Node.js 18, etc.) immediately available.

Lambda offers rich trigger mechanisms: HTTP requests (via API Gateway), S3 bucket file uploads, DynamoDB table changes, CloudWatch schedules, and SNS message receipts can all trigger function execution. Detailed execution logs are automatically saved to CloudWatch Logs, making debugging and monitoring easy.

Scaling is completely automatic—even with hundreds of simultaneous requests, AWS automatically increases execution environments. Billing is calculated as a combination of "execution count" and "memory × execution time," with 1 million monthly executions provided free, so small applications often cost nothing.

## Competing Services

**Google Cloud Functions**

Google Cloud's FaaS service with the same basic concept as Lambda. It supports multiple languages (Python, Node.js, Go, Java) at comparable pricing. Its strength is integration with the Google Cloud ecosystem (BigQuery, Cloud Datastore), making it popular with data-driven companies.

**Azure Functions**

Microsoft's FaaS service supporting .NET, JavaScript, Python, and Java. Strong integration with Microsoft 365 and Dynamics 365 makes it popular with enterprise customers, particularly Windows-based organizations. Pricing tends to be slightly higher than Lambda.

**Kubernetes + Knative**

A technology stack for building FaaS-like function execution environments on your own servers. While offering full control, operational complexity is high, requiring you to manage scaling and maintenance yourself.

## Real-World Use Cases

**Automated Image Processing Pipeline**

In a photo-sharing application, when users upload images, an S3 trigger automatically executes a Lambda function to instantly generate multiple thumbnail sizes, extract metadata, and perform AI-based content moderation. Previously requiring constantly-running worker servers, Lambda reduces costs to only the actual processing execution time.

**Real-Time Log Processing**

When IoT devices or web servers send thousands of logs per second, Kinesis streams send each log to Lambda functions in real-time for automatic anomaly detection, aggregation, and notifications. Lambda auto-scales during traffic spikes, eliminating concerns about processing failures.

**Scheduled Maintenance Tasks**

Nightly database backups, monthly report generation, and account deactivation checks are implemented with Lambda. Simply specify the time in CloudWatch Events (now EventBridge) to auto-execute Lambda functions.

## Benefits and Considerations

**Lambda's greatest benefit is "focus on business logic."** Server management, OS patching, and scaling configuration are all automated by AWS, so developers concentrate solely on code implementation. Usage-based billing for execution time and count lets startups leverage AWS's scalability with zero initial investment. Direct integration with many AWS services (S3, DynamoDB, SQS) enables building serverless architectures concisely.

However, limitations exist. The 15-minute execution time limit makes it unsuitable for longer-running tasks. Stateful processing (retaining data across multiple executions) is difficult, requiring external services (RDS, DynamoDB) and increasing implementation complexity. Additionally, there's vendor lock-in risk. Dependency on Lambda-specific features (IAM role integration, VPC connections, custom runtimes) makes migration to other cloud providers difficult. Debugging is also challenging, as local reproduction is hard and relies on CloudWatch Logs.

## Frequently Asked Questions

**Q: Can I implement complex workflows by combining multiple Lambda functions?**

A: Yes. Using AWS Step Functions, you can combine multiple Lambda functions to define workflow logic including conditional branching, parallel execution, and retries. However, complex workflows risk reduced maintainability, so it's important to design with the single responsibility principle in mind.

**Q: What should I do if my Lambda function needs long-running computations?**

A: If exceeding the 15-minute limit, split the processing and distribute it across multiple Lambda functions, or use constantly-running compute like [Kubernetes](Kubernetes-K8s.md) or EC2 instances. Alternatively, queue processing in SQS and have worker Lambda functions handle it asynchronously.

**Q: Is Lambda really "serverless"?**

A: From a developer perspective, "serverless" means "no server management," but AWS maintains enormous server infrastructure behind the scenes. Understand it as "no server management burden" and "automatic scaling"—this is a more accurate definition of "serverless."
