# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 10:46:18 2023

@author: Arpit Akar
"""
""" socket imported socket familytype AF_INET=ipv4 
type of socket is socket_stream=TCP
s.bind--> hostname local host port--> 1234 
socket  is endpoint that recieve data have two endpont connection
s.listen--> heavy data came then queue of 5
client socket is also an socket  object 
is used to send/recieve message using socket client
"""
import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host=socket.gethostname()
port = 1255
s.bind((host,port))
#NOW Our SERVER will run now we add client
s.listen(5)
#maximum allowable client numbers
# accept will accet the client over network and will return socketclientobject
# and adress
socketclient,address =s.accept()
#socket client used to send and recieve messages
print("got connection from",address)
#using socket client object to recieve messages
msg=socketclient.recv(1024)
msg=msg.decode("utf-8")
print(msg)
"""
con=True
while con:
    msg=socketclient.recv(1024) #size of reciving data 1byte
    msg= msg.decode("utf-8")
    print(msg)
    if (msg=="quit"):
        con=False
        s.close()
        """