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
  numbers = re.findall(r'\d+' , line)
  if len(numbers) > 0: 
    num = int(numbers[0])
    numlist.append(num)

print(len(numlist))


