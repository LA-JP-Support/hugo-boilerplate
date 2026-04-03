---
title: DynamoDB
date: 2025-03-01
lastmod: 2026-04-02
translationKey: dynamodb
description: DynamoDB is a fully managed NoSQL database service provided by AWS, offering high performance and automatic scalability.
keywords:
- NoSQL
- AWS
- database
- key-value store
- scalability
category: Cloud & Infrastructure
type: glossary
draft: false
url: /en/glossary/dynamodb/
---

## What is DynamoDB?

**DynamoDB is a fully managed NoSQL database service provided by AWS (Amazon Web Services).** It doesn't require pre-defined schemas and stores data as key-value pairs, offering flexible data structures. It automatically scales based on demand, handling everything from small applications to global services with billions of users on the same database. As an AWS managed service, AWS handles server management, backups, and high-availability configuration.

> **In a nutshell:** "A massive warehouse where you instantly retrieve goods (values) using product numbers (keys). The warehouse automatically expands."

**Key points:**

- **What it does:** Enables scalable, NoSQL-based data management
- **Why it's needed:** Handles large-scale, high-speed data processing that traditional relational databases struggle with
- **Who uses it:** Startups to enterprises needing real-time applications

## Why it matters

Traditional relational databases (RDBMs) optimize for structured data but struggle with scalability. As data grows, horizontal scaling (across multiple servers) becomes difficult, and schema changes require planning. DynamoDB solves these problems through NoSQL flexibility and automatic scaling. It frees developers from infrastructure management so they focus on applications.

## How it works

DynamoDB uses a key-value store architecture. Each table requires at least a partition key (primary search identifier). Optionally, a sort key orders data within partitions. For example, a user table might use user ID as partition key and registration date as sort key. Each row (item) can have any number of attributes without strict schema requirements.

Auto-scaling is a powerful feature—users specify capacity, and DynamoDB automatically adds resources when access increases. AWS distributes data across multiple partitions (server divisions) for scalability.

Global tables offer advanced distribution—replicate data across AWS regions for low-latency worldwide access.

## Basic information

| Item | Details |
|------|---------|
| Company | Amazon Web Services (AWS) - Amazon.com subsidiary |
| Service launch | January 2012 |
| Headquarters | United States (Seattle, Washington) |
| Delivery model | Managed service (FaaS) |
| Global support | Multi-region, global tables |

## Key features

DynamoDB optimizes for low-latency performance, delivering millisecond responses. Automatic scaling means users specify initial capacity and AWS handles everything else. High availability is built-in through multi-AZ (availability zone) replication with automatic failover.

Enterprise-grade security includes encryption, access control, and audit logs. Backup and point-in-time recovery simplify recovery from mistakes.

## Competing services

DynamoDB's main competitors are Google Cloud's "Firestore" and Microsoft Azure's "Cosmos DB." Firestore optimizes for mobile development with rich real-time sync features. Cosmos DB supports multiple data models (NoSQL, graph, table formats) with high flexibility.

On-premises environments use open-source NoSQL databases like MongoDB or Cassandra, which have lower initial costs but higher operational burdens. DynamoDB minimizes operational load but creates AWS lock-in risk.

## Real-world use cases

**Ecommerce product catalogs** Large ecommerce sites store millions of products in DynamoDB. Using product ID (partition key) provides instant access. Even during sales with concentrated traffic, DynamoDB's auto-scaling maintains performance.

**Game player rankings** Online games display real-time player score rankings. DynamoDB's key-value nature enables instant access to player scores with millisecond updates. Global tables let worldwide players play with low latency.

**IoT sensor data ingestion** When thousands of IoT sensors send data per second, DynamoDB captures and stores it rapidly. Auto-scaling means no management work when adding sensors. Queries instantly retrieve specific sensor or time-range data.

## Benefits and considerations

DynamoDB's biggest advantage is being fully managed—AWS handles infrastructure, so developers focus on applications. Auto-scaling handles unpredictable traffic, maintaining stable performance. High availability and security come by default, simplifying enterprise application development.

However, there are considerations. DynamoDB struggles with complex queries (multiple combined conditions), lacking traditional SQL flexibility. Its pricing model is complex, and inaccurate capacity prediction can cause unexpected bills. AWS dependence also creates vendor lock-in concerns.

## Related terms

- **[NoSQL](NoSQL.md)** — DynamoDB is a leading NoSQL database offering schema-free flexibility
- **[Auto-scaling](Auto-Scaling.md)** — DynamoDB automatically adjusts resources based on load
- **[Cloud computing](Cloud-Computing.md)** — DynamoDB is an AWS service using on-demand billing
- **[Microservices](Microservices.md)** — DynamoDB powers microservices architectures where each service has independent data stores
- **[API](API.md)** — applications use DynamoDB APIs; SDKs enable easy integration

## Frequently asked questions

**Q: When is DynamoDB the right choice?**

A: DynamoDB suits real-time applications (games, SNS, IoT), large-scale unpredictable traffic, and frequent schema changes. For complex JOIN operations or analytical queries, relational databases work better.

**Q: Does DynamoDB truly scale infinitely?**

A: Theoretically yes, but AWS account throughput limits and regional constraints apply. Ultra-large applications need to consult AWS support about limit increases.

**Q: Can data disappear?**

A: DynamoDB replicates across availability zones with automatic backups, making data loss extremely unlikely. However, for user error protection (full deletion), additional backup policies are recommended.
