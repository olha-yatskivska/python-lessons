# Application Protocol

---
## What is Protocol
* A set oof rules that all parties follow so we can predict each other's behavior
```python
http://www.dr-chuck.com/pagel.htm 
protocol // host       / document
```
 ## HTTP - Hypertext Transfer Protocol
 * The dominant Application Layer Protocol on the Internet
 * Invented for the Web - to Retrieve HTML, Images, Documents, etc
 * Extended to be data in addition to documents - RSS, Web Services, etc. Basic Concept - Make a Connection - Request a document - Retrieve the Document - Close the Connection

---
## Getting Data From The Server
* each the user clicks on an anchor tag with an href= value to switch to a new page, the browser makes a connection to the web server and issues a "GET" request - to GET the content of the page ate specified URL
* The server returns the HTML document to the Browser which formats and displays the document to the user
---

## Making an HTTP request
* Connect to the server like www.dr-chuck.com
* Request a document
    * GET http://www.dr-chuck.com/page1.htm HTTP/1.0
 
---
## Structure of an HTTP Request
* When you type a URL or click a link, the browser sends a formatted block of text. As a tester, you need to know its parts:

```HTTP
GET /page1.htm HTTP/1.1          <-- Request Line (Method, Path, Protocol)
Host: www.dr-chuck.com           <-- Header (Mandatory in HTTP/1.1)
User-Agent: Mozilla/5.0          <-- Header (Metadata about the client)
Accept-Language: en-US           <-- Header (Preferences)

```
## The HTTP Response (The Server's Answer)
* After the request, the server sends back data. This is the first thing you check in a test case:

```HTTP
HTTP/1.1 200 OK                  <-- Status Line (Protocol, Status Code, Phrase)
Content-Type: text/html          <-- Header (Tells the browser what to render)
Content-Length: 128              <-- Header (Size of the document)

<html>...</html>                 <-- Response Body (The actual content)

```
---
🧪 Why this matters for a Test Analyst
1. Verification of Status Codes
Your most basic test case: "Does the server return 200 OK for a valid page and 404 Not Found for a missing one?"

💡 Test Tip: If a page doesn't exist but the server returns 200 OK (this is called "Soft 404"), it's a bug that hurts SEO and user experience.

2. Performance & User Experience (UX)
Statelessness: HTTP is "stateless" — it forgets you as soon as the connection closes.

💡 Test Tip: To test "Remember Me" features or "Shopping Carts," you must verify Cookies in the headers. Without cookies, the server wouldn't know it's the same user.

3. Content-Type Validation
   
💡 Test Tip: If the server sends an image but the Content-Type header says text/plain, the browser won't display the image. Always check if headers match the actual content.


