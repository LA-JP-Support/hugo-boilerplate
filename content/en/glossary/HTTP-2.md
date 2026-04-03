---
title: HTTP/2
date: 2025-03-01
lastmod: 2026-04-02
description: A newer, faster, and more efficient web communication protocol than traditional HTTP.
translationKey: http-2
category: Web Development & Design
type: glossary
draft: false
url: /en/glossary/HTTP-2/
keywords:
  - HTTP/2
  - Web Performance
  - Communication Protocol
  - Multiplexing
  - Server Push
---

## What is HTTP/2?

**HTTP/2 is a new protocol (communication standard) that speeds communication between web servers and clients (browsers), succeeding the traditional HTTP/1.1.** Through "multiplexing" that processes multiple requests simultaneously and efficiently, "header compression" that compresses and transmits data, and "server push" where servers proactively send data, it dramatically shortens page load times. Since standardization in 2015, adoption across global websites has advanced.

> **In a nutshell:** HTTP/2 is like traffic rules for roads evolving to enable "simultaneous multi-lane traffic." Previously only one vehicle could travel at a time; now multiple can simultaneously.

**Key points:**

- **What it does:** New web communication protocol enabling simultaneous processing of multiple file requests and data compression for fast overall loading
- **Why it's needed:** Efficiently retrieve multiple files (images, scripts, stylesheets), reducing user wait time
- **Who uses it:** Web developers, server administrators, all web users

## Why it matters

In HTTP/1.1, clients cannot start requesting a second file until receiving the first. For example, if a webpage needs 10 images, HTTP/1.1 processes "request image 1 → receive → request image 2 → receive..." sequentially, taking time. Particularly in slow connections (mobile networks), this delay is pronounced, degrading user experience.

HTTP/2's multiplexing enables "request all 10 images simultaneously → receive all," efficient processing. This can shorten total communication time by seconds, especially for image-heavy sites. For mobile users, experience significantly improves. For high-traffic sites like Google and Amazon, a one-second improvement reduces user abandonment by several percent, making HTTP/2 migration a critical business initiative.

## How it works

HTTP/2 brings three major improvements. First, "binary format"—while HTTP/1.1 used text, HTTP/2 sends data as binary (0s and 1s). This makes data parsing faster for computers. Next, "multiplexing" allows a single TCP connection to simultaneously handle multiple streams (request/response flows). HTTP/1.1 needed multiple connections for multiple files; HTTP/2 needs just one.

Third, "header compression." HTTP communication includes similar header information (browser type, language settings) with each request. HTTP/1.1 sent the entire header each time; HTTP/2's HPACK compression removes duplicate data, reducing transmission volume. Additionally, "server push" lets servers proactively send "you'll probably need style.css, so I'm sending it in advance" before clients request it.

Consider a webpage composed of "HTML, CSS, JavaScript, and 3 images." HTTP/1.1 requires at least 5 sequential communications, with delay accumulating. HTTP/2 can request all 5 simultaneously through one connection, requiring only the slowest file's transfer time. This significantly shortens overall loading time.

## Real-world use cases

**News and media sites**

Media sites like BuzzFeed and CNN load article bodies plus dozens of images, ad scripts, analytics tools, social widgets, etc. HTTP/2 efficiently simultaneously retrieves these resources, shortening article-reading wait time by seconds.

**Mobile app acceleration**

Mobile networks have greater latency and limited bandwidth than wired networks. HTTP/2's multiplexing and compression enable efficient data retrieval over unreliable connections, reducing user stress.

**Efficient IoT device-server communication**

For scenarios where numerous IoT devices (smart homes, smartwatches, industrial sensors) regularly communicate with servers, HTTP/2 efficiency reduces communication volume and battery drain.

## Benefits and considerations

HTTP/2's greatest benefit is "obvious speed improvement." Field measurements report 10-30% load time reduction, especially pronounced for image-heavy sites. Multiplexing eliminates the need for multiple connections, reducing network load. Compression and binary format reduce transfer volume, cutting mobile battery drain.

However, HTTP/2 defaults to HTTPS encryption, making server setup more complex than HTTP/1.1. Legacy browsers (old IE) without HTTP/2 support won't work. Additionally, leveraging HTTP/2 requires reconsidering site construction "file bundling strategy." HTTP/1.1 benefited from bundling multiple files into one to reduce requests; HTTP/2 sometimes benefits from finer-grained file division. Development teams need learning.

## Related terms

- **[HTTP/3](HTTP-3.md)** — HTTP/2's successor. Aims for further speedup via QUIC protocol
- **[HTTPS](HTTPS.md)** — Encrypted HTTP; HTTPS is essential for full HTTP/2 benefits
- **[Web Performance](Web-Performance.md)** — General webpage speed measurement/improvement; HTTP/2 is one key initiative
- **[CDN](CDN.md)** — Global content delivery via distributed servers; combined with HTTP/2 for further effect
- **[Caching Strategy](Caching-Strategy.md)** — Efficiently using browser/server caches; important alongside HTTP/2 for speed improvement

## Frequently asked questions

**Q: How do I check if my website supports HTTP/2?**

A: Check Chrome DevTools' Network tab. The "Protocol" column shows "h2" for HTTP/2 or "http/1.1" for HTTP/1.1. Online HTTP/2 checkers also work.

**Q: How do I upgrade to HTTP/2?**

A: Most modern web servers (Nginx, Apache) and cloud hosting (AWS, Google Cloud) support HTTP/2. Contact your provider or enable HTTP/2 in server settings. HTTPS is prerequisite, requiring an SSL certificate.

**Q: Is file bundling truly bad with HTTP/2?**

A: HTTP/1.1 benefited from bundling to reduce requests. HTTP/2 enables simultaneous retrieval, so finer-grained bundling is effective. Don't split everything; adjust bundle size for your project.
