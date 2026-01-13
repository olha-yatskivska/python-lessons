#Exercise 2: This program counts the distribution of the hour of the day for each of the messages. You can pull the hour from the “From” line by finding the time string and then splitting that string into parts using the colon character. Once you have accumulated the counts for each hour, print out the counts, one per line, sorted by hour as shown below.

counts = dict()
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
try:
  fhandle = open(name)
except:
  print("File cannot be opened:", name)
  quit()

for line in fhandle:
  line = line.rstrip()
  words = line.split()
  if len(words) < 3 or words[0] != 'From':
    continue
  
  t = words[5].split(':')
    
  
    
  #num  = t.find(':') 
  #h = t[:num]
  
  counts[h] = counts.get(h,0) + 1
  print(mail)

#newlist = list()
#for k, v in counts.items() :
 # tup = (k,v)
 # newlist.append(tup)
 
#hours = sorted(newlist)

#print(hours[1], hours[0])


