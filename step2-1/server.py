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
        try:
            c,addr=s.accept()
            print 'Got connection from',addr
            c.send('Thank you for connecting')
            store={}
            while 1:#客户端输入循环
                client_input=str(c.recv(1024)).strip(' ')
                if client_input=='quit':
                    print 'Client quit\nNot connnected'                    
                    c.close()
                    break
                else:    
                    print 'Server received:'+client_input
                    cmd=client_input.split()
                    try:                        
                        if cmd[0]=='set':
                            store[cmd[1]]=cmd[2]
                            c.send('True')
                        elif cmd[0]=='get':
                            c.send(store.get(cmd[1]))
                        elif cmd[0]=='delete':
                            c.send(store[cmd[1]])
                            del store[cmd[1]]
                        else:
                            c.send('Illegal Input')
                    except (IndexError,TypeError):
                        c.send('Illegal Input')
        except socket.error:
           print 'Client has been disconnected'
           raw_input('Please press any key to close\n')
           break

Server()   