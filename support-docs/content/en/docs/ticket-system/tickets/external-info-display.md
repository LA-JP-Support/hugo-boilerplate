---
title: "Display External Information in Tickets"
date: 2026-01-30
lastmod: 2026-01-30
draft: false
translationKey: "external-info-display"
description: "Since version 4.25.6.4, LiveAgent has added a plugin called 'Display External Information in Tickets' that allows agents to load data from external servers or applications when opening tickets. As some development skills are required to create connections, this plugin becomes a very useful tool for agents to find detailed information about external systems."
keywords: ["ticket", "information", "display", "LiveAgent", "agent"]
category: "ticket-system/tickets"
---
## Display External Information in Tickets Plugin Overview

Since version 4.25.6.4, LiveAgent has added a plugin called "Display External Information in Tickets" that allows agents to load data from external servers or applications when opening tickets. As some development skills are required to create connections, this plugin becomes a very useful tool for agents to find detailed information about external systems.

### Plugin Use Cases

For example, by calling an e-commerce system's API to list the last orders of the customer the agent is currently communicating with, agents can directly check what the customer ordered in their store within the LiveAgent backend. The plugin's possibilities are extensive and can save many unnecessary clicks for your agents.

## Plugin Activation and Configuration

You can enable and configure the plugin by going to **"Configuration" -> "System" -> "Plugins"** in the LiveAgent agent login screen. There, click "Enable" next to **"Display External Information in Tickets"**. Once the plugin is activated and the application is reloaded, return to the plugin section and click the "Configure" button to actually configure the plugin.

### How the Plugin Works

What the plugin does is essentially load the content of the target URL via iframe and display it in the ticket sidebar within the application under a small "cloud" icon in the ticket section.

## Plugin Configuration Details

### Display Method Selection

The display method is used to select how the script content is displayed to agents. There are two options:

- **Proxy Request via LiveAgent** - If you choose the proxy method, the script is loaded by the LiveAgent server and only the actual content is displayed to the agent, so there is no way for the agent to obtain the script's URL that displays the content.

- **Load Directly in Agent's Browser** - If you are not concerned about agents being able to catch the script's URL, you can easily use this option.

### URL Configuration

**"Url"** should contain the URL address to the custom script that will be called when an agent opens a ticket and navigates to the custom plugin section. You can construct the URL using variables as needed.

Example: `https://mydomain.com/info.php?customer={$contact_email}&customer_phone={$contact_phone}`

### HTTP Method and Request Body

**HTTP Method** determines how to send HTTP requests to the specified URL address, whether using GET or POST methods.

The **Request Body** field is only used when POST is selected as the HTTP request method and is used to construct POST requests and include any available LiveAgent variables you want to use in your custom script.

Example: `ticket = {$ conv_conversationid}&subject = {$ conv_subject}`

### HTTP Authentication

**HTTP Authentication User** and **HTTP Authentication Password** are used when your script is protected with .htaccess HTTP authentication. This allows the application to authenticate itself when displaying content.