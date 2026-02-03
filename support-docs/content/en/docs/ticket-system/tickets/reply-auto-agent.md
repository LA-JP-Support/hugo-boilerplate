---
title: "How to Automatically Assign Tickets to Agents After Replies"
date: 2026-01-30
lastmod: 2026-01-30
draft: false
translationKey: "reply-auto-agent"
description: "There are several ways to create rules to achieve this functionality. Here are some examples. You can customize the rules using additional conditions and actions."
keywords: ["agent", "ticket", "assignment", "customization", "status"]
category: "ticket-system/tickets"
---
## Overview of Automatic Assignment Rules After Ticket Replies

There are several implementation methods for rules that automatically assign tickets to agents. Below are specific examples.

## Rule 1: Automatic Assignment for All Actions

![](/liveagent/scripts/file.php?view=Y&file=a32a728c2e810d9d0fbd9f70b4db42ba)

### Features
This rule automatically assigns tickets to agents who perform the following actions, not just replying to tickets:

- Replying to tickets
- Adding notes
- Completing tickets with the "Resolve" button

## Rule 2: Automatic Assignment for Specific Statuses

![](/liveagent/scripts/file.php?view=Y&file=4ff1e56918c09a77953c6ca0257bf7de)

### Features
This rule operates under more limited conditions:

- Only targets tickets with "New" or "Open" status
- Automatically assigns tickets to the agent who replied

## Customization Points

You can further customize the rules by using additional conditions and actions. Settings can be flexibly configured to match your organization's needs.