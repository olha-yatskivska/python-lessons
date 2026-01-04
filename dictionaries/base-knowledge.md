# 🐍 Python Dictionaries
---

## Lists vs Dictionaties
* **List:** a linear collection of values. Lookup by position 0....length - 1.
* We append values to the end of a List and look them up by position.
```python
>>> cards = list()
>>> cards.append(12)
>>> cards.append(3)
>>> cards.append(75)
>>> print(cards)
[12, 3, 75]
>>> cards[1] = cards[1] + 2
>>> print(cards)
[12, 5, 75]
```
* **Dictionary:** a linear collection of key-value pairs looking up by "tag" or "key".
* We insert values into a Dictionary using a key and retrieve them using a key.
* Python 3.7 (2018) and later dixtionaries keep entries in the order they were inserted.
```python
>>> cabinet = dict()
>>> cabinet['summer'] = 12
>>> cabinet['fall'] = 3
>>> cabinet['spring'] = 75
>>> print(cabinet)
{'summer': 12, 'fall': 3, 'spring': 75}
>>> print(cabinet['fall'])
3
>>> cabinet['fall'] = cabinet['fall'] + 2
>>> print(cabinet)
{'summer': 12, 'fall': 5, 'spring': 75}
```
---
## Dictionary Tracebacks
* It's an error to reference a key which is not in the dictionary.
* We can use the **in** operator to see if a key is in a dictionary:

```python
>>> ccc = dict()
>>> print(ccc['csev'])
Traceback (most recent call last):
  File "<stdin>", line ,, in <module>
KeyError: 'csev'
>>> 'csev' in ccc
False
```
## Simplified counting with get() method
* A **get() method** is for  checking  if a key is already in a dictionary and assuming a default value if the key is not there.
* Default value if key does not exist (and no Traceback).

```python
if name in counts:
  x = counts[name]
else :
  x = 0

or can use next: 
x = counts.get(name, 0)

The same result:
{'csev':2, 'zqian': 1, 'cwen': 2}
```
---
## Counting Pattern
* The general pattern to count the words in a line of text is to split the line into words, then loop through the words and use a dictionary to track the count of each word independently. [Program](https://github.com/olha-yatskivska/python-lessons/blob/main/dictionaries/exercises/counting-pattern.py)
---
## Definite Loops and Dictionaries
* Historically, dictionaries were unordered, but now they maintain insertion order, we can write a for loop that goes through all the entries in dictionary and looks up the value [Program](https://github.com/olha-yatskivska/python-lessons/blob/main/dictionaries/exercises/definite-loops.py)

---
## Retrieving Lists of Keys and Values
* You can get a list of keys, values or items (both) from a dictionary [Program](https://github.com/olha-yatskivska/python-lessons/blob/main/dictionaries/exercises/retrieving-lists-of-keys-and-values.py)

---
## Two Iteration Variables
* We loop through the key-value pairs in a dictionary using *two* iteration variables.
* Each iteration, the first variable is the key and the second variable is the corresponding value for the key [Program](https://github.com/olha-yatskivska/python-lessons/blob/main/dictionaries/exercises/find-the-largest.py)
   
