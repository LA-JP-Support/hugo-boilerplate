---
title: "Can SSL communication be used for chat and contact forms"
date: 2026-01-30
lastmod: 2026-01-30
draft: false
translationKey: "contact-form-ssl-usage"
description: "Input data sent from LiveAgent's standard widgets (live chat and contact form buttons, windows, etc.) transmits and receives data without encryption when communicating via HTTP protocol (website URLs starting with \"http://\")."
keywords: ["contact form", "chat", "form", "LiveAgent", "live chat"]
category: "ticket-system/live-chat"
---
## SSL Communication and LiveAgent Widgets

### The Need for SSL Communication
Input data sent from LiveAgent's standard widgets (live chat and contact form buttons, windows, etc.) transmits and receives data without encryption when communicating via HTTP protocol (website URLs starting with "http://").

To encrypt communication data, you need to implement either "make the widget script SSL-compatible" or "make the webpage where the widget is installed SSL-compatible".

## Methods for SSL Implementation

### Changing Widget Scripts to SSL
Change the following parts of the embedded script to SSL-compatible scripts.

The part after "URL_TO_LiveAgent" remains the same as the configured URL

- For cases using company servers or domain settings other than liveagent.jp, that server must be in an environment that can utilize SSL.

- With this method, only the contact form or chat frame window that pops up with the button uses SSL communication, so SSL communication indication will not appear in the browser URL. To confirm, you need to display information for the frame section.

`//URL_TO_LiveAgent/scripts/track.js

//URL_TO_LiveAgent/scripts/pix.gif`

↓　Add "https:" at the beginning

`https://URL_TO_LiveAgent/scripts/track.js

https://URL_TO_LiveAgent/scripts/pix.gif`

### Making the Entire Webpage SSL-Compatible
When you change all pages where widgets are placed to SSL webpages, communication using widgets will be automatically encrypted.

- This cannot be used if SSL is not configured for your website.

- With this method, SSL communication indication will appear in the browser URL.