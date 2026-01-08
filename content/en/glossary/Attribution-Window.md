---
title: "Attribution Window"
date: 2025-12-18
lastmod: 2025-12-18
translationKey: "attribution-window"
description: "An attribution window is the time period after a customer interacts with an ad during which a purchase is credited to that marketing effort."
keywords: ["attribution window", "marketing attribution", "conversion window", "campaign effectiveness", "digital advertising"]
category: "Analytics & Content Effectiveness"
type: "glossary"
draft: false
---

## What Is an Attribution Window?

An attribution window is a set period after a marketing interaction—like an ad click, impression, or view—during which conversions are credited to that touchpoint. This is a foundational concept in digital advertising and analytics, as it determines which touchpoints are "eligible" to receive credit for driving a conversion.

If a user clicks your Facebook ad and purchases six days later, and your attribution window is 7 days, that ad gets credit for the conversion. If the purchase occurs on day eight, the ad receives no credit. This timing mechanism is crucial for evaluating which marketing efforts are actually driving results.

An attribution window (also called a conversion window or lookback window) defines the period after a user interacts with a marketing channel (ad click, view, email open, etc.) in which a subsequent conversion can be attributed back to that interaction.

## Why Attribution Windows Matter

Attribution windows are critical to measuring campaign effectiveness, optimizing spend, and accurately understanding customer journeys.

**Budget Allocation**- Attribution windows shape which channels and campaigns appear most effective, influencing budget decisions

**Performance Metrics**- Metrics like ROAS (Return on Ad Spend), CPA (Cost Per Acquisition), and others are affected by attribution timing

**Strategic Decisions**- Attribution settings determine whether slow or fast-converting channels are undervalued or over-credited

Incorrect window settings lead to misattribution:
- Undervaluing slow-converting channels (if the window is too short)
- Over-crediting passive exposures (if the window is too long)

## Types of Attribution Windows

| Type | What It Tracks | Common Use Cases |
|------|----------------|------------------|
| **Click-based**| User clicks (e.g., ad, email, link) | Paid search, Facebook/Instagram Ads |
| **View-through**| User views (impression), no click | Display, video, social ads |
| **Custom windows**| User-defined, flexible per channel | Cross-platform, custom journeys |
| **Event-based**| Offline/online events | Influencer, podcast, offline media |

## Attribution Window Length

| Window Length | Ideal For | Risks |
|---------------|-----------|-------|
| 1 day | Flash sales, urgent offers | Misses delayed or researched conversions |
| 7 days | Mid-funnel, moderate consideration | Can ignore slow-burn touchpoints |
| 14 days | Products with moderate research phase | May overcredit passive exposures |
| 30 days | High-AOV, long consideration products | Over-attributes if decision cycle is shorter |
| 60–180 days | B2B, SaaS, high-ticket, complex journeys | Attribution overlap, diminishing influence |

## How Attribution Window Length Affects Reporting

The length of your attribution window can dramatically alter campaign insights:

**Short Windows**- Undercount impact from channels with long consideration cycles
- Favor last-touch, direct-response tactics

**Long Windows**- Capture more delayed conversions
- Risk over-crediting early, passive, or unrelated exposures

**Example:**A customer sees your Facebook ad on Monday, clicks your Google ad on Wednesday, and finally converts through email on Friday.
- With a 1-day window, only the email gets credit
- With a 7-day window, all touchpoints may get partial credit, depending on your attribution model

The window you choose is as important as the attribution model (first-touch, last-touch, linear, time-decay, etc.). Together, they define how credit is distributed.

## Choosing the Right Attribution Window

No universal "best" window exists. The optimal length depends on your business model, sales cycle, customer behavior, and campaign goals.

**Decision Framework: The "TIME" Method**| Factor | Questions to Ask |
|--------|------------------|
| **Time to Conversion**| What's the average lag between first touch and conversion? |
| **Intent Level**| Are users acting impulsively or after long research? |
| **Marketing Mix**| Are you using quick-response channels or nurturing over time? |
| **Evaluation Type**| What's your reporting objective: last-click, first-touch, multi-touch? |

**Step-by-Step Guidance**1. Audit your customer journey: Check time-lag reports in Google Analytics, CRM, or ad platforms
2. Segment by product/channel: Different campaigns may require different windows
3. Test and compare: Run parallel reporting with multiple windows (e.g., 7 vs. 30 days)
4. Standardize (where possible): Align windows across platforms to avoid double-counting
5. Review regularly: Revisit window length as your business, products, or customer behavior evolves

