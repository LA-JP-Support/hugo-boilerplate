---
title: CloudFront
date: 2026-01-29
lastmod: 2026-04-02
translationKey: cloudfront
description: Amazon CloudFront is AWS's global content delivery network (CDN). It delivers content with low latency from over 400 edge locations worldwide while integrating security features.
keywords:
- CloudFront
- CDN
- content delivery
- AWS
- edge locations
category: Cloud & Infrastructure
type: glossary
draft: false
url: /en/glossary/cloudfront/
---

## What is CloudFront?

**Amazon CloudFront is a global content delivery network (CDN) provided by AWS.** It leverages over 400 edge locations (data centers) worldwide to deliver websites, APIs, and video content with high speed to end users from locations closest to them. Positioned between the origin (source server) and users, it caches content to dramatically reduce response times. It handles everything from static assets (images, CSS) to dynamic API responses, with automatic scaling for traffic spikes.

> **In a nutshell:** "It's like placing inventory from headquarters in local branch offices geographically close to customers for ultra-fast delivery"—applied to web content.

**Key points:**

- **What it does:** Uses global edge locations to deliver web content with low latency through a CDN service
- **Why it's needed:** Slower page loading increases user bounce and exit rates; CloudFront improves speed to enhance search rankings and conversion rates
- **Who uses it:** Globally distributed websites, e-commerce platforms, media streaming companies, SaaS businesses

## Importance and Use Background

User satisfaction depends heavily on page load speed. When Japanese users load content from US servers, physical distance and network latency create delays of several seconds. CloudFront eliminates this delay, delivering from a Japan-based edge instantly. This improves SEO rankings, increases user satisfaction, and boosts conversion rates. For global companies and media sites especially, CloudFront is essential business infrastructure.

## Key Features

**Global edge network** with over 400 locations across six continents automatically selects the nearest server. **Multiple origin support** lets you combine S3 buckets, EC2 instances, and custom servers. **Real-time cache control** through TTL settings and cache invalidation manages content freshness. **Lambda@Edge** enables function execution at edges for A/B testing and personalization.

## Delivery Mechanism

User requests are automatically routed to the nearest edge location via Anycast routing. The edge first checks its local cache—if content exists and is still valid, it delivers immediately (cache hit). Otherwise, it fetches from the origin, stores in cache, and delivers to the user. This dramatically reduces origin server requests, lowering server load and costs.

## Concrete Use Cases

**E-commerce product pages** deliver high-resolution product images from edges, enabling fast worldwide display and boosting cart clicks by 30% in some cases. **Video streaming** delivers live events and on-demand video without buffering, allowing students to view educational content with consistent quality globally. **API acceleration** caches mobile app backend API responses, improving response speed by 50% or more.

## Benefits and Optimization Points

**Performance improvement** is the biggest benefit, directly improving SEO rankings and search traffic. **Bandwidth cost reduction** comes from reduced origin server requests. **Scalability** automatically handles traffic spikes without intervention. Optimization requires smart cache strategies, compression configuration, and origin selection.

## Related Terms

- **[CDN (Content Delivery Network)](CDN.md)** — General technology for geographically distributed content delivery, including CloudFront
- **[Caching](Caching.md)** — CloudFront's core feature that stores frequently accessed content temporarily for faster delivery
- **[Latency](Latency.md)** — Network delay that CloudFront significantly reduces
- **[AWS Lambda@Edge](Lambda-Edge.md)** — Advanced feature enabling function execution at CloudFront edges
- **[DDoS Protection](DDoS-Protection.md)** — Integrated security feature protecting against large-scale attacks

## Frequently Asked Questions

**Q: How does CloudFront differ from Cloudflare?**
A: CloudFront is AWS-specific; Cloudflare is independent of AWS with more comprehensive security features. If you already use AWS, CloudFront integrates more easily. For independent CDN needs, Cloudflare is an alternative.

**Q: Can I deliver only static content?**
A: No. CloudFront delivers dynamic content too, though cache efficiency varies by content type, making cache policy optimization important.

**Q: What's the cost structure?**
A: Pay-per-region data transfer costs based on volume. Reduced origin load usually results in overall cost savings.

## Reference Materials

- [AWS CloudFront Official Documentation](https://aws.amazon.com/cloudfront/)
- [CloudFront Best Practices](https://docs.aws.amazon.com/cloudfront/)
- [CDN Performance Optimization Guide](https://aws.amazon.com/jp/)
- [AWS re:Invent CloudFront Sessions](https://reinvent.awsevents.com/)
- [CloudFront Pricing Page](https://aws.amazon.com/cloudfront/pricing/)
