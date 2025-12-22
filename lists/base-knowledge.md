# 🐍  Python Lists 

---
> ## Programming
> **Algorith:** a set of rules or steps used to solve a problem.
> 
> **Data Structure:** a particular way of organizing data in computer.
---

## A List is a Kind of Collection
* A collection allows us to put many values in a single "variable".
* A collection is nice because we can carry all many values around in one convenient package.
```python
friends = ['Joseph', 'Glenn', 'Sally']
carryon = ['socks', 'shirt', 'perfume']
```
## List Constants
* List constatnts are surrounded by square brackets and the elements in the list are separated by commas.
* A list element can be any Python object - even another list.
* A list can be empty.
* Lists and Definite Loops work together
```python
friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends :
    print('Happy New Year:', friend)
print('Done!')

z = ['Joseph', 'Glenn', 'Sally']
for x in z:
    print('Happy New Year', x)
print('Done!')
```
## Looking Inside Lists
* Just like strings, we can get at any single element in a list using an index specified in square brackets.
```python
friends = ['Joseph', 'Glenn', 'Sally']
print(friends[1])
>>> Glenn
```
## Lists are Mutable
* Strings are "immutable" - we cannot change the contents of a string - we must make a new string to make any change.  
* Lists are "mutable" - we can change an element of a list using the index operator. [Program]()
