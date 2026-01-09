# Exercise 4: Add code to the above program to figure out who has the most messages in the file. 
# After all the data has been read and the dictionary has been created, look through the dictionary using a maximum loop 
# (see Chapter 5: Maximum and minimum loops) to find who has the most messages and print how many messages the person has.

#Enter a file name: mbox-short.txt
#cwen@iupui.edu 5

#Enter a file name: mbox.txt
#zqian@umich.edu 195

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
  if len(words) < 3 or words[0] != 'From':
    continue
  
  mail = words[1]   
  counts[mail] = counts.get(mail,0) + 1
  #print(mail)
# Find the word with largest count
messages = None
most = None
for cle, valeur in mail.items() :
  print(cle, valeur)
  if messages is None or valeur  > messages  :
    messages = valeur
    most = cle

print(most, messages)
  
#print(counts)
