---
title: "Customer Management in LiveAgent: 'Contacts' and 'Companies'"
date: 2026-01-30
lastmod: 2026-01-30
draft: false
translationKey: "liveagent-customer-management"
description: "LiveAgent ticketizes 'inquiries' from each communication channel while simultaneously acquiring and managing 'customer information' associated with tickets."
keywords: ["LiveAgent", "Agent", "customer", "email address", "agent"]
category: "settings"
---
## LiveAgent Customer Management: Basics of Contacts and Companies

LiveAgent ticketizes "inquiries" from each communication channel while simultaneously acquiring and managing "customer information" associated with tickets.

## Contacts: Basic Unit of Customer Information

### Automatic Contact Creation and Display
This "customer information" is displayed as "requester" in the upper right of the screen when expanding a ticket in the agent interface. LiveAgent calls this a "contact". Contacts are automatically created by reading only the information obtained from inquiry channels (email addresses, phone numbers, etc.). They can also be manually registered from within LiveAgent.

[The red frame in the figure below shows a "contact". Since it was created from a post to the user forum, the name (user ID) and email address are registered.]

![](/liveagent/scripts/file.php?view=Y&file=7be3be711e8ed55d2b9fa1ab7e8f31c6)

### Contact Tracking and Management
When the same customer makes another inquiry, the existing contact is automatically associated with the ticket. Therefore, searching and viewing tickets from each contact is also a possible use case.

### Contact Information Details
Contacts can be edited from the left menu in the agent interface via Settings > Contacts. The information that can be registered for contacts is as follows:

- Name
- Avatar
- Email address (multiple registration possible)
- Phone number (multiple registration possible)
- Group
- Time zone
- Language
- URL
- Address
- Text box (free description)

## Companies: Customer Management by Organization Unit

### Company Overview
LiveAgent contacts can also be grouped by organization, company, or other units. This grouping is called "companies". Unlike "contacts", "companies" are not automatically generated and must be registered from the agent interface.

### Company Information Registration
Companies can be created and edited by selecting "Settings" > "Companies" from the left menu in the agent interface. The information that can be registered is as follows:

- Customer company name
- Avatar such as company logo
- Email address (multiple registration possible)
- Phone number (multiple registration possible)
- Group
- Time zone
- Language
- URL
- Address
- Text box (free description)

![](/liveagent/scripts/file.php?view=Y&file=d1358c80e70b3d58b1e156e40e202b4c)

## Groups: Customer Classification and Automation

### Group Functions
"Groups" function as tags attached to customer information. They can be applied to both "contacts" and "companies". By creating and applying "groups", automation rules different from normal routing workflows can be applied to the automatic processing of tickets created by specific customers.

### Group Management
"Groups" can be created and edited from the left menu in the agent interface via "Settings" > "Automation" > "Contact Groups". Additionally, since "groups" are applied only in the editing screens of "contacts" or "companies", there is no worry of confusing them with ticket "tags" during inquiry handling.