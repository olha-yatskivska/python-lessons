# 🐍  Files In Python

---
> **File Processing**: A text file can be thought of as a sequence of lines.
> A text file has newlines at the end of each line (\n)
---
## Opening Files
* The **open()** function tells Python which file we are going to work with and what we will be doing with the file.
* Open() returns a *"file handle"* - variable used to perform operations on the file.
```python
fhand = open('mbox.txt','r')
```
* handle = open(filename, mode).
* Returns a handle use to manipulate the file.
* Filename is a string.
* Mode is optional and should be 'r' - read or 'w' write.

## Reading Files
* A **file handle** open for read can be treated as a sequence of strings where each line in the file is a string in the sequence.
* We can use the **for** statement to iterate through a sequence.
* ! Remember - a sequence is an ordered set.
```python
xfile = open('mbox.txt')
for cheese in xfile:
    print(cheese)
```
* **Reading the "Whole" File**: We can read the whole file (newlines and all) into a single string [Program](https://github.com/olha-yatskivska/python-lessons/blob/main/files/exercises/reading-whole-file.py)

---
## Counting Lines in a File
* Open a file read-only.
* Use a for loop to read each line.
* Count the lines and print out the number of lines [Program](https://github.com/olha-yatskivska/python-lessons/blob/main/files/exercises/counting-lines-in-a%20file.py).
---
## Searching Through a File
* We can put an if statement in our for loop to only print lines that meet som criteria.
* We can strip the whitespace from the right-hand side of the string using rstrip() from the string library [Program](https://github.com/olha-yatskivska/python-lessons/blob/main/files/exercises/searching-through-file.py)
---
## Skipping with continue
* We can conveniently skip a line by using the *continue* statement [Program](https://github.com/olha-yatskivska/python-lessons/blob/main/files/exercises/skipping-with-continue.py)
---
## Using in to Selct Lines
* We can look for a string anywhere in a line as our selection criteria [Program](https://github.com/olha-yatskivska/python-lessons/blob/main/files/exercises/using-in-to-select-line.py)
* We can also prompt for File Name [Program](https://github.com/olha-yatskivska/python-lessons/blob/main/files/exercises/prompt-for-file-name.py)
---

