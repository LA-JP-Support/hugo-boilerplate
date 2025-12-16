+++
title = "HTTP Request Node"
translationKey = "http-request-node"
description = "Learn about the HTTP Request Node, a vital component in automation platforms like n8n and Node-RED, for sending HTTP requests to external APIs and integrating systems."
keywords = [
  "HTTP Request Node",
  "API integration",
  "automation platforms",
  "n8n",
  "Node-RED"
]
category = "AI Chatbot & Automation"
type = "glossary"
date = 2025-12-05
lastmod = 2025-12-05
draft = false
url = "/internal/glossary/HTTP-Request-Node/"

+++
## Introduction

An **HTTP Request Node** is a central component in automation and integration platforms, including [n8n](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest/), [Node-RED](https://flowfuse.com/node-red/core-nodes/http-request/), and Node.js. It allows sending HTTP requests (GET, POST, PUT, PATCH, DELETE, etc.) to external servers or APIs, processing their responses within automation workflows. This node is vital for integrating different systems, consuming third-party services, triggering webhooks, and exchanging data between applications.

## Node Capabilities

### Supported HTTP Methods

HTTP Request Nodes support the following methods, each corresponding to a specific RESTful operation:

- **GET**: Retrieve data from a specified resource.
- **POST**: Send data to create or update a resource.
- **PUT**: Replace or update a resource.
- **PATCH**: Partially update a resource.
- **DELETE**: Remove a resource.
- **HEAD**: Retrieve headers without a response body.
- **OPTIONS**: Query supported communication options.
### Authentication Options

HTTP Request Nodes cater to a wide array of authentication standards:

- **No Authentication**: For open endpoints.
- **Basic Authentication**: Username and password in the header, typically Base64-encoded.
- **Digest Authentication**: More secure than Basic, with hashed credentials.
- **Bearer Token**: Token-based (e.g., JWT) in the Authorization header.
- **OAuth1 & OAuth2**: For delegated, token-based access.
- **Header Auth**: Custom header for API keys or other tokens.
- **Custom Auth**: User-defined authentication logic.
- **Query Auth**: Credentials sent via query parameters.
### Supported Data Formats

HTTP Request Nodes handle various data formats for both request and response:

- **application/json**: JSON payloads.
- **application/x-www-form-urlencoded**: Key/value pairs encoded in the body.
- **multipart/form-data**: For file uploads and complex data.
- **Raw**: Arbitrary content with a specified content type.
- **Plain Text**: Unstructured text payloads.
- **Binary**: For file and binary data transfer.
### Additional Features

- **Custom Headers**: Set arbitrary HTTP headers (e.g., Content-Type, Authorization).
- **Query Parameters**: Dynamically filter or modify requests.
- **Proxy Support**: Route requests through HTTP proxies.
- **Timeouts**: Control request and connection timeouts.
- **SSL Validation Control**: Optionally ignore SSL certificate errors.
- **Automatic & Manual Pagination**: Retrieve multi-page API results.
- **Redirect Handling**: Configure how redirects are followed.
- **Response Handling**: Output as JSON, text, binary, or file.
- **Batching**: Control the number and timing of requests sent in parallel or sequence.
- **Optimizations for AI Agents**: (n8n) Optimize responses for AI tool consumption.
## Configuration Steps

The configuration process and available parameters are platform-specific. The following sections illustrate the typical configuration workflow for n8n, Node-RED, and Node.js.

### n8n HTTP Request Node

**Official Docs:**  
[n8n HTTP Request Node Documentation](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest/)  
[Mastering the n8n HTTP Request Node (AutomateGeniusHub)](https://automategeniushub.com/mastering-the-n8n-http-request-node/)

#### 1. Node Parameters

- **Method:** Select the HTTP method (DELETE, GET, HEAD, OPTIONS, PATCH, POST, PUT).
- **URL:** Enter the API endpoint. Can be static or constructed dynamically using [expressions](https://docs.n8n.io/code-expressions/).
- **Authentication:** Choose from predefined credentials or configure manually (Basic, Digest, Bearer, OAuth, etc.).
- **Send Query Parameters:** Filters or modifies requests; define as key/value pairs or JSON.
- **Send Headers:** Specify custom headers as key/value pairs or JSON.
- **Send Body:** Enable for POST, PUT, PATCH requests. Choose body content type (form URL-encoded, form-data, JSON, raw, binary).
- **Output Variables:** Map outputs (status code, body, headers) to workflow variables.

#### 2. Advanced Options

- **Array Format in Query Parameters:** Controls array encoding (no brackets, brackets, brackets with indices).
- **Batching:** Items per batch and delay between batches.
- **Ignore SSL Issues:** Only for trusted endpoints.
- **Lowercase Headers:** Toggle header name casing.
- **Redirects:** Enable/disable, set max redirects.
- **Response Handling:** Include headers/status, never error, specify format (auto, file, JSON, text).
- **Pagination:** Off, parameter update, next URL in response.
- **Proxy:** Specify HTTP proxy.
- **Timeout:** Set request timeout in ms.

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

**Official Docs:**  
[Node-RED HTTP Request Node](https://flowfuse.com/node-red/core-nodes/http-request/)  
[Node-RED Security Best Practices](https://nodered.org/docs/user-guide/runtime/securing-node-red)

#### Node Configuration

- **Method:** GET, POST, PUT, DELETE, PATCH, etc.
- **URL:** Static or dynamic using Mustache syntax (`{{variable}}` or `{{{variable}}}`).
- **Payload:** Ignore, append to query string, or send as request body.
- **Authentication:** None, Basic, Digest, Bearer Token.
- **Proxy:** Route requests via proxy server if needed.
- **Headers:** Add custom headers via node config or `msg.headers`. Reset headers between nodes to avoid inheritance.
- **Output:** Specify response as string, parsed JSON, or binary buffer.
- **Catch Node:** Handle non-2xx HTTP responses.

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
**Tip:** Reset `msg.headers` to `{}` between HTTP nodes to avoid header leakage.

### Node.js HTTP Requests

#### Native HTTP/HTTPS Modules

- **http / https**: Low-level modules for full control over requests (method, headers, body, authentication).
- **Streaming:** Built-in support for large payloads.
- **Proxy Support:** Via [environment variables](/en/glossary/environment-variables--secrets-/) or custom code.

**Docs:**  
[Node.js HTTP Module](https://nodejs.org/api/http.html)  
[W3Schools Node.js HTTP Module](https://www.w3schools.com/nodejs/nodejs_http.asp)

#### Fetch API (Node.js 18+)

- **Fetch API** is built-in since Node.js 18. Returns Promises, supports async/await syntax.
- **node-fetch**: For earlier Node.js versions, or when you want Fetch-style syntax.

**Example: GET Request with Fetch API**
```js
const response = await fetch('https://api.example.com/data');
const data = await response.json();
console.log(data);
```
[Node.js Fetch API Guide](https://oxylabs.io/blog/nodejs-fetch-api)

#### axios

- **axios**: Promise-based HTTP client for Node.js and browsers.
- **Features:** Interceptors, timeout, automatic JSON body/response handling, request/response transformation, progress tracking.

**Example: POST Request with axios**
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
[Axios Docs](https://axios-http.com/docs/intro)

## Best Practices and Tips

### Security

- **Credentials Storage:** Use built-in credential managers. Never hard-code secrets.
- **HTTPS:** Always validate SSL certificates. Ignore SSL only for trusted, internal endpoints ([Node-RED HTTPS Config](https://nodered.org/docs/user-guide/runtime/securing-node-red#enabling-https-access)).
- **Sanitize Input:** Validate all dynamic input (headers, params, body).
- **Token Management:** Rotate, expire, and securely store tokens.

### Error Handling

- **Status Codes:** Always check and handle HTTP status codes.
- **Timeouts:** Set appropriate timeouts to avoid hanging requests.
- **Retries:** Implement retries for transient failures (network, 5xx errors).

### Content Types and Encoding

- **Content-Type Header:** Always match the body format (`application/json`, `application/x-www-form-urlencoded`).
- **URL-Encoding:** Encode query parameters to handle special characters.
- **Array Format:** Check API docs for required array encoding in query params.

### Pagination

- **Pattern Recognition:** APIs use page/limit, offset, or next URL patterns.
- **Automation:** Use platform pagination features where possible.

### Headers and Response Handling

- **Header Reset:** In Node-RED, reset `msg.headers` between HTTP nodes.
- **Inspect Headers:** Check for rate limits, authentication challenges, and pagination cues in response headers.

### Proxy

- **Proxy Settings:** Configure if required by network or provider (see [Node-RED Proxy Config](https://flowfuse.com/node-red/core-nodes/http-proxy/)).

### Debugging and Testing

- **Use Test Tools:** Validate configs with built-in test features or tools like [Postman](https://www.postman.com/).
- **Log Responses:** Capture full responses for troubleshooting.

## Common Pitfalls

- **Incorrect Content-Type:** Mismatched content types cause API rejections.
- **Unencoded Query Params:** Special characters must be encoded.
- **Header Inheritance:** Node-RED users must reset headers between nodes to avoid leakage.
- **Ignoring Non-2xx Responses:** Always check status codes and handle errors.
- **Missing Authentication:** Most APIs require valid credentials or tokens.

## Use Cases and Examples

### 1. API Integration

- **Scenario:** Fetch user info from a REST API.
- **Steps:** Configure GET method, set URL, add Authorization header, map response.

### 2. Sending Data to a Web Service

- **Scenario:** Submit a form.
- **Steps:** POST method, Content-Type `application/x-www-form-urlencoded`, enter fields.

### 3. File Upload

- **Scenario:** Upload a file using `multipart/form-data`.
- **Steps:** POST/PUT, Content-Type `multipart/form-data`, attach file.

### 4. Webhook Trigger

- **Scenario:** Notify an external system upon an event.
- **Steps:** POST method, set URL, send JSON body.

### 5. Automation with AI Agents (n8n)

- **Scenario:** Use HTTP Request Node in LLM workflow.
- **Steps:** Attach node, configure optimized response extraction, select fields.

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

- **Credentials:** Predefined OAuth2, API Key, generic auth options.
- **UI:** Drag-and-drop, cURL import.
- **Body/Headers/Query:** Fields or direct JSON input.
- **Pagination:** Supports parameter increment and next-URL.
- **AI Agent Integration:** Optimize responses for LLMs.
- **Docs:** [n8n HTTP Request Node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest/)

### Node-RED

- **Dynamic Config:** Use `msg.method`, `msg.url`, `msg.headers`.
- **Mustache Syntax:** For dynamic URLs/headers.
- **Payload Handling:** Auto Content-Type for object payloads.
- **Response Handling:** String, JSON, binary buffer.
- **Security:** [Securing Node-RED](https://nodered.org/docs/user-guide/runtime/securing-node-red)
- **Docs:** [Node-RED HTTP Request Node](https://flowfuse.com/node-red/core-nodes/http-request/)

### Node.js

- **HTTP/HTTPS:** Low-level, full control.
- **axios/node-fetch/Fetch API:** High-level, Promise-based, easy JSON support.
- **Streaming:** Native support.
- **Proxy:** Environment or library options.
- **Docs:** [Node.js HTTP Module](https://nodejs.org/api/http.html), [Axios Docs](https://axios-http.com/docs/intro), [Node.js Fetch API](https://oxylabs.io/blog/nodejs-fetch-api)

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