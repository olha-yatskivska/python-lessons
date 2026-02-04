import urllib.request, urllib.parse, urllib.error 
from bs4 import BeautifulSoup

url = input('Enter - ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrievw all of the anchor tags
tags = soup('a')
    # Look at the parts of a tag
    print('TAG:', tag)
    print('URL:', tag.get('href', None))
    print('Contents:', tag.contents[0])
    print('Attrs:', tag.attrs)

#http://www.dr-chuck.com/page1.htm
#http://www.dr-chuck.com/page2.htm
