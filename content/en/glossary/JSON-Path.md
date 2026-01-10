---
title: "JSON Path"
translationKey: "json-path"
description: "A query language that lets you quickly find and extract specific data from JSON files, similar to how you'd search through a nested folder structure."
keywords: ["JSON Path", "JSON data", "query syntax", "data extraction", "API testing"]
category: "AI Chatbot & Automation"
type: "glossary"
date: 2025-12-18
lastmod: 2025-12-18
draft: false
---

## What is JSON Path?

JSON Path is a query language designed for navigating, extracting, and evaluating elements within JSON documents. Analogous to XPath for XML, JSON Path enables targeted data retrieval from any depth of a JSON structure using standardized, readable syntax. The language is extensively used in programming, automation, API testing, data engineering, and configuration management.

JSON Path was standardized in RFC 9535 by the IETF, providing uniform syntax and semantics for query expressions. The language has implementations across numerous programming environments including JavaScript, Python, Java, PHP, and SQL databases. Common applications span API testing and validation, ETL processes, database JSON column queries, configuration management, and chatbot data parsing.

**Example Query:**```json
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

Extract user ID:
```jsonpath
$.user.id
// Output: 123
```

JSON Path dramatically simplifies extracting or validating data within deeply nested documents. It enables concise queries at any nesting depth, filters arrays and objects based on property values, selects and transforms data in API responses and configuration files, and automates repetitive extraction tasks in programming and testing.

## Core Syntax Elements

### Root and Path Operators

**Root Object (`$`)**Denotes the root of the JSON document. All paths start with `$`.**Child Access**- Dot notation: `$.user.name` (simple properties)
- Bracket notation: `$['user']['profile']` (special characters, spaces, reserved words)
- Brackets always use single quotes

**Array Access**- Index: `$.store.book[0]` (0-based indexing)
- Multiple indices: `$.store.book[0,2]` (union of elements)
- Negative indices: `$.store.book[-1]` (last element)

**Array Slicing**Python-style slicing: `[start:end:step]`
- `$.store.book[0:2]` (first two books)
- `$.store.book[::2]` (every other book)
- `$.store.book[1:]` (all except first)

**Wildcards and Recursion**- `*`: All elements at current level (`$.store.book[*].author`)
- `..`: Recursive descent, finds all matches at any depth (`$..price`)

### Filter Expressions

**Basic Filters**Syntax: `[?(condition)]` where `@` refers to current element

```jsonpath
$.store.book[?(@.price < 10)]        // Books under $10
$.store.book[?(@.category == 'fiction')]  // Fiction books
```

**Comparison Operators**- `==`, `!=`: Equality comparison
- `>`, `>=`, `<`, `<=`: Numeric comparison
- `=~`: Regex match (implementation-dependent)

**Logical Operators**- `&&`: Logical AND
- `||`: Logical OR

```jsonpath
$.store.book[?(@.category=='fiction' && @.price < 10)]
```

**Advanced Operators (Implementation-Specific)**- `in`, `nin`: Array membership
- `subsetof`: Array subset checking
- `contains`: String/array containment
- `size`: Length checking
- `empty`: Empty/non-empty testing

### Union and References

**Union Operator**Select multiple properties or indices: `[,]`

```jsonpath
$.store.book[0,1]  // First two books
$['name','age']    // Multiple properties
```

**Current Object**Inside filters, `@` references the current item being tested.

## Syntax Quick Reference

| Operator | Description | Example |
|----------|-------------|---------|
| `$` | Root object | `$.store` |
| `.property` | Child access | `$.user.name` |
| `['property']` | Bracket access | `$['user']['profile']` |
| `[n]` | Array index | `$.books[0]` |
| `[n,m]` | Multiple indices | `$.books[0,2]` |
| `[start:end:step]` | Array slice | `$.books[1:3]` |
| `[*]` | All elements | `$.store.book[*].title` |
| `..` | Recursive descent | `$..price` |
| `[?()]` | Filter expression | `$.books[?(@.price < 10)]` |
| `@` | Current object | `@.price > 20` |

## Practical Examples

Sample JSON for demonstrations:

```json
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
  }
}
```

### Common Query Patterns

**All Book Titles:**```jsonpath
$.store.book[*].title
// ["Sayings of the Century", "Sword of Honour", "Moby Dick", "The Lord of the Rings"]
```**Fiction Authors:**```jsonpath
$.store.book[?(@.category == 'fiction')].author
// ["Evelyn Waugh", "Herman Melville", "J. R. R. Tolkien"]
```**Books Under $10:**```jsonpath
$.store.book[?(@.price < 10)]
// Returns two book objects
```**All Prices (Recursive):**```jsonpath
$..price
// [8.95, 12.99, 8.99, 22.99, 19.95]
```**First Two Book Titles:**```jsonpath
$.store.book[0:2].title
// ["Sayings of the Century", "Sword of Honour"]
```**All ISBN Numbers:**```jsonpath
$.store.book[*].isbn
// ["0-553-21311-3", "0-395-19395-8"]
```

## Advanced Filter Operators

| Operator | Description | Example |
|----------|-------------|---------|
| `==` | Equals | `[?(@.color=='red')]` |
| `!=` | Not equals | `[?(@.color!='red')]` |
| `>` | Greater than | `[?(@.price>10)]` |
| `<` | Less than | `[?(@.price<10)]` |
| `>=` | Greater or equal | `[?(@.price>=10)]` |
| `<=` | Less or equal | `[?(@.price<=10)]` |
| `=~` | Regex match | `[?(@.author =~ /Evelyn.*/)]` |
| `&&` | Logical AND | `[?(@.category=='fiction' && @.price < 10)]` |
| `||` | Logical OR | `[?(@.category=='fiction' || @.price < 10)]` |
| `in` | In array | `[?(@.size in ['M','L'])]` |
| `nin` | Not in array | `[?(@.size nin ['M','L'])]` |
| `contains` | String/array contains | `[?(@.name contains 'Alex')]` |
| `size` | Length check | `[?(@.name size 4)]` |
| `empty` | Empty check | `[?(@.name empty true)]` |

Note: Operator support varies by implementation. RFC 9535 defines core operators, while extended operators may be library-specific.

## Implementation in Popular Languages

### JavaScript (Node.js)

**Library:**jsonpath

```javascript
const jsonpath = require('jsonpath');
const data = require('./data.json');

