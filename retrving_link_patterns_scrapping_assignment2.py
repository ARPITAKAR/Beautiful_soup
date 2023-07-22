# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 22:29:44 2023

@author: Arpit Akar
"""
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
list=[]
for tag in tags:
    tag.get('href', None)
    list.append(tag)
link=str(list[17])
# Replace 'your_html_link' with the HTML link provided
#link = '<a href="http://py4e-data.dr-chuck.net/known_by_Montgomery.html">Montgomery</a>'

# Regular expression pattern to extract the URL from the HTML link
pattern = r'<a href="([^"]+)">'

# Find the URL using re.findall
urls = re.findall(pattern, link)

# Print the extracted URL
print(urls[0])
k=[]
k.append(urls[0])
print(k[0])
address=str(k[0])
for i in range (0,6):
    print(address)
    html = urllib.request.urlopen(address, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    # Retrieve all of the anchor tags
    tags = soup('a')
    list=[]
    for tag in tags:
        tag.get('href', None)
        list.append(tag)
    link=str(list[17])
    print(type(link))
    # Replace 'your_html_link' with the HTML link provided
    #link = '<a href="http://py4e-data.dr-chuck.net/known_by_Montgomery.html">Montgomery</a>'

    # Regular expression pattern to extract the URL from the HTML link
    pattern = r'<a href="([^"]+)">'

    # Find the URL using re.findall
    urls = re.findall(pattern, link)

    # Print the extracted URL
    print(urls[0])
    address=str(urls[0])
    i+=1
    
    
