* __dict__ attribute contains a dictionary of an object's writable attributes and their values, useful for inspecting or modifying an object's properties dynamically
* creating a dictionary using a comprehension in Python {key: value for key, value in iterable}
* oct() int into base-8. # oct(23): 23 / 8 = 2 with 7.  Result: + prefix Oo '0o27'
* creating a multiline f-string with triple quotes where literal newlines are considered part of the string. However, any spaces at the start of the line would also be part of the string, so it can mess with code indentation.
```python
multiline_string = f"""I will {string1} there.
I will go {string2}.
{string3}."""
```
* " ".join(list) -  converting a list of strings to a single string in Python
* y = filter(lambda a: a % 2 == 0, x) filter() function keeps only elements where the lambda returns True. Here, it keeps even numbers, so the output is [2, 4]
* enumerate() function the purpose is to get the index and value of each item in an iterable
* key in dictionary - check if a key is present in a dictionary
* A variable in Python is a named location in memory used to store data values.
* isinstance(var, int)  checking if a variable is of a specific type in Python
* the scope of a global variable in Python is Limited to the module it is defined in
* dentifiers must start with a letter or underscore and can contain letters, digits and underscores. Names cannot start with a digit, contain hyphens or be Python keywords (like global).
* Class is a user defined data type
* Lists always maintain insertion order. Starting from Python 3.7, dictionaries (dict) also maintain the insertion order of keys by default.
*  The bitwise OR operator | is overloaded by the special method __or__() in Python. You can define this method in your class to customize the behavior of |
*  The break statement is used to exit a loop prematurely.
*  The try-except block is used to handle exceptions in Python.
*  The if statement is used to execute a block of code only if a specified condition is true.
*  The else statement is executed when the if condition is false. The else clause is executed when the loop completes its iterations without encountering a break statement.
*  The elif statement is used to check additional conditions if the initial if statement is false.
*  The range function is used to generate a sequence of numbers that can be iterated over in a for loop.
* The enumerate function is used to iterate over both the index and the value of elements in an iterable.
* The reversed function can be used to iterate over a string in reverse order.
* enumerate() provides both index and value during iteration.
* Using a for loop directly iterates over the elements of a tuple.
* The nested for loop prints combinations of i and j.
* The primary purpose of a for loop is to iterate over a sequence or iterable, executing a block of code for each iteration.
* Using a for loop directly iterates over the characters of a string.
* The else block after a for loop executes only if the loop completes without a break. If break runs, else is skipped.
* In Python, to iterate over both the keys and values of a dictionary, you can use the items() method, which returns a view of the dictionary's key-value pairs. Here's how you do it:
```python
for key, value in dictionary.items():
```
* The pass statement is a no-operation statement used when a statement is syntactically required but no action is desired.
* For loops iterate over a sequence (iterables).
* While loops repeat as long as a condition is True.
* Both can be used for iteration, but for loops are more concise with known sequences.
* The continue keyword is used to skip the remaining code inside the loop and move to the next iteration.
* By using a negative step in the range function, you can iterate over the elements of a list in reverse order.
* range(start, end, step) the range function is commonly used with a for loop to generate a sequence of numbers with a specified start, end, and step.
---
### While loop
* You can use the range function with the length of the list to iterate over its indices using a while loop.
* While loops can be used to iterate over the keys of a dictionary.
* You can use a custom exception and handle it outside the loop to achieve a similar effect to the break statement.
* A while loop can have at most one else block.
* The assert statement is used for debugging purposes to check if a condition is true. If it's not, an AssertionError is raised.
* The else block in a while loop is executed when the loop condition becomes False without encountering a break statement.
* The continue statement skips the remaining code inside the loop and moves to the next iteration.
* The basic syntax of a while loop in Python is while (condition):
* locals() function returns a dictionary of the current local symbol table, providing access to all local variables in the current scope.
* Python doesn't have a do-while loop that guarantees execution at least once. To mimic this, you can use a while loop with a condition set to True and use a break statement inside the loop to exit based on your logic. This ensures the loop body runs at least once
* An infinite loop can be avoided by ensuring there is a condition that evaluates to False at some point.
* A while loop with the condition True will run indefinitely until interrupted.
* While loops execute as long as a condition is true (entry-controlled), whereas for loops iterate over a sequence with a predetermined number of iterations (exit-controlled).
---
### List
* The task of the index is to find the position of a supplied value in a given list. #pos = nameList.index("name")
* REVERSE() reverses the list and returns it.
* pop() will delete and return the element whose index was passed as parameter.
* The zip() function in Python combines multiple iterables such as lists, tuples, strings, dict etc, into a single iterator of tuples where each tuple contains elements from the input iterables at the same index.
* In the given code the lists 'a' and 'b' are combined by the zip method and then the difference between the elements from a and b are added to the new list ( subtracted ).
* In python list slicing can also be done by using the syntax listName[x:y:z] where x means the initial index, y-1 defines the final index value and z specifies the step size. If anyone of the values among x, y, and z is missing the interpreter takes the default value.
* The beauty of python list datatype is that within a list, a programmer can nest another list, a dictionary, or a tuple.
* In python, we can slice a list but we can also slice an element within the list if it is a string. The declaration list[x][y] will mean that ‘x’ is the index of the element within a list and ‘y’ is the index of an entity within that string.

