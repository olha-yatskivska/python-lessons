# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# or pip install beautifulsoup4 to ensure you have the latest version
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl # defaults to certificate verification and most secure protocol (now TLS)

# Ignore SSL/TLS certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
try:
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
except:
  print("File cannot be opened:", url)
  quit()

# Retrieve all of the anchor tags
namelist = list()

i = input('Enter count:')
try: 
    i = int(i)
except: 
    print('Count must be a number')
    quit()
    
j = input('Enter position:')
try: 
    j = int(j)
except:
    print('Position must be a number')
    quit()
    
tags = soup('a')
for tag in tags:
    # Look at the parts of a tag
    tag = tag.rstrip()
    name = tag.contents[0]
    namelist.append(name)
print('Retrieving:', namelist[i])
    
    #print(tag[i].get('href', None))  
    #print(tag.contents[3])
    #j = input('Enter position:')
    #link = tag[i].get('href', None)
    #name = (tag.contents[0])
   
    #namelist.append(name)
    
   # 
#print('Retrieving:', name)
