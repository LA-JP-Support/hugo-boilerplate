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

A **Loop Node**automates the repetition of actions in a workflow. It can process a list of items, repeat tasks a specific number of times, or run until a condition is met. Loop Nodes are essential in workflow automation, RPA, and AI chatbot platforms for handling repetitive operations such as sending emails to a list of users, validating inputs, or retrying failed actions.

- **Typical Use Cases:**- Processing lists/collections (e.g., send messages to each contact)
  - Automating repetitive tasks (e.g., generate reports for multiple departments)
  - [Batch processing](/en/glossary/batch-processing/) (e.g., handle API calls in groups)
  - Input validation (e.g., prompt until valid input is received)
## How Does a Loop Node Work?

The fundamental logic of a Loop Node is to evaluate, on each cycle, whether to continue or exit the loop. This evaluation is based on:

- The current iteration count (in fixed loops)
- The contents or properties of the current item (in collection loops)
- The result of a logical condition or expression (in conditional loops)

### Generic Loop Node Flow

1. **Input:**Receives a list, count, or trigger from a previous node.
2. **Check Condition:**Decides whether to continue based on the type of loop.
3. **Execute:**Runs the contained actions/sub-nodes.
4. **Iteration:**Advances to the next item, increments the counter, or re-evaluates the condition.
5. **Exit:**Stops when the exit condition is met or the list is exhausted.

