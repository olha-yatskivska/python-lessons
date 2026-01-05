fname = input('Enter file: ')
if len(fname) < 1 : fname = 'clown.txt'
fhand = open(fname)
for line in fhandle :
  line = line.rstrip()
  print(line)
  
#print(fname, len(fname))
