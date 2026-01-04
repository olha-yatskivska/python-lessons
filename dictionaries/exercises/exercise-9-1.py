# Write a program that reads the words in words.txt and stores them as keys in a dictionary
# It doesn’t matter what the values are
# Then you can use the in operator as a fast way to check whether a string is in the dictionary


name = "words.txt"
handle = open(name)

new_dict = dict()
for line in handle:
  words = line.split()
  for word in words:
    new_dict[words] = counts.get(word,0) + 1

print(new_dict)
     
