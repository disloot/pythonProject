import socket
import select
import sys
from struct import unpack
from struct import pack


#运行参数： python xxx.py ip port
class MyUnicodeDecodeError(Exception):
    pass


def tcp_client():
    client = socket.socket()
    des_addr = (ip, prot)
    client.connect(des_addr)
    print('连接成功')
    pre_data = b''
    int_0 = pack('I', 0)
    int_1 = pack('I', 1)
    while True:
        while True:
            user_name = input('请输入你的昵称(长度不超过10):')
            if len(user_name) > 10:
                print('昵称过长')
            else:
                break
        client.send(int_1 + user_name.encode('utf8'))
        flag = unpack('I', client.recv(4))[0]
        if flag == 0:
            print('该用户名已被注册')
        elif flag == 1:
            break
    epoll = select.epoll()
    epoll.register(sys.stdin.fileno(), select.EPOLLIN)
    epoll.register(client.fileno(), select.EPOLLIN)
    client.send(int_0 + f'{user_name} 加入房间\n'.encode('utf8'))
    user_name_bf = f'{user_name}:'.encode('utf8')
    print('欢迎进入聊天室')
    while True:
        try:
            events = epoll.poll()
            for fd, _ in events:
                if fd == sys.stdin.fileno():
                    low = 0
                    high = 32
                    message = (user_name_bf + input().encode('utf8') +
                               '\n'.encode('utf8'))
                    while high <= len(message):
                        data = message[low:high]
                        client.send(int_0 + data)
                        low += 32
                        high += 32
                    client.send(int_0 + message[low:])
                elif fd == client.fileno():
                    if data := client.recv(32):
                        try:
                            data = pre_data + data
                            if data.endswith('\n'.encode('utf8')):
                                print(data.decode('utf8'), end='')
                                pre_data = b''
                                continue
                            raise MyUnicodeDecodeError()
                        except UnicodeDecodeError:
                            pre_data = data
                        except MyUnicodeDecodeError:
                            pre_data = data
                    else:
                        client.close()
                        print('对方断开连接')
                        return
        except Exception as ex:
            client.close()
            print(f'意外结束了:{ex}')


if __name__ == '__main__':
    if len(sys.argv) == 1:
        ip = '192.168.3.129'
        prot = 2000
    else:
        ip = sys.argv[1]
        port = sys.argv[2]
    tcp_client()
