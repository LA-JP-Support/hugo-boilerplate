---
title: Average Speed of Answer (ASA)
date: 2025-12-19
lastmod: 2026-04-02
translationKey: Average-Speed-of-Answer--ASA-
description: Average Speed of Answer (ASA) is the average waiting time from when a customer calls a contact center through queuing until an operator answers. A fundamental KPI measuring contact center responsiveness.
keywords:
- average speed of answer
- ASA
- call center
- wait time
- responsiveness
category: Data & Analytics
type: glossary
draft: false
url: /en/glossary/average-speed-of-answer--asa-/
---

## What is Average Speed of Answer (ASA)?

**Average Speed of Answer (ASA) is the average wait time from when a customer calls a contact center until an operator answers.** Measured in seconds, it's one of the most intuitive and important KPIs measuring contact center responsiveness. Shorter ASA correlates with higher customer satisfaction and lower abandonment rates, directly impacting customer service management decisions.

> **In a nutshell:** "Time for a restaurant staff member to answer the phone before customers hear 'Please hold while we assist another customer.'" Long waits frustrate customers into hanging up.

**Key points:**

- **What it does:** System records call receipt time and operator pickup time, calculating the difference as average
- **Why it matters:** Directly impacts customer experience and abandonment rate, determining staffing efficiency and satisfaction balance
- **Who uses it:** Telecoms, banks, insurance, customer support, healthcare—all sectors with phone interactions

## Calculation method

ASA calculation is simple:

```
ASA = (Total wait time for answered calls) ÷ (Number of answered calls)
```

For example, if 100 calls were answered during a shift with 1,000 seconds total wait time, ASA = 1,000 ÷ 100 = 10 seconds.

### Benchmarks

| Industry/Type | Excellent | Good | Standard | Needs Improvement |
|---|---|---|---|---|
| Financial institutions | Under 10 sec | 10–20 sec | 20–30 sec | Over 30 sec |
| Healthcare | Under 5 sec | 5–10 sec | 10–20 sec | Over 20 sec |
| E-commerce | Under 15 sec | 15–25 sec | 25–35 sec | Over 35 sec |
| Telecom | Under 10 sec | 10–20 sec | 20–40 sec | Over 40 sec |
| Insurance | Under 15 sec | 15–30 sec | 30–45 sec | Over 45 sec |

Industry benchmarks with your customer base and interaction content adjustments are important for realistic targets.

## How it works

ASA measurement proceeds as follows. When customers call the contact center, the PBX (automatic exchange) or ACD system recognizes the call and records a timestamp. The system then, based on customer selection (menu navigation) or skill-based routing configuration, places the customer in the optimal operator queue. During wait, the system plays messages like "you are fifth in line" to discourage abandonment.

When an operator finishes current calls and becomes available, the system routes the call to a qualified operator's workstation, recording operator pickup time. The difference between call receipt and pickup times is that call's "answer time." These times are aggregated to calculate ASA average.

Importantly, **abandoned calls (customers hanging up before operator connection) are not included in ASA calculation.** High abandonment requires separate tracking.

## Main benefits

**Direct customer satisfaction impact** is the biggest benefit. Research shows longer wait times increase customer dissatisfaction, lowering Net Promoter Score (NPS). Conversely, short ASA creates positive first impressions, improving subsequent interaction quality perception. **Workforce optimization** is enabled. ASA data enables calculating necessary staff, balancing over-staffing (cost waste) and under-staffing (service degradation). Furthermore, **real-time management** is possible. Monitoring current ASA via dashboard, exceeding acceptable range triggers immediate actions like calling additional staff. Additionally, **call abandonment reduction** results. Shorter response wait times encourage customer patience versus hanging up.

## Real-world use cases

**Operating hours optimization**
When data reveals "daily 3 PM ASA spikes," operators concentrate during that time. Peak handling becomes possible without labor cost waste.

**Campaign period staffing planning**
Large sales and campaigns expect multiples of normal call volume. Calculating required additional staff for target ASA enables hiring and dispatch decisions.

**Omnichannel quality monitoring**
Measuring phone, chat, email, and SNS ASA by channel identifies imbalances for correction.

## Benefits and considerations

ASA's biggest advantage is instant measurement and readily visible improvement results. However, **pursuing brevity risks quality harm.** Over-emphasizing ASA pressures operators to rush customer handling, leaving complex problems unresolved, increasing callbacks and ultimately degrading overall efficiency. Additionally, **peak handling challenges** exist. Sudden traffic surges (news events, emergencies) create scaling bottlenecks, dramatically worsening ASA. Furthermore, **skill set requirement conflicts** are challenging. Routing to specific-skilled operators improves satisfaction but lengthens ASA.

## Related terms

- **[Average Handle Time (AHT)](Average-Handle-Time.md)** — Post-response processing time for total efficiency measurement. Combined with ASA, it reveals overall efficiency
- **[Call Abandonment Rate](Call-Abandon-Rate.md)** — Long ASA typically increases this. Customer hang-up percentage when impatient waiting
- **[Workforce Management](Workforce-Management.md)** — Using ASA data to plan optimal shifts and staffing
- **[Automatic Call Distribution (ACD)](Automatic-Call-Distribution.md)** — Routing technology impacting ASA
- **[Interactive Voice Response (IVR)](IVR.md)** — Technology auto-handling simple inquiries, reducing operator queue load

## Frequently asked questions

**Q: What's the ASA and customer satisfaction relationship?**
A: Generally, ASA under 10 seconds indicates high satisfaction, while exceeding 30 seconds shows increased dissatisfaction. However, industries and customer expectations vary. Analyzing your NPS and ASA correlation to set optimal targets is important.

**Q: How do I improve ASA?**
A: (1) Staff increases, (2) IVR auto-handling simple inquiries, (3) skill set review, (4) shift optimization are options. Analyzing the primary constraint and addressing high-impact measures first is essential.

**Q: Does remote work change ASA?**
A: Basic measurement methods remain the same, but internet connection quality, VPN delays, and other factors unlike office environments affect ASA. Remote-specific target adjustments may be necessary.
