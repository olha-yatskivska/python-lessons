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
>>> friends = ['Joseph', 'Glenn', 'Sally']
>>> print(friends[1])
Glenn
```
## Lists are Mutable
* Strings are "immutable" - we cannot change the contents of a string - we must make a new string to make any change.  
* Lists are "mutable" - we can change an element of a list using the index operator. [Program](https://github.com/olha-yatskivska/python-lessons/blob/main/lists/exercises/changing-element-in-list.py)
---
## Length of a List
* The len() function takes a list as a parameter and returns the number of elements in the list.
* Actually len() tells us the number of elements of any set of sequence (such as a string) [Program](https://github.com/olha-yatskivska/python-lessons/tree/main/lists/exercises)
---
## Using the range Function
* The range function returns a list of numbers that range from zero to one less than the parameter. [Program](https://github.com/olha-yatskivska/python-lessons/tree/main/lists/exercises)
```python
>>> print(range(4))
[0, 1, 2, 3]
>>> friends = ['Joseph', 'Glenn', 'Sally']
>>> print(len(friends))
3
>>> print(list(range(len(friends))))
[0, 1, 2]
```
* We can construct an index loop using for and an integer iteration. [Program](https://github.com/olha-yatskivska/python-lessons/blob/main/lists/exercises/loops-with-list.py)
---
## Concatenating Lists
* We can concatenating Lists using '+'.
* We can create a new list by adding two existing lists together. [Program](https://github.com/olha-yatskivska/python-lessons/blob/main/lists/exercises/concatenating.py)
---
## Lists Can be Sliced
* Just like in strings, the second number is "up to but not including" [1:3] [Program](https://github.com/olha-yatskivska/python-lessons/blob/main/lists/exercises/sliced-lists.py)
---
## List Methods

---
> Text and Binary Sequence Type Methods Summary [**List Methods**](https://docs.python.org/3/library/stdtypes.html#lists)
---

## Building a List from Scratch:
* We can create an empty list and then add elements using the append method.
* The list stays in order and new elements are added at the end of the list. [Program](https://github.com/olha-yatskivska/python-lessons/blob/main/lists/exercises/scratch.py)
---

## Searching in List 
* Python provides two operators that let you check if an item is is a list.
* These are logical operators that return True or False.
* They do not modify the list. [Program](https://github.com/olha-yatskivska/python-lessons/tree/main/lists/exercises)

---
## Lists are in Order
* A list can hold many items and keeps those items in the order until we do something to change the order.
* A list can be sorted (i.e., change its order).
* The sort method (unlike in strings) means "sort yourself" [Program](https://github.com/olha-yatskivska/python-lessons/blob/main/lists/exercises/ordered-list.py)


