#!/usr/bin/python
#author: Lyle
#time：2023/06/09 23:39

import socket
from struct import unpack
from multiprocessing import Manager, Pool
import os,select

class User():
    def __init__(self,initfunction) -> None:
        temp  = initfunction
        self.client:socket.socket=temp[0] 
        self.addr:str = temp[1]
        self.username = None
        self._path = os.getcwd()
    
    def deal_task(self,command):
        if command == 'a':
            print('a')
        if command == 'b':
            print('b')


class server:

    def __init__(self, ip: str, port: int) -> None:
        self.server = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
        addr = (ip, port)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.bind(addr)
        self.server.listen(128)

    def creat_client(self):
        return User(self.server.accept())
    
    def deal_task(self,user:User,command):
        user.deal_task(command)
#git test
#ddddd
        

def main():
    s = server('',2000)
    pool = Pool(3)
    user_list={}
    epoll = select.epoll(-1)
    epoll.register(s.server.fileno(),select.EPOLLIN)
    while True:
        poll = epoll.poll()
        for fd,_ in poll:
            if fd == s.server.fileno():
                user=s.creat_client()
                user_list[user.client.fileno()] = user
                epoll.register(user.client.fileno(),select.EPOLLIN)
                print('连接成功')
            else:
                user:User = user_list[fd]
                command_len = unpack('I',user.client.recv(4))[0]
                command = user.client.recv(command_len).decode('utf8')
                pool.apply_async(s.deal_task,(user,command))
                



        
if __name__ == '__main__':
    main()
    
