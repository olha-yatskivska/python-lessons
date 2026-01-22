#Exercise 2: Write a program to look for lines of the form:
#New Revision: 39772
#Extract the number from each of the lines using a regular expression and the findall() method. 
#Compute the average of the numbers and print out the average as an integer.

import re

numlist = list()
name = input('Enter file name:')
try: 
  fhand = open('mbox-short.txt')
except:
  print("File cannot be opened:", name)
  quit()

for line in fhand:
  line = line.rstrip()
  numbers = re.findall('^New Revision: ([0-9]+)', line)
  if len(numbers) !=1 : continue
  num = float(numbers[0])
  numlist.append(num)
  average = sum(numlist)/len(numlist)
print(average)
