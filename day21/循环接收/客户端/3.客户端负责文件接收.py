# 作者: 王道 龙哥
# 2022年03月04日16时51分11秒
from socket import *
import select
import sys
import time
import struct


# 循环接收
def cycle_recv(client,file,file_size):
    total=0

    while total<file_size:
        data=client.recv(10000)
        file.write(data)
        total+=len(data)
        print('\r %5.2f%s' % (total/file_size*100,'%'),end='')

def main():
    tcp_client_socket = socket(AF_INET, SOCK_STREAM)

    # 本地IP地址和端口
    address = ('192.168.5.7', 2000)

    # 连接服务器
    tcp_client_socket.connect(address)

    #每次要先读4个字节的火车头
    train_head_bytes=tcp_client_socket.recv(4)
    train_content_len=struct.unpack('I',train_head_bytes)
    file_name=tcp_client_socket.recv(train_content_len[0])  #接到文件名

    #接一个文件大小
    train_head_bytes=tcp_client_socket.recv(4)
    train_content_len = struct.unpack('I', train_head_bytes)
    file_size=train_content_len[0]

    f=open(file_name.decode('utf8'),'wb')

    #接文件内容的长度
    cycle_recv(tcp_client_socket,f,file_size)
    print('\r100.00%')
    f.close()
    tcp_client_socket.close()

if __name__ == '__main__':
    main()