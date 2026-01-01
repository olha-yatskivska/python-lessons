counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
if name in counts :
  x = counts[name]
else :
  x = 0

x = counts.get(name, 0)
print(counts)
