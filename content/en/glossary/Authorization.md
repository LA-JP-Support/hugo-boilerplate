---
title: Authorization
date: 2026-04-02
lastmod: 2026-04-02
translationKey: authorization
description: After authentication, the permission management process determining what users can do and which resources they can access.
keywords:
- authorization
- access control
- RBAC
- permission management
- security
category: Security & Compliance
type: glossary
draft: false
url: /en/glossary/authorization/
---

## What is Authorization?

**Authorization is the process determining what authenticated users can actually do—which data they can access and what operations they can perform.** Where authentication asks "who are you?", authorization asks "what can you do?" Following the principle of least privilege, only absolutely necessary permissions should be granted.

> **In a nutshell:** A police officer undergoes identity verification (authentication), then is authorized to arrest suspects and conduct searches. Non-police cannot be authorized these actions.

**Key points:**

- **What it does:** Control permitted operations based on user permissions
- **Why it's needed:** Prevent unauthorized operations and properly restrict data and feature access
- **Who uses it:** IT administrators, security managers, system architects

## Why it matters

Vague authorization creates impossible permission structures—new employees viewing all customer personal info, contractors accessing annual budgets, system admins approving financial transactions. Most unauthorized access comes from careless mistakes rather than intentional tampering, making system-level enforcement critical.

Real data shows 95%+ of over 1000 unauthorized access attempts at a major corporation involved out-of-authority access. Proper authorization controls prevent most internal threats.

## How it works

Authorization determines permissions through multiple factors. First, check user **role**—sales staff get sales role, accounting staff get accounting role, etc. Organizational position applies permission templates.

Next, consider **attributes** beyond role. Sales staff "focused on East Japan" and "West Japan" access different customer data. "Access only during employment" adds time constraints. This is **attribute-based access control (ABAC)**.

Finally, the policy engine processes all information, determining "this user, at this time, for this resource, which operations are permitted?" If OK, grant access. If NG, deny. Simple flow but complex rule evaluation underlies it.

## Real-world use cases

**Hospital patient information management**
Doctors view their patients' records only, not other departments'. Nurses enter records but cannot change prescriptions—only doctors can. Fine-grained permission control by role and responsibility.

**Financial institution transaction approval**
Managers approve up to ¥1 million, directors ¥10 million, executives ¥100 million. Amount-based permission reflecting risk response.

**SaaS multi-tenant environment**
Customer A's sales director only sees Customer A data, not Customer B's. Same "sales director" role, but organization-isolated permissions.

## Benefits and considerations

Authorization's biggest benefit is protecting organizations from internal threats. Even authorization-lacking people attempting sensitive access get system-blocked. Unauthorized access records audit logs for post-incident investigation.

However, complex authorization rules dramatically increase management burden. Frequent permission-change requests (new department joining projects) risk rule conflicts and gaps. Users blocked from necessary operations see decreased efficiency. Constant authorization strictness vs. usability balance pressure exists.

## Related terms

- **RBAC (Role-Based Access Control)** — Permission-setting based on job roles
- **ABAC (Attribute-Based Access Control)** — Permission control based on multiple user and resource attributes
- **Access Control List (ACL)** — Explicitly listing who can access specific resources
- **Principle of Least Privilege** — Security principle granting only absolutely necessary permissions
- **Audit Log** — Recording all access and permission usage

## Frequently asked questions

**Q: How to choose between RBAC and ABAC?**
A: Simple hierarchy (director > manager > employee) works fine with RBAC. Project-based or complex job structures need ABAC's flexibility. Most use hybrid—RBAC foundation with ABAC covering exceptions.

**Q: Is permission escalation necessary?**
A: Temporary higher permissions for urgent situations (absent administrator) work if pre-approved. But needing escalation repeatedly signals original permission design review is needed.

**Q: How to remove excess permissions from employees?**
A: Conduct regular permission audits (access reviews), retaining only current job permissions. Leaving old permissions dangling is common risk. Check during job transfers or regular audits.
