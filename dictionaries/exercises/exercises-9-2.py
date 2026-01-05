# Exercise 2: Write a program that categorizes each mail message by which day of the week the commit was done. 
# To do this look for lines that start with “From”, then look for the third word and keep a running count of each of the days of the week. 
# At the end of the program print out the contents of your dictionary (order does not matter).
counts = dict()
name = input("Enter file:")
fhandle = open(name)
for line in fhandle :
  line = line.rstrip()
  words = line.split()
  if len(words) < 3 or words[0] != 'From':
    continue
  if words[0] == 'From' :  
    print(words[2])
    
    
    for words[2] in line:
      
      counts[word] = counts.get(word,0) + 1
      print(counts)
