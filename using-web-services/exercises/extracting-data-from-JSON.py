import urllib.request
import json

url = input('Enter location: ')
if len(url) < 1 : 
    url = 'http://py4e-data.dr-chuck.net/comments_42.xml'

print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()

info = json.loads(data)
print('User count:', len(info))

#nums = list()
#for item in info:
 #   print('count', item['count'])
  #  print('Id', item['id'])
   # print('Attribute', item['x'])
