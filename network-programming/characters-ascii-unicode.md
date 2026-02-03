# Characters, ASCII & Unicode

## ASCII 
* Upper and lower letters are different characters
* For letters only Latin
* Each character is represented by a number between 0 and 256 stored in 8 bits memory
* We refer to "8 bits of memory as a "byte" of memory
* The ord() function tells us the numeric value of a simple ASCII character

```python
>>> print(ord('H'))
72
>>> print(ord('e'))
101
>>> print(ord('\n'))
10
```
* Lowercase E is higher that uppercase H because in the simplest of sorts we sort them numerically
---

## Unicode 

> [Unicode site](https://unicode.org/charts/)
---
* To represent the wide range of characters computers must handle we represent characters with more than one byte
* UTF-16 - fixed length - Two bytes
* UTF-32 - fixed length - Four bytes
* UTF - dynamic length - 1-4 bytes
   * Upwards compatible with ASCII
   * Automatic detection between ASCII and UTF-8
   * UTF-8 is recommended practice for encoding data to be exchanged between systems (compression)
   * In Python 3, all strings are internally Unicode
   * Working with string variables in Python programs are reading data from files usually "just works"
   * When we talk to a network resource using sockets or talk to a database we have to encode and decode data (usually to UTF-8)

  ## Python Strings to Bytes
  * When we talk to an external resource like a network socket we sends bytes, so we need to encode Python 3 strings into a given character encoding
  * When we read data from an external resource, wee must decode it based on the character set so it is properly represented in Python 3 as a string
```python
while True: 
   data = mesock.recv(512)
   if (len (data) < 1 ) :
       break
   mystring = data.decode()
   print(mystring)
```
[An HTTP Request in Python](https://github.com/olha-yatskivska/python-lessons/blob/main/network-programming/exercises/http-request.py)

---
## Why this is important for a Test Analyst (English)

* **Data Corruption Detection:** Many "invisible" bugs happen when a String is encoded in one format (e.g., UTF-8) but the system expects another (e.g., Windows-1252). Verify that special characters, accents, and non-Latin scripts remain intact throughout the entire lifecycle.

* **Buffer and Memory Management:** Strings and Bytes have different sizes. A single character in a Unicode String might take up to 4 bytes in a UTF-8 Byte stream. If you are testing a system with strict memory limits or fixed-length database fields, this is where "Buffer Overflow" or "Data Truncation" errors are born.

* **Security & Input Validation:** Attackers often use "Double Encoding" or invalid byte sequences to bypass web application firewalls (WAF). Understanding how the Socket receives raw bytes and how decode() processes them helps you design security test cases to ensure the system doesn't execute malicious code hidden in the byte stream.

* **Integration Testing:** When testing communication between different services (e.g., a Python backend talking to a Java microservice), the "handshake" depends on both sides agreeing on the encoding. Testing the "Send/Receive" methods ensures that no data is lost "in translation" across the network.
