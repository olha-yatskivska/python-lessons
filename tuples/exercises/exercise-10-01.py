#Exercise 1: Revise a previous program as follows: Read and parse the “From” lines and pull 
#out the addresses from the line. Count the number of messages from each person using a dictionary.

#After all the data has been read, print the person with the most commits by creating a list of 
#(count, email) tuples from the dictionary. Then sort the list in reverse order and print out the
#person who has the most commits.

counts = dict()
name = input("Enter file:")
try:
  fhandle = open(name)
except:
  print("File cannot be opened:", name)
  quit()

for line in fhandle:
  line = line.rstrip()
  words = line.split()
  if len(words) < 2 or words[0] != 'From':
    continue

  email = words[1]
  counts[email] = counts.get(email,0) + 1
#print(counts.items())
  
tmp = dict()
newlist = list()
for k, v in counts.items() :
  tup = (v, k)
  newlist.append(tup)
  answer = sorted(newlist, reverse=True)

  
  for v, k in answer[:1] :
    print(k, v)

