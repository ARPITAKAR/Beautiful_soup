# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 19:28:17 2023

@author: Arpit Akar
"""

import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup
url=input('enter-')
# ,read() says read it all till the new line comes in the end
html=urllib.request.urlopen(url).read()
soup=BeautifulSoup(html,'html.parser')
 
#retrive list of all the anchor tags
#ENter - http://www.dr-chuck.com/page1.htm
tags=soup('a')
for tag in tags:
    print(tag.get('href',None))