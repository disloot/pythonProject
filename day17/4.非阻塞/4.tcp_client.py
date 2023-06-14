
import socket
def tcp_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    dest_addr = ('192.168.3.129', 2000)
    client.connect(dest_addr)
    data=input()
    client.send(data.encode('utf8'))
    client.close()
    socket.MSG_DONTWAIT
if __name__ == '__main__':
    tcp_client()