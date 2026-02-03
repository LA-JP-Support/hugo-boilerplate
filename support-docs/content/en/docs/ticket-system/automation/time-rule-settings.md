---
title: "How to Set Up Time Rules"
date: 2026-01-30
lastmod: 2026-01-30
draft: false
translationKey: "time-rule-settings"
description: "You can create 'Time Rules' based on your unique business processes. If you can think of rules within your business operations, you can create either 'Time-based' or 'Regular Rules'."
keywords: ["rules", "settings", "method", "LiveAgent", "escalation"]
category: "ticket-system/automation"
---
## What are Time Rules

You can create "Time Rules" based on your unique business processes. If you can think of rules within your business operations, you can create either "Time-based" or "Regular Rules".

For example, through time rule settings, it becomes possible to "automatically complete tickets" if there is no action from customers 24 hours after responding to a ticket, "automatically send emails after 3 days", or "tag tickets that remain unresolved after a week".

## Time Rule Setup Procedure

### Determining Time Conditions

First, determine the name of the time rule to be created and the time conditions to apply to the rule.

From the agent screen's left menu, click "Settings" > "Automation" > "Time Rules" to display the time rules menu. Time conditions can be set in units of "days", "hours", and "minutes". If no time conditions are set, regular rule settings will be applied.

The time conditions applicable in "Time Rules" are as follows:

- Ticket is older than specified
- Ticket status changed before specified time
- Ticket due date is within deadline
- Ticket due date has passed deadline

![](/liveagent/scripts/file.php?view=Y&file=265dc2f635cfc679d2064f8b617ae7a2)

### Setting Rule Application Conditions

Determine the conditions for applying time rules. Conditions can be created using combinations of AND and OR conditions, and it's possible to define multiple "conditions" that form one condition group.

The available "application conditions" are as follows:

- Ticket status
- Ticket creation
- Ticket status was changed
- Ticket was deleted
- Ticket initial referrer URL
- Ticket priority
- Ticket team
- Ticket assignee
- Customer group
- Ticket tags

![](/liveagent/scripts/file.php?view=Y&file=cc740db677a5c8f6a9a3e91324015b55)

### Action Settings

Determine the actions (automatic processing) for tickets that match the time conditions and application conditions. In addition to ticket escalation and tagging, it's also possible to send emails with ticket content inserted using variables. Like application conditions, multiple actions can be combined to handle ticket processing.

The applicable "Actions" are as follows:

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
- Send email to specified recipient
- Stop other rules

![](/liveagent/scripts/file.php?view=Y&file=222656bd5a896ab3cc328925bcea23fc)