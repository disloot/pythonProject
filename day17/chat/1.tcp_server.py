
import socket

def tcp_server():
    # SOCK_STREAM代表tcp的socket
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    addr=('192.168.5.7',2000)
    s.bind(addr) #绑定,端口并没有激活
    s.listen(128) #listen时，端口才激活
    new_client,client_addr=s.accept()
    print(client_addr)
    while True:
        # 服务器端先接
        data=new_client.recv(100)
        print(data.decode('utf8'))
        data=input()  #服务器端说话，发给对方
        new_client.send(data.encode('utf8'))

    new_client.close()
    s.close()



if __name__ == '__main__':
    tcp_server()