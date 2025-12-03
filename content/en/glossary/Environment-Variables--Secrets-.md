---
title: "Environment Variables (Secrets): The Deep Glossary"
translationKey: "environment-variables-secrets-the-deep-glossary"
description: "Learn about environment variables (secrets) for secure application configuration. Decouple sensitive data like API keys and passwords from code, ensuring security and flexibility."
keywords: ["environment variables", "secrets management", "API keys", "application security", "configuration management"]
category: "General"
type: "glossary"
date: 2025-12-03
draft: false
---
## What Are Environment Variables (Secrets)?

Environment variables are named, externally-defined key-value pairs that provide runtime configuration to applications. When utilized for secrets, they store sensitive data—API keys, passwords, connection strings, tokens—outside codebases, UIs, or logs. The decoupling ensures that secrets are never hardcoded in source code or checked into version control.

- **Analogy:** The value of an environment variable acts as a placeholder in your code. For example, instead of writing `API_KEY = "secret123"`, you reference `API_KEY`, which is only defined at runtime in the execution environment.
- **Security Context:** Storing secrets in environment variables minimizes the risk of accidental exposure through code leaks, Git repository access, or logs. Sensitive values are injected at runtime and not stored in visual interfaces or configuration files unless specifically required.
- **Secret Types:** Database passwords, API tokens, OAuth credentials, cryptographic keys, feature flags, and more.

