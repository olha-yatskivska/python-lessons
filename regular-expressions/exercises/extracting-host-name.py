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
words = data.split()
email=words[1]
pieces = email.split('@')
print(pieces[1])

#the regex version
import re
lin = 'From stephen.marquard@utc.ac.za Sat Jan 5 09:14:16 2008'
y = re.findall('^From .*@([^ ]*)',lin)
print(y)
