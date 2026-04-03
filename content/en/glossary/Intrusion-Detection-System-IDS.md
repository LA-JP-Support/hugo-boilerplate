---
title: Intrusion Detection System (IDS)
date: 2025-03-01
lastmod: 2026-04-02
translationKey: intrusion-detection-system-ids
description: A security tool that detects unauthorized access attempts to networks and systems, sends alerts to administrators, and minimizes damage through early detection.
keywords:
  - IDS
  - intrusion detection
  - network monitoring
  - security threats
  - real-time detection
category: Security & Compliance
type: glossary
draft: false
url: /en/glossary/intrusion-detection-system-ids/
---

## What is an Intrusion Detection System (IDS)?

**An IDS is a security tool that detects unauthorized access attempts to networks and systems and alerts administrators.** In other words, it's a "security watchman" that monitors attacks that bypass firewalls and unauthorized access from within. Unlike firewalls, IDS doesn't block attacks; instead, it specializes in "detecting anomalous activity and reporting it." Because of this, IDS functions as a "second line of defense," an essential element of a multi-layered defense strategy.

> **In a nutshell:** It's like a bank's security camera. It doesn't prevent intrusions, but detects "someone is trying to break in" and reports it to security.

**Key points:**

- **What it does:** Analyzes network traffic patterns for anomalies and monitors for possible attacks
- **Why it's needed:** Can detect threats from inside and sophisticated attacks that firewalls alone cannot prevent
- **Who uses it:** IT operations teams, Security Operations Centers (SOC), large enterprise network administrators

## Why it matters

Modern cyberattacks use sophisticated techniques to bypass firewalls. For example, embedding malicious payloads in legitimate-looking HTTP requests or infiltrating systems in multiple stages—attacks that traditional firewall inspection cannot detect are increasing. Additionally, internal threats (information theft by departing employees or dishonest staff) exist, and firewalls alone cannot address them.

By using IDS to detect attacks at their initial stage, organizations can minimize damage. Research shows that companies with shorter breach-to-detection times suffer less financial loss. IDS is the most critical tool for achieving "early detection."

## How it works

There are two main types of IDS. The first is "signature-based detection," which matches network traffic against a database of known attack patterns (signatures). For example, it pre-learns "SQL injection attack signatures" and checks communication logs for matching patterns. This method has high accuracy for known attacks but cannot handle new, unknown ones.

The second is "anomaly-based detection," which uses machine learning to learn what "normal network traffic" looks like and identifies deviations as anomalies. For example, it learns that traffic is typically 100 gigabytes per second during business hours and 5 gigabytes per second at night, then flags a sudden 100 gigabyte per second spike at night as anomalous. This approach adapts better to unknown attacks but tends to increase false positives (legitimate large transfers being mistaken for attacks).

IDS deployment location is also important. "Network-based IDS (NIDS)" is placed at the core of the network and monitors all company traffic. "Host-based IDS (HIDS)" is installed on individual servers or computers and monitors only that host. NIDS provides broad monitoring but cannot inspect encrypted traffic content. HIDS enables fine-grained monitoring but requires more deployment and operational effort. Most enterprises combine both approaches.

## Real-world use cases

**Large bank SOC detects malware infection**
IDS detects unusual database access patterns different from baseline. The SOC team immediately isolates the affected server from the network. Subsequent forensic analysis reveals an insider attempting data theft. The perpetrator is dismissed.

**Game company detects initial stages of DDoS attack**
IDS detects abnormal rise in network traffic. DDoS mitigation service is immediately activated. The attack is completely blocked, preventing service downtime. Had detection been delayed by 5 minutes, servers would have crashed under overload.

**Hospital detects unauthorized medical record access**
IDS detects massive access to medical records database outside business hours. It's found that a physician's account accessed patient records without authorization. Internal audit begins, and the physician receives a reprimand.

## Benefits and considerations

IDS's greatest benefit is "real-time threat detection." Administrators are alerted immediately after an attack occurs, enabling rapid response. With signature-based detection, accuracy against known attacks is high. Additionally, IDS detection logs serve as powerful evidence in post-breach legal proceedings (litigation, regulatory reporting).

A key consideration is "balancing false positives and false negatives." Strict detection rules increase the likelihood of legitimate traffic being mistaken for attacks. Conversely, relaxed rules risk missing actual attacks. This "tuning" is extremely difficult, and IDS operations require advanced technical expertise.

Also, since IDS "detects but does not block," attacks can continue until administrators respond. Systems that automatically block attack traffic triggered by IDS detection exist (IPS: Intrusion Prevention System), but IPS risks blocking legitimate traffic due to false positives, requiring careful consideration before deployment.

## Related terms

- **[Firewall](Firewall.md)** — Unlike IDS, actively blocks attack traffic as a network defense device
- **[Web Application Firewall (WAF)](Web-Application-Firewall-WAF.md)** — Detects and blocks threats at the application layer
- **[Intrusion Prevention System (IPS)](Intrusion-Prevention-System.md)** — Evolution of IDS that automatically blocks detected attacks
- **[Security Monitoring](Security-Monitoring.md)** — Continuous process of monitoring IDS logs and responding
- **[Incident Response](Incident-Response.md)** — Initial response procedures after IDS detection

## Frequently asked questions

**Q: What's the difference between IDS and IPS?**
A: IDS "detects and reports," while IPS "detects and automatically blocks." IPS provides stronger defense but risks blocking legitimate users due to false positives. The typical approach is to verify detection accuracy with IDS before switching to IPS.

**Q: IDS generates hundreds of detection logs daily. Should I respond to all of them?**
A: No. This indicates the rules are "too strict" or "low precision." Security analysts categorize detection logs and prioritize those with high actual attack likelihood. Typically, 10-50 alerts per day is the target to avoid "alert fatigue."

**Q: Can IDS inspect encrypted HTTPS traffic?**
A: IDS cannot inspect encrypted payloads (contents). However, it can detect unusual patterns in pre-encryption metadata (source/destination IPs, port numbers, packet length). Alternatively, [SSL/TLS interception](SSL-Inspection.md) within the enterprise allows IDS inspection after decryption, but privacy concerns require careful consideration before implementation.
