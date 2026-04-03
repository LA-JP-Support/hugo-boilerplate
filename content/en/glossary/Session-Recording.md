---
title: Session Recording
date: '2026-04-02'
lastmod: 2026-04-02
translationKey: session-recording
description: Session Recording is an analytics technology that records and replays the interactions users perform on websites and apps.
keywords:
- Session Recording
- User Behavior Analysis
- UX Improvement
- User Experience
- Web Analytics
category: Data & Analytics
type: glossary
draft: false
url: /en/glossary/session-recording/
---

## What is Session Recording?

**Session Recording is a technology that captures all user actions (clicks, scrolls, inputs, etc.) on a website or app, then replays and analyzes them.** It makes user behavior visible and helps discover problems that numbers alone cannot reveal.

> **In a nutshell:** Like recording user operations on video tape and replaying them later.

**Key points:**

- **What it does:** Record all user clicks, scrolls, and inputs
- **Why it matters:** Discover actual user pain points and behavior patterns
- **Who uses it:** Website operators, UX designers, product managers

## Why it matters

[Web Analytics](Web-Analytics.md) provides statistical information like "how many people visited" and "where they clicked." But it doesn't answer "why" they clicked or "where" they struggled.

When you watch session recordings, user problems become obvious at a glance—users scrolling up and down repeatedly and getting lost, or frantically searching for a button. This information is far more valuable than statistics.

## How it works

Session recording uses multiple technologies:

**DOM recording:** Capture all changes to the page structure (DOM) and replay them later. Lightweight and efficient.

**Video recording:** Record the entire screen as video. Most accurate but requires significant storage.

**Event tracking:** Record individual events like mouse movements, clicks, and scrolls, then reconstruct them later.

For privacy protection, passwords and payment information are automatically masked.

Execution flow: User visits → JavaScript monitoring starts → All actions recorded → Sent to server → Recording played back and analyzed

## Real-world use cases

**Checkout optimization**
Discover where users abandon checkout and use those insights to simplify forms.

**Mobile app improvement**
Find buttons where tap positions are off and adjust their size.

**Customer support assistance**
When a customer reports an error, replay their actual actions to identify the cause.

## Benefits and considerations

**Benefits:** Visualize true user behavior and problems, gaining information worth many times more than data. Efficient bug report verification.

**Considerations:** Requires consent due to privacy concerns. Also requires storage and costs for large datasets. You face a dilemma of recording too much to analyze.

## Related terms

- **[Web Analytics](Web-Analytics.md)** — Analysis that includes Session Recording
- **[User Experience (UX)](User-Experience--UX-/)** — The area Session Recording improves
- **[A/B Testing](AB-Testing.md)** — Testing method combined with recording
- **[Heatmap](Heatmap.md)** — Visualization generated from recording data
- **[User Behavior](User-Behavior.md)** — Information captured by recording

## Frequently asked questions

**Q: Who can view the recorded data?**
A: Only teams with approval within the company can view it. You must strictly comply with privacy regulations.

**Q: Must every user be recorded?**
A: No. To reduce costs and protect privacy, typically only a percentage of users are recorded.
