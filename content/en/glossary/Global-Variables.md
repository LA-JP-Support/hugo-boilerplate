---
title: "Global Variables"
translationKey: "global-variables"
description: "A variable that can be accessed and used from anywhere in a program or automation workflow, enabling data sharing across different functions and processes."
keywords: ["Global Variables", "AI Chatbot", "Automation Platform", "Programming Variables", "Variable Scope"]
category: "AI Chatbot & Automation"
type: "glossary"
date: 2025-12-18
lastmod: 2025-12-18
draft: false
---

## What are Global Variables?

A global variable is a variable defined outside any function, block, or node and is accessible throughout the entire program or automation workflow. In both traditional programming languages (C, Python) and AI chatbot platforms, global variables can be accessed and potentially modified from any part of the codebase or flow, contrasting with local variables confined to their declaration scope.

Global variables enable data sharing across modules, maintaining user session data across conversation flows, and context sharing between disparate application parts. They persist throughout program execution or session duration, making them ideal for configuration settings, user information, and cross-component communication.

## Scope and Accessibility

**Global Scope:**  
Variables defined in global scope are accessible from every function, node, or topic in the application after declaration.

**Local vs Global Comparison:**

- **Local variables** – Confined to function, block, or node where declared
- **Global variables** – Accessible anywhere in code after declaration
- **Shadowing** – Local variables with same name can shadow global variables within their scope

## Programming Language Examples

### Python

**Defining and Accessing:**
```python
x = "awesome"  # Global variable

def myfunc():
    print("Python is " + x)  # Accesses global x

myfunc()
print("Python is " + x)
```

**Modifying Global Variables:**
```python
x = "awesome"

def myfunc():
    global x
    x = "fantastic"

myfunc()
print("Python is " + x)  # Output: Python is fantastic
```

The `global` keyword is necessary to modify global variables from within functions. Without it, Python creates a new local variable instead.

### C Language

**Declaration and Use:**
```c
#include <stdio.h>
int x = 5; // global variable

int main() {
    int y = 10; // local variable
    printf("%d", x + y); // x accessible here
    return 0;
}
```

**Multiple Function Access:**
```c
#include <stdio.h>
int a, b; // global variables

void add() {
    printf("%d", a + b);
}

int main() {
    a = 10;
    b = 15;
    add(); // Output: 25
    return 0;
}
```

C global variables are initialized to zero by default if not explicitly initialized.

## Chatbot Platform Implementation

### Microsoft Copilot Studio

**Creating Global Variables:**

1. Create a variable in the variable panel
2. Set scope to "Global (any topic can access)"
3. Variable receives prefix (e.g., `Global.UserName`)
4. Accessible and modifiable across all topics and automation nodes

**Using Global Variables:**

- Access via variable picker or type prefixed name
- Set values from user input, API calls, or query strings
- Initialize from external sources via URL parameters

**Example URL Initialization:**
```
https://web.powerva.microsoft.com/webchat/bots/12345?UserName=Ana
```

This sets `Global.UserName` to "Ana" before session starts.

**Resetting:**  
Use "Reset Conversation" system topic to clear all global variables, restoring initial state.

### ServiceNow

**Catalog Item Variables:**  
Setting variable as global makes it available across multiple workflows or catalog items.

**Caution:**  
Improper use can cause resource usage spikes and data integrity issues through accidental overwrites.

## Lifecycle and Persistence

**Lifetime:**

- **Programs** – Entire runtime duration
- **Chatbot sessions** – Duration of user session
- **Cross-session** – Requires external storage (database)

**Initialization:**

- **C** – Uninitialized globals default to zero
- **Python** – Must be assigned before use
- **Chatbot platforms** – Initialized at conversation start or from external parameters

**Persistence:**

- Standard global variables reset when application/session ends
- Cross-session persistence requires database or external storage
- Platform-specific mechanisms for long-term data retention

## Common Use Cases

**User Data Persistence:**  
Store user information (name, email, preferences) once and reuse across topics without repeated prompts.

**Session Management:**  
Maintain state or session attributes throughout conversation or workflow execution.

**Configuration Settings:**  
Hold feature flags or environment settings accessed by multiple flows or modules.

**Context Sharing:**  
Pass data between subflows, scripts, or branches for coordinated workflows.

**External Integration:**  
Accept initial context or session data from external systems or web applications.

## Advantages and Disadvantages

### Advantages

- **Accessibility** – Access and modify from any part of application or flow
- **Data Sharing** – Simplifies information sharing across isolated modules
- **Reduced Redundancy** – One-time declaration avoids repeated user prompts
- **Session Data Handling** – Ideal for session-level data in chatbots and automation

### Disadvantages

- **Side Effects Risk** – Any part can modify, potentially causing unintended behaviors
- **Debugging Complexity** – Difficult to trace changes in large codebases
- **Naming Conflicts** – Accidental overwrites without careful naming conventions
- **Resource Usage** – Excessive globals can increase memory consumption
- **Concurrency Issues** – Multi-user environments may experience data inconsistency

## Best Practices

**Limit Use:**  
Use global variables sparingly. Prefer local variables for non-shared data.

**Unique Naming:**  
Use clear, unique names with prefixes (e.g., `Global.`, `bot.`) to avoid conflicts.

**Controlled Modification:**  
Limit places where global variables can be changed. Document all modification points.

**Always Initialize:**  
Set default values to avoid undefined states and unexpected behavior.

**Document Usage:**  
Clearly document which flows or modules use each global variable for maintenance.

**Reset Appropriately:**  
Provide mechanisms to reset globals at appropriate points (session end, logout).

**Security Considerations:**  
Avoid storing sensitive data in global variables unless properly protected with encryption.

## Platform-Specific Features

### Microsoft Copilot Studio

- **Prefix System** – `Global.` or `bot.` prefix for identification
- **Scope Setting** – Configure via variable properties panel
- **Session Duration** – Persists throughout user session
- **External Initialization** – Set via URL parameters or programmatic calls
- **Reset Topic** – "Reset Conversation" clears all global variables

### ServiceNow

- **Cross-Workflow Access** – Global variables available across catalog tasks and flows
- **Resource Monitoring** – Track usage to prevent resource spikes
- **Access Control** – Implement proper permissions to prevent unauthorized modifications

## Related Concepts

**Local Variables:**  
Confined to specific function, node, or topic scope.

**Session Variables:**  
Persist only for session duration, often equivalent to globals in chatbot contexts.

**Environment Variables:**  
System or environment-level settings, typically for configuration.

**Constants:**  
Variables with unchangeable values, often implemented as globals.

**State Management:**  
Techniques for managing application state using both local and global variables.

## References


1. W3Schools. (n.d.). Python Global Variables. W3Schools.
2. GeeksforGeeks. (n.d.). Global Variables in C. GeeksforGeeks.
3. Microsoft. (n.d.). Work with Global Variables. Microsoft Copilot Studio.
4. ServiceNow Community. (n.d.). Global Variables Discussion. ServiceNow Community.
5. YouTube. (n.d.). Python Global Variables. YouTube.
