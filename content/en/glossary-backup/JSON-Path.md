---
title: "JSON Path"
translationKey: "json-path"
description: "JSON Path is a query syntax for extracting, searching, and manipulating specific values from complex JSON data structures using concise path expressions."
keywords: ["JSON Path", "JSON data", "query syntax", "data extraction", "API testing"]
category: "AI Chatbot & Automation"
type: "glossary"
date: 2025-12-05
lastmod: 2025-12-05
draft: false
---
## What is JSON Path?

JSON Path is a query language designed for navigating, extracting, and evaluating elements within JSON (JavaScript Object Notation) documents. It is analogous to XPath for XML, enabling targeted data retrieval from any depth of a JSON structure using a standardized, readable syntax. JSON Path is extensively used in programming, automation, API testing, data engineering, and configuration management, serving as an essential tool for anyone who needs to work efficiently with JSON data.

- <strong>Standardization:</strong>JSON Path was standardized in [RFC 9535](https://datatracker.ietf.org/doc/html/rfc9535) by the IETF, providing a uniform syntax and semantics for JSONPath query expressions.
- <strong>Cross-language support:</strong>JSON Path is implemented in numerous programming languages (e.g., JavaScript, Python, Java, PHP, and SQL databases).
- <strong>Use cases:</strong>API testing, validation, data extraction, ETL (Extract, Transform, Load) processes, configuration management, and chatbot automation.

<strong>Example JSON:</strong>```json
{
  "user": {
    "id": 123,
    "profile": {
      "name": "Alice",
      "roles": ["admin", "editor"]
    }
  }
}
```
**Extract the user’s ID:**```jsonpath
$.user.id
// Output: 123
```
## Why Use JSON Path?

JSON Path dramatically simplifies extracting or validating data within deeply nested JSON documents. It enables you to:

- Write concise queries to retrieve data at any depth of nesting.
- Filter arrays and objects based on property values.
- Select, transform, or validate data in API responses, configuration files, logs, and databases.
- Automate repetitive data extraction tasks in programming, testing, and analytics.

<strong>Common Use Cases:</strong>- <strong>API Testing & Automation:</strong>Assert and validate specific fields in REST API responses (e.g., with Postman, Rest-Assured).
- <strong>Data Processing Pipelines:</strong>Extract targeted data from JSON logs or data lakes for analytics and ETL.
- <strong>Database Integration:</strong>Query JSON columns in databases (SQL Server, PostgreSQL, MongoDB).
- <strong>Configuration Management:</strong>Retrieve or update settings in JSON config files.
- <strong>AI Chatbots:</strong>Parse user attributes, intents, or message history in JSON-formatted conversations.
## JSON Path Syntax and Operators

### Core Syntax Elements

JSON Path expressions consist of selectors and operators to traverse and filter JSON data. The [SmartBear JSONPath Syntax Documentation](https://support.smartbear.com/alertsite/docs/monitors/api/endpoint/jsonpath.html) and [RFC 9535](https://datatracker.ietf.org/doc/html/rfc9535) provide a comprehensive reference.

#### 1. <strong>Root Object (`$`)</strong>- Denotes the root of the JSON document.
- Example: `$.store` selects the `store` object at the root.

#### 2. <strong>Child Operators (`.` and `[]`)</strong>- Dot notation (`.`): Accesses child properties (e.g., `$.user.name`).
- Bracket notation (`['property']`): Handles property names with spaces, special characters, or reserved words (e.g., `$['user']['profile']`). Brackets always use single quotes.

#### 3. <strong>Array Access</strong>- Index (`[n]`): Selects the nth (0-based) element (`$.store.book[0]`).
- Multiple indices (`[n,m]`): Selects several elements (`$.store.book[0,2]`).

#### 4. <strong>Array Slice Operator (`[start:end:step]`)</strong>- Selects a range of array elements (Python-style).
- Examples: `$.store.book[0:2]` selects the first two books; `$.store.book[::2]` selects every other book.

#### 5. **Wildcard (`*`)**- Selects all elements at the current level.
- Example: `$.store.book[*].author` retrieves all authors in the book array.

#### 6. <strong>Recursive Descent (`..`)</strong>- Selects all matching elements at any depth under the current node.
- Example: `$..price` finds all `price` fields anywhere in the document.

#### 7. <strong>Filter Expressions (`[?(...)]`)</strong>- Filters array elements based on a condition.
- Example: `$.store.book[?(@.price < 10)]` selects books priced below 10.
- `@` refers to the current element, `$` refers to the document root.

#### 8. <strong>Script Expressions</strong>- Some implementations support functions like `length`, `max`, or `min` (not part of the RFC standard).
- Example: `$.store.book[?(@.author =~ /Evelyn.*/)]` selects authors starting with "Evelyn".

#### 9. <strong>Union Operator (`[,]`)</strong>- Selects a union of multiple properties or array indices.
- Example: `$.store.book[0,1]` selects the first and second books.

#### 10. <strong>Current Object (`@`)</strong>- Used inside filters to reference the current item.
- Example: `$.store.book[?(@.category == 'fiction')]`

#### 11. <strong>Case Sensitivity</strong>- JSON Path is case-sensitive for property names and values.

## JSON Path Syntax Cheat Sheet

| Operator           | Description                                          | Example                                |
|--------------------|------------------------------------------------------|----------------------------------------|
| `$`                | Root object                                          | `$.store`                              |
| `.` / `['name']`   | Child/property access                                | `$.user.name`, `$['user']['profile']`  |
| `[*]`              | Wildcard (all elements)                              | `$.company.employees[*].name`          |
| `..`               | Recursive descent (all descendants)                  | `$..price`                             |
| `[n]`              | Array index access                                   | `$.books[0]`                           |
| `[n,m]`            | Multiple indices (union)                             | `$.books[0,2]`                         |
| `[start:end:step]` | Array slice operator                                 | `$.books[1:3]`                         |
| `[?()]`            | Filter expression                                    | `$.books[?(@.price < 10)]`             |
| `@`                | Current object in filter                             | `@.price > 20`                         |
| `*`                | Wildcard (all keys or values at this level)          | `$.store.*`                            |
## Practical Examples

<strong>Sample JSON:</strong>```json
{
  "store": {
    "book": [
      {
        "category": "reference",
        "author": "Nigel Rees",
        "title": "Sayings of the Century",
        "price": 8.95
      },
      {
        "category": "fiction",
        "author": "Evelyn Waugh",
        "title": "Sword of Honour",
        "price": 12.99
      },
      {
        "category": "fiction",
        "author": "Herman Melville",
        "title": "Moby Dick",
        "isbn": "0-553-21311-3",
        "price": 8.99
      },
      {
        "category": "fiction",
        "author": "J. R. R. Tolkien",
        "title": "The Lord of the Rings",
        "isbn": "0-395-19395-8",
        "price": 22.99
      }
    ],
    "bicycle": {
      "color": "red",
      "price": 19.95
    }
  },
  "expensive": 10
}
```

### Example Queries

1. **Get All Book Titles**```jsonpath
   $.store.book[*].title
   // Output: ["Sayings of the Century", "Sword of Honour", "Moby Dick", "The Lord of the Rings"]
   ```

2. <strong>Get All Authors of Fiction Books</strong>```jsonpath
   $.store.book[?(@.category == 'fiction')].author
   // Output: ["Evelyn Waugh", "Herman Melville", "J. R. R. Tolkien"]
   ```

3. **Find All Books Priced Below 10**```jsonpath
   $.store.book[?(@.price < 10)]
   // Output: [ ... two book objects ... ]
   ```

4. <strong>Get All Prices in the Store (Books and Bicycle)</strong>```jsonpath
   $.store..price
   // Output: [8.95, 12.99, 8.99, 22.99, 19.95]
   ```

5. **Select the Last Book in the Array**```jsonpath
   $.store.book[-1]
   // Output: { ... Tolkien book ... }
   ```

6. <strong>Get Titles of the First Two Books</strong>```jsonpath
   $.store.book[0:2].title
   // Output: ["Sayings of the Century", "Sword of Honour"]
   ```

7. **Get All ISBN Numbers in the Store**```jsonpath
   $.store.book[*].isbn
   // Output: ["0-553-21311-3", "0-395-19395-8"]
   ```

8. <strong>Get All Items in Store (Books and Bicycle) Using Wildcard</strong>```jsonpath
   $.store.*
   // Output: [book array, bicycle object]
   ```

9. **Recursive Descent to Get All Prices Anywhere**```jsonpath
   $..price
   // Output: [8.95, 12.99, 8.99, 22.99, 19.95, 10]
   ```
## JSON Path Operators and Filters (Advanced)

### Supported Operators ([SmartBear Documentation](https://support.smartbear.com/alertsite/docs/monitors/api/endpoint/jsonpath.html#filters))

| Operator | Description                                 | Example                                              |
|----------|---------------------------------------------|------------------------------------------------------|
| `==`     | Equals to                                   | `[?(@.color=='red')]`                                |
| `!=`     | Not equal to                                | `[?(@.color!='red')]`                                |
| `>`      | Greater than                                | `[?(@.price>10)]`                                    |
| `>=`     | Greater than or equal to                    | `[?(@.price>=10)]`                                   |
| `<`      | Less than                                   | `[?(@.price<10)]`                                    |
| `<=`     | Less than or equal to                       | `[?(@.price<=10)]`                                   |
| `=~`     | Regex match (implementation-dependent)      | `[?(@.author =~ /Evelyn.*/)]`                        |
| `&&`     | Logical AND                                 | `[?(@.category=='fiction' && @.price < 10)]`         |
| `||`     | Logical OR                                  | `[?(@.category=='fiction' || @.price < 10)]`         |
| `in`     | Value is in an array                        | `[?(@.size in ['M','L'])]` (SmartBear TestEngine)    |
| `nin`    | Value NOT in an array                       | `[?(@.size nin ['M','L'])]` (SmartBear TestEngine)   |
| `subsetof` | Array is a subset of another array        | `[?(@.sizes subsetof ['M','L'])]` (TestEngine only)  |
| `contains` | String or array contains a value          | `[?(@.name contains 'Alex')]` (TestEngine only)      |
| `size`   | Array or string has specific length         | `[?(@.name size 4)]` (TestEngine only)               |
| `empty true/false` | Is empty/non-empty                | `[?(@.name empty true)]` (TestEngine only)           |

<strong>Note:</strong>Operator support may vary by library. See [RFC 9535 Section 2.3.5](https://datatracker.ietf.org/doc/html/rfc9535#section-2.3.5) for standardization.

## How JSON Path is Used in Practice

### 1. API Automation and Testing

- <strong>Validate API responses</strong>using JSONPath in tools like [Postman](https://learning.postman.com/docs/writing-scripts/script-references/variables-list/), [Rest-Assured](https://toolsqa.com/rest-assured/jsonpath-and-query-json-using-jsonpath/), or [SoapUI](https://support.smartbear.com/alertsite/docs/monitors/api/endpoint/jsonpath.html).
- <strong>Example:</strong>Assert that the returned user's email matches the expected value:
  ```javascript
  // Postman
  pm.expect(pm.response.json().user.email).to.eql("test@example.com");
  // With JSONPath
  const email = jsonpath.query(response, '$.user.email')[0];
  ```

### 2. Data Transformation and ETL

- Extract nested attributes from JSON logs or files for analytics using libraries like [jsonpath-ng](https://github.com/h2non/jsonpath-ng) (Python).
  ```python
  from jsonpath_ng import parse
  errors = [match.value for match in parse('$..errors[*].message').find(log_data)]
  ```

### 3. Database Queries

- Query JSON columns in SQL Server or PostgreSQL using JSONPath.
  - <strong>SQL Server:</strong>[JSON Path Expressions in SQL Server](https://learn.microsoft.com/en-us/sql/relational-databases/json/json-path-expressions-sql-server?view=sql-server-ver17)
  - <strong>Example:</strong>```sql
    SELECT *
    FROM OPENJSON(@json, '$.store.book[?(@.price < 10)]')
    ```

### 4. AI Chatbots and Automation

- Parse user attributes, intents, or conversation history in JSON-formatted chat logs.
  ```jsonpath
  $.conversation[*].user_message
  ```

### 5. Configuration Management

- Dynamically update or read configuration values in JSON files using JSONPath update methods.
  ```javascript
  jsonpath.value(config, '$.env.mode', 'production');
  ```
## Comparison to XPath

| Feature         | JSON Path           | XPath         |
|-----------------|--------------------|--------------|
| Data Format     | JSON               | XML          |
| Syntax          | Path-like, `$..`   | Path-like, `//`, `/` |
| Filters         | `[?(condition)]`   | `[condition]`|
| Recursion       | `..`               | `//`         |
| Standardized?   | Yes (RFC 9535)     | Yes          |
| Parent/Sibling  | Not supported      | Supported    |

- JSON Path is for JSON, XPath is for XML.
- JSON Path lacks parent/sibling navigation found in XPath.
## JSON Path in Code: Multi-Language Examples

### JavaScript (Node.js)
- [jsonpath](https://github.com/dchester/jsonpath)
```javascript
const jsonpath = require('jsonpath');
const data = require('./data.json');

// Get all book titles
const titles = jsonpath.query(data, '$.store.book[*].title');
console.log(titles);

// Filter books cheaper than 10
const cheapBooks = jsonpath.query(data, '$.store.book[?(@.price < 10)]');
console.log(cheapBooks);
```

### Python
- [jsonpath-ng](https://github.com/h2non/jsonpath-ng)
```python
import json
from jsonpath_ng import parse

with open('data.json') as file:
    data = json.load(file)

titles = [match.value for match in parse('$.store.book[*].title').find(data)]
print(titles)
```

### Java
- [JsonPath](https://github.com/json-path/JsonPath)
```java
import com.jayway.jsonpath.JsonPath;

String json = new String(Files.readAllBytes(Paths.get("data.json")));
DocumentContext ctx = JsonPath.parse(json);

List<String> titles = ctx.read("$.store.book[*].title");
```

### PHP
- [Flow\JSONPath](https://github.com/Flow-Communications/JSONPath)
```php
use Flow\JSONPath\JSONPath;

$data = json_decode(file_get_contents('data.json'), true);

$titles = (new JSONPath($data))->find('$.store.book[*].title');
print_r($titles->data());
```

## Best Practices and Tips

- **Strict vs. Lax Mode:**Some implementations (e.g., SQL Server) offer strict/lax modes for error handling of missing paths.
- **Bracket Not
