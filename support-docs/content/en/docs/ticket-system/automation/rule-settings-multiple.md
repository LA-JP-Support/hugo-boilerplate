---
title: "Is there a way to register multiple condition keywords in rule settings?"
date: 2026-01-30
lastmod: 2026-01-30
draft: false
translationKey: "rule-settings-multiple"
description: "To register multiple keywords when creating rule application conditions, use the 'Matches regular expression' option in the condition settings. Please refer to the link below for detailed configuration instructions."
keywords: ["rules", "settings", "multiple", "items", "creation"]
category: "ticket-system/automation"
---
## Method for Registering Multiple Keywords

### Keyword Configuration Using Regular Expressions

When creating rule application conditions, regular expression functionality is convenient for registering multiple keywords in a single configuration item. Regular expressions are a powerful tool that allows advanced control over string pattern matching, enabling flexible condition specification in SmartWeb rule settings.

Specifically, by separating keywords with "|" (pipe), you can search for multiple keywords simultaneously. For example, by setting "apple|banana|orange", you can extract content that matches any of these three keywords.

#### Regular Expression Usage Examples
- Keywords: `sale|campaign|promotion`
- Matching strings: "Summer sale in progress", "Campaign ongoing", "Promotion information"

### Related Information

【Related Item】　How to set multiple keywords in one item when specifying conditions

By using regular expressions, you can create more complex search patterns and flexibly control the scope of rule application. It's important to find optimal settings through test operations.