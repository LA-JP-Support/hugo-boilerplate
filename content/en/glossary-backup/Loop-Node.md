---
title: "Loop Node"
translationKey: "loop-node"
description: "A Loop Node automates repetitive actions in workflows, repeating tasks until a condition is met, a fixed number of times, or for each item in a collection. Essential for automation."
keywords: ["Loop Node", "Workflow Automation", "AI Chatbot", "RPA", "Iteration"]
category: "AI Chatbot & Automation"
type: "glossary"
date: 2025-12-05
lastmod: 2025-12-05
draft: false
---
## What is a Loop Node?

A <strong>Loop Node</strong>automates the repetition of actions in a workflow. It can process a list of items, repeat tasks a specific number of times, or run until a condition is met. Loop Nodes are essential in workflow automation, RPA, and AI chatbot platforms for handling repetitive operations such as sending emails to a list of users, validating inputs, or retrying failed actions.

- <strong>Typical Use Cases:</strong>- Processing lists/collections (e.g., send messages to each contact)
  - Automating repetitive tasks (e.g., generate reports for multiple departments)
  - Batch processing (e.g., handle API calls in groups)
  - Input validation (e.g., prompt until valid input is received)
## How Does a Loop Node Work?

The fundamental logic of a Loop Node is to evaluate, on each cycle, whether to continue or exit the loop. This evaluation is based on:

- The current iteration count (in fixed loops)
- The contents or properties of the current item (in collection loops)
- The result of a logical condition or expression (in conditional loops)

### Generic Loop Node Flow

1. <strong>Input:</strong>Receives a list, count, or trigger from a previous node.
2. <strong>Check Condition:</strong>Decides whether to continue based on the type of loop.
3. <strong>Execute:</strong>Runs the contained actions/sub-nodes.
4. <strong>Iteration:</strong>Advances to the next item, increments the counter, or re-evaluates the condition.
5. <strong>Exit:</strong>Stops when the exit condition is met or the list is exhausted.

