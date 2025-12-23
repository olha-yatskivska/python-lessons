# 🐍  Python Lists 

---
> ## Programming
> **Algorith:** a set of rules or steps used to solve a problem.
> 
> **Data Structure:** a particular way of organizing data in computer.
---

## Concept of collection
* A collection allows us to put many values in a single "variable".
* A collection is nice because we can carry all many values around in one convenient package.
```python
friends = ['Joseph', 'Glenn', 'Sally']
carryon = ['socks', 'shirt', 'perfume']
```
## Lists and definie loops
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
## Indexing and lookup
* Just like strings, we can get at any single element in a list using an index specified in square brackets.
```python
>>> friends = ['Joseph', 'Glenn', 'Sally']
>>> print(friends[1])
Glenn
```
## List mutability
* Strings are "immutable" - we cannot change the contents of a string - we must make a new string to make any change.  
* Lists are "mutable" - we can change an element of a list using the index operator. [Program](https://github.com/olha-yatskivska/python-lessons/blob/main/lists/exercises/changing-element-in-list.py)
---
## Length of a List
* The len() function takes a list as a parameter and returns the number of elements in the list.
* Actually len() tells us the number of elements of any set of sequence (such as a string) [Program](https://github.com/olha-yatskivska/python-lessons/blob/main/lists/exercises/length-of-list.py)
---
## Using the range Function
* The range function returns a list of numbers that range from zero to one less than the parameter. [Program](https://github.com/olha-yatskivska/python-lessons/blob/main/lists/exercises/length-vs-range.py)
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
## Slicing lists
* Just like in strings, the second number is "up to but not including"
```python
t = [9, 41, 12, 3, 74, 15]
t = [1:3]
t = [:4]
t = [3:]
t = [:]
```
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
* They do not modify the list. [Program](https://github.com/olha-yatskivska/python-lessons/blob/main/lists/exercises/searching-in-list.py)

---
## Sorting lists
* A list can hold many items and keeps those items in the order until we do something to change the order.
* A list can be sorted (i.e., change its order).
* The sort method (unlike in strings) means "sort yourself" [Program](https://github.com/olha-yatskivska/python-lessons/blob/main/lists/exercises/ordered-list.py)
---
## Built-in Functions and Lists
* There are number of functions built into Python that take lists as parameters.
* Simple version of the loop: [Program](https://github.com/olha-yatskivska/python-lessons/blob/main/lists/exercises/built-in-functions.py)
* Two versions of calculation average: [Program](https://github.com/olha-yatskivska/python-lessons/blob/main/lists/exercises/average.py) Version with list uses more memory.
---
## Splitting strings into lists of words
* Split breaks a string into parts and produces a list of strings.
* We think of these as words.
* We can access a particular word or loop through all the words. [Product](https://github.com/olha-yatskivska/python-lessons/blob/main/lists/exercises/string-into-list.py)
* When you do not specify a delimiter, multiple spaces are treated like one delimiter.
* You can specify what delimiter character to use in the splitting. [Product](https://github.com/olha-yatskivska/python-lessons/blob/main/lists/exercises/split.py)
----
## Using split to parse strings
* Sometimes we split a line one way, and then grab one of the pieces of the line and split that piece again. [Product](https://github.com/olha-yatskivska/python-lessons/blob/main/lists/exercises/split.py)

---


## Best practice
* **Don’t forget that most list methods modify the argument and return None:**
```python
word = word.strip()
t = t.sort()           # WRONG!
```
---
## ⚠️ Read the documentation
> * The methods and operators that lists share with other sequences (like strings) are documented at:  [Library](https://docs.python.org/3/library/stdtypes.html#common-sequence-operations)
> * The methods and operators that only apply to mutable sequences are documented at: [Library](https://docs.python.org/3/library/stdtypes.html#mutable-sequence-types)
---

* **Pick an idiom and stick with it:**  there are too many ways to do things with lists. For example, remove an element from a list, you can use pop, remove, del, or even a slice assignment. To add an element, you can use the append method or the + operator.
```python
 # these are right:
t.append(x)
t = t + [x]

# And these are wrong:
t.append([x])          # WRONG!
t = t.append(x)        # WRONG!
t + [x]                # WRONG!
t = t + x              # WRONG!
```
* **Make copies to avoid aliasing:** If you want to use a method like sort that modifies the argument, but you need to keep the original list as well, you can make a copy.
```python
orig = t[:]
t.sort()
```
* **Lists, split, and files:**  it is a good idea to revisit the guardian pattern when it comes to writing programs that read through a file and look for a “needle in the haystack”.  The best place to add the print statement is right before the line where the program failed and print out the data that seems to be causing the failure. [Program](https://github.com/olha-yatskivska/python-lessons/blob/main/lists/exercises/dow.py)
```python
fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    words = line.split()
    # print('Debug:', words)
    if len(words) == 0 : continue
    if words[0] != 'From' : continue
    print(words[2])
```

