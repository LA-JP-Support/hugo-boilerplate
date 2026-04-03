---
title: Git
date: 2026-02-08
lastmod: 2026-04-02
translationKey: Git
description: A distributed version control system enabling developers to track code changes, collaborate on projects, and manage multiple branches. The foundation of modern software development workflows.
keywords:
- Git
- version control
- distributed version control
- source code management
- branch management
category: Knowledge & Collaboration
type: glossary
draft: false
url: /en/glossary/git/
---

## What is Git?

**Git is a distributed version control system that tracks changes to code files, enabling developers to collaborate, maintain complete project history, and manage parallel development branches.** Unlike centralized systems requiring constant server connection, Git stores complete repository copies locally, enabling offline work and redundant backups. From solo projects to massive open-source efforts, Git has become the de facto industry standard.

> **In a nutshell:** A system that tracks every code change, who made it, and when—enabling collaboration without overwriting each other's work.

**Key points:**

- **What it does:** Tracks code changes, enables branching, and manages collaboration
- **Why it matters:** Prevents code loss, enables team collaboration, maintains complete project history
- **Who uses it:** All software developers, DevOps teams, technical documentation projects

## Why it matters

Early software development lacked systematic change tracking. Developers overwrote each other's work, revisions were lost, and undoing changes was impossible. Git solved these fundamental problems through distributed, immutable history.

Git's design enables sophisticated workflows: developers work independently on branches, collaborate through pull requests, maintain production and development versions simultaneously, and instantly revert problematic changes. This flexibility scales from individual developers to organizations coordinating thousands of contributors across repositories.

For modern development, Git is non-negotiable—job listings assume Git proficiency, deployment systems integrate with Git workflows, and code review processes depend on Git's capabilities.

## How it works

**Repositories and Commits**
Developers create local repositories containing complete project history. Each commit represents a snapshot of all files at a point in time, with metadata identifying the author, timestamp, and description. Commits link to previous commits, forming an immutable chain of changes.

**Branching**
Developers create branches for features, bug fixes, or experiments. Branches diverge from existing commits, enabling parallel development without affecting the main codebase. Merging branches combines changes back together.

**Distributed Architecture**
Unlike centralized systems with a single server, Git gives every developer a complete repository copy. This provides redundancy, enables offline work, and distributes load—no single failure point.

**Staging and Committing**
The staging area selects specific changes to include in the next commit. This flexibility enables logical, focused commits grouping related changes rather than committing all modifications indiscriminately.

## Real-world use cases

**Open-Source Collaboration**
Thousands of developers contribute to projects like Linux or React. Git enables reviewing changes before acceptance, managing contributions from strangers, and maintaining code quality.

**Team Development**
Multiple developers work on features simultaneously without collisions. Pull requests enforce code review, automated tests verify quality, and history maintains complete accountability.

**Continuous Integration/Deployment**
Deployment systems monitor Git repositories and automatically build, test, and deploy when changes appear, enabling rapid iteration and quality assurance.

## Benefits and considerations

Git's primary advantages include **distributed redundancy** (every developer has complete history), **offline capability**, **flexible branching for complex workflows**, and **immutable history**. Merging changes from multiple developers is more sophisticated than simpler tools.

Challenges include learning curve—Git's flexibility and distributed nature confuse newcomers. Merge conflicts require manual resolution when branches modify the same code. Large binary files (videos, datasets) are problematic, as Git stores complete history including large file changes. Repository cleanup requires careful operations to avoid data loss.

## Related terms

- **[GitHub](GitHub-Copilot.md)** — The most popular Git hosting platform
- **[Branch Management](GitHub-Actions.md)** — Core Git functionality
- **[Pull Requests](GitHub-Pages.md)** — GitHub's collaboration model based on Git
- **[Merge Conflict](Generative-AI.md)** — Common Git challenge
- **[Git Workflow](Git-Based-CMS.md)** — Patterns for using Git

## Frequently asked questions

**Q: Is Git only for software development?**
A: No. Documentation, configuration files, research papers, and any text-heavy projects benefit from version control. Some people version control theses or books.

**Q: Can Git handle large binary files efficiently?**
A: Not well. Git wasn't designed for binary files. Git LFS (Large File Storage) is a workaround but adds complexity. For large binaries, consider dedicated systems.

**Q: What happens if I delete a commit?**
A: Deleted commits remain in Git history (reflog) for 30 days before garbage collection. Accidental deletions are usually recoverable. Force-pushing is dangerous but rarely permanent.

**Q: Is Git secure?**
A: Git uses SHA-1 hashing to verify integrity and detect corruption. Modern Git mitigates SHA-1 weaknesses. Hosting platforms (GitHub, GitLab) provide additional security features and access control.