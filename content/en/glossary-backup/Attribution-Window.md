---
title: "Attribution Window"
date: 2025-11-25
lastmod: 2025-12-05
translationKey: "attribution-window"
description: "An attribution window defines the period after a marketing interaction when conversions are credited to that touchpoint. Learn why it's crucial for campaign effectiveness and budget allocation."
keywords: ["attribution window", "marketing attribution", "conversion window", "campaign effectiveness", "digital advertising"]
category: "Analytics & Content Effectiveness"
type: "glossary"
draft: false
---
## What Is an Attribution Window?

An <strong>attribution window</strong>is a set period after a marketing interaction—like an ad click, impression, or view—during which conversions are credited to that touchpoint. This is a foundational concept in digital advertising and analytics, as it determines which touchpoints are “eligible” to receive credit for driving a conversion.

<strong>Example:</strong>If a user clicks your Facebook ad and purchases six days later, and your attribution window is 7 days, that ad gets credit for the conversion. If the purchase occurs on day eight, the ad receives no credit. This timing mechanism is crucial for evaluating which marketing efforts are actually driving results.

An attribution window (also called a <strong>conversion window</strong>or <strong>lookback window</strong>) is a core concept for marketers analyzing campaign effectiveness. It defines the period after a user interacts with a marketing channel (ad click, view, email open, etc.) in which a subsequent conversion can be attributed back to that interaction.

- <strong>Start:</strong>Clock starts when a user interacts with your marketing (e.g., clicks an ad, views a video, opens an email).
- <strong>End:</strong>Window closes after a set period (1, 7, 30, 90 days, etc.), depending on platform settings and business needs. Only conversions within this window are attributed to the given touchpoint.

