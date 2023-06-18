from socket import *
import struct
import re
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad


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


class Client:

    def __init__(self, ip, port):
        self.socket: socket = None
        self.ip = ip
        self.port = port

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

    def send_command(self):
        """
        发送各种命令给服务器
        :return:
        """
        while True:
            # 读取命令并发送到服务器端
            command = input('->')
            self.send_train(command)
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
            elif command == 'sign':
                self.do_sign_up()
            elif command == 'b':
                print(self.recv_train())
            else:
                print('wrong command')

    def do_ls(self):
        data = self.recv_train()
        print(data)

    def do_cd(self):
        print(self.recv_train())

    def do_pwd(self):
        print(self.recv_train())

    def do_rm(self, command):
        pass

    def do_gets(self, command):
        pass

    def do_puts(self, command):
        pass

    def do_sign_up(self):
        while True:
            while True:
                user_name = input('输入用户名（数字或字母或下划线长度不超过8位）：')
                if not re.search(r'[\W]', user_name):
                    break
            self.send_train(user_name)
            is_sign = self.recv_train()
                # 用户名未被注册
            if is_sign =='1010':
                key = self.recv_train().encode()
                pc = My_DES_ECB(key)
                while True:
                    pass_word = input('输入密码：')
                    if conf_pswd := input('再次输入密码：') == pass_word:
                        break
                    else:
                        print('两次密码不一致')
                crypto_pswd=pc.encrypt(pass_word)
                train_head_bytes = struct.pack('I', len(crypto_pswd))
                self.socket.send(train_head_bytes + crypto_pswd)
                print('注册成功')
                break
            elif is_sign=='1110':
                print('该用户名已被注册')
                continue
        
if __name__ == '__main__':
    client = Client('192.168.198.128', 2000)
    client.tcp_connect()
    client.send_command()