---
title: "Writing style definition"
translationKey: "writing-style-definition"
description: "--- title: "Conditional Router – Glossary & Deep Technical Reference" translationKey: "conditional-router-glossary-deep-technical-reference"..."
keywords: ['Writing style definition', 'AI Chatbots', 'Automation', 'Customer Support']
category: "AI Chatbot & Automation"
type: "glossary"
draft: false
---

---
title: "Conditional Router – Glossary & Deep Technical Reference"
translationKey: "conditional-router-glossary-deep-technical-reference"
description: "Learn about Conditional Routers: configurable nodes for dynamic data routing in AI workflows, automation, and software systems based on user-defined or AI-driven logic."
keywords: ["conditional router", "dynamic routing", "AI workflow", "model selection", "conditional routing"]
category: "Glossary"
type: "glossary"
draft: true
---




# Writing style definition

***

## **Copywriter Task Definition: Writing Style and Structure for "Conditional Router" Articles**

---

**Content Type:**  
Technical product documentation and glossary/reference articles with practical configuration guides and example-driven explanations.

**Search Intent & Document Purpose:**  
- **Search Intent:** Informational and practical—users seek to understand what a "Conditional Router" is, how it works, and how to implement it in AI, automation, or dev workflows.
- **Document Intent:**  
  - Define the Conditional Router concept clearly.
  - Explain configuration and implementation details step-by-step.
  - Provide practical, real-world use cases and code/config examples.
  - Guide users on best practices, troubleshooting, and model selection.
  - Reference specific platforms or frameworks when appropriate.

---

**Writing Style and Structure Guidelines**

**Structure:**  
1. **Clear, Concise Introduction**
   - State what a Conditional Router is and its role.
   - Example: “A Conditional Router node enables intelligent routing of data or requests to one of several outputs based on user-defined or AI-driven rules.”

2. **Feature/Component Breakdown**
   - Use bullet points or short sub-sections to list key capabilities, parameters, or options.
   - Example: “Key features include: multiple conditional outputs, support for rule-based or AI-based routing, and default/fallback handling.”

3. **Step-by-Step Configuration/Implementation**
   - Numbered or bulleted steps for setting up the router, with explicit reference to UI fields, JSON/config objects, or code snippets.
   - Include code/config samples in fenced blocks.
   - Example:  
     ```
     {
       "strategy": {
         "mode": "conditional",
         "conditions": [ ... ],
         "default": "target_1"
       },
       "targets": [ ... ]
     }
     ```
   - Call out required vs. optional fields.

4. **Detailed Explanation of Conditions**
   - Explain syntax for conditions (operators, logical structure).
   - Example: “Conditions support operators such as $eq (equals), $gt (greater than), $and, $or, and regular expressions.”

5. **Practical, Contextual Examples**
   - Provide real-world scenarios (e.g. support ticket triage, user plan-based routing, parameter-based routing).
   - Use “Example:” or “Sample Config:” labels.
   - Include both configuration and usage code in context.

6. **Best Practices and Troubleshooting**
   - Use checklists or bullet points for best practices, common pitfalls, and debugging.
   - Explicitly mention order of conditions, fallback/default routes, and importance of testing with edge cases.

