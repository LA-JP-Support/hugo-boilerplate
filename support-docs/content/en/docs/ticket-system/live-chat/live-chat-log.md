---
title: "Can live chat conversation logs be exported?"
date: 2026-01-30
lastmod: 2026-01-30
draft: false
translationKey: "live-chat-log"
description: "Live chat conversation logs can be exported via API. Data formats are JSON or XML."
keywords: ["live chat", "chat", "log", "message", "ticket"]
category: "ticket-system/live-chat"
---
## Live Chat Conversation Log Export Methods

### Log Export Using API

SmartWeb's live chat system allows you to easily export conversation logs through the API. This feature enables customer support teams to efficiently manage customer interactions and perform detailed analysis and record-keeping. Using the API, you can flexibly retrieve real-time or historical conversation logs.

### Supported Data Formats

- JSON: JavaScript Object Notation format, lightweight and optimal for data exchange
- XML: eXtensible Markup Language format, suitable for structured data representation

### Specific Steps for Log Export

1. Obtaining API Authentication Key
   - Get a dedicated API authentication key from the SmartWeb dashboard
   - Set appropriate permissions in security settings

2. Creating API Request
   - Endpoint URL: `/api/v1/chat-logs`
   - Parameters:
     * Date range
     * Chat agent
     * Customer ID

3. Selecting Data Format
   - Specify JSON or XML format
   - Response includes the following information:
     * Message content
     * Sender information
     * Timestamp

### Benefits of Log Export

- Improved customer support quality
- Utilization for training and quality management
- Record retention for legal requirements and audit compliance

## Related Information

### Related API

Ticket-related API - Retrieving all conversation history messages