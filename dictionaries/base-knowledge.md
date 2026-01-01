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
>>> cards[1] + 2
>>> print(cards)
[12, 5, 75]
```
* **Dictionary:** a linear collection of key-value pairs looking up by "tag" or "key".
* We insert values into a Dictionary using a key and retrieve them using a key.
* Python 3.7 (2018) and later dixtionaries keep entries in the order they were inserted.
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
## 

  
