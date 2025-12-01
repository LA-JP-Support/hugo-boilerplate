---
title: "Conditional Router – Glossary & Deep Technical Reference"
translationKey: "conditional-router-glossary-deep-technical-reference"
description: "Learn about Conditional Routers: configurable nodes for dynamic data routing in AI workflows, automation, and software systems based on user-defined..."
keywords: ["conditional router", "dynamic routing", "AI workflow", "model selection", "conditional routing"]
category: "Glossary"
type: "glossary"
draft: false
---

## Definition

A **Conditional Router** is a configurable node, module, or component that directs each input—such as a message, data packet, API request, or conversation entity—to a single output path based on user-defined or AI-driven logic. It evaluates complex conditions using request parameters, metadata, context, or runtime data to decide the most suitable route. Conditional Routers are fundamental in intelligent workflow branching, model selection, dynamic conversation flows, and automated decision-making across AI, automation, and software systems.

---

## 1. What Is a Conditional Router?

A Conditional Router serves as the workflow-level equivalent of a programmable “if-else-if-else” or “switch-case” block, but with advanced capabilities and dynamic, data-driven routing. It is integral to:

- **Dynamic Routing:** Directing requests, messages, or data through different branches depending on evaluated conditions ([Haystack](https://docs.haystack.deepset.ai/docs/conditionalrouter), [FlowHunt](https://www.flowhunt.io/components/ConditionalRouter/)).
- **Complex Decision Logic:** Handling simple to highly-complex rules, including nested and logical operators.
- **Model and Resource Selection:** Choosing backend models/resources, or enforcing compliance-based routing.
- **Automation and AI:** Powering chatbots, LLM gateways, ETL/data orchestration, business process models, and dynamic workflow engines ([Frontline](https://help.getfrontline.ai/en/articles/10174140-understanding-conditional-routing-in-ai-agent-flows)).

**Analogy:**  
A Conditional Router can be thought of as a central “traffic controller” for automated systems, making real-time, context-aware decisions at every workflow juncture.

---

## 2. Feature and Component Breakdown

### Key Capabilities

- **Multiple Output Paths:** Inputs are evaluated, and each is routed to exactly one of several defined outputs.
- **Rule-Based or AI-Based Routing:** Supports deterministic rules as well as AI/NLP-powered semantic understanding ([Frontline](https://help.getfrontline.ai/en/articles/10174140-understanding-conditional-routing-in-ai-agent-flows)).
- **Complex Condition Support:** Conditions can use logical operators (`AND`, `OR`), comparison operators, regular expressions, and support for nesting.
- **Parameter and Metadata Evaluation:** Routing can reference input parameters, metadata fields, user context, API responses, or other runtime variables ([Haystack](https://docs.haystack.deepset.ai/docs/conditionalrouter#variables); [Portkey Docs](https://portkey-docs.mintlify.dev/docs/product/ai-gateway/conditional-routing)).
- **Default/Fallback Handling:** Ensures inputs are always routed, even if no specific conditions match.
- **Ordered Evaluation:** Conditions are checked in sequence; the first match determines the route ([Haystack](https://docs.haystack.deepset.ai/docs/conditionalrouter)).
- **Batch/List Handling:** Some platforms route each item in a batch independently (see [Gumloop router node](https://agenthub.mintlify.app/nodes/flow_basics/router)).
- **Model Selection and Override:** Dynamic backend selection, with ability to override model/parameters per route.
- **Type Preservation:** All input fields are preserved along the selected route; data integrity is maintained.

### Typical Parameters

| Parameter/Field        | Description                                                          | Required/Optional     |
|------------------------|----------------------------------------------------------------------|----------------------|
| `strategy.mode`        | Routing strategy, usually set to `conditional`                       | Required             |
| `conditions`           | Ordered list of condition/query objects                              | Required             |
| `default`              | Default output/target if no condition matches                        | Required             |
| `targets`              | List of named output targets with provider/config details            | Required             |
| `query`                | Condition logic referencing metadata/params/context                  | Required (per cond.) |
| `then`                 | Output/target name if condition passes                               | Required (per cond.) |
| `override_params`      | Parameter overrides for the target/model                             | Optional             |
| `output_name`          | (e.g., Haystack) Name(s) for output variable(s)                      | Required (per route) |
| `output_type`          | (e.g., Haystack) Data type(s) for route outputs                      | Optional             |
| `unsafe`               | (Haystack) Allows extended template output types                     | Optional             |

### Operator Support

| Operator   | Description                   |
|------------|------------------------------|
| `$eq`      | Equals                       |
| `$ne`      | Not equals                   |
| `$in`      | Value is in array            |
| `$nin`     | Value not in array           |
| `$regex`   | Matches regular expression   |
| `$gt`      | Greater than                 |
| `$gte`     | Greater than or equal to     |
| `$lt`      | Less than                    |
| `$lte`     | Less than or equal to        |

For a full list, see [Portkey Docs](https://portkey-docs.mintlify.dev/docs/product/ai-gateway/conditional-routing).

---

## 3. Step-by-Step Configuration & Implementation

### Example: JSON Configuration (Portkey)

```json
{
  "strategy": {
    "mode": "conditional",
    "conditions": [
      {
        "query": { "metadata.user_plan": { "$eq": "paid" } },
        "then": "finetuned-gpt4"
      },
      {
        "query": { "metadata.user_plan": { "$eq": "free" } },
        "then": "base-gpt4"
      }
    ],
    "default": "base-gpt4"
  },
  "targets": [
    {
      "name": "finetuned-gpt4",
      "provider": "@xx",
      "override_params": { "model": "ft://gpt4-xxxxx" }
    },
    {
      "name": "base-gpt4",
      "provider": "@yy",
      "override_params": { "model": "gpt-4" }
    }
  ]
}
```

### Setup Steps

1. **Define Routing Strategy**: Set `strategy.mode` to `conditional`.
2. **Specify Conditions**: Add ordered `conditions` objects with `query` and `then` fields.
3. **Set Default Output**: Define `strategy.default` as fallback route.
4. **Configure Targets**: List `targets` with unique `name` and provider details; optionally override parameters.
5. **Apply and Obtain Config ID**: Save configuration in the platform UI; copy the returned Config ID.
6. **Integrate in Requests**: Pass the Config ID with each request to enable routing.

More details: [Portkey Conditional Routing](https://portkey-docs.mintlify.dev/docs/product/ai-gateway/conditional-routing)

### Haystack Example

Haystack’s `ConditionalRouter` requires a list of routes, each with Jinja2 string expressions for conditions and outputs:

```python
routes = [
    {
        "condition": '{{ path == "rag" }}',
        "output": "{{ question }}",
        "output_name": "rag_route",
        "output_type": str
    },
    {
        "condition": "{{ True }}",  # fallback route
        "output": "{{ question }}",
        "output_name": "default_route",
        "output_type": str
    }
]

router = ConditionalRouter(
    routes=routes,
    optional_variables=["path"]
)
```
Source: [Haystack Documentation](https://docs.haystack.deepset.ai/docs/conditionalrouter)

---

## 4. Detailed Explanation of Conditions

### Syntax and Structure

Conditions can reference:

- `metadata.<key>`: Request metadata
- `params.<key>`: Input parameters
- `url.pathname`: Path-based routing

#### Supported Operators

- `$eq`, `$ne`, `$in`, `$nin`, `$regex`, `$gt`, `$gte`, `$lt`, `$lte`
- Logical operators: `$and`, `$or`
- Nested conditions are supported

#### Example: Nested Condition

```json
{
  "query": {
    "$and": [
      { "metadata.user_tier": { "$eq": "enterprise" } },
      { "params.temperature": { "$gte": 0.7 } }
    ]
  },
  "then": "creative-premium-target"
}
```

#### Example: Regex Condition

```json
{
  "query": {
    "metadata.email": { "$regex": "^.*@company\\.com$" }
  },
  "then": "internal-support"
}
```

- If a field is missing or type mismatched, the condition evaluates as `false`.
- For Jinja2-based routers (e.g., Haystack), all variables used in conditions must be set, or marked as “optional.”

See: [Haystack Variables](https://docs.haystack.deepset.ai/docs/conditionalrouter#variables)

---

## 5. Practical, Contextual Examples

### A. Model Selection Based on Input Parameter

Route LLM requests to different providers based on the `model` parameter.

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
  },
  "targets": [
    {
      "name": "smart-model",
      "provider": "@anthropic-vk",
      "override_params": { "model": "claude-3.5-sonnet" }
    },
    {
      "name": "fast-model",
      "provider": "@openai-vk",
      "override_params": { "model": "gpt-4o-mini" }
    },
    {
      "name": "balanced-model",
      "provider": "@openai-vk",
      "override_params": { "model": "gpt-3.5-turbo" }
    }
  ]
}
```

[Full details and code samples](https://portkey-docs.mintlify.dev/docs/product/ai-gateway/conditional-routing)

---

### B. User Tier-Based Routing

Premium users get advanced models, free users get cost-optimized models:

```json
{
  "strategy": {
    "mode": "conditional",
    "conditions": [
      { "query": { "metadata.user_tier": { "$eq": "premium" } }, "then": "premium-model" },
      { "query": { "metadata.user_tier": { "$eq": "free" } }, "then": "basic-model" }
    ],
    "default": "basic-model"
  },
  "targets": [
    { "name": "premium-model", "provider": "@openai-vk", "override_params": { "model": "gpt-4o" } },
    { "name": "basic-model", "provider": "@openai-vk", "override_params": { "model": "gpt-3.5-turbo" } }
  ]
}
```

---

### C. Support Ticket Triage (Gumloop)

Classify support tickets and route to relevant support queues:

- If ticket is urgent → Escalation
- If billing-related → Finance
- Otherwise → Standard Support

![Support Ticket Routing Example](https://mintcdn.com/agenthub/w1F7hfGEH4EChCiL/images/router_basic_example.png?fit=max&auto=format&n=w1F7hfGEH4EChCiL&q=85&s=196bee59769fa9a49b4c3de3a2cac1b0)

Example AI Routing (Gumloop):

```yaml
Route 1: "Urgent"
  AI Condition: "when the ticket expresses urgency or escalation requests"
Route 2: "Billing"
  AI Condition: "when the ticket mentions billing or invoices"
Route 3: "General"
  AI Condition: "all other cases"
```
[Workflow Example](https://gumloop.com/pipeline?workbook_id=2YiTXF7pcXBMgiaiSetQWT)

---

### D. Combined Metadata and Parameter Routing

Route to a creative model for enterprise users with high `temperature` settings.

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
  },
  "targets": [
    { "name": "creative-premium-target", "provider": "@anthropic-vk", "override_params": { "model": "claude-3-opus" } },
    { "name": "standard-target", "provider": "@openai-vk", "override_params": { "model": "gpt-3.5-turbo" } }
  ]
}
```

---

### E. Workflow ProcessModel Example

- If policy value ≤ $10,000 → Path A (simple processing)
- If policy value > $10,000 → Path B (complex processing)

Condition expressions:

- `a_Policy_Value <= 10000`
- `a_Policy_Value > 10000`

Source: [ProcessModel Conditional Route](https://www.processmodel.com/help/what-is-a-conditional-route/)

---

## 6. Best Practices and Troubleshooting

### Best Practices

- Use descriptive route/output names.
- Place specific conditions first, catch-all routes last.
- Always define a fallback/default route.
- Test with diverse and edge-case data.
- Start simple, add complexity gradually.
- Monitor logs to verify routing.
- Validate input data types and presence.
- Document complex logic.
- For AI-powered routes, provide clear prompt templates and choose robust models.

### Troubleshooting

- **No Route Matched:** Review fallback, check if conditions are too restrictive or misordered, inspect input data.
- **Input Type Mismatch:** Ensure all referenced fields exist and are of correct type.
- **List Size Mismatch (batch routing):** Match list lengths; use filter/duplicate nodes if needed.
- **Debugging:** Start with simple cases; use platform-specific run logs to trace routing.

See [FlowHunt best practices](https://www.flowhunt.io/glossary/ai-ethics/) and [Portkey troubleshooting](https://portkey-docs.mintlify.dev/docs/product/ai-gateway/conditional-routing).

---

## 7. Visuals and Workflow Diagrams

- **Support Ticket Routing Example:**  
  ![Router node](https://mintcdn.com/agenthub/w1F7hfGEH4EChCiL/images/router_basic_example.png?fit=max&auto=format&n=w1F7hfGEH4EChCiL&q=85&s=196bee59769fa9a49b4c3de3a2cac1b0)
- **Route Configuration Example:**  
  ![AI mode config](https://mintcdn.com/agenthub/w1F7hfGEH4EChCiL/images/router_ai_mode.png?fit=max&auto=format&n=w1F7hfGEH4EChCiL&q=85&s=6f72bc9c66684c25eaa6f6d296082bbb)
- **Workflow Example:**  
  [Support triage workflow (Gumloop)](https://gumloop.com/pipeline?workbook_id=2YiTXF7pcXBMgiaiSetQWT)

---

## 8. Operator & Field Reference Table

| Operator   | Meaning                      |
|------------|-----------------------------|
| `$eq`      | Equals                      |
| `$ne`      | Not equals                  |
| `$in`      | Value is in array           |
| `$nin`     | Value not in array          |
| `$regex`   | Matches regular expression  |
| `$gt`      | Greater than                |
| `$gte`     | Greater than or equal to    |
| `$lt`      | Less than                   |
| `$lte`     | Less than or equal to       |

| Field                | Description                              |
|----------------------|------------------------------------------|
| `strategy.mode`      | Routing mode (set to `conditional`)      |
| `conditions`         | List of routing conditions               |
| `default`            | Fallback output name                     |
| `targets`            | Output definitions and providers         |
| `output_name`        | Output variable name (Haystack)          |
| `output_type`        | Output data type (Haystack)              |

---

## 9. References and Further Reading

- [Portkey: Conditional Routing](https://portkey-docs.mintlify.dev/docs/product/ai-gateway/conditional-routing)
- [Gumloop: Router Node](https://agenthub.mintlify.app/nodes/flow_basics/router)
- [Haystack: ConditionalRouter](https://docs.haystack.deepset.ai/docs/conditionalrouter)
- [Frontline: Conditional Routing in AI Agent Flows](https://help.getfrontline.ai/en/articles/10174140-understanding-conditional-routing-in-ai-agent-flows)
- [FlowHunt: Conditional Router](https://www.flowhunt.io/components/ConditionalRouter/)
- [ProcessModel: Conditional Route](https://www.processmodel.com/help/what-is-a-conditional-route/)
- [AWS Glue: Conditional Router](https://docs.aws.amazon.com/glue/latest/dg/transforms-conditional-router.html)
- [LogicNets: Router Node](https://community.logicnets.com/t/m1hxg9l/router-node)
- [Haystack Routers API Reference](https://docs.haystack.deepset.ai/reference/routers-api)
- [Gumloop Community Forum](https://forum.gumloop.com)

---

## 10. Further Exploration and Use Cases

| Use Case                                    | Example Condition / Logic                                      |
|----------------------------------------------|---------------------------------------------------------------|
| Model selection based on request param       | `params.model == "smartest"` → Claude-3.5, else GPT-4o-mini   |
| User subscription tier                       | `metadata.user_tier == "premium"` → advanced model            |
| Compliance by region                         | `metadata.country == "EU"` → EU-hosted model                  |
| Ticket triage (AI content understanding)     | `ticket_description` contains "urgent" → escalation            |
| Batch processing (list routing)              | Each item routed individually                                 |
| Path-based routing                           | `url.pathname == "/admin/users"` → admin path                  |

- [Conditional Routing in
