# Tuples in Python

## Tuples are immutable
* A tuple is a sequence of values much like a list.
* They have elements which are indexed starting at 0.
* Unlike a list, you cannot alter its contents - similar to a string.

```python
>>> x = ('Glenn', 'Sally', 'Joseph')
>>> print(x[2])
Joseph
>>> y = (1, 9, 2)
>>> print(y)
(1, 9, 2)
>>> print(max(y))
9
>>> for iter in y:
...   print(iter)
...
1
9
2
>>>
```
## Tuples are more efficient
* More efficient in terms of memory use and performance than lists.
* For "temporary variables" prefer tuples over lists

##  Tuples and Assignment
* we can put a tuple on the left-hand side of an assignment statement.
* We can even omit the parentheses

```python
>>> (x, y) = (4, 'fred')
>>> print (y)
fred
>>> (a, b) = (99, 98)
>>> print(a)
99
```

## Tuples and Dictionaries
* The items() method in dictionaries returns a lists of (key, value) tuples [Program](https://github.com/olha-yatskivska/python-lessons/blob/main/tuples/exercises/tuples-and-dictionaries.py)

## Tuples are Comparable
* The comparison operators work with tuples and other sequences.
* If the first item is equal, Python goes on to the next element, and so on, until it finds elements that differ.
* Once a comparison is resolved (e.g., $0 < 1$), Python stops comparing the remaining elements
[Program](https://github.com/olha-yatskivska/python-lessons/blob/main/tuples/exercises/top-10-most-common-words.pyq1)

---
## Sorting Lists of Tuples
* We can take advantage of the ability to sort a list of tuples to get a sorted version of a dictionary.
* First we sort the dictionary by the key using the items() method and sorted() function.
```python
>>> d = {'a': 10, 'c':22, 'b':1}
>>> d.items()
dict_items([('a', 10), ('c', 22), ('b', 1)])
>>> sorted(d.items())
[('a', 10),  ('b', 1), ('c', 22)]

```
---
* We can do this even more directly using the built-in function sorted that takes a sequence as a parameter and returns a sorted sequece [Program](https://github.com/olha-yatskivska/python-lessons/blob/main/tuples/exercises/sorted-function-by-key.py)

---
## Sort by values instead of key
* If we could construct a list of tuples of the form(value,key) we could sort by value
* We do this with a for loop that creates a list of tuples [Program](https://github.com/olha-yatskivska/python-lessons/blob/main/tuples/exercises/sorted-function-by-key.py)
---

##  Shorter Version
* List comprehension creates a dynamic list.
* In this case, we make a list of reversed tuples and then sort it. [Program](https://github.com/olha-yatskivska/python-lessons/blob/main/tuples/exercises/short-version-of-sorting.py)

---

