---
title: Load Balancing
date: 2026-04-02
lastmod: 2026-04-02
translationKey: load-balancing
description: A technology that distributes network traffic across multiple servers to optimize application availability, reliability, and performance.
keywords:
- load balancing
- load balancer
- network traffic
- server scalability
- application performance
category: Cloud & Infrastructure
type: glossary
draft: false
url: /en/glossary/Load-Balancing/
---

## What is Load Balancing?

**Load balancing distributes incoming network traffic across multiple backend servers equally.** A central [load balancer](Load-Balancer.md) receives client requests and routes them to the optimal server based on algorithm and server health. This prevents single-server overload.

> **In a nutshell:** Like a restaurant with multiple servers—the host guides arriving customers to less-busy tables.

**Key points:**
- **What it does:** Distribute traffic across multiple servers
- **Why it matters:** Prevent downtime, improve response speed
- **Who uses it:** High-traffic sites, [cloud services](Cloud-Computing.md), API servers

## Why it matters

Without load balancing, traffic concentration causes server overload and service stoppage. Distributing load across multiple servers means one server failure doesn't stop service—others process requests, achieving **high availability**. Also improves user experience, system reliability, infrastructure efficiency.

## How it works

Load balancing operates in 4 main steps:

First, load balancer **receives client requests**. Next, health checks (monitoring) confirm responsive servers. Then using algorithms like round-robin (rotating sequence) or minimum-connection (choosing least-loaded server), it selects optimal server. Finally, it forwards requests and returns responses to clients.

Like library receptionists guiding customers to shortest-wait windows, load balancers efficiently distribute requests.

## Real-world use cases

**E-commerce sale traffic spikes**
During sale periods, traffic surge is distributed across multiple web servers. Load balancers monitor each server's load, automatically controlling traffic, preventing site stoppage.

**Streaming services**
Worldwide user access is distributed to geographically-dispersed server groups. Serving from nearest server reduces latency and improves playback quality.

**API infrastructure**
[Microservices](Microservices.md) architecture with multiple API servers uses load balancers for even distribution. Partial server stoppage doesn't stop processing.

## Benefits and considerations

**Benefits** include high availability, [performance](Performance.md) improvement, scalability assurance. **Considerations** include load balancer redundancy (preventing single point-of-failure) and complex session management.

## Related terms

- **[Round-Robin](Round-Robin.md)** — Basic server selection algorithm, rotating order
- **[Least-Connections](Least-Connections.md)** — Connect-count-based server preference
- **[Health Check](Health-Check.md)** — Periodic server operation status confirmation
- **[Failover](Failover.md)** — Automatic server-switching on failure
- **[Cloud](Cloud-Computing.md)** — Load balancing is cloud's important feature

## Frequently asked questions

**Q: What if load balancer fails?**
A: Load balancers themselves are usually redundantly configured. Multiple load balancers ensure one failure doesn't cause issues.

**Q: Do all applications need load balancing?**
A: Small apps with single-server adequate load don't need it, but considering scalability, early adoption is recommended.

**Q: How much load balancing latency?**
A: Usually under several milliseconds. Modern load balancers are highly optimized; performance impact is negligible.
**Disadvantages:** Shared resources, potential performance variability

### Request Routing Process

**Request Reception:** Load balancer receives client request at single entry point (IP address or DNS name).

**Health Check Evaluation:** Continuously monitors backend server health through TCP pings, HTTP probes, or application-level health checks.

**Server Selection:** Applies configured algorithm (round robin, least connections, etc.) to select optimal backend server based on current state.

**Request Forwarding:** Routes request to selected server, potentially modifying headers or applying transformations.

**Response Handling:** Receives response from backend, optionally caches or modifies it, then returns to client.

**Session Management:** Maintains session persistence (sticky sessions) when required by application.

### Health Checks and Failover

Load balancers perform continuous health monitoring:

**Active Health Checks:** Proactively send test requests to backends at regular intervals (e.g., HTTP GET to /health every 5 seconds).

**Passive Health Checks:** Monitor actual traffic and mark servers unhealthy based on error rates or timeouts.

**Failure Detection:** When server fails health checks (e.g., 3 consecutive failures), it's removed from active pool.

**Automatic Recovery:** Once server passes health checks again, it's automatically reinstated into rotation.

**Graceful Degradation:** During partial failures, load balancer continues serving from healthy servers while alerting operations team.

## Types of Load Balancers

### By OSI Layer

**Layer 4 (Transport Layer) Load Balancers:** Route traffic based on TCP/UDP information (IP address, port). Fast and efficient but limited routing intelligence. Ideal for high-performance, low-latency workloads requiring simple distribution.

**Use cases:** Database connections, generic TCP services, UDP applications
**Advantages:** High throughput, low latency, protocol-agnostic
**Disadvantages:** Limited routing intelligence, cannot inspect application data

