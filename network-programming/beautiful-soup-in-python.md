## What is Web Scraping?
* Web scraping is the process where a program or script simulates a browser to interact with websites.
  * **Mechanism:** The script retrieves web pages, parses the content, extracts specific information, and can navigate to further pages based on found links.
  * **Terminology:** This is often referred to as "spidering" or "web crawling", commonly used by search engines to index the internet.

## Scraping Ethics and Legality
* Scraping exists in a legal and ethical "gray area," and many site owners are protective of their data.
  * **Copyright:** It is strictly prohibited to republish copyrighted information obtained via scraping.
  * **Terms of Service (ToS):** Most websites have specific clauses forbidding automated access; violating these can lead to IP bans or legal action.

## Beautiful Soup (BS4)
* While you could manually search through raw HTML strings using regular expressions, it is inefficient and error-prone.
  * **Purpose:** [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/) is a Python library designed to make parsing HTML and XML documents easy and robust.
  * Corrected Implementation:

```python
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

# Use urllib to open the URL and BS4 to parse the HTML

```
[Program](https://github.com/olha-yatskivska/python-lessons/blob/main/network-programming/exercises/beautiful-soup.py)

---
> Note: The urllib module handles the connection (the "pipe"), while Beautiful Soup handles the data extraction (the "content").
---
## Why this is Important for a Test Analyst

| Feature | Importance for Test Analysts |
| :--- | :--- |
| **UI Automation** | Tools like Selenium or Playwright use scraping logic to "find" elements. Understanding how BS4 navigates the HTML tree helps you write better, more resilient locators (CSS selectors/Xpath). |
| **Test Data Generation** | You can scrape production like data from public sites to populate your test environments with realistic information instead of using "Test 123" placeholders. |
| **Data Integrity** | When testing a web application, you can use a scraping script to verify that the data shown in the UI matches exactly what is in the database or the API response. |
| **Regression Testing** | If a developer changes the HTML structure (e.g., changing a `<div>` to a `<span>`), your "scraping-based" automated tests will break. Understanding this flow helps you debug why a test failed. |
| **Broken Link Checking** | A "crawler" is the perfect tool for a Smoke Test to ensure every link on a page returns a 200 OK status and doesn't lead to a 404 error. |


## Summary of Network Concepts
* TCP/IP: Acts as the "pipes" or "sockets" that allow applications to talk to each other.
* We designed application protocols to make use of these pipes
* Application Protocols: HTTP (HyperText Transfer Protocol) is the language spoken over those pipes to request and send web content.
* Python's Role: Python is a preferred language for this because it has native, high-level support for sockets, HTTP requests, and complex HTML parsing.
