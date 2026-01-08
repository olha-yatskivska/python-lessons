fname = input('Enter file: ')
if len(fname) < 1 : fname = 'clown.txt'
fhand = open(fname)
for line in fhand :
  line = line.rstrip()
    
  wds = line.split()
  # print(wds)

  for w in wds: 
    print(w)
#print(fname, len(fname))
