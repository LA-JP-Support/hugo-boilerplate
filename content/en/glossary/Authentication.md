---
title: Authentication
date: 2026-04-02
lastmod: 2026-04-02
translationKey: authentication
description: A security process verifying users or devices are truly who they claim to be. Multiple methods include passwords, biometrics, and multi-factor authentication.
keywords:
- authentication
- identity verification
- multi-factor authentication
- biometric authentication
- access control
category: Security & Compliance
type: glossary
draft: false
url: /en/glossary/authentication/
---

## What is Authentication?

**Authentication is a security process confirming whether a user or device is truly that person.** It answers the question "who are you?" with definitive proof. This is the first defense line before system access, ensuring only legitimate users reach sensitive information and services. Unlike authorization, authentication only asks "are you who you claim?" not "what can you do?"

> **In a nutshell:** Like bank card authentication. Through multiple methods—password (knowledge), IC card (possession), fingerprint (biometrics)—you prove "you are really you."

**Key points:**

- **What it does:** Confirm users are who they claim through multiple verification factors
- **Why it's needed:** Prevent unauthorized access and protect system-user trust
- **Who uses it:** IT administrators, security managers, developers

## Why it matters

Weak authentication lets attackers take over multiple accounts with a single password. Financial institutions face embezzlement, healthcare faces patient data leaks, enterprises face intellectual property theft. Strong authentication dramatically reduces these risks.

Data shows enterprises implementing multi-factor authentication (MFA) experience 95% reduction in security incident rates. In other words, strengthening authentication methods is not just technical response—it's a business risk reduction strategy.

## How it works

Authentication has three factors. First, **knowledge**—passwords and security questions only you know. Second, **possession**—security keys and smartphones only you have. Third, **biometrics**—fingerprints and face recognition only you possess.

Combining these factors enables multi-layered defense. For bank online transactions, both password (knowledge) and one-time codes sent to your smartphone (possession) are required. Just stealing passwords won't gain access.

Concretely: User enters an ID. The system retrieves authentication info linked to that ID from its database and compares against what the user provided. Match means session start, and subsequent requests require continuous authentication verification.

## Real-world use cases

**Corporate system login**
Employees accessing email or file servers use password + employee ID card. Instant authentication invalidation upon termination prevents unauthorized access.

**Financial transactions**
Bank ATMs and online banking use cash card (possession) and PIN (knowledge), sometimes adding biometrics for extremely strict authentication.

**Cloud service access**
Google detects suspicious logins and requests recovery email codes or registered smartphone confirmation, multi-part verification.

## Benefits and considerations

Strong authentication's biggest benefit is complete unauthorized access prevention. Encrypted data becomes meaningless without authentication breakthrough. Audit logs recording successes and failures enable tracking "who accessed when."

However, strict authentication creates usability challenges. Mandatory multi-factor means users take multiple steps every time. Overly strict authentication prompts users to bypass security. Passwords are naturally weak because humans choose easy ones. Biometrics require expensive hardware, requiring cost-benefit consideration.

## Related terms

- **Multi-Factor Authentication (MFA)** — Authentication combining password alternatives
- **Passwordless Authentication** — Authentication methods not relying on passwords
- **Session Management** — Maintaining and managing user access post-authentication
- **Encryption** — Security technology protecting data alongside authentication
- **Audit Log** — Recording all access and authentication attempts

## Frequently asked questions

**Q: Which is safer—password or biometrics?**
A: Biometrics are generally safer. Passwords are vulnerable to eavesdropping and dictionary attacks. Stealing biometrics is physically difficult and nearly impossible to copy. However, breached biometrics can't be changed (no new fingerprints grow), so combining both is ideal.

**Q: How many failed attempts before account lock?**
A: Typically 3-5 failures trigger temporary lock. This prevents brute-force attacks (trying all combinations). Some organizations permanently lock requiring admin intervention.

**Q: What's the difference between authentication and authorization?**
A: Authentication asks "are you really person A?" Authorization asks "what can person A do?" Even after authentication success, if person A lacks permission to view financial data, authorization blocks access. Authentication is like a security camera; authorization is like a door lock.