**See:**  
- [OWASP Secrets Management Cheat Sheet—Intro and General Concepts](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html#1-introduction)  
- [Kinsta: What Is an Environment Variable?](https://kinsta.com/blog/what-is-an-environment-variable/)

## Why Use Environment Variables for Secrets?

**Separation of Code and Configuration:**  
- Keeps sensitive data out of codebases and version control.  
- Enables the same codebase to run in different environments (development, staging, production) with different credentials.

**Security:**  
- Reduces risk of secret leakage by not embedding them in code or public repositories.
- Prevents secrets from being exposed in logs, error messages, or UIs.

**Flexibility and Maintainability:**  
- Secrets can be updated or rotated without code changes.
- Supports rapid response to incidents (e.g., credential leaks) by changing the environment variable and restarting the application.

**Scalability and Consistency:**  
- Manage environment-specific values (dev/staging/prod) centrally.
- Consistent deployment pipelines (CI/CD) that do not require code changes for configuration updates.

**Process Isolation:**  
- Each process has access only to relevant secrets, reducing accidental exposure or privilege escalation.

**References:**  
- [Microsoft Learn: Best practices for protecting secrets](https://learn.microsoft.com/en-us/azure/security/fundamentals/secrets-best-practices)  
- [OWASP: Centralize and Standardize Secrets Management](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html#22-centralize-and-standardize)

## Types of Environment Variables

### 1. System Environment Variables
- Set at the OS level.
- Affect all processes and users on the machine.
- Example: Adding directories to the `PATH` variable on Unix or Windows.

### 2. User Environment Variables
- Scoped to a specific user profile.
- Only processes launched by that user can access these variables.
- Example: Windows allows editing user environment variables via Control Panel.

### 3. Process/Runtime Environment Variables
- Scoped to a specific process or session.
- Set temporarily for a session or when launching a process.

### 4. Build-Time vs. Runtime Secrets
- **Build-Time:** Used during the building/compilation process (e.g., fetching dependencies).
- **Runtime:** Used while the application is running (e.g., connecting to live services).

### 5. Application/Project Level (.env Files, Secret Managers)
- `.env` files store environment variables for local development.
- Secret managers (e.g., AWS Secrets Manager, Azure Key Vault, HashiCorp Vault) provide encrypted storage with audit, access control, and rotation capabilities.

### Platform Differences
- **Windows:** Set via Control Panel, CLI (`set`), or PowerShell (`$env:VAR_NAME`).
- **Unix/Linux/macOS:** Set via `export VAR=value` in shell, or add to `.bashrc`/`.zshrc` for persistence.

**References:**  
- [DreamHost: Environment Variables Explained](https://www.dreamhost.com/blog/environment-variables/)  
- [Kinsta: Environment Variable Types](https://kinsta.com/blog/what-is-an-environment-variable/)

## How Environment Variables Are Used

**Workflow:**
1. Define secrets outside the codebase (OS, `.env` file, secret manager, deployment dashboard).
2. Reference them in application code via environment variable APIs.
3. Deploy the application—secrets are injected at runtime.

**Example:**  
Instead of hardcoding `API_KEY = "abc123"`, set the value as an environment variable and let the application read it securely at runtime.

**Automated Secret Injection:**  
- In CI/CD, secrets are often injected at build or deployment time.
- Secret managers or deployment dashboards provide UIs/APIs for defining and rotating secrets.

**References:**  
- [Render: Configure Environment Variables](https://render.com/docs/configure-environment-variables)  
- [OWASP: Automate Secrets Management](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html#24-automate-secrets-management)

## Common Use Cases & Examples

- **API Keys:** External services (OpenAI, Google Cloud, Stripe).
- **Database Credentials:** Securely pass DB usernames, passwords, hostnames.
- **Secret Tokens:** JWT signing keys, OAuth client secrets, webhook tokens.
- **Feature Flags:** Enable/disable features dynamically.
- **Environment Tags:** Indicate `development`, `staging`, or `production`.

**.env Example:**
```
OPENAI_API_KEY=sk-abc123
DATABASE_URL=postgres://user:pass@host:5432/db
MODE=production
```

**Platform Examples:**
- [Netlify Environment Variables](https://docs.netlify.com/configure-builds/environment-variables/)
- [Vercel Environment Variables](https://vercel.com/docs/concepts/projects/environment-variables)

## Setting and Accessing Environment Variables

### At the OS Level

#### Unix/Linux/macOS

- Set for current session:
  ```sh
  export API_KEY="abc123"
  ```
- Set for a single command:
  ```sh
  API_KEY="abc123" python app.py
  ```
- Persistent for user:
  ```sh
  echo 'export API_KEY="abc123"' >> ~/.bashrc
  source ~/.bashrc
  ```

#### Windows

- Set for current session (Command Prompt):
  ```bat
  set API_KEY=abc123
  ```
- Persistent via GUI:  
  Control Panel → System → Advanced → Environment Variables
- PowerShell:
  ```powershell
  $env:API_KEY="abc123"
  ```

### In Application Code (.env Files, Secret Managers, Platform Dashboards)

#### .env Files

- Place a `.env` file in the project root:
  ```
  API_KEY=abc123
  DB_PASS=supersecret
  ```
- **Security:** Always add `.env` to `.gitignore` to avoid accidental commits to version control.

#### Secret Managers

- **AWS Secrets Manager:** [Official Docs](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html)
- **Azure Key Vault:** [Official Docs](https://learn.microsoft.com/en-us/azure/key-vault/)
- **HashiCorp Vault:** [Official Docs](https://www.vaultproject.io/docs)
- Secrets are encrypted, access-controlled, and auditable.

#### Platform Dashboards

- **Render:** [Configure Environment Variables](https://render.com/docs/configure-environment-variables)
- **Netlify:** [Environment Variables](https://docs.netlify.com/configure-builds/environment-variables/)
- **Vercel:** [Environment Variables](https://vercel.com/docs/concepts/projects/environment-variables)

### Code Examples: Node.js, Python, .NET

#### Node.js

- Access environment variables:
  ```js
  // index.js
  console.log(process.env.API_KEY);
  ```
- With dotenv:
  ```js
  require('dotenv').config();
  const apiKey = process.env.API_KEY;
  ```

#### Python

- Access environment variables:
  ```python
  import os
  api_key = os.environ.get('API_KEY')
  ```
- With python-dotenv:
  ```python
  from dotenv import load_dotenv
  load_dotenv()
  api_key = os.getenv('API_KEY')
  ```

#### .NET (C#)

- Access environment variables:
  ```csharp
  var apiKey = Environment.GetEnvironmentVariable("API_KEY");
  ```
- ASP.NET Core User Secrets:
  1. Initialize secrets:
     ```
     dotnet user-secrets init
     ```
  2. Set secret:
     ```
     dotnet user-secrets set "Movies:ServiceApiKey" "12345"
     ```
  3. Access in code:
     ```csharp
     var builder = WebApplication.CreateBuilder(args);
     var movieApiKey = builder.Configuration["Movies:ServiceApiKey"];
     ```

**References:**  
- [Microsoft Docs: Safe storage of app secrets in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/security/app-secrets?view=aspnetcore-10.0)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
- [npm dotenv](https://www.npmjs.com/package/dotenv)

## Managing & Rotating Secrets

**Secret Lifecycle:**
- **Set Multiple Secrets:** Batch via `.env` files, platform dashboards, or secret manager APIs.
- **List Secrets:** CLI tools (e.g., `dotnet user-secrets list`), dashboards, APIs.
- **Update/Rotate:** Change values in secret managers, `.env` files, or dashboards; redeploy/restart apps if required.
- **Remove/Expire:** Delete or revoke secrets when no longer needed. Expired secrets should be purged.

**Automated Rotation:**
- Use dynamic secrets (where possible) that expire after use or session, e.g., temporary DB credentials via Vault.
- Configure scheduled rotation in secret managers (e.g., AWS, Azure, HashiCorp Vault).
- Ensure application code supports hot-reload or graceful re-authentication on secret changes.

**Mapping to Configuration Objects:**
- .NET: Map secrets to POCOs for structured access.
- Node.js/Python: Use config libraries or custom wrappers for validation and aggregation.

**References:**  
- [OWASP: Automated Secrets Rotation](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html#24-automate-secrets-management)
- [Azure Key Vault: Secret Rotation](https://learn.microsoft.com/en-us/azure/key-vault/secrets/tutorial-rotation)

## Security Best Practices

- **Never store secrets in version control.**
- **Add `.env` and similar files to `.gitignore`.**
- **Use secret managers for production, not plaintext files.**
- **Principle of Least Privilege:** Restrict access to only those who need it.
- **Rotate and revoke secrets regularly.**
- **Audit and log all secret access.**
- **Never expose runtime secrets to client-side code (e.g., browser JavaScript).**
- **Automate secret scanning in CI/CD pipelines:**
    - [GitHub Secret Scanning](https://docs.github.com/en/code-security/secret-security/about-secret-scanning)
    - [Azure DevOps Credential Scanner](https://learn.microsoft.com/en-us/azure/devops/repos/security/github-advanced-security-secret-scanning)

- **Encrypt secrets at rest and in transit.**
- **Isolate secrets by environment and service.**
- **Minimize human interaction with secrets—use automated pipelines.**

**References:**  
- [OWASP: Access Control & Automation](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html#23-access-control)
- [Microsoft Learn: Best practices for protecting secrets](https://learn.microsoft.com/en-us/azure/security/fundamentals/secrets-best-practices)

## Advanced Scenarios: Multiple Environments, Secret Files, Environment Groups

- **Multiple Environments:** Use separate `.env` files or secret sets for `development`, `staging`, and `production`.
- **Secret Files:** Upload secret files (e.g., private keys) via platform dashboards (e.g., Render, Vercel).
- **Environment Groups:** Group variables for microservices or multi-app deployments.
- **Centralized Configuration:** Use environment groups or secret managers to share secrets across teams/services.

**Architectural Patterns:**
- **Kubernetes Sidecar:** Use a sidecar container (e.g., Vault Agent) to fetch secrets and mount into main container ([OWASP Example](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html#example-1-kubernetes-with-a-sidecar-container)).
- **Dynamic Secrets:** Applications request secrets at startup and receive temporary, auto-expiring credentials.

## Limitations and Alternatives

**Limitations:**
- **Plaintext Storage:** `.env` files and OS-level variables are unencrypted on disk.
- **Complex Configs:** Structuring nested or large configs in env variables is difficult.
- **Manual Sync:** Distributing secrets across teams/environments can be error-prone without a central manager.

**Alternatives:**
- **Secret Managers:** AWS Secrets Manager, Azure Key Vault, HashiCorp Vault.
- **Encrypted Configuration Files:** For complex configs (must be excluded from version control).
- **Platform Tools:** Use deployment dashboards (Render, Vercel, Netlify) for managing and grouping secrets.

**References:**  
- [Azure Key Vault Overview](https://learn.microsoft.com/en-us/azure/key-vault/general/overview)
- [HashiCorp Vault Overview](https://www.vaultproject.io/docs)

## Key Takeaways

- Environment variables securely inject sensitive values into apps without exposing them in code or UIs.
- They separate configuration from code, supporting secure and flexible deployments.
- Use `.env` files for local dev (with strict `.gitignore`); use secret managers or platform dashboards for production.
- Rotate and audit secrets; never log or expose them in client-side code.
- Manage secrets per environment and team for isolation.
- Never commit secrets to source control; use access controls and encryption for production.

## References & Further Reading

- [OWASP: Secrets Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html)
- [Microsoft Learn: Best practices for protecting secrets](https://learn.microsoft.com/en-us/azure/security/fundamentals/secrets-best-practices)
- [Microsoft Docs: Safe storage of app secrets in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/security/app-secrets?view=aspnetcore-10.0)
- [Kinsta: What Is an Environment Variable?](https://kinsta.com/blog/what-is-an-environment-variable/)
- [DreamHost: Environment Variables Explained](https://www.dreamhost.com/blog/environment-variables/)
- [Render Docs: Environment Variables and Secrets](https://render.com/docs/configure-environment-variables)
- [Stack Overflow: How to store and access API keys and passwords with Gatsby?](https://stackoverflow.com/questions/62231572/how-to-store-and-access-api-keys-and-passwords-with-gatsby)
- [HashiCorp Vault Documentation](https://www.vaultproject.io/docs)
- [GitHub Secret Scanning](https://docs.github.com/en/code-security/secret-security/about-secret-scanning)

## Example Scenario: AI Chatbot in Production

Suppose you have an AI chatbot requiring an external LLM API key. Instead of embedding the API key in your codebase, you:
1. Store the API key in your platform’s environment variable dashboard or secret manager.
2. Application reads `OPENAI_API_KEY` from the environment at runtime.
3. The key is never exposed to users, code, or logs.
4. To rotate, update it in the dashboard/secret manager and redeploy—no code changes.

**Sample Node.js:**
```js
require('dotenv').config();
const openai = require('openai');
openai.apiKey = process.env.OPENAI_API_KEY;
```
**Sample Python:**
```python
import os
from openai import OpenAI

api_key = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=api_key)
```
**Sample .NET:**
```csharp
var builder = WebApplication.CreateBuilder(args);
var openAiApiKey = builder.Configuration["OPENAI_API_KEY"];
```

**See Also:**  
- [Safe storage of app secrets in ASP.NET Core – Microsoft Docs](https://learn.microsoft.com/en-us/aspnet/core/security/app-secrets?view=aspnetcore-10.0)
- [How to store and access

