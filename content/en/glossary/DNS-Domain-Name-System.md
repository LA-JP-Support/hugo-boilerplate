---
title: "Domain Name System"
date: 2025-03-01
lastmod: 2026-04-02
translationKey: "dns-domain-name-system"
description: "The internet's address system that converts human-readable domain names into IP addresses computers understand."
keywords:
  - Domain
  - IP Address
  - Network
  - Internet
  - Name Resolution
category: "Cloud & Infrastructure"
type: glossary
draft: false
url: /en/glossary/DNS-Domain-Name-System/
---

## What is DNS (Domain Name System)?

**DNS (Domain Name System) is a system that converts human-readable domain names (like example.com) into IP addresses that computers understand (like 192.0.2.1).** It functions as the "address book" of the internet, allowing users to enter a URL while DNS translates it to the actual server location (IP address), enabling browsers to access the desired website.

> **In a nutshell:** Just as a phone book finds a phone number from a person's name, DNS automatically finds an IP address from a domain name.

**Key points:**

- **What it does:** Automatically translates domain names into IP addresses
- **Why it's needed:** Users can use easy-to-remember domain names while computers reliably connect to the correct server
- **Who uses it:** Everyone connected to the internet uses DNS constantly, often without realizing it

## Why it matters

In the early stages of the internet, server access required specifying the IP address directly (a string of numbers like 192.0.2.1). Users had to memorize the IP address of the server they wanted to visit, which was a major obstacle to internet adoption.

The introduction of DNS dramatically solved this problem. Users can now use human-readable domain names like "google.com" and "yahoo.co.jp," while the DNS system automatically converts these to actual IP addresses in the background. Without this simplicity, the internet would not have achieved the widespread adoption we see today.

Additionally, DNS has become even more critical in the cloud computing era. When websites are distributed across multiple servers or server locations change frequently, DNS automatically directs access to the optimal server, allowing users to continue accessing using the same consistent domain name.

## How it works

DNS operates through a distributed network of servers working together. There are four main components.

When a user types "example.com" in the browser's address bar, a DNS client called a Resolver begins operating. This runs on the user's computer or the internet provider's server and sends a DNS query. Next, the Root Nameserver indicates where the TLD Nameserver holding information about the ".com" domain is located. The TLD Nameserver returns the location of the Authoritative Nameserver holding the specific IP address for "example.com." Finally, the Authoritative Nameserver returns the IP address (for example, 192.0.2.1) corresponding to "example.com."

This entire process typically completes in milliseconds. Users experience almost no waiting time accessing websites. Combined with [load balancing](Load-Balancing.md), it's also possible to distribute access across [autoscaled instances](Auto-Scaling.md) on multiple servers.

## Real-world use cases

**Optimizing global content delivery**

Major video streaming services cache content across multiple data centers worldwide. When users access, DNS returns the IP address of the closest server based on the user's geographic information. This ensures users always get a fast streaming experience.

**Zero-downtime migration during domain transfers**

When companies move servers, migrations traditionally caused hours of downtime. With DNS, simply changing the DNS settings to the new server's IP address automatically redirects users worldwide to the new server. The migration proceeds smoothly.

**Protection against DDoS attacks**

DDoS attackers target specific IP addresses. Using DNS to distribute load across multiple IP addresses when an attack is detected prevents complete site outage and creates infrastructure capable of withstanding attacks.

## Benefits and considerations

DNS's greatest benefit is that the entire internet operates stably through a simple, scalable mechanism. Various operational flexibilities are enabled by DNS—changing domain names, migrating servers, load balancing across multiple servers, and leveraging geographically distributed servers. Caching functionality also speeds up resolution of frequently accessed domains.

However, there are considerations. DNS typically uses UDP, a protocol with low response reliability, exposing it to security threats such as cache poisoning and DNS spoofing. Malicious actors can forge DNS responses and redirect users to fraudulent sites. Incorrect DNS configuration can also cause sites to become temporarily inaccessible. Additionally, privacy concerns exist regarding how DNS query history can reveal users' browsing habits.

## Related terms

- **[IP Address](IP-Address.md)** — The target that DNS translates to; a unique identifier for computers on the internet
- **[Domain](Domain.md)** — The human-readable name that DNS manages for websites
- **[Cloud Computing](Cloud-Computing.md)** — DNS is essential infrastructure when operating multiple distributed servers
- **[Security](Security.md)** — DNSSEC (DNS Security Extensions) and other DNS security enhancements are important
- **[Network](Network.md)** — DNS is a critical technology supporting the foundation of internet communication

## Frequently asked questions

**Q: What should I do if DNS response is slow?**

A: First, check which DNS server you're using. If your internet provider's DNS server is slow, switching to a public DNS server like Google DNS (8.8.8.8) or Cloudflare DNS (1.1.1.1) may improve response speed.

**Q: How long does it take for DNS record changes to take effect?**

A: Usually several minutes to several hours. The TTL (Time To Live) setting determines the propagation speed. Setting a shorter TTL allows changes to propagate faster, but increases DNS server queries.

**Q: Can I change DNS settings for my domain?**

A: Yes. You can edit various DNS records from your domain registrar's control panel, including A records (IPv4 addresses), AAAA records (IPv6 addresses), and CNAME records (aliases). However, configuration mistakes can cause site outages, so changes must be made carefully.
