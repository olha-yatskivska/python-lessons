fname = input('Enter file: ')
if len(fname) < 1 : fname = 'clown.txt'
fhand = open(fname)
many = dict()

for line in fhand :
  line = line.rstrip()
    
  wds = line.split()
  # print(wds)

  for w in wds: 
    print('===>', w)
    print('before', many)
    oldvalue = 0
    if w in many : oldvalue = many[w]
    many[w] =  oldvalue + 1
    print('after', many)
    

print(many)
