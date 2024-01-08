#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 06:48:41 2020

@author: ali
"""


# client.py  
import socket

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# get local machine name
#host = socket.gethostname()                           
host = "192.168.0.109"
port = 9996

# connection to hostname on the port.
s.connect((host, port))                               

# Receive no more than 1024 bytes
tm = s.recv(1024)                                     

s.close()

#print("The time got from the server is %s" % tm.decode('ascii'))
print ('The order: %s' % tm.decode())