---
title: HTTP Request Node
translationKey: http-request-node
description: "A tool that automatically sends requests to external websites or services, allowing different applications to exchange data and work together without manual intervention."
keywords:
- HTTP Request Node
- API integration
- automation platforms
- n8n
- Node-RED
category: AI Chatbot & Automation
type: glossary
date: 2025-12-18
lastmod: 2025-12-18
draft: false
---

## What is an HTTP Request Node?

An HTTP Request Node is a central component in automation and integration platforms (n8n, Node-RED, Node.js) that sends HTTP requests (GET, POST, PUT, PATCH, DELETE) to external servers or APIs, processing responses within automation workflows. This node is vital for integrating systems, consuming third-party services, triggering webhooks, and exchanging data between applications.

## Core Capabilities

<strong>Supported HTTP Methods:</strong>- <strong>GET</strong>– Retrieve data from specified resource
- <strong>POST</strong>– Send data to create or update resource
- <strong>PUT</strong>– Replace or update resource
- <strong>PATCH</strong>– Partially update resource
- <strong>DELETE</strong>– Remove resource
- <strong>HEAD</strong>– Retrieve headers without response body
- <strong>OPTIONS</strong>– Query supported communication options

<strong>Authentication Options:</strong>- No Authentication (open endpoints)
- Basic Authentication (username/password, Base64-encoded)
- Digest Authentication (hashed credentials)
- Bearer Token (JWT in Authorization header)
- OAuth1 & OAuth2 (delegated, token-based access)
- Header Auth (custom headers for API keys)
- Custom Auth (user-defined logic)
- Query Auth (credentials via query parameters)

<strong>Supported Data Formats:</strong>- application/json (JSON payloads)
- application/x-www-form-urlencoded (key/value pairs)
- multipart/form-data (file uploads, complex data)
- Raw (arbitrary content with specified content type)
- Plain Text (unstructured text)
- Binary (file and binary data transfer)

<strong>Additional Features:</strong>- Custom headers (Content-Type, Authorization)
- Query parameters (dynamic filtering)
- Proxy support (HTTP proxies)
- Timeouts (request and connection control)
- SSL validation control (ignore certificate errors)
- Automatic and manual pagination
- Redirect handling
- Response handling (JSON, text, binary, file)
- Batching (parallel or sequential requests)

## Configuration by Platform

### n8n HTTP Request Node

<strong>Basic Parameters:</strong>- <strong>Method</strong>– Select HTTP method (DELETE, GET, HEAD, OPTIONS, PATCH, POST, PUT)
- <strong>URL</strong>– API endpoint (static or dynamic using expressions)
- <strong>Authentication</strong>– Choose predefined credentials or configure manually
- <strong>Send Query Parameters</strong>– Define as key/value pairs or JSON
- <strong>Send Headers</strong>– Specify custom headers
- <strong>Send Body</strong>– Enable for POST, PUT, PATCH requests
- <strong>Output Variables</strong>– Map status code, body, headers to workflow variables

<strong>Advanced Options:</strong>- Array format in query parameters
- Batching (items per batch, delay between batches)
- Ignore SSL issues (trusted endpoints only)
- Lowercase headers toggle
- Redirects (enable/disable, max redirects)
- Response handling (include headers/status, format)
- Pagination (off, parameter update, next URL)
- Proxy specification
- Timeout (request timeout in ms)

<strong>Example POST Request:</strong>```json
{
  "method": "POST",
  "url": "https://api.example.com/resource",
  "headers": {
    "Content-Type": "application/json"
  },
  "body": {
    "name": "John Doe",
    "email": "john@example.com"
  }
}
```

### Node-RED HTTP Request Node

**Configuration:**- **Method**– GET, POST, PUT, DELETE, PATCH
- **URL**– Static or dynamic using Mustache syntax (`{{variable}}`)
- **Payload**– Ignore, append to query string, or send as body
- **Authentication**– None, Basic, Digest, Bearer Token
- **Proxy**– Route via proxy server if needed
- **Headers**– Add via node config or `msg.headers`
- **Output**– Specify response as string, parsed JSON, or binary buffer
- **Catch Node**– Handle non-2xx HTTP responses

**Example Dynamic GET Request:**```json
{
  "method": "GET",
  "url": "https://api.example.com/users/{{userId}}",
  "headers": {
    "Authorization": "Bearer {{token}}"
  }
}
```

<strong>Important:</strong>Reset `msg.headers` to `{}` between HTTP nodes to avoid header leakage.

