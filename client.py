# -*- coding: utf-8 -*-
"""
Created on Wed Mar 08 12:46:06 2017

@author: HP
"""
import socket

def Client():
   
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    host=socket.gethostname()
    port=1289

    s.connect((host,port))
    print s.recv(1024)    
    while 1:
        my_input=raw_input('input something\n')
        print my_input
        s.send(my_input)
        if my_input.strip(' ')=='quit':
            break
        
Client()