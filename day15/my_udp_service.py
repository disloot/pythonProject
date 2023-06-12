#!usr/bin/python3
# author lyle

import socket

service = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
addr = ('', 2001)
service.bind(addr)
data, client_addr = service.recvfrom(100)
print(data.decode('utf8'))
service.sendto('你已成功连接服务器'.encode('utf8'), client_addr)
service.close()
