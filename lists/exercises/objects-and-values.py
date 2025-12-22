# a and b refer to the same object
a = 'banana'
b = 'banana'
print(a is b)

# a and b refer to two different objects that have the same value
c = [1, 2, 3]
d = [1, 2, 3]
print(c is d)

# there are two references to the same object
a = [1, 2, 3]
a = b
print(b is a)

# the object with more than one reference has more than one name - that object is aliased
# if the aliased object is mutable, changes made with one alias affect the other
b[0] = 17
print(a)

