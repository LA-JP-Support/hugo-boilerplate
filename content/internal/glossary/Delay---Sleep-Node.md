+++
title = "Delay / Sleep Node"
translationKey = "delay-sleep-node-glossary-technical-guide-for-ai-chatbot-automation-workflows"
description = "A Delay/Sleep Node pauses workflow execution in AI chatbots & automation for a set period or until a condition is met, crucial for API rate limiting & orchestration."
keywords = [
  "Delay Node",
  "Sleep Node",
  "Automation Workflows",
  "AI Chatbot",
  "Workflow Orchestration",
]
category = "AI Chatbot & Automation"
type = "glossary"
date = 2025-12-05
lastmod = 2025-12-05
draft = false
url = "/internal/glossary/Delay---Sleep-Node/"

+++
## What is a Delay / Sleep Node?

A Delay or Sleep Node is a component, often seen in automation platforms or as a function in code, that introduces a pause in execution for a configurable period or until a condition is fulfilled.  
- In code (JavaScript/Node.js), it’s implemented as a function (`sleep`, `delay`, etc.) that suspends further execution in a non-blocking way, e.g., using Promises and async/await.  
- In workflow automation tools (n8n, Make, AWS SSM, Cognigy, Jira), it’s a visual node/block that can be configured for a specific time or event.

**Why pause execution?**- To space out API calls and prevent rate limiting.
- To wait for external processes (e.g., file upload, payment confirmation).
- For orchestrating workflows with time-based or event-based conditions.
## Purpose and Use Cases

**When and why are Delay/Sleep Nodes used?**- **API Rate Limiting:**Prevent exceeding quotas by spacing requests.
- **Workflow Orchestration:**Ensure steps occur in a specific order with controlled intervals.
- **Polling/Condition Waits:**Pause until an external event or condition is met.
- **Testing & Simulation:**Simulate slow operations or network [latency](/en/glossary/latency/).
- **Retry & Backoff:**Implement retries with exponential backoff.
- **Buffer for External Systems:**Allow time for data sync before continuing.

**Examples:**- Waiting several seconds between notification emails.
- Pausing until a file upload is confirmed.
- Polling an API every minute until status is “complete”.

## How Delay / Sleep is Implemented

### JavaScript & Node.js

JavaScript and Node.js are single-threaded, non-blocking environments. There is no built-in `sleep()` function.  
- The standard pattern is to use asynchronous approaches (Promises, async/await) to insert delays without blocking the event loop.  
- Community best practice is to wrap `setTimeout` in a Promise:

