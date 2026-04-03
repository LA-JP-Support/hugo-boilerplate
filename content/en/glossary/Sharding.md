---
title: Sharding
date: '2025-12-19'
lastmod: 2026-04-02
translationKey: sharding
description: Database technique splitting large data across servers for scalability and performance improvements.
keywords:
- Sharding
- Database Scaling
- Horizontal Partitioning
- Shard Key
- System Design
category: Data & Analytics
type: glossary
draft: false
url: /en/glossary/sharding/
---

## What is Sharding?

**Sharding splits large databases into smaller pieces (shards) stored on different servers.** Single servers have data and processing limits. Sharding overcomes these by dividing data. Each shard is independent, and together they form the complete dataset.

> **In a nutshell:** Like dividing products into multiple boxes and storing each in a different warehouse.

**Key points:**

- **What it does:** Split data across multiple servers to spread processing load
- **Why it matters:** Scale beyond single-server limits while keeping performance
- **Who uses it:** Companies handling massive data and high traffic

## Why it matters

Without sharding, growing users/data becomes impossible. Twitter with hundreds of millions of users can't store all data on one server. Sharding solves this by spreading data. Each shard handles less, so queries are fast. Failure in one shard doesn't crash others.

## How it works

**Shard key selection:** Pick the column (user ID, region, date) that determines which shard data goes to. Must be stable and evenly distributed.

**Data distribution:** Use hash or range rules to assign data to shards based on the shard key.

**Query routing:** Application directs each operation to the correct shard.

Can work at application level (app decides routing) or database level (DBMS handles it).

## Sharding vs. Partitioning

**Partitioning:** Splits data into segments, usually within one database.

**Sharding:** Horizontal partitioning specifically—splits rows across separate databases on different machines.

Partitioning typically stays in one machine, so it doesn't scale out. Sharding distributes across machines, enabling true scale-out.

## Why use sharding

Single-node limits:

**Storage:** Finite disk/memory per server.

**Compute:** Limited concurrent queries/writes possible.

**Network:** Throughput becomes a bottleneck.

**Geography:** Storing everything at one site causes latency and regulatory issues.

Sharding overcomes these by spreading data and load across many machines.

## When to use sharding

**Good scenarios:**
- Data exceeds single server capacity
- Write/read throughput needs exceed single server+replicas
- Multi-tenant: isolate each tenant's data
- Regulatory: need location-specific data storage
- Need independent tenant/region/domain scaling

**Bad scenarios:**
- Small/medium data works fine with vertical scaling
- Simpler optimizations (indexing, caching) suffice
- Management complexity outweighs benefits

**Guidance:** Always exhaust vertical scaling, replication, and optimization before sharding.

## Benefits and challenges

**Benefits:** Unlimited scaling potential. Fast queries (smaller datasets). Failure containment (one shard failure doesn't affect others).

**Challenges:** Complex to manage multiple databases. Poor shard key choices create hot spots (unbalanced traffic). Cross-shard queries are difficult. Changing sharding strategy after launch is very hard.

## Real-world examples

**Social media (Twitter, Facebook)**
Shard by user ID. Each shard manages a user subset's posts and follows. Scales with user growth.

**E-commerce (Amazon)**
Shard order/product data by customer ID or region. Parallelize workload, improve query speed.

**Search engines (Google, Yahoo)**
Shard global web index by region or query type. Deliver search results quickly worldwide.

## Related terms

- **[Database Scaling](Database-Scaling.md)** — Sharding is one scaling method; others include vertical and replication
- **[Caching](Caching.md)** — Combine with sharding for better performance
- **[Distributed Systems](Distributed-Systems.md)** — Sharding forms distributed database foundation
- **[Load Balancing](Load-Balancing.md)** — Distribute requests evenly across shards

## Frequently asked questions

**Q: How does sharding differ from replication?**
A: Sharding splits data for scalability. Replication copies data for availability and read speed.

**Q: Can we reverse sharding after implementing it?**
A: Very difficult. Massive migration complexity. Plan carefully upfront.

**Q: Do small companies need sharding?**
A: Usually no. Sharding's complexity suits large data companies. Small companies use caching and read replicas.
