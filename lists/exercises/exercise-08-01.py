# Exercise 1: Write a function called chop that takes a list and modifies it, removing the first and last elements, and returns None. 
# Then write a function called middle that takes a list and returns a new list that contains all but the first and last elements.

def chop(t):
  del t[0]

numbers = [5, 6, 7, 8, 9]
chop(numbers)
print(numbers)





