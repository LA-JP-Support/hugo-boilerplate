---
title: 'Environment Variables (Secrets): The Deep'
translationKey: environment-variables-secrets
description: Learn about environment variables (secrets) for secure application configuration.
  Decouple sensitive data like API keys and passwords from code, ensuring security
  and flexibility.
keywords:
- environment variables
- secrets management
- API keys
- application security
- configuration management
category: General
type: glossary
date: 2025-12-18
lastmod: 2025-12-18
draft: false
---

## What Are Environment Variables (Secrets)?

Environment variables are named key-value pairs defined externally that provide runtime configuration to applications. When used for secrets, they store sensitive data—API keys, passwords, database credentials, tokens—outside source code, preventing accidental exposure through code repositories or logs. This separation ensures secrets never appear in version control, UI displays, or application logs unless explicitly required.

The value of an environment variable acts as a placeholder in code. Instead of writing `API_KEY = "secret123"`, you reference `API_KEY`, which only exists at runtime in the execution environment. This approach minimizes risks of credential leaks through code commits, repository access, or log files. Sensitive values inject at runtime and remain isolated from visual interfaces unless specifically configured otherwise.

Common secret types include database passwords, API tokens, OAuth credentials, cryptographic keys, feature flags, and environment-specific configuration values. Modern applications across all platforms—web, mobile, cloud, IoT—rely on environment variables to maintain security while enabling flexible deployment across development, staging, and production environments.

## Why Use Environment Variables for Secrets?

**Code-Configuration Separation**Keeping sensitive data out of codebases and version control enables the same code to run across different environments with different credentials. Development, staging, and production each use appropriate secrets without code modifications.**Enhanced Security**Secrets embedded in code face constant exposure risk through repository access, code sharing, or accidental commits. Environment variables eliminate this attack vector by keeping secrets external to the codebase. They prevent exposure in error messages, stack traces, and debugging outputs.**Operational Flexibility**Update or rotate secrets without touching code. Change environment variables and restart applications to implement new credentials. This agility supports rapid incident response when credentials leak or require rotation.**Deployment Consistency**CI/CD pipelines inject secrets automatically during deployment, maintaining consistent processes across environments. Teams avoid manual credential management and reduce human error.**Process-Level Isolation**Each application process accesses only relevant secrets, reducing blast radius if one process becomes compromised. Granular access control prevents privilege escalation.

## Types of Environment Variables

**System-Level Variables**Set at operating system level, affecting all processes and users. Examples include `PATH` directories on Unix systems or Windows environment settings.**User-Scoped Variables**Limited to specific user profiles. Only processes launched by that user can access these variables, providing user-level isolation.**Process-Scoped Variables**Exist only for individual processes or sessions. Set temporarily when launching specific processes without affecting the broader system.**Build vs Runtime Secrets**Build-time secrets support compilation and dependency fetching. Runtime secrets enable running application connections to live services and databases.**Application-Level Management**`.env` files store variables for local development. Secret managers (AWS Secrets Manager, Azure Key Vault, HashiCorp Vault) provide encrypted storage with audit trails, access control, and automated rotation for production environments.

## Common Use Cases

**API Integration**External services (OpenAI, Google Cloud, Stripe, payment processors) require API keys passed via environment variables rather than hardcoded.**Database Connectivity**Connection strings with usernames, passwords, and hostnames remain secure and environment-specific.**Authentication Tokens**JWT signing keys, OAuth client secrets, and webhook verification tokens stay protected outside source code.**Feature Management**Feature flags control functionality across environments without code deployments.**Environment Identification**Tags like `development`, `staging`, or `production` guide application behavior appropriately.

## Implementation Approaches

### Local Development with .env Files

Create a `.env` file in project root:

```
OPENAI_API_KEY=sk-abc123
DATABASE_URL=postgres://user:pass@host:5432/db
MODE=production
```

**Critical:**Always add `.env` to `.gitignore` to prevent version control commits.

### Node.js Implementation

```javascript
require('dotenv').config();
const apiKey = process.env.API_KEY;
const dbUrl = process.env.DATABASE_URL;
```

### Python Implementation

```python
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('API_KEY')
db_url = os.getenv('DATABASE_URL')
```

### .NET Implementation

```csharp
var builder = WebApplication.CreateBuilder(args);
var apiKey = builder.Configuration["API_KEY"];

// Using User Secrets for local development
// dotnet user-secrets init
// dotnet user-secrets set "Movies:ServiceApiKey" "12345"
var movieKey = builder.Configuration["Movies:ServiceApiKey"];
```

### Operating System Configuration

**Unix/Linux/macOS**```bash
# Current session
export API_KEY="abc123"

# Single command
API_KEY="abc123" python app.py

# Persistent (add to ~/.bashrc or ~/.zshrc)
echo 'export API_KEY="abc123"' >> ~/.bashrc
source ~/.bashrc
```**Windows**```bat
# Command Prompt
set API_KEY=abc123

# PowerShell
$env:API_KEY="abc123"

# Persistent: Control Panel → System → Advanced → Environment Variables
```

