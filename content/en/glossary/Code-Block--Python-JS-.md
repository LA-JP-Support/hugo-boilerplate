---
title: "Writing style definition"
translationKey: "writing-style-definition"
description: "--- title = "Code Block (Python/JS)" translationKey = "code-block-python-js" description = "A node enabling developers to write custom JavaScript or..."
keywords: ['Writing style definition', 'AI Chatbots', 'Automation', 'Customer Support']
category: "AI Chatbot & Automation"
type: "glossary"
draft: false
---

---
title = "Code Block (Python/JS)"
translationKey = "code-block-python-js"
description = "A node enabling developers to write custom JavaScript or Python scripts for advanced logic, data manipulation, and dynamic workflow control in chatbot/automation platforms."
keywords = ["code block", "code execution", "custom code", "javascript python", "input parameters"]
category = "AI Chatbot & Automation"
type = "glossary"
draft = true
---




# Writing style definition

***

## **Copywriter Technical Task Definition: Writing Style & Structure for "Code Block (Python/JS)" Articles**

---

**Content Type:**  
- Technical documentation article (product documentation, feature guide)
- Targeting blog post or help center/knowledge base format  
- May include step-by-step guides, configuration walkthroughs, practical code examples, and reference sections

**Primary Audience & Search Intent:**  
- Audience: Technical users (developers, bot builders, automation specialists) seeking to learn how to use "Code Block" (Python/JS) features in AI chatbot and automation platforms
- Search Intent: Informational & instructional—users want to understand what a Code Block node is, how/when to use it, its capabilities/limitations, and how to configure and write scripts for it

---

### Structure & Organization

1. **Title & Brief Introduction**
   - Clearly state the feature ("Code Block", "Code Node", etc.)
   - One-sentence summary of what the feature does and its purpose
   - Example:  
     “The Code Block node allows you to write custom JavaScript or Python code to handle advanced logic that standard nodes can’t achieve.”

2. **Feature Overview**
   - High-level explanation of when and why to use the node
   - Bullet points highlighting main use cases (data processing, API calls, flow control, etc.)
   - Example:  
     “Use a Code Block to manipulate incoming data, call APIs, or implement complex business logic within your automation workflow.”

3. **Supported Environments & Languages**
   - Explicitly list supported languages (typically JavaScript and/or Python)
   - Mention runtime versions and available libraries/packages (with reference links)
   - Example:  
     “The Code Block supports JavaScript (Node.js v10.16.3) and Python (3.7.5). Pre-installed modules include moment, lodash, node-fetch for JS, and requests, pandas for Python.”

4. **Step-by-Step Usage/Configuration**
   - Numbered or bulleted steps for adding and configuring the node in the UI
   - Clearly indicate where in the workflow/bot builder to find the node
   - Include screenshots or callout boxes when appropriate (reference image links)
   - Example:  
     “1. Drag and drop the Code Execution Node onto your workflow canvas.  
      2. Select your programming language (JavaScript or Python).  
      3. Click ‘Edit Code’ to open the code editor.”

5. **Variable Handling & Data Flow**
   - Explain how to pass data into the node (input), access variables, and output data
   - Demonstrate with code snippets and variable naming conventions  
   - Example:  
     “Access input parameters via `input.PARAM_NAME` and output results using `output = { key: value }`.”

6. **Code Editor Features**
   - List editor features (syntax highlighting, AI code generation, error detection, etc.)
   - Mention test mode or debugging facilities if available

7. **Example Code Snippets**
   - Provide concise, practical code samples for common tasks (data manipulation, API call, flow control)
   - Comment code for clarity
   - Example:  
     ```javascript
     var idcard = input.IDCard;
     var birthday = idcard.substr(6, 4) + '-' + idcard.substr(10, 2) + '-' + idcard.substr(12, 2);
     output = { Birthdate: birthday };
     ```

8. **Best Practices / Limitations**
   - Note any constraints (e.g., cannot access filesystem, HTTP requests may require separate nodes)
   - Mention performance notes (e.g., “Python execution is slower due to compilation steps”)

9. **Integrating with Workflow/Next Steps**
   - Explain how outputs are used by subsequent nodes
   - Show how to direct flow based on code block results (e.g., dynamic path branching)