### Node.js HTTP Requests

<strong>Native HTTP/HTTPS Modules:</strong>Low-level modules for full control over requests with built-in streaming support.

<strong>Fetch API (Node.js 18+):</strong>Built-in since Node.js 18, returns Promises, supports async/await syntax.

```js
const response = await fetch('https://api.example.com/data');
const data = await response.json();
console.log(data);
```

<strong>axios:</strong>Promise-based HTTP client with interceptors, timeout, automatic JSON handling, request/response transformation.

```js
const axios = require('axios');
axios.post('https://api.example.com/resource', {
  name: 'John Doe',
  email: 'john@example.com'
}, {
  headers: {
    'Authorization': 'Bearer YOUR_TOKEN'
  }
}).then(response => {
  console.log(response.data);
});
```

## Best Practices

<strong>Security:</strong>- Use built-in credential managers, never hard-code secrets
- Always use HTTPS with SSL certificate validation
- Sanitize all dynamic input (headers, params, body)
- Rotate, expire, and securely store tokens

<strong>Error Handling:</strong>- Always check and handle HTTP status codes
- Set appropriate timeouts to avoid hanging requests
- Implement retries for transient failures (network, 5xx errors)

<strong>Content Types and Encoding:</strong>- Match Content-Type header to body format
- URL-encode query parameters for special characters
- Check API docs for required array encoding

<strong>Pagination:</strong>- Recognize API patterns (page/limit, offset, next URL)
- Use platform pagination features where possible

<strong>Headers and Response Handling:</strong>- In Node-RED, reset `msg.headers` between HTTP nodes
- Check response headers for rate limits, authentication challenges, pagination

<strong>Debugging:</strong>- Validate configs with built-in test features or tools like Postman
- Log full responses for troubleshooting

## Common Pitfalls

- Incorrect Content-Type causing API rejections
- Unencoded query params with special characters
- Header inheritance in Node-RED (must reset between nodes)
- Ignoring non-2xx responses without proper error handling
- Missing authentication for APIs requiring credentials

## Use Cases

<strong>API Integration:</strong>Fetch user info from REST API. Configure GET method, set URL, add Authorization header, map response.

<strong>Sending Data:</strong>Submit form. POST method, Content-Type `application/x-www-form-urlencoded`, enter fields.

<strong>File Upload:</strong>Upload file using `multipart/form-data`. POST/PUT, attach file.

<strong>Webhook Trigger:</strong>Notify external system upon event. POST method, set URL, send JSON body.

<strong>Automation with AI Agents (n8n):</strong>Use HTTP Request Node in LLM workflow. Attach node, configure optimized response extraction.

## Platform-Specific Notes

<strong>n8n:</strong>- Predefined OAuth2, API Key, generic auth options
- Drag-and-drop UI, cURL import
- Body/Headers/Query as fields or direct JSON input
- Pagination supports parameter increment and next-URL
- AI Agent Integration optimizes responses for LLMs

<strong>Node-RED:</strong>- Dynamic config via `msg.method`, `msg.url`, `msg.headers`
- Mustache syntax for dynamic URLs/headers
- Auto Content-Type for object payloads
- Response handling: string, JSON, binary buffer

<strong>Node.js:</strong>- HTTP/HTTPS: Low-level, full control
- axios/node-fetch/Fetch API: High-level, Promise-based
- Native streaming support
- Proxy via environment or library options

## References


1. n8n. (n.d.). HTTP Request Node Documentation. n8n Documentation.
2. Automate Genius Hub. (n.d.). Mastering the n8n HTTP Request Node. Automate Genius Hub Blog.
3. FlowFuse. (n.d.). Node-RED HTTP Request Node. FlowFuse Documentation.
4. Node-RED. (n.d.). Node-RED Securing Guide. Node-RED Documentation.
5. Node-RED. (n.d.). Node-RED HTTPS Configuration. Node-RED Documentation.
6. FlowFuse. (n.d.). Node-RED Proxy Configuration. FlowFuse Documentation.
7. Node.js. (n.d.). HTTP Module Documentation. Node.js API Reference.
8. W3Schools. (n.d.). Node.js HTTP Module. W3Schools Tutorial.
9. Axios. (n.d.). Axios Documentation. Axios Official Documentation.
10. Oxylabs. (n.d.). Node.js Fetch API Guide. Oxylabs Blog.
11. Stack Overflow. (n.d.). HTTP POST in Node.js. Stack Overflow Discussion.
12. Postman. Postman API Development Tool. URL: https://www.postman.com/
