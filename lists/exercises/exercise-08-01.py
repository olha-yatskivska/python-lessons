# Exercise 1: Write a function called chop that takes a list and modifies it, removing the first and last elements, and returns None. 
# Then write a function called middle that takes a list and returns a new list that contains all but the first and last elements.
numbers = [5, 6, 7, 8, 9]
min_numbers = [5, 6]


def chop(t):
  del t[0]
  del t[-1] 

test_me = min_numbers
chop(test_me)
print(test_me)



def middle(t):
  return t[1:-1]
  
test_me = min_numbers
rest = middle(test_me)
print(rest)

  
