# 作者: 王道 龙哥
# 2022年03月03日10时32分15秒
import socket
def tcp_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    dest_addr = ('192.168.5.7', 2000)
    client.connect(dest_addr)
    # 一旦对端断开，recv不会卡主，会返回空,内核会把client标记为一致可读
    data=client.recv(5)
    print(data)
    client.close()

if __name__ == '__main__':
    tcp_client()