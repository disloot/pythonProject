#!/usr/bin/python
#author: Lyle
#time：2023/06/09 23:39

import socket
import struct
from multiprocessing import Manager, Pool
import os, select
import threading
import uuid
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad


def get_key(len=8):
    """获取指定位数的动态密钥
    """
    return str(uuid.uuid4()).replace('-', '')[4:4 + len].upper()


class My_DES_ECB():

    def __init__(self, key):
        # 密钥必须为8位
        self.key = key
        self.mode = DES.MODE_ECB
        self.cryptor = DES.new(self.key, self.mode)

    def encrypt(self, plain_text):
        return self.cryptor.encrypt(
            pad(plain_text.encode('utf-8'), DES.block_size))

    def decrypt(self, encrypted_text):
        plain_text = self.cryptor.decrypt(encrypted_text)
        plain_text = unpad(plain_text, DES.block_size).decode()
        return plain_text


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
        if command[:2] == 'ls':
            self.do_ls()
        elif command[:2] == 'cd':
            self.do_cd()
        elif command[:3] == 'pwd':
            self.do_pwd()
        elif command[:2] == 'rm':
            self.do_rm(command)
        elif command[:4] == 'gets':
            self.do_gets(command)
        elif command[:4] == 'puts':
            self.do_puts(command)
        elif command == 'a':
            print('a')
        elif command == 'b':
            print('b')

        elif command == 'log':
            self.do_log
        else:
            print('wrong command')
            #raise Exception('wrong command')

       

    def sign_up(self,epoll:select.epoll):  # sourcery skip: extract-method
        while True:
            user_name = self.recv_train()
            print('成功接收用户名')     
            if user_name not in self.server.user_pswd.keys():
                self._path = f'/home/ly/pythonProject/项目/MyNetDisk/users/{user_name}'
                self.send_train('1010')
                key = get_key()
                self.send_train(key)
                train_head = struct.unpack('I', self.socket.recv(4))[0]
                crypo_pswd = self.socket.recv(train_head)
                pc = My_DES_ECB(key.encode())
                pass_word = pc.decrypt(crypo_pswd)
                self.server.user_pswd[user_name] = pass_word
                # 可优化为数据库
                print('注册成功')
                with open("/home/ly/pythonProject/项目/MyNetDisk/user_pswd.txt",mode='w+') as f:             
                    f.write(str(self.server.user_pswd))
                os.mkdir(self._path)
                break
            else:
                self.send_train('1110')
        epoll.register(self.socket.fileno(),select.EPOLLIN)

class Server:

    def __init__(self, ip: str, port: int) -> None:
        self.socket = socket.socket(family=socket.AF_INET,
                                    type=socket.SOCK_STREAM)
        addr = (ip, port)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind(addr)
        self.socket.listen(128)
        self.user_pswd = {}
        with open('/home/ly/pythonProject/项目/MyNetDisk/user_pswd.txt',mode='r+') as f:
            self.user_pswd |= eval(f.read())
            

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
                elif command [:4] == 'sign':
                    epoll.unregister(fd)
                    sign_thread = threading.Thread(target=user.sign_up,args=(epoll,),daemon=True)
                    sign_thread.start()
                else:
                    # try:
                        user.deal_task(command)
                    # except Exception as ex:
                    #     print(ex)


if __name__ == '__main__':
    main()
