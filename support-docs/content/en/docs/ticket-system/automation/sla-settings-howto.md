---
title: "How to Configure SLA Settings"
date: 2026-01-30
lastmod: 2026-01-30
draft: false
translationKey: "sla-settings-howto"
description: "SLA (Service Level Agreement) is a quality standard for your company's customer support. By defining time limits for responding to tickets, you can manage support quality."
keywords: ["SLA", "settings", "configuration", "customer support", "LiveAgent"]
category: "ticket-system/automation"
---
## About SLA

SLA (Service Level Agreement) is a quality standard for your company's customer support. By defining time limits for responding to tickets, you can manage support quality.

SLA settings in LiveAgent have "Levels (priority)" and "Rules (conditions)". By combining these two elements, LiveAgent automatically adjusts ticket prioritization according to inquiry situations such as "standard time", "emergency", and "incident occurrence".

## How to Configure SLA

Select Settings > Automation > SLA from the menu.

![](/liveagent/scripts/file.php?view=Y&file=054181510e6203296f8fd7a311e51d05)

### SLA Level Configuration

Define the standard SLA for LiveAgent operations. Set up "SLA Levels" to specify the response times that agents should meet for tickets. Multiple SLA levels can be configured as needed.

#### SLA Level Configuration Items

- SLA level name
- Response time settings
- Email reply target deadline (first response/next response)
- Live chat response time target limit (chat response)
- Phone and voice conversation response time target limit (phone response)
- Time zone
- Business hours for support in LiveAgent (holiday settings can also be added)

※If you need to define different time limits based on conditions, create additional SLA levels.

#### Examples of Creating Multiple SLA Levels

- Set shorter response time limits for incident handling compared to normal responses
- Set shorter response time limits for specific customer groups like VIP customers compared to normal responses

[Configuration Example]

![](/liveagent/scripts/file.php?view=Y&file=6946075bbb1f9d711d8e45a73ea6d058)

### SLA Rules Configuration

When setting up multiple "SLA Levels", create level assignment conditions using "SLA Rules".

#### SLA Rules Configuration Items

- SLA rule name
- Application condition definition
- Definition of "SLA Level" to use

SLA rule application conditions are created by selecting from the following items. Advanced condition settings are possible by combining multiple items.

#### List of SLA Rule Application Conditions

- Ticket source
- Ticket status
- Ticket creation
- Ticket modification
- Ticket deletion
- Ticket start referrer URL
- Ticket priority
- Last received message
- Assigned agent status
- Ticket department
- Ticket assignment
- Customer group
- Created from invitation
- Ticket tags

[Configuration Example: When "incident" tag is added to a ticket, apply "Incident SLA" to the SLA level]

![](/liveagent/scripts/file.php?view=Y&file=afb9f527b8c1d7677c4fed9863a3cd80)