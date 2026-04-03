---
title: Canary Release
date: 2025-12-19
lastmod: 2026-04-02
translationKey: canary-release
description: A canary release is a deployment strategy that gradually rolls out a new version to a small subset of users to detect issues early before full rollout.
keywords:
- canary release
- deployment strategy
- continuous delivery
- risk mitigation
- software deployment
category: Data & Analytics
type: glossary
draft: false
url: /en/glossary/canary-release/
---

## What is a Canary Release?

**A canary release is a deployment strategy where a new version is not released to everyone at once, but instead is initially released to a limited number of users, problems are verified, and then the rollout is gradually expanded.** The name comes from the historical practice of miners bringing canaries into mines to provide early warning of the danger of toxic gases. If "canary" users discover a problem, adjustments can be made before it impacts the entire user base.

> **In a nutshell:** A canary release is like "testing a new menu item in just a few store locations first, observing customer reaction, and then rolling it out chain-wide."

**Key points:**

- **What it does:** Gradually deploys a new version starting with a small number of users and detects issues in stages
- **Why it's needed:** To prevent large-scale outages and maintain system stability while advancing improvements rapidly
- **Who uses it:** SaaS companies, large-scale web applications, companies practicing continuous delivery

## Why it matters

Releasing a version update to all users at once and discovering a critical bug means millions are affected. It takes time to fix, and the company loses trust. With canary releases, only 1% of users get the new version initially, so problems are limited. If no issues appear, the rollout expands to 5%, 10%, and eventually 100%. This process allows discovery of real production environment issues that can't be found in the testing phase.

## How it works

The process is straightforward. First, develop the new version and perform standard testing in a test environment. Then, in the production environment, route "1-5% of traffic" to the new version. Monitor this "canary" user behavior for 24 hours, checking whether error rates are increasing or page load speeds are decreasing. If there are no problems, gradually increase the percentage to 10%, 20%, and so on. If a critical issue is found, immediately revert all traffic back to the previous version.

## Real-world use cases

**New feature release** If a bug exists in a new feature, only a small number of users are affected, allowing quick fixes.

**API changes** When changing backend specifications, gradual deployment detects integration problems with other systems early.

**Performance-focused changes** When optimizing database queries, gradual deployment allows verification that there are no issues under actual load.

**Significant UI changes** During design or layout changes, you can observe user reactions and make adjustments accordingly.

## Benefits and considerations

Benefits include minimizing risk while enabling rapid improvements. Data-driven decision-making is possible, and rollback (reverting to the previous version) can happen quickly if issues arise.

As a consideration, there is technical complexity. Since both old and new versions operate simultaneously, system design becomes complex. Additionally, some users get early access to new features while others still use the old version, which may raise questions like "Why do I see different features?"

## Frequently asked questions

**Q: What's the difference from Blue-Green deployment?**
A: Blue-Green switches all users to the new version at once. Canary switches gradually. Canary provides greater risk reduction benefits but more complex management.

**Q: How gradually should the rollout proceed?**
A: Typically, 1% → 5% → 10% → 25% → 50% → 100%. Each stage should be monitored for at least 24 hours to confirm no issues.

**Q: Do canary users realize they're testing?**
A: Usually they don't. However, some users may realize they're being tested by seeing new features or new UI. Advance announcements help.

## References

- [Martin Fowler: Canary Release](https://martinfowler.com/bliki/CanaryRelease.html)
- [Google Cloud: Canary Deployments](https://cloud.google.com/deploy/docs/deployment-strategies/canary)
- [Netflix: Kayenta Canary Analysis](https://netflix.github.io/)
- [LaunchDarkly: Feature Flags for Canary](https://launchdarkly.com/)
- [Spinnaker: Deployment Strategies](https://spinnaker.io/)
- [Kubernetes: Rolling Updates](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)
- [AWS CodeDeploy: Rolling Deployment](https://docs.aws.amazon.com/codedeploy/)
- [Harness: Continuous Deployment](https://harness.io/)
