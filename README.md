# **🐍 Python for Everybody (PY4E) Learning Progress**

My collection of exercises and scripts from the [PY4E course](https://www.py4e.com/lessons) by Dr. Chuck.

## **📂 Completed Lessons**

[**Chapter 01-04: Basics & Control Flow**](https://github.com/olha-yatskivska/python-lessons/tree/main/basics-and-control-flow) - Introduction to variables, expressions, and logical branching using if/else statements.

[**Chapter 05: Functions**](https://github.com/olha-yatskivska/python-lessons/tree/main/functions) - Learning code reusability, defining functions, and understanding arguments/parameters.

[**Chapter 06: Loops and Iteration**](https://github.com/olha-yatskivska/python-lessons/tree/main/loops-and-iterations) - Mastering loops (for and while), using break and continue to control program flow.

[**Chapter 07: Strings**](https://github.com/olha-yatskivska/python-lessons/tree/main/strings) - String manipulation, slicing, and using built-in methods like .find() and .upper().

[**Chapter 08: Files**](https://github.com/olha-yatskivska/python-lessons/tree/main/files) - Handling external text data, memory-efficient line-by-line parsing.

[**Chapter 09: Lists**](https://github.com/olha-yatskivska/python-lessons/tree/main/lists) - Storing multiple values in a single variable, list methods (append, sort), and using the "split" function to turn strings into searchable data.

[**Chapter 10: Dictionaries**](https://github.com/olha-yatskivska/python-lessons/tree/main/dictionaries) - Implementing "maps" or "associative arrays" to link keys to values; focusing on counting patterns and the "Get" idiom for frequency analysis.

[**Chapter 11: Tuples**](https://github.com/olha-yatskivska/python-lessons/tree/main/tuples) - Understanding the power of immutability, comparing and sorting data by keys or values, and efficient memory usage in data structures.

[**Chapter 12: Regular Expressions**](https://github.com/olha-yatskivska/python-lessons/tree/main/regular-expressions) - Using the re library for sophisticated pattern matching, extracting specific substrings from large datasets, and mastering special characters (meta-characters).

[ **Chapter 13: Network Programming**](https://github.com/olha-yatskivska/python-lessons/tree/main/network-programming) - This chapter covers how Python interacts with the web, moving beyond the browser to handle raw data transfer, urllib: built-in library for requesting and reading data from URLs, Beautiful Soup: A library used to parse and extract specific information from HTML/XML.

[ **Chapter 14: Using Web Services**](https://github.com/olha-yatskivska/python-lessons/blob/main/using-web-services.md) - This chapter focuses on structured data exchange between systems, moving from raw web pages to machine-readable formats like XML and JSON, which are the backbone of modern APIs.

[ **Chapter 15: Object-Oriented Programming**](https://github.com/olha-yatskivska/python-lessons/tree/main/object-oriented-programming)

## **📂 Current & Next Steps**

**Currently Learning:** Chapter 16 (Databases)

**Next:** Chapter 17 (Data Visualization).

## **🛠️ Key Concepts Learned (QA Perspective)**

### **🧩 Programming Fundamentals**

[**Error Handling:**](https://github.com/olha-yatskivska/python-lessons/blob/main/basics-and-control-flow/exercises/salary-calculator-with-except.py) Using try/except blocks to prevent program crashes (essential for robust automation).

[**Functions:**](https://github.com/olha-yatskivska/python-lessons/tree/main/functions) Wrapping logic into reusable blocks to avoid code duplication (DRY principle).

[**Loops:**](https://github.com/olha-yatskivska/python-lessons/tree/main/loops-and-iterations) Automating repetitive tasks and searching through data sets.

[**Efficient Test Data Management** (Lists):](https://github.com/olha-yatskivska/python-lessons/tree/main/lists) Lists are essential for handling collections of test cases, input values, or web elements. They allow you to iterate through datasets to perform repetitive testing (Data-Driven Testing) efficiently.

[**API & JSON Validation** (Dictionaries):](https://github.com/olha-yatskivska/python-lessons/tree/main/dictionaries) Since most modern APIs exchange data in JSON format, dictionaries are the primary tool for a tester to parse and validate server responses, ensuring that the actual data matches the expected business requirements.

[**Data Integrity & Configuration** (Tuples):](https://github.com/olha-yatskivska/python-lessons/tree/main/tuples) Tuples provide a secure way to store test configurations, environment constants, or database credentials. Their immutability ensures that critical test parameters are not accidentally modified during script execution.

[**Advanced Log Analysis & Field Validation** (Regular Expressions):](https://github.com/olha-yatskivska/python-lessons/tree/main/regular-expressions) Regex is an indispensable tool for a Test Analyst. It allows you to:
  * Sift through massive system logs to identify specific error patterns.
  * Perform complex UI validation (e.g., verifying that email formats, password strengths, or zip codes strictly follow requirements).
  * Extract dynamic values (like Session IDs or Tokens) from responses for subsequent test steps.

[**Network Programming**](https://github.com/olha-yatskivska/python-lessons/tree/main/network-programming)
As a Test Analyst, mastering network programming transforms how I approach technical testing:
  * [Grey Box Testing:](https://github.com/olha-yatskivska/python-lessons/blob/main/network-programming/exercises/http-request.py) Sockets and protocols allow me to verify communication between the Client and Server, helping distinguish between UI rendering bugs and backend connection failures. 
  * [Automated Data Verification:](https://github.com/olha-yatskivska/python-lessons/blob/main/network-programming/exercises/beautiful-soup.py) Using Beautiful Soup, I can automate the verification of page content, meta tags, and broken links without the overhead of a full browser automation tool (e.g., checking if all <img> tags have alt attributes)..
  * [API Fundamentals:](https://github.com/olha-yatskivska/python-lessons/blob/main/network-programming/exercises/urllinks.py) Understanding HTTP via urllib is the foundation for API testing, allowing me to analyze status codes, headers, and payloads.


### **🧪 Data Manipulation**

[**String Slicing:**](https://github.com/olha-yatskivska/python-lessons/tree/main/strings) Extracting specific data from text (e.g., pulling a username from an email string).

[**File Parsing:**](https://github.com/olha-yatskivska/python-lessons/tree/main/files) Looking for specific patterns (like "Errors" or "Failures") in large system logs.

[**Cleaning Data:**](https://github.com/olha-yatskivska/python-lessons/blob/main/strings/exercises/stripping-whitespace.py) Using .rstrip() and .strip() to ensure data consistency during comparisons.



_Status: Learning in progress..._ 🚀