// Get all book titles
const titles = jsonpath.query(data, '$.store.book[*].title');

// Filter books cheaper than $10
const cheapBooks = jsonpath.query(data, '$.store.book[?(@.price < 10)]');

// Update values
jsonpath.value(data, '$.store.bicycle.price', 25.00);
```

### Python

**Library:**jsonpath-ng

```python
import json
from jsonpath_ng import parse

with open('data.json') as f:
    data = json.load(f)

# Extract titles
expression = parse('$.store.book[*].title')
titles = [match.value for match in expression.find(data)]

# Extract with filter
expression = parse('$.store.book[?(@.price < 10)]')
cheap_books = [match.value for match in expression.find(data)]
```

### Java

**Library:**JsonPath (Jayway)

```java
import com.jayway.jsonpath.JsonPath;

String json = Files.readString(Paths.get("data.json"));
DocumentContext ctx = JsonPath.parse(json);

// Read titles
List<String> titles = ctx.read("$.store.book[*].title");

// Read with filter
List<Map<String, Object>> cheapBooks = 
    ctx.read("$.store.book[?(@.price < 10)]");
```

### PHP

**Library:**Flow\JSONPath

```php
use Flow\JSONPath\JSONPath;

$data = json_decode(file_get_contents('data.json'), true);

// Find titles
$titles = (new JSONPath($data))->find('$.store.book[*].title');

// Find with filter
$cheapBooks = (new JSONPath($data))
    ->find('$.store.book[?(@.price < 10)]');
```

### SQL Server

**Native JSON Path Support:**```sql
-- Query JSON column
SELECT *
FROM Products
WHERE JSON_VALUE(Details, '$.category') = 'fiction';

-- Extract array elements
SELECT value
FROM OPENJSON(@json, '$.store.book')
WHERE JSON_VALUE(value, '$.price') < 10;
```

## Common Use Cases

### API Testing and Automation

**Postman Example:**```javascript
// Test response contains expected value
pm.test("User email is correct", function() {
    const email = jsonpath.query(pm.response.json(), '$.user.email')[0];
    pm.expect(email).to.eql("test@example.com");
});
```**Rest-Assured (Java):**```java
given()
    .when().get("/api/users")
    .then()
    .body("users[0].email", equalTo("test@example.com"));
```

### Data Transformation (ETL)

**Extract Errors from Logs:**```python
from jsonpath_ng import parse

errors = [match.value 
          for match in parse('$..errors[*].message').find(log_data)]
```

### Database JSON Queries

**PostgreSQL:**```sql
SELECT data->>'name' as name
FROM users
WHERE data @> '{"active": true}';
```

### Configuration Management

**Update Config Values:**```javascript
const config = require('./config.json');
jsonpath.value(config, '$.database.port', 5432);
fs.writeFileSync('config.json', JSON.stringify(config, null, 2));
```

### Chatbot Data Parsing

**Extract User Messages:**```jsonpath
$.conversation[*].user_message
```**Filter by Intent:**```jsonpath
$.messages[?(@.intent == 'purchase')].text
```

## JSON Path vs XPath

| Feature | JSON Path | XPath |
|---------|-----------|-------|
| Data Format | JSON | XML |
| Root Notation | `$` | `/` |
| Recursive Descent | `..` | `//` |
| Filter Syntax | `[?(condition)]` | `[condition]` |
| Standardized | Yes (RFC 9535) | Yes (W3C) |
| Parent/Sibling | Not supported | Supported |
| Axes | Limited | Comprehensive |

**Key Differences:**- JSON Path designed specifically for JSON's simpler structure
- XPath offers more complex navigation (ancestors, siblings)
- JSON Path focuses on forward traversal
- Both use similar filter and predicate concepts

## Best Practices

**Performance Optimization:**- Use specific paths over recursive descent when possible
- Cache compiled expressions in performance-critical code
- Consider indexing for repeated queries on large datasets

**Error Handling:**- Always validate JSON before querying
- Use strict/lax modes appropriately (SQL Server)
- Handle empty results gracefully
- Catch parsing exceptions

**Code Organization:**- Store complex paths as constants
- Document path semantics
- Use meaningful variable names for results
- Test paths with sample data

**Security Considerations:**- Validate and sanitize user-provided paths
- Avoid exposing internal data structures
- Use appropriate access controls
- Log suspicious query patterns

## References


1. IETF. (2023). RFC 9535: JSONPath Specification. IETF RFC.

2. SmartBear. (n.d.). JSONPath Syntax Documentation. SmartBear Support.

3. Microsoft. (n.d.). JSON Path Expressions in SQL Server. Microsoft Learn.

4. Postman. (n.d.). JSONPath Variables. Postman Learning.

5. ToolsQA. (n.d.). REST-Assured JSONPath. ToolsQA.

6. jsonpath. JavaScript Library. URL: https://github.com/dchester/jsonpath

7. jsonpath-ng. Python Library. URL: https://github.com/h2non/jsonpath-ng

8. JsonPath. Java Library. URL: https://github.com/json-path/JsonPath

9. Flow\JSONPath. PHP Library. URL: https://github.com/Flow-Communications/JSONPath
