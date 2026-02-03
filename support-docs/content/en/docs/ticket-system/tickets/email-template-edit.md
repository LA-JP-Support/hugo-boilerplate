---
title: "Editing Email Templates"
date: 2026-01-30
lastmod: 2026-01-30
draft: false
translationKey: "email-template-edit"
description: "To quickly respond to emails, LiveAgent allows you to create and store email templates in the system. There are two types of email templates: customer-facing and agent-facing."
keywords: ["templates", "email", "editing", "LiveAgent", "email address"]
category: "ticket-system/tickets"
---
## Overview of Email Templates

To quickly respond to emails, LiveAgent allows you to create and store email templates in the system. There are two types of email templates: customer-facing and agent-facing.

## Email Template Configuration

### Navigating to the Email Template Screen
From the agent screen left menu, select Settings > Email > Customer Templates

### Editing Customer Email Templates
- Select the email template you want to edit and click Edit
- To create team-specific templates, click the "+ Create Team-Specific Template" button
- Email configuration options:
  - Notify customers via email when tickets are resolved
  - Retrieve chat conversation logs

### Editing Email Body
- Select email template format (Plain Text or HTML)
- Using variables
  - Use variables like `{$firstname}`
  - Variables allow data insertion based on ticket conditions and assigned agents

### Important Notes When Editing Email Templates
- Backup the original template before editing
- Utilize "Quote Options"
- Use the "Test Send" function

## Email Template Variable List

### Available Merge Fields
| Data Type | Variable |
|-----------|----------|
| Server Information | Server date, Server time |
| Ticket Information | Ticket subject, Ticket code, Ticket ID, Ticket status, Ticket URL |
| Recipient Information | Recipient name (last/first), Recipient email address |
| Agent Information | Agent ID, Agent last/first name |
| Others | Message, Latest message from requester |

### Notes on Recipient Name Variables
- Names can be split into first and last names by separating with a half-width space
- Pay attention to variable order (first part is first name, latter part is last name)

## Editing Agent Templates
- The editing procedure for agent templates is the same as for customer templates
- Select the template you want to edit and click "Edit"