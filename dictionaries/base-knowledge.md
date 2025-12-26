# 🐍 Python Dictionaries
---
> ## What is Collection?
> * We have a bunch of values in a single "variable".
> * We do this by having more one place "in" the variable.
> * We have ways of finding the different places in the variable.
> * **Variables:** have one value in them - when put a new value in the **variable** - the old value is overwritten -  x = 2.
> * **List:** a linear collection of values. Lookup by position 0....length - 1.
> * **Dictionary:** a linear collection of key-value pairs/ Lookup by "tag" or "key".
---

## Lists vs Dictionaties
* We append values to the end of a List and look them up by position.
```python
>>> cards = list()
>>> cards.append(12)
>>> cards.append(3)
>>> cards.append(75)
>>> print(cards)
[12, 3, 75]
>>> cards[1] + 2
>>> print(cards)
[12, 5, 75]
```
* We insert values into a Dictionary using a key and retrieve them using a key.
```python
>>> cabinet = dict()
>>> cabinet.['summer'] = 12
>>> cabinet.['fall'] = 3
>>> cabinet.['spring'] = 75
>>> print(cabinet)
{'summer': 12, 'fall': 3, 'spring': 75}
>>> print(cabinet['fall'])
3
>>> cabinet['fall'] = cabinet['fall'] + 2
>>> print(cabinet)
{'summer': 12, 'fall': 5, 'spring': 75}
```
---
  
