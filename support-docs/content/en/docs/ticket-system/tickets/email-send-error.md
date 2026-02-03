---
title: "How to Receive Bounce Emails (Email Send Error Messages)"
date: 2026-01-30
lastmod: 2026-01-30
draft: false
translationKey: "email-send-error"
description: "When customers enter an incorrect email address in contact forms, replies from received tickets will not reach the customer. To receive bounce notification emails (MAILER-DAEMON or Mail Delivery Subsystem) that arrive in such cases, configuration is required on the LiveAgent side."
keywords: ["email", "error", "send", "LiveAgent", "email address"]
category: "ticket-system/tickets"
---
## What are Bounce Emails

When customers enter an incorrect email address in contact forms or similar, replies from received tickets will not reach the customer. To receive bounce notification emails (MAILER-DAEMON or Mail Delivery Subsystem) that arrive in such cases, configuration is required on the LiveAgent side.

## How to Configure Bounce Email Reception

### Email Settings Configuration

Go to "Settings" - "Email" - "Email Settings" and enable the following options:

- "Fetch bulk mail"
- "Fetch junk mail"
- "Fetch emails with blank return path"

![](/liveagent/scripts/file.php?view=Y&file=e84dedd16caf45232135bc34e68efbaa)

↓↓↓↓↓↓↓↓↓　You will now be able to receive bounce emails as tickets.

![](/liveagent/scripts/file.php?view=Y&file=bea368d388c7e89dad121a196b1528a6)

## Managing and Organizing Bounce Emails

### Tags and Rules Configuration

Additionally, by creating "Tags" and "Rules," you can sort them into ticket views (folders).

### Specific Configuration Steps

1. Go to "Settings" - "Automation" - "Tags" and create a tag with a name like [Bounce Email].

2. Go to "Settings" - "Automation" - "Rules" and create a rule like example 2 to automatically tag tickets.

![](/liveagent/scripts/file.php?view=Y&file=a78b5e58e35da5ce437e8afff802a234)

3. Create a ticket view (folder) like example 3 to sort tickets tagged with "Bounce Email."

![](/liveagent/scripts/file.php?view=Y&file=d8d3689d64c63299ac97317691fc7bfc)

## Benefits of Bounce Email Handling

This enables alternative measures such as contacting customers via phone or other methods when reply emails from tickets bounce back.