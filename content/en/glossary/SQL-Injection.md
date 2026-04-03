---
title: SQL Injection
date: 2026-01-29
lastmod: 2026-04-02
translationKey: SQL-Injection
description: A cyberattack where attackers input malicious code into web forms to illegally manipulate databases. One of the most dangerous cyberattacks.
keywords:
- SQL Injection
- Database security
- Web application attacks
- Security vulnerability
- Input validation
category: Security & Compliance
type: glossary
draft: false
url: /en/glossary/SQL-Injection/
---

## What is SQL Injection?

**SQL Injection is a cyberattack where attackers input malicious code into web forms to illegally manipulate company databases.** If user input is directly used in database operations without checking, attackers can insert bad code to steal or modify unauthorized information. Security organization OWASP ranks it among "Most Dangerous Security Threats" constantly—extremely serious.

> **In a nutshell:** Hackers put bad code in web forms to secretly steal or damage database information.

**Key points:**

- **What it is:** Cyberattack illegally manipulating databases
- **Why it's dangerous:** User passwords, credit cards, personal info can be stolen
- **Who's targeted:** Websites and apps with weak input checking

## Why it matters

Most websites store user and product info in databases, using user input for search and registration. If bad code executes due to unchecked input, attackers can bypass login screens to become administrators, steal entire customer databases, or modify data. Finance, healthcare, e-commerce suffering attacks means massive customer impact. Reputation damage from breaches, GDPR violation fines (max 2 billion euros), directly threaten business survival. Security breaches are corporate existential risks.

## How it works

Consider an e-commerce login form. Normally, username "tanaka" and password "12345" create database query: "SELECT * FROM users WHERE username='tanaka' AND password='12345'"—finding matching users.

Attackers target this. They enter username "admin' --" (double dash). Now the query becomes: "SELECT * FROM users WHERE username='admin'--' AND password='12345'". Double-dash makes everything after it comments (ignored by programs), so only "SELECT * FROM users WHERE username='admin'" executes. Password check disappears—attackers become administrators!

More dangerous: "' UNION SELECT password FROM users--" extracts all user passwords. Attackers exploit the security gap—the program's false belief that "user input = safe data"—and execute bad commands.

## Real-world examples

**Major breach incidents**
2011, a famous social media site suffered SQL injection, stealing over 6 million personal records. Stolen passwords later sold on dark web, causing impersonation damages.

**Financial institution harm**
Bank online banking systems infiltrated by SQL injection, enabling illegal account transfers. Customer funds flowed out without their notice in some cases.

**Healthcare patient leak**
Hospital systems breached via SQL injection, stealing patient medical history, medications, personal identifiers. Medical info trades high on dark markets—especially targeted.

## Defense and notes

**Note:** SQL injection is pure attack with no benefits—only defense perspective matters. Defense merits: proper input validation prevents attacks, database access minimization limits damage.

**Defense points:** Developers must never directly include user input in SQL commands. Use "parameterized queries"—treating user input as data, not executable commands. Validate all input (numbers only get numbers, emails only get email format), rejecting unexpected input.

## Related terms

- **[Cybersecurity](Cybersecurity.md)** — Technology protecting computers and networks from attacks
- **[Input Validation](Input-Validation.md)** — Checking if user input is safe
- **[Database Security](Database-Security.md)** — Protecting databases from attacks
- **[Web Application Firewall](WAF.md)** — Auto-detect and block SQL injection attacks
- **[Encryption](Encryption.md)** — Technology protecting important data

## Frequently asked questions

**Q: Can all companies suffer SQL injection?**
A: Any website or app with weak input checking can. Large companies with weak security still get targeted. Modern languages and frameworks standardize safe methods, so proper development prevents it.

**Q: Can you detect after SQL injection happens?**
A: Usually hard. Attackers can secretly steal information, undetected for months. Security log monitoring and system audits are therefore critical.

**Q: Does complex passwords prevent SQL injection?**
A: No. SQL injection is system design problem, unrelated to password strength. Strong passwords defend other attacks (brute force), but not SQL injection. Design security is what matters.
