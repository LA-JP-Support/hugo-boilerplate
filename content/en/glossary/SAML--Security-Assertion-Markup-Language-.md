---
title: SAML (Security Assertion Markup Language)
date: 2025-12-19
lastmod: 2026-04-02
translationKey: SAML--Security-Assertion-Markup-Language-
description: An XML-based authentication and authorization protocol that enables single sign-on (SSO) across different organizations. The enterprise security standard.
keywords:
- SAML authentication
- single sign-on
- federation
- enterprise security
- XML security
category: Security & Compliance
type: glossary
draft: false
url: /en/glossary/SAML--Security-Assertion-Markup-Language-/
---

## What is SAML (Security Assertion Markup Language)?

**SAML is an XML-based authentication protocol that securely enables single sign-on (SSO) across different organizations.** It allows employees to log in once with their company account and access multiple cloud applications (such as Salesforce or Slack). An Identity Provider (IdP—the company's account system) performs user authentication, and Service Providers (SP—each application) verify SAML assertions (digitally signed authentication information), establishing a trust relationship that realizes secure collaboration.

> **In a nutshell:** An electronic identity certificate system that exchanges "you are an employee of this company with this proof" between organizations to consolidate login across multiple systems.

**Key points:**

- **What it does:** Integrate the organization's identity system with multiple cloud apps to enable single sign-on
- **Why it's needed:** Centralize password management while balancing security and convenience
- **Who uses it:** IT departments of large enterprises, security managers at SaaS companies

## Why it matters

Without SAML, employees must create and remember new passwords for each new cloud application (password fatigue). SAML allows employees to access multiple systems with one company account, greatly reducing password management burden. Also, enterprise security policies (multi-factor authentication, strong password rules, etc.) can be applied centrally, improving security. Furthermore, when an employee leaves, simply deleting their account from the company directory automatically revokes access to all cloud services.

## How it works

SAML authentication proceeds through five steps. (1) **User requests access to app** → (2) App (SP) redirects user to company login page (IdP) → (3) User authenticates with company username/password (or multi-factor authentication) → (4) Company system issues a digitally signed "this user is authenticated" SAML assertion and sends it to the app via user's browser → (5) App verifies the assertion and logs in the user.

This entire process uses secure XML format with encryption and digital signatures, minimizing risks of tampering or eavesdropping.

## Scope of application

SAML is primarily adopted in enterprise environments and is used in the following scope:

- **Target organizations** — Companies with 100+ employees, organizations using multiple cloud apps
- **Target apps** — Salesforce, Office 365, Google Workspace, Slack, Jira, Confluence, etc. SAML-supporting SaaS
- **Geographic scope** — No particular restrictions. Enables integration of on-premises and cloud systems
- **Industries** — Finance, healthcare, manufacturing, education, etc., where security requirements are high

## Key requirements

When implementing SAML, organizations must comply with these key requirements:

- **Identity Provider configuration** — Configure employee directory (Active Directory, Okta, Azure AD, etc.) as SAML IdP
- **Metadata exchange** — Exchange SAML metadata (configuration information) between IdP and SP to establish trust
- **Digital signatures and encryption** — Digitally sign SAML assertions and encode before sending
- **Session management** — Manage user session validity periods and terminate all SP-side sessions on logout
- **Attribute mapping** — Map IdP user attributes (department, title, etc.) to SP side

## Violations and consequences

Improper SAML implementation or operational security violations carry these types of risks and impacts:

- **Authentication failure causing business interruption** — Outdated SAML metadata, signature key update mistakes prevent user app access. Thousands of employees' work can stop
- **Unauthorized access** — If SAML assertion signature is invalidated or encryption keys leak, others can impersonate authority and log in
- **Compliance violations** — Regulations like [SOX Act](SOX.md) and [GDPR](GDPR.md) require "proper access control"; non-implementation is viewed as violation, risking fines or correction orders
- **Post-termination access retention** — If an account deleted from IdP remains active on SP, former employees can access confidential data
- **Unauditable state** — Without preserved SAML logs, you cannot track "who accessed what when," making incident investigation impossible

## Real-world use cases

**Global company employee portal**
US headquarters Active Directory serves as central IdP; branch employees worldwide access regional Salesforce, Slack, etc. with unified authentication. One termination at headquarters removes access worldwide.

**University campus system**
Students log in once with university account; automatically access library system, learning management system, email, and other services. Professor additions/deletions auto-reflect via directory update.

**Partner company access sharing**
Healthcare provider and insurance company link patient information-sharing system via SAML. Each company's employees can access the other's systems using their own accounts (trust only between vetted partners).

## Benefits and considerations

SAML's major advantage is **security and convenience together** in enterprise environments. However, implementation is relatively complex, and metadata configuration errors between IdP and SP can cause authentication failures. Also, SAML is not widely supported in mobile apps; OAuth 2.0 or API key authentication may be needed instead.

## Related terms

- **[Single sign-on (SSO)](SSO.md)** — Technology enabling access to multiple systems with one login
- **[OAuth 2.0](OAuth-2.md)** — Authorization protocol for mobile apps. Complements SAML
- **[LDAP](LDAP.md)** — On-premises directory service. Often used as SAML IdP
- **[Multi-factor authentication (MFA)](MFA.md)** — Used with SAML to enhance security
- **[Federation](Federation.md)** — Account linking between independent organizations. Foundational concept for SAML

## Frequently asked questions

**Q: What is SAML an acronym for?**
A: Security Assertion Markup Language. "Security assertion" means "secure authentication information."

**Q: What is the difference between SAML and OAuth 2.0?**
A: SAML is for enterprise (B2B), OAuth 2.0 is mainly for consumers (B2C). Also, SAML handles identity ("who are you") while OAuth 2.0 handles authorization ("what can you do").

**Q: Which apps don't support SAML?**
A: Many mobile apps, social media integration tools, small SaaS. In those cases, use API keys or alternative single sign-on features.
