#!usr/bin/python3
# author lyle

import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
des_addr = ('192.168.3.14', 2001)
client.sendto(b'hello', des_addr)
data, _ = client.recvfrom(100)
client.close()
print(data.decode('utf8'))
