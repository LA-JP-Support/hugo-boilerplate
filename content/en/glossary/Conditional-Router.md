---
title: "Conditional Router"
lastmod: 2025-12-18
translationKey: "conditional-router"
description: "A Conditional Router evaluates data against rules, directing it to specific routes. Essential for dynamic, rule-based branching in automation pipelines, AI chatbots, and software."
keywords: ["Conditional Router", "Workflow automation", "Rule-based branching", "AI chatbots", "Data routing"]
category: "General"
type: "glossary"
date: 2025-12-18
draft: false
---

## What Is a Conditional Router?

A Conditional Router is a workflow component or node that evaluates incoming data against one or more user-defined rules and directs the data to a specific downstream route based on which condition matches. Its purpose is to enable dynamic, rule-based branching in automation pipelines, AI chatbots, business process automation, and software architectures. Each output port corresponds to a possible routed outcome, determined by customizable rules using a variety of operators.

**Key Capabilities:**
- Receives input (text, structured objects, metadata, etc.)
- Applies user-defined conditions (e.g., `equals`, `contains`, `is_email`, `regex`)
- Activates exactly one output (route) per evaluation, except in some ETL contexts
- Supports deterministic, manageable flows in complex automations

## How the Conditional Router Works

### Core Logic

The Conditional Router compares incoming data to specified values or logical expressions using a set of configurable operators. Each condition is linked to a named output. The router checks conditions in order: the first `true` condition determines the output route. If no condition matches, the router triggers a default or fallback route (if configured).

**Single-path Routing:** Only one output is activated per evaluation (exclusive routing), except in some ETL frameworks.

**Configurable Rules:** Conditions are defined with operators and can reference multiple fields, including nested data.

**Extensible:** Supports logical composition, nested conditions, and custom expressions.

### Evaluation Sequence

1. **Input Reception:** Receives data and optional metadata or parameters
2. **Condition Evaluation:** Sequentially evaluates each defined condition using the configured operators
3. **Routing Decision:** First condition that evaluates to `true` determines the output
4. **Default Handling:** If no conditions match, data is sent to a default route (if defined)
5. **Downstream Processing:** Data is passed to the next component or action

## Inputs

Input parameters for Conditional Routers may vary by platform, but typically include:

| Input Name | Type | Description | Required |
|-----------|------|-------------|----------|
| Input Data/Text | String/Object | The primary data to evaluate | Yes |
| Match Value | String/Object | The value or expression to compare against | No |
| Operator | String | The comparison operator | Yes |
| Case Sensitive | Boolean | Enables case-sensitive comparisons | No |
| Metadata/Params | Object | Additional fields for routing | No |
| Message Object | Object | Payload to pass along the route | No |

## Available Operators

Conditional Routers support a wide variety of operators for flexible routing:

| Operator | Description | Example Usage |
|----------|-------------|---------------|
| `equals` / `$eq` | Value is equal to match | `"status" == "active"` |
| `not equals`/ `$ne` | Value is not equal to match | `"role" != "admin"` |
| `contains` | Value contains substring | `"hello@example.com" contains "@"` |
| `starts with` | Value starts with substring | `"prefix"` starts with "pre" |
| `ends with` | Value ends with substring | `"file.pdf"` ends with ".pdf" |
| `is empty` | Value is empty/null/undefined | `""` |
| `is not empty` | Value is not empty | `"not empty"` |
| `is_url` | Value matches URL format | `"https://..."` |
| `is_email` | Value matches email format | `"name@domain.com"` |
| `is_number` | Value is numeric | `123` |
| `$in` | Value is in array/list | `tier in ["pro", "enterprise"]` |
| `$nin` | Value not in array/list | `status not in ["error"]` |
| `$regex` | Value matches regular expression | `input matches /pattern/` |
| `$gt`, `$gte` | Greater than / greater or equal | `score >= 0.8` |
| `$lt`, `$lte` | Less than / less or equal | `temperature < 0.7` |

**Logical Operators:** `$and` (all conditions must be true), `$or` (any condition true)

## Outputs

Each Conditional Router node provides multiple output ports:

| Output Name | Trigger Condition | Output Data Type |
|-------------|-------------------|------------------|
| True Route | When condition evaluates to `true` | Message/Object |
| False Route | When condition evaluates to `false` | Message/Object |
| Custom Routes | Named outputs for each condition | Message/Object |
| Default Route | When no condition matches | Message/Object |

**Named Output Ports:** Each condition links to a named output.  
**Default Output:** Handles unmatched data.  
**Data Forwarding:** The original (or transformed) message/data is passed through the activated output.

## Advanced Configuration

### Logical Operators

To define multi-condition logic for a single route, use logical operators:

```json
{
  "query": {
    "$and": [
      { "metadata.user_type": { "$eq": "pro" } },
      { "params.model": { "$eq": "gpt-4" } }
    ]
  },
  "then": "pro_gpt4_target"
}
```

Supports `$and`, `$or`, and even nested logical blocks.

### Case Sensitivity

Configure whether string comparisons should be case-sensitive:
- `case_sensitive: true` for exact match
- `case_sensitive: false` for case-insensitive

## Practical Examples

### Example 1: Simple Text Match
Route user message to support if it contains the keyword "help", otherwise route to the bot.

```json
{
  "input_text": "I need help with my order",
  "match_text": "help",
  "operator": "contains",
  "case_sensitive": false
}
```

