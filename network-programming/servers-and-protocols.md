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
