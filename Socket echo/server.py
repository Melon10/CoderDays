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
    
    s.listen(5)
    print '等待链接'
    while 1:
        c,addr=s.accept()
        print 'Go connection from',addr
        c.send('Thank you for connecting')
        #c.close()

Server()   