#!/usr/bin/python
#author: Lyle

import re
import socket


class WSGIServer:
    def __init__(self,ip,port,document_root='/home/ly/pythonProject/项目/MyWebServer/html') -> None:
        self.socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        self.socket.bind((ip,port))
        self.socket.listen(128)
        self.socket.setblocking(False)
        self.client_socket_list = [socket.socket]
        self.document_root = document_root

    def run_forever(self):
        while True:
            try:
                new_client_socket,_ = self.socket.accept()
            except Exception as ex:
                pass
            else:
                new_client_socket.setblocking(False)
                self.client_socket_list.append(new_client_socket)
            for client_socket in self.client_socket_list:
                try:
                    request = client_socket.recv(4096).decode('utf8')
                except Exception as ex:
                    pass
                else:
                    if request:
                        self.deal_request(request,client_socket)
                    else:
                        client_socket.close()
                        self.client_socket_list.remove(client_socket)

    def deal_request(self,request:str,client_socket:socket.socket):
        request_line = request.splitlines()
        if ret := re.match(r"[^/]+(/[^ ]*)", request_line[0]):
            file_name = ret[1]
            print(request_line)
            print('>'*50)
            print(file_name)
            if file_name == '/':
                file_name = '/index.html'

        try:
            print(f"{self.document_root}{file_name}")
            f = open(f"{self.document_root}{file_name}",'rb')
        except Exception as ex:
            response_body = "file not found, 请输入正确的url"
            response_header = (
                "HTTP/1.1 404 not found\r\n"
                + "Content-Type: text/html; charset=utf-8\r\n"
            )
            response_header += "Content-Length: %d\r\n" % (len(response_body))
            response_header += "\r\n"
            client_socket.send((response_header+response_body).encode('utf8'))
        else:
            self._extracted_from_deal_request_18(f, client_socket)

    def _extracted_from_deal_request_18(self, f, client_socket):
        content = f.read()
        f.close()

        response_body = content
        response_header = "HTTP/1.1 200 OK\r\n"
        response_header += "Content-Length: %d\r\n" % (len(response_body))
        response_header += "\r\n"

        # 将header返回给浏览器
        client_socket.send( response_header.encode('utf-8') + response_body)

def main():
    http_server = WSGIServer('',7890)
    http_server.run_forever()

if __name__ == '__main__':
    main()

        