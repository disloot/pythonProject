# 作者: 王道 龙哥
# 2022年03月05日09时46分34秒

from socket import *
import struct
class Client:
    def __init__(self,ip,port):
        self.client:socket=None
        self.ip = ip
        self.port = port

    def tcp_connect(self):
        self.client=socket(AF_INET, SOCK_STREAM)
        self.client.connect((self.ip,self.port))


    def send_train(self,send_bytes):
        """
        send火车，就是把某个字节流内容以火车形式发过去
        :param send_bytes:
        :return:
        """
        train_head_bytes = struct.pack('I', len(send_bytes))
        self.client.send(train_head_bytes + send_bytes)

    def recv_train(self):
        """
        recv火车，就是把火车recv的内容返回出去
        :return:
        """
        train_head_bytes=self.client.recv(4)
        train_head=struct.unpack('I',train_head_bytes)
        return self.client.recv(train_head[0])

    def send_command(self):
        """
        发送各种命令给服务器
        :return:
        """
        while True:
            # 读取命令并发送到服务器端
            command=input()
            self.send_train(command.encode('utf8'))
            if command[:2]=='ls':
                self.do_ls()
            elif command[:2]=='cd':
                self.do_cd()
            elif command[:3]=='pwd':
                self.do_pwd()
            elif command[:2]=='rm':
                self.do_rm(command)
            elif command[:4]=='gets':
                self.do_gets(command)
            elif command[:4]=='puts':
                self.do_puts(command)
            else:
                print('wrong command')
    def do_ls(self):
        data=self.recv_train().decode('utf8')
        print(data)

    def do_cd(self):
        print(self.recv_train().decode('utf8'))

    def do_pwd(self):
        print(self.recv_train().decode('utf8'))

    def do_rm(self,command):
        pass

    def do_gets(self,command):
        pass

    def do_puts(self,command):
        pass


if __name__ == '__main__':
    client=Client('192.168.5.7',2000)
    client.tcp_connect()
    client.send_command()