**Layer 7 (Application Layer) Load Balancers:** Route based on HTTP headers, URLs, cookies, or application-specific data. Enable sophisticated routing rules based on content.

**Use cases:** Web applications, API gateways, microservices
**Advantages:** Content-based routing, SSL termination, application awareness
**Disadvantages:** Higher latency than L4, more resource intensive

### By Deployment Model

**Global Server Load Balancer (GSLB):** Distributes traffic across geographic locations and data centers using DNS-based routing. Essential for disaster recovery and global applications.

**Use cases:** Multi-region deployments, disaster recovery, geographic optimization
**Features:** DNS-based routing, health monitoring across regions, latency-based decisions

**Hardware Load Balancers:** Physical appliances for enterprise data centers requiring deterministic performance.

**Software Load Balancers:** Flexible, cloud-native solutions running on standard infrastructure.

**Virtual Load Balancers:** Run within VMs or containers, integrate with orchestration platforms like Kubernetes.

**Elastic Load Balancers:** Cloud-native services that automatically scale with demand (AWS ELB, Azure Load Balancer, Google Cloud Load Balancing).

## Load Balancing Algorithms

### Static Algorithms

**Round Robin:** Cycles through servers sequentially, assigning each request to next server in list. Simple and effective for servers with equal capacity.

**Weighted Round Robin:** Assigns more requests to higher-capacity servers based on weights. Server with weight 3 receives 3× traffic of server with weight 1.

**IP Hash:** Hashes client IP address to consistently route same client to same server. Provides natural session persistence.

### Dynamic Algorithms

**Least Connections:** Routes to server with fewest active connections. Ideal for applications with varying request duration.

**Weighted Least Connections:** Combines least connections with server capacity weighting.

**Least Response Time:** Sends requests to server with lowest average response time and fewest connections. Optimizes for user-perceived performance.

**Resource-Based (Agent-Based):** Uses server-reported metrics (CPU, memory, disk) to dynamically route traffic. Requires agent software on backends.

**Consistent Hashing:** Maps servers and clients to hash ring, minimizing disruption when servers are added or removed. Popular in distributed caching.

**Power of Two Random Choices:** Randomly selects two servers, routes request to less-loaded one. Surprisingly effective with minimal overhead.

### Advanced Algorithms

**Waterfall by Region:** Sends traffic to primary region until capacity reached, then overflows to secondary regions.

**Spray Distribution:** Distributes traffic evenly across all available regions or zones.

**Adaptive Algorithms:** Machine learning-based approaches that learn optimal routing patterns from historical data.

## Key Benefits

### Availability and Reliability

**Zero Downtime Deployments:** Gradually shift traffic during updates without service interruption.

**Automatic Failover:** Detect and route around failed servers in seconds.

**Health Monitoring:** Continuous verification of backend availability and performance.

### Scalability and Performance

**Horizontal Scaling:** Add servers to handle increased load without application changes.

**Auto-Scaling Integration:** Coordinate with cloud auto-scaling to match capacity to demand.

**Performance Optimization:** Route requests to fastest or closest servers.

### Security

**SSL/TLS Termination:** Offload encryption/decryption to load balancer, reducing backend server load.

**DDoS Protection:** Absorb and distribute attack traffic across multiple servers.

**Web Application Firewall Integration:** Filter malicious requests before they reach backends.

**Backend Obfuscation:** Hide backend server details from external clients.

## Common Use Cases

### E-Commerce Platforms

**Challenge:** Handle traffic spikes during sales events, maintain shopping cart state.

**Solution:** Layer 7 load balancing with cookie-based session persistence. Auto-scaling backend servers based on traffic patterns.

**Benefits:** Maintain service during 10× traffic spikes, ensure cart persistence across requests.

### Streaming Services

**Challenge:** Distribute media content with minimal buffering across global audience.

**Solution:** Geographic load balancing routing users to nearest edge location. CDN integration for content caching.

**Benefits:** Reduced latency, improved streaming quality, lower bandwidth costs.

### AI Inference APIs

**Challenge:** Distribute inference requests across GPU servers for low-latency predictions.

**Solution:** Least connections algorithm with GPU availability monitoring. Connection pooling for efficient resource use.

**Benefits:** Optimal GPU utilization, consistent inference latency, automatic failover.

### Microservices Architecture

**Challenge:** Route requests across dynamically scaling service instances in Kubernetes.

**Solution:** Service mesh integration with intelligent routing, circuit breaking, and retry logic.

**Benefits:** Resilient inter-service communication, automatic service discovery, traffic shaping.

## Implementation Best Practices

**Start with Simple Algorithms:** Begin with round robin or least connections. Add complexity only when needed.

**Implement Comprehensive Health Checks:** Use application-level health endpoints that verify actual service functionality, not just TCP connectivity.

