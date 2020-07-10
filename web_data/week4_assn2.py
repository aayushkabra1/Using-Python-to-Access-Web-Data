# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
# for tag in tags:
#     print(tag.get('href', None))
names = []
for i in range(7):
    url = tags[17].get('href', None)
    html = urllib.request.urlopen(url, context=ctx).read() 
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')

    name = re.search("(by_)([a-zA-z]*)", url)   
    names.append(name[2])

print(names[-1])    