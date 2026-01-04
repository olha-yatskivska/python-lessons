# 💡 Dictionaries for QA: Practical Applications

## 🌐 API Testing (JSON handling)
* Context: REST API responses are almost always in JSON format, which Python reads as a dictionary.
* Usage: You can easily validate specific fields in a large response.
```python
# Checking if the API returned the correct user role
response = {"id": 101, "name": "Olha", "role": "QA_Lead"}
assert response["role"] == "QA_Lead"
```
---
## 📊 Data-Driven Testing
* Context: Instead of hardcoding values, you can store multiple test scenarios in a list of dictionaries.
* Usage: This allows you to run the same test logic with different "keys" (inputs) and "values" (expected results).
```python
test_cases = [
    {"user": "admin", "access": True},
    {"user": "guest", "access": False}
]
```
---
## 🛠 Database Mocking & State Management
* Context: If the database is unavailable, you can "mock" it using a dictionary where the key is the ID and the value is the record.
* Usage: Fast lookup of expected data without complex SQL queries during the initial script development.

##  🧩 Element Locators (UI Automation)
* Context: In Selenium or Playwright, you can store UI elements (selectors) in a dictionary to keep them organized.
* Usage: If a button's ID changes, you only update it in one dictionary instead of searching through 50 test scripts.
```python
locators = {
    "login_btn": "id_001",
    "logout_btn": "id_042"
}
```
