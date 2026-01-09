---
title: Scenarios (Pre-Prepared Conversation Flows)
lastmod: 2025-12-18
date: 2025-12-18
translationKey: scenarios-pre-prepared-conversation-flows
description: "A pre-written conversation blueprint that guides how a chatbot responds to users and performs actions to achieve specific business goals."
keywords:
- scenario
- chatbot
- automation
- conversation flow
- AI
category: AI Chatbot & Automation
type: glossary
draft: false
---

## What Are Scenarios?

A <strong>scenario</strong>(also called a chatbot script, bot story, or conversation flow) is a pre-prepared, structured sequence of interactions between a user and an AI-powered automation system. Scenarios define the complete path of a conversation, including the logic, branching, data collection, and actions that guide how a chatbot responds to user input and executes operations to achieve specific outcomes.

Scenarios are the operational backbone of modern chatbot and automation platforms, translating business requirements into executable conversation flows. They are constructed using visual or code-based workflow builders where modular blocks—representing events, actions, conditions, and exits—are connected to create dynamic, context-aware experiences across digital channels including web chat, mobile apps, messaging platforms, and voice interfaces.

## Scenarios vs. User Stories vs. Use Cases

Understanding the relationship between these related concepts is essential for effective scenario design:

| Aspect | Scenario | User Story | Use Case |
|--------|----------|------------|----------|
| <strong>Definition</strong>| Executable conversation flow with specific steps, logic, and actions | Brief feature description from user perspective (Agile format) | Comprehensive specification of all system interactions |
| <strong>Format</strong>| Visual workflow or flowchart with blocks, branches, conditions | Text card: "As a [user], I want [goal], so that [benefit]" | Detailed text with main/alternate flows and error handling |
| <strong>Detail Level</strong>| Step-by-step implementation with specific actions and responses | High-level, abstract | Comprehensive, covering all variations |
| <strong>Purpose</strong>| Guide actual automated conversation or process execution | Capture requirement or feature to implement | Specify complete system requirements |
| <strong>Focus</strong>| User behavior and system automation in practice | User need and desired outcome | System behavior and responses |
| <strong>Audience</strong>| Chatbot builders, automation engineers | Product owners, development teams | System analysts, developers, QA |
| <strong>Granularity</strong>| Operational (what actually happens) | Strategic (what should be built) | Tactical (how system should behave) |

<strong>Example Comparison:</strong>

<strong>User Story:</strong>```
As a new visitor, I want to get product support
so that I can resolve my issue quickly.
```

**Use Case:**```
Title: Get Product Support
Actor: New Visitor
Main Flow:
1. User requests support
2. System identifies issue category
3. System provides solution
4. User confirms resolution
Alternate Flows:
- 2a. Category unclear → Ask clarifying questions
- 3a. Solution not available → Escalate to agent
```

<strong>Scenario:</strong>```
[Entry Gate]
→ [Event: New User Message]
→ [Send Message: "How can I help you today?"]
→ [Event: Button/Input Action]
→ [Condition: Intent = "Product Support"]
  → If True: [AI Action: Search Knowledge Base]
  → [Send Message: Solution + "Did this help?"]
  → [Event: Button Click]
    → If "Yes": [Send Message: "Great! Anything else?"]
    → If "No": [Action: Assign to Agent]
```

## Scenario Structure: Building Blocks

Scenarios are composed of interconnected **blocks**, each representing a discrete function:

### Block Type Overview

| Block Type | Purpose | Key Characteristics |
|------------|---------|---------------------|
| **Entry Gate**| Marks scenario starting point | Required for scenario activation |
| **Event Blocks**| Listen for triggers to pause/resume flow | User messages, button clicks, data updates |
| **Action Blocks**| Execute operations | Send messages, update data, call APIs |
| **Condition Blocks**| Evaluate data to branch flow | If-then logic, data comparisons |
| **Exit Blocks**| End or hand off scenario | Stop or launch another scenario |

### Entry Gate

**Function:**Defines the beginning of a scenario flow.

**Critical rule:**Every executable scenario must begin with an Entry Gate. Without it, the scenario cannot be activated or executed.

