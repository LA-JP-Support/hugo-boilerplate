---
title: "Code Block (Python/JS)"
lastmod: 2025-12-18
translationKey: "code-block-python-js"
description: "A group of related programming statements grouped together and treated as a single unit. Python uses indentation to define blocks, while JavaScript uses curly braces, helping organize code in functions, loops, and conditions."
keywords: ["code block", "Python", "JavaScript", "automation", "chatbot"]
category: "AI Chatbot & Automation"
type: "glossary"
date: 2025-12-18
draft: false
---

## What Is a Code Block?

A code block in programming is a contiguous section of code that a language's interpreter or compiler treats as a single executable unit. Code blocks are foundational in structuring programs, encapsulating logic for functions, loops, conditionals, classes, and more.

### Python

A Python program is constructed from code blocks. Each code block executes in its own execution frame, which manages scope, debugging info, and the flow of execution upon completion.

According to the Python Execution Model: "A block is a piece of Python program text that is executed as a unit. The following are blocks: a module, a function body, and a class definition. Each command typed interactively is a block. A script file is a code block. A module run as a top level script from the command line using a `-m` argument is also a code block."

### JavaScript

In JavaScript, a block statement is used to group zero or more statements, delimited by curly braces `{}`. This is sometimes called a "compound statement." Blocks are essential in control flow constructs such as `if`, `for`, `while`, and function declarations. Blocks also define scope for variables declared with `let` and `const`.

**Example:**
```javascript
if (condition) {
    // code block: statements here are executed if condition is true
}
```

## Syntax and Usage

### Python Code Blocks

Blocks in Python are defined by consistent indentation, typically four spaces per level. Indentation signals the start and end of a block, unlike curly braces in other languages.

**Correct Syntax Example:**
```python
if age >= 18:
    print("Adult")
    print("Can vote")
print("Done")  # Outside the block
```

**Incorrect Syntax Example:**
```python
if age >= 18:
print("Adult")  # Raises IndentationError
```

**Key Points:**
- All lines in a block must be indented by the same amount
- Mixing tabs and spaces causes errors. Use spaces only
- An empty block is invalid; use `pass` as a placeholder if needed:
```python
if condition:
    pass  # Do nothing
```

### JavaScript Code Blocks

Blocks in JavaScript are denoted by curly braces:

```javascript
if (age >= 18) {
    console.log("Adult");
    console.log("Can vote");
}
console.log("Done"); // Outside the block
```

**Incorrect Syntax Example:**
```javascript
if (age >= 18)
    console.log("Adult");
    console.log("Can vote"); // Not part of the if-block!
```

**Best Practice:** Always use curly braces, even for single-statement blocks, to avoid logic errors and improve readability.

## Naming, Binding, and Scope

### Python

- Names (variables) are bound within a block where they are assigned
- Local variables are defined within function or class blocks unless declared `global` or `nonlocal`
- Free variables are referenced within a block but defined outside it

### JavaScript

- Variables declared with `let` and `const` are block-scoped
- Variables declared with `var` are function-scoped, not block-scoped
- Block scoping is crucial for avoiding unintentional variable leaks or shadowing

**Example:**
```javascript
var x = 1;
let y = 1;
if (true) {
  var x = 2; // modifies outer x
  let y = 2; // block-scoped
}
console.log(x); // 2
console.log(y); // 1
```

## Usage in Automation and Chatbot Platforms

### Code Block Nodes

Automation platforms like Contentstack, n8n, and others provide "code block" nodes that let users embed custom Python or JavaScript.

**Features:**
- **Custom Scripting:** Write bespoke logic for data transformation, validation, or external API calls
- **Input/Output Mapping:** Pass data from previous nodes, operate on it, and output results for downstream nodes
- **Debugging:** Console logs and error reporting for troubleshooting
- **Integration:** Enables operations not possible with standard drag-and-drop nodes

**Example: Contentstack**  
Set up a Code Block action to execute JavaScript code. Inputs can be mapped from previous nodes, e.g., user data, API responses. Supports inline debugging with `console.log`.

**Example: n8n**  
Supports both JavaScript and Python (via Pyodide). Two execution modes: "Run Once for All Items" or "Run Once for Each Item". Built-in methods and variables for workflow data access.

## Practical Examples

