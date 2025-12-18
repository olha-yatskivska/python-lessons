# 🐍 Chapter 04: Functions

## 📝 Core Concepts

### To function or not to function...
* **Organize code into "paragraphs"**: Capture a complete thought and "name it".
* **DRY (Don't Repeat Yourself)**: Make it work once and then reuse it.
* **Modularity**: If a task is complex, break it into logical chunks.
* **Library**: Build a collection of common tasks you perform frequently.



### Function Definition & Types
* **Definition**: Reusable code that takes inputs (arguments), computes, and returns results.
* **Reserved Word**: Defined using `def`.
* **Invocation**: Called using the name followed by parentheses `name()`.

**Two Main Types:**
1.  **Built-in Functions**: Provided by Python (e.g., `print()`, `type()`, `float()`, `len()`).
2.  **User-defined Functions**: Created by the programmer for specific tasks.

---

## 🧪 Why this matters for a Test Analyst
As a Test Analyst, functions are your best friend for **Test Automation**:
* **Reusable Actions**: Instead of writing "Login" steps 100 times, you create a `login()` function.
* **Maintenance**: If the login button ID changes, you only fix it in *one* function, not in 100 test cases.
* **Data-Driven Testing**: You can pass different usernames/passwords as **arguments** to the same test function to check various scenarios.
* **Readability**: Your test scripts look like a story (e.g., `check_balance()`, `withdraw_money()`) rather than a mess of code.

---

## 🛠 Building Your Own Functions

### Structure
1.  Use the `def` keyword.
2.  Indicate **Parameters** inside parentheses.
3.  **Indent** the body of the function.

> [!WARNING] 
> **Syntax Alert:** Use `==` for comparison in `if` statements. The `return` statement does **not** use an equals sign.

#### Example: Fruitful Function (Returns a value)
```python
def greet(lang):
    if lang == 'es':
        return 'Hola'
    elif lang == 'fr':
        return 'Bonjour'
    else:
        return 'Hello'

print(greet('en'), 'Glenn')
print(greet('es'), 'Sally')
```
---
### Example: Multiple Parameters
```python
def computepay(hours, rate):
    if hours <= 40:
        pay = hours * rate
    else:
        pay = 40 * rate + (hours - 40) * rate * 1.5
    return pay

# Calling the function with arguments
xp = computepay(45, 10)
print("Pay:", xp)
```
---
### Void (Non-fruitful) Functions
* These perform an action (like printing) but do not return a value to the caller.
* Example: print_lyrics() simply displays text on the screen.

---
### 💡Terminology Table

| Term | Definition | 
| :--- | :--- | :---: |
| **Argument** | The value sent to the function during a call (e.g., greet('en')) |
| **Parameter** | The variable defined in the def statement (e.g., def greet(lang):) | 
| **Return Value** | The "fruit" or result sent back by the function to the calling code |
| **Scope** | The area of the program where a variable is recognized (Local vs. Global) |

---
### ❓Interview Questions (Q&A)

**Q1: What is the difference between a Parameter and an Argument?**
* *Answer:* A parameter is the variable listed inside the parentheses in the function definition (the blueprint). An argument is the actual value that is sent to the function when it is called.

**Q2: What happens if a function does not have a return statement?**
* *Answer:* The function is considered "Void". It will execute its code, but the result of the function call will be None.

**Q3: Why should we use functions instead of just writing code line-by-line?**
* *Answer:* For code reusability, easier debugging, and better readability. It follows the DRY principle.

**Q4: Can a Python function return multiple values?**
* *Answer:* Yes, you can return multiple values separated by commas (technically returning them as a tuple).



  




