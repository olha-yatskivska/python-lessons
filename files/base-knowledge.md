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
## Counting Lines in a File
* Open a file read-only.
* Use a for loop to read each line.
* Count the lines and print out the number of lines [Program]()
