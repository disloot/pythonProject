# 作者: 王道 龙哥
# 2022年03月03日10时10分00秒

import socket
import select
import sys

def tcp_server():
    # SOCK_STREAM代表tcp的socket
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    addr=('',2000)
    s.bind(addr) #绑定,端口并没有激活
    s.listen(128) #listen时，端口才激活
    epoll=select.epoll()  # 创建一个epoll对象
    # 让epoll监控new_client sys.stdin
    epoll.register(s.fileno(),select.EPOLLIN)
    epoll.register(sys.stdin.fileno(),select.EPOLLIN)
    while True:
        # 谁的缓冲区有数据，就填写到events,events是列表里边存的是元组，（fd,事件）
        events=epoll.poll(-1)
        for fd,event in events:
            if fd == s.fileno():
                # 有客户端连接，就连上，注册它
                new_client, client_addr = s.accept()
                print(client_addr)
                epoll.register(new_client.fileno(), select.EPOLLIN)
            if fd==new_client.fileno():
                if data := new_client.recv(100):
                    print(data.decode('utf8'))
                else:
                    print('对方断开了')
                    #对方断开要解除监控
                    epoll.unregister(new_client.fileno())
                    new_client.close()
                    break
            elif fd==sys.stdin.fileno():
                try:
                    data=input()  #服务器端说话，发给对方
                except EOFError:  #按ctrl d后让服务器断开
                    print('I want go')
                    return
                new_client.send(data.encode('utf8'))

    new_client.close()
    s.close()



if __name__ == '__main__':
    tcp_server()