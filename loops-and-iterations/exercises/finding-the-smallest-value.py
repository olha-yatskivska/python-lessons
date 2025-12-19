smallest = None
print('Before')
for value in [9, 41, 12, 3, 74, 15]:
    if smallest is None:
        smallest = value
    elif value < smallest :
        smallest = value
    print(smallest, value)
print('After', smallest)

# The first time through the loop smallest is None, so we take the first value to be the smallest.
