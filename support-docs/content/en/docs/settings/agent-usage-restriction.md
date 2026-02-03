---
title: "Restricting Agent Usage Environment by IP Address"
date: 2026-01-30
lastmod: 2026-01-30
draft: false
translationKey: "agent-usage-restriction"
description: "LiveAgent allows you to restrict the usage environment when support agents log into the agent panel by IP address. You can also specify using wildcards, address ranges, and subnet masks."
keywords: ["agent", "restriction", "usage", "LiveAgent", "Agent"]
category: "settings"
---
## IP Address Restriction Overview

LiveAgent allows you to restrict the usage environment when support agents log into the agent panel by IP address. You can also specify using wildcards, address ranges, and subnet masks.

## How to Configure IP Address Restrictions

### Login Restriction Setup Procedure

From the left menu of the agent panel, open "Settings" > "System" > "General" and scroll to the bottom of the page where you'll find the "Agent panel access" section. Enter the IP addresses from which agent login should be allowed. This functions as a whitelist for login restrictions. Click "Save" to complete the configuration.

### IP Address Specification Options

When entering multiple IP addresses, separate them with line breaks or commas. In addition to IP address specification (example: 192.168.1.1), wildcards (example: *.*.*.*), range specification (example: 1.1.1.1-1.2.1.1), and subnet masks (example: 192.168.0.0/16) are also supported.

![](/liveagent/scripts/file.php?view=Y&file=9e2a5125543d66648eea49550faf9cb8)

## Behavior When IP Address Restrictions Are Violated

After configuration, when login attempts are made from IP addresses outside the specified range, the following warning message will be displayed:

![](/liveagent/scripts/file.php?view=Y&file=5cf29837016274ee0e0ded12aae000ff)