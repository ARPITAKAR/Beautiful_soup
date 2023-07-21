# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 22:04:52 2023

@author: Arpit Akar
"""

from bs4 import BeautifulSoup
import requests
url="https://www.youtube.com/channel/UCCezIgC97PvUuR4_gbFUs5g"
#request.get willgive response object
source=requests.get(url).text
#to get source objectwe can add .text to it
soup=BeautifulSoup(source,'lxml')
#print formatted object
#print(soup.prettify())
#match=soup.find('div',class_='footer')
#print(match.prettify())
#akar=soup.find('div',class_='inlined-html')
#print(akar.prettify())
article=soup.find('article')
#find all for all videos
#summary=article.find('div',class_='entry-content').p.text
#print(summary)
#youtube link getting
vid_src=article.find('iframe',class_='youtube-player')['']
#['']willacces as source attribiute
print(vid_src)
vid_id=vid_src.split('/')[4]
vid_id=vid_src.split('/')[0]
print(vid_id) 
yt_link=f'https://youtube.com/watch/v={vid_id}'
print(yt_link)
#usetry xcept o we can go last