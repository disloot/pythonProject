#!/usr/bin/python
#author: Lyle
#time：2023/06/09 23:39

import socket
import struct
from multiprocessing import Manager, Pool
import os, select
import threading
import pymysql
import re


class User():

    def __init__(self, initfunction, server) -> None:
        temp = initfunction
        self.socket: socket.socket = temp[0]
        self.addr: str = temp[1]
        self.username = None
        self._path = os.getcwd()
        self.is_login = False
        self.server = server

    def send_train(self, send_body):
        """
        send火车，就是把某个字节流内容以火车形式发过去
        :param send_bytes:
        :return:
        """
        send_bytes = send_body.encode()
        train_head_bytes = struct.pack('I', len(send_bytes))
        self.socket.send(train_head_bytes + send_bytes)

    def recv_train(self):
        """
        recv火车，就是把火车recv的内容返回出去
        :return:
        """
        train_head_bytes = self.socket.recv(4)
        train_head = struct.unpack('I', train_head_bytes)
        return self.socket.recv(train_head[0]).decode()

    def deal_task(self, command):  # sourcery skip: raise-specific-error

        command_dict = {
            'ls': self.do_ls,
            'cd': self.do_cd,
            'pwd': self.do_pwd,
            'rm': self.do_rm,
            'get': self.do_get,
            'put': self.do_put,
            'sign': self.do_sign_up,
            'log': self.do_log_in
        }
        command_title = re.match(r'[\S]+', command).group()
        print(command_title)
        command_dict[command_title]()
    
    def do_ls(selft):
        pass

    def do_cd(self):
        print('cd')

    def do_pwd(self):
        print('pwd')

    def do_rm(self, command):
        pass

    def do_get(self, command):
        pass

    def do_put(self, command):
        pass

    def do_sign_up(self, epoll: select.epoll):  # sourcery skip: extract-method
        while True:
            database = pymysql.connect(host='192.168.10.129',
                                       user='root',
                                       password='123',
                                       database='NetDisk',
                                       port=3306,
                                       charset='utf8')
            curs = database.cursor()
            user_name = self.recv_train()
            print('成功接收用户名')
            if not curs.execute(
                    f"SELECT NAME FROM users WHERE name = '{user_name}'"):
                self._path = f'/home/ly/pythonProject/项目/MyNetDisk/users/{user_name}'
                self.send_train('1010')
                pass_word = self.recv_train()
                curs.execute(
                    f"INSERT INTO users(name,password) VALUES('{user_name}','{pass_word}');"
                )
                os.mkdir(self._path)
                database.commit()
                curs.close()
                database.close()
                print('注册成功')
                break
            else:
                self.send_train('1110')
        epoll.register(self.socket.fileno(), select.EPOLLIN)

    def do_log_in():
        pass

class Server:

    def __init__(self, ip: str, port: int) -> None:
        self.socket = socket.socket(family=socket.AF_INET,
                                    type=socket.SOCK_STREAM)
        addr = (ip, port)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind(addr)
        self.socket.listen(128)

    def creat_client(self):
        return User(self.socket.accept(), self)

    # def deal_task(self, user: User, command):
    #     try:
    #         user.deal_task(command)
    #     except Exception as ex:
    #         print(ex)


def main():
    s = Server('', 2000)

    pool = Pool(3)
    user_list = {}
    epoll = select.epoll(-1)
    epoll.register(s.socket.fileno(), select.EPOLLIN)
    while True:
        poll = epoll.poll()
        for fd, _ in poll:
            if fd == s.socket.fileno():
                user = s.creat_client()
                user_list[user.socket.fileno()] = user
                epoll.register(user.socket.fileno(), select.EPOLLIN)
                print('连接成功')
            else:
                user: User = user_list[fd]
                command = user.recv_train()
                if command[:3] in ['get', 'put']:
                    pool.apply_async(s.deal_task, (user, command))
                elif command[:4] == 'sign':
                    epoll.unregister(fd)
                    sign_thread = threading.Thread(target=user.do_sign_up,
                                                   args=(epoll, ),
                                                   daemon=True)
                    sign_thread.start()
                else:
                    # try:
                    user.deal_task(command)
                # except Exception as ex:
                #     print(ex)


if __name__ == '__main__':
    main()
