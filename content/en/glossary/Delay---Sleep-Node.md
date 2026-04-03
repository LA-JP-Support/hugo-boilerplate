---
title: Delay / Sleep Node
date: 2025-12-19
lastmod: 2026-04-02
translationKey: delay-sleep-node
description: A workflow automation feature that pauses execution for a specified duration. Used to avoid API rate limits and wait for external processes to complete.
keywords:
- Delay Node
- Sleep Node
- Workflow Automation
- Rate Limiting
- Orchestration
category: Cloud & Infrastructure
type: glossary
draft: false
url: /en/glossary/delay-sleep-node/
---

## What is a Delay / Sleep Node?

**A Delay (or Sleep) Node is a component that pauses workflow execution for a specified period.** Provided as a visual node in workflow automation tools like n8n, Make, and AWS SSM, it suspends processing for a configured number of seconds. In JavaScript, similar functionality is implemented using Promises or async/await.

> **In a nutshell:** Like waiting 15 minutes before calling someone at a restaurant, a Delay Node tells an automation tool to wait a specific number of seconds before proceeding to the next step.

**Key points:**

- **What it does:** Pauses execution within a workflow
- **Why it's needed:** To avoid API rate limits and wait for external systems to complete processing
- **Who uses it:** Workflow designers, automation engineers

## Why it matters

API servers have call limits (rate limiting). Sending too many requests in a short time causes the server to reject additional requests. By inserting delays between requests using a Delay Node, you can avoid hitting these limits.

Additionally, Delay Nodes are used when waiting for time-consuming external processes like file uploads or payment processing to complete. Proceeding without waiting risks passing incomplete data to the next step. By implementing polling (periodic checks) with a Delay Node, you can ensure reliable completion.

## How it works

A Delay Node's operation is straightforward: it pauses processing to the next step for a configured duration. The entire workflow doesn't stop—only that specific flow enters a waiting state.

Typical usage patterns include **fixed delays** and **conditional delays**. Fixed delays mean waiting the same amount of time each time, like "always wait 5 seconds." Conditional delays involve repeating checks at intervals until a condition is met, like "check every minute until status is complete." The latter pattern is called polling and is commonly used when waiting for external API call results.

Multiple Delay Nodes can be combined within a workflow. For example: "Send email → Wait 5 seconds → Call another API → Wait 10 seconds → Final verification."

## Real-world use cases

**Avoiding API rate limits**

An external API has a limit of 10 requests per second. When processing 1,000 records, sending them continuously in 0.1-second intervals hits the limit. By inserting a 500-millisecond delay between requests, you adjust to 2 requests per second—well within the limit.

**Waiting for file uploads**

After uploading a file to cloud storage, wait for a virus scan to complete. Poll (up to 5 times) the scan status API every 30 seconds to reliably retrieve results.

**Adjusting email delivery intervals**

When sending bulk emails to avoid overloading recipient servers, insert a 2-second delay between messages. This ensures reliable delivery and reduces spam risk.

## Benefits and considerations

The main benefit of Delay Nodes is avoiding rate limits without complex error handling. Simply read your API documentation, confirm the limits, set an appropriate delay, and you're done.

However, excessive delays significantly extend overall workflow execution time. Processing 1,000 records with a 2-second delay per record takes 2,000 seconds (over 33 minutes). It's important to confirm beforehand whether the delay is truly necessary. Additionally, if external systems don't respond, the workflow could wait indefinitely, making timeout settings essential.

## Related terms

- **[Workflow Automation](Workflow-Automation.md)** — A Delay Node is a fundamental component of workflow automation tools
- **[API](API.md)** — Delay Nodes are used to handle API rate limiting
- **[Polling](Polling.md)** — A technique combining Delay Nodes with periodic checks of external system status
- **[Asynchronous Processing](Asynchronous-Processing.md)** — Delay implementation in JavaScript uses asynchronous patterns
- **[Timeout](Timeout.md)** — Works alongside Delay Nodes to prevent infinite waiting

## Frequently asked questions

**Q: How long should I set a Delay Node?**

A: If an API states "60 requests per minute," a 1-second delay works (1 request + 1 second delay = approximately 60 requests/minute). For large volumes, test in a staging environment to find the minimum delay that avoids errors.

**Q: Will polling continue waiting indefinitely?**

A: Yes, it can. That's why setting limits like "check up to 5 times, every 1 minute" is important. Unlimited polling can cause workflows to stop indefinitely.

**Q: Can multiple Delay Nodes run in parallel?**

A: Yes. Using parallel execution tools (like n8n's split node) lets you process multiple flows simultaneously, reducing total time. However, watch for total API request limits.
