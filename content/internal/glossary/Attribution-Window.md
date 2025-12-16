+++
title = "Attribution Window"
date = 2025-11-25
lastmod = 2025-12-05
translationKey = "attribution-window"
description = "An attribution window defines the period after a marketing interaction when conversions are credited to that touchpoint. Learn why it's crucial for campaign effectiveness and budget allocation."
keywords = ["attribution window", "marketing attribution", "conversion window", "campaign effectiveness", "digital advertising"]
category = "Analytics & Content Effectiveness"
type = "glossary"
draft = false
url = "/internal/glossary/Attribution-Window/"

+++
## What Is an Attribution Window?

An **attribution window** is a set period after a marketing interaction—like an ad click, impression, or view—during which conversions are credited to that touchpoint. This is a foundational concept in digital advertising and analytics, as it determines which touchpoints are “eligible” to receive credit for driving a conversion.

**Example:**  
If a user clicks your Facebook ad and purchases six days later, and your attribution window is 7 days, that ad gets credit for the conversion. If the purchase occurs on day eight, the ad receives no credit. This timing mechanism is crucial for evaluating which marketing efforts are actually driving results.

An attribution window (also called a **conversion window** or **lookback window**) is a core concept for marketers analyzing campaign effectiveness. It defines the period after a user interacts with a marketing channel (ad click, view, email open, etc.) in which a subsequent conversion can be attributed back to that interaction.

- **Start:** Clock starts when a user interacts with your marketing (e.g., clicks an ad, views a video, opens an email).
- **End:** Window closes after a set period (1, 7, 30, 90 days, etc.), depending on platform settings and business needs. Only conversions within this window are attributed to the given touchpoint.

