# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 11:11:39 2023

@author: Arpit Akar
"""
import socket
#library importing
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host=socket.gethostname()
port = 1255
# making connection 
s.connect((host,port))
msg="this is host2"
s.send(msg.encode("utf-8"))
s.close()
"""
con=True
while con:
    msg=input("enter the msg")
    s.send(msg.encode("utf-8"))
    if (msg=="quit"):
        con=False
        s.close()
  """      