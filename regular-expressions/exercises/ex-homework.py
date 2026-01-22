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
  numbers = re.findall('([0-9.]+)' , line)

  #num = int(numbers[0])
  #numlist.append(num)
print(numbers)
#print(numlist)