> “An attribution window is the period of time in which a media partner can claim a click or impression engagement they generated, and that has materialized into an install of an advertiser’s app.”  
> — [AppsFlyer: What is an attribution window?](https://www.appsflyer.com/glossary/attribution-window/)

## Why Attribution Windows Matter

Attribution windows are critical to measuring campaign effectiveness, optimizing spend, and accurately understanding customer journeys.

- **Budget allocation:** Attribution windows shape which channels and campaigns appear most effective, influencing budget decisions.
- **Performance metrics:** Metrics like ROAS (Return on Ad Spend), CPA (Cost Per Acquisition), and others are affected by attribution timing.
- **Strategic decisions:** Attribution settings determine whether slow or fast-converting channels are undervalued or over-credited.

> “A key ingredient in any campaign, attribution windows set between advertisers and media partners define the framework in which a user’s install can be associated to the ad presented by the publisher, allowing non-immediate funnels to exist.”  
> — [AppsFlyer Glossary](https://www.appsflyer.com/glossary/attribution-window/)

Incorrect window settings lead to misattribution: 
- Undervaluing slow-converting channels (if the window is too short)
- Over-crediting passive exposures (if the window is too long)

## Types of Attribution Windows

Attribution windows vary by action, channel, and platform. The most common types are:

| **Type**                  | **What It Tracks**                                | **Common Use Cases**                          |
|---------------------------|---------------------------------------------------|-----------------------------------------------|
| **Click-based**           | User clicks (e.g., ad, email, link)               | Paid search, Facebook/Instagram Ads           |
| **View-through**          | User views (impression), no click                 | Display, video, social ads                    |
| **Custom windows**        | User-defined, flexible per channel                | Cross-platform, custom journeys               |
| **Event-based**           | Offline/online events (e.g., post-purchase survey)| Influencer, podcast, offline media            |

**Platform terminology nuances:**  
- **Google Ads:** “Conversion window” and “lookback window.”  
- **Meta (Facebook):** “Attribution setting” (window + model).  
- **AppsFlyer/Adjust:** “Attribution window” for both click and view engagements.

For mobile apps, the window is commonly discussed in the context of attributing installs to marketing partners:  
> “An attribution window is the period of time in which a media partner can claim a click or impression engagement they generated, and that has materialized into an install.”  
> — [AppsFlyer Glossary](https://www.appsflyer.com/glossary/attribution-window/)

### Attribution Window Length: Common Options & Use Cases

| **Window Length** | **Ideal For**                                | **Risks**                                   |
|-------------------|----------------------------------------------|---------------------------------------------|
| 1 day             | Flash sales, urgent offers                   | Misses delayed or researched conversions    |
| 7 days            | Mid-funnel, moderate consideration           | Can ignore slow-burn or high-value touchpoints|
| 14 days           | Products with moderate research phase        | May overcredit passive exposures            |
| 30 days           | High-AOV, long consideration products        | Over-attributes if decision cycle is shorter|
| 60–180 days       | B2B, SaaS, high-ticket, complex journeys     | Attribution overlap, diminishing influence  |

Some platforms (like [Usermaven](https://usermaven.com/blog/attribution-window)) support up to 180-day windows; most restrict to 90 days or less.

## How Attribution Window Length Affects Reporting

The length of your attribution window can dramatically alter campaign insights:

- **Short windows:**  
  - Undercount impact from channels with long consideration cycles.
  - Favor last-touch, direct-response tactics.
- **Long windows:**  
  - Capture more delayed conversions.
  - Risk over-crediting early, passive, or unrelated exposures.

**Example:**  
A customer sees your Facebook ad on Monday, clicks your Google ad on Wednesday, and finally converts through email on Friday.  
- *With a 1-day window, only the email gets credit.*  
- *With a 7-day window, all touchpoints may get partial credit, depending on your attribution model.*

> “If you set your conversion window to 7 days, any conversion that happens more than 7 days after the ad interaction won’t be recorded. This means it won’t appear in your reports.”  
> — [Google Ads Help: About conversion windows](https://support.google.com/google-ads/answer/3123169?hl=en)

The window you choose is as important as the attribution model (first-touch, last-touch, linear, time-decay, etc.). Together, they define how credit is distributed.

## Choosing the Right Attribution Window

No universal “best” window exists. The optimal length depends on your business model, sales cycle, customer behavior, and campaign goals.

### Decision Framework: The “TIME” Method

| **Factor**        | **Questions to Ask**                                             |
|-------------------|------------------------------------------------------------------|
| **Time to Conversion** | What’s the average lag between first touch and conversion?   |
| **Intent Level**        | Are users acting impulsively or after long research?        |
| **Marketing Mix**       | Are you using quick-response channels or nurturing over time?|
| **Evaluation Type**     | What’s your reporting objective: last-click, first-touch, multi-touch?|

### Step-by-Step Guidance

1. **Audit your customer journey:**  
   Check time-lag reports in Google Analytics ([Google Attribution reporting](https://support.google.com/google-ads/answer/1722023?hl=en)), CRM, or ad platforms.
2. **Segment by product/channel:**  
   Different campaigns may require different windows (e.g., retargeting vs. awareness).
3. **Test and compare:**  
   Run parallel reporting with multiple windows (e.g., 7 vs. 30 days) to see the impact.
4. **Standardize (where possible):**  
   Align windows across platforms to avoid double-counting and ensure apples-to-apples comparison.
5. **Review regularly:**  
   Revisit window length as your business, products, or customer behavior evolves.

> “If 75% of conversions happen between the 25th and 30th day after an ad interaction, you’ll want to make sure you set a window for at least this long, or you might miss recording conversions.”  
> — [Google Ads Help](https://support.google.com/google-ads/answer/3123169?hl=en)

## Attribution Windows Across Platforms: Comparison Table

| **Platform**         | **Default Click Window** | **Default View Window** | **Customization**               |
|----------------------|-------------------------|------------------------|---------------------------------|
| Facebook (Meta)      | 7 days                  | 1 day                  | Limited (since iOS14)           |
| Google Ads           | 30 days                 | 1 day (view-through)   | 1–90 days (click), 1–30 (view)  |
| Adjust (MMP)         | 7 days                  | 24 hours               | Customizable                    |
| AppsFlyer (MMP)      | 7 days                  | 24 hours               | Customizable                    |
| Usermaven            | Up to 180 days          | Customizable           | Extensive                       |
| Cometly              | Custom                  | Custom                 | Extensive, real-time analysis   |
| AttributionApp       | Custom                  | Custom                 | Extensive, machine learning     |
| GA4                  | 30 days                 | 1 day (engaged view)   | 1–90 days (click), 1–30 (view)  |

- **Facebook:** Customization is limited after Apple’s iOS14 privacy updates ([Meta Attribution Settings](https://www.facebook.com/business/help/460276478298895)).
- **Google Ads:** Allows separate windows per conversion action ([Official Help](https://support.google.com/google-ads/answer/3123169?hl=en)).
- **AppsFlyer/Adjust:** Widely used for mobile app campaigns, both offer customizable click/view windows ([AppsFlyer glossary](https://www.appsflyer.com/glossary/attribution-window/), [Adjust glossary](https://www.adjust.com/glossary/attribution-window/)).

> More platform-specific guidance:  

## Practical Examples & Use Cases

### Retail Flash Sale
- **Attribution window:** 1 day
- **Why?** Most purchases happen immediately after exposure; delayed conversions are rare.
- **Risk:** Misses users who want to return later, but generally aligns with intent.

### High-Consideration SaaS
- **Attribution window:** 30–90 days
- **Why?** Decision-making involves research, demos, approvals.
- **Risk:** Over-credits if window is too long, but under-credits with a short window.

### Multi-Touch, Multi-Platform
- **User journey:** Facebook Ad → Google Search Ad → Email → Conversion (over 2 weeks)
- **Best practice:** Use a 14–30 day window, multi-touch model, standardized settings.
- **Outcome:** Each channel receives appropriate fractional credit; reporting is consistent.

### Mobile App Install Campaign
- **Attribution window:** 7-day click, 24-hour view (industry standard for MMPs like AppsFlyer/Adjust)
- **Why?** App installs typically occur soon after ad exposure.

## Common Mistakes & Best Practices

### Common Mistakes

- **Using platform defaults blindly:**  
  Default settings may not reflect your customer journey.
- **Inconsistent windows across platforms:**  
  Leads to double-counting or missed conversions.
- **Changing windows mid-campaign:**  
  Disrupts reporting; makes pre- and post-change data incomparable.
- **Neglecting sales cycle differences:**  
  Short windows miss long journeys; long windows inflate the impact of minor touchpoints.
- **Lack of documentation:**  
  Teams lose track of what settings were used.

### Best Practices

- **Standardize windows across platforms:**  
  Prevents overlap/double-counting; enables reliable multi-channel analysis.
- **Align with business goals and sales cycles:**  
  Tailor window to product, channel, and campaign.
- **Test and iterate:**  
  Adjust based on real data; don’t “set and forget.”
- **Document settings and changes:**  
  Maintain [transparency](/en/glossary/transparency/) and measurement integrity.
- **Segment by customer type or journey:**  
  Use different windows for new vs. repeat buyers, B2B vs. B2C, etc.
- **Use advanced attribution tools:**  
  Platforms like [Usermaven](https://usermaven.com/blog/attribution-window), [AttributionApp](https://www.attributionapp.com/blog/attribution-windows/), and [Cometly](https://www.cometly.com/post/what-is-conversion-window-attribution) offer unified, customizable window management and reporting.

## Step-by-Step: Setting & Optimizing Attribution Windows

**1. Audit your current settings:**   
   List all active channels and their attribution settings. Identify inconsistencies and overlaps.

**2. Gather historical customer journey data:**  
   Use analytics to determine average time-to-conversion. Segment by channel, product, and customer type.

**3. Select preliminary window length:**  
   Use the TIME framework and industry benchmarks as a starting point.

**4. Run tests with different windows:**  
   Compare results using 7, 14, and 30-day windows. Analyze impact on KPIs and channel performance.

**5. Standardize and implement:**  
   Set chosen window(s) across all platforms where possible. Document all changes and communicate to stakeholders.

**6. Monitor and review:**  
   Schedule quarterly reviews, or after major business changes. Adjust as necessary based on customer journey and reporting needs.

**Official instructions for Google Ads:**  
[How to set or change conversion windows](https://support.google.com/google-ads/answer/3123169?hl=en)

## FAQs: Attribution Windows

**Q: What’s the difference between an attribution window, lookback window, and conversion window?**  
A:  
- *Attribution window* is the period after a touchpoint during which conversions are credited.
- *Lookback window* often refers to how far back a platform looks for qualifying interactions when a conversion is recorded.
- *Conversion window* is the time frame defined for recording a conversion after interaction in some platforms (e.g., Google Ads). Platform terminology varies—always check documentation.

**Q: How do I know what attribution window is right for my business?**  
A:  
Analyze your sales cycle and customer journey. Use time-lag and path analysis reports. If 80% of conversions happen within 14 days, a 14-day window is a good fit. Test and refine.

**Q: What happens to conversions outside the window?**  
A:  
They are not credited to the original touchpoint—often labeled “organic” or assigned to another channel depending on your attribution model.

**Q: Can different platforms use different attribution windows?**  
A:  
Yes, often by default. Facebook, Google Ads, and analytics tools may not align. Standardize where possible for clean, cross-channel reporting.

**Q: How often should I review or change my attribution window settings?**  
A:  
Quarterly at minimum, or after major changes (e.g., new products, channels, shifts in customer behavior).

**Q: Can I change attribution windows mid-campaign?**  
A:  
Technically yes, but it will disrupt reporting consistency. Best to change between campaigns or run parallel tests.

**Q: How do attribution windows affect ROAS and budget optimization?**  
A:  
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

**Template use:**  
This article structure can be adapted for other analytics glossary topics by following the same logical breakdown: concise definition, scenario/example, technical explanation, platform comparison, best practices, actionable steps, common mistakes, FAQs, conclusion, and curated further reading.

**For maximum clarity and trust, always refer to official documentation and platform resources before making changes to attribution window settings.**