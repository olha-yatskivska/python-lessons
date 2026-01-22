import re

name = input ("Enter file:")
try:
  fhandle = open(name)
except: 
  print("Print cannot be opened:", name)
  quit()
numlist = list()
for line in fhandle:
  line = line.rstrip()
  numbers = re.findall('[0-9]+' , line)
  if len(numbers) > 0: 
    for n in numbers:
      numlist.append(n)

print(len(numlist), sum(numlist))


