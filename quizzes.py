li = [2e-04, 'a', False, 87] 
tup = (6.22, 'boy', True, 554) 
for i in range(len(li)): 
	if li[i]: 
		li[i] = li[i] + tup[i] 
	else: 
		tup[i] = li[i] + li[i] 
		break
