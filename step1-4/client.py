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
    Sever_condition=False

    try:
        s.connect((host,port))
        print s.recv(1024)
        Sever_condition=True
    except socket.error:
        print 'Server haven\'t opened' 
    
    while Sever_condition:
        try:
            my_input=raw_input('input something\n')
            print my_input
            s.send(my_input)
            if my_input.strip(' ')=='quit':
                break
        except socket.error:
            print 'Disconnected with Server'
            raw_input('Please press any key to close\n')
            break

Client()