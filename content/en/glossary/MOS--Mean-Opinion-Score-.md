---
title: MOS (Mean Opinion Score)
date: 2025-12-19
lastmod: 2026-04-02
translationKey: MOS--Mean-Opinion-Score-
description: MOS is a standard measurement method where multiple users evaluate audio and video quality on a 1-5 scale, and the average value quantifies quality based on human perception.
keywords:
- Mean Opinion Score
- MOS evaluation
- quality measurement
- subjective assessment
- audio quality
category: Data & Analytics
type: glossary
draft: false
url: /en/glossary/mos--mean-opinion-score-/
---

## What is MOS (Mean Opinion Score)?

**MOS is a standard quality measurement method where multiple users evaluate audio or video quality on a 1-5 scale and the average value quantifies that quality.** Unlike technical metrics such as signal-to-noise ratio, it numerically expresses "how humans actually perceive quality." It is the most trusted metric for telecommunications providers, broadcasters, and streaming services to determine whether quality improvement is necessary.

> **In a nutshell:** A test method that asks multiple people "how is this video quality actually?" and determines quality by averaging their scores.

**Key points:**

- **What it does:** Quality measurement based on human perception (different from technical metrics)
- **Why it matters:** Systems may be technically normal but provide poor user experience
- **Who uses it:** Telecom carriers, video streaming companies, voice communication companies, equipment manufacturers

## Why it matters

When VoIP audio quality is described as "2% data loss rate," it is unclear how bad the user experience actually is. With MOS, you immediately understand quality level at a glance as "4.2 points (almost no problems)." When introducing new codecs, network configurations, or encoding settings, comparing by MOS rather than technical metrics reveals the actual improvement effect. This provides important evidence for prioritizing development investments and guaranteeing quality to customers.

## How it works

MOS testing is conducted in five steps. **Test design** selects evaluation content (videos and audio samples of various qualities). **Participant recruitment** gathers representative users without hearing impairments. **Environment setup** standardizes external factors like noise and lighting to ensure fair evaluation. **Sample presentation and evaluation** shows multiple samples to participants in sequence, who rate each 1-5. **Statistical analysis** calculates average ratings and confidence intervals.

The rating scale meaning is standardized: 5 points is "excellent" (usable quality for daily use), 4 points is "good" (no problems for commercial use), 3 points is "fair" (some users dissatisfied), 2 points is "poor" (most dissatisfied), and 1 point is "bad" (barely usable).

## Calculation method

MOS = (Sum of all ratings) ÷ (Number of raters)

Example: If 10 people rate a video and scores are "5, 4, 4, 5, 3, 4, 4, 5, 4, 4":
MOS = (5+4+4+5+3+4+4+5+4+4) ÷ 10 = 42 ÷ 10 = 4.2 points

Typically, **confidence intervals are also reported**. For example, "MOS 4.2 ± 0.3 (95% confidence interval)" means there is 95% probability the true mean falls between 3.9-4.5 points.

## Benchmarks

| MOS Score | Quality Level | User Satisfaction | Typical Applications | Practical Assessment |
|----------|-----------|-------------|---------------------|-----------|
| 4.5-5.0 | Excellent | Very Satisfied | Reference quality, premium services | Operate at highest quality |
| 4.0-4.4 | Good | Satisfied | Commercial VoIP, standard delivery | Practical level |
| 3.5-3.9 | Acceptable | Somewhat Dissatisfied | Low-bandwidth baseline | Target for improvement |
| 3.0-3.4 | Fair | Dissatisfaction evident | Emergency response level | Early improvement essential |
| 2.5-2.9 | Poor | Highly Dissatisfied | Emergency communication only | Cannot operate |
| 2.0-2.4 | Bad | Nearly unusable | Rehabilitation/testing | Immediate improvement |

**Industry-specific targets:**
- **VoIP (voice calling):** Target MOS 4.0 or above. Below 3.5 increases cancellations
- **Video delivery:** Target MOS 4.2 or above. Sports broadcasts recommend 4.5+
- **Streaming music:** Target MOS 4.5+ (high quality even with compressed audio)

## Real-world use cases

**Network improvement by telecom carriers**
Before deploying new voice codecs nationwide, measure MOS with multiple configurations to confirm actual quality improvement benefits.

**Video platform quality monitoring**
Monitor real-time MOS, and when network failure causes degradation, automatically reduce bitrate to prevent "unwatchable" situations.

**Game streaming latency mitigation**
Balance voice quality (MOS 4.0+) and video quality (MOS 4.2+) to optimize communication quality during gameplay.

## Benefits and considerations

**On the benefits side,** MOS is understandable to non-technical users, making quality improvement prioritization easy. It is trusted as a standard recognized by regulators with high reliability and enables international comparison.

**As for considerations,** MOS testing involves human evaluation, which can introduce bias based on demographics (age, technical literacy). If testing occurs in environments different from actual use scenarios, real-world divergence can occur. As quality perception changes over time, periodic retesting is necessary.

## Related terms

- **[Quality Assurance](Quality-Assurance.md)** — Foundation of quality management that MOS supports
- **[Video Codec](Video-Codec.md)** — Compression technology subject to video MOS measurement
- **[Network Optimization](Network-Optimization.md)** — Improvement initiatives based on MOS results
- **[User Experience](User-Experience.md)** — User satisfaction that MOS measures
- **[A/B Testing](A-B-Testing.md)** — Comparative verification method using MOS

## Frequently asked questions

**Q: What is the relationship between MOS and objective quality metrics (PSNR, etc.)?**
A: MOS is subjective while PSNR is objective—they are different. Typically, both are combined: objective metrics enable real-time automated monitoring while MOS periodically confirms actual user experience.

**Q: What criteria determine new codec adoption?**
A: Consider adoption if expecting 0.2+ point improvement. Below 0.1 point improvement is judged not worth the compatibility cost.

**Q: Does MOS differ across scenes (sports vs. movies)?**
A: Yes, it does. The same MOS score produces different user experiences between dynamic sports broadcasts and static movies. Individual testing for each use case is necessary.
