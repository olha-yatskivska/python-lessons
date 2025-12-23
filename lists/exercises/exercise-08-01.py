# Exercise 1: Write a function called chop that takes a list and modifies it, removing the first and last elements, and returns None. 
# Then write a function called middle that takes a list and returns a new list that contains all but the first and last elements.
numbers = [5, 6, 7, 8, 9]
min_numbers = [5, 6]
one_element = [7]
letters = ['a', 'b', 'c', 'd', 'e']

def chop(t):
   if len(t) < 2:
    print('Give me more numbers')
    return
   else: 
    del t[0]
    del t[-1] 
    

test_me = letters
chop(test_me)
print(test_me)



def middle(t):
  if len(t) < 2:
     print('Give me more numbers')
     return
  else: 
     return t[1:-1]
 
    
  
test_me = letters
rest = middle(letters)
print(rest)

  
