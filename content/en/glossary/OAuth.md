---
title: OAuth
date: 2025-12-19
lastmod: 2026-04-02
translationKey: oauth
description: OAuth is an open standard authorization framework enabling third-party applications to access protected resources without users sharing passwords.
keywords:
- oauth
- authorization framework
- api security
- access token
- authentication protocol
category: Cloud & Infrastructure
type: glossary
draft: false
url: /en/glossary/OAuth/
---

## What is OAuth?

**OAuth is an open standard enabling users to safely delegate access to protected resources to third-party applications without sharing passwords.** For example, it's used when logging into other apps with Google accounts.

> **In a nutshell:** Instead of sharing your Google password with an app, you give it a temporary authorization token saying "this app can access my Google Photos."

**Key points:**

- **What it does:** A framework enabling applications to access resources while protecting user credentials
- **Why it matters:** Reduces password theft risk, enables fine-grained access control, improves user confidence
- **Who uses it:** Large platforms, companies publishing APIs, security-conscious developers

## Why it matters

Historically, to use Service A, you'd share Service B's password (like Facebook) directly with A. This was dangerously risky. Knowing passwords let applications perform any action (delete photos, change settings).

OAuth takes a different approach. Users log directly into authorization servers (Facebook, Google) and explicitly approve: "give this app this permission." Then only temporary tokens are passed to the app. Tokens have limited permissions and expire, enabling both security and convenience.

## How it works

OAuth flow has multiple steps. When users click "connect with Google" on a photo printing service, the browser navigates to Google's authorization server. Users log into their Google account and consent: "let this printing service access my photos."

Google issues an authorization code (temporary pass) returned to the printing service. The service uses this code to call Google's API and get an access token (real permission). Then it can access the user's Google Photos.

If users later want to revoke access, they simply delete the app from Google's settings, immediately invalidating the token.

## Real-world use cases

**Social login** — Log into other sites using Facebook or Google accounts.

**API permission management** — Slack bots get only the permissions needed to read Slack workspace messages.

**Mobile app authentication** — iPhones use OS-managed OAuth when apps access contact data securely.

**Microservice communication** — Multiple services use OAuth tokens for mutual authentication and permission management.

## Benefits and considerations

**Benefits** — Reduced password theft risk; users control fine-grained permissions per app. App developers reduce authentication implementation burden; users seamlessly log in across apps.

**Considerations** — OAuth implementation is complex—developer mistakes create risks. Malicious apps impersonate trusted ones and deceive users into granting permissions. Improper token management creates security vulnerabilities.

## Related terms

- **[API](API.md)** — OAuth enables secure API access control.
- **[Authentication](Authentication.md)** — User identity verification is OAuth's foundation.
- **[Token](Token.md)** — OAuth's temporary access permission.
- **[JWT](JWT.md)** — One standard token format.
- **[OIDC](OpenID-Connect.md)** — An authentication framework extending OAuth.

## Frequently asked questions

**Q: What's the difference between OAuth and traditional password authentication?**
A: Traditional approaches share passwords directly, granting full permissions. OAuth passes limited-permission, time-limited tokens.

**Q: What happens if an OAuth token is stolen?**
A: Stolen tokens have limited permissions and expiration dates, minimizing damage. Even if unnoticed long-term, tokens eventually expire.

**Q: Does every app support OAuth?**
A: Many apps support it, but not all. Security-focused services tend to implement it more.
