---
title: "How to Set Up Rules"
date: 2026-01-30
lastmod: 2026-01-30
draft: false
translationKey: "rule-settings-howto"
description: "You can create 'rules' to automatically process tickets in LiveAgent based on your specific business processes. If you can think of rules for your business operations, you can create either 'time-based' or 'regular rules'."
keywords: ["rules", "settings", "method", "LiveAgent", "escalation"]
category: "ticket-system/automation"
---
## What are Rules

You can create "rules" to automatically process tickets in LiveAgent based on your specific business processes. If you can think of rules for your business operations, you can create either "time-based" or "regular rules".

"Rules" allow you to complete tickets under certain conditions, add tags (categorize content), increase ticket priority by customer (improves display order), or automatically process unnecessary inquiries. By clarifying business processes, rules can be set up and automation can be advanced.

## Rule Setup Procedure

### Determining Rule Name and Application Conditions

First, determine the name of the rule to be created and the conditions to which the rule will apply.

From the agent screen left menu, click "Settings" > "Automation" > "Rules" to display the rules menu. Time conditions can be set in units of "days", "hours", and "minutes". If time conditions are needed, set up [time rule settings](#).

The conditions that can be applied in "Rules" are as follows:

- Tickets created from email
- Ticket creation
- Ticket status changed
- Ticket transferred
- Offline message group added
- Agent evaluation
- Ticket tags changed

### Time Rule Application Conditions

Determine the conditions for applying time rules. Conditions can be created using combinations of AND and OR conditions, and it's possible to define multiple "conditions" that form one condition group.

The content that can be used as "application conditions" is as follows:

- Created from inquiry widget
- Ticket source
- Ticket status
- Ticket creation
- Ticket modification
- Ticket deleted
- Ticket start referrer URL
- Ticket priority
- Last received message
- Assigned agent status
- Ticket team
- Ticket assignment
- Customer group
- Created from invitation
- Ticket tags

### Determining Actions to Apply to Rules

Determine the actions (automatic processing) for tickets that match the conditions and application conditions. In addition to ticket escalation and tagging, it's also possible to send emails that insert ticket messages and customer information using variables. Like application conditions, multiple actions can be combined to handle ticket processing.

The applicable "actions" are as follows:

- Transfer ticket
- Resolve ticket
- Delete ticket
- Change ticket priority
- Change SLA level
- Mark as spam
- Unmark as spam
- Purge ticket
- Send reply
- Add tags
- Remove tags
- Send email to specified destination
- Stop other rules