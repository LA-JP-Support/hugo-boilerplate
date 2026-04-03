---
title: RTP (Real-time Transport Protocol)
date: 2025-12-19
lastmod: 2026-04-02
translationKey: rtp-real-time-transport-protocol
description: RTP is the standard protocol for delivering audio and video over the internet in real-time. It's the foundation for VoIP and video conferencing where latency is critical.
keywords:
- RTP protocol
- Real-time transport
- Multimedia streaming
- VoIP communication
- Video conferencing
category: Voice & Communication
type: glossary
draft: false
url: /en/glossary/RTP--Real-time-Transport-Protocol-/
---

## What is RTP?

**RTP (Real-time Transport Protocol) is the standard protocol for delivering audio and video over the internet in real-time.** While traditional file transfer protocols (FTP) prioritize "reliably delivering all data," RTP prioritizes "minimizing latency and delivering data timely." Essential for VoIP calls, video conferences, live streaming, and online game voice chat—applications where audio and video involve human conversation or interaction. As the foundation of global communication infrastructure, billions daily depend on it.

> **In a nutshell:** Website downloads prioritize completeness, but call audio and video must arrive "without delay." RTP enables this. Live broadcasts matter more than edited video similarly.

**Key points:**

- **What it does:** Delivers audio and video through networks with low-latency real-time delivery
- **Why it's needed:** Excessive latency breaks human conversation, severely degrading user experience
- **Who uses it:** VoIP systems, video conference platforms, live streaming, online game developers
- **Target latency:** Audio 150-400ms, video under 1000ms ideally

## Why it matters

Call delays over 500 milliseconds break conversation flow. Video conference lip-sync misalignment causes strong discomfort. RTP addresses "real-time" requirements, providing mechanisms compensating for network variability (packet loss, latency, jitter).

RTP also is established as an international standard, enabling systems from different vendors to communicate. This realizes VoIP calling across various devices and applications, promoting market-wide innovation. Today, Zoom and Microsoft Teams can interoperate across enterprises and individuals thanks to RTP.

Furthermore, with mobile network evolution, RTP realizes high-quality communication in 5G and local 5G environments, letting more people enjoy good communication experiences.

## How it works

RTP operates on UDP (User Datagram Protocol), an internet foundation protocol. UDP is fast but unreliable; RTP provides complementary mechanisms. RTP leverages existing internet infrastructure while ensuring reliable, low-latency communication.

Audio and video are first divided into small "packets." Each packet receives header information including "timestamps" for synchronization, "sequence numbers" confirming order, "SSRC (Synchronization Source Identifier)" showing stream belonging, etc. This information enables receivers to correctly synchronize multiple streams and reconstruct packet order.

Receivers place packets in "jitter buffers," temporary storage absorbing slight delays before playback. By absorbing network latency variation (jitter), stable playback quality is achieved. When packets are lost, redundancy information from surrounding packets reconstructs missing packets. These mechanisms compensate for network imperfection while maintaining real-time guarantees.

Additionally, RTP combines with "RTCP (RTP Control Protocol)," an auxiliary protocol. RTCP monitors network quality in real-time and implements dynamic adaptation where senders automatically adjust data rates when communication quality drops.

## Real-world use cases

**VoIP telephone services**

Enterprise VoIP system deployment centers on RTP for call audio. It realizes traditional phone line quality through internet at low cost.

**Video conferencing**

Zoom and Microsoft Teams internally use RTP for audio and video delivery. Complex multi-participant synchronization is realized through RTP.

**Live streaming**

Broadcasting stations and content creators delivering live events use RTP and RTCP for low-latency, high-quality streaming.

## Benefits and considerations

RTP's greatest benefits are "low latency" and "high interoperability." As standard protocol, equipment from different companies communicates. Combined with priority control (QoS), even network congestion allows prioritized audio/video delivery. Efficient bandwidth use and packet loss resilience are key advantages.

Considerations include implementation complexity and network environment dependency. Poor network quality degrades RTP audio/video despite its mechanisms. NAT firewall passage requires additional technology (STUN, TURN). Security-wise, standard RTP lacks encryption; confidential communication requires SRTP deployment.

## Related terms

- **RTCP** — RTP's auxiliary protocol monitoring and controlling call quality
- **VoIP** — Voice communication technology using RTP
- **SIP** — Protocol managing VoIP call start/end while RTP handles voice/video transmission
- **WebRTC** — Real-time browser communication using RTP internally
- **QoS** — Technology prioritizing RTP traffic

## Frequently asked questions

**Q: Is RTP security-deficient?**
A: Standard RTP lacks encryption, but SRTP extension adds encryption and authentication. Confidential calls require SRTP.

**Q: What's the difference between RTP and video streaming (YouTube)?**
A: YouTube tolerates seconds to tens-of-seconds delay, implementing thorough quality control. RTP minimizes delay tolerating slight quality reduction. Usage determines selection.
