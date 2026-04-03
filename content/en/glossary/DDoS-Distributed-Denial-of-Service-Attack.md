---
title: DDoS (Distributed Denial of Service) Attack
date: 2025-12-19
lastmod: 2026-04-02
translationKey: DDoS-Distributed-Denial-of-Service-Attack
description: Attack flooding servers with massive simultaneous requests from multiple computers, rendering services unavailable and causing business disruption and reputation damage.
keywords:
- DDoS attack
- distributed denial of service
- botnet
- bandwidth exhaustion
- availability
category: Security & Compliance
type: glossary
draft: false
url: /en/glossary/ddos-distributed-denial-of-service-attack/
---

## What is a DDoS Attack?

**A DDoS (Distributed Denial of Service) attack simultaneously sends massive request volumes from multiple computers worldwide to a server, overwhelming the system and rendering services unavailable.** Unlike simple DoS attacks from single sources, "distributed" means coordinated attacks from numerous sources, making defense far more difficult. Attackers typically exploit botnets—networks of malware-infected computers—commandeering their resources without owner knowledge.

> **In a nutshell:** Like thousands of people simultaneously rushing ticket windows at a cinema, exceeding capacity and preventing legitimate customers from purchasing.

**Key points:**
- **What it does:** Send massive traffic from multiple sources simultaneously overwhelming servers.
- **Why attackers use it:** (From attacker perspective) Disrupt competitor/rival services and damage business operations.
- **Who's affected:** Online service providers, financial institutions, gaming companies, news sites.

## Why It Matters

DDoS attacks are "simple but powerful" threats. Attack technical difficulty is low (renting botnets enables amateurs to execute); defense is extremely hard. All enterprise sizes experience attacks. Security research shows DDoS incident frequency increased 50%+ year-over-year in 2023, particularly targeting financial, retail, and SaaS companies.

Business impact is severe. Multi-hour website downtime halts online sales, damages brand trust, and diverts customers to competitors. One major ecommerce site lost billions in sales from 4-hour DDoS attacks. Building DDoS defense is critical business continuity planning.

## How It Works

DDoS attacks take three primary forms: **Volumetric attacks** flood server bandwidth with massive data volumes. **Protocol attacks** exceed network equipment processing limits with malformed request formats. **Application layer attacks** send high-volume requests appearing normal, evading WAF detection.

Botnet structure: Attackers infect tens of thousands to millions of computers with malware; each infected computer ("bot") receives attack commands from attacker control servers. During execution, all bots simultaneously send requests to target servers. The target becomes resource-exhausted; legitimate user requests go unprocessed and timeout.

Specifically, volumetric attacks often use "UDP Flood"—normally lightweight UDP protocol doesn't require responses, but attackers spoof response addresses and send massive UDP packets. Network infrastructure becomes overloaded attempting processing.

## Real-world Examples

**Political activism attacks** - Government websites experience DDoS from activist groups supporting political opposition, disabling citizen services (voting information provision). Post-recovery, security companies deploy DDoS mitigation services.

**Intense competitive rivalry** - During ecommerce major sales periods, competitors launch DDoS attacks against rival sites; victim sales drop 90%. Attackers face criminal prosecution afterward.

**Extortion through ransomware groups** - Security firms notify targets: "Pay us to stop DDoS attacks"; multiple companies submit to payment demands.

## Benefits and Considerations

**(Attacker perspective) DDoS advantages:** Direct, visible results; target goes down within minutes after attack execution; hard to trace attack origins through botnet routing.

**(Defense perspective) DDoS cautions:** Complete defense is impossible. Distinguishing legitimate from attack traffic is difficult; strict defense rules risk blocking legitimate users. Large-scale DDoS defense (Tbps-level) requires specialized service provider engagement with continuous costs. Attack methods constantly evolve; last-year's effective defenses may fail today.

## Related Terms

- **[Botnet](Botnet.md)** — Malware-infected computer networks used for DDoS attacks.
- **[Web Application Firewall (WAF)](Web-Application-Firewall-WAF.md)** — Security tool detecting/blocking application-layer DDoS attacks.
- **[Security Auditing](Security-Auditing.md)** — Evaluates security posture including DDoS resilience.
- **[Incident Response](Incident-Response.md)** — Initial procedures when DDoS attacks occur.
- **[Bandwidth Management](Bandwidth-Management.md)** — Network configuration protecting circuits from DDoS.

## Frequently Asked Questions

**Q: What are the legal consequences of launching DDoS attacks?**
A: Nearly universally illegal. Japan's Computer Fraud Prevention Law results in arrest and prosecution. Sentences may include imprisonment without probation and substantial fines. International attacks face prosecution under target country laws regardless of attacker location.

**Q: Can companies completely prevent DDoS attacks?**
A: No—complete prevention is impossible. Combining DDoS mitigation provider services, layered defense, cloud-based DDoS solutions, and multiple tactics can minimize damage. Business continuity planning focusing on "rapid recovery when attacked" is realistic.

**Q: How do we detect if our company is infected (botnet participant)?**
A: Typically undetectable; malware operates silently. Regular network monitoring for abnormal outbound traffic (sending direction) anomalies can reveal infection. Monitor upstream providers for suspicious traffic patterns.

## Mitigation Strategies

- Deploy DDoS mitigation services from specialized security providers.
- Implement multi-layer defense across network, application, and infrastructure levels.
- Use cloud-based DDoS protection services.
- Develop and test business continuity plans for outage scenarios.
- Monitor network traffic continuously for anomalies.
- Establish incident response procedures for rapid attack response.
