---
title: "How to Set Multiple Keywords to a Single Item When Specifying Conditions"
date: 2026-01-30
lastmod: 2026-01-30
draft: false
translationKey: "multiple-items-settings"
description: "When specifying conditions for 'Rules' and setting multiple keywords to a single item, use 'matches regular expression'."
keywords: ["settings", "items", "multiple", "rules", "usage"]
category: "ticket-system/automation"
---
## Condition Specification for Rules Using Regular Expressions

When specifying conditions for "Rules" and setting multiple keywords to a single item, use "matches regular expression".

![](/liveagent/scripts/file.php?view=Y&file=1f2915508d402c20ff7d3efd1c0e8589)

### Basic Usage of Regular Expressions

#### Setting Positive Conditions
To set a condition that includes one keyword (positive), write:

/keyword/

For example, a condition that includes one keyword "A" in the subject would be /A/.

#### Setting Negative Conditions
To set a condition that does not include one keyword (negative), write:

/\[^keyword\]*/

For example, a condition that does not include one keyword "B" in the subject would be /\[^B\]*/.

※Backslashes or half-width yen symbols are used to escape special characters like "@" or half-width parentheses

### Condition Settings Using Multiple Keywords

#### Setting OR Conditions (Logical OR)
To include any of multiple keywords, write:

/keyword1|keyword2|keyword3|.../

Separate the keywords used for "or" conditions with pipe symbols ( | ).

Example: To include either A or B → /A|B/

#### Setting AND Conditions (Logical AND)
To include all of multiple keywords, write:

/^(?=.*keyword1)(?=.*keyword2).../

Example: To include both A and B → /^(?=.*A)(?=.*B)/

#### Negative Logical OR Conditions
To exclude any of multiple keywords, write:

/\[^keyword1\]*|/[^keyword2\]*|.../

Connect the keywords you want to exclude with pipe symbols.

Example: To exclude either A or B → /\[^A\]*|\[^B\]*/

#### Negative Logical AND Conditions
To exclude all of multiple keywords, write:

/\[^(?=.*keyword1)(?=.*keyword2)...\]*/

Example: To exclude both A and B → /\[^(?=.*A)(?=.*B)\]*/