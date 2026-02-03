---
title: "Smart Ticket Deletion and Restoration"
date: 2026-01-30
lastmod: 2026-01-30
draft: false
translationKey: "delete-restore"
description: "Tickets can be deleted from individual ticket screens. By selecting 'Delete' from the bottom menu of the individual ticket screen, the ticket will be removed from the ticket list."
keywords: ["Smart Ticket", "Ticket", "Delete", "LiveAgent", "Agent"]
category: "ticket-system/tickets"
---
## Ticket Deletion and Management

### Deleting Tickets
Tickets can be deleted from individual ticket screens. By selecting "Delete" from the bottom menu of the individual ticket screen, the ticket will be removed from the ticket list.

![](/liveagent/scripts/file.php?view=Y&file=3634330ea157a617c052687f5fd43089)

### Complete Ticket Purging Methods

Even after deleting tickets using the "Delete Ticket" function above, tickets are not completely purged from the system. There are two methods to purge (completely delete) tickets.

#### System Retention Period Settings
You can set the period before tickets are purged. The default setting is "30 days".

##### Procedure
Select "Configuration" > "System" > "General" from the left menu of the agent interface.

- Enter the desired retention period in days in the "Days" field, then click "Save".

![](/liveagent/scripts/file.php?view=Y&file=4d2117e8fcb627206ee66a8d4e852ada)

#### Manual Ticket Purging
You can also manually purge deleted tickets.

##### Procedure
Select "Search" > "Tickets", then click "Custom Search Conditions".

- In the search conditions under "Status", check only "Deleted", then click "Apply".

![](/liveagent/scripts/file.php?view=Y&file=27ae5a3eea02a2e28dfb763492bc6d0d)

- Deleted tickets will be displayed in the list.

- After selecting the tickets you want to completely delete, click "Purge" to remove the selected tickets from LiveAgent permanently.

### Ticket Restoration

Tickets that have not been purged can be restored to the agent interface ticket list.

#### Procedure
Select "Search" > "Tickets" from the left menu of the agent interface, then click "Custom Search Conditions".

- In the search conditions under "Status", check only "Deleted", then click "Apply".

![](/liveagent/scripts/file.php?view=Y&file=27ae5a3eea02a2e28dfb763492bc6d0d)

- Deleted tickets will be displayed in the list.

- After selecting the tickets you want to restore, click "Restore" to restore the tickets to the list screen.