import urllib.request, urllib.parse, urllib.error 
from bs4 import BeautifulSoup

url = input('Enter - ')
html = urllib.request.urlopen(url).read()
soup = BeatifulSoup(html, 'html.parser')

# Retrievw all of the anchor tags
tags = soap('a')
for tag in tags:
  print(tag.get('href', None))
