# Handling Nested JSON Structures with Python Dictionaries

> 💡 Pro-Tip: The "Brackets Rule" for JSON Navigation
> Technical Rule of Thumb: Always identify the bracket type to determine your data access strategy.
>
> 1. Curly Braces { } (Object/Dictionary): Use a Key in quotes to access the value.
> Syntax: data['key_name']
>
> 2. Square Brackets [ ] (Array/List): Use a Loop to iterate through multiple items.
> Syntax: for item in data:
---

## The Concept of Nesting (JSON Mapping)
* Nesting occurs when a dictionary contains other dictionaries or lists as values.
* This is exactly how JSON data is structured in API responses.
```python
  user_data = {
    "id": 101,
    "profile": {
        "name": "Alex",
        "settings": {"theme": "dark", "notifications": True}
    }
}

# Standard access (risky if keys are missing)
theme = user_data["profile"]["settings"]["theme"]
```
## Safe Access with the .get() Method
* To avoid KeyError when dealing with optional nested fields, use the .get() method.
* It allows you to provide a default value (like an empty dictionary {}) to continue "drilling down" into the data safely.
```python
# Safe navigation through multiple levels
# Even if 'profile' or 'settings' is missing, the code won't crash
theme = user_data.get("profile", {}).get("settings", {}).get("theme", "default_light")

print(f"Active Theme: {theme}")
```  
