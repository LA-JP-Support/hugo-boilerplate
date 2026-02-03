---
title: "About Live Chat Assignment Methods"
date: 2026-01-30
lastmod: 2026-01-30
draft: false
translationKey: "live-chat-howto-about"
description: "Live chat routing (assignment methods) to each agent (support representative) can be selected from four different methods."
keywords: ["live chat", "chat", "about", "agent", "online"]
category: "ticket-system/live-chat"
---
## Overview of Live Chat Assignment Methods

Chat routing (assignment methods) can be selected from four different methods for agents (support representatives).

Configuration is done from the agent screen left menu: Settings > Chat > Chat Settings.

![](/liveagent/scripts/file.php?view=Y&file=e41cb9c1f686b1eee4df643ff07722fe)

## Details of Chat Assignment Methods

### Random Assignment

New live chats are assigned randomly and evenly distributed to agents who are available for chat support.

### Priority Assignment

New live chats are assigned to agents according to their assignment priority order until that agent's chat capacity (slots) reaches the maximum number. For example, if an agent with a slot setting of "3" is handling 3 chats simultaneously, the next incoming new chat will be assigned to the agent with the next highest priority.

This setting is used in situations where "chat specialist" agents primarily handle chat inquiries, while other agents prioritize other channels while supporting the former agents.

### Load Balancing Assignment

New chats are assigned to the agent with the least number of active chats at that moment, following priority order. Assignment is also kept balanced among agents on average. This setting allows for load balancing of simultaneous connections. The load is also related to the number of simultaneous chats per agent.

### Ring All

When a new chat arrives, all available agents are called until someone responds.

## Chat Assignment Priority Settings

New incoming live chats that apply the above three types of assignment conditions are automatically assigned to online agents with higher priority (lower priority numbers) who have available chat slots.