> “An attribution window is the period of time in which a media partner can claim a click or impression engagement they generated, and that has materialized into an install of an advertiser’s app.”  
> — [AppsFlyer: What is an attribution window?](https://www.appsflyer.com/glossary/attribution-window/)

## Why Attribution Windows Matter

Attribution windows are critical to measuring campaign effectiveness, optimizing spend, and accurately understanding customer journeys.

- <strong>Budget allocation:</strong>Attribution windows shape which channels and campaigns appear most effective, influencing budget decisions.
- <strong>Performance metrics:</strong>Metrics like ROAS (Return on Ad Spend), CPA (Cost Per Acquisition), and others are affected by attribution timing.
- <strong>Strategic decisions:</strong>Attribution settings determine whether slow or fast-converting channels are undervalued or over-credited.

> “A key ingredient in any campaign, attribution windows set between advertisers and media partners define the framework in which a user’s install can be associated to the ad presented by the publisher, allowing non-immediate funnels to exist.”  
> — [AppsFlyer Glossary](https://www.appsflyer.com/glossary/attribution-window/)

Incorrect window settings lead to misattribution: 
- Undervaluing slow-converting channels (if the window is too short)
- Over-crediting passive exposures (if the window is too long)

## Types of Attribution Windows

Attribution windows vary by action, channel, and platform. The most common types are:

| <strong>Type</strong>| <strong>What It Tracks</strong>| <strong>Common Use Cases</strong>|
|---------------------------|---------------------------------------------------|-----------------------------------------------|
| <strong>Click-based</strong>| User clicks (e.g., ad, email, link)               | Paid search, Facebook/Instagram Ads           |
| <strong>View-through</strong>| User views (impression), no click                 | Display, video, social ads                    |
| <strong>Custom windows</strong>| User-defined, flexible per channel                | Cross-platform, custom journeys               |
| <strong>Event-based</strong>| Offline/online events (e.g., post-purchase survey)| Influencer, podcast, offline media            |

<strong>Platform terminology nuances:</strong>- <strong>Google Ads:</strong>“Conversion window” and “lookback window.”  
- <strong>Meta (Facebook):</strong>“Attribution setting” (window + model).  
- <strong>AppsFlyer/Adjust:</strong>“Attribution window” for both click and view engagements.

For mobile apps, the window is commonly discussed in the context of attributing installs to marketing partners:  
> “An attribution window is the period of time in which a media partner can claim a click or impression engagement they generated, and that has materialized into an install.”  
> — [AppsFlyer Glossary](https://www.appsflyer.com/glossary/attribution-window/)

### Attribution Window Length: Common Options & Use Cases

| <strong>Window Length</strong>| <strong>Ideal For</strong>| <strong>Risks</strong>|
|-------------------|----------------------------------------------|---------------------------------------------|
| 1 day             | Flash sales, urgent offers                   | Misses delayed or researched conversions    |
| 7 days            | Mid-funnel, moderate consideration           | Can ignore slow-burn or high-value touchpoints|
| 14 days           | Products with moderate research phase        | May overcredit passive exposures            |
| 30 days           | High-AOV, long consideration products        | Over-attributes if decision cycle is shorter|
| 60–180 days       | B2B, SaaS, high-ticket, complex journeys     | Attribution overlap, diminishing influence  |

Some platforms (like [Usermaven](https://usermaven.com/blog/attribution-window)) support up to 180-day windows; most restrict to 90 days or less.

## How Attribution Window Length Affects Reporting

The length of your attribution window can dramatically alter campaign insights:

- <strong>Short windows:</strong>- Undercount impact from channels with long consideration cycles.
  - Favor last-touch, direct-response tactics.
- <strong>Long windows:</strong>- Capture more delayed conversions.
  - Risk over-crediting early, passive, or unrelated exposures.

<strong>Example:</strong>A customer sees your Facebook ad on Monday, clicks your Google ad on Wednesday, and finally converts through email on Friday.  
- *With a 1-day window, only the email gets credit.*  
- *With a 7-day window, all touchpoints may get partial credit, depending on your attribution model.*

> “If you set your conversion window to 7 days, any conversion that happens more than 7 days after the ad interaction won’t be recorded. This means it won’t appear in your reports.”  
> — [Google Ads Help: About conversion windows](https://support.google.com/google-ads/answer/3123169?hl=en)

The window you choose is as important as the attribution model (first-touch, last-touch, linear, time-decay, etc.). Together, they define how credit is distributed.

## Choosing the Right Attribution Window

No universal “best” window exists. The optimal length depends on your business model, sales cycle, customer behavior, and campaign goals.

### Decision Framework: The “TIME” Method

| <strong>Factor</strong>| <strong>Questions to Ask</strong>|
|-------------------|------------------------------------------------------------------|
| <strong>Time to Conversion</strong>| What’s the average lag between first touch and conversion?   |
| <strong>Intent Level</strong>| Are users acting impulsively or after long research?        |
| <strong>Marketing Mix</strong>| Are you using quick-response channels or nurturing over time?|
| <strong>Evaluation Type</strong>| What’s your reporting objective: last-click, first-touch, multi-touch?|

### Step-by-Step Guidance

1. <strong>Audit your customer journey:</strong>Check time-lag reports in Google Analytics ([Google Attribution reporting](https://support.google.com/google-ads/answer/1722023?hl=en)), CRM, or ad platforms.
2. <strong>Segment by product/channel:</strong>Different campaigns may require different windows (e.g., retargeting vs. awareness).
3. <strong>Test and compare:</strong>Run parallel reporting with multiple windows (e.g., 7 vs. 30 days) to see the impact.
4. <strong>Standardize (where possible):</strong>Align windows across platforms to avoid double-counting and ensure apples-to-apples comparison.
5. <strong>Review regularly:</strong>Revisit window length as your business, products, or customer behavior evolves.

> “If 75% of conversions happen between the 25th and 30th day after an ad interaction, you’ll want to make sure you set a window for at least this long, or you might miss recording conversions.”  
> — [Google Ads Help](https://support.google.com/google-ads/answer/3123169?hl=en)

## Attribution Windows Across Platforms: Comparison Table

| <strong>Platform</strong>| <strong>Default Click Window</strong>| <strong>Default View Window</strong>| <strong>Customization</strong>|
|----------------------|-------------------------|------------------------|---------------------------------|
| Facebook (Meta)      | 7 days                  | 1 day                  | Limited (since iOS14)           |
| Google Ads           | 30 days                 | 1 day (view-through)   | 1–90 days (click), 1–30 (view)  |
| Adjust (MMP)         | 7 days                  | 24 hours               | Customizable                    |
| AppsFlyer (MMP)      | 7 days                  | 24 hours               | Customizable                    |
| Usermaven            | Up to 180 days          | Customizable           | Extensive                       |
| Cometly              | Custom                  | Custom                 | Extensive, real-time analysis   |
| AttributionApp       | Custom                  | Custom                 | Extensive, machine learning     |
| GA4                  | 30 days                 | 1 day (engaged view)   | 1–90 days (click), 1–30 (view)  |

- <strong>Facebook:</strong>Customization is limited after Apple’s iOS14 privacy updates ([Meta Attribution Settings](https://www.facebook.com/business/help/460276478298895)).
- <strong>Google Ads:</strong>Allows separate windows per conversion action ([Official Help](https://support.google.com/google-ads/answer/3123169?hl=en)).
- <strong>AppsFlyer/Adjust:</strong>Widely used for mobile app campaigns, both offer customizable click/view windows ([AppsFlyer glossary](https://www.appsflyer.com/glossary/attribution-window/), [Adjust glossary](https://www.adjust.com/glossary/attribution-window/)).

> More platform-specific guidance:  

## Practical Examples & Use Cases

### Retail Flash Sale
- <strong>Attribution window:</strong>1 day
- <strong>Why?</strong>Most purchases happen immediately after exposure; delayed conversions are rare.
- <strong>Risk:</strong>Misses users who want to return later, but generally aligns with intent.

### High-Consideration SaaS
- <strong>Attribution window:</strong>30–90 days
- <strong>Why?</strong>Decision-making involves research, demos, approvals.
- <strong>Risk:</strong>Over-credits if window is too long, but under-credits with a short window.

### Multi-Touch, Multi-Platform
- <strong>User journey:</strong>Facebook Ad → Google Search Ad → Email → Conversion (over 2 weeks)
- <strong>Best practice:</strong>Use a 14–30 day window, multi-touch model, standardized settings.
- <strong>Outcome:</strong>Each channel receives appropriate fractional credit; reporting is consistent.

### Mobile App Install Campaign
- <strong>Attribution window:</strong>7-day click, 24-hour view (industry standard for MMPs like AppsFlyer/Adjust)
- <strong>Why?</strong>App installs typically occur soon after ad exposure.

## Common Mistakes & Best Practices

### Common Mistakes

- <strong>Using platform defaults blindly:</strong>Default settings may not reflect your customer journey.
- <strong>Inconsistent windows across platforms:</strong>Leads to double-counting or missed conversions.
- <strong>Changing windows mid-campaign:</strong>Disrupts reporting; makes pre- and post-change data incomparable.
- <strong>Neglecting sales cycle differences:</strong>Short windows miss long journeys; long windows inflate the impact of minor touchpoints.
- <strong>Lack of documentation:</strong>Teams lose track of what settings were used.

### Best Practices

- <strong>Standardize windows across platforms:</strong>Prevents overlap/double-counting; enables reliable multi-channel analysis.
- <strong>Align with business goals and sales cycles:</strong>Tailor window to product, channel, and campaign.
- <strong>Test and iterate:</strong>Adjust based on real data; don’t “set and forget.”
- <strong>Document settings and changes:</strong>Maintain transparency and measurement integrity.
- <strong>Segment by customer type or journey:</strong>Use different windows for new vs. repeat buyers, B2B vs. B2C, etc.
- <strong>Use advanced attribution tools:</strong>Platforms like [Usermaven](https://usermaven.com/blog/attribution-window), [AttributionApp](https://www.attributionapp.com/blog/attribution-windows/), and [Cometly](https://www.cometly.com/post/what-is-conversion-window-attribution) offer unified, customizable window management and reporting.

## Step-by-Step: Setting & Optimizing Attribution Windows

<strong>1. Audit your current settings:</strong>List all active channels and their attribution settings. Identify inconsistencies and overlaps.

<strong>2. Gather historical customer journey data:</strong>Use analytics to determine average time-to-conversion. Segment by channel, product, and customer type.

<strong>3. Select preliminary window length:</strong>Use the TIME framework and industry benchmarks as a starting point.

<strong>4. Run tests with different windows:</strong>Compare results using 7, 14, and 30-day windows. Analyze impact on KPIs and channel performance.

<strong>5. Standardize and implement:</strong>Set chosen window(s) across all platforms where possible. Document all changes and communicate to stakeholders.

<strong>6. Monitor and review:</strong>Schedule quarterly reviews, or after major business changes. Adjust as necessary based on customer journey and reporting needs.

<strong>Official instructions for Google Ads:</strong>[How to set or change conversion windows](https://support.google.com/google-ads/answer/3123169?hl=en)

## FAQs: Attribution Windows

<strong>Q: What’s the difference between an attribution window, lookback window, and conversion window?</strong>A:  
- *Attribution window* is the period after a touchpoint during which conversions are credited.
- *Lookback window* often refers to how far back a platform looks for qualifying interactions when a conversion is recorded.
- *Conversion window* is the time frame defined for recording a conversion after interaction in some platforms (e.g., Google Ads). Platform terminology varies—always check documentation.

<strong>Q: How do I know what attribution window is right for my business?</strong>A:  
Analyze your sales cycle and customer journey. Use time-lag and path analysis reports. If 80% of conversions happen within 14 days, a 14-day window is a good fit. Test and refine.

<strong>Q: What happens to conversions outside the window?</strong>A:  
They are not credited to the original touchpoint—often labeled “organic” or assigned to another channel depending on your attribution model.

<strong>Q: Can different platforms use different attribution windows?</strong>A:  
Yes, often by default. Facebook, Google Ads, and analytics tools may not align. Standardize where possible for clean, cross-channel reporting.

<strong>Q: How often should I review or change my attribution window settings?</strong>A:  
Quarterly at minimum, or after major changes (e.g., new products, channels, shifts in customer behavior).

<strong>Q: Can I change attribution windows mid-campaign?</strong>A:  
Technically yes, but it will disrupt reporting consistency. Best to change between campaigns or run parallel tests.

<strong>Q: How do attribution windows affect ROAS and budget optimization?</strong>A:  
Longer windows may inflate ROAS by crediting more conversions; shorter windows can underreport. Align window with your real customer journey for accurate ROI measurement.

For further technical FAQs, see:  
- [Google Ads: About conversion windows](https://support.google.com/google-ads/answer/3123169?hl=en)
- [AppsFlyer: Attribution window](https://www.appsflyer.com/glossary/attribution-window/)

## Further Reading & References

- [Usermaven on Attribution Window](https://usermaven.com/blog/attribution-window)
- [Fairing: What are Attribution Windows](https://fairing.co/resources/measurement-faqs/what-are-attribution-windows)
- [Anderson Collaborative: Attribution Window](https://www.andersoncollaborative.com/knowledge-base/what-is-an-attribution-window-choose-the-right-settings-in-2025/)
- [Ongage Glossary: Attribution Window](https://www.ongage.com/glossary/attribution-window/)
- [Cometly: What Is Conversion Window Attribution](https://www.cometly.com/post/what-is-conversion-window-attribution)
- [AttributionApp: Attribution Windows Guide](https://www.attributionapp.com/blog/attribution-windows/)
- [AppsFlyer: What is an attribution window?](https://www.appsflyer.com/glossary/attribution-window/)
- [Google Ads Help: About conversion windows](https://support.google.com/google-ads/answer/3123169?hl=en)
- [YouTube - Cometly Channel](https://www.youtube.com/@Cometly)

<strong>Template use:</strong>This article structure can be adapted for other analytics glossary topics by following the same logical breakdown: concise definition, scenario/example, technical explanation, platform comparison, best practices, actionable steps, common mistakes, FAQs, conclusion, and curated further reading.

<strong>For maximum clarity and trust, always refer to official documentation and platform resources before making changes to attribution window settings.</strong>
