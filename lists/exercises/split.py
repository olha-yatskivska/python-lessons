line = 'From stephen.marquard@uct.ac.za Sat Jan    5   09:14:16 2008'
words = line.split()
print(words)

fhand = open('mbox-short.txt')
for line in fhand:
  line = line.rstrip()
  if not line.startswith('From ') : continue 
  words = line.split()
  print(words[2])

#the double split pattern
# 1. words = line.split()
email = words[1]
pieces = email.split('@')
print(pieces[1])