**Visual representation:**Typically shown as a distinctive icon or shape at the top of the workflow canvas.

### Event Blocks: Triggers and Listeners

Event blocks pause scenario execution and wait for specific triggers:

| Event Type | Trigger | Common Use |
|------------|---------|------------|
| **New User Message**| Any incoming message (text, image, file) | Universal message handler |
| **User Message Matches**| Keyword/phrase/intent patterns | Topic-specific flows |
| **Button/Input Action**| User clicks button or submits input | Form submissions, choices |
| **Conversation State Changed**| Status update (pending, resolved, etc.) | Workflow state management |
| **User Profile Updated**| Changes to user data fields | Personalization triggers |
| **Custom Data Updated**| Specific backend field changes | Data-driven automation |
| **Segments Updated**| User/conversation segment changes | Audience targeting |
| **URL Change Detected**| Navigation to specific page | Contextual assistance |
| **New Crisp Event**| Programmatic trigger via SDK/API | Integration events |
| **Awaiting Operator**| Unread message timeout | Escalation scenarios |

**Pattern Matching:**- **Exact match:**"reset password" (precise phrase)
- **Wildcard:**"*refund*" (contains word anywhere)
- **Multiple patterns:**"help|assist|support" (any variant)

**Critical Note:**After collecting user input (Field Input, Button Picker), always place an Event Block to capture the response and store the value. Without this, the scenario cannot properly pause, resume, and process user input.

### Action Blocks: Executing Operations

Action blocks perform specific operations within scenarios:

| Action Category | Block Types | Purpose |
|----------------|-------------|---------|
| **Send Message**| Text, Button Picker, Field Input, File, Animation, Carousel, Note | Display content to user |
| **Update User**| Email, Name, Phone, Custom Fields, Segments | Modify user profile data |
| **Conversation Control**| Change State, Assign Operator, Block User | Manage conversation lifecycle |
| **Integration**| Run Webhook, HTTP Request, Custom API | Connect to external systems |
| **AI Operations**| Intent Analysis, Knowledge Base Search, Dynamic Reply | Leverage AI capabilities |
| **Flow Control**| Delay, Wait, Set Variable | Manage timing and data |

**Send Message Types:**

**Text Message:**```
Plain text or formatted content with variables:
"Hello {{user_name}}, your order #{{order_id}} has shipped!"
```

<strong>Button Picker:</strong>```
Message: "How would you like to proceed?"
Buttons: 
  - "Check Order Status"
  - "Speak to Agent"
  - "Browse FAQs"
```

**Field Input:**```
Type: Email
Label: "Please provide your email address"
Required: Yes
Validation: Email format
Store in: user.email
```

<strong>Carousel:</strong>```
Display multiple cards with images, text, and buttons
Use case: Product showcase, feature comparison
```

### Condition Blocks: Branching Logic

Condition blocks evaluate data or context to direct flow:

| Condition Type | Evaluation | Branch Logic |
|---------------|------------|--------------|
| **Conversation Status**| New, pending, resolved | Route by state |
| **Time-Based**| Time passed since event | Delay-triggered actions |
| **User Data**| Email set, name exists, segment membership | Personalization paths |
| **Custom Data**| Any custom field value | Business logic branching |
| **Message Intent**| AI-detected user intent | Intent-based routing |
| **API Response**| HTTP status, response values | Integration-driven flow |
| **User Metadata**| Location, language, device, time of day | Context-aware branching |

**Example Condition Structure:**```
[Condition: User Email is Set]
  → If TRUE:
    [Send Message: "Thanks {{user_name}}, we'll follow up at {{user_email}}"]
  → If FALSE:
    [Send Message: "Please provide your email"]
    [Field Input: Email]
```

### Exit Blocks: Ending or Transitioning

Exit blocks control how scenarios conclude:

<strong>Stop Scenario:</strong>- Terminates current flow completely
- Returns control to main chat system
- Use when objective achieved or error encountered

<strong>Run Scenario:</strong>- Launches another scenario
- Enables modular, reusable flows
- Supports scenario chaining for complex workflows

