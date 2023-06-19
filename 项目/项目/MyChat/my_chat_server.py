#author: Lyle
#time：2023/06/03 19:31

# 运行参数： python xxx.py port
import socket
import sys
import select
from struct import pack
from struct import unpack


def tcp_serve():
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # 重用地址和端口
    s.bind(('', int(port)))
    s.listen(10)
    epoll = select.epoll()
    epoll.register(s.fileno(), select.EPOLLIN)
    clients: dict[socket.socket.fileno, socket.socket] = {}
    user_list = {}
    while True:
        events = epoll.poll()
        for fd, _ in events:
            if fd == s.fileno():
                new_client, new_client_addr = s.accept()
                print(f'新客户端已连接：{new_client_addr}')
                clients[new_client.fileno()] = new_client

                epoll.register(new_client.fileno(), select.EPOLLIN)
            elif fd in clients:
                try:
                    while True:
                        title =  unpack('I',clients[fd].recv(4))[0]
                        if title != 1:
                            break
                        user_name = clients[fd].recv(32).decode('utf8')
                        if user_name in user_list.values():
                            clients[fd].send(pack('I', 0))
                        else:
                            clients[fd].send(pack('I', 1))
                            user_list[clients[fd]] = user_name
                            break
                except Exception as ex:
                    print(f'客户端{new_client_addr}注册时出错，错误代码{ex}')
                finally:
                    if title == 0:
                        if data := clients[fd].recv(32):
                            for client in user_list:
                                if client is not clients[fd]:
                                    client.send(data)
                        else:
                            for client in user_list:
                                if client is not clients[fd]:
                                    client.send(
                                        f'{user_list[clients[fd]]} 离开房间\n'.
                                        encode('utf8'))
                            epoll.unregister(fd)
                            user_list.pop(clients[fd])
                            print(f'{clients[fd].getpeername()}断开连接')
                            clients[fd].close()
                            clients.pop(fd)


    s.close()


if __name__ == '__main__':
    if len(sys.argv) == 1:
        port = 2000
    tcp_serve()