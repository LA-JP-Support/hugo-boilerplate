---
title: "Logic Node / Conditional Branching"
translationKey: "logic-node-conditional-branching"
description: "A decision point in workflows that evaluates conditions and automatically routes users to different paths, enabling personalized and intelligent responses based on their choices or data."
keywords: ["Logic Node", "Conditional Branching", "Chatbot", "Automation", "Workflow"]
category: "AI Chatbot & Automation"
type: "glossary"
date: 2025-12-18
lastmod: 2025-12-18
draft: false
---

## What is a Logic Node?

A Logic Node is a modular decision block in chatbot and automation workflows that evaluates conditions—such as user choices, variables, or system states—and branches the flow accordingly. It represents the "decision point" where workflows diverge based on custom rules, enabling dynamic, intelligent responses to user input or changing contexts.

Also known as Conditional Branching Node, If/Then Branch, Split Action, Condition Node, Switch Node, or Branch Node, logic nodes are fundamental building blocks in modern automation platforms. They transform linear workflows into sophisticated, adaptive systems capable of handling complex business logic and user interactions.

<strong>Core Function:</strong>Logic nodes enable workflows to respond dynamically to user input or context, route users to specific actions based on their choices or data, implement business rules (eligibility checks, escalations, approvals), personalize experiences based on tags, user properties, or history, and reduce manual intervention by automating complex decision-making processes.

## Why Use Conditional Branching?

<strong>Dynamic Response:</strong>Workflows adapt to user input in real-time, providing contextually appropriate responses rather than following rigid, predetermined paths.

<strong>Intelligent Routing:</strong>Direct support requests to appropriate teams (technical, billing, equipment) based on issue type, urgency, or customer tier without manual intervention.

<strong>Business Rule Implementation:</strong>Encode complex business logic including eligibility checks, multi-tier approvals, compliance requirements, and exception handling directly into automated workflows.

<strong>Personalization at Scale:</strong>Deliver customized experiences based on user tags, CRM properties, purchase history, or behavioral patterns without individual configuration.

<strong>Process Automation:</strong>Eliminate manual decision-making for routine scenarios, freeing human agents for complex, high-value interactions requiring judgment and empathy.

<strong>Example Scenario:</strong>Customer selects "Report an Issue" → bot asks for details and creates ticket. Customer selects "Check Order Status" → bot retrieves order information and provides tracking updates. Customer selects "Billing Question" → bot routes to billing department with full conversation context.

## Core Features and Capabilities

### Conditional Evaluation

Define single or multiple conditions using variables, user inputs, system states, timestamps, or external data sources. Support for complex Boolean logic (AND, OR, NOT) enables sophisticated decision trees matching real-world business requirements.

### Flow Control and Branching

Route execution to different nodes or actions based on condition evaluation results. Support for multiple branch paths enables parallel processing, fallback handling, and graceful degradation when primary paths fail.

### Context Variable Management

Read and write variables in conversation or workflow context, maintaining state across multiple interactions. Variables can store user preferences, transaction data, session information, or temporary calculation results.

### Nested Logic Support

Build multi-level conditional structures ("If A, then check B; else if C, then check D; else do E") enabling complex decision-making that mirrors human reasoning processes.

### Visual Representation

Most platforms provide drag-and-drop editors for connecting and configuring logic nodes, making complex workflows comprehensible to non-technical stakeholders and enabling collaborative design.

### No-Code/Low-Code Configuration

Configure logic through graphical interfaces with form-based inputs, though advanced scenarios may leverage scripting or pseudo-code for maximum flexibility.

## Types and Branching Patterns

### Binary Decision (If/Then)

Simple true/false evaluation directing flow to one of two paths. Ideal for yes/no questions, boolean checks, or presence/absence validation.

### Multi-Way Branching (Switch/Case)

Evaluate single variable against multiple discrete values, routing to appropriate branch for each case. Efficient for menu selections, status codes, or category classifications.

### Split Actions

Branch based on user input, context variables, or randomization. Used for A/B testing, load distribution, or dynamic content delivery based on user characteristics.

### Condition Evaluation

General-purpose conditional nodes accepting complex expressions with multiple operators and operands. Support mathematical comparisons, string matching, regex patterns, and custom functions.

### Iterative Logic (Loop, Break, Continue)

Implement looping constructs for processing collections, retry logic, or repeated validation checks until conditions are met or limits reached.

### Random Branching

Distribute traffic randomly across multiple paths for A/B testing, feature rollout, or load balancing across equivalent service endpoints.

### Multi-Level Branching

Nested conditional structures enabling complex decision trees with multiple evaluation stages and interdependent conditions.

## Implementation Guide

### Platform-Agnostic Configuration Steps

