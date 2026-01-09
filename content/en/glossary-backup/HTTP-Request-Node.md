---
title: HTTP Request Node
translationKey: http-request-node
description: Learn about the HTTP Request Node, a vital component in automation platforms
  like n8n and Node-RED, for sending HTTP requests to external APIs and integrating
  systems.
keywords:
- HTTP Request Node
- API integration
- automation platforms
- n8n
- Node-RED
category: AI Chatbot & Automation
type: glossary
date: 2025-12-05
lastmod: 2025-12-05
draft: false
---
## Introduction

An <strong>HTTP Request Node</strong>is a central component in automation and integration platforms, including [n8n](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest/), [Node-RED](https://flowfuse.com/node-red/core-nodes/http-request/), and Node.js. It allows sending HTTP requests (GET, POST, PUT, PATCH, DELETE, etc.) to external servers or APIs, processing their responses within automation workflows. This node is vital for integrating different systems, consuming third-party services, triggering webhooks, and exchanging data between applications.

## Node Capabilities

### Supported HTTP Methods

HTTP Request Nodes support the following methods, each corresponding to a specific RESTful operation:

- <strong>GET</strong>: Retrieve data from a specified resource.
- <strong>POST</strong>: Send data to create or update a resource.
- <strong>PUT</strong>: Replace or update a resource.
- <strong>PATCH</strong>: Partially update a resource.
- <strong>DELETE</strong>: Remove a resource.
- <strong>HEAD</strong>: Retrieve headers without a response body.
- <strong>OPTIONS</strong>: Query supported communication options.
### Authentication Options

HTTP Request Nodes cater to a wide array of authentication standards:

- <strong>No Authentication</strong>: For open endpoints.
- <strong>Basic Authentication</strong>: Username and password in the header, typically Base64-encoded.
- <strong>Digest Authentication</strong>: More secure than Basic, with hashed credentials.
- <strong>Bearer Token</strong>: Token-based (e.g., JWT) in the Authorization header.
- <strong>OAuth1 & OAuth2</strong>: For delegated, token-based access.
- <strong>Header Auth</strong>: Custom header for API keys or other tokens.
- <strong>Custom Auth</strong>: User-defined authentication logic.
- <strong>Query Auth</strong>: Credentials sent via query parameters.
### Supported Data Formats

HTTP Request Nodes handle various data formats for both request and response:

- <strong>application/json</strong>: JSON payloads.
- <strong>application/x-www-form-urlencoded</strong>: Key/value pairs encoded in the body.
- <strong>multipart/form-data</strong>: For file uploads and complex data.
- <strong>Raw</strong>: Arbitrary content with a specified content type.
- <strong>Plain Text</strong>: Unstructured text payloads.
- <strong>Binary</strong>: For file and binary data transfer.
### Additional Features

- <strong>Custom Headers</strong>: Set arbitrary HTTP headers (e.g., Content-Type, Authorization).
- <strong>Query Parameters</strong>: Dynamically filter or modify requests.
- <strong>Proxy Support</strong>: Route requests through HTTP proxies.
- <strong>Timeouts</strong>: Control request and connection timeouts.
- <strong>SSL Validation Control</strong>: Optionally ignore SSL certificate errors.
- <strong>Automatic & Manual Pagination</strong>: Retrieve multi-page API results.
- <strong>Redirect Handling</strong>: Configure how redirects are followed.
- <strong>Response Handling</strong>: Output as JSON, text, binary, or file.
- <strong>Batching</strong>: Control the number and timing of requests sent in parallel or sequence.
- <strong>Optimizations for AI Agents</strong>: (n8n) Optimize responses for AI tool consumption.
## Configuration Steps

The configuration process and available parameters are platform-specific. The following sections illustrate the typical configuration workflow for n8n, Node-RED, and Node.js.

### n8n HTTP Request Node

<strong>Official Docs:</strong>[n8n HTTP Request Node Documentation](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest/)  
[Mastering the n8n HTTP Request Node (AutomateGeniusHub)](https://automategeniushub.com/mastering-the-n8n-http-request-node/)

#### 1. Node Parameters

- <strong>Method:</strong>Select the HTTP method (DELETE, GET, HEAD, OPTIONS, PATCH, POST, PUT).
- <strong>URL:</strong>Enter the API endpoint. Can be static or constructed dynamically using [expressions](https://docs.n8n.io/code-expressions/).
- <strong>Authentication:</strong>Choose from predefined credentials or configure manually (Basic, Digest, Bearer, OAuth, etc.).
- <strong>Send Query Parameters:</strong>Filters or modifies requests; define as key/value pairs or JSON.
- <strong>Send Headers:</strong>Specify custom headers as key/value pairs or JSON.
- <strong>Send Body:</strong>Enable for POST, PUT, PATCH requests. Choose body content type (form URL-encoded, form-data, JSON, raw, binary).
- <strong>Output Variables:</strong>Map outputs (status code, body, headers) to workflow variables.

#### 2. Advanced Options

- <strong>Array Format in Query Parameters:</strong>Controls array encoding (no brackets, brackets, brackets with indices).
- <strong>Batching:</strong>Items per batch and delay between batches.
- <strong>Ignore SSL Issues:</strong>Only for trusted endpoints.
- <strong>Lowercase Headers:</strong>Toggle header name casing.
- <strong>Redirects:</strong>Enable/disable, set max redirects.
- <strong>Response Handling:</strong>Include headers/status, never error, specify format (auto, file, JSON, text).
- <strong>Pagination:</strong>Off, parameter update, next URL in response.
- <strong>Proxy:</strong>Specify HTTP proxy.
- <strong>Timeout:</strong>Set request timeout in ms.

#### 3. Example: Sending a POST Request with JSON Body

```json
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

<strong>Official Docs:</strong>[Node-RED HTTP Request Node](https://flowfuse.com/node-red/core-nodes/http-request/)  
[Node-RED Security Best Practices](https://nodered.org/docs/user-guide/runtime/securing-node-red)

#### Node Configuration

- <strong>Method:</strong>GET, POST, PUT, DELETE, PATCH, etc.
- <strong>URL:</strong>Static or dynamic using Mustache syntax (`{{variable}}` or `{{{variable}}}`).
- <strong>Payload:</strong>Ignore, append to query string, or send as request body.
- <strong>Authentication:</strong>None, Basic, Digest, Bearer Token.
- <strong>Proxy:</strong>Route requests via proxy server if needed.
- <strong>Headers:</strong>Add custom headers via node config or `msg.headers`. Reset headers between nodes to avoid inheritance.
- <strong>Output:</strong>Specify response as string, parsed JSON, or binary buffer.
- <strong>Catch Node:</strong>Handle non-2xx HTTP responses.

#### Example: Dynamic GET Request with Header

```json
{
  "method": "GET",
  "url": "https://api.example.com/users/{{userId}}",
  "headers": {
    "Authorization": "Bearer {{token}}"
  }
}
```
<strong>Tip:</strong>Reset `msg.headers` to `{}` between HTTP nodes to avoid header leakage.

### Node.js HTTP Requests

#### Native HTTP/HTTPS Modules

- <strong>http / https</strong>: Low-level modules for full control over requests (method, headers, body, authentication).
- <strong>Streaming:</strong>Built-in support for large payloads.
- <strong>Proxy Support:</strong>Via environment variables or custom code.

<strong>Docs:</strong>[Node.js HTTP Module](https://nodejs.org/api/http.html)  
[W3Schools Node.js HTTP Module](https://www.w3schools.com/nodejs/nodejs_http.asp)

#### Fetch API (Node.js 18+)

- <strong>Fetch API</strong>is built-in since Node.js 18. Returns Promises, supports async/await syntax.
- <strong>node-fetch</strong>: For earlier Node.js versions, or when you want Fetch-style syntax.

<strong>Example: GET Request with Fetch API</strong>```js
const response = await fetch('https://api.example.com/data');
const data = await response.json();
console.log(data);
```
[Node.js Fetch API Guide](https://oxylabs.io/blog/nodejs-fetch-api)

#### axios

- **axios**: Promise-based HTTP client for Node.js and browsers.
- **Features:**Interceptors, timeout, automatic JSON body/response handling, request/response transformation, progress tracking.

**Example: POST Request with axios**```js
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
[Axios Docs](https://axios-http.com/docs/intro)

## Best Practices and Tips

### Security

- <strong>Credentials Storage:</strong>Use built-in credential managers. Never hard-code secrets.
- <strong>HTTPS:</strong>Always validate SSL certificates. Ignore SSL only for trusted, internal endpoints ([Node-RED HTTPS Config](https://nodered.org/docs/user-guide/runtime/securing-node-red#enabling-https-access)).
- <strong>Sanitize Input:</strong>Validate all dynamic input (headers, params, body).
- <strong>Token Management:</strong>Rotate, expire, and securely store tokens.

### Error Handling

- <strong>Status Codes:</strong>Always check and handle HTTP status codes.
- <strong>Timeouts:</strong>Set appropriate timeouts to avoid hanging requests.
- <strong>Retries:</strong>Implement retries for transient failures (network, 5xx errors).

### Content Types and Encoding

- <strong>Content-Type Header:</strong>Always match the body format (`application/json`, `application/x-www-form-urlencoded`).
- <strong>URL-Encoding:</strong>Encode query parameters to handle special characters.
- <strong>Array Format:</strong>Check API docs for required array encoding in query params.

### Pagination

- <strong>Pattern Recognition:</strong>APIs use page/limit, offset, or next URL patterns.
- <strong>Automation:</strong>Use platform pagination features where possible.

### Headers and Response Handling

- <strong>Header Reset:</strong>In Node-RED, reset `msg.headers` between HTTP nodes.
- <strong>Inspect Headers:</strong>Check for rate limits, authentication challenges, and pagination cues in response headers.

### Proxy

- <strong>Proxy Settings:</strong>Configure if required by network or provider (see [Node-RED Proxy Config](https://flowfuse.com/node-red/core-nodes/http-proxy/)).

### Debugging and Testing

- <strong>Use Test Tools:</strong>Validate configs with built-in test features or tools like [Postman](https://www.postman.com/).
- <strong>Log Responses:</strong>Capture full responses for troubleshooting.

## Common Pitfalls

- <strong>Incorrect Content-Type:</strong>Mismatched content types cause API rejections.
- <strong>Unencoded Query Params:</strong>Special characters must be encoded.
- <strong>Header Inheritance:</strong>Node-RED users must reset headers between nodes to avoid leakage.
- <strong>Ignoring Non-2xx Responses:</strong>Always check status codes and handle errors.
- <strong>Missing Authentication:</strong>Most APIs require valid credentials or tokens.

## Use Cases and Examples

### 1. API Integration

- <strong>Scenario:</strong>Fetch user info from a REST API.
- <strong>Steps:</strong>Configure GET method, set URL, add Authorization header, map response.

### 2. Sending Data to a Web Service

- <strong>Scenario:</strong>Submit a form.
- <strong>Steps:</strong>POST method, Content-Type `application/x-www-form-urlencoded`, enter fields.

### 3. File Upload

- <strong>Scenario:</strong>Upload a file using `multipart/form-data`.
- <strong>Steps:</strong>POST/PUT, Content-Type `multipart/form-data`, attach file.

### 4. Webhook Trigger

- <strong>Scenario:</strong>Notify an external system upon an event.
- <strong>Steps:</strong>POST method, set URL, send JSON body.

### 5. Automation with AI Agents (n8n)

- <strong>Scenario:</strong>Use HTTP Request Node in LLM workflow.
- <strong>Steps:</strong>Attach node, configure optimized response extraction, select fields.

### Real-World Example: Node-RED HTTP Request Node for Weather API

1. Insert HTTP Request node.
2. Method: GET
3. URL: `https://api.openweathermap.org/data/2.5/weather?q={{city}}&appid={{apiKey}}`
4. Output: Parsed JSON.
5. Connect output to function node for processing.

### Real-World Example: n8n HTTP Request Node with Pagination

- Configure GET to `/users`.
- Enable Pagination: Update page/offset param per request.
- Aggregate results.

### Real-World Example: Node.js HTTPS POST with Form URLencoded Body

```js
const querystring = require('querystring');
const https = require('https');

const postData = querystring.stringify({
  'username': 'demo',
  'password': 'secret'
});

const options = {
  hostname: 'api.example.com',
  path: '/login',
  method: 'POST',
  headers: {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Content-Length': Buffer.byteLength(postData)
  }
};

const req = https.request(options, (res) => {
  let data = '';
  res.on('data', (chunk) => data += chunk);
  res.on('end', () => {
    console.log('Status:', res.statusCode);
    console.log('Body:', data);
  });
});

req.on('error', (e) => {
  console.error('Error:', e);
});

req.write(postData);
req.end();
```

## Platform-Specific Notes

### n8n

- <strong>Credentials:</strong>Predefined OAuth2, API Key, generic auth options.
- <strong>UI:</strong>Drag-and-drop, cURL import.
- <strong>Body/Headers/Query:</strong>Fields or direct JSON input.
- <strong>Pagination:</strong>Supports parameter increment and next-URL.
- <strong>AI Agent Integration:</strong>Optimize responses for LLMs.
- <strong>Docs:</strong>[n8n HTTP Request Node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest/)

### Node-RED

- <strong>Dynamic Config:</strong>Use `msg.method`, `msg.url`, `msg.headers`.
- <strong>Mustache Syntax:</strong>For dynamic URLs/headers.
- <strong>Payload Handling:</strong>Auto Content-Type for object payloads.
- <strong>Response Handling:</strong>String, JSON, binary buffer.
- <strong>Security:</strong>[Securing Node-RED](https://nodered.org/docs/user-guide/runtime/securing-node-red)
- <strong>Docs:</strong>[Node-RED HTTP Request Node](https://flowfuse.com/node-red/core-nodes/http-request/)

### Node.js

- <strong>HTTP/HTTPS:</strong>Low-level, full control.
- <strong>axios/node-fetch/Fetch API:</strong>High-level, Promise-based, easy JSON support.
- <strong>Streaming:</strong>Native support.
- <strong>Proxy:</strong>Environment or library options.
- <strong>Docs:</strong>[Node.js HTTP Module](https://nodejs.org/api/http.html), [Axios Docs](https://axios-http.com/docs/intro), [Node.js Fetch API](https://oxylabs.io/blog/nodejs-fetch-api)

## References

- [n8n HTTP Request Node Docs](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest/)
- [Mastering the n8n HTTP Request Node](https://automategeniushub.com/mastering-the-n8n-http-request-node/)
- [Node-RED HTTP Request Node](https://flowfuse.com/node-red/core-nodes/http-request/)
- [Node-RED Securing Guide](https://nodered.org/docs/user-guide/runtime/securing-node-red)
- [Node.js HTTP Module Docs](https://nodejs.org/api/http.html)
- [Axios Docs](https://axios-http.com/docs/intro)
- [Node.js Fetch API Guide](https://oxylabs.io/blog/nodejs-fetch-api)
- [W3Schools Node.js HTTP Module](https://www.w3schools.com/nodejs/nodejs_http.asp)
- [Stack Overflow: HTTP POST in Node.js](https://stackoverflow.com/questions/6158933/how-is-an-http-post-request-made-in-node-js)

This glossary provides a comprehensive, deeply detailed reference for the HTTP Request Node, including configuration, authentication, supported formats, best practices, pitfalls, and platform-specific guidance for n8n, Node-RED, and Node.js. For specific code examples, troubleshooting, and advanced integrations, consult the linked documentation and resources.
