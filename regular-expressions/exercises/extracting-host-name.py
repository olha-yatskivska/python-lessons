# using find and string slicing
data = 'From stephen.marquard@utc.ac.za Sat Jan 5 09:14:16 2008'
atpos = data.find('@')
print(atpos)
sppos = data.find(' ',atpos)
print(sppos)
host = data[atpos+1 : sppos]
print(host)

# the double split pattern

data = 'From stephen.marquard@utc.ac.za Sat Jan 5 09:14:16 2008'

for line in fhandle:
  words = line.split()
  email=words[1]
  pieces = email.split('@')
print(pieces[1])
