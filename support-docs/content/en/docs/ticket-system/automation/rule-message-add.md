---
title: "What do the items in 'Message Added' - 'Message Group Type' under 'Rules' refer to?"
date: 2026-01-30
lastmod: 2026-01-30
draft: false
translationKey: "rule-message-add"
description: "In the rule creation screen under 'Settings' > 'Automation' > 'Rules', when you select 'Message Added' in 'Apply', there is a condition called 'Message Group Type'. There are many items as shown below, and we will explain each one. *The displayed items vary depending on your subscription plan. (The example below is from the Advanced plan)"
keywords: ["message", "group", "rules", "customer portal", "LiveAgent"]
category: "ticket-system/automation"
---

## About Message Group Types

### What is Message Group Type

In the rule creation screen under "Settings" > "Automation" > "Rules", when you select "Message Added" in "Apply", there is a condition called "Message Group Type". *The displayed items vary depending on your [subscription plan](https://www.liveagent.jp/pricing/). (The example below is from the Advanced plan)

![](/liveagent/scripts/file.php?view=Y&file=0ae470e924c2db0dd1fb525bb252ae72)

## Details of Message Group Types

### Chat Related

#### Chat
- Started a chat

### Ticket Management

#### Delete
- Deleted a ticket

#### Internal Ticket
- Created an internal ticket

#### Offline Related
- Offline Internal: (When an agent replies from a mailer that received offline ticket notifications) the reply does not reach the requester and a message is added as an internal notification
  - This condition works when "Do not send replies to ticket recipients" is set in "Mail Settings"

![](/liveagent/scripts/file.php?view=Y&file=d705a19d07bdd2c1355e67383869bed4)

- Offline: A ticket was created from a chat offline message

#### Ticket Status
- Resolve: Resolved a ticket
- Spam: An agent or system marked a ticket as spam

### Ticket Creation Related

#### Initial Ticket Information
- Start Information: A new ticket was created via chat button/form/call button, or a new ticket was submitted by a user logged into the customer portal
  - Excludes email, phone calls, new ticket creation by agents, new internal tickets, new Twilio calls, forum topic creation, and new tweets

### Ticket Transfer

#### Transfer Related
- Transfer: Assigned a ticket to another agent (or team)
- Forward: Forwarded an email from a ticket
- Reply to Forward: Received a reply from the email forward destination of a ticket

### Other Operations

- Split: Split a ticket
- Postpone: Extended a ticket

### Social Media & External Service Related

- Facebook: A ticket was created from Facebook
- Knowledge Base: A ticket created from a forum topic or feedback was updated
- Knowledge Base Start: A new ticket was created from a forum topic or feedback

### Call Related

- Phone (Incoming): A ticket was created from an incoming phone call
- Phone Internal: This feature is not available in Japan
- Phone Outgoing: A ticket was created from an outgoing call made from LiveAgent

### Others

- Tag: A tag was added to a ticket
- Twitter: A ticket was created from Twitter
- Retweet: Retweeted from a ticket