```js
function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}
```
- [Stack Overflow: JS sleep best practice](https://stackoverflow.com/questions/951021/what-is-the-javascript-version-of-sleep)  
- [Mimo Glossary: JavaScript Sleep Function](https://mimo.org/glossary/javascript/sleep-function)

### Automation Platforms (n8n, Make, AWS SSM, Cognigy, Jira)

Workflow tools provide visual Delay/Sleep nodes:
- **Duration:**Fixed time (seconds, minutes, hours, ISO 8601).
- **Condition/Event-based:**Wait until a logical condition is true.
- **Timeouts:**Prevent indefinite waits.
- **Exponential Backoff:**For intelligent polling or retries.

## Implementation Techniques in JavaScript/Node.js

### `setTimeout` with Callbacks

**Pattern:**```js
function sleep(ms, callback) {
  setTimeout(callback, ms);
}
console.log('Start');
sleep(2000, () => console.log('End after 2 seconds'));
```
- **Use case:**Simple, single-use delays.
- **Drawback:**Callback hell, difficult to chain sequential operations.

### Promises & `async`/`await`

**Modern sleep function:**```js
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
- **Pros:**Clean, readable, non-blocking, easy to compose.
- **Cons:**Requires use of `async` functions.

**One-liner:**```js
await new Promise(resolve => setTimeout(resolve, 5000));
```
### Third-Party Packages (e.g., `sleep-promise`)

**Example:**```js
const sleep = require('sleep-promise');
await sleep(5000); // Wait for 5 seconds
```
- **Pros:**Features like cancellation, timeouts, better cross-platform support.
- **Cons:**Extra dependency.

### Blocking & Synchronous Sleep Methods

**Not recommended for production.**- Blocks the entire event loop, degrading all concurrent tasks.
- Example (Node.js, Unix only):
```js
const { execSync } = require('child_process');
function sleep(seconds) {
  execSync(`sleep ${seconds}`);
}
```
- **Use case:**Debugging or quick scripts, never in production.

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
- **Use case:**Aborting or timing out long-running waits.

**Intelligent polling (exponential backoff):**```js
let interval = 1000, maxInterval = 30000;
while (!conditionMet) {
  await sleep(interval);
  if (checkCondition()) break;
  interval = Math.min(interval * 2, maxInterval);
}
```
- **Use case:**Waiting for asynchronous external events.
## Delay/Sleep Nodes in Automation Workflows

### AWS SSM (Systems Manager) Automation

- **Node:**`aws:sleep`
- **Configuration:**- `Duration` (ISO 8601, e.g., `PT10M`)
    - `Timestamp` (e.g., `2020-01-01T01:00:00Z`)
- **Max delay:**7 days (604799 seconds)
**Example:**```yaml
name: sleep
action: aws:sleep
inputs:
  Duration: PT10M
```

### Cognigy

- **Node:**Sleep Node
- **Function:**Pauses chatbot flow for a set duration.
- **Configuration:**Duration in ms, seconds, etc.
- **Official Docs:**- [Cognigy Sleep Node](https://docs.cognigy.com//ai/agents/develop/node-reference/logic/sleep)

### n8n & Make

- **Node:**Delay/Sleep/Wait Node
- **Configuration:**Duration, units, and in some cases, event-based waits.
- **Best Practices:**- Use Delay/Wait nodes sparingly to conserve execution resources.
    - For processing arrays with delays, handle each item with a loop and insert a delay between iterations.  
    - [n8n Community: Delays Between Array Items](https://community.n8n.io/t/processing-array-items-individually-with-delays-between-each-item/86897)
    - [n8n Community: Wait Node & Parallel Execution](https://community.n8n.io/t/wait-node-parelle-node-workflow-execution/154867)

### Jira Automation

- **Component:**Delay / Pause / Wait Step
- **Function:**Inserts a pause to prevent race conditions and sequence automation reliably.
- **Configuration:**Duration, or stacking multiple delays for longer waits.
- **Best Practices:**- Be aware that branches in Jira automation may execute in parallel. Serializing actions with delays or splitting into separate rules may be necessary.
    - [Jira Issue: Support for delay / pause / wait step](https://jira.atlassian.com/browse/AUTO-238)
    - [Atlassian Community: Can I set a delay in Jira Automation?](https://community.atlassian.com/forums/Jira-questions/Can-I-set-a-delay-in-Jira-Automation/qaq-p/3074180)

## Best Practices

- **Always use non-blocking delays (Promises, async/await, or platform-native delay nodes).**- **Avoid synchronous/blocking sleep in servers or production environments.**- **Use timeouts to prevent indefinite waits.**- **Apply exponential backoff for polling external systems or retries.**- **Limit the scope of delays to only where necessary.**- **Support cancellation (e.g., with AbortController in JS, or abort/timeout configs in workflows).**- **Avoid excessive or unnecessary delays to conserve execution resources and avoid hitting quotas, especially in cloud automation platforms.**- **For platforms like n8n, distribute delays to avoid bottlenecks and resource contention.**## Troubleshooting / FAQ

**Why doesn't Node.js have a built-in `sleep()` function?**Node.js is designed for asynchronous, non-blocking I/O. Blocking the event loop would degrade all concurrent tasks. Use `async`/`await` or Promises.

**My delay node seems to block other flows!**Check for accidental use of blocking sleep (e.g., while loops or execSync in Node.js). In automation platforms, avoid excessive or long delays in shared (single-threaded) environments.

**How do I wait for a condition, not just a fixed time?**Use a polling loop with increasing delays (exponential backoff), or use “wait until” nodes if your platform supports it.  
- [LinkedIn: Intelligent Delay Node](https://www.linkedin.com/posts/muhammedadnanvv_alright-lets-cut-through-the-noise-youre-activity-7341374262135373825-6xUv)

**Can I cancel a delay/sleep operation?**In modern JavaScript, use `AbortController`. In workflow tools, look for nodes supporting abort/timeout.

## References & Further Reading

- [What is the JavaScript version of sleep()? (Stack Overflow)](https://stackoverflow.com/questions/951021/what-is-the-javascript-version-of-sleep)
- [Mimo: JavaScript Sleep Function](https://mimo.org/glossary/javascript/sleep-function)
- [Nodejs Sleep Function: Pause for a Period of Time](https://www.zignuts.com/blog/nodejs-sleep-function)
- [JavaScript Sleep, Wait & Delay Guide](https://www.index.dev/blog/javascript-sleep-wait-delay-guide)
- [AWS SSM Sleep Action](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-action-sleep.html)
- [Cognigy Sleep Node](https://docs.cognigy.com//ai/agents/develop/node-reference/logic/sleep)
- [n8n Community: Delays Between Array Items](https://community.n8n.io/t/processing-array-items-individually-with-delays-between-each-item/86897)
- [n8n Community: Wait Node & Parallel Execution](https://community.n8n.io/t/wait-node-parelle-node-workflow-execution/154867)
- [Jira Issue: Support for delay / pause / wait step](https://jira.atlassian.com/browse/AUTO-238)
- [Atlassian Community: Can I set a delay in Jira Automation?](https://community.atlassian.com/forums/Jira-questions/Can-I-set-a-delay-in-Jira-Automation/qaq-p/3074180)
- [LangChain Chatbot Real Python Tutorial](https://realpython.com/build-llm-rag-chatbot-with-langchain/)

## Parameter Table: Delay/Sleep Node (Generalized)

| Parameter    | Type            | Description                                   | Example Value          |
|--------------|-----------------|-----------------------------------------------|-----------------------|
| Duration     | Number/String   | How long to delay (ms/s/min/h, ISO 8601)      | `5000`, `"PT10M"`     |
| Condition    | Function/String | Optional: Wait until condition is met         | `status === "done"`   |
| Max Wait     | Number          | Maximum time to wait                          | `60000` (1 minute)    |
| Abort Signal | Object          | For JS: `AbortController.signal`              | -                     |
| Timeout      | Number          | Timeout for polling or waiting                | `30000` (30 seconds)  |

## Example Use Cases

### Chatbot Flow

- **Scenario:**Wait 3 seconds after user input before responding to simulate processing.  
- **How:**Place a “Sleep” node (e.g., 3000 ms) in Cognigy or n8n.

### API Rate Limiting

- **Scenario:**Integration sends requests with 1 req/sec limit.  
- **How:**Use `await sleep(1000)` in Node.js, or a 1-second Delay node in automation.

### Intelligent Polling (Event Wait)

- **Scenario:**Wait for payment confirmation, but avoid excessive API calls.  
- **How:**Use exponential backoff polling loop:

```js
let delay = 1000, maxDelay = 30000;
while (!(await isConfirmed())) {
  await sleep(delay);
  delay = Math.min(delay * 2, maxDelay);
}
```

## Related Keywords & Concepts

sleep function, pause period time, await promise resolve, asynchronous operations, await sleep, delay automation, return promise resolve, sleep promise, function sleep, const sleep, delay node, sleep delay, event loop, async function, async await syntax, sleep 2000

## Summary

A Delay/Sleep Node is a fundamental building block for orchestrating time-based and conditional flows in both code and modern workflow automation platforms. The current best practice in JavaScript is to use Promises and async/await for non-blocking, readable code. In automation platforms, delay/wait nodes should be used judiciously—configured to maximize reliability and efficiency, and always with an eye toward resource management and clarity of execution.

For code samples, workflow diagrams, and more advanced use patterns, consult the [References & Further Reading](#references--further-reading) section.

*This glossary entry is maintained for developers seeking robust solutions for time management, pacing, and conditional waits in automation and chatbot workflows.*