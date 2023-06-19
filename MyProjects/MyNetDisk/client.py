#!/usr/bin/python
#author: Lyle
#time：2023/06/19 22:15

from socket import *
import struct
import re
import hashlib

VERSION = 'beta'


def get_crypto(password):
    f_md5 = hashlib.md5()
    f_md5.update(password.encode())
    return f_md5.hexdigest()


class Client:

    def __init__(self, ip, port):
        self.socket: socket = None
        self.ip = ip
        self.port = port
        self.work_path = '/home'

    def tcp_connect(self):
        self.socket = socket(AF_INET, SOCK_STREAM)
        self.socket.connect((self.ip, self.port))

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

    def beginning(self):
        print('-' * 50)
        print(f'NetDisk  version:{VERSION}')
        print('\n')
        while True:
            choose = input('选择要进行的操作(l.log in   or   s.sign up):')
            if choose == 'l':
                self.send_train('log')
                self.do_log_in()
                break
            elif choose == 's':
                self.send_train('sign')
                self.do_sign_up()
                break
            else:
                print('无效的命令，请输入 “l” or "s" ')

    def send_command(self):
        """
        发送各种命令给服务器
        :return:
        """
        while True:
            # 读取命令并发送到服务器端
            command = input(f'NetDisk:{self.work_path}> ')
            self.send_train(command)
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
            try:
                command_dict[command_title]()
            except KeyError:
                print('wrong command')

    def do_ls(self):
        print('ls')

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

    def do_sign_up(self): # 待加入返回上一级功能
        while True:
            while True:
                user_name = input('输入用户名（数字或字母或下划线长度不超过8位）：')
                if not re.search(r'[\W]', user_name):
                    break
            self.send_train(user_name)
            is_sign = self.recv_train()
            # 用户名未被注册
            if is_sign == '1010':
                while True:
                    pass_word = input('输入密码：')
                    if conf_pswd := input('再次输入密码：') == pass_word:
                        break
                    else:
                        print('两次密码不一致')
                crypto_pswd = get_crypto(pass_word)
                self.send_train(crypto_pswd)
                print('注册成功')
                break
            elif is_sign == '1110':
                print('该用户名已被注册,请重新输入')
                continue
            self.send_command()

    def do_log_in(self):
        while True:
            user_name = input('请输入用户名：')
            password = input('请输入密码：')
            self.send_train(user_name)
            self.send_train(get_crypto(password))
            is_correct = self.recv_train()
            if is_correct == '1110':
                print('--登陆成功--')
                break
            elif is_correct == '0001':
                print('--密码错误，请重新输入--')
            elif is_correct == '0101':
                print('--用户不存在--')
        self.send_command()


def main():
    client = Client('192.168.10.129', 2000)
    client.tcp_connect()
    client.beginning()


if __name__ == '__main__':
    main()