---
### String
* Strings in Python are sequences (arrays) of Unicode characters used to store and work with text.
* The join() method in Python is a built-in string method that is used to concatenate (join) a sequence of strings into a single string.
* Triple quotes allow you to use both single and double quotes inside the string without escaping them.
* In python repr() function ensure that the escape sequences are displayed as part of the string rather than being processed.
* Python strings are immutable. This means that once a string is created, it cannot be modified. Any operation that seems to modify a string will instead create a new string.
* In Python, the find() method is used to search for a substring within a string. It returns the index of the first occurrence of the substring. If the substring is not found, it returns -1.
* In Python, the startswith() method is used to check whether a string starts with a specified prefix. It returns True if the string starts with the given prefix, otherwise, it returns False.
* The title() method in Python converts the first character of each word in a string to uppercase and the rest of the characters to lowercase.
* For a string of length n and a substring of length m, the find() method compares each possible starting position in the string where the substring could fit, and checks for a match. If no match is found, it will continue until the end of the string.
* Therefore the time complexity for find() in O(n) where n is the length of the string.
* In Python, the count() method counts the occurrences of a substring within a string. It returns the number of non-overlapping occurrences of the specified substring.
* n Python, the isalpha() method is used to check whether all characters in a string are alphabetic (i.e., they are letters).
* The method returns True if all characters in the string are alphabetic and the string is non-empty, otherwise, it returns False.
* The strip() method in Python is used to remove leading and trailing whitespaces (spaces, tabs, newlines, etc.) from a string. It can also remove specific characters if provided as an argument.
* expandtabs() method is best suited to replace all tab characters with whitespace using the given tab size
* re.compile() function compiles a regular expression pattern into a Regex object, which can be used for matching and searching efficiently.
* translate() function modifies a string based on a translation table created using maketrans().

### Tuples
* Elements in tuples is compared one by one. So, when it compares 4 with 3 it will return False.
* The ‘*’ operator is used to concatenate tuples.

### Dictionaries
* Mutable members can be used as the values of the dictionary but they cannot be used as the keys of the dictionary
* del deletes the entire dictionary and any further attempt to access it will throw an error.
* in is used to check the key exist in the dictionary or not (True/False)
* The ‘>’ operator is not supported between instances of two dictionaries in Python 3.
* Tuples can be used for keys into dictionary. The tuples can have mixed length and the order of the items in the tuple is considered when comparing the equality of the keys.
* Dictionaries were unordered in Python versions before 3.7, so the output order can vary in older versions, matching option D.
* In Python 3.7 and later, dictionaries keep the order of insertion, so the output will match the order items were added, hence the option 'A' is correct..
* A dictionary can hold any value such as an integer, string, list or even another dictionary holding key value pairs.
* dictionary1.update(dictionary2) is used to update the entries of dictionary1 with entries of dictionary2. If there are same keys in two dictionaries, then the value in the second dictionary is used.
* The values of a dictionary can be accessed using keys but the keys of a dictionary can’t be accessed using values.
* The all() method returns: True – If all elements in an iterable are true ot iterable is empty. False – If any element in an iterable is false.
* fromkeys() method returns a new dictionary but does not modify the original dictionary
---
### Functions
* 
