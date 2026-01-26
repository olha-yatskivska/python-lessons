# 📚 Essential RFC Documents for API & Web Testing

* As a Test Analyst, these documents serve as the "Single Source of Truth" (SSOT) when defining expected behavior and validating system requirements.

## 1. **HTTP/1.1 (The Core Standards)** 
* These are the foundation of all API interactions and web communication.
   * [RFC 9110: HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110.html) **Core content:** Definition of HTTP methods (GET, POST, PUT, DELETE), headers, and status codes (200 OK, 400 Bad Request, 404 Not Found, 500 Internal Server Error).
     * *Use case:* Essential for verifying if the server returns the correct status code and handles methods according to global standards.

   * [RFC 9112: HTTP/1.1 Message Syntax and Routing](https://www.rfc-editor.org/rfc/rfc9112.html) **Core content:** Focuses on how the data packets are physically "wrapped" into text format for transmission.
---
## 2. **JSON (The Data Exchange Language)**
* Since most modern APIs communicate via JSON, understanding its formal structure is critical for data integrity testing.
   * [RFC 8259: The JavaScript Object Notation (JSON) Data Interchange Format](https://www.rfc-editor.org/rfc/rfc8259.html)
     * **Core content:** Defines the valid syntax for JSON objects, arrays, numbers, and strings.
     * **💡 Test Analyst Tip:** If an API returns a JSON with syntax errors (e.g., trailing commas, unquoted keys, or incorrect brackets), this RFC is your official proof that the output is a bug.
---
## 3. **URI/URL (Resource Addressing)**
* Defines how links and endpoints must be structured
* [RFC 3986: Uniform Resource Identifier (URI) Generic Syntax](https://www.rfc-editor.org/rfc/rfc3986.html)
  * **Core content:** Defines the formal structure of a URL (Scheme, Authority, Path, Query, Fragment).
  * **💡 Test Analyst Tip:** Use this for Boundary Value Analysis. Check how the system handles special characters, reserved symbols, or extremely long strings in the URL path or query parameters.
---
## 4. Authentication & Security (Access Control)
* Standardized methods for securing data and identifying users.
* [RFC 6749: The OAuth 2.0 Authorization Framework](https://www.rfc-editor.org/rfc/rfc6749.html)
  * **Core content:** The industry standard for token-based authentication (e.g., "Login with Google/Facebook").
  * **💡 Test Analyst Tip:** Helps in debugging security flaws. Understanding this standard allows you to distinguish between 401 Unauthorized (missing/invalid credentials) and 403 Forbidden (valid credentials but insufficient permissions).
