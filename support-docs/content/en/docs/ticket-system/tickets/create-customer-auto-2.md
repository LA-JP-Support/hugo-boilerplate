---
title: "How to Send Automatic Responses to Customers After Tickets Are Created"
date: 2026-01-30
lastmod: 2026-01-30
draft: false
translationKey: "create-customer-auto-2"
description: "LiveAgent makes it easy to create automatic responses using the rules feature."
keywords: ["tickets", "customers", "automatic", "LiveAgent", "inquiries"]
category: "ticket-system/tickets"
---
## Setting Up Automatic Ticket Responses in LiveAgent

### Basic Scope of Automatic Responses

LiveAgent makes it easy to create automatic responses using the rules feature.

Use different "Apply" settings depending on whether you want to use automatic responses for all new tickets (including tickets created from contact forms) or only for tickets created from emails:

- Ticket is created
- Ticket created from email

### Available Actions for Automatic Responses

There are two actions available for automatic response rules:

- Send answer (with option to maintain ticket status)
- Send mail (maintains ticket status by default)

### Precautions to Avoid Automatic Response Loops

When customers are using automatic responses, we recommend using the "send answer" action to avoid creating loops where automatic responses trigger each other.

The "send mail" action doesn't retain original message information, which can cause loops. Specifically, when a ticket is created, an automatic response email is sent but the status remains "New." If a customer replies to this automatic response email, it's received as a new ticket with a different ticket ID, triggering another automatic response email. This means if the customer has automatic response settings configured, an endless loop of automatic responses will occur, creating new tickets for each exchange.

### Ticket Status Management

Pay attention to the "Maintain ticket status" checkbox on the "send answer" action screen.

#### Keeping Ticket Status as "New"

When this checkbox is enabled, the ticket status remains "New" even after sending an automatic response email, marking it as a ticket that requires attention. If a customer replies to the automatic response email, the status remains "New" when received. Of course, the automatic response email won't be sent again. In most cases, this checkbox should be enabled.

#### Changing Ticket Status to "Answered"

When this checkbox is disabled, sending an automatic response changes the status to "Answered" (meaning it's been handled). Since it won't be marked as a ticket requiring attention, be careful about missing responses. This setting might be appropriate for cases where staff don't need to provide additional responses. This distinction is very important.

### Detailed Automatic Response Rule Configuration

These rules also allow you to set conditions where automatic responses only trigger for tickets created from specific contact forms, or add additional actions alongside automatic responses.