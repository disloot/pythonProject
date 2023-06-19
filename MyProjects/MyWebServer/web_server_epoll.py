#!/usr/bin/python
#author: Lyle

import select
import socket
import re

class TcpServer:
    def __init__(self,ip,port) -> None:
        self.socket:socket.socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind((ip,port))
        self.socket.listen(128)
        
    def service_client(self,request,new_socket:socket.socket):
        if request_lines := request.splitlines():
            if ret := re.match(r"[^/]+(/[^ ]*)", request_lines[0]):
                file_name = ret[1]
                print('>'*50)
                print(file_name)
                if file_name == '/':
                    file_name = "/index.html"

        try:
            f = open(f"./html{file_name}", mode="rb")
        except Exception as ex:
            response = (
                "HTTP/1.1 404 NOT FOUND\r\n\r\n"
                + "<html><h1>---file not found---</h1></html>"
            )
            new_socket.send(response.encode('utf8'))
        else:
            html_content = f.read()
            f.close()
            response = "HTTP/1.1 200 OK\r\n\r\n".encode('utf8')
            new_socket.send(response+html_content)
        new_socket.close()

def main():
    tcp_server = TcpServer('',7890)
    epoll = select.epoll()
    epoll.register(tcp_server.socket.fileno(),select.EPOLLIN)
    fd_dict = {}
    while True:
        fd_event = epoll.poll()
        for fd,event in fd_event:
            if fd == tcp_server.socket.fileno():
                new_socket,_ = tcp_server.socket.accept()
                epoll.register(new_socket.fileno(),select.EPOLLIN)
                fd_dict[new_socket.fileno()]=new_socket
            elif event == select.EPOLLIN:
                if request := fd_dict[fd].recv(4096).decode('utf8'):
                    tcp_server.service_client(request,fd_dict[fd])
                else:
                    fd_dict[fd].close()
                    epoll.unregister(fd)
                    fd_dict.pop(fd)

if __name__ == '__main__':
    main()