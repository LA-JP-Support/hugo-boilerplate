---
title: "About the Agent 'Auto Pause' Feature"
date: 2026-01-30
lastmod: 2026-01-30
draft: false
translationKey: "agent-auto-pause"
description: "If agents leave their workstations without logging out or pausing, they will not respond to chat or phone calls, resulting in unanswered inquiries. The 'Auto Pause' feature addresses this issue."
keywords: ["agent", "pause", "about", "LiveAgent", "keyboard"]
category: "settings"
---
## Overview
If agents leave their workstations without logging out or pausing, they will not respond to chat or phone calls, resulting in unanswered inquiries. The "Auto Pause" feature addresses this issue.

## How Auto Pause Works

### Triggering Inactive States
When this feature is enabled, an "inactive time" timer begins the moment an agent stops being active in LiveAgent. Examples of such states include:

- No longer typing on the keyboard within the LiveAgent interface

- No longer clicking buttons or other elements within LiveAgent

- Making another application window active, etc.

### Auto Pause Conditions
If this state continues for 5 minutes AND the agent is unresponsive to LiveAgent events (such as not responding to incoming chats), the system will change that agent to a paused state. The LiveAgent interface will display the same screen as when an agent manually pauses themselves (offline).

### Important Notes
If no customer interactions are assigned to the agent, or if automatic assignment is not configured for incoming emails, this feature will not activate.

## Configuration Method
From the agent interface left menu, go to Settings > System > General, and enable (check) the "Auto Pause" checkbox.