<strong>Example Modular Design:</strong>```
Scenario A: Lead Qualification
  → [Exit: Run Scenario B "Email Collection"]
  
Scenario B: Email Collection
  → [Collect email, validate, store]
  → [Exit: Run Scenario C "Meeting Scheduler"]
```

## Scenario Creation Process

### Step-by-Step Methodology

| Phase | Activities | Deliverables |
|-------|-----------|--------------|
| **1. Define Objective**| Clarify goal, audience, success criteria | Objective statement, requirements |
| **2. Map User Journey**| Document steps, decision points, edge cases | Flow diagram, user personas |
| **3. Build Structure**| Add Entry Gate, Events, Actions, Conditions, Exits | Visual workflow |
| **4. Configure Blocks**| Set parameters, patterns, variables, conditions | Detailed block configuration |
| **5. Test Thoroughly**| Simulate all paths, edge cases, error handling | Test results, bug reports |
| **6. Iterate and Refine**| Gather feedback, optimize performance | Updated scenario |

### Configuration Best Practices

**Event Configuration:**- Set appropriate message origins (channels)
- Use specific patterns for better matching
- Enable memorization to store collected data
- Consider multilingual requirements

**Action Configuration:**- Use variables for personalization: `{{user_name}}`
- Set clear button labels and actions
- Validate input fields (email format, phone number)
- Provide helpful error messages

**Condition Configuration:**- Keep logic simple and readable
- Plan for all possible outcomes
- Handle edge cases (missing data, invalid input)
- Document complex condition reasoning

**Integration Configuration:**- Securely store API credentials
- Handle timeouts and errors gracefully
- Log integration calls for debugging
- Test with real data and endpoints

## Practical Examples and Use Cases

### Example 1: Email Collection Scenario

**Objective:**Capture user email during conversation

**Flow:**```
[Entry Gate]
↓
[Send Message: "Welcome! May I have your email for follow-up?"]
↓
[Field Input: Email (required, validated)]
↓
[Event: Button/Input Action] ← Critical: captures the input
↓
[Update User: Set email field]
↓
[Condition: User Email is Set]
  → If TRUE:
    [Send Message: "Thank you! How may I assist you?"]
  → If FALSE:
    [Send Message: "Invalid email. Please try again."]
    [Loop back to Field Input]
```

<strong>Key Features:</strong>- Input validation
- Data storage
- Confirmation feedback
- Error handling

### Example 2: FAQ Resolution Scenario

<strong>Objective:</strong>Automatically answer common questions

<strong>Flow:</strong>```
[Entry Gate]
↓
[Event: User Message Matches "*refund*|*return*"]
↓
[AI Action: Search Knowledge Base query="refund policy"]
↓
[Condition: Knowledge Base Result Found]
  → If TRUE:
    [Send Message: {{kb_answer}}]
    [Button Picker: "Did this help?" Options: Yes/No]
    [Event: Button Click]
      → If "Yes": [Send: "Great! Anything else?"]
      → If "No": [Action: Assign to Agent]
  → If FALSE:
    [Send Message: "Let me connect you with a specialist."]
    [Action: Assign to Agent queue="Customer Service"]
```

**Key Features:**- Pattern matching with wildcards
- AI-powered knowledge retrieval
- User satisfaction check
- Escalation path

### Example 3: Multichannel Welcome Scenario

**Objective:**Greet users differently based on channel

**Flow:**```
[Entry Gate]
↓
[Event: New User Message]
↓
[Condition: Conversation is New]
  → If TRUE:
    [Condition: Current Channel]
      → If "WhatsApp":
        [Send: "👋 Welcome to our WhatsApp support!"]
      → If "Facebook":
        [Send: "Hi there! Thanks for messaging us on Facebook!"]
      → If "Website Chat":
        [Send: "Hello! How can we help you today?"]
      → Default:
        [Send: "Welcome! We're here to help."]
↓
[Event: User Message]
↓
[Continue to main conversation flow...]
```

<strong>Key Features:</strong>- Channel detection
- Personalized greetings
- Consistent user experience across platforms

### Example 4: Lead Qualification and Routing

<strong>Objective:</strong>Qualify leads and route to appropriate sales team

