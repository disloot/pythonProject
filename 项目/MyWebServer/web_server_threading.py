import threading
import socket
import re

def service_client(new_socket:socket.socket):
    request = new_socket.recv(4096).decode('utf8')
    print(request)
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
    
class TcpServer:
    def __init__(self,ip,port) -> None:
        self.socket:socket.socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind((ip,port))

    def listen(self,n=128):
        return self.socket.listen(n)

    def accept(self):
        return self.socket.accept()
    def close(self):
        return self.socket.close()

def main():
    tcp_server=TcpServer('',7890)
    tcp_server.listen()
    while True:
        new_socket,_=tcp_server.accept()
        cliend_thread= threading.Thread(target=service_client,args=(new_socket,))
        cliend_thread.start()
    
    tcp_server.close()

if __name__ == '__main__':
    main()