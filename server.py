# -*- coding: utf-8 -*-
"""
Created on Tue Mar 07 23:53:27 2017

@author: HP
"""

import socket  
  
#Server  
def Server():  
    
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    
    host=socket.gethostname()
    port=1289
    s.bind((host,port))
    print 'protoclo build\nNot connected'
    
    s.listen(5)
    
    while 1:#监听循环
        c,addr=s.accept()
        print 'Got connection from',addr
        c.send('Thank you for connecting')
        while 1:#客户端输入循环
            client_input=str(c.recv(1024)).strip(' ')
            if client_input=='quit':
                print 'Client quit\nNot connnected'
                c.close()
                break
            else:    
                print 'Server received:'+client_input

Server()   