
import socket
def tcp_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    dest_addr = ('192.168.5.7', 2000)
    client.connect(dest_addr)
    # 先接
    data=client.recv(5)
    print(data.decode('utf8'))
    data=client.recv(5)
    print(data.decode('utf8'))
    client.send('我是男生abc123'.encode('utf8'))
    client.close()

if __name__ == '__main__':
    tcp_client()