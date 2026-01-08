fname = input('Enter file: ')
if len(fname) < 1 : fname = 'clown.txt'
fhand = open(fname)
for line in fhand :
  line = line.rstrip()
  # print(line)
  
  wds = line.split()
  print(wds)
#print(fname, len(fname))
