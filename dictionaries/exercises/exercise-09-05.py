#Exercise 5: This program records the domain name (instead of the address) 
#where the message was sent from instead of who the mail came from (i.e., the whole email address). 
#At the end of the program, print out the contents of your dictionary.

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
  num  = mail.find('@') 
  domaim = mail[num-1 :]
  
  counts[domain] = counts.get(domain,0) + 1
  #print(mail)
  
print(counts)
