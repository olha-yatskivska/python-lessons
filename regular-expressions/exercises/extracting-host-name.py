# using find and string slicing
data = 'From stephen.marquard@utc.ac.za Sat Jan 5 09:14:16 2008'
atpos = data.find('@')
print(atpos)
sppos = data.find('',atpos)
print(sppos)
host = data[atpos+1 : sspos]
print(host)