## Platform Comparison

| Platform | Default Click Window | Default View Window | Customization |
|----------|---------------------|---------------------|---------------|
| Facebook (Meta) | 7 days | 1 day | Limited (since iOS14) |
| Google Ads | 30 days | 1 day (view-through) | 1–90 days (click), 1–30 (view) |
| Adjust (MMP) | 7 days | 24 hours | Customizable |
| AppsFlyer (MMP) | 7 days | 24 hours | Customizable |
| Usermaven | Up to 180 days | Customizable | Extensive |
| Cometly | Custom | Custom | Extensive, real-time analysis |
| GA4 | 30 days | 1 day (engaged view) | 1–90 days (click), 1–30 (view) |

## Practical Examples

**Retail Flash Sale**- Attribution window: 1 day
- Why? Most purchases happen immediately after exposure
- Risk: Misses users who want to return later

**High-Consideration SaaS**- Attribution window: 30–90 days
- Why? Decision-making involves research, demos, approvals
- Risk: Over-credits if window is too long

**Multi-Touch, Multi-Platform**- User journey: Facebook Ad → Google Search Ad → Email → Conversion (over 2 weeks)
- Best practice: Use a 14–30 day window, multi-touch model, standardized settings
- Outcome: Each channel receives appropriate fractional credit

**Mobile App Install Campaign**- Attribution window: 7-day click, 24-hour view (industry standard for MMPs)
- Why? App installs typically occur soon after ad exposure

## Common Mistakes & Best Practices

**Common Mistakes**- Using platform defaults blindly: Default settings may not reflect your customer journey
- Inconsistent windows across platforms: Leads to double-counting or missed conversions
- Changing windows mid-campaign: Disrupts reporting
- Neglecting sales cycle differences: Short windows miss long journeys
- Lack of documentation: Teams lose track of settings

**Best Practices**- Standardize windows across platforms: Prevents overlap/double-counting
- Align with business goals and sales cycles: Tailor window to product, channel, and campaign
- Test and iterate: Adjust based on real data
- Document settings and changes: Maintain transparency and measurement integrity
- Segment by customer type or journey: Use different windows for new vs. repeat buyers
- Use advanced attribution tools: Platforms offer unified, customizable window management

## Frequently Asked Questions

**What's the difference between an attribution window, lookback window, and conversion window?**- Attribution window is the period after a touchpoint during which conversions are credited
- Lookback window often refers to how far back a platform looks for qualifying interactions
- Conversion window is the time frame defined for recording a conversion after interaction in some platforms

**How do I know what attribution window is right for my business?**- Analyze your sales cycle and customer journey
- Use time-lag and path analysis reports
- If 80% of conversions happen within 14 days, a 14-day window is a good fit

**What happens to conversions outside the window?**- They are not credited to the original touchpoint—often labeled "organic" or assigned to another channel

**Can different platforms use different attribution windows?**- Yes, often by default. Facebook, Google Ads, and analytics tools may not align
- Standardize where possible for clean, cross-channel reporting

**How often should I review or change my attribution window settings?**- Quarterly at minimum, or after major changes (e.g., new products, channels, shifts in customer behavior)

**Can I change attribution windows mid-campaign?**- Technically yes, but it will disrupt reporting consistency
- Best to change between campaigns or run parallel tests

**How do attribution windows affect ROAS and budget optimization?**- Longer windows may inflate ROAS by crediting more conversions
- Shorter windows can underreport
- Align window with your real customer journey for accurate ROI measurement

## References


1. Usermaven. (n.d.). Attribution Window. Usermaven Blog.
2. Fairing. (n.d.). What are Attribution Windows. Fairing Resources.
3. Anderson Collaborative. (2025). Attribution Window. Anderson Collaborative Knowledge Base.
4. Ongage. (n.d.). Attribution Window. Ongage Glossary.
5. Cometly. (n.d.). What Is Conversion Window Attribution. Cometly Blog.
6. AttributionApp. (n.d.). Attribution Windows Guide. AttributionApp Blog.
7. AppsFlyer. (n.d.). What is an attribution window?. AppsFlyer Glossary.
8. Google. (n.d.). About conversion windows. Google Ads Help.
9. Cometly. (n.d.). Cometly Channel. YouTube.
10. Meta. (n.d.). Attribution Settings. Meta Business Help.
11. Adjust. (n.d.). Attribution Window. Adjust Glossary.
