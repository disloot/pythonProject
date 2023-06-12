# 作者: 王道 龙哥
# 2022年03月04日15时29分49秒
from socket import *
import select
import sys

tcp_server_socket = socket(AF_INET, SOCK_STREAM)

# 重用对应地址和端口
# tcp_server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

# 本地IP地址和端口
address = ('', 2000)

tcp_server_socket.bind(address)
# 端口激活
tcp_server_socket.listen(100)
tcp_server_socket.setblocking(False)
client_socket = None
temp_client =None
while True:
    try:
        temp_client, clientAddr = tcp_server_socket.accept()
    except Exception as e:
        # print(e)
        client_socket = temp_client
        if client_socket:
            client_socket.setblocking(False)
            try:
                text = client_socket.recv(1024)
                #如果对方断开
                if not text:
                    print('byebye')
                    client_socket.close()
                    temp_client=None
                    continue
                print(text.decode('utf-8'))
            except Exception as e:
                    pass