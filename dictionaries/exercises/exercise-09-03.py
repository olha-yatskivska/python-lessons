# Exercise 3: Write a program to read through a mail log,
# build a histogram using a dictionary to count how many messages have come from each email address, 
#and print the dictionary.

#Enter file name: mbox-short.txt
#{'gopal.ramasammycook@gmail.com': 1, 'louis@media.berkeley.edu': 3,
#'cwen@iupui.edu': 5, 'antranig@caret.cam.ac.uk': 1,
#'rjlowe@iupui.edu': 2, 'gsilver@umich.edu': 3,
#'david.horwitz@uct.ac.za': 4, 'wagnermr@iupui.edu': 1,
#'zqian@umich.edu': 4, 'stephen.marquard@uct.ac.za': 2,
#'ray@media.berkeley.edu': 1}

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
  #counts[day] = counts.get(day,0) + 1
  print(mail)
  
#print(counts)
