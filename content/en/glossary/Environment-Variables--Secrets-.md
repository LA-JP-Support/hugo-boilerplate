---
title: "Environment Variables (Secrets)"
date: 2025-12-19
lastmod: 2026-04-02
description: "A mechanism for securely storing sensitive data such as API keys and passwords outside of code, enabling safe management across different environments."
translationKey: "environment-variables-secrets"
category: "Cloud & Infrastructure"
type: glossary
draft: false
url: /en/glossary/Environment-Variables--Secrets-/
---

## What are Environment Variables (Secrets)?

**Environment variables are configuration values passed to applications at runtime rather than written directly into code. When used for secrets, API keys, passwords, and database authentication credentials are stored outside the code.** Instead of writing `API_KEY = "abc123"` directly in code, the application references the environment variable `API_KEY`.

> **In a nutshell:** Instead of attaching your house key to the front door, you keep it in a separate secure location and only people who need it can retrieve it—a management method applied to code.

**Key points:**

- **What it does:** Stores API keys and passwords outside code, managing them safely
- **Why it's needed:** Prevents accidentally uploading secrets to GitHub
- **Who uses it:** All developers, especially those working with cloud/infrastructure

## Why it matters

Developers sometimes accidentally include API keys in code and commit them to GitHub. When hackers discover these keys, they can misuse them—stealing data or running up charges by using the service. Using environment variables keeps secrets out of code, making it safe.

Additionally, different API keys are needed for development, testing, and production environments. With environment variables, the same code automatically uses different keys for each environment.

## How it works

Using environment variables takes three steps.

**Step 1: Store value in configuration file or system**
In local development, write `OPENAI_API_KEY=sk-abc123` in a `.env` file. In production, use specialized tools like AWS Secrets Manager or Azure Key Vault.

**Step 2: Reference from code**
In Node.js, reference with `process.env.OPENAI_API_KEY`; in Python use `os.getenv('OPENAI_API_KEY')`.

**Step 3: Auto-inject at application startup**
Environment variables are loaded when the application starts and passed to the code.

## Real-world use cases

**API integration** — Store API keys for OpenAI, Stripe, Google Cloud in environment variables.

**Database connection** — Manage username, password, host in environment variables rather than in code.

**Feature flags** — Control thresholds for enabling/disabling specific features with environment variables.

## Benefits and considerations

**Improved security is the greatest benefit** — Secrets aren't included in the codebase, greatly reducing leakage risk.

**Easy environment-specific configuration** — Same code works across multiple environments.

**However, `.env` files must also be managed securely** — If `.env` files aren't added to `.gitignore` locally, they're still exposed.

**Weakness with complex structures** — Not well-suited for hierarchical configuration; configuration files (YAML, JSON) may be better.

## Related terms

- **[Secrets Management](Secrets-Management.md)** — An extended concept of environment variables with features like auto-rotation
- **[Cloud Security](Cloud-Security.md)** — Secrets management is an important cloud security measure
- **[CI/CD Pipeline](CI-CD.md)** — Environment variables are auto-injected during deployment
- **[API Key](API-Key.md)** — A typical secret managed with environment variables
- **[YAML Configuration](YAML.md)** — Format used for complex configuration management

## Frequently asked questions

**Q: Can `.env` files be committed to Git in local development?**

A: No, absolutely not. Always add to `.gitignore` to avoid commits. Create a template `.env.example` file for team members to fill in.

**Q: How are environment variables managed in production?**

A: Use enterprise tools like AWS Secrets Manager, Azure Key Vault, or HashiCorp Vault with encryption, audit logging, and auto-rotation.

**Q: When do environment variable values change?**

A: They're loaded at application startup, so changes made after startup aren't reflected. Restart the application to use new values.
