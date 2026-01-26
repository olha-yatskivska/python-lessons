# Network and Packets
---
## 📜 Official Protocols & Standards
* [RFC 9110 HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110.html) (Methods, Status Codes, Headers)
* [RFC 9112 HTTP/1.1](https://www.rfc-editor.org/rfc/rfc9112.html) (Methods Syntax and Routing)

---
# 🔧 Technical Fundamentals
---

## What is TCP (Transmission Control Protocol)?
TCP is a connection-oriented transport protocol. It ensures that data sent from one point to another arrives intact (the data arrives exactly as it was sent) and in the correct order.
* **Key Feature:** It uses a "Three-Way Handshake" (SYN, SYN-ACK, ACK) to establish a connection before sending data.
* **Reliability:** If a packet is lost, TCP detects it and requests a retransmission.
---
## What is a Socket?
A socket is the internal endpoint for sending or receiving data. It is the combination of an IP Address and a Port Number.
* **Analogy:** If the IP is the building address, the Socket is the specific plug in the wall you use to connect your phone.

---
##  What are TCP Port Numbers?
Ports are virtual "doors" on a computer used to distinguish between different types of traffic.
* Common TCP Ports:
  * 80: HTTP (Unencrypted web traffic)
  * 443: HTTPS (Encrypted web traffic)
  * 21: FTP (File transfer)
  * 22: SSH (Secure remote login)
  * 25: SMTP (Email)
---
## Layers in Stack Connections (OSI Model simplified)
Data travels through layers. For a web developer/tester, the most important are:
  1. **Application Layer:** (HTTP, FTP) – What the user sees.
  2. **Transport Layer:** (TCP, UDP) – How data is moved (packets).
  3. **Internet Layer:** (IP) – Routing data to the right address.
  4. **Network Access:** (Ethernet, Wi-Fi) – The physical hardware.
---
## What is IIS (Internet Information Services)?

* IIS is a Web Server software created by Microsoft. It runs on Windows and "listens" for incoming HTTP requests on ports 80 or 443 to serve websites. (Competitors: Apache, Nginx).
---
## 🐍 Python Specifics: String Handling
* When sending data over a network, Python must convert text into a format the "wire" understands (binary).
   * .encode(): Converts a String (human-readable) $\rightarrow$ Bytes (machine-readable). Default is usually UTF-8.
   * .decode(): Converts Bytes $\rightarrow$ String.
* Test Note: If you see "mojibake" (weird characters like Ã«), it usually means there is a mismatch between encoding and decoding.


---
 # Sockets in Python  
 * Python has built-in support fot TCP Sockets
```python
import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect( ('data.pr4e.org', 80) )

```

---
## Retrieving an image over HTTP
[Program](https://github.com/olha-yatskivska/python-lessons/blob/main/network-programming/exercises/image-over-http.py)

---
## Retrieving web pages with urllib
* Once the web page has been opened with urllib.request.urlopen, we can treat it like a file and read through it using a for loop.
* [Program](https://github.com/olha-yatskivska/python-lessons/blob/main/network-programming/exercises/urlib.py)
---