<strong>Access Workflow Builder:</strong>Open your automation platform (Yellow.ai, HubSpot, Slack Workflow Builder, TextIt, or similar).

<strong>Navigate to Flow:</strong>Locate the specific workflow, journey, or dialog task requiring conditional logic.

<strong>Add Logic Node:</strong>Find Logic, If/Then, Condition, or Split Action in the node palette. Drag and drop onto canvas at appropriate decision point.

<strong>Define Conditions:</strong>- Specify property or variable for evaluation
- Select comparison operator (equals, contains, greater than, less than, in list)
- Input target values or expressions
- Configure additional conditions with AND/OR logic

<strong>Connect Branches:</strong>Wire each conditional branch to subsequent actions, creating complete execution paths for all possible outcomes.

<strong>Configure Fallback:</strong>Define default branch for conditions not explicitly matched, ensuring graceful handling of unexpected inputs.

<strong>Test Thoroughly:</strong>Use platform preview tools to verify correct branching for all input variations, edge cases, and error conditions.

### Kore.ai-Specific Implementation

Logic nodes in Kore.ai must be added within Bot Action nodes, providing scoped isolation for complex dialog management.

<strong>Procedure:</strong>1. Open dialog task requiring branching
2. Add or expand Bot Action node
3. Insert Logic Node (Component Properties tab displays)
4. Configure Name and Display Name
5. Assign variable namespaces for scope management
6. Use Manage Context Variables to define/update variables (e.g., `_context.BotUserSession.<variable_name>_`)
7. Set Instance Properties for tags or dialog-specific metadata
8. Define Connection Properties with conditional statements controlling next node execution
9. Save and visually connect branches

## Configuration Properties

### Component Properties (Global)

<strong>Name:</strong>Internal identifier for programmatic reference and debugging.

<strong>Display Name:</strong>User-friendly label appearing in visual editor for team communication.

<strong>Variable Namespaces:</strong>Scope management for variables ensuring task or node-level isolation prevents naming conflicts.

<strong>Context Variable Management:</strong>Interface for creating, reading, updating variables in conversation context, maintaining state across multiple turns.

Changes to Component Properties affect all instances of logic node across entire workflow.

### Instance Properties (Local)

<strong>Tags:</strong>Custom metadata for tracking, segmentation, analytics, or conditional processing downstream.

<strong>Dialog-Scoped Settings:</strong>Configuration specific to current dialog instance without affecting other uses of same node template.

Instance Properties apply only to current node instance, enabling customization without global impact.

### Connection Properties

<strong>Conditional Connections:</strong>Define which node executes next based on evaluated conditions, creating dynamic routing.

<strong>Fallback Path:</strong>Default branch when no conditions match, ensuring workflow never terminates unexpectedly.

<strong>Intent/Entity Integration:</strong>Use detected intents or extracted entity values in branching decisions, leveraging NLP capabilities.

Platform-specific restrictions may apply—for example, Kore.ai restricts logic node connections to Bot Action node scope.

## Conditional Logic Syntax

### Common Operators

<strong>Equality:</strong>`==` (equals), `!=` (not equals)

<strong>Comparison:</strong>`>` (greater than), `<` (less than), `>=` (greater or equal), `<=` (less or equal)

<strong>String Operations:</strong>`contains`, `starts_with`, `ends_with`, `matches` (regex)

<strong>List Operations:</strong>`in` (membership), `not_in`

<strong>Logical Operators:</strong>`and`, `or`, `not` for combining multiple conditions

### Expression Examples

```pseudo
if (user_response == "yes" && account_verified) {
    go_to("CompleteTransaction");
} else if (user_response == "yes" && !account_verified) {
    go_to("VerifyAccount");
} else if (user_response == "no") {
    go_to("CancelProcess");
} else {
    go_to("ClarifyIntent");
}
```

### Platform-Specific Syntax

<strong>HubSpot:</strong>Configure through If/then branches tab, adding rules based on contact properties, form responses, or agent availability status.

<strong>Slack Workflow Builder:</strong>Select criteria from dropdown values, form field contents, channel data, or custom variables.

<strong>TextIt:</strong>Visual flow editor with drag-and-drop split nodes supporting regex validation and variable evaluation.

## Practical Applications

### User Response Processing

Route based on explicit choices (yes/no, menu selections) or implicit signals (message tone, keyword presence, response length).

### Support Ticket Routing

Direct inquiries to specialized teams based on issue type, customer tier, SLA requirements, or technical complexity indicators.

### Multi-Stage Approvals

Implement hierarchical approval workflows (team lead → department head → finance director) with automatic escalation and timeout handling.

### Experience Personalization

Customize content, tone, offers based on user segments, purchase history, engagement level, or demographic data.

### Data Validation

