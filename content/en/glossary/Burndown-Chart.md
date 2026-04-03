---
title: Burndown Chart
date: 2025-12-19
lastmod: 2026-04-02
translationKey: Burndown-Chart
description: A burndown chart visualizes remaining work during agile sprints, showing at a glance whether teams will meet sprint goals.
keywords:
- Burndown Chart
- Agile Project Management
- Sprint Tracking
- Scrum Methodology
- Work Progress Visualization
category: Data & Analytics
type: glossary
draft: false
url: /en/glossary/burndown-chart/
---

## What is Burndown Chart?

**A burndown chart is a graph showing remaining work over time during sprint periods.** The horizontal axis shows days, vertical axis shows remaining work, comparing ideal progress lines with actual progress. With perfect on-schedule execution, the graph descends linearly toward zero at sprint end. This simple mechanism allows teams to determine at a glance whether sprint goals will be achieved, making it an essential tool for [Scrum](Scrum.md) and agile development teams.

> **In a nutshell:** A burndown chart visualizes "to-do list" progress. Decreasing work indicates smooth progress; unchanged work indicates delays—instantly apparent from the graph.

**Key points:**

- **What it does:** Records sprint work progress daily to determine if completion happens on schedule
- **Why it matters:** Enables team-wide progress sharing and early problem detection
- **Who uses it:** Scrum masters, development teams, product owners

## Why it matters

Burndown charts reveal when work stalls days before sprint end. Traditional project management discovers problems late, but daily-updated burndown charts make delays obvious by day three. This "visualization" lets teams quickly implement scope reduction or resource addition.

Psychological benefits are significant. Graphs descending toward bottom-right create "we're progressing" feelings, maintaining motivation. Flat graphs clarify issues, triggering investigation and improvement.

Accumulating sprint burndown data reveals team work speed ([velocity](Velocity.md)). "This team completes 100 story points per sprint" informs future sprint planning and estimate accuracy.

## How it works

Burndown charts update daily. On sprint day one, teams decide "we'll complete 100 story points this sprint," making 100 the chart's maximum. Daily, as tasks complete, values update to "95 points remaining," "80 points remaining," etc. These points form graph lines during scrum meetings.

Simultaneously, "ideal pace" is graphed. To complete 100 points in 10 days, teams should consume 10 points daily, creating a 10-day line reaching zero—the "ideal line."

If actual progress (remaining work) sits below the ideal line (less work remaining), progress is on track. If above (more work remaining), progress is behind. Just looking at the graph shows status.

Sprint scope additions create "jump-ups." Adding 20 points on day six makes the line jump up, visually showing "scope expanded," preventing stakeholder-team misalignment.

## Real-world use cases

**Sprint planning**
Starting a two-week sprint, teams create burndown charts. With 100 points across 14 working days, they know they should complete about 7 points daily.

**Daily standup reporting**
Morning team meetings review burndown charts. Progress updates like "Yesterday 5 points completed, total 45 completed. Ideal is 35 so we're on track" concisely report status.

**Mid-sprint adjustments**
At sprint midpoint, discovering "7 days passed but only 30 points done against 50-point ideal" triggers scope reduction or member addition, preventing sprint failure.

## Benefits and considerations

Burndown's major advantage is simplicity—everyone understands it. Non-technical managers and stakeholders grasp progress from graphs.

Considerations include inaccurate story point estimates reducing value, excessive mid-sprint additions reducing chart reliability, and bottlenecks (which task types are slow) remaining invisible. Burndown charts show "big picture," requiring other [metrics](Metrics.md) for detailed analysis.

## Related terms

- **[Scrum](Scrum.md)** — The agile framework utilizing burndown charts
- **[Story Points](Story-Points.md)** — Work estimation units
- **[Velocity](Velocity.md)** — Average sprint completion quantity
- **[Sprint](Sprint.md)** — Agile development's basic iteration period
- **[Agile](Agile.md)** — Development methodology employing burndown charts

## Frequently asked questions

**Q: Is estimating with story points difficult?**
A: Initially, yes. After several sprint experiences, teams develop intuition. Estimating like "this resembles that previous 5-point task, so it's 5 points" uses past comparisons.

**Q: What if burndown stays above the ideal line?**
A: Either reduce scope or add resources. Adding resources post-sprint-start reduces efficiency, so usually scope reduces. "We complete 80 points; 20 points push to next sprint."

**Q: Can burndown charts help retrospectives?**
A: Yes. Patterns emerge—"started behind but accelerated at end" versus "steady pace"—revealing psychological or organizational factors. This drives process improvements.
