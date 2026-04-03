---
title: WebRTC
date: 2025-12-19
lastmod: 2026-04-02
description: WebRTC is a peer-to-peer communication protocol enabling real-time audio, video, and data exchange between web browsers and mobile apps. Powers video conferencing and telemedicine.
translationKey: webrtc
category: Voice & Communication
type: glossary
draft: false
url: /en/glossary/webrtc/
keywords:
  - WebRTC
  - real-time communication
  - peer-to-peer
  - video conferencing
  - browser API
---

## What is WebRTC?

**WebRTC (Web Real-Time Communication) is a peer-to-peer communication protocol enabling real-time audio, video, and data exchange on web browsers without plugins.** Co-developed by Google, Mozilla, and Opera, this technology establishes direct connections between two browsers and transmits media streams without server intermediation. Comprising three main components—MediaStream API, RTCPeerConnection, and RTCDataChannel—it's used across fields requiring real-time communication including video conferencing, online education, telemedicine, and live streaming.

> **In a nutshell:** It's like two people exchanging letters face-to-face without a post office as intermediary. No intermediary means speed, privacy, and security.

**Key points:**

- **What it does:** Exchange audio, video, and data in real-time between browsers
- **Why it matters:** Achieves low-latency, secure communication without plugins
- **Who uses it:** Video conference companies, education platforms, healthcare providers, game developers

## Why it matters

Before WebRTC, dedicated plugins like Flash required installation, creating security issues, maintenance burdens, and device compatibility challenges. WebRTC solved these problems and democratized real-time communication. Today, major video conferencing tools like Zoom, Google Meet, and Microsoft Teams use WebRTC, establishing it as the industry standard.

Technically, peer-to-peer connections reduce server load, decrease latency, and improve privacy. In telemedicine, built-in encryption is crucial for HIPAA compliance and medical privacy. In education, low latency improves online learning experiences. From a [web performance](Web-Performance.md) perspective, it also contributes to internet-wide bandwidth efficiency.

## How it works

WebRTC connection establishment progresses through eight steps. The first stage is "media capture," obtaining user permission to access camera and microphone through the getUserMedia API.

The second stage is "peer connection creation," where each participant creates an RTCPeerConnection object to prepare for managing communication sessions.

The third stage is "offer creation," where one browser generates a Session Description (SDP) containing supported codecs and network capabilities using createOffer().

The fourth stage is "signaling exchange," transmitting this offer to the other browser through a WebSocket server. This is the only step using a server.

The fifth stage is "answer generation," where the receiving end creates a compatible response using createAnswer() and sends it back.

The sixth stage is "ICE candidate gathering," where both browsers simultaneously collect network addresses (local, reflexive, relay) for NAT traversal.

The seventh stage is "connection establishment," where the ICE framework tests candidate pairs and selects the optimal communication path.

The eighth stage is "media transmission," where audio and video streams flow directly, protected by DTLS and SRTP encryption.

## Real-world use cases

**Video conferencing platforms** – Zoom, Google Meet, Microsoft Teams, Discord use WebRTC for multiparty video calls, screen sharing, and real-time collaboration.

**Telemedicine applications** – Enable secure video consultations between doctors and patients. Built-in encryption meets HIPAA compliance and protects medical privacy.

**Online education platforms** – Virtual classrooms, one-on-one tutoring, and group projects achieve low-latency real-time collaboration.

**Customer support systems** – Website visitors access video support without plugin installation. Immediate assistance available without installing separate apps.

**IoT device monitoring** – Real-time streaming and control from security cameras, smart home devices, and industrial sensors.

## Benefits and considerations

WebRTC benefits include plugin-free cross-platform support, built-in encryption for security, and low latency from reduced server load. Adaptive bitrate control automatically adjusts communication quality on low-speed networks.

Considerations include NAT traversal complexity (requiring STUN/TURN servers), handling implementation differences between browsers, and the need to build signaling servers. Additionally, multiparty communication's bandwidth consumption grows exponentially with participant numbers, creating scalability constraints. Connection establishment under firewall restrictions also presents challenges.

## Related terms

- **[Peer-to-Peer](peer-to-peer.md)** — The direct connection method WebRTC uses
- **[Encryption](encryption.md)** — The security foundation of WebRTC
- **[Video Codec](video-codec.md)** — Compression methods used in WebRTC
- **[Web Performance](Web-Performance.md)** — Low-latency communication contributes to performance
- **[API](API.md)** — WebRTC browser API interface

## Frequently asked questions

**Q: Does WebRTC work on smartphones?**
A: Yes, on both iOS and Android. However, consider battery consumption and reconnection handling during network switching.

**Q: Can I do group video calls like Zoom?**
A: Yes, but it becomes complex with 3+ participants. Typically, implement a media server (SFU - Selective Forwarding Unit) for efficient topology.

**Q: What should I do when NAT traversal is needed?**
A: Configure STUN/TURN servers. If STUN connection fails, fall back to TURN relay.
