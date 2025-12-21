#Exercise 1: Write a program to read through a file and print the contents of the file (line by line) all in upper case. Executing the program will look as follows:
fn = input('Enter a file name: ')
fh = open(fn)

print(fh)

for lx in fh:
    ly = lx.rstrip()
    print(ly.upper())
