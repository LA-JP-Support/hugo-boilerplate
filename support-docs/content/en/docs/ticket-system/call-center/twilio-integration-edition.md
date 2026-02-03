---
title: "Integration with Twilio (Software Edition/Cloud Edition)"
date: 2026-01-30
lastmod: 2026-01-30
draft: false
translationKey: "twilio-integration-edition"
description: "Please refer to this page for configuration methods.**"
keywords: ["Twilio", "integration", "edition", "LiveAgent", "dashboard"]
category: "ticket-system/call-center"
---
## Twilio Integration Overview

### Service Overview
By integrating [cloud-based voice call service Twilio](http://twilio.kddi-web.com/) with [LiveAgent](http://liveagent.jp), telephone functionality becomes available.

### Usage Considerations
- Available for trial with trial account
- Cloud edition recommends alternative integration method
- Advanced features like IVR available

### Main Features
Even when customers use telephone lines (landlines, mobile phones, or IP phones), agents can receive and handle calls on PCs logged into LiveAgent. It's also possible to make outbound calls from LiveAgent through Twilio.

## Twilio Configuration Steps

### Acquiring Twilio Account

#### Trial Application
1. Access the Twilio website
2. Enter phone number for verification

#### Phone Number Acquisition
1. Select "Phone Numbers" from the Twilio management dashboard
2. Acquire your first Twilio number

### Twilio Webhook Configuration

#### Request URL Configuration
1. In the "Voice Calls" configuration screen, enter the request URL provided by LiveAgent
2. Save the settings

### API Credentials Acquisition
1. Click "Show API Credentials" on the dashboard
2. Obtain ACCOUNT SID, AUTH TOKEN, and phone number (Caller ID)

## LiveAgent Configuration

### Basic Configuration
1. Log in to LiveAgent as an agent
2. Open "Settings" → "Twilio" → "Twilio Integration" screen
3. Enter the acquired Twilio credential information

### Team Phone Configuration
1. Add outbound numbers
2. Enable number selection during outbound calls

## Important Notes

### Trial Account Limitations
- Outbound calls only possible to "verified phone numbers"
- Calls to other numbers are not possible

**【Important】**
Legacy Twilio webhook integration with LiveAgent ended support on June 30, 2023. Migration to Twilio SIP Trunk is recommended.