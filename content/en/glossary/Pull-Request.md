---
title: "Pull Request"
date: 2025-03-01
lastmod: 2026-04-02
translationKey: "pull-request"
description: "A proposal to integrate changes into the main codebase. A Git-based process for documenting, explaining, and reviewing changes before integration."
keywords:
  - Pull Request
  - PR
  - Merge Request
  - Change Proposal
category: "Knowledge & Collaboration"
type: glossary
draft: false
url: /en/glossary/Pull-Request/
---

## What is a Pull Request?

**A Pull Request (PR) is a formal proposal to integrate changes made on a development branch into the main codebase.** Rather than simply notifying "I changed this file," it explicitly explains "what was changed" and "why it was changed," allowing teammates to review and approve before integration. This Git-based workflow is essential for team development.

> **In a nutshell:** "Can my code go into the main branch? Can you check it?" – a formal approval form for software development teams.

**Key points:**

- **What it does:** Explicitly propose and manage integration of changes from development branches to main codebase
- **Why it matters:** To implement quality control and code review systematically
- **Who uses it:** All software development teams

## Why it matters

Without pull requests, managing multiple developers' changes to the main codebase becomes uncontrolled. There's no record of the intent behind each change.

Pull requests achieve several critical outcomes:

**Transparency of changes:** All team members can see "what changes are pending" and "why these changes are needed."

**Quality gates:** By making code review mandatory, you ensure code quality before it reaches production. Making merges impossible without review prevents defects from reaching production.

**Traceability:** "This bug was introduced by which code, when, and for what purpose?" becomes traceable through PR logs. This enables efficient root cause analysis when issues occur.

## How it works

The entire PR flow is built on Git's branching functionality.

When developers work on new features or fixes, they create a new branch (e.g., feature/login) branched from main. They implement changes following the relevant specifications.

When implementation is complete and local tests pass, developers push the branch to the remote repository.

Next, they create a PR on a Git hosting service (GitHub, GitLab, etc.). Here they write explanations of "what was done" and "why." Good PRs include related issue numbers, background of changes, testing methods, and known limitations.

Team members review the PR, conducting code review. Questions or comments are discussed on the PR. Developers make revisions based on feedback. New commits automatically appear in the PR.

When all reviewers approve, the PR is merged. Changes from feature/login branch are integrated into main.

Then continuous integration systems run automated tests, and deployment to production follows in modern development workflows.

## Real-world use cases

**Proposing and validating new features**

Designers propose new UI; development teams implement it. After implementation, designers and developers verify through PR that "implementation matches design" and "performance is acceptable." Visual review requests can be made in PR comments.

**Quality assurance for bug fixes**

When bugs are found in production, hotfix branches enable rapid fixes. Once complete, a PR enables swift review. Bug fixes "must be correct," making double-checking through PR critical.

**Managing security updates**

When security vulnerabilities in dependencies are discovered, PRs clarify the update scope and impact before integration into main. "Which library was updated" and "are there compatibility issues" remain documented.

## Benefits and considerations

PR's greatest benefit is achieving transparency and quality assurance systematically. All team members know "what's awaiting approval," making development progress visible.

PRs also become knowledge-sharing records. Discussions about "why this implementation" remain in comments, becoming learning material for newcomers and those seeking architectural history.

A consideration is that PR processes create "overhead." Even small changes require certain procedures, and some organizations feel development speed suffers. However, considering cost of production bugs, this overhead has substantial value.

Also avoid PRs remaining "pending" for long periods. Load-balancing reviewers and setting PR approval SLAs become key team management points.

## Related terms

- **Git** — The version control system enabling pull requests
- **Code Review** — The core practice of PR approval process
- **Continuous Integration** — Running automated tests during PR
- **Continuous Deployment** — Process from PR merge to automatic deployment
- **API Documentation** — Technical standard that PR review follows

## Frequently asked questions

**Q: Is a PR necessary even for tiny changes (one line)?**

A: Fundamentally yes. "Just one line" judgments skip peer review. However, some organizations exempt certain operations like documentation changes.

**Q: What's the average PR wait time before merge?**

A: Varies by organization, but ideally "within 24 hours." If waits exceed 48 hours, your workflow has issues. Consider reviewer load-balancing or rule improvements.

**Q: How do I cancel a PR if priorities change?**

A: Use the "Close" button to close the PR. Noting "why it was canceled" in comments helps future reference.
