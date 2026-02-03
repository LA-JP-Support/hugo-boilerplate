---
title: "How to Remove 'Login' and 'My Tickets' Links from Customer Portal Menu"
date: 2026-01-30
lastmod: 2026-01-30
draft: false
translationKey: "customer-portal-menu-login"
description: "Learn how to hide the 'Login' and 'My Tickets' menu items in the customer portal."
keywords: ["customer portal", "tickets", "portal", "LiveAgent", "tickets"]
category: "ticket-system/tickets"
---

## How to Hide Menu Links in Customer Portal

Learn how to hide the "Login" and "My Tickets" menu items in the customer portal.

### When Using the "Montana" Theme

Place the following CSS code in the **"Customer Portal" > "Settings" > "Customize Design" > "Design" > "Custom CSS"** section of your LiveAgent agent interface.

*.MenuLinkI, .MenuLinkT {
display:none;
}*

*.montana #menu-item-login, .montana #menu-item-mytickets {
display:none;
}*

![](/liveagent/scripts/file.php?view=Y&file=4e0a43663f2d7f33cf8f705c8546f9f8)

![](/liveagent/scripts/file.php?view=Y&file=ad15827eebfc47cc28c5d69ba6821b3a)

![](/liveagent/scripts/file.php?view=Y&file=4fa8dbf6342a504de7efd0016a4f93f1)

#### Hiding Ticket Submission

To also hide "Submit Ticket", go to **"Customer Portal" > "Settings" > Submit a Ticket** and configure the settings to prohibit ticket submission.

![](/liveagent/scripts/file.php?view=Y&file=941d96f873b974f9f38e647481e7ecee)

### When Using "Minimalist" or "Classic" Theme

Add the following 3 lines to "Custom CSS" to hide the box containing the menu items.

*.RightBox:first-child  {
display:none;
}*

## Important Notes

When switching to a different theme, you will need to reapply the custom CSS code, as each theme has its own custom CSS.