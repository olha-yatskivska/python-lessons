import sys 
tup = tuple() 
print(sys.getsizeof(tup), end = " ") 
tup = (1, 2) 
print(sys.getsizeof(tup), end = " ") 
tup = (1, 3, (4, 5)) 
print(sys.getsizeof(tup), end = " ") 
tup = (1, 2, 3, 4, 5, [3, 4], 'p', '8', 9.777, (1, 3)) 
print(sys.getsizeof(tup)) 
