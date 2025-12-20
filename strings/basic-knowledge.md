
# 🐍 String Data Type

* A string is a sequence of characters.
* A string uses quotes 'Hello' or "Hello".
* For strings, + means "concatenate".
* When a string contains numbers, it is still a string.
* We can convert numbers in a string into a number using int().
* **Length of strings:** the function len gives us the length of a string.
---
> A ***function*** is some stored code that we use. a function takes some *input* and produces an *output*.
---
## Reading and Converting

* We prefer to read data in using strings and then parse and convert the data as we need.
* This gives us more control over error situations and/or bad user input.
* Input numbers must be converted from strings.
---
# Looking Inside Strings
* We can get at any single character in a string using an index specified in square brackets.  
* The index value must be an integer and starts at zero.
* The index value can be an expression that is computed.

```python
fruit= 'banana'
letter = fruit[1]
print(letter)
x=3
w=fruit[x-1]
print(w)
```
---
# A Character Too Far
* You will get a *python error* if you attempt to index beyond the end of a string.
* So be careful when constructing index values and slices.

# Looping Through Strings
* Using a *while* statement, an *iteration variable*, and the *len* function, we can construct a loop to look at each of the letters in a string individually:

```python
fruit = 'banana'
index = 0 
while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index = index + 1

```
* A definite loop using a *for* statement is much elegant.
* The iteration variable is completely taken care of by the *for* loop.

```python
fruit = 'banana'
for letter in fruit:
    print(letter)
```
---
# Looking Deeper into in
* The **iteration variable** "iterates" through the sequence (ordered set).
* The **block (body)** of code is executed once for each value *in* the *sequence*
* The **iteration variable** moves through all of the values *in* the *sequence*

```python
for letter in 'banana' :
    print(letter)
```

# Slicing Strings
* We can also look at any continuous section of a string using a **colon operator**.
* The second number is one beyond the end of the slice - "up to but not including".
* If the second number is beyond the end of the string, it stops at the end.
* If we leave off the first number or the last number of the slice, it is assumed to be the beginning or end of the string respectively. [Program](https://github.com/olha-yatskivska/python-lessons/blob/main/strings/exercises/slicing-strings.py)
---
# String Concatenation
* When the **+** operator is applied to strings, it means **"concatenation"**. [Program](https://github.com/olha-yatskivska/python-lessons/blob/main/strings/exercises/string-concatenation.py)

---
# Using in as a Logical Operator
* The **in** keyword can alsi be used to check to see if one string is in another string.
* The **in** expression is a logical expression that return *True* or *False* and can be used in an *if* statement. [Program](https://github.com/olha-yatskivska/python-lessons/blob/main/strings/exercises/logical-operator.py)
* [String Comparison](https://github.com/olha-yatskivska/python-lessons/tree/main/strings/exercises)
---
# String Library
* Python has a number of string functions wch are in the strinh library.
* These *functions* are already *build into* every string - we invoke them by appending the function to the string variable.
* These *functions* do not modify the original string, instead they return a new string that has been altered.
[Library](https://docs.python.org/3/library/stdtypes.html#string-methods)
```python
str.capitalize()
str.center(wigth[, fillchar])
str.endswith(suffix[, start[, end]])
str.lstripo([chars])
str.replace(old, new[, count])
str.lower()
str.rstrip([chars])
str.strip([chars])
str.upper()
```
---
# Searching a String
* We use the **find()** function to search for a substring within another string.
* **find()** finds the first occurrence of the substring.
* If the subscring is not found, **find()** returns -1.
* Remember that string position starts at zero. [Program](https://github.com/olha-yatskivska/python-lessons/tree/main/strings/exercises).
* Often when we are searching for a string using **find()** we first convert the string to lower case so we can search a string regardless of case. [Program](https://github.com/olha-yatskivska/python-lessons/tree/main/strings/exercises)
---
# Search and Replace
* The **replace()** function is like a "search and replace" operation in a word processor.  
* It replaces *all occurrences* of the search string with replacement string [Program](https://github.com/olha-yatskivska/python-lessons/blob/main/strings/exercises/search-and-replace.py)

---
## Stripping Whitespace
* **lstrip()** and **rstrip()** remove whitespace at the left or right.
* **strip()** remove both beginning and ending whitespace. [Program](https://github.com/olha-yatskivska/python-lessons/blob/main/strings/exercises/stripping-whitespace.py)
---
> In Python 3 all strings are Unicode
