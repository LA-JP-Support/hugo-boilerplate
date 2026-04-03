---
title: Definition of Done
date: 2025-12-19
lastmod: 2026-04-02
translationKey: definition-of-done
description: A checklist of criteria that must be met for work to be considered complete in Agile development. Ensures quality, testing, and documentation completeness.
keywords:
- definition of done
- DoD
- agile development
- scrum
- quality standards
category: Business & Strategy
type: glossary
draft: false
url: /en/glossary/definition-of-done/
---

## What is Definition of Done?

**Definition of Done (DoD) is a checklist of criteria that user stories and tasks must meet to be considered "complete."** It combines quality standards, testing requirements, documentation, security reviews, and more. It's a mechanism ensuring the entire team understands "done" consistently.

> **In a nutshell:** "Just like homework completion requires 'turned in papers,' 'reviewed your work,' and 'teacher confirmation,' development also pre-defines 'what makes it complete' through a checklist."

**Key points:**

- **What it does:** Document unifying "done" criteria across the team
- **Why it's needed:** Prevent quality variation; ensure shippable deliverables
- **Who uses it:** Development teams, scrum masters, product owners

## Why it matters

Without DoD, "done" interpretation varies by developer and project. One thinks "code finished" is done; another thinks it includes "testing." This ambiguity creates quality variation and increases production bugs.

Clear DoD alignment ensures everyone pursues the same goal. Estimation accuracy improves; "is it really done?" debate decreases. For new team member onboarding, it becomes learning material.

## How it works

DoD typically includes both technical and business aspects. Technical aspects include code review, unit testing, integration testing, documentation. Business aspects include acceptance criteria confirmation, stakeholder approval, performance verification.

Typical DoD elements include: **Code quality:** Complete code review, confirm coding standards compliance. **Testing:** Unit and integration tests executed, achieving specified coverage. **Documentation:** Technical and API documentation updated. **Integration:** Verify seamless integration with existing systems.

When starting DoD, begin simple: "code review complete," "testing complete"—three to five items. As the team matures, add performance testing, security review. Gradual expansion is effective.

## Real-world use cases

**New feature development**
For "add user registration feature," follow DoD: developer writes code, receives code review, executes manual and automated tests, updates documentation. Security team confirms password security, DBA confirms migration, then mark "done."

**Bug fixing**
Same process: reproduce problem, identify root cause, fix it, write test confirming the fix, verify existing tests unaffected, pass code review, deploy to production.

**Documentation updates**
When API specs change, code changes and documentation updates are both in DoD, enabling new members to understand the latest specification.

## Benefits and considerations

DoD's greatest benefit is quality consistency. All tasks meet the same criteria, reducing low-quality code in production. Estimation becomes more accurate; developers estimate realistic time knowing DoD requirements.

However, overly strict DoD can reduce productivity. Requiring perfect automated tests and security review for simple bug fixes wastes time. Regular DoD review and team maturity-based adjustment is important.

## Related terms

- **[Scrum](Scrum.md)** — DoD is a critical Scrum element, ensuring transparency during sprints
- **[User Story](User-Story.md)** — DoD criteria determine whether user stories are truly complete
- **[Sprint](Sprint.md)** — Each sprint end, verify work completes against DoD
- **[Acceptance Criteria](Acceptance-Criteria.md)** — Individual task requirements; DoD is universal to all tasks
- **[Code Review](Code-Review.md)** — Important process in DoD ensuring quality
- **[Test-Driven Development](Test-Driven-Development.md)** — Including test requirements in DoD promotes TDD

## Frequently asked questions

**Q: Should DoD include security review?**
A: Depends on data sensitivity. For systems handling personal or payment information, include security review. For non-sensitive internal tools, simplified versions work. Key is pre-deciding "which features need review."

**Q: Our DoD is too strict. What should we do?**
A: Recommend gradual review. After three months, ask the team "which criteria actually help?" Remove unused ones, keep genuinely necessary ones. Periodically check productivity and quality balance.

**Q: New team members aren't following DoD. How do I help?**
A: DoD reflects team agreement. During onboarding, explain the reasoning behind criteria, not just the rules. When people understand why, they follow voluntarily.
