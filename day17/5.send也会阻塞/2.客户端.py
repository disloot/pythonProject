from socket import *


tcp_client_socket = socket(AF_INET, SOCK_STREAM)

# 本地IP地址和端口
address = ('192.168.5.7', 2000)

# 连接服务器
tcp_client_socket.connect(address)
temp_str = 'a' * 1000
total = 0
try:
    while True:
        send_size = tcp_client_socket.send(temp_str.encode('utf-8'))
        total += send_size
        print(total)
        if send_size != 1000:
            print("peer close")
            exit(1)
except Exception as e:
    print('我们自己的调试信息')
    print(e)