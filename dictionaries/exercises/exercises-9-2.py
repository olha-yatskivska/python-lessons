
name = input("Enter file:")
handle = open(name)
counts = dict()

for words in line :
  words = line.split()
  for word in words :
    word = counts[word] = counts.get(word,0) + 1
print('Counts', counts)
