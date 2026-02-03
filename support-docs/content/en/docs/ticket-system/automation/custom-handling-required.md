---
title: "How to Tag Tickets That Require Urgent Response Based on Custom Field Values"
date: 2026-01-30
lastmod: 2026-01-30
draft: false
translationKey: "custom-handling-required"
description: "You can create rules to tag tickets when user inquiries submitted through forms are marked as requiring urgent response. This scenario provides guidance on how to set this up."
keywords: ["ticket", "custom", "required", "inquiry", "form"]
category: "ticket-system/automation"
---
## Overview
This explains how to create a rule that automatically tags tickets when user inquiries are marked as requiring urgent response.

## Prerequisites
### Creating Tags
Create a tag named "Urgent Response Required" in advance.

### Adding Custom Fields
#### Setting Custom Fields in Forms
1. Edit the form and add a new custom field.
2. Select "Checkbox" as the field type.
3. Enter a description.

#### Enabling the Field
Submit a test ticket from "Preview and Test" and add the custom field to the list of ticket fields.

## Creating Rules
### Rule Configuration
- Condition: "Urgent" checkbox is checked in the form's custom field
- Action: Add "Urgent Response Required" tag to the ticket

## Testing the Function
### Behavior When Creating Tickets
1. User submits form with urgent flag turned on
2. "Urgent Response Required" tag is automatically assigned when ticket is created

## Additional Information
### System Name Verification
- Value of isUrgent checkbox
- Displays Y (Yes) when checked