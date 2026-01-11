# Tuples in Python

## Tuples are immutable
* A tuplel is a sequence of values much like a list.
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
