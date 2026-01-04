# Write a program that reads the words in words.txt and stores them as keys in a dictionary
# It doesn’t matter what the values are
# Then you can use the in operator as a fast way to check whether a string is in the dictionary


name = "mbox-short.txt"
handle = open(name)

programs = dict()
 for line in handle :
  words = line.split()
   for word in words :
     counts[words] = counts.get(word,0) + 1
     
