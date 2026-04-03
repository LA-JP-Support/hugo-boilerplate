---
title: Single Sign-On (SSO)
date: 2025-12-19
lastmod: 2026-04-02
translationKey: Single-Sign-On--SSO-
description: Login once to access multiple apps. One password for all your work tools.
keywords:
- Single Sign-On
- SSO Authentication
- Identity Management
- SAML Protocol
- OAuth
category: Security & Compliance
type: glossary
draft: false
url: /en/glossary/single-sign-on--sso-/
---

## What is Single Sign-On (SSO)?

**SSO lets you access multiple apps with one login.** Before, Gmail login, Drive login, Sheets login, etc. With SSO, one Google login gives you access to all Google services.

> **In a nutshell:** One theme park ticket gets you on all rides.

**Key points:**

- **What it does:** One login unifies access to multiple systems
- **Why you need it:** Reduce password management burden and improve security
- **Who uses it:** Enterprises using multiple SaaS tools or companies with many internal systems

## Why it matters

Employees using 10+ systems must remember 10+ passwords. This leads to weak passwords, reuse, sticky notes—major security risks. SSO means one strong password for everything.

For companies, one change grants/revokes all system access. Onboarding and offboarding become easier. Help desk password reset requests drop dramatically, reducing IT costs.

## How it works

Employee tries to access System A. SSO server (identity provider) checks: "Are you logged in?" If no, asks for password. If yes, gives a token saying "this employee is verified."

System B request? Employee presents the token. Verified—access granted. No extra password needed. Token expires at logout or timeout.

Standards like SAML and OAuth 2.0 handle this securely.

## Real-world use cases

**Large IT company**
Dozens of tools unified. Morning login gives access to chat, email, documents, pay systems—all day.

**SaaS for enterprises**
Slack, Notion, etc. provide SSO connecting to company's own directory (Active Directory, Okta).

**Universities**
Students/staff one login: learning management, library, email, grades.

**Healthcare**
Doctors one login: medical records, tests, appointments. HIPAA compliance too.

## Benefits and considerations

**Benefits:** One strong password. Simple password management. IT manages centrally. Help desk ticket volume drops.

**Considerations:** If SSO server goes down, you can't access anything. Complex setup especially for older systems. Some third-party SaaS might not support it.

## Related terms

- **[Authentication](Authentication.md)** — SSO is authentication technology
- **[Identity Management](Identity-Management.md)** — SSO's key function
- **[Multi-Factor Authentication (MFA)](Multi-Factor-Authentication--MFA-/)** — Combine with SSO for more security
- **[OAuth 2.0](OAuth-2.0.md)** — One SSO protocol standard
- **[Access Control](Access-Control.md)** — Unified permission management via SSO

## Frequently asked questions

**Q: How do we start SSO in our company?**
A: First, inventory current apps and check SSO compatibility. Then choose an SSO solution (Okta, Azure AD, etc.).

**Q: Does SSO work in cloud?**
A: Yes, especially SaaS. Cloud-based SSO (Okta, Azure AD) is standard now.

**Q: Does SSO really improve security?**
A: Yes. One strong password beats reused weak passwords across systems. Session management centralizes too.
