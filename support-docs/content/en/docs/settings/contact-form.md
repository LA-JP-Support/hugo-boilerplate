---
title: "Contact Form Configuration"
date: 2026-01-30
lastmod: 2026-02-03
draft: false
translationKey: "contact-form"
description: "Use LiveAgent's contact form to directly convert customer inquiries into tickets. Accept inquiries without exposing email addresses."
keywords: ["contact form", "inquiry form", "tickets", "LiveAgent"]
category: "settings"
weight: 50
---

## What is a Contact Form

A web form that can directly convert customer inquiries into tickets.

| Feature | Description |
|---------|-------------|
| **Automatic Ticketing** | Instantly register customer input as tickets |
| **Security** | Accept inquiries without exposing email addresses or phone numbers |
| **24/7 Availability** | Accept inquiries at any time |
| **FAQ Integration** | Automatically suggest related FAQs during input |

## Form Types

| Type | Description | Use Case |
|------|-------------|----------|
| **Inquiry Button** | Display form within page on button click | Site-wide inquiry acceptance |
| **Page Form** | Create dedicated inquiry page | When detailed information collection is needed |

## Form Gallery

Start using immediately by simply selecting from pre-prepared templates.

### Gallery Benefits

| Benefit | Description |
|---------|-------------|
| **Easy Implementation** | Simply select a template |
| **Branding** | Unified design and format |
| **Multiple Channels** | Set up purpose-specific forms for support, sales, etc. |

## Configuration Steps

### 1. Creating a Button

Create a new form from "Settings" → "Contact Forms" → "Create".

- Color style selection
- Customization with original images
- Language settings

### 2. Form Configuration

| Configuration Item | Content |
|-------------------|---------|
| **Title** | Form heading |
| **Logo** | Company logo display |
| **FAQ Display** | Integration with knowledge base |
| **Post-submission Message** | Content displayed upon completion |

### 3. Input Field Configuration

| Configuration Item | Content |
|-------------------|---------|
| **Team Selection** | Department selection for inquiries |
| **Custom Fields** | Additional input fields |
| **Required Fields** | Designation of mandatory input |

### 4. Design Customization

- Style and color adjustments
- Color tone settings to match site design

### 5. Installation on Website

Place the generated code before the `</body>` tag on your website.

```html
<!-- LiveAgent Contact Form -->
<script>...</script>
```

## Important Notes

| Item | Content |
|------|---------|
| **Local Files** | Cannot be displayed (web server required) |
| **SSL Support** | Dedicated configuration required for HTTPS environments |

## Related Information

- [Department Management](/docs/settings/department-management/) - Inquiry destination configuration
- [Email Templates](/docs/settings/email-template/) - Auto-reply configuration
