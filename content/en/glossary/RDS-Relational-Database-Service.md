---
title: RDS (Relational Database Service)
date: 2025-03-01
lastmod: 2026-04-02
translationKey: rds-relational-database-service
description: RDS is AWS's fully managed relational database service, automating database operations like patching, backups, and replication so organizations can focus on application development.
keywords:
- relational database
- AWS
- SQL
- managed service
- backup
category: Cloud & Infrastructure
type: glossary
draft: false
url: /en/glossary/RDS-Relational-Database-Service/
---

## What is RDS (Relational Database Service)?

**RDS is a fully managed relational database service provided by AWS (Amazon Web Services).** Supporting multiple database engines—MySQL, PostgreSQL, MariaDB, Oracle Database, SQL Server—users select the optimal engine. AWS automatically manages database installation, patching, backups, replication, and failover, enabling users to focus on database design and application development rather than operations.

> **In a nutshell:** Outsourcing complex in-house database system operations to external specialists, focusing on data utilization only.

**Key points:**

- **What it does:** Use enterprise-grade relational databases without complex management
- **Why it's needed:** Reduce operational burden while ensuring high availability and performance
- **Who uses it:** Organizations from enterprises to SMBs needing structured data management

## Why it matters

Traditionally, operating relational databases required dedicated DBAs (database administrators), extensive management work—server procurement, installation, monitoring, backups, security patches—requiring specialized expertise making difficult for small businesses. Hardware failure recovery also required enterprise responsibility, demanding 24/7 monitoring to ensure business continuity.

RDS dramatically reduced these burdens. AWS automates most management, letting users focus only on "what" and "where" to store. Multi-AZ (multiple availability zone) deployment enables automatic failover during hardware failures, ensuring business continuity. Now organizations of all sizes—startups to enterprises—can access enterprise-grade databases.

## How it works

RDS operates through completely managed infrastructure and powerful automation.

When creating RDS instances, users need only database engine type, instance class (memory/CPU combination), storage capacity, and username/password. AWS configures databases within minutes in a connected state. Behind the scenes, AWS automates complex tasks—physical server allocation, OS setup, database installation, security configuration.

Operationally, AWS automatically does the following. Patch management (security updates) applies automatically regularly. Backups run daily with weeks of retention for disaster recovery. [Auto-scaling](Auto-Scaling.md) automatically expands storage when approaching capacity. Multi-AZ deployments automatically failover to standby replicas during failures, providing zero-downtime recovery.

To improve read performance, configure multiple read-only replicas. This prevents reporting and analysis processing from affecting main database.

## Key information

| Item | Details |
|------|---------|
| Provider | Amazon Web Services (AWS) - Amazon.com subsidiary |
| Launch date | October 2009 |
| Headquarters | USA (Washington, Seattle) |
| Supported databases | MySQL, PostgreSQL, MariaDB, Oracle Database, SQL Server |
| Deployment | Single-AZ, Multi-AZ, read-only replica support |

## Primary features

RCS provides automatic backup and recovery capabilities protecting data against mistakes and disasters. Point-in-time recovery (PITR) restores databases to any point up to 35 days ago.

High availability is RCS's core. Multi-AZ deployment places synchronous standby replicas in different availability zones, automatically failover during main failures. RTO (recovery time objective) and RPO (recovery point objective) reach seconds to minutes, ensuring business continuity.

Security features are comprehensive—network isolation (VPC placement), encryption (in-transit and at-rest), IAM authentication, audit logging.

## Competitors and alternatives

RCS's main competitors are Google Cloud's "Cloud SQL" and Microsoft Azure's "Azure Database." Cloud SQL excels in Google Cloud/Workspace integration with small-app pricing. Azure Database strengthens Microsoft ecosystem (Active Directory, Office 365) integration.

On-premises alternatives include open-source MySQL, PostgreSQL, or Oracle's commercial database. These have lower (or free) license costs but significant operational management burden, typically requiring DBA placement.

## Real-world use cases

**Large-scale e-commerce customer database**
E-commerce sites with millions of customers use RCS Multi-AZ. Auto-backups and read-only replicas enable fast customer order processing simultaneously with analytics team analysis. Hardware failures trigger automatic failover within seconds, minimizing user impact.

**Financial institution transaction records**
Banks manage customer transaction records via RCS. Audit logging records all database access, simplifying regulatory compliance (PCI-DSS, GDPR). Multi-region replication enables transaction continuation from overseas branches if headquarters systems fail—business continuity achieved.

**SaaS company customer isolation**
Multi-tenant SaaS companies support multiple customers on single RCS instances via embedded customer IDs in tables. Read-only replicas distribute per-customer report generation load while optimizing costs.

## Benefits and considerations

RCS's main benefit is dramatically reduced operational complexity. Small enterprises without DBAs can operate enterprise-grade databases. Auto-backups, patch management, failover ensure high availability and security. Read-only replicas flexibly enable scalability.

Considerations exist. Complex query optimization and large-scale migration remain user responsibility. Unlike [DynamoDB](DynamoDB.md) and other NoSQL databases, schema changes can cause downtime. License-based engines (Oracle, SQL Server) can be expensive.

## Related terms

- **[Relational Database](Relational-Database.md)** — RCS is the leading managed relational database service
- **[Backup](Backup.md)** — RCS auto-backup enables disaster recovery
- **[VPC](VPC-Virtual-Private-Cloud.md)** — RCS instances typically deploy in VPC for network security
- **[Security](Security.md)** — Encryption, IAM, audit logging address enterprise requirements
- **[High Availability](High-Availability.md)** — Multi-AZ and auto-failover ensure business continuity

## Frequently asked questions

**Q: Is RCS or on-premises database cheaper?**
A: Initial costs favor on-premises, but total cost of ownership (TCO) usually favors RCS. Including personnel costs, hardware replacement, power expenses, long-term RCS is typically more economical.

**Q: Are there RCS data size limits?**
A: Per-instance storage limits reach several TB, but table partitioning (sharding) and replicas theoretically enable unlimited scaling. For massive cases, AWS support consultation is needed.

**Q: Can we migrate from RCS to another database?**
A: Yes. AWS Database Migration Service (DMS) enables RCS to other database migration. Continuous replication minimizes downtime.
