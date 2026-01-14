# Regular Expressions 

[Regular expression operations](https://docs.python.org/3/library/re.html)
---
[regular expressions](https://regex101.com/)

| **Special characters** | **Meaning** | 
| :--- | :--- |
|^ |Matches the beginning of the line.|
|$| Matches the end of the line.|
|.| Matches any character (a wildcard).|
|\s| Matches a whitespace character.|
|\S| Matches a non-whitespace character (opposite of \s).|
|*| Applies to the immediately preceding character(s) and indicates to match zero or more times.|
|*?| Applies to the immediately preceding character(s) and indicates to match zero or more times in “non-greedy mode”.|
|+| Applies to the immediately preceding character(s) and indicates to match one or more times.|
|+?| Applies to the immediately preceding character(s) and indicates to match one or more times in “non-greedy mode”.|
|?| Applies to the immediately preceding character(s) and indicates to match zero or one time.|
|??| Applies to the immediately preceding character(s) and indicates to match zero or one time in “non-greedy mode”.|
|[aeiou]| Matches a single character as long as that character is in the specified set. In this example, it would match “a”, “e”, “i”, “o”, or “u”, but no other characters.|
|[a-z0-9]| You can specify ranges of characters using the minus sign. This example is a single character that must be a lowercase letter or a digit.|
|[^A-Za-z]| When the first character in the set notation is a caret, it inverts the logic. This example matches a single character that is anything other than an uppercase or lowercase letter.|
|( ) |When parentheses are added to a regular expression, they are ignored for the purpose of matching, but allow you to extract a particular subset of the matched string rather than the whole string when using findall().|
|\b| Matches the empty string, but only at the start or end of a word.|
|\B| Matches the empty string, but not at the start or end of a word.|
|\d| Matches any decimal digit; equivalent to the set [0-9].|
|\D| Matches any non-digit character; equivalent to the set [^0-9].|

## The Regular Expressin Module
* The regular expression module re must be imported into your program before you can use it.
* You can use re.search() to see if a string matches a regular expression, similar to using the find() method for strings. [Program](https://github.com/olha-yatskivska/python-lessons/blob/main/regular-expressions/exercises/search-function.py)
*  The caret character is used in regular expressions to match “the beginning” of a line. [Program](https://github.com/olha-yatskivska/python-lessons/blob/main/regular-expressions/exercises/search-with-start-with.py)
---
## Character matching in regular expressions
* The most commonly used special character is the period or full stop, which matches any character. [Program](https://github.com/olha-yatskivska/python-lessons/blob/main/regular-expressions/exercises/character-matching.py)
* using the * or + characters in your regular expression. These special characters mean that instead of matching a single character in the search string, they match zero-or-more characters (in the case of the asterisk) or one-or-more of the characters (in the case of the plus sign). [Program](https://github.com/olha-yatskivska/python-lessons/blob/main/regular-expressions/exercises/wild-card-character.py)
* [more details](https://docs.python.org/3/library/re.html)
---
## Extracting data using regular expressions
* This following program uses findall() to find the lines with email addresses in them and extract one or more addresses from each of those lines. [Program](https://github.com/olha-yatskivska/python-lessons/blob/main/regular-expressions/exercises/find-all-2.py)
---
## Combining searching and extracting 
* Translating this, we are saying, we want lines that start with X-, followed by zero or more characters (.*), followed by a colon (:) and then a space. [Program](https://github.com/olha-yatskivska/python-lessons/blob/main/regular-expressions/exercises/search-for-lines-start-with.py)
---
## The translation of this regular expression is that we are looking for lines that start with From (note the space), followed by any number of characters (.*), followed by a space, followed by two digits [0-9][0-9], followed by a colon character. This is the definition of the kinds of lines we are looking for.
[Program](https://github.com/olha-yatskivska/python-lessons/blob/main/regular-expressions/exercises/search-for-lines.py)

---
## Escape character
* We can indicate that we want to simply match a character by prefixing that character with a backslash. For example, we can find money amounts with the following regular expression.
```python
import re
x = 'We just received $10.00 for cookies.'
y = re.findall('\$[0-9.]+',x)
```


  

