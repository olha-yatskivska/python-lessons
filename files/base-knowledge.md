# 🐍  Files In Python

---
> **File Processing**: A text file is a sequence of lines.
> Each line ends with a special "newline" character (\n).
---
## Opening Files
* The open() function establishes a connection between Python and the file on your disk.
* It returns a *"file handle"*  - a variable used to perform operations (read, write, close) on the file.
```python
fhand = open('mbox.txt','r')
```
* **Syntax:** handle = open(filename, mode).
* **Filename:** A string representing the path to the file.
* **Mode**: Optional. Common modes are 'r' (read) and 'w' (write).
---
> **The "Handle" Concept:** the handle is not the data itself, but a "pointer" or "connection" to the data.
---

## Reading Files
* A **file handle** open for read can be treated as a sequence of strings where each line in the file is a string in the sequence.
* We can use the **for** statement to iterate through a sequence.
* ! Remember - a sequence is an ordered set.
```python
xfile = open('mbox.txt')
for cheese in xfile:
    print(cheese)
```
* **Reading the "Whole" File**: If the file is small, you can use .read() and read the whole file (newlines and all) into a single string [Program](https://github.com/olha-yatskivska/python-lessons/blob/main/files/exercises/reading-whole-file.py)

---
## Counting Lines in a File
* Open a file read-only.
* Use a for loop to read each line.
* Count the lines and print out the number of lines [Program](https://github.com/olha-yatskivska/python-lessons/blob/main/files/exercises/counting-lines-in-a%20file.py).
---
## Searching Through a File
* **Filtering:** Use if statements inside the loop to find specific data (e.g., if line.startswith('From:')).
* **rstrip():** When reading a file, each line has a newline (\n) at the end. The print() function adds another newline. Use line.rstrip() to remove the extra whitespace from the right side so your output isn't double-spaced.
* **continue:** Use this to skip "uninteresting" lines and keep your code clean (the "guardian" pattern). [Program](https://github.com/olha-yatskivska/python-lessons/blob/main/files/exercises/searching-through-file.py)
---
## Skipping with continue
* We can conveniently skip a line by using the *continue* statement [Program](https://github.com/olha-yatskivska/python-lessons/blob/main/files/exercises/skipping-with-continue.py)
---
## Using in to Select Lines
* We can look for a string anywhere in a line as our selection criteria [Program](https://github.com/olha-yatskivska/python-lessons/blob/main/files/exercises/using-in-to-select-line.py)
* **Dynamic Filenames:** Use input() to let the user type the filename. 
* **Reliability:** Always wrap open() in a try...except block to handle cases where the user types a filename that doesn't exist. [Program](https://github.com/olha-yatskivska/python-lessons/blob/main/files/exercises/prompt-for-file-name.py)
---

