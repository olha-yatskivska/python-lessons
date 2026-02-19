a = ['Learn', 'Quiz', 'Practice', 'Contribute'] 
b = a 
c = a[:] 

b[0] = 'Code'
c[1] = 'Mcq'

count = 0
for c in (a, b, c): 
	if c[0] == 'Code': 
		count += 1
	if c[1] == 'Mcq': 
		count += 10

print (count) 
