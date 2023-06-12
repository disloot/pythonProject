# 作者: 王道 龙哥
# 2022年03月04日16时08分35秒
# 作者: 王道 龙哥
# 2022年03月04日16时08分42秒
from socket import *
import select
import sys

tcp_server_socket = socket(AF_INET, SOCK_STREAM)

#重用对应地址和端口
tcp_server_socket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

# 本地IP地址和端口
address = ('192.168.5.7', 2000)

tcp_server_socket.bind(address)
# 端口激活
tcp_server_socket.listen(100)

client_socket, clientAddr = tcp_server_socket.accept()

print(clientAddr)

# 服务器端accept之后，不去接client_socket缓冲区内的内容
while True:
    pass