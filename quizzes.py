d = {'GFG' : 'geeksforgeeks.org', 
			'google' : 'google.com', 
			'facebook' : 'facebook.com'
			} 
del d['google']; 
for key, values in d.items(): 
	print(key, end=" ") 
d.clear(); 
for key, values in d.items(): 
	print(key) 
del d; 
for key, values in d.items(): 
	print(key) 
