fhand = open('mbox.txt')
for line in fhand: 
    line = line.rstrip()
    if not '@utc.ac.za' in line : 
        continue
    print(line)
