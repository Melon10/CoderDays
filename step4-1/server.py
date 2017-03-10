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
    try:
        s.bind((host,port))
        print 'protoclo build\nNot connected'
    except socket.error:
        print 'Another Server is working'
        raw_input('Please press any key to close this Server')
        exit()
    
    s.listen(5)
    
    while True:#监听循环
        try:
            c,addr=s.accept()
            print 'Got connection from',addr
            c.send('Thank you for connecting')
            while True:#客户端服务循环
                client_input=str(c.recv(1024)).strip(' ')
                if client_input=='quit':
                    c.send(Client_quitting())                    
                    c.close()
                    break
                elif client_input.upper()=='MULTI':#开始事务
                    c.send('OK')
                    print 'Begin MULTI'
                elif client_input.upper()=='EXEC':#处理并清楚命令仓库
                    c.send(cmd_solver())
                    cmd_cleaner()
                    print 'Dealing CMD'
                elif client_input.upper()=='RESET':#重置命令仓库
                    cmd_cleaner()
                    c.send('True')
                    print 'Reset CMD'
                else:#错误输入或者其他增删查等命令    
                    cmd_storer(client_input)
                    c.send('QUEUED')
            client_cleaner()#清除客户端数据
        except socket.error:
            print 'Client has been disconnected\nWaiting for next connnection'           
            client_cleaner()

def cmd_solver():#处理除quit以外的命令
    result=[]#命令处理结果，在客户端输出
    for client_input in cmd_store:
        cmd=client_input.split(' ')
        if cmd[0][0]=='l' or cmd[0][0]=='r':
            result.append(List_cmd_solver(client_input))
        elif cmd[0][0]=='h':
            result.append(Dict_cmd_solver(client_input))
        else:
            result.append(Prim_cmd_solver(client_input))
    
    return str(result).strip('[\']').replace(',' ,'').replace('\'','').replace(' ','\n').replace('l\nI','l I')
    #上一语句可能是整段代码中最为晦涩，可读性较低的一段代码，但是这句语句的使用是为了
    #解决result使用列表而非字符串带来的问题（使用字符串可能会使内存的使用量大大增加），
    #所以我就没有办法了。。。


def List_cmd_solver(client_input):#处理列表数据
    print 'Server received:'+client_input
    cmd=client_input.split()
    try:                        
        if not store_List.get(cmd[1]):#为新key创建新列表
            store_List[cmd[1]]=[]
        if cmd[0]=='rpush':#头添加
            store_List[cmd[1]].append(cmd[2])
            return 'True'
        elif cmd[0]=='lpush':#尾添加
                store_List[cmd[1]][0:0]=cmd[2]
                return 'True'
        elif cmd[0]=='rpop':
            return store_List[cmd[1]].pop()
        elif cmd[0]=='lpop':
            return store_List[cmd[1]].pop(0)
        elif cmd[0]=='llen':
            return str(len(store_List[cmd[1]]))
        elif cmd[0]=='lrange':
            return str(store_List[cmd[1]][int(cmd[2]):int(cmd[3])])
        else:
            return 'Illegal Input'
    except (IndexError,TypeError,KeyboardInterrupt,KeyError):
        return 'Illegal Input'


def Dict_cmd_solver(client_input):#处理字典数据
    print 'Server received:'+client_input
    cmd=client_input.split()
    try:                        
        if cmd[1]=='hash':
            if cmd[0]=='hset':
                store_Dict[cmd[2]]=cmd[3]
                return 'True'
            elif cmd[0]=='hget':
                return str(store_Dict.get(cmd[2]))
            elif cmd[0]=='hdel':
                str1=store_Dict[cmd[2]]
                del store_Dict[cmd[2]]
                return str1
            elif cmd[0]=='hkeys':
                return str(store_Dict.keys())
            else:
                return 'Illegal Input'
        else:
            return 'Illegal Input'
    except (IndexError,TypeError,KeyboardInterrupt,KeyError):
        return 'Illegal Input'


def Prim_cmd_solver(client_input):#处理基本数据储存那个版本使用的命令
    print 'Server received:'+client_input
    cmd=client_input.split()
    try:                        
        if cmd[0]=='set':
            store_Prim[cmd[1]]=cmd[2]
            return 'True'
        elif cmd[0]=='get':
            return str(store_Prim.get(cmd[1]))
        elif cmd[0]=='delete':
            str1=store_Prim[cmd[1]]
            del store_Prim[cmd[1]]
            return str1
        else:
            return 'Illegal Input'
    except (IndexError,TypeError,KeyboardInterrupt,KeyError):
        return 'Illegal Input'
        

def client_cleaner():
    store_List.clear()
    store_Dict.clear()
    store_Prim.clear()


def cmd_cleaner():
    global cmd_store
    cmd_store=cmd_store[-1:0]    


def cmd_storer(client_input):#对增删查等命令进行储存以及错误命令的回馈
    global cmd_store
    cmd_store.append(client_input)

def Client_quitting():
    print 'Client quit\nNot connnected'
    return 'Looking forward to seeing you again'


store_List={}
store_Dict={}
store_Prim={}
cmd_store=[]
Server()   