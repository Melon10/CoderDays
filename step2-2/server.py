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
            while 1:#客户端输入循环
                client_input=str(c.recv(1024)).strip(' ')
                if client_input=='quit':
                    c.send(Client_quitting())                    
                    c.close()
                    break
                else:    
                    c.send(CMD_solver(client_input))
        except socket.error:
            print 'Client has been disconnected'
            raw_input('Please press any key to close\n')           


def CMD_solver(client_input):#处理除quit以外的命令
    print 'Server received:'+client_input
    cmd=client_input.split()
    store={}
    try:                        
        if cmd[0]=='set':
            store[cmd[1]]=cmd[2]
            return 'True'
        elif cmd[0]=='get':
            return store.get(cmd[1])
        elif cmd[0]=='delete':
            return store[cmd[1]]
            del store[cmd[1]]
        else:
            return 'Illegal Input'
    except (IndexError,TypeError):
        return 'Illegal Input'
        

def Client_quitting():
    print 'Client quit\nNot connnected'
    return 'Looking forward to seeing you again'


Server()   