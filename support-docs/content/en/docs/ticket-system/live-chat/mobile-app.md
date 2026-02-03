---
title: "Mobile App Chat and Inline Chat"
date: 2026-01-30
lastmod: 2026-01-30
draft: false
translationKey: "mobile-app"
description: "Using GET parameters opens the chat window in a browser (popup mode)."
keywords: ["chat", "mobile", "app", "LiveAgent", "email address"]
category: "ticket-system/live-chat"
---
## LiveAgent Chat Integration for Mobile Apps

### Using GET Parameters

Using GET parameters opens the chat window in a browser (popup mode).

#### Available GET Parameters

*cwid* - Required - The ID of the LiveAgent chat widget.

You can find it in the chat button integration script located at "*Settings" -> "**Chat" -> "Chat Buttons" -> "Edit Chat Button (click chat button name)" -> "Edit Chat Button" -> "Integration"*.

Here's an example of a widget ID with the value 71e8b44f.

function(e){ LiveAgent.createButton('71e8b44f', e); }); 

Available parameters:
- *firstName* - Customer's first name
- *lastName* - Customer's last name
- *phone* - Customer's phone number
- *email* - Customer's email address
- *note* - Note displayed when accepting chat (any text)
- *pt* - Subject displayed when accepting chat (any text)

#### Widget ID Usage Example

Example of a basic call using only the widget ID: [https://URL_to_LiveAgent/scripts/inline_chat.php?cwid=71e8b44f](https://localhost/scripts/inline_chat.php?cwid=71e8b44f)

### Chat Window Style Customization

The chat window style can be edited in the settings of the chat widget you want to use. You can also add your own styles with custom CSS code.

## How to Implement Inline Chat

### Direct Use of URL and Parameters

You can use the same URL and parameters directly in a browser to start a chat. It can be added as a link/button to websites or email templates. Chat pre-forms cannot be used with inline chat.

## Setting Up In-Page Chat

### Embedding Chat Window Using iframe

The chat window can be embedded in another element using the <iframe> tag. Chat starts automatically when the page loads, but chat pre-forms cannot be used in this case.

#### Implementation Example

<iframe src="https://URL_to_LiveAgent/scripts/inline_chat.php?cwid=widgetID" style="width: 350px;height: 450px;"></iframe>

Replace **"URL_to_LiveAgent"** with the correct LiveAgent URL (yourdomain.liveagent.jp) and **"widgetID"** with your chat button ID.