<strong>Flow:</strong>```
[Entry Gate]
↓
[Send: "What's your company size?"]
[Button Picker: "1-10", "11-50", "51-200", "201+"]
[Event: Button Click]
[Update User: Custom Field "company_size"]
↓
[Send: "What's your primary need?"]
[Button Picker: "Sales CRM", "Marketing Automation", "Customer Support"]
[Event: Button Click]
[Update User: Custom Field "primary_need"]
↓
[Condition: company_size AND primary_need]
  → If company_size IN ["51-200", "201+"] AND primary_need = "Sales CRM":
    [Update User: Add to Segment "Enterprise-Sales-Qualified"]
    [Action: Assign to Operator group="Enterprise Sales"]
  → If company_size IN ["1-10", "11-50"]:
    [Update User: Add to Segment "SMB-Qualified"]
    [Action: Assign to Operator group="SMB Sales"]
  → Default:
    [Send: "Thanks! A specialist will reach out within 24 hours."]
```

**Key Features:**- Progressive profiling
- Segment assignment
- Intelligent routing
- Fallback handling

## Best Practices for Scenario Design

### User-Centric Design

| Principle | Implementation | Example |
|-----------|---------------|---------|
| **Clear Language**| Use simple, conversational tone | "What brings you here today?" vs. "State your inquiry purpose" |
| **Minimal Friction**| Reduce steps, prefill when possible | Auto-detect location vs. ask for country/state/city |
| **Error Prevention**| Validate input, provide examples | "Email format: name@company.com" |
| **Graceful Degradation**| Handle unexpected input | Catch-all fallback: "I didn't understand. Can you rephrase?" |
| **Accessibility**| Support screen readers, keyboard navigation | Alt text for images, button labels |

### Technical Best Practices

**Modularity:**- Create reusable scenario components
- Use "Run Scenario" for common flows (email collection, authentication)
- Maintain scenario library for quick deployment

**Data Management:**- Always use Event Blocks after input collection
- Store data in appropriate fields (user profile, custom fields)
- Validate data before storing
- Clear temporary data when no longer needed

**Error Handling:**- Plan for invalid input
- Handle API failures gracefully
- Provide clear error messages
- Log errors for debugging

**Performance:**- Avoid unnecessary API calls
- Cache frequently accessed data
- Limit scenario depth (avoid excessive chaining)
- Monitor execution time

### Common Pitfalls to Avoid

| Pitfall | Problem | Solution |
|---------|---------|----------|
| **Missing Event Blocks**| Input not captured or processed | Always add Event Block after Field Input or Button Picker |
| **Neglecting Branches**| Dead ends, unhandled responses | Plan for all possible user responses |
| **Over-Complication**| Confusing flow, hard to maintain | Keep scenarios focused, use modular design |
| **No Error Handling**| Breaks on unexpected input | Add catch-all conditions and error messages |
| **Ignoring Context**| Generic, unhelpful responses | Use user data and conversation history |
| **Poor Documentation**| Team can't understand or modify | Add notes, clear naming, documentation |

## Benefits of Scenarios

### For End Users

**Consistent Experience:**- Predictable conversation flow
- Reliable information delivery
- Professional interaction quality

**Personalization:**- Responses adapted to user data
- Context-aware recommendations
- Relevant content and offers

**Efficiency:**- Fast resolution of common issues
- No waiting for human agents
- 24/7 availability

### For Organizations

**Scalability:**- Handle unlimited concurrent conversations
- Serve global audience without proportional headcount
- Process high volumes consistently

**Data Collection:**- Structured information capture
- Complete interaction history
- Actionable insights and analytics

**Quality Assurance:**- Standardized processes
- Compliance adherence
- Audit trail for all interactions

**Agility:**- Rapid deployment of updates
- A/B testing of flows
- Quick response to business changes

**Cost Efficiency:**- Reduced support costs (30-70% typical)
- Lower error rates
- Optimized resource allocation

## Integration with AI and Automation

Modern scenarios leverage AI capabilities:

