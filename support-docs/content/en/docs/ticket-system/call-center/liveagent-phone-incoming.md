---
title: "Making and Receiving Phone Calls with LiveAgent"
date: 2026-01-30
lastmod: 2026-01-30
draft: false
translationKey: "liveagent-phone-incoming"
description: "The voice support service realized with LiveAgent includes"
keywords: ["LiveAgent", "Agent", "phone", "live chat", "call center"]
category: "ticket-system/call-center"
---
## Overview of LiveAgent's Phone Features

The voice support service realized with LiveAgent includes two types:

- **Phone calls** using Twilio, a cloud-based IP phone service
- Browser-based **voice conversations**

![](/liveagent/scripts/file.php?view=Y&file=7978391d804426a1145df705d13e5517)

Customers can make calls through regular phone numbers or initiate calls from buttons on websites. To use phone and voice conversation features, audio devices (microphone, speakers, headset, etc.) that can be connected to a PC are required.

**Related Topics:** Using voice call service "Twilio", Using PC-to-PC voice conversations

## Outbound Calls by Agents

### Making Calls from Tickets
From the ticket details screen, click **"Other"** > **"Twilio Call"** to make an outbound call from an agent to a customer.

![](/liveagent/scripts/file.php?view=Y&file=cbde1e026feebde430e33488365dc500)

### Making New Outbound Calls
When an agent makes a new outbound call, LiveAgent treats this as manually creating a new ticket. Select the **"New"** tab at the top of the agent screen, then click **"New Twilio Call"**. From the **"New Call"** tab, enter the phone number in the **"Destination"** field and click **"Call"** to start making the call.

*Note: If you get an error when dialing regular phone numbers (03-xxxx-xxxx), replace the leading "0" with "81" (81-3-xxxx-xxxx)*

![](/liveagent/scripts/file.php?view=Y&file=7ee9b1b29d5d7bad105cc3bb7c8ce9d4)

## Handling Incoming Calls by Agents
When receiving an incoming call from a customer, an alert screen appears on the agent's screen along with a ringtone. Click **"Answer"** on the alert screen to start the conversation with the customer.

![](/liveagent/scripts/file.php?view=Y&file=55975738b2fd330928ab7624a99b9c1a)

## Customer Phone Calls
When customers make or receive phone calls, no special operations are required. They can handle Twilio phone numbers just like regular phones.

## Phone Calls and Ticket Management
When a customer makes a phone call, LiveAgent routes the call to an available and appropriate agent. Calls received outside business hours go to voicemail, and LiveAgent creates tickets from the recorded voicemail audio data. When processing these tickets, you can handle them through regular email responses or call the customer back.

To use LiveAgent's phone features, you need to contract and configure a third-party IP phone provider [Twilio](http://twilio.kddi-web.com/). Additionally, fixed phone lines or IP phone services other than Twilio are not supported for service integration.

**Related Topics:** About tickets created from phone calls and voice conversations

## Business Benefits of Cloud Voice Call Services

- You can set up an advanced contact center anywhere in the world in just a few minutes. For example, you can operate call centers using local phone numbers in multiple languages for different regions.

- When customers call, they automatically enter a waiting queue. LiveAgent routes calls to available agents in order.

- All call audio is recorded and can be easily accessed and reviewed from tickets. Outside business hours, voicemail functionality automatically creates voice messages and tickets.

- Calls from websites can also use live chat simultaneously, preventing issues from misunderstandings.