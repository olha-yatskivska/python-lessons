import urllib.request
import json

url = input('Enter location: ')
if len(url) < 1 : 
    url = 'http://py4e-data.dr-chuck.net/comments_42.json'

print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()

info = json.loads(data)
print('User count:', len(info['comments']))


nums = list()
for item in info['comments']:
    count=item['count']
    nums.append(int(count))

print('Count:', len(nums))
print('Sum:', sum(nums))

   # print('Attribute', item['x'])