7. **Visuals and Links**
   - Where relevant, reference or embed illustrative diagrams, screenshots, or external links.
   - Example: “See [full workflow example](https://gumloop.com/pipeline?workbook_id=2YiTXF7pcXBMgiaiSetQWT) for support request triage.”

8. **Summary Table or Quick Reference (Optional)**
   - Provide a table of supported operators, configuration fields, or a step summary.

9. **References and Further Reading**
   - Link to official documentation, guides, or example repositories at the end or within context.

---

**Stylistic Tone and Language:**
- **Concise, Direct, and Technical:** Prioritize clarity and brevity, avoiding unnecessary filler.
- **Instructional and Action-Oriented:** Use imperative verbs for steps, e.g., “Set the strategy mode to ‘conditional’. Save the config and obtain the Config ID.”
- **Use of Formatting:**  
  - Bold for key terms: **condition**, **default**, **metadata**.
  - Inline code style for parameter names, operators, and code references: `params.model`, `$eq`.
  - Headings and subheadings for logical separation.
  - Lists and tables for clarity.

- **Contextual Explanations:**  
  - Explain the “why” behind configuration choices and best practices.
  - Clarify technical details, e.g., “Only primitive types are supported for parameter routing.”

---

**Examples Showcasing Style:**

> “The Conditional Router acts as a decision point, directing data to one of several paths based on pre-defined rules or AI model outputs. Think of it as an advanced ‘if-else’ logic node, capable of evaluating complex conditions using metadata, request parameters, or context variables.”

> “To configure a conditional router:
> 1. Define your routing strategy as ‘conditional’ in the config.
> 2. Specify an ordered list of conditions, each referencing metadata or request parameters.
> 3. Assign a default target for unmatched cases.
> 
> Example Condition:
> ```
> { "query": { "metadata.user_plan": { "$eq": "paid" } }, "then": "finetuned-gpt4" }
> ```”

> “Best Practice: Always add a fallback route as the last condition to handle unmatched cases and avoid dropped requests.”

---

**Sample Links to Reference for Source-Backed Content & Examples:**
- [Portkey: Conditional Routing](https://portkey-docs.mintlify.dev/docs/product/ai-gateway/conditional-routing)
- [Gumloop: Router Node](https://agenthub.mintlify.app/nodes/flow_basics/router)
- [Haystack: ConditionalRouter](https://docs.haystack.deepset.ai/docs/conditionalrouter)
- [Frontline: Conditional Routing in AI Agent Flows](https://help.getfrontline.ai/en/articles/10174140-understanding-conditional-routing-in-ai-agent-flows)
- [LogicNets: Router Node](https://community.logicnets.com/t/m1hxg9l/router-node)
- [ProcessModel: Conditional Route](https://www.processmodel.com/help/what-is-a-conditional-route/)
- [AWS Glue: Conditional Router](https://docs.aws.amazon.com/glue/latest/dg/transforms-conditional-router.html)

---

**Prompt for LLM Model:**

> Write a technical documentation article or glossary entry on "Conditional Router" for an AI workflow or automation platform.  
> - Begin with a concise definition and role of a Conditional Router.  
> - Break down its capabilities and configurable options using bullet points or tables.  
> - Provide step-by-step setup instructions, with code/configuration samples and explicit requirements.  
> - Explain how to write and order conditions, supported operators, and logical constructs, using code examples.  
> - Illustrate real-world use cases relevant to the target audience (AI chatbot routing, user-tier-based model selection, etc.) with config and usage code.  
> - List best practices and troubleshooting tips in checklist format.  
> - Reference visuals, workflow diagrams, or external documentation links as appropriate.  
> - Keep language clear, direct, and technical; use formatting for clarity (bold, inline code, headings, lists).  
> - Where relevant, conclude with further reading or links to platform-specific guides.

---

By following this structure and style, the resulting articles will match the technical clarity, actionable detail, and practical focus found in leading documentation from Portkey, Haystack, Gumloop, and similar AI automation platforms.


| Keyword | Score |
| --- | --- |
| multiple conditions | 304.59 |
| simple conditional | 283.50 |
| routing based | 237.66 |
| conditional routing routing | 227.81 |
| conditional routing condition | 157.69 |
| specific conditions | 152.30 |
| model selection | 126.56 |
| conditional router | 121.50 |
| setting conditions | 101.25 |
| based routing | 84.50 |
| router node | 83.19 |
| creating conditional | 75.00 |
| condition query | 56.25 |
| decisions require | 54.19 |
| default output | 49.00 |
| route based | 45.38 |
| based decisions | 42.19 |
| required inputs | 42.19 |
| fallback route | 36.75 |
| connect router | 36.75 |



# Conditional Router – Glossary & Deep Technical Reference

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
