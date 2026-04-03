---
title: API Gateway
date: 2025-12-19
lastmod: 2026-04-02
translationKey: API-Gateway
description: Central hub managing all API requests between clients and backend services, handling authentication, traffic control, and routing.
keywords:
- API Gateway
- Microservices
- API Management
- Load Balancing
- Traffic Control
category: Cloud & Infrastructure
type: glossary
draft: false
url: /en/glossary/api-gateway/
aliases:
- /en/glossary/API-Gateway/
---

## What is an API Gateway?

**An API Gateway sits between clients and multiple backend services, acting like a "building manager."** It manages all requests centrally, handling authentication, permission verification, traffic control, and routing—freeing backend services to focus on business logic.

> **In a nutshell:** "Like a receptionist fielding multiple department calls—screening callers, blocking suspicious calls, prioritizing urgent ones, and routing each to the right department."

**Key points:**

- **What it does:** Accepts all external requests, verifies access, controls traffic, and routes to appropriate internal systems
- **Why it matters:** Large systems with multiple services need centralized security and performance management for efficiency
- **Who uses it:** Infrastructure teams and architects implementing microservices architecture

## Why it matters

Large-scale systems require multiple independent services. Without an API Gateway, each client app must track service locations, authentication methods, and protocols—complexity grows exponentially. Gateways solve this: clients know one address; the Gateway routes internally. Services move or multiply without client changes. Critically, gateways centralize security checks and DDoS attack defense.

## How it works

API Gateway operates through four steps: request acceptance, authentication/control, routing, and response handling.

Client requests arrive; the Gateway receives them. It verifies [API Keys](api-keys/) or tokens ensure legitimate access (like checking building access credentials). Then it applies [Rate Limiting](api-rate-limiting/) ("this client: max 1000 requests/hour") blocking excessive traffic.

Based on request URL and method (GET, POST, etc.), the Gateway determines which backend service handles it and forwards the request. The response returns with format conversion or header additions before reaching the client.

## Real-world use cases

**E-commerce scaling**

Online shops juggle user authentication, product search, payments, and shipping. Apps use one Gateway address; the Gateway routes internally. During traffic spikes, the Gateway distributes requests across multiple payment servers preventing overload.

**Mobile app with multiple APIs**

Apps calling weather, maps, and ad-network APIs face different authentication methods. A Gateway between the app and services unifies authentication, so apps send consistent requests regardless of downstream differences.

**Threat protection**

Botnets attack via brute-force or unusual patterns. The Gateway detects and blocks suspicious traffic before reaching backends. Enterprise-wide security exists in one place.

## Benefits and considerations

Greatest benefits: **complexity abstraction and centralized management.** Clients see one address; the Gateway manages complexity. **Caching** stores frequent data at the Gateway, reducing backend load. **Unified security policy** applies everywhere with quick threat responses.

Critical risk: **Gateway becomes a bottleneck.** All traffic flows through it; Gateway failure means system-wide outage. Gateways need high availability (multiple redundant units). Configuration complexity can breed bugs and vulnerabilities.

## Related terms

- **[API Management](api-management/)** — Full lifecycle API management including Gateways
- **[API Rate Limiting](api-rate-limiting/)** — Gateway-implemented traffic control feature
- **[Microservices](microservices/)** — Architecture style where Gateways excel
- **[Load Balancing](load-balancing/)** — Gateway feature distributing traffic across servers
- **[API Security](api-security/)** — Authentication/authorization managed at Gateways

## Frequently asked questions

**Q: How do API Gateways differ from load balancers?**

A: Load balancers distribute traffic across servers at network layer, specializing in traffic distribution. Gateways work at application layer, providing authentication, routing, rate limiting, and data transformation—higher-level functionality. Modern Gateways include load-balancing capabilities.

**Q: How prevent API Gateway downtime?**

A: Eliminate single points of failure with redundant Gateway instances. Client requests auto-distribute across multiple Gateways. Add load-balancing above Gateways too. Health checks quickly detect failures; auto-failover switches to healthy Gateways.

**Q: Benefits of cloud-managed API Gateways?**

A: AWS API Gateway or Google Cloud handle scaling and availability automatically—less operational burden. However, custom-built solutions (Kong) work better for specific requirements or cost-focused situations. Match requirements to solution choice.
