li = [3, 1, 2, 4] 
tup = ('A', 'b', 'c', 'd') 
li.sort() 
counter = 0
for x in tup: 
	li[counter] += int(x) 
	counter += 1
	break
print(li) 
