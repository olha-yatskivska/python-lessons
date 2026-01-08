fname = input('Enter file: ')
if len(fname) < 1 : fname = 'clown.txt'
fhand = open(fname)
many = dict()

for line in fhand :
  line = line.rstrip()
    
  wds = line.split()
  # print(wds)

  for w in wds: 
    #print('===>', w)
    #print('before', many)
    #oldvalue = 0
    #if w in many : oldvalue = many[w]
    #oldvalue = many.get(w, 0)
 
    #print('oldvalue', oldvalue)
    #many[w] =  oldvalue + 1
    many[w] = many.get(w, 0) + 1
    #print('after', many)
   
print(many)

# Find the word with largest count
largest = None
for cle, valeur in many.items() :
  print(cle, valeur)
  if largest is None or largest > valeur :
    largest = valeur

print('Yay!!', largest)
