---
title: "Logic Node / Conditional Branching"
translationKey: "logic-node-conditional-branching"
description: "A Logic Node (Conditional Branching) evaluates conditions in chatbot and automation workflows, directing paths dynamically based on user input or context."
keywords: ["Logic Node", "Conditional Branching", "Chatbot", "Automation", "Workflow"]
category: "AI Chatbot & Automation"
type: "glossary"
date: 2025-12-05
lastmod: 2025-12-05
draft: false
---
## What is a Logic Node?

A **Logic Node**is a modular decision block in chatbot and automation workflows that evaluates conditions (such as user choices, variables, or statuses) and branches the flow accordingly. The logic node is the “decision point” (conditional branching) where the workflow diverges based on custom rules.

**Also known as:**- Conditional Branching Node
- If/Then Branch
- Split Action ([TextIt](https://help.textit.com/en/article/introduction-to-flows-1vmh15z/))
- Condition Node ([Noca AI](https://support.noca.ai/logic-nodes/))
- Switch Node
- Branch Node
## Why Use Conditional Branching?

Logic nodes enable workflows to:

- **Respond dynamically**to user input or context
- **Route users**to specific actions based on their choices or data
- **Implement business rules**(eligibility checks, escalations, approvals)
- **Personalize experiences**(based on tags, user properties, or history)
- **Reduce manual intervention**by automating complex processes

**Example:**If a customer selects “Report an Issue”, the bot asks for details; if they choose “Check Order Status”, it fetches order info.

**More:**- [BotStacks: Use Conditions and Logic Branching](https://docs.botstacks.ai/common-tasks/conversation-design/conditions-logic)

## Core Features of Logic Nodes

1. **Conditional Evaluation:**Define one or more conditions using variables, user inputs, or system states.

2. **Branching/Flow Control:**Route to different nodes/actions based on which condition is true.

3. **Context Variable Access:**Read/write variables in the conversation or workflow context.

4. **Nested Logic:**Support for multi-level or nested conditions (e.g., “If A, then check B; else do C”).

5. **Visual Representation:**Most platforms provide a visual editor for connecting and configuring logic nodes.

6. **No-Code/Low-Code Setup:**Configurable via graphical UI, but advanced logic may be supported by code or pseudo-code.
## Types of Logic Nodes and Branching

Platform offerings may include:

- **If/Then Branches:**Binary branching (true/false).
- **Switch/Case Nodes:**Multi-way branching for discrete values.
- **Split Actions:**Branching based on user input, variables, or randomization ([TextIt](https://help.textit.com/en/article/introduction-to-flows-1vmh15z/)).
- **Condition Nodes:**General-purpose true/false evaluators.
- **Loop, Break, Continue:**For iterative logic ([Noca AI](https://support.noca.ai/logic-nodes/)).
- **Random Branching:**For A/B testing or randomized flows.
- **Multi-Level Branching:**Nested or multi-layered logic ([Slack Workflow Builder](https://slack.com/blog/news/conditional-branching-workflow-builder)).

## How to Add and Configure a Logic Node

### Kore.ai Example

Logic nodes in Kore.ai can only be added as part of a Bot Action node.

**Steps:**1. Open the dialog task where you want to add branching.
2. Add/expand a **Bot Action**node ([Bot Action Node docs](https://developer.kore.ai/docs/bots/bot-builder-tool/dialog-task/bot-action-node/)).
3. Insert a **Logic Node**.  
   - The **Component Properties**tab is displayed by default.
   - ![Adding a logic node in Kore.ai](https://kore-wordpress.s3.us-east-2.amazonaws.com/developer.kore.ai/wp-content/uploads/20220921084031/add-logic-node-1024x456.gif)
4. Configure:
   - **Name**and **Display Name**in **Component Properties**.
   - Assign variable namespaces as needed.
   - Use **Manage Context Variables**to define/update variables (e.g., `_context.BotUserSession.<variable_name>_`).
   - In **Instance Properties**, set tags or dialog-specific metadata.
   - In **Connection Properties**, define conditional statements to control which node executes next, based on entity values, context objects, or intents.
5. Save and connect branches visually.
### Platform-Agnostic Guide

Most platforms follow a similar pattern:

1. Open your bot/automation builder (e.g., [Yellow.ai](https://docs.yellow.ai/docs/platform_concepts/studio/build/nodes/logic-nodes), [HubSpot](https://knowledge.hubspot.com/chatflows/use-if-then-branches-with-chatflows), [Slack](https://slack.com/blog/news/conditional-branching-workflow-builder), [TextIt](https://help.textit.com/en/article/introduction-to-flows-1vmh15z/)).
2. Navigate to the relevant flow or journey.
3. Add a logic/condition/split node:
   - Look for **Logic**, **If/Then**, **Condition**, or **Split Action**in the node palette.
   - Drag and drop onto your canvas.
4. Define condition(s):
   - Specify property or variable to evaluate.
   - Set comparison operators (equals, contains, >, etc.).
   - Input values to match.
5. Connect branches to next steps.
6. Test the flow using preview/testing tools.
## Logic Node Settings & Properties

### Component Properties

- **Name:**Internal identifier.
- **Display Name:**User-friendly label.
- **Variable Namespaces:**Scope for variables (task or node-level isolation).
- **Manage Context Variables:**Set/update variables in conversation context.

*Component Properties changes affect all instances of a logic node.*

### Instance Properties

- **Tags:**Custom metadata or tags for tracking/segmentation.
- **Dialog-Scoped Settings:**Settings specific to the current dialog/flow.

*Instance Properties affect only the current node instance.*

### Connection Properties

- **Conditional Connections:**Define which node executes next, based on conditions.
- **Fallback Path:**Default branch if no conditions are met.
- **Intents/Entity Values:**Use detected intents/entity values for branching.

*Some platforms restrict logic node connections to specific scopes (e.g., inside Bot Action nodes in Kore.ai).*
## Conditional Statements and Syntax

Conditional statements determine how branches are evaluated. These may be set via UI or written as expressions.

**Common Operators:**- equals (==)
- not equals (!=)
- contains
- greater than (>)
- less than (<)
- in (list membership)
- and, or, not (logical operators)

**Pseudo-code Example:**```pseudo
if (user_response == "yes") {
    go_to("ConfirmOrder");
} else if (user_response == "no") {
    go_to("CancelOrder");
} else {
    go_to("ClarifyIntent");
}
```

**Platform UI Example:**- In [HubSpot](https://knowledge.hubspot.com/chatflows/use-if-then-branches-with-chatflows), use the **If/then branches**tab to add rules based on user response, property, or agent availability.
- In [Slack Workflow Builder](https://slack.com/blog/news/conditional-branching-workflow-builder), select criteria such as dropdown values, form responses, or channel data.

## Practical Usage Scenarios

**1. User Response Handling**Route users based on “Yes/No” answers, option selections, or free text.

**2. Support Request Routing**Direct support tickets to the right team (e.g., technical, billing, equipment).

**3. Multi-Step Approvals**Implement tiered approvals (e.g., manager, then director).

**4. Personalization**Show responses based on user tags or CRM properties.

**5. Data Validation**Check for valid phone numbers, emails, or required fields before progressing.

**6. A/B Testing**Randomly branch users for experimentation or feature rollout.

**7. Error Handling**Route to fallback or clarification paths for invalid/missing inputs.
## Examples: Real-World Conditional Branching

### Example 1: Yes/No Decision
**Scenario:**Bot asks, “Do you want to receive notifications?”
- If user response equals “yes” → Go to **Enable Notifications**node.
- Else → Go to **Disable Notifications**node.

### Example 2: Support Request Routing ([Slack Workflow Builder](https://slack.com/blog/news/conditional-branching-workflow-builder))
**Scenario:**User submits a support request with issue type.
- If `issue_type == "technical"` → Route to `#tech-support`
- If `issue_type == "billing"` → Route to `#billing-support`
- If `issue_type == "equipment"` → Route to `#equipment-support`

### Example 3: Quick Reply Branching ([HubSpot Bot](https://knowledge.hubspot.com/chatflows/use-if-then-branches-with-chatflows))
**Scenario:**Bot asks, “What can we help you with?”  
[Quick replies](/en/glossary/quick-replies/): “Order Status”, “Technical Support”, “Other”
- If **Order Status**→ Go to order lookup
- If **Technical Support**→ Go to support
- If **Other**→ General inquiry

### Example 4: Multi-Layered Approval ([Slack](https://slack.com/blog/news/conditional-branching-workflow-builder))
- If `manager_approval == "approved"`:
  - Route to finance director.
  - If `finance_approval == "approved"`: Notify procurement.
  - Else: Notify rejection.
- Else: Notify rejection.

### Example 5: Split Action for Data Validation ([TextIt](https://help.textit.com/en/article/introduction-to-flows-1vmh15z/))
- If input is a valid phone number → Proceed.
- Else → Send error and prompt for re-entry.

## Best Practices & Tips

- Define all branches, including fallback (“else”).
- Use descriptive node names for clarity.
- Group related logic for modularity.
- Test every branch using preview/testing tools.
- Use variables/tags for analytics and personalization.
- Avoid overly nested logic; break complex logic into smaller flows.
- Document business rules using comments or descriptions.
## Limitations & Edge Cases

- **Scope Restrictions:**- In Kore.ai, logic nodes are scoped inside Bot Action nodes.
- **Global vs. Instance Settings:**- Component Properties are global, Instance Properties are local.
- **Node Limits:**- Some platforms have node-per-flow limits (e.g., Yellow.ai: 150 nodes).
- **Deletion Dependencies:**- Active branches must be deleted before deleting the parent node (HubSpot).
- **Data Type Considerations:**- Data types in conditions (string vs. number) must be compatible.
- **Random/A/B Branching:**- May yield unpredictable results without seeding or tracking.
## Related Concepts and Further Reading

- [Bot Action Node (Kore.ai)](https://developer.kore.ai/docs/bots/bot-builder-tool/dialog-task/bot-action-node/)
- [Yellow.ai Node Types](https://docs.yellow.ai/docs/platform_concepts/studio/build/nodes)
- [TextIt Flows](https://help.textit.com/en/article/introduction-to-flows-1vmh15z/)
- [Slack Workflow Builder Guide](https://slack.com/help/articles/360035692513-Guide-to-Slack-Workflow-Builder)
- [Noca AI Logic Nodes](https://support.noca.ai/logic-nodes/)
- [HubSpot Chatflows](https://knowledge.hubspot.com/chatflows/use-if-then-branches-with-chatflows)


## Source Links and Further Reading

- [BotStacks: Use Conditions and Logic Branching](https://docs.botstacks.ai/common-tasks/conversation-design/conditions-logic/)
- [Kore.ai: Working with the Logic Node](https://developer.kore.ai/docs/bots/bot-builder-tool/dialog-task/working-with-the-logic-node/)
- [Yellow.ai: Logic Nodes](https://docs.yellow.ai/docs/platform_concepts/studio/build/nodes/logic-nodes)
- [HubSpot: If/Then Branches](https://knowledge.hubspot.com/chatflows/use-if-then-branches-with-chatflows)
- [Slack: Conditional Branching Workflow Builder](https://slack.com/blog/news/conditional-branching-workflow-builder)
- [TextIt: Introduction to Flows](https://help.textit.com/en/article/introduction-to-flows-1vmh15z/)
- [Kore.ai: Managing Namespace](https://developer.kore.ai/docs/bots/bot-settings/bot-management/managing-namespace/)
- [Kore.ai: Custom Meta Tags](https://developer.kore.ai/docs/bots/bot-builder-tool/dialog-task/custom-meta-tags/)
- [Slack: Workflow Builder Guide](https://slack.com/help/articles/360035692513-Guide-to-Slack-Workflow-Builder)
- [Noca AI: Logic Nodes](https://support.noca.ai/logic-nodes/)

**For more details, always consult your platform's official documentation and developer guides.**
