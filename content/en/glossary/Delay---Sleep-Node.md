---
title: Delay / Sleep Node
translationKey: delay-sleep-node
description: "A workflow component that pauses execution for a set time or until a condition is met, commonly used to space out API requests and prevent system overload."
keywords:
- Delay Node
- Sleep Node
- Automation Workflows
- AI Chatbot
- Workflow Orchestration
category: AI Chatbot & Automation
type: glossary
date: 2025-12-18
lastmod: 2025-12-18
draft: false
---

## What Is a Delay / Sleep Node?

A Delay or Sleep Node is a component that introduces a pause in execution for a configurable period or until a condition is fulfilled. In code (JavaScript/Node.js), it's implemented as a function (`sleep`, `delay`, etc.) that suspends further execution in a non-blocking way, typically using Promises and async/await. In workflow automation tools (n8n, Make, AWS SSM, Cognigy, Jira), it's a visual node/block that can be configured for a specific time or event.

<strong>Why pause execution?</strong>To space out API calls and prevent rate limiting, wait for external processes (e.g., file upload, payment confirmation), orchestrate workflows with time-based or event-based conditions, simulate slow operations or network latency in testing, implement retries with exponential backoff, and allow time for data synchronization before continuing.

## Purpose and Use Cases

### When and Why Delay/Sleep Nodes Are Used

<strong>API Rate Limiting:</strong>Prevent exceeding quotas by spacing requests.  
<strong>Workflow Orchestration:</strong>Ensure steps occur in a specific order with controlled intervals.  
<strong>Polling/Condition Waits:</strong>Pause until an external event or condition is met.  
<strong>Testing & Simulation:</strong>Simulate slow operations or network latency.  
<strong>Retry & Backoff:</strong>Implement retries with exponential backoff.  
<strong>Buffer for External Systems:</strong>Allow time for data sync before continuing.

<strong>Examples:</strong>- Waiting several seconds between notification emails
- Pausing until a file upload is confirmed
- Polling an API every minute until status is "complete"

## How Delay / Sleep Is Implemented

### JavaScript & Node.js

JavaScript and Node.js are single-threaded, non-blocking environments. There is no built-in `sleep()` function. The standard pattern is to use asynchronous approaches (Promises, async/await) to insert delays without blocking the event loop.

<strong>Community best practice:</strong>```js
function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}
```

**Modern sleep function:**```js
async function main() {
  console.log('Start');
  await sleep(2000);
  console.log('End after 2 seconds');
}
```

<strong>One-liner:</strong>```js
await new Promise(resolve => setTimeout(resolve, 5000));
```

### Automation Platforms

Workflow tools provide visual Delay/Sleep nodes with configuration options:
- **Duration:**Fixed time (seconds, minutes, hours, ISO 8601)
- **Condition/Event-based:**Wait until a logical condition is true
- **Timeouts:**Prevent indefinite waits
- **Exponential Backoff:**For intelligent polling or retries

## Implementation Techniques in JavaScript/Node.js

### setTimeout with Callbacks

**Pattern:**```js
function sleep(ms, callback) {
  setTimeout(callback, ms);
}
console.log('Start');
sleep(2000, () => console.log('End after 2 seconds'));
```

<strong>Drawback:</strong>Callback hell, difficult to chain sequential operations.

### Promises & async/await

<strong>Modern approach:</strong>```js
function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}
async function main() {
  console.log('Start');
  await sleep(2000);
  console.log('End after 2 seconds');
}
main();
```

**Pros:**Clean, readable, non-blocking, easy to compose.

### Third-Party Packages

**Example (sleep-promise):**```js
const sleep = require('sleep-promise');
await sleep(5000); // Wait for 5 seconds
```

<strong>Pros:</strong>Features like cancellation, timeouts, better cross-platform support.

### Blocking & Synchronous Sleep Methods

<strong>Not recommended for production.</strong>Blocks the entire event loop, degrading all concurrent tasks.

<strong>Example (Node.js, Unix only):</strong>```js
const { execSync } = require('child_process');
function sleep(seconds) {
  execSync(`sleep ${seconds}`);
}
```

### Advanced: AbortController, Timeouts, and Intelligent Polling

**Cancelable sleep:**```js
const sleep = (ms, { signal, timeout } = {}) => {
  return new Promise((resolve, reject) => {
    const timer = setTimeout(resolve, ms);
    if (signal) {
      signal.addEventListener('abort', () => {
        clearTimeout(timer);
        reject(new Error('Sleep aborted'));
      });
    }
    if (timeout) {
      setTimeout(() => reject(new Error('Timeout')), timeout);
    }
  });
};
```

<strong>Intelligent polling (exponential backoff):</strong>```js
let interval = 1000, maxInterval = 30000;
while (!conditionMet) {
  await sleep(interval);
  if (checkCondition()) break;
  interval = Math.min(interval * 2, maxInterval);
}
```

## Delay/Sleep Nodes in Automation Workflows

### AWS SSM (Systems Manager) Automation

**Node:**`aws:sleep`  
**Configuration:**Duration (ISO 8601, e.g., `PT10M`) or Timestamp (e.g., `2020-01-01T01:00:00Z`)  
**Max delay:**7 days (604799 seconds)

**Example:**```yaml
name: sleep
action: aws:sleep
inputs:
  Duration: PT10M
```

### Cognigy