**Visual Reference:**![n8n Loop Node Example](https://docs.n8n.io/_images/flow-logic/looping/example_workflow.png)
## Types of Loop Nodes and Looping Methods

Loop nodes can be classified by their exit criteria or iteration mechanism:

### 1. Fixed Count Loop (Simple Loop)

- Repeats actions a specified number of times.
- Configured with start, end, and increment values.
- **Ideal for:**Scenarios where the repetition count is known in advance.

**Example:**Send a reminder email three times.

### 2. For Each / Loop Over Items

- Iterates over each item in a list, array, or table.
- Each iteration processes one element.
- **Ideal for:**Processing data collections, e.g., sending personalized emails.

### 3. Conditional Loop (While / Until)

- Repeats actions as long as a condition is true.
- Configured with logical operators and operands.
- **Ideal for:**Input validation, retry logic, dynamic workflows.

### 4. Batch Loop

- Processes items in groups, useful for bulk operations or rate limiting.
- **Ideal for:**API integrations where requests must be chunked.
## How to Use Loop Nodes

### General Steps (Applicable to MindPal, n8n, Power Automate, etc.)

1. **Insert the Loop Node:**In the workflow designer, add a Loop Node from the logic/flow control section.

2. **Configure the Loop:**- **Fixed Count:**Specify start, end, and increment.
   - **For Each:**Select the collection/list to iterate over.
   - **Conditional:**Define the exit condition with logical expressions.

3. **Add Actions Inside the Loop:**Drag and drop (or connect) other nodes/actions inside the loop to be executed on each cycle.

4. **Handle Outputs:**Use the outputs from the looped actions as inputs for subsequent workflow steps.

**MindPal Example:**- Define the list of items ("For each item in" field).
- Select the agent (processing logic or AI).
- Write clear, variable-driven instructions for processing.
- [Reference](https://docs.mindpal.space/workflow/build/loop-node#configuring-a-loop-node)

**n8n Example:**- Most nodes process all items automatically.
- Use “Loop Over Items” for batch or chunked processing.
- Manual looping possible with wiring and IF nodes.
- [Reference](https://docs.n8n.io/flow-logic/looping/#creating-loops)

**Power Automate Example:**- Choose between “Loop,” “Loop Condition,” or “For Each.”
- Set start, end, increment, or input list as needed.
- Use "Exit loop" and "Next loop" for control.
- [Reference](https://learn.microsoft.com/en-us/power-automate/desktop-flows/use-loops)

## Loop Node Configuration: Key Parameters

| Parameter            | Description                                                                                | Example Value         |
|----------------------|--------------------------------------------------------------------------------------------|----------------------|
| **Start From**| The initial value of the counter (fixed count loops)                                       | 1                    |
| **End To**| The value at which to stop (fixed count loops)                                             | 10                   |
| **Increment By**| How much to increase the counter each iteration                                            | 1                    |
| **Collection**| The array or list to iterate over (for-each loops)                                        | `[{"name":"A"}]`     |
| **Batch Size**| Number of items to process per batch                                                       | 5                    |
| **Exit Condition**| Logical expression controlling loop termination                                            | `input == valid`     |
| **Current Item**| The current item being processed                                                           | `{ "email": ... }`   |
| **Output**| The result of actions performed in each iteration                                          | `{"status":"sent"}`  |

**Power Automate Example:**- Start from: 1, Increment by: 1, End to: 5  
- For Each: List of filenames  
- Loop Condition: `count < 10`  
- [Reference](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/loops)

## Examples of Loop Nodes in Action

### 1. Batch Email Sending
**Scenario:**Send emails to a list of customers.
**Workflow:**Fetch customers → Loop Node (for each) → Send Email

### 2. Input Validation (Chatbot)
**Scenario:**Prompt user for a valid email until correct.
**Workflow:**Loop Node (exit when valid) → Prompt and validate

### 3. API Request Retry
**Scenario:**Retry an API call up to 3 times until successful.
**Workflow:**Loop Node (exit on success or max attempts) → API call

### 4. Inventory Check (E-commerce)
**Scenario:**Check stock for products in a catalog.
**Workflow:**Fetch catalog → Loop Node (for each) → Check inventory
## Use Cases for Loop Nodes

- **Processing Lists:**Send notifications, emails, updates, or perform calculations on each item in a database or spreadsheet.
- **Batch Handling:**Process records in groups to avoid rate limits (e.g., API calls in chunks).
- **Retry Logic:**Reattempt operations (like file downloads or API requests) until success or a limit is reached.
- **Input Validation:**Continuously prompt a user until correct data is entered.
- **Conditional Iteration:**Execute steps until a business rule is satisfied.
- **Dynamic Sequences:**Loop through dynamic sets of questions, tasks, or logic branches.

## Platform-Specific Notes

### MindPal

- **Loop Node:**Takes a list, assigns an agent, and processes each item with specific instructions.
- **Variables:**Use variables to pass data between loop cycles and other nodes.
- [MindPal Loop Node Docs](https://docs.mindpal.space/workflow/build/loop-node)

### n8n

- **Implicit Iteration:**Nodes typically process all input items individually.
- **Loop Over Items Node:**For batch processing and explicit chunking.
- **Manual Loops:**Possible with wiring and IF nodes for custom logic.
- **Node Exceptions:**Some nodes (see [Node exceptions](https://docs.n8n.io/flow-logic/looping/#node-exceptions)) require manual looping.
- [n8n Looping Docs](https://docs.n8n.io/flow-logic/looping/)

### Power Automate

- **Three Loop Types:**Simple Loop (fixed count), Loop Condition (while/until), For Each (collections).
- **Control Actions:**"Exit loop" to break early, "Next loop" to skip current iteration.
- **Variables:**Loops generate index or current item variables for use inside actions.
- [Power Automate Loops Reference](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/loops)
- [Power Automate Using Loops](https://learn.microsoft.com/en-us/power-automate/desktop-flows/use-loops)

### Node.js Event Loop

- **Distinct from workflow Loop Node:**The Node.js event loop is a low-level mechanism that enables asynchronous, non-blocking operations in JavaScript.
- **Phases:**timers, pending callbacks, poll, check, close callbacks.
- **How It Works:**JavaScript executes synchronously; async operations (I/O, timers) are handled by libuv, callbacks are queued and run in event loop phases.
- **Relevance:**Foundation for asynchronous "loops" in code such as setTimeout, setInterval, and event-driven programming.
- [Node.js Event Loop Official Guide](https://nodejs.org/en/learn/asynchronous-work/event-loop-timers-and-nexttick)
- [GeeksforGeeks Event Loop Article](https://www.geeksforgeeks.org/node-js/node-js-event-loop/)

## Special Considerations and Best Practices

- **Infinite Loops:**Always define clear exit conditions to avoid unintentional infinite loops.
- **Performance & Rate Limits:**Large or unbounded loops can negatively impact performance and may trigger API or platform rate limits.
- **Batch Size:**Adjust batch processing to balance efficiency and compliance with external system limits.
- **Error Handling:**Implement retry limits and graceful error handling for loops that interact with unreliable services.
- **Node Exceptions:**Not all workflow nodes auto-iterate; consult platform documentation.
- **Variable Scope:**Ensure variables for counters, current items, and results are scoped correctly within and outside loops.
## Key Terms and Related Concepts

| Term                   | Definition                                                                                      |
|------------------------|------------------------------------------------------------------------------------------------|
| **Loop Node**| A node/function that repeats actions until a condition is met or items are processed.          |
| **Iteration**| One complete cycle through the loop’s actions.                                                 |
| **Exit Condition**| The logic that determines when the loop ends.                                                  |
| **For Each Loop**| Processes every item in a collection or array.                                                 |
| **Batch Processing**| Dividing a large set into smaller groups for processing.                                       |
| **Event Loop**| (Node.js) A system for managing asynchronous callbacks and tasks.                              |
| **Pending Callbacks**| Callbacks waiting to be handled in a phase of the event loop.                                  |
| **Timers**| Scheduled callbacks executed after a delay (setTimeout/setInterval in Node.js).                |
| **Flow Logic**| The sequence and rules governing how nodes execute in a workflow.                              |

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
