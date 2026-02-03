---
title: "Raise SLA Level When Complaint Tag is Added"
date: 2026-01-30
lastmod: 2026-01-30
draft: false
translationKey: "tag-add-sla"
description: "When SLA (Service Level Agreement) functionality is in use, multiple conditions are often configured."
keywords: ["SLA", "level", "tag", "service level", "inquiry"]
category: "ticket-system/automation"
---
## Dynamic SLA Level Changes: Complaint Tag Integration Guide

SLA (Service Level Agreement) is often operated with multiple conditions configured. This article explains how to change SLA levels in conjunction with tag additions for high-priority inquiries such as complaints.

### Prerequisites
This configuration requires multiple steps.

### Tag Creation

#### Step 1: Complaint Tag Setup
1. Create a "Complaint" tag in advance under *"Settings" > "Automation" > "Tags"*.

### SLA Configuration

#### Step 2: Priority Response SLA Creation
1. Under *"Settings" > "Automation" > "SLA"*, create a "Priority Response" SLA with shorter response times than usual.

### Rule Configuration

#### Step 3: Automation Rule Construction
1. Under *"Settings" > "Automation" > "Rules"*, create the following rules:
   - Change the SLA level to "Priority Response" for tickets with the "Complaint" tag added
   - Raise the priority order for ticket handling

### Priority Order Operation

#### Impact of SLA Level Changes
Unlike normal SLA levels (e.g., respond within 6 hours), the "Priority Response" SLA has the following characteristics:

- Rearranges priority order regardless of chronological sequence
- Takes precedence over tickets with more than 30 minutes remaining response time
- Displays tickets with complaint tags at the top

This mechanism enables rapid response to urgent complaints.