## Secret Management Best Practices

**Never Store Secrets in Version Control**Git repositories maintain complete history. Committed secrets remain accessible even after removal. Use `.gitignore` religiously.**Production Secret Managers**AWS Secrets Manager, Azure Key Vault, and HashiCorp Vault provide encryption, access logging, automated rotation, and compliance features essential for production.**Least Privilege Access**Restrict secret access to minimum necessary personnel and systems. Implement role-based access controls.**Regular Rotation**Rotate secrets on schedules or after incidents. Automate where possible using secret manager capabilities or dynamic secrets that expire automatically.**Comprehensive Audit Logging**Track all secret access for security monitoring and compliance requirements.**Client-Side Isolation**Never expose runtime secrets (database passwords, API keys) to browser JavaScript. Use backend proxies for external service access.**Automated Security Scanning**Implement CI/CD pipeline secret scanning to catch accidental commits before they reach repositories.**Encryption Requirements**Encrypt secrets at rest in storage systems and in transit over networks.**Environment Segmentation**Maintain separate secret sets for development, staging, and production to prevent cross-environment contamination.

## Advanced Patterns

**Multiple Environment Management**Use separate `.env` files (`.env.development`, `.env.production`) or secret manager namespaces for each environment.**Secret File Handling**Platform dashboards (Render, Vercel, Netlify) support uploading entire secret files like private keys or certificates.**Microservices Secret Sharing**Environment groups or secret managers enable sharing configuration across related services while maintaining security boundaries.**Kubernetes Sidecar Pattern**Deploy Vault Agent as sidecar container to fetch and inject secrets into application containers at runtime.**Dynamic Secrets**Applications request temporary credentials from secret managers, receiving auto-expiring access tokens that enhance security through time-limited exposure.

## Security Considerations

**Plaintext Limitations**Local `.env` files and OS-level variables store data unencrypted. Acceptable for development but insufficient for production.**Configuration Complexity**Environment variables struggle with nested or hierarchical configuration. Consider encrypted config files for complex structures.**Distribution Challenges**Manual secret distribution across teams introduces errors and security gaps. Centralized secret managers solve this problem.**Alternative Solutions**For complex configurations requiring structure, use encrypted configuration files (excluded from version control) combined with platform-specific secret management tools.

## Production Architecture Example

Consider an AI chatbot requiring external LLM API access:

1. Store API key in secret manager or platform dashboard
2. Application reads `OPENAI_API_KEY` from environment at startup
3. Key never appears in code, logs, or user interfaces
4. Rotation requires only updating secret manager value and redeploying
5. Different keys for development, staging, and production environments
6. Audit trail tracks all API key access

**Node.js:**```javascript
require('dotenv').config();
const { OpenAI } = require('openai');
const client = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY
});
```**Python:**```python
import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
```**C#:**```csharp
var builder = WebApplication.CreateBuilder(args);
var apiKey = builder.Configuration["OPENAI_API_KEY"];
```

## Key Takeaways

Environment variables provide secure, flexible secret injection into applications without embedding sensitive data in code. They separate configuration from implementation, enabling identical codebases across environments with environment-specific credentials. Local development uses `.env` files with strict `.gitignore` protection. Production deployments leverage secret managers or platform dashboards providing encryption, access control, audit logging, and automated rotation. Regular secret rotation, comprehensive logging, and client-side isolation maintain security posture. Proper implementation prevents credential leaks while enabling rapid deployment and incident response.

## References


1. OWASP. (n.d.). Secrets Management Cheat Sheet. OWASP Cheat Sheets Series.

2. Microsoft. (n.d.). Best Practices for Protecting Secrets. Microsoft Learn.

3. Microsoft. (n.d.). Safe Storage of App Secrets in ASP.NET Core. Microsoft Docs.

4. Kinsta. (n.d.). What Is an Environment Variable?. Kinsta Blog.

5. DreamHost. (n.d.). Environment Variables Explained. DreamHost Blog.

6. Render. (n.d.). Environment Variables and Secrets. Render Documentation.

7. Netlify. (n.d.). Environment Variables. Netlify Documentation.

8. Vercel. (n.d.). Environment Variables. Vercel Documentation.

9. AWS. (n.d.). AWS Secrets Manager Documentation. AWS Documentation.

10. Microsoft. (n.d.). Azure Key Vault Documentation. Azure Documentation.

11. HashiCorp. (n.d.). HashiCorp Vault Documentation. HashiCorp Documentation.

12. GitHub. (n.d.). Secret Scanning. GitHub Documentation.

13. Microsoft. (n.d.). Azure DevOps Credential Scanner. Azure DevOps Documentation.

14. Stack Overflow. (n.d.). Storing API Keys with Gatsby. Stack Overflow.
