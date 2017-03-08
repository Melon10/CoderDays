# -*- coding: utf-8 -*-
"""
Created on Wed Mar 08 12:46:06 2017

@author: HP
"""
import socket

def Client():
    print '我已经在准备了'
    
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    host=socket.gethostname()
    port=1289

    s.connect((host,port))
    print s.recv(1024)
    

Client()