---
title: "About Tag Reports"
date: 2026-01-30
lastmod: 2026-01-30
draft: false
translationKey: "tag-about"
description: "This is a report compiled based on 'tags' added to tickets. You can display report content by date, period, as well as by agent (assignee), team, and channel. Data reflected in the report starts measurement from the point when tags are used. Therefore, if tags are added after email replies or chats have ended, the tags..."
keywords: ["reports", "about", "tags", "LiveAgent", "agent"]
category: "ticket-system/reports"
---
## What are Tag Reports

Tag reports are compiled based on "tags" added to tickets. Detailed analysis is possible by date, period, agent, team, and channel.

### Important Notes When Using Reports

- Data measurement begins from the point when tags are used.
- If tags are added after email replies or chat completion, some items may not be reflected in the report.
- Unlike other LiveAgent reports, some items require advance configuration.

### Report Configuration Tips

To include tags added to tickets after completion in the aggregation, please add "Created Tickets" from the information type to the items.

## Detailed Tag Report Items

### Items Requiring Advance Configuration

#### Chat-Related Items
- **Chat Incoming**: Aggregates the number of incoming chats and invitation chats
- **Chats**: Aggregates the number of chat and invitation chat responses
- **Missed Chats**: Aggregates the number of unanswered incoming chats
- **Chat Pickup Average Time**: Average time from chat incoming to response start

#### Voice Call-Related Items
- **Incoming Calls**: Aggregates the number of incoming Twilio and voice conversation calls
- **Calls**: Aggregates the number of Twilio and voice conversation calls
- **Missed Calls**: Aggregates the number of missed Twilio and voice conversation calls
- **Call Duration**: Aggregates the duration of Twilio and voice conversations

#### Other Advance Configuration Items
- **New Reply Average Time**: Average time from ticket being "new" to becoming "replied"

### Items Not Requiring Advance Configuration

#### Basic Information
- **Tags**: Display of tag names

#### Report Aggregation Items
- **Replies**: Number of replies to tickets with added tags
- **Chat Messages**: Number of message responses in chats with added tags
- **Chat Average Time**: Average duration of chats with added tags
- **Unresolved Average Time**: Average time until tickets become "completed"

#### Evaluation-Related
- **Good Ratings/Good Ratings (%)**: Positive evaluations from customers
- **Bad Ratings/Bad Ratings (%)**: Negative evaluations from customers
- **No Rating/No Rating (%)**: Support responses without evaluations