---
title: "Velocity (Agile)"
date: 2025-12-19
lastmod: 2026-04-02
translationKey: "Velocity--Agile-"
category: "Knowledge & Collaboration"
type: glossary
draft: false
url: /en/glossary/Velocity--Agile-/
description: "A relative measurement of the amount of work an agile team can complete within a single sprint. A metric enabling sprint planning and predictability."
keywords:
  - agile velocity
  - sprint planning
  - story points
  - team performance
  - scrum metrics
---

## What is Velocity (Agile)?

### Quick Understanding Zone

**In a nutshell**

Velocity is a metric that measures the relative amount of work an agile team can complete in one sprint (typically 1-4 weeks) using story points. It becomes a forecasting tool helping teams make realistic commitments based on past performance.

**Key points**

- **Measuring relative work volume** - Measured not in hours but in story points (relative complexity and effort)
- **Team-specific metric** - Don't use for comparing teams; apply it to track the same team's improvement
- **Basis for forecasting and planning** - Use past velocity to plan future sprints and predict releases

### Deep Dive Zone

**Why it matters**

Velocity is a mechanism for teams to objectively understand "what we can realistically accomplish" in the context of software development's inherent uncertainties. Relative sizing (this story is twice as complex as that) more accurately reflects actual team capacity than time-based estimates (this task takes 3 days). Through continuous velocity measurement, teams balance burnout prevention, realistic commitments, and quality maintenance.

**How it works**

The velocity cycle functions through the following flow.

First, in **backlog refinement**, the product owner and development team estimate user stories in story points. Using techniques like planning poker, the team reaches consensus on relative complexity.

Next, in **sprint planning**, the team reviews past velocity history. For example, if the average of the last five sprints is 40 points, they select approximately 40 points worth of stories this sprint.

During **daily standups** within the sprint, progress is confirmed and obstacles addressed to assess whether plans will complete on schedule.

At sprint end, **velocity equals the total points of complete stories meeting the definition of done**. Partially complete or quality-deficient stories don't count.

Finally, in **retrospectives**, performance is analyzed. If velocity drops, identify causes like team composition changes or increased technical debt, then establish improvement strategies.

Repeating this cycle, teams gain increasingly accurate estimation and stable velocity.

**Real-world use cases**

1. **Sprint planning** - A team with average 40-point velocity selects 38-42 points worth of stories for the next sprint, confidently committing to what they can achieve

2. **Release planning** - When 200 points of critical features are needed and team velocity averages 40 points per sprint (2 weeks), estimate 5 sprints (10 weeks) to completion, facilitating coordination with marketing

3. **Capacity forecasting** - When planning new projects, use velocity actual data to judge "this team can deliver this much in three months"

4. **Performance monitoring** - Continuous velocity decline signals problems like increasing technical debt or team member changes, enabling early discovery

**Benefits and considerations**

Benefits
- **Realistic planning** - Plans based on actual performance, not wishful thinking
- **Team autonomy improvement** - Members visualize their pace, advancing self-organization
- **Stakeholder trust building** - Cumulative track record of "delivering on promises" builds executive confidence
- **Early risk discovery** - Velocity anomalies quickly reveal problems

Considerations
- **No team comparison** - Comparing different teams' velocity causes gaming
- **Estimation calibration is essential** - Inconsistent story point definitions undermine velocity credibility
- **Vulnerable to team composition changes** - Member turnover requires recalibration periods
- **External factor fragility** - Technical debt and external dependencies prevent purely measuring team capacity

**Related terms**

- [Sprint](Sprint.md) - The time unit where velocity is measured
- [Story Points](Story-Points.md) - The basic unit of velocity measurement
- [Scrum](Scrum.md) - The agile framework leveraging velocity
- [Product Backlog](Product-Backlog.md) - The list of items measured by velocity
- [Definition of Done](Definition-of-Done.md) - The judgment standard when counting velocity

**Frequently asked questions**

**Q1: Does continuously increasing velocity mean the team is truly growing?**

A: Not necessarily. Early stages (first 3-5 sprints) may show increases from improved estimation accuracy. After stabilizing, that's normal. Continuous increases signal "estimation is drifting," "definition of done is loosening," or "gaming is occurring." What matters is "stability."

**Q2: How many sprints until a new team's velocity becomes trustworthy?**

A: Typically 3-5 sprints are needed. However, unstable member composition means restarting. Treat the first sprint as "calibration," learning from those results is crucial.

**Q3: When velocity suddenly drops, what should we do?**

A: Root cause identification is everything. Consider team composition changes, new technology adoption, increased bug fixes, estimation standard changes, and more. Retrospectives should thoroughly discuss whether it's "temporary variation" or "structural issues."
