
import socket

client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
dest_addr=('192.168.5.7',2000)
# client.sendto(b'hello',dest_addr)
client.sendto('howare'.encode('utf8'),dest_addr)  #放汉字还是不放都行
data,_=client.recvfrom(100)
print(data.decode('utf8'))
client.close()  #关闭时端口会释放