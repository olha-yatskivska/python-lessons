a = [10, 20, 30, 40, 50] 
b = [1, 2, 3, 4, 5] 


subtracted = list()
for a, b in zip(a, b):
    item = a -b
    subtracted.append(item)

print(subtracted)