### Python: Code Block Node (Chatbot Eligibility Check)
```python
age = input_data.get('age', 0)
if age >= 18:
    result = "Eligible"
else:
    result = "Not eligible"
output = {"eligibility": result}
```
`input_data` is the incoming data payload. Output is passed to the next automation node.

### JavaScript: Extracting Data
```javascript
var idcard = input.IDCard;
var birthday = idcard.substr(6, 4) + '-' + idcard.substr(10, 2) + '-' + idcard.substr(12, 2);
var sex = 'Female';
if (idcard.substr(16, 1) % 2 == 1) {
    sex = 'Male';
}
output = { Birthdate: birthday, Gender: sex };
```

### Nested Code Blocks

**Python:**
```python
x = 10
if x > 5:
    print("x is greater than 5")
    if x % 2 == 0:
        print("x is even")
```

**JavaScript:**
```javascript
let x = 10;
if (x > 5) {
    console.log("x is greater than 5");
    if (x % 2 === 0) {
        console.log("x is even");
    }
}
```

### Multiple Statements per Block

**Python:**
```python
for i in range(3):
    print(i)
    print(i * 2)
```

**JavaScript:**
```javascript
for (let i = 0; i < 3; i++) {
    console.log(i);
    console.log(i * 2);
}
```

## Common Issues & Troubleshooting

### Python

**IndentationError**  
Caused by inconsistent indentation. Always use four spaces per level.

**Mixing Tabs and Spaces**  
Can lead to hidden bugs. Use spaces only.

**Empty Blocks**  
Not allowed. Use `pass` for placeholder blocks.

### JavaScript

**Missing Braces**  
Omitting `{}` can produce logic errors, especially with multiple statements.

**Block Scope**  
`let` and `const` are block-scoped; `var` is not. Be careful with variable declarations.

### Automation/Chatbot Platforms

**Input/Output Handling**  
Ensure your code node expects and emits data matching the workflow requirements.

**Debugging**  
Use `console.log` for troubleshooting in platforms that support it (e.g., Contentstack, n8n).

**Code Formatting**  
In chatbots, especially Microsoft Teams, use Markdown with triple backticks for code:
````
```python
print("Hello, world!")
```
````

**Formatting Limitations**  
Not all formatting is supported on all platforms/devices. Test thoroughly.

## Formatting Code Blocks in Chatbots

**Microsoft Teams Bot Messages:**  
Use the `TextFormat` property set to `markdown` to enable code block formatting.

**Supported features:** Preformatted text (code blocks), bold, italic, hyperlinks.

**Note:** Not all formatting is supported on mobile clients; test across devices.

## Best Practices

### Python

- Use four spaces per indentation level
- Never mix tabs and spaces
- Use `pass` for empty blocks
- Keep code blocks clear and concise

### JavaScript

- Always use curly braces for blocks, even for a single statement
- Use `let`/`const` for block-scoped variables
- Be mindful of variable shadowing

### Automation/Chatbot Platforms

- Validate input/output objects' structure
- Use `console.log` for debugging where supported
- Add comments for clarity in complex scripts
- Follow platform documentation for node configuration and supported libraries

### Chatbot Code Formatting

- For Microsoft Teams, use Markdown triple backticks for code blocks
- Avoid using both HTML and Markdown in a single message
- Test formatting in the target client (desktop, iOS, Android)

## References


1. Python Software Foundation. (n.d.). Python Execution Model. Python Documentation.
2. Python Software Foundation. (n.d.). PEP 8: Python Style Guide. Python Enhancement Proposals.
3. Python Software Foundation. (n.d.). PEP 8: Indentation. Python Enhancement Proposals.
4. Python Software Foundation. (n.d.). PEP 8: Tabs or Spaces. Python Enhancement Proposals.
5. Mozilla. (n.d.). JavaScript Block Statement. MDN Web Docs.
6. Mozilla. (n.d.). Block Statement Examples. MDN Web Docs.
7. Mozilla. (n.d.). Block Scoping Rules with var. MDN Web Docs.
8. Mozilla. (n.d.). JavaScript Control Flow. MDN Web Docs.
9. Contentstack. (n.d.). Code Block Documentation. Contentstack Docs.
10. n8n. (n.d.). Code Node Documentation. n8n Documentation.
11. Microsoft. (n.d.). Bot Message Formatting. Microsoft Teams Documentation.
12. Stack Overflow. (n.d.). Python Blocks. Stack Overflow.
13. Mimo. (n.d.). Python Glossary - Code Block. Mimo Learning Platform.