<strong>Node:</strong>Sleep Node  
<strong>Function:</strong>Pauses chatbot flow for a set duration  
<strong>Configuration:</strong>Duration in ms, seconds, etc.

### n8n & Make

<strong>Node:</strong>Delay/Sleep/Wait Node  
<strong>Configuration:</strong>Duration, units, and in some cases, event-based waits

<strong>Best Practices:</strong>- Use Delay/Wait nodes sparingly to conserve execution resources
- For processing arrays with delays, handle each item with a loop and insert a delay between iterations
- Consider parallel execution implications

### Jira Automation

<strong>Component:</strong>Delay / Pause / Wait Step  
<strong>Function:</strong>Inserts a pause to prevent race conditions and sequence automation reliably  
<strong>Configuration:</strong>Duration, or stacking multiple delays for longer waits

<strong>Best Practices:</strong>- Be aware that branches in Jira automation may execute in parallel
- Serializing actions with delays or splitting into separate rules may be necessary

## Best Practices

<strong>1. Always use non-blocking delays</strong>(Promises, async/await, or platform-native delay nodes)  
<strong>2. Avoid synchronous/blocking sleep</strong>in servers or production environments  
<strong>3. Use timeouts</strong>to prevent indefinite waits  
<strong>4. Apply exponential backoff</strong>for polling external systems or retries  
<strong>5. Limit the scope of delays</strong>to only where necessary  
<strong>6. Support cancellation</strong>(e.g., with AbortController in JS, or abort/timeout configs in workflows)  
<strong>7. Avoid excessive delays</strong>to conserve execution resources and avoid hitting quotas  
<strong>8. Distribute delays</strong>in platforms like n8n to avoid bottlenecks and resource contention

## Troubleshooting / FAQ

<strong>Why doesn't Node.js have a built-in sleep() function?</strong>Node.js is designed for asynchronous, non-blocking I/O. Blocking the event loop would degrade all concurrent tasks. Use async/await or Promises.

<strong>My delay node seems to block other flows!</strong>Check for accidental use of blocking sleep (e.g., while loops or execSync in Node.js). In automation platforms, avoid excessive or long delays in shared (single-threaded) environments.

<strong>How do I wait for a condition, not just a fixed time?</strong>Use a polling loop with increasing delays (exponential backoff), or use "wait until" nodes if your platform supports it.

<strong>Can I cancel a delay/sleep operation?</strong>In modern JavaScript, use AbortController. In workflow tools, look for nodes supporting abort/timeout.

## Parameter Table: Delay/Sleep Node (Generalized)

| Parameter | Type | Description | Example Value |
|-----------|------|-------------|---------------|
| <strong>Duration</strong>| Number/String | How long to delay (ms/s/min/h, ISO 8601) | `5000`, `"PT10M"` |
| <strong>Condition</strong>| Function/String | Optional: Wait until condition is met | `status === "done"` |
| <strong>Max Wait</strong>| Number | Maximum time to wait | `60000` (1 minute) |
| <strong>Abort Signal</strong>| Object | For JS: `AbortController.signal` | - |
| <strong>Timeout</strong>| Number | Timeout for polling or waiting | `30000` (30 seconds) |

## Example Use Cases

### Chatbot Flow

<strong>Scenario:</strong>Wait 3 seconds after user input before responding to simulate processing.  
<strong>How:</strong>Place a "Sleep" node (e.g., 3000 ms) in Cognigy or n8n.

### API Rate Limiting

<strong>Scenario:</strong>Integration sends requests with 1 req/sec limit.  
<strong>How:</strong>Use `await sleep(1000)` in Node.js, or a 1-second Delay node in automation.

### Intelligent Polling (Event Wait)

<strong>Scenario:</strong>Wait for payment confirmation, but avoid excessive API calls.  
<strong>How:</strong>Use exponential backoff polling loop:

```js
let delay = 1000, maxDelay = 30000;
while (!(await isConfirmed())) {
  await sleep(delay);
  delay = Math.min(delay * 2, maxDelay);
}
```

## Summary

A Delay/Sleep Node is a fundamental building block for orchestrating time-based and conditional flows in both code and modern workflow automation platforms. The current best practice in JavaScript is to use Promises and async/await for non-blocking, readable code. In automation platforms, delay/wait nodes should be used judiciously—configured to maximize reliability and efficiency, and always with an eye toward resource management and clarity of execution.

## References


1. Stack Overflow. (n.d.). What is the JavaScript version of sleep()?. Stack Overflow.

2. Mimo. (n.d.). JavaScript Sleep Function. Mimo Glossary.

3. Zignuts. (n.d.). Nodejs Sleep Function: Pause for a Period of Time. Zignuts Blog.

4. Index.dev. (n.d.). JavaScript Sleep, Wait & Delay Guide. Index.dev Blog.

5. AWS. (n.d.). SSM Sleep Action. AWS Documentation.

6. Cognigy. (n.d.). Sleep Node. Cognigy Documentation.

7. n8n Community. (n.d.). Delays Between Array Items. n8n Community Forum.

8. n8n Community. (n.d.). Wait Node & Parallel Execution. n8n Community Forum.

9. Jira. (n.d.). Support for delay / pause / wait step. Jira Issue Tracker.

10. Atlassian Community. (n.d.). Can I set a delay in Jira Automation?. Atlassian Community Forum.

11. LinkedIn. (n.d.). Intelligent Delay Node. LinkedIn Post.

12. Real Python. (n.d.). LangChain Chatbot Tutorial. Real Python.
