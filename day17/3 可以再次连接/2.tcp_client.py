# 作者: 王道 龙哥
# 2022年03月03日10时32分15秒
import socket
import select
import sys

def tcp_client():
    if len(sys.argv) == 1:
        return
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    dest_addr = (sys.argv[1], 2000)
    client.connect(dest_addr)
    epoll = select.epoll()  # 创建一个epoll对象
    # 让epoll监控new_client sys.stdin
    epoll.register(client.fileno(), select.EPOLLIN)
    epoll.register(sys.stdin.fileno(), select.EPOLLIN)
    while True:
        # 谁的缓冲区有数据，就填写到events
        events = epoll.poll(-1)
        for fd,event in events:
            if fd == client.fileno():
                data = client.recv(100)
                if data:
                    print(data.decode('utf8'))
                else:
                    print('对方断开了')
                    return
            elif fd == sys.stdin.fileno():
                data = input()  # 服务器端说话，发给对方
                client.send(data.encode('utf8'))
    client.close()

if __name__ == '__main__':
    tcp_client()