<strong>Visual Reference:</strong>![n8n Loop Node Example](https://docs.n8n.io/_images/flow-logic/looping/example_workflow.png)
## Types of Loop Nodes and Looping Methods

Loop nodes can be classified by their exit criteria or iteration mechanism:

### 1. Fixed Count Loop (Simple Loop)

- Repeats actions a specified number of times.
- Configured with start, end, and increment values.
- <strong>Ideal for:</strong>Scenarios where the repetition count is known in advance.

<strong>Example:</strong>Send a reminder email three times.

### 2. For Each / Loop Over Items

- Iterates over each item in a list, array, or table.
- Each iteration processes one element.
- <strong>Ideal for:</strong>Processing data collections, e.g., sending personalized emails.

### 3. Conditional Loop (While / Until)

- Repeats actions as long as a condition is true.
- Configured with logical operators and operands.
- <strong>Ideal for:</strong>Input validation, retry logic, dynamic workflows.

### 4. Batch Loop

- Processes items in groups, useful for bulk operations or rate limiting.
- <strong>Ideal for:</strong>API integrations where requests must be chunked.
## How to Use Loop Nodes

### General Steps (Applicable to MindPal, n8n, Power Automate, etc.)

1. <strong>Insert the Loop Node:</strong>In the workflow designer, add a Loop Node from the logic/flow control section.

2. <strong>Configure the Loop:</strong>- <strong>Fixed Count:</strong>Specify start, end, and increment.
   - <strong>For Each:</strong>Select the collection/list to iterate over.
   - <strong>Conditional:</strong>Define the exit condition with logical expressions.

3. <strong>Add Actions Inside the Loop:</strong>Drag and drop (or connect) other nodes/actions inside the loop to be executed on each cycle.

4. <strong>Handle Outputs:</strong>Use the outputs from the looped actions as inputs for subsequent workflow steps.

<strong>MindPal Example:</strong>- Define the list of items ("For each item in" field).
- Select the agent (processing logic or AI).
- Write clear, variable-driven instructions for processing.
- [Reference](https://docs.mindpal.space/workflow/build/loop-node#configuring-a-loop-node)

<strong>n8n Example:</strong>- Most nodes process all items automatically.
- Use “Loop Over Items” for batch or chunked processing.
- Manual looping possible with wiring and IF nodes.
- [Reference](https://docs.n8n.io/flow-logic/looping/#creating-loops)

<strong>Power Automate Example:</strong>- Choose between “Loop,” “Loop Condition,” or “For Each.”
- Set start, end, increment, or input list as needed.
- Use "Exit loop" and "Next loop" for control.
- [Reference](https://learn.microsoft.com/en-us/power-automate/desktop-flows/use-loops)

## Loop Node Configuration: Key Parameters

| Parameter            | Description                                                                                | Example Value         |
|----------------------|--------------------------------------------------------------------------------------------|----------------------|
| <strong>Start From</strong>| The initial value of the counter (fixed count loops)                                       | 1                    |
| <strong>End To</strong>| The value at which to stop (fixed count loops)                                             | 10                   |
| <strong>Increment By</strong>| How much to increase the counter each iteration                                            | 1                    |
| <strong>Collection</strong>| The array or list to iterate over (for-each loops)                                        | `[{"name":"A"}]`     |
| <strong>Batch Size</strong>| Number of items to process per batch                                                       | 5                    |
| <strong>Exit Condition</strong>| Logical expression controlling loop termination                                            | `input == valid`     |
| <strong>Current Item</strong>| The current item being processed                                                           | `{ "email": ... }`   |
| <strong>Output</strong>| The result of actions performed in each iteration                                          | `{"status":"sent"}`  |

<strong>Power Automate Example:</strong>- Start from: 1, Increment by: 1, End to: 5  
- For Each: List of filenames  
- Loop Condition: `count < 10`  
- [Reference](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/loops)

## Examples of Loop Nodes in Action

### 1. Batch Email Sending
<strong>Scenario:</strong>Send emails to a list of customers.
<strong>Workflow:</strong>Fetch customers → Loop Node (for each) → Send Email

### 2. Input Validation (Chatbot)
<strong>Scenario:</strong>Prompt user for a valid email until correct.
<strong>Workflow:</strong>Loop Node (exit when valid) → Prompt and validate

### 3. API Request Retry
<strong>Scenario:</strong>Retry an API call up to 3 times until successful.
<strong>Workflow:</strong>Loop Node (exit on success or max attempts) → API call

### 4. Inventory Check (E-commerce)
<strong>Scenario:</strong>Check stock for products in a catalog.
<strong>Workflow:</strong>Fetch catalog → Loop Node (for each) → Check inventory
## Use Cases for Loop Nodes

- <strong>Processing Lists:</strong>Send notifications, emails, updates, or perform calculations on each item in a database or spreadsheet.
- <strong>Batch Handling:</strong>Process records in groups to avoid rate limits (e.g., API calls in chunks).
- <strong>Retry Logic:</strong>Reattempt operations (like file downloads or API requests) until success or a limit is reached.
- <strong>Input Validation:</strong>Continuously prompt a user until correct data is entered.
- <strong>Conditional Iteration:</strong>Execute steps until a business rule is satisfied.
- <strong>Dynamic Sequences:</strong>Loop through dynamic sets of questions, tasks, or logic branches.

## Platform-Specific Notes

### MindPal

- <strong>Loop Node:</strong>Takes a list, assigns an agent, and processes each item with specific instructions.
- <strong>Variables:</strong>Use variables to pass data between loop cycles and other nodes.
- [MindPal Loop Node Docs](https://docs.mindpal.space/workflow/build/loop-node)

### n8n

- <strong>Implicit Iteration:</strong>Nodes typically process all input items individually.
- <strong>Loop Over Items Node:</strong>For batch processing and explicit chunking.
- <strong>Manual Loops:</strong>Possible with wiring and IF nodes for custom logic.
- <strong>Node Exceptions:</strong>Some nodes (see [Node exceptions](https://docs.n8n.io/flow-logic/looping/#node-exceptions)) require manual looping.
- [n8n Looping Docs](https://docs.n8n.io/flow-logic/looping/)

### Power Automate

- <strong>Three Loop Types:</strong>Simple Loop (fixed count), Loop Condition (while/until), For Each (collections).
- <strong>Control Actions:</strong>"Exit loop" to break early, "Next loop" to skip current iteration.
- <strong>Variables:</strong>Loops generate index or current item variables for use inside actions.
- [Power Automate Loops Reference](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/loops)
- [Power Automate Using Loops](https://learn.microsoft.com/en-us/power-automate/desktop-flows/use-loops)

### Node.js Event Loop

- <strong>Distinct from workflow Loop Node:</strong>The Node.js event loop is a low-level mechanism that enables asynchronous, non-blocking operations in JavaScript.
- <strong>Phases:</strong>timers, pending callbacks, poll, check, close callbacks.
- <strong>How It Works:</strong>JavaScript executes synchronously; async operations (I/O, timers) are handled by libuv, callbacks are queued and run in event loop phases.
- <strong>Relevance:</strong>Foundation for asynchronous "loops" in code such as setTimeout, setInterval, and event-driven programming.
- [Node.js Event Loop Official Guide](https://nodejs.org/en/learn/asynchronous-work/event-loop-timers-and-nexttick)
- [GeeksforGeeks Event Loop Article](https://www.geeksforgeeks.org/node-js/node-js-event-loop/)

## Special Considerations and Best Practices

- <strong>Infinite Loops:</strong>Always define clear exit conditions to avoid unintentional infinite loops.
- <strong>Performance & Rate Limits:</strong>Large or unbounded loops can negatively impact performance and may trigger API or platform rate limits.
- <strong>Batch Size:</strong>Adjust batch processing to balance efficiency and compliance with external system limits.
- <strong>Error Handling:</strong>Implement retry limits and graceful error handling for loops that interact with unreliable services.
- <strong>Node Exceptions:</strong>Not all workflow nodes auto-iterate; consult platform documentation.
- <strong>Variable Scope:</strong>Ensure variables for counters, current items, and results are scoped correctly within and outside loops.
## Key Terms and Related Concepts

| Term                   | Definition                                                                                      |
|------------------------|------------------------------------------------------------------------------------------------|
| <strong>Loop Node</strong>| A node/function that repeats actions until a condition is met or items are processed.          |
| <strong>Iteration</strong>| One complete cycle through the loop’s actions.                                                 |
| <strong>Exit Condition</strong>| The logic that determines when the loop ends.                                                  |
| <strong>For Each Loop</strong>| Processes every item in a collection or array.                                                 |
| <strong>Batch Processing</strong>| Dividing a large set into smaller groups for processing.                                       |
| <strong>Event Loop</strong>| (Node.js) A system for managing asynchronous callbacks and tasks.                              |
| <strong>Pending Callbacks</strong>| Callbacks waiting to be handled in a phase of the event loop.                                  |
| <strong>Timers</strong>| Scheduled callbacks executed after a delay (setTimeout/setInterval in Node.js).                |
| <strong>Flow Logic</strong>| The sequence and rules governing how nodes execute in a workflow.                              |

## Further Reading and Resources

- [MindPal Docs: Loop Node](https://docs.mindpal.space/workflow/build/loop-node)
- [n8n Looping Documentation](https://docs.n8n.io/flow-logic/looping/)
- [Power Automate Loops Reference](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/loops)
- [Power Automate Using Loops](https://learn.microsoft.com/en-us/power-automate/desktop-flows/use-loops)
- [Node.js Event Loop Guide](https://nodejs.org/en/learn/asynchronous-work/event-loop-timers-and-nexttick)
- [Node.js Event Loop (GeeksforGeeks)](https://www.geeksforgeeks.org/node-js/node-js-event-loop/)
- [Master Loop Node in n8n (YouTube)](https://www.youtube.com/watch?v=acFkskQj-kw)
- [Loops in Microsoft Power Automate (YouTube)](https://www.youtube.com/watch?v=54ZFR4SCkO0)

This glossary page includes authoritative explanations, platform-specific configurations, technical examples, and best practices for Loop Nodes, with direct links to the most current official documentation for every major workflow automation environment.
