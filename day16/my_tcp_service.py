import socket
import sys


# 参数： xxx.py port
def main():
    service = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = int(sys.argv[1])
    addr = ('', port)
    service.bind(addr)
    service.listen(16)
    while True:
        client1, client_addr = service.accept()
        print('连接成功')
        rec_path = client1.recv(64)
        file_path = rec_path.decode('utf8')
        if content := get_file(file_path):
            client1.send(content)
        flag = int(client1.recv(64).decode('utf8'))
        client1.close()
        if flag == 'n':
            break
    service.close()


def get_file(path):
    try:
        with open(path, mode='rb') as f:
            content = f.read()
        return content
    except Exception:
        print('未找到此文件')


if __name__ == '__main__':
    main()
