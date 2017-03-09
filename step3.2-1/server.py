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
            store.clear()#清除客户端数据
        except socket.error:
            print 'Client has been disconnected\nWaiting for next connnection'           


def CMD_solver(client_input):#处理除quit以外的命令
    print 'Server received:'+client_input
    cmd=client_input.split()
    try:                        
        if not store.get(cmd[1]):#为新key创建新列表
            store[cmd[1]]=[]
        if cmd[0]=='rpush':#头添加
            store[cmd[1]].append(cmd[2])
            return 'True'
        elif cmd[0]=='lpush':#尾添加
                store[cmd[1]][0:0]=cmd[2]
                return 'True'
        elif cmd[0]=='rpop':
            return store[cmd[1]].pop()
        elif cmd[0]=='lpop':
            return store[cmd[1]].pop(0)
        elif cmd[0]=='llen':
            return str(len(store[cmd[1]]))
        elif cmd[0]=='lrange':
            return str(store[cmd[1]][int(cmd[2]):int(cmd[3])])
        else:
            return 'Illegal Input'
    except (IndexError,TypeError,KeyboardInterrupt,KeyError):
        return 'Illegal Input'
        

def Client_quitting():
    print 'Client quit\nNot connnected'
    return 'Looking forward to seeing you again'


store={}
Server()   