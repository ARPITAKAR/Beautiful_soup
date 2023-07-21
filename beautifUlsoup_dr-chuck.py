# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 06:40:52 2023

@author: Arpit Akar
"""

import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup
import ssl


#ignores SSL certfication ERROR
ctx=ssl.create_default_context()
ctx.check_hostname= False
ctx.verify_name=ssl.CERT_NONE
url=input('ENter-')
#This basically will return entire documnet of that web page
html=urllib.request.urlopen(url,context=ctx).read()
soup=BeautifulSoup(html,'html.parser')
tags=soup('a')
for tag in tags:
    print(tag.get('href',None))