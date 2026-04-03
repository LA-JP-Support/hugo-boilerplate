---
title: HTTP/3
date: 2025-03-01
lastmod: 2026-04-02
description: The latest web communication standard based on the QUIC protocol, achieving further speed improvement and stability.
translationKey: http-3
category: Web Development & Design
type: glossary
draft: false
url: /en/glossary/HTTP-3/
keywords:
  - HTTP/3
  - QUIC
  - Web Performance
  - UDP
  - Next-Generation Communication
---

## What is HTTP/3?

**HTTP/3 is the latest web communication standard based on QUIC (Quick UDP Internet Connection), developed by Google.** Until [HTTP/2](HTTP-2.md), TCP (Transmission Control Protocol)—reliable but slow—was used. HTTP/3 switches to UDP (User Datagram Protocol)—a fast method—achieving further speedup and reliability improvements. Formally standardized in 2022, major browsers (Chrome, Firefox, Safari) support it, accelerating adoption across websites.

> **In a nutshell:** HTTP/3 is like "improved delivery methods." Previously, "arranging packages in order to ensure delivery" was the method; now, "dividing into smaller shipments, sending via shortest route, then reassembling" is more efficient.

**Key points:**

- **What it does:** New web communication standard based on QUIC protocol using UDP for fast communication with reduced latency
- **Why it's needed:** Quick reconnection on network interruption, shortened webpage/app load times, improved mobile user experience
- **Who uses it:** Web developers, infrastructure engineers, product developers prioritizing user experience

## Why it matters

HTTP/2 is sufficiently fast, but fundamental challenges remain. TCP guarantees "reliable delivery," so if one packet (data unit) is lost, subsequent packet processing waits for that packet. This is "Head-of-Line (HOL) blocking." Mobile networks frequently experience interruptions and delays, making this wait time directly perceptible as user delay.

HTTP/3's UDP adoption realizes "one delayed packet doesn't block others; other packets continue"—independent communication. Additionally, TCP requires "three-way handshake"—multiple communication stages—for connection; QUIC completes initial connection in one round-trip, with nearly zero-delay reconnection. For mobile users switching from WiFi to mobile networks, HTTP/2 requires new connection establishment with hundreds-of-milliseconds delay; HTTP/3 switches instantly.

## How it works

The fundamental difference between HTTP/3 and earlier protocols lies in "layering." HTTP/2 runs on TCP (Layer 4: transport layer), constrained by TCP limitations. HTTP/3 adopts QUIC—a new protocol—building a QUIC layer over UDP, implementing "reliable delivery," "communication order assurance," "retransmission control"—previously TCP-only features—more efficiently.

QUIC's main improvements are five-fold. First, "0-RTT (Zero Round-Trip Time) resumption" enables starting data transmission immediately without handshake to previously connected servers. Second, "connection migration" allows continuing the same connection despite network changes. Mobile users switching from WiFi to LTE don't need fresh connection; communication continues smoothly. Third, "improved multiplexing" enables finer-grained parallel processing than HTTP/2.

Fourth, "Forward Error Correction (FEC)" lets some packet loss recovery through calculation. Fifth, "fast connection establishment" completes initial connection in one round-trip. These improvements realize "transparent latency reduction" in unstable environments like mobile networks, impossible with HTTP/2.

Specifically, consider a smartphone user starting article reading in a news app on WiFi, then leaving the café and switching to LTE network. HTTP/2 requires reconnection and article load interrupts. HTTP/3's "connection migration" continues loading without network interruption, invisible to users.

## Real-world use cases

**Mobile-first applications**

Smartphone users frequently switch networks (WiFi to LTE or moving). HTTP/3's connection migration minimizes rebuffering in video apps like YouTube and Instagram, providing seamless viewing.

**Real-time gaming and streaming services**

Online games and live streaming demand low latency. HTTP/3's latency reduction improves real-time interactivity, enhancing competitive gaming and live event experiences.

**Efficient IoT device communication**

IoT devices typically use low bandwidth with unstable connections. HTTP/3's efficiency and packet-loss recovery improve cloud-server communication stability and reduce device battery drain.

## Benefits and considerations

HTTP/3's greatest benefit is "major mobile user improvement." Network disconnection recovery speed improves dramatically, and data loss minimizes over unstable connections. Field measurements report 10-50% load time reduction in mobile versus HTTP/2. QUIC's built-in security encrypts connections early, improving security.

However, HTTP/3 migration is more complex than [HTTP/2](HTTP-2.md). As UDP-based, firewall configuration and NAT (Network Address Translation) issues can arise. Legacy network infrastructure filters UDP, potentially requiring HTTP/2 fallback. Server-side implementation demands more extensive configuration than HTTP/2, requiring infrastructure engineer skills. Additionally, QUIC/HTTP/3 debugging tools and monitoring haven't matured like HTTP/2.

## Related terms

- **[HTTP/2](HTTP-2.md)** — HTTP/3's immediate predecessor; HTTP/3 further improves it
- **[QUIC Protocol](QUIC-Protocol.md)** — New communication protocol underlying HTTP/3, built over UDP
- **[UDP](UDP.md)** — User Datagram Protocol; faster but less reliable than TCP
- **[Web Performance](Web-Performance.md)** — General webpage speed measurement/improvement; HTTP/3 is the cutting edge
- **[TLS 1.3](TLS-1-3.md)** — Latest encryption version; combined with HTTP/3 for fast, secure communication

## Frequently asked questions

**Q: If most visitors don't use HTTP/3 browsers, is HTTP/3 adoption unnecessary?**

A: Not entirely unnecessary, but priority might be low. Google increasingly considers HTTP/3 support in ranking factors, so preparatory work has SEO value. For high-mobile-user sites, user experience benefits warrant adoption.

**Q: Is HTTP/3 migration simple?**

A: More complex than HTTP/2 migration. Most modern web servers and CDNs support HTTP/3, but server and DNS configuration adjustment is needed. Cloud hosting users (AWS, Google Cloud, Cloudflare) typically need only enable settings.

**Q: Do we lose old browser support during HTTP/3 migration?**

A: No. Non-HTTP/3 browsers automatically fallback to HTTP/2 or HTTP/1.1. HTTP/3 is "a plus for new users," with no negative impact on existing users.
