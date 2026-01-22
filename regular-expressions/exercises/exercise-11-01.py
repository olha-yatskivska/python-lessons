#Write a simple program to simulate the operation of the grep command on Unix. Ask the user to enter a regular expression
#and count the number of lines that matched the regular expression:

import re

fhand = open('mbox.txt')
regex = input ("Enter a regular expression:")
count = 0
lst = list()

for line in fhand: 
    #line = line.rstrip()
    mtch = re.search (f'{regex}', line)
    if mtch:
        count = count + 1 
        #for n in mtch:
            #lst.append(n)
             
                

print(count)