| AI Feature | Scenario Application | Benefit |
|-----------|---------------------|---------|
| **Natural Language Understanding**| Intent detection, entity extraction | Better conversation routing |
| **Knowledge Base Search**| Automatic answer retrieval | Accurate responses without manual rules |
| **Sentiment Analysis**| Detect frustration, satisfaction | Proactive escalation or satisfaction surveys |
| **Generative AI**| Dynamic response creation | Flexible, natural conversations |
| **Predictive Analytics**| Next-best-action recommendations | Optimized user journeys |

**Example AI-Enhanced Scenario:**```
[Event: User Message]
↓
[AI Action: Detect Intent and Extract Entities]
  → Intent: "cancel_subscription"
  → Entity: subscription_tier = "premium"
↓
[Condition: Intent = "cancel_subscription"]
  → [AI Action: Analyze Sentiment]
    → If sentiment = "frustrated":
      [Priority: High]
      [Action: Assign to Senior Agent]
    → If sentiment = "neutral":
      [Send: "I can help cancel your {{subscription_tier}} plan."]
      [Button Picker: "Confirm Cancel" | "Talk to Retention"]
```

## Measuring Scenario Success

### Key Performance Indicators

| KPI | Description | Target |
|-----|-------------|--------|
| <strong>Completion Rate</strong>| % of users who finish scenario | >80% |
| <strong>Drop-off Points</strong>| Where users abandon flow | Minimize |
| <strong>Average Duration</strong>| Time to complete scenario | Minimize while maintaining quality |
| <strong>User Satisfaction</strong>| Post-interaction rating | >4/5 |
| <strong>Containment Rate</strong>| % of issues resolved without escalation | >70% |
| <strong>Error Rate</strong>| Invalid inputs, failed actions | <5% |

### Optimization Strategies

<strong>Analyze Logs:</strong>- Identify common drop-off points
- Review misunderstood inputs
- Spot technical errors

<strong>A/B Testing:</strong>- Test different message phrasings
- Compare button arrangements
- Optimize input field placement

<strong>User Feedback:</strong>- Survey satisfaction
- Collect improvement suggestions
- Monitor social media mentions

## Glossary of Key Terms

| Term | Definition |
|------|------------|
| <strong>Scenario</strong>| Pre-prepared conversation flow built from modular blocks |
| <strong>Block</strong>| Discrete unit of logic or function (Event, Action, Condition, Exit) |
| <strong>Entry Gate</strong>| Starting point of scenario flow |
| <strong>Event Block</strong>| Triggers that pause/resume scenario based on user or system events |
| <strong>Action Block</strong>| Operations executed within scenario (send message, update data, API call) |
| <strong>Condition Block</strong>| Decision points that branch scenario flow based on evaluated criteria |
| <strong>Exit Block</strong>| Ends scenario or transitions to another scenario |
| <strong>Pattern Matching</strong>| Detecting keywords or phrases in user messages |
| <strong>Memorization</strong>| Storing collected user data for later use in scenario |
| <strong>Chaining</strong>| Connecting multiple scenarios in sequence |
| <strong>Fallback</strong>| Default action when no conditions match |
| <strong>Escalation</strong>| Transferring conversation from bot to human agent |

## References


1. Chatbot.com. (n.d.). How to Write a Chatbot Script – Examples Included. Chatbot.com Blog.

2. Marutitech. (n.d.). How do Chatbots Work? A Guide to Chatbot Architecture. Marutitech Blog.

3. Interaction Design Foundation. (n.d.). What are User Scenarios?. Interaction Design Foundation Literature.

4. Interaction Design Foundation. (n.d.). Design Scenarios – Communicating the Small Steps. Interaction Design Foundation Literature.

5. Make.com. (n.d.). Scenarios for AI Agents – Help Center. Make Help Center.

6. Zendesk. (n.d.). Was ist ein Chatbot? Funktionen & Vorteile. Zendesk Blog.

7. OpenAI. (n.d.). Chatbot Best Practices. OpenAI Platform Documentation.

8. Chatbot.com. (n.d.). Documentation and Help Center. Chatbot.com Help Center.

9. Google. (n.d.). Conversation Design Best Practices. Google Dialogflow Documentation.
