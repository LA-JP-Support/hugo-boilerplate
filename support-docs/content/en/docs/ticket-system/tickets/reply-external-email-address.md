---
title: "How to Re-send Ticket Reply Content to External Email Addresses (BCC)"
date: 2026-01-30
lastmod: 2026-01-30
draft: false
translationKey: "reply-external-email-address"
description: "While there is no function to automatically insert BCC into ticket replies, it is possible to configure rules to re-send to specified email addresses. Below shows an example of rule creation. Enter the destination email address in 'To'. The sender name is optional (default is 'System'). Variables can be used in the subject and body. In the example below, the subject uses '..."
keywords: ["email address", "ticket", "email", "message", "system"]
category: "ticket-system/tickets"
---
## Automatic BCC Configuration for Ticket Replies

### Overview
While there is no function to automatically insert BCC into ticket replies, it is possible to configure rules to re-send to specified email addresses.

### Rule Creation Steps

#### Email Address and Sending Configuration
Below shows an example of rule creation. Enter the destination email address in "To". The sender name is optional (default is "System").

#### Variable Configuration for Subject and Body
Variables can be used in the subject and body. The example below uses the following variables:
- Subject: "Ticket Subject" "Ticket ID"
- Body: "Message Text (← refers to email body)"

### Using Variables
A list of available variables is displayed within the rule creation screen.

### Configuration Screen Screenshot
![](/liveagent/scripts/file.php?view=Y&file=06dd5cb95b00320a1dc833d6732debbf)