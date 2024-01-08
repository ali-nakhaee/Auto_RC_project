#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 06:46:09 2020

@author: ali
"""


# server.py 
import socket                                         
import time

# create a socket object
serversocket = socket.socket(
	        socket.AF_INET, socket.SOCK_STREAM) 

# get local machine name
#host = socket.gethostname()                           
host = "192.168.0.109"
port = 9999                          

# bind to the port
serversocket.bind((host, port))                                  

# queue up to 5 requests
serversocket.listen(5)                                           

while True:
    # establish a connection
    clientsocket,addr = serversocket.accept()      

    print("Got a connection fro %s" % str(addr))
    currentTime = time.ctime(time.time()) + "\r\n"
    clientsocket.send(currentTime.encode('ascii'))
    clientsocket.send("Alioooo".encode())
    #clientsocket.send(10)
    clientsocket.close()
