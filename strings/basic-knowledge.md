
# String Data Type

* A string is a sequence of characters.
* A string uses quotes 'Hello' or "Hello".
* For strings, + means "concatenate".
* When a string contains numbers, it is still a string.
* We can convert numbers in a string into a number using int().
* **Length of strings:** the function len gives us the length of a string.
* 

---
## Reading and Converting

* We prefer to read data in using strings and then parse and convert the data as we need.
* This gives us more control over erroe situations and/or bad user input.
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
  