**Configure Appropriate Timeouts:** Set connection, read, and write timeouts to prevent slow backends from degrading overall service.

**Enable Access Logging:** Log all requests for troubleshooting, security analysis, and capacity planning.

**Monitor Key Metrics:** Track request rate, error rate, response time, and backend health status continuously.

**Plan for Failure:** Test failover scenarios regularly. Ensure system operates acceptably with reduced capacity.

**Implement Rate Limiting:** Protect backends from overload with request rate limiting at load balancer.

**Use Connection Pooling:** Maintain persistent connections to backends to reduce connection overhead.

**Enable Compression:** Compress responses at load balancer to reduce bandwidth and improve client performance.

**Regular Capacity Planning:** Monitor trends and plan infrastructure scaling before hitting limits.

## Platform-Specific Solutions

### AWS Elastic Load Balancing

**Application Load Balancer (ALB):** Layer 7 load balancing for HTTP/HTTPS with advanced routing capabilities.

**Network Load Balancer (NLB):** Layer 4 load balancing for ultra-high performance and static IP addresses.

**Gateway Load Balancer:** Layer 3 load balancing for third-party virtual appliances.

### Google Cloud Load Balancing

**Global Load Balancing:** Single anycast IP serving traffic globally with automatic failover.

**Regional Load Balancing:** Lower-latency option for single-region deployments.

**Internal Load Balancing:** Private load balancing for internal service communication.

### Azure Load Balancer

**Azure Load Balancer:** Layer 4 load balancing with high availability.

**Azure Application Gateway:** Layer 7 load balancing with WAF integration.

**Azure Front Door:** Global HTTP load balancing with CDN capabilities.

### Open Source Solutions

**NGINX Plus:** Commercial version with advanced features, support, and monitoring.

**HAProxy:** High-performance Layer 4/7 load balancer with extensive configuration options.

**Traefik:** Cloud-native load balancer with automatic service discovery for containers.

## Performance Considerations

**Throughput:** Hardware load balancers handle 10-100 Gbps. Software load balancers typically handle 1-10 Gbps per instance.

**Latency:** Layer 4 adds <1 ms latency. Layer 7 adds 1-5 ms depending on processing complexity.

**Connection Limits:** Hardware appliances support 10M+ concurrent connections. Software solutions typically support 100K-1M per instance.

**SSL/TLS Performance:** Dedicated hardware accelerators process 10-100K TLS handshakes per second. Software solutions achieve 1-10K per second.

## Monitoring and Troubleshooting

**Key Metrics to Monitor:**
- Request rate (requests/second)
- Error rate (4xx, 5xx responses)
- Response time percentiles (P50, P95, P99)
- Backend health status
- Connection counts (active, idle)
- SSL/TLS handshake rate

**Common Issues:**
- Uneven traffic distribution
- Session persistence breaking
- Health check misconfigurations
- SSL certificate expiration
- Backend server overload

## References

- [IBM: What Is Load Balancing?](https://www.ibm.com/think/topics/load-balancing)
- [AWS: What is Load Balancing?](https://aws.amazon.com/what-is/load-balancing/)
- [AWS Elastic Load Balancing](https://aws.amazon.com/elasticloadbalancing/)
- [Kemp: What Is Load Balancing](https://kemptechnologies.com/what-is-load-balancing)
- [F5: What Is a Load Balancer?](https://www.f5.com/glossary/load-balancer)
- [F5 BIG-IP](https://www.f5.com/products/big-ip-services.html)
- [Google Cloud Load Balancing](https://cloud.google.com/load-balancing)
- [Google Cloud Load Balancing Overview](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)
- [Google Cloud Health Check Concepts](https://cloud.google.com/load-balancing/docs/health-check-concepts)
- [Google Cloud Service Mesh: Advanced Load Balancing](https://docs.cloud.google.com/service-mesh/docs/service-routing/advanced-load-balancing-overview)
- [Loadbalancer.org: Layer 4 vs Layer 7](https://www.loadbalancer.org/blog/comparing-layer-4-layer-7-and-gslb-load-balancing-techniques/)
- [Kemp: Round Robin Load Balancing](https://kemptechnologies.com/load-balancer/round-robin-load-balancing)
- [Kemp: Weighted Round Robin](https://kemptechnologies.com/load-balancer/weighted-round-robin-load-balancing)
- [Kemp: Least Connections](https://kemptechnologies.com/load-balancer/least-connections-load-balancing)
- [Kemp: Load Balancing Algorithms](https://kemptechnologies.com/load-balancer/load-balancing-algorithms-techniques)
- [NGINX: Load Balancing](https://docs.nginx.com/nginx/admin-guide/load-balancer/http-load-balancer/)
- [HAProxy Official Site](https://www.haproxy.org/)
- [Kubernetes Service Load Balancing](https://kubernetes.io/docs/concepts/services-networking/service/)
