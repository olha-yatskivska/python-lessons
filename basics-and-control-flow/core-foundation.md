# 🐍 Lessons 01-03: Python Basics & Numeric Expressions

This section covers the core foundation of the language: from naming conventions to mathematical operations and handling user input.

## 📝 Core Concepts

### Constants & Variables
* **Constants:** Fixed values such as numbers (1, 2.5) or strings. Use single quotes (`'`) or double quotes (`"`) for strings.
* **Variable Name Rules:**
    * Must start with a letter or an underscore `_`.
    * Can only consist of letters, numbers, and underscores.
    * **Case Sensitive:** `x` and `X` are different variables.
    * **Mnemonic:** Use descriptive names (e.g., `hours` is better than `h`) for better readability.

### Sentences & Statements
* **Assignment Statement (`=`):** Calculates the expression on the right-hand side and stores the result in the variable on the left.
* **Assignment with Expression:** e.g., `x = x + 2`.



---

## 🔢 Numeric Expressions

Python follows the standard order of operations (**PEMDAS**):
1. **P**arentheses `()`
2. **E**xponentiation `**`
3. **M**ultiplication `*`, **D**ivision `/`, **R**emainder `%`
4. **A**ddition `+`, **S**ubtraction `-`
5. Left to right.

| Operator | Operation | Example |
| :--- | :--- | :--- |
| `+` | Addition | `2 + 3 = 5` |
| `-` | Subtraction | `10 - 2 = 8` |
| `*` | Multiplication | `4 * 2 = 8` |
| `/` | Division | `10 / 2 = 5.0` (Result is always a float) |
| `**` | Power | `2 ** 3 = 8` |
| `%` | Remainder | `10 % 3 = 1` |

---

## 🛠 Data Types & Conversion

The type of data determines what operations can be performed on it.
* **int:** Integers (whole numbers).
* **float:** Floating-point numbers (decimals).
* **str:** Strings (text).



**Essential Functions:**
* `type()` — Check the data type of a variable.
* `int()`, `float()`, `str()` — Convert data from one type to another.
* `input()` — **Always** returns data as a `string`.

Conditional statements allow us to change the flow of the program based on certain criteria. This is the heart of automated decision-making in scripts.

### Boolean Expressions
A boolean expression is an expression that is either **True** or **False**. Python uses standard comparison operators:
* `==` : Equal to
* `!=` : Not equal to
* `>` : Greater than
* `<` : Less than
* `>=` : Greater than or equal to
* `<=` : Less than or equal to

### Logical Structures
1. **Simple If:** Executes code only if the condition is True.
2. **If-Else:** Provides an alternative path if the condition is False.
3. **Multi-way (If-Elif-Else):** Checks multiple conditions in order. Once one is True, the rest are skipped.



### Error Handling with `try` and `except`
This is a "safety net" for your code. If a block of code inside `try` fails, Python jumps to the `except` block instead of crashing.
