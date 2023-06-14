
import socket
import time
def tcp_server():
    # SOCK_STREAM代表tcp的socket
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    addr=('192.168.5.7',2000)
    s.bind(addr) #绑定,端口并没有激活
    s.listen(128) #listen时，端口才激活
    new_client,client_addr=s.accept()
    time.sleep(20)
    new_client.close()
    s.close()



if __name__ == '__main__':
    tcp_server()