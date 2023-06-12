# 作者: 王道 龙哥
# 2022年03月03日10时10分00秒

#聊天室
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
    # 让epoll监控s, sys.stdin
    epoll.register(s.fileno(),select.EPOLLIN)
    epoll.register(sys.stdin.fileno(),select.EPOLLIN)
    client_list=[] #存储所有的client对象
    while True:
        # 谁的缓冲区有数据，就填写到events,events是列表里边存的是元组，（fd,事件）
        events=epoll.poll(-1)
        for fd,event in events:
            if fd == s.fileno():
                # 有客户端连接，就连上，得到客户端new_client，放入列表，注册它
                new_client, client_addr = s.accept()
                print(client_addr)
                client_list.append(new_client)
                epoll.register(new_client.fileno(), select.EPOLLIN)
            else:
                remove_client=None
                for client in client_list: #遍历所有的客户端对象
                    if client.fileno() ==fd:
                        if data := client.recv(1000):
                            for other_client in client_list:
                                if other_client is not client:
                                    other_client.send(data)
                        else:
                            remove_client=client
                if remove_client:
                    client_list.remove(remove_client)
                    epoll.unregister(remove_client.fileno())
                    remove_client.close()

    s.close()



if __name__ == '__main__':
    tcp_server()