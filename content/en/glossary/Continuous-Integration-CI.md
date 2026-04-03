---
title: Continuous Integration (CI)
date: 2025-03-01
lastmod: 2026-04-02
translationKey: continuous-integration-ci
description: A process that automatically tests code changes, continuously ensuring quality and enabling early bug detection.
keywords:
- Continuous Integration
- CI
- Automated Testing
- Build Automation
category: Cloud & Infrastructure
type: glossary
draft: false
url: /en/glossary/continuous-integration-ci/
---

## What is Continuous Integration (CI)?

**Continuous Integration (CI) is a process where each time developers commit code changes to a repository, automated builds and tests run immediately to ensure quality continuously.** Relying on machines rather than manual work, bugs and design problems surface early. Combined with [Git](Git.md) [pull requests](Pull-Request.md), it guarantees quality before reaching production—a foundational modern software development technology.

> **In a nutshell:** Each new code addition triggers a "test robot" that automatically checks and reports problems.

**Key points:**

- **What it does:** Automatically runs tests and quality checks when code changes
- **Why it's needed:** Detects bugs early, prevents flawed code from reaching production
- **Who uses it:** Modern software development teams everywhere

## Why it matters

Without CI, developers manually run tests every time, which takes time and invites human error. Testing gets forgotten or done incompletely—bugs reach production.

CI delivery enables:

First, early bug detection. Automated tests run within minutes of code changes, finding issues quickly before production.

Second, uninterrupted development. Removing manual test burden lets teams focus on coding. No test-waiting delays.

Third, quality visibility. CI dashboards make test success rates and coverage (percentage of tested code) visible to the whole team.

## How it works

CI typically follows these steps:

Developers push commits or create [pull requests](Pull-Request.md) to [Git](Git.md), automatically triggering CI.

CI first performs "build"—compiling source code to executable form and verifying dependencies resolve correctly. Build failure gets reported immediately.

After successful build, automated tests run: unit tests (individual functions), integration tests (module interactions), end-to-end tests (overall functionality)—as organizational policy dictates.

Test results are reported: success shows "green (OK)," failure shows "red (NG)." Failed tests notify developers to investigate and fix.

"Code quality analysis" often runs simultaneously, checking security vulnerabilities, code complexity, coverage sufficiency, etc.

This entire process completes within minutes. Developers see results and decide "proceed or fix."

## Real-world use cases

**Automated quality checks during pull requests**

Creating a [pull request](Pull-Request.md) auto-runs CI to verify all tests pass. Test failure marks status "red," signaling reviewers "not ready." Developers fix tests, push again. Passing tests signal "review ready."

**Production release verification**

Completed features merged to main trigger CI to run comprehensive test suites (unit, integration, performance, security). Pass completely → [Continuous Deployment](Continuous-Deployment-CD.md) deploys automatically. Failures halt deployment.

**Parallel development stability**

Multiple developers working in parallel branches get CI checking each branch. When merging, CI verifies no mutual impact and all tests pass.

## Benefits and considerations

CI's greatest benefits are automated bug detection and accelerated development cycles. Manual test burden disappears; developers focus on coding.

Team development discipline improves. "No production without tests" becomes system-enforced, raising quality consciousness.

However, initial CI setup costs effort. Deciding "which tests to automate" and "execution time limits" demands technical experience. Too many tests slow each run, delaying development.

Test quality is critical. "Having tests" doesn't guarantee safety—test content appropriateness is decisive. Inadequate tests miss bugs.

CI system reliability matters too. Unstable results (intermittent failures) make developers distrust CI, reducing its value.

## Related terms

- **[Git](Git.md)** — CI triggers on commits; the foundational version control
- **[Pull-Request](Pull-Request.md)** — CI runs during PR to determine merge readiness
- **[Continuous-Deployment](Continuous-Deployment-CD.md)** — CD proceeds after successful CI
- **[Configuration-Management](Configuration-Management.md)** — Code-based environment configuration enables CI reproducibility
- **[Code-Review](Code-Review.md)** — Combined with CI testing for multi-layer quality management

## Frequently asked questions

**Q: Is 10-minute test execution practical for CI?**

A: Development speed matters. Ideal is "under 3 minutes." At 10 minutes, consider parallel test execution or test optimization. Some security tests necessarily take time.

**Q: Test automation costs money—where to start?**

A: Automate "most frequently breaking" parts. Login feature automation dramatically reduces production risk. Phase automation gradually rather than all at once.

**Q: How do I handle test failures?**

A: Test failures signal quality issues. Investigate, fix, and improve. Never delete tests—that defeats the purpose.