10. **Further Resources/References**
    - Link to official docs, API references, related glossary entries, and relevant help articles
    - Example:  
      “See [Built-in methods and variables](https://docs.n8n.io/code/builtin/overview/) for more details.”

---

### Writing Style

- **Tone:** Professional, clear, and concise with a focus on technical accuracy; friendly but direct
- **Sentence Structure:**  
  - Mix of short, instructive sentences and slightly longer explanatory ones  
  - Use imperative (“Click...” “Enter...”) for steps, present tense for factual statements
- **Formatting:**  
  - Use headings, subheadings, and callouts for structure  
  - Bulleted and numbered lists for options, steps, features  
  - Code snippets are clearly separated and labeled with language
  - Visuals/screenshots referenced with captions or alt text
- **Examples of Sentences:**
  - “Select the Code node from the toolbar and drag it into your workflow.”
  - “You can write JavaScript or Python code directly in the editor to process incoming data.”
  - “Built-in libraries such as `moment` and `requests` are available for use without additional setup.”
  - “After saving your script, click ‘Test’ to run it with sample input and view the output.”
  - “To access a variable passed from a previous step, use `input.variableName`.”

---

### Requirements for Copywriter

- **Be precise and explicit**: Always state supported versions, available modules, and constraints.
- **Ensure clarity for both novice and experienced users**: Avoid jargon unless defined; explain key concepts.
- **Include practical, real-world code examples**: Code should be ready to copy and adapt.
- **Reference official sources**: Insert inline links to documentation, API references, or related articles wherever relevant.
- **Maintain consistent structure across articles**: Start with overview, proceed to setup, usage, examples, and further resources.
- **Use active voice**: Prefer “Write your code in the editor” over “The code is written in the editor.”
- **When possible, add callout notes or warnings**: E.g., “Note: External modules are only available in self-hosted environments.”

---

### Source Links (Reference in Your Articles)

- [n8n Code Node Docs](https://docs.n8n.io/code/code-node/)
- [Kore.ai Script Node Docs](https://developer.kore.ai/docs/bots/bot-builder-tool/dialog-task/working-with-the-script-node/)
- [YourGPT Code Execution Node](https://help.yourgpt.ai/article/how-to-execute-code-in-your-chatbot-834)
- [Bland AI Custom Code Node](https://blandai.mintlify.app/enterprise-features/custom-code-node)
- [HAP Code Block Node](https://help.nocoly.com/workflow/node-code-block)

---

**Prompt for LLM Model:**

Write a product documentation article or help center guide targeting technical users, explaining the “Code Block” or “Code Node” feature for Python and JavaScript in AI chatbot or automation platforms.  
- Start with a clear overview and use case summary.  
- List supported languages, runtime versions, and pre-installed libraries.  
- Provide step-by-step configuration instructions, using concise, direct language and numbered/bulleted lists.  
- Clearly explain variable input/output handling with code snippets.  
- Include practical, real-world code examples, each with comments.  
- Use headings, subheadings, and bold formatting for structure.  
- Note any limitations, performance notes, or best practices.  
- Reference official documentation with inline links for further reading.  
- Maintain a professional, instructive, and concise tone throughout.  
- Ensure the article is self-contained, actionable, and consistent with the structure and style outlined above.


| Keyword | Score |
| --- | --- |
| code block | 466.67 |
| code execution | 392.00 |
| custom code | 322.67 |
| javascript python | 289.00 |
| javascript code | 150.00 |
| input parameters | 142.22 |
| dynamic variables | 128.44 |
| execute code | 128.00 |
| code editor | 121.00 |
| processing data | 100.00 |
| custom javascript | 96.33 |
| data types | 77.78 |
| data processing | 75.00 |
| code node code | 65.33 |
| api response | 64.00 |
| node supports | 56.33 |
| add configure | 56.33 |
| api call | 35.56 |
| fetch data | 33.33 |
| node fetch | 33.33 |



---

# Glossary: Code Block (Python/JS)

**Category:** AI Chatbot & Automation  
**Definition:**  
A node enabling developers to write custom scripts for advanced logic, data manipulation, and dynamic workflow control beyond standard nodes in chatbot/automation platforms. Supports direct code execution, typically in JavaScript and/or Python.

---

## What is a Code Block (Python/JS)?

A **Code Block**—also referred to as a Code Node, Script Node, or Code Execution Node—acts as a programmable element within AI chatbot and automation platforms. It allows direct embedding and execution of custom code, generally in **JavaScript** or **Python**, within workflow or conversational flows. This unlocks capabilities for advanced logic, data transformation, third-party API interaction, and operational flexibility not possible with drag-and-drop or configuration nodes.

- **JavaScript** is the most widely supported language, leveraging a Node.js runtime.
- **Python** support is available in select platforms (e.g., n8n with Pyodide, HAP with native runner).

By integrating code, developers can implement context-aware, dynamic, and highly customized behaviors within automation or chatbot solutions.

**Key references:**  
- [n8n Code Node Documentation](https://docs.n8n.io/code/code-node/)  
- [Kore.ai Script Node Documentation](https://developer.kore.ai/docs/bots/bot-builder-tool/dialog-task/working-with-the-script-node/)  
- [ChatMaxima Code Block Help](https://support.chatmaxima.com/en/code-block-in-chatmaxima-studio--176210f4-31fb-406e-8938-2fa09e7f8e09/)

---

## Primary Use Cases and When to Use a Code Block

**Code Blocks** are applied when workflows require:

- **Data Processing & Transformation:** Parsing, filtering, aggregating, or reformatting data.
- **API Integration:** Making HTTP requests, handling API responses, or working with webhooks.
- **Advanced Business Logic:** Custom calculations, multi-step conditions, loops, or decision trees.
- **Workflow Branching:** Dynamic determination of next steps based on logic or data.
- **Custom Error Handling:** Specific error detection and messaging beyond built-in options.
- **Variable Management:** Reading/writing to context, session, or flow variables for persistent or cross-step data sharing.
- **Calculations:** From simple arithmetic to complex statistical or date-time operations.

**Typical scenario examples:**

- Pre-processing user input before an API call (e.g., input validation or normalization).
- Post-processing an API response (e.g., extracting required fields or transforming payload).
- Validating form data, chatbot entities, or user actions.
- Generating dynamic content or responses based on context/session variables.
- Implementing business-specific authentication, encryption, or masking routines.
- Custom branching: Returning path names (e.g., `"success"`, `"error"`) to control flow.

**Platform-specific use case details:**  
- [Kore.ai: Script Node Use Cases](https://developer.kore.ai/docs/bots/bot-builder-tool/dialog-task/working-with-the-script-node/)  
- [ChatMaxima: Code Block Use Cases](https://support.chatmaxima.com/en/code-block-in-chatmaxima-studio--176210f4-31fb-406e-8938-2fa09e7f8e09/)

---

## Supported Environments & Languages

| Platform      | JS Support | Python Support | Notes                                                               |
|---------------|------------|---------------|---------------------------------------------------------------------|
| n8n           | Yes        | Yes (Pyodide) | Python via WebAssembly; JS with optional self-hosted npm modules    |
| Kore.ai       | Yes        | No            | Only JavaScript (ES6) supported in Script Node                      |
| ChatMaxima    | Yes        | No            | JavaScript only, no network or file access                          |
| HAP           | Yes        | Yes           | JS and native Python (beta); custom deps for self-hosted            |
| Bland AI      | Yes        | No            | JavaScript (with support for async/await and modern syntax)         |

### JavaScript

- **Runtime:** Node.js (platform version varies; e.g., n8n uses v18.x for cloud, v10.x-v18.x for self-hosted).
- **Pre-installed Libraries:**
  - n8n Cloud: `moment`, `crypto` ([reference](https://docs.n8n.io/code/code-node/))
  - Self-hosted n8n: Any npm package if enabled ([instructions](https://docs.n8n.io/hosting/configuration/configuration-examples/modules-in-code-node/))
  - ChatMaxima: No external module support.
- **Features:** Full ES6+ syntax, async/await, Promises, console debugging.

### Python

- **Runtime:** Python 3.x via Pyodide (n8n), 3.7+ in HAP (beta).
- **Pre-installed Libraries:**
  - n8n: [Pyodide packages only](https://pyodide.org/en/stable/usage/packages-in-pyodide.html)
  - HAP: Common scientific/data packages (`pandas`, `numpy`, etc.)
- **Features:** Standard Python syntax; performance slower under Pyodide due to WebAssembly.

**Security and Limitations:**  
- No direct file system access.
- Network requests must use dedicated HTTP nodes (n8n), or are disallowed (ChatMaxima).
- External module imports are typically limited to allowlists (cloud) or disabled.

---

## Step-by-Step: How to Add and Configure a Code Block

### 1. Locate the Code Block Node
- Open your platform’s workflow or bot builder palette.
- Search for nodes named **Code Block**, **Code Node**, **Script Node**, or similar.

### 2. Add the Node to Your Workflow
- Drag and drop onto your workflow canvas.

### 3. Select Programming Language
- Choose **JavaScript** or **Python** (if supported).

### 4. Open the Code Editor
- Click to open configuration and code editor interface.

### 5. Configure Input Parameters
- Define and map input variables from previous nodes, typically via objects like `input`, `context`, or `FLOW`.

### 6. Write Custom Code
- Use platform-provided editor with syntax highlighting, IntelliSense, and built-in documentation.
- Example (JavaScript, n8n):
  ```javascript
  const { name, age } = $input.item;
  $output.set('isAdult', age >= 18);
  ```
- Example (Python, n8n):
  ```python
  name = _item['name']
  age = _item['age']
  _output['isAdult'] = age >= 18
  ```

### 7. Define Outputs
- Assign output data to specified variable/object, e.g., `output = {...}` (JS) or `return {...}` (Python).

### 8. Test and Debug
- Use test mode or sample data to validate scripts.
- Check logs, console output, or error messages for troubleshooting.

### 9. Connect Outputs
- Map output variables to subsequent nodes.
- Set up dynamic branching based on output.

**UI Reference:**  
- [n8n Code Node UI](https://docs.n8n.io/code/code-node/)  
- [ChatMaxima Code Block UI](https://support.chatmaxima.com/en/code-block-in-chatmaxima-studio--176210f4-31fb-406e-8938-2fa09e7f8e09/)

---

## Variable Handling & Data Flow

### Input Variables

- **JavaScript (n8n, ChatMaxima):**
  ```javascript
  const username = input.username;
  ```
- **Python (n8n Pyodide):**
  ```python
  username = input["username"]
  ```
- **Kore.ai:**
  - Use `context`, `session`, and `entity` objects.
  - Example:
    ```javascript
    var amount = context.entities.Amount;
    ```

### Output Variables

- **JavaScript:**
  ```javascript
  output = { isAdult: age >= 18 };
  ```
- **Python:**
  ```python
  return { "isAdult": age >= 18 }
  ```
- **n8n:**
  - Use `$output` (JS) or `_output` (Python) methods for assignment.

### Passing Data to Next Steps

- Outputs from a Code Block are available to subsequent nodes for further processing or branching.
- Dynamic branching is possible by returning specific path names or status strings.

---

## Code Editor Features

- **Syntax Highlighting:** Improves readability.
- **Autocomplete/IntelliSense:** Suggests functions and variables.
- **Inline Error Detection:** Catches syntax and runtime errors.
- **Test Mode:** Run scripts with dummy data before production.
- **Keyboard Shortcuts:** For rapid editing ([n8n shortcuts](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.code/keyboard-shortcuts/)).
- **AI Code Generation:** Some platforms offer code gen/fix via AI prompts (YourGPT, n8n AI Beta).

---

## Practical Example Code Snippets

### 1. Extracting Birthdate and Gender (JavaScript)

```javascript
var idcard = input.IDCard;
var birthday = idcard.substr(6, 4) + '-' + idcard.substr(10, 2) + '-' + idcard.substr(12, 2);
var sex = idcard.substr(16, 1) % 2 == 1 ? 'Male' : 'Female';
output = { Birthdate: birthday, Gender: sex };
```

### 2. API Call with Dynamic Routing (JavaScript, YourGPT)

```javascript
const axios = require('axios');
let apiResponse;
try {
  apiResponse = await axios.get('https://pokeapi.co/api/v2/pokemon?limit=10');
  FLOW.pokemons = apiResponse.data.results;
  return "pokemonsFound";
} catch (err) {
  FLOW.pokemons = [];
  return "error";
}
```

### 3. Bank Transfer Validation (Kore.ai)

```javascript
var valid = 0;
for (var i = 0; i < context.accdata.length; i++) {
  if (context.accdata[i].accountType == context.entities.FromAccountName) {
    if ((context.accdata[i].amount - context.entities.Amount) < 0) {
      valid = 3;
    } else {
      valid = (context.entities.Amount > context.accdata[i].transferLimit) ? 0 : 2;
    }
  }
}
context.canProceed = valid;
```

### 4. Data Transformation (Python, n8n)

```python
import pandas as pd

date_str = input["start_date"]
months = int(input["months_to_add"])
date = pd.to_datetime(date_str)
new_date = date + pd.DateOffset(months=months)
output = { "result_date": new_date.strftime("%Y-%m-%d") }
```

---

## Best Practices and Limitations

### Best Practices

- **Use try-catch for error handling** ([Kore.ai docs](https://developer.kore.ai/docs/bots/bot-builder-tool/dialog-task/working-with-the-script-node/))
- **Validate all inputs** to avoid runtime issues.
- **Modularize code:** Split logic into reusable functions.
- **Add comments** for clarity.
- **Test thoroughly** with sample data before going live.
- **Avoid long-running scripts** to prevent timeouts or performance degradation.
- **Use built-in utilities** where possible for consistency and security.
- **Do not store sensitive data** in plain text within context/session variables.

### Limitations

- **File System Access:** Generally disallowed for security.
- **Network Requests:** Often require dedicated HTTP nodes (n8n) or are blocked (ChatMaxima).
- **Module Imports:** Restricted in cloud; self-hosted platforms may allow.
- **Performance:** Python (via Pyodide) is slower than JS (n8n).
- **Data Volume:** There may be row/item limits per block (e.g., 100 in HAP).
- **Security:** Execution is sandboxed; arbitrary code may be filtered or monitored.

**Platform specifics:**  
- [n8n limitations](https://docs.n8n.io/code/code-node/)  
- [ChatMaxima limitations](https://support.chatmaxima.com/en/code-block-in-chatmaxima-studio--176210f4-31fb-406e-8938-2fa09e7f8e09/)

---

## Integrating Code Block Outputs With Workflows

- **Data Passing:** Outputs become variables/context for downstream nodes.
- **Dynamic Routing:** Return strings or path names to control workflow branches.
- **Persistence:** Assign processed data to flow/session/global vars for reuse.
- **Branching:** Output can trigger different branches (e.g., `"success"`, `"error"`).

**Example:**
```javascript
if (input.amount > 1000) {
  return "largeTransfer";
} else {
  return "normalTransfer";
}
```

---

## Platform Feature Comparison Table

| Feature                    | n8n                            | Kore.ai           | ChatMaxima        | HAP                |
|----------------------------|--------------------------------|-------------------|-------------------|--------------------|
| Languages                  | JS, Python (Pyodide)           | JS (ES6)          | JS                | JS, Python (native)|
| External Modules           | Self-hosted only               | No                | No                | Self-hosted only   |
| Input/Output               | $input/$output                 | context/entity    | input/output      | input/output       |
| File System Access         | No                             | No                | No                | No                 |
| Network Requests           | HTTP node only                 | HTTP node only    | No                | HTTP node only     |
| Syntax Highlighting        | Yes                            | Yes               | Yes               | Yes                |
| AI Code Gen                | Beta                           | No                | No                | No                 |
| Test Mode                  | Yes                            | Yes               | Yes               | Yes                |
| Keyboard Shortcuts         | Yes                            | Yes               | Yes               | Yes                |

---

## Frequently Asked Questions

**Q: Can I use both JavaScript and Python in the same workflow?**  
A: Yes, if supported by the platform. Each block runs a single language, but multiple blocks can be used in sequence.

**Q: How do I access data from previous steps?**  
A: Use platform-specific input objects (`input`, `context`, `$input.item`, etc.).

**Q: What happens if my code throws an error?**  
A: The workflow may halt or follow an error path. Use try-catch or explicit error handling.

**Q: Can I install new libraries?**  
A: Only if using a self-hosted environment with support for external modules.

**Q: How do I test my code?**  
A: Use built-in test features or supply mock data in the editor.

---

## Related Keywords

| Keyword           | Score   |
|-------------------|---------|
| code block        | 466.67  |
| code execution    | 392.00  |
| custom code       | 322.67  |
| javascript python | 289.00  |
| input parameters  | 142.22  |
| dynamic variables | 128.44  |
| execute code      | 128.00  |
| code editor       | 121.00  |
| processing data   | 100.00  |

---

## Further Resources & References

- [n8n Code Node Documentation](https://docs.n8n.io/code/code-node/)
- [Kore.ai Script Node Documentation](https://developer.k