### Example 2: Parameter-Based Model Selection
Route requests to different models based on the `model` parameter.

```json
{
  "strategy": {
    "mode": "conditional",
    "conditions": [
      {
        "query": { "params.model": { "$eq": "fastest" } },
        "then": "fast-model"
      },
      {
        "query": { "params.model": { "$eq": "smartest" } },
        "then": "smart-model"
      }
    ],
    "default": "balanced-model"
  }
}
```

### Example 3: Data Validation
Route based on input length:

```python
routes = [
  {
    "condition": "{{ query|length > 10 }}",
    "output": ["{{ query }}", "{{ query|length }}"],
    "output_name": ["ok_query", "length"],
    "output_type": [str, int],
  },
  {
    "condition": "{{ query|length <= 10 }}",
    "output": ["query too short: {{ query }}", "{{ query|length }}"],
    "output_name": ["too_short_query", "length"],
    "output_type": [str, int],
  },
]
```

### Example 4: Combined Metadata and Parameter Routing
Route enterprise users with high creativity requests to a premium model.

```json
{
  "strategy": {
    "mode": "conditional",
    "conditions": [
      {
        "query": {
          "$and": [
            { "metadata.user_tier": { "$eq": "enterprise" } },
            { "params.temperature": { "$gte": 0.7 } }
          ]
        },
        "then": "creative-premium-target"
      }
    ],
    "default": "standard-target"
  }
}
```

## Typical Use Cases

### 1. Branching Logic
Direct users to different dialog or process paths based on intent, content, or attributes. Orchestrate automation workflows that diverge depending on event or message data.

### 2. Validation and Filtering
Enforce input validation (e.g., required fields, correct formats). Detect and filter spam or inappropriate content.

### 3. Personalization and User Segmentation
Route premium vs. free users to different flows. Implement A/B testing by allocating users to experimental branches.

### 4. Model Selection and Feature Flags
Select AI models dynamically based on user segment or request properties. Enable/disable features using configuration flags.

### 5. Access Control and Compliance
Ensure data routing based on region for regulatory compliance. Apply role-based access restrictions using metadata.

## Best Practices

**Order of Conditions**  
Place specific conditions before generic ones to prevent premature matches.

**Fail-Safe Defaults**  
Always configure a default output for unmatched data.

**Testing**  
Validate logic with test data to ensure correct routing; use logging and analytics to monitor routing decisions.

**Documentation**  
Comment or document complex conditions for maintainability.

**Security**  
Avoid unsafe template evaluation unless essential and inputs are trusted.

**Performance**  
Avoid excessive nesting or extremely complex conditions to keep routing fast and maintainable.

**No-Code Accessibility**  
Use platforms providing graphical or no-code interfaces for broader accessibility.

## Troubleshooting & FAQ

**Q: What happens if multiple conditions match?**  
A: Only the first matching condition (in order) is selected; subsequent matches are ignored. In some ETL tools, data can be routed to multiple outputs.

**Q: How do I route based on multiple fields?**  
A: Use logical operators (`$and`, `$or`) to combine conditions on multiple fields.

**Q: What if a referenced field is missing?**  
A: The condition usually evaluates to `false`, and the router proceeds to the next condition or default.

**Q: Can I use regex or advanced matching?**  
A: Yes, many routers support `$regex` or pattern-based operators.

**Q: Is this suitable for non-developers?**  
A: Many platforms offer no-code configuration.

**Q: Can I perform parallel routing?**  
A: Most routers are exclusive (single-path per evaluation). For parallel actions, use specialized multi-route or branching components.

## References

- [AWS Glue: Conditional Router](https://docs.aws.amazon.com/glue/latest/dg/transforms-conditional-router.html)
- [FlowHunt: Conditional Router](https://www.flowhunt.io/components/ConditionalRouter/)
- [Haystack: ConditionalRouter](https://docs.haystack.deepset.ai/docs/conditionalrouter)
- [Portkey AI: Conditional Routing](https://docs.portkey.ai/docs/product/ai-gateway/conditional-routing)
- [Portkey AI: Combined Routing with Multiple Conditions](https://docs.portkey.ai/docs/product/ai-gateway/conditional-routing#combined-routing-with-multiple-conditions)
- [Fluix: Conditional Logic Tutorial](https://fluix.io/help/conditional-logic-tutorial)
- [Slack: Conditional Branching Workflow Builder](https://slack.com/blog/news/conditional-branching-workflow-builder)
- [Slack: Guide to Slack Workflow Builder](https://slack.com/help/articles/360035692513-Guide-to-Slack-Workflow-Builder)
- [Frontline AI: Understanding Conditional Routing in AI Agent Flows](https://help.getfrontline.ai/en/articles/10174140-understanding-conditional-routing-in-ai-agent-flows)
- [Rapidomize: Conditional Routing](https://rapidomize.com/docs/services/router/)
- [FlowHunt: Live Demo](https://www.flowhunt.io/demo/)
- [Conditional Routing in Slack Workflow Builder (YouTube)](https://www.youtube.com/watch?v=3O4c7iYhD5Y)
- [How to Use Conditional Router in FlowHunt (YouTube)](https://www.youtube.com/watch?v=rgqX7Qj3QAo)
- [AWS Glue Conditional Router Tutorial (YouTube)](https://www.youtube.com/watch?v=90p4Vq8F9pQ)
