---
title: "API for Customer Portal (Knowledge Base/Suggestions)"
date: 2026-01-30
lastmod: 2026-01-30
draft: false
translationKey: "customer-portal-knowledge-base-suggestion"
description: "※ Compatible with LiveAgent version 4.7.3.0 and later."
keywords: ["Customer Portal", "Knowledge Base", "Knowledge", "Suggestions", "LiveAgent"]
category: "settings"
---
## Customer Portal API Reference

### Table of Contents
- [Knowledge Base Search](#knowledge-base-search)
- [Suggestion Categories List](#suggestion-categories-list)

### Knowledge Base Search

#### API Overview
- **Compatible Version**: LiveAgent version 4.7.3.0 and later

#### Request Method
GET `http://example.com/api/knowledgebase/search?query=[value]&apikey=[value]`

#### Required Parameters
| Parameter Name | Format | Content |
|--------------|------|------|
| query | text | Search query string |
| apikey | text | API key |

#### Optional Parameters
| Parameter Name | Format | Content |
|--------------|------|------|
| top_article_id | text | Top article ID. Start search from specified ID |

#### Response Fields
- `articles`: Knowledge base article list
  - `kb_entry_id`: Article ID
  - `urlcode`: Article URL ID
  - `title`: Title
  - See other detailed field references

#### Response Example
- XML and JSON format sample responses available

### Suggestion Categories List

#### API Overview
- **Compatible Version**: LiveAgent version 2.8.2.1 and later

#### Request Method
GET `http://example.com/api/suggestioncategories?apikey=[value]`

#### Required Parameters
| Parameter Name | Format | Content |
|--------------|------|------|
| apikey | text | API key |

#### Response Fields
- `suggestioncategories`: Suggestion categories list
  - `id`: Category ID
  - `title`: Category title
  - `path`: Category path

#### Response Example
- XML and JSON format sample responses available