Verify phone numbers, email formats, postal codes, credit card numbers before processing, prompting for correction when validation fails.

### A/B Testing

Randomly assign users to experimental variants for feature testing, messaging optimization, or conversion funnel analysis.

### Error Recovery

Route to fallback paths, clarification dialogs, or human escalation when inputs are ambiguous, invalid, or outside expected parameters.

## Real-World Examples

### E-Commerce Order Status

Bot asks: "What can I help you with today?"
- User selects "Track Order" → Request order number → Retrieve tracking data → Display status
- User selects "Return Item" → Verify purchase date → Check return eligibility → Generate return label
- User selects "Product Question" → Route to product specialist with context

### Financial Services Routing

Customer submits inquiry:
- Issue type = "Account Access" → Verify identity → Reset credentials or escalate to fraud team
- Issue type = "Transaction Dispute" → Retrieve transaction → Check dispute eligibility → Create case
- Issue type = "Investment Advice" → Route to licensed financial advisor with customer profile

### Healthcare Appointment Scheduling

Patient interaction:
- "Schedule new appointment" AND insurance_verified → Show available slots → Confirm booking
- "Schedule new appointment" AND !insurance_verified → Request insurance information → Verify → Proceed
- "Reschedule existing" → Retrieve current appointment → Show alternatives → Update booking

### HR Onboarding Automation

New employee workflow:
- Department = "Engineering" → Assign development environment → Schedule technical orientation
- Department = "Sales" → Assign CRM access → Schedule sales methodology training
- Contract type = "Contractor" → Limited access provisioning → Compliance documentation

## Best Practices

<strong>Define Complete Branch Coverage:</strong>Ensure all possible condition outcomes have defined paths, including edge cases and unexpected inputs.

<strong>Use Descriptive Naming:</strong>Label nodes, variables, conditions with clear, business-meaningful names enabling collaboration and maintenance.

<strong>Implement Modular Logic:</strong>Break complex decision trees into smaller, reusable flows improving testability and reducing coupling.

<strong>Test Exhaustively:</strong>Verify every branch path using platform testing tools with representative data covering normal, edge, and error cases.

<strong>Leverage Variables for Analytics:</strong>Capture decision paths, user choices in variables enabling downstream analysis and optimization.

<strong>Avoid Deep Nesting:</strong>Limit nesting depth to 3-4 levels; refactor complex logic into separate flows preventing maintenance nightmares.

<strong>Document Business Rules:</strong>Use comments, descriptions, or external documentation explaining decision logic and rationale for future reference.

<strong>Monitor Performance:</strong>Track branch execution frequency, conversion rates, abandonment points identifying optimization opportunities.

## Limitations and Considerations

<strong>Platform Scope Restrictions:</strong>Some platforms (e.g., Kore.ai) restrict logic nodes to specific container nodes, limiting flexibility.

<strong>Global vs. Instance Settings:</strong>Changes to Component Properties affect all instances; Instance Properties provide isolation but limited configurability.

<strong>Node Count Limits:</strong>Platforms may impose per-flow limits (e.g., Yellow.ai: 150 nodes) requiring careful design for complex workflows.

<strong>Deletion Dependencies:</strong>Active branches must be removed before deleting parent nodes, requiring careful coordination during refactoring.

<strong>Data Type Consistency:</strong>Ensure variables maintain consistent types (string vs. number) across conditions preventing unexpected behavior.

<strong>Random Branching Repeatability:</strong>Random distribution without seeding may produce unpredictable results for returning users or testing scenarios.

<strong>Performance Impact:</strong>Complex nested conditions or excessive branching can impact response latency in high-throughput scenarios.

## References


1. BotStacks. (n.d.). Conditions and Logic Branching. BotStacks Documentation.
2. Kore.ai. (n.d.). Working with Logic Node. Kore.ai Developer Documentation.
3. Kore.ai. (n.d.). Bot Action Node. Kore.ai Developer Documentation.
4. Yellow.ai. (n.d.). Logic Nodes. Yellow.ai Documentation.
5. Yellow.ai. (n.d.). Node Types. Yellow.ai Documentation.
6. HubSpot. (n.d.). If/Then Branches. HubSpot Knowledge Base.
7. Slack. (n.d.). Conditional Branching Workflow Builder. Slack Blog.
8. Slack. (n.d.). Workflow Builder Guide. Slack Help Center.
9. TextIt. (n.d.). Introduction to Flows. TextIt Help Center.
10. Kore.ai. (n.d.). Managing Namespace. Kore.ai Developer Documentation.
11. Kore.ai. (n.d.). Custom Meta Tags. Kore.ai Developer Documentation.
12. Noca AI. (n.d.). Logic Nodes. Noca AI Support.
