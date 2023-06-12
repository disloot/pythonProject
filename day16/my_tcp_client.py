import socket
import sys

# xxx.py ip port get_path rec_path
def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ip = sys.argv[1]
    des_addr = (ip, 2000)
    client.connect(des_addr)
    get_path = sys.argv[3]
    rec_path = sys.argv[4]
    client.send(get_path.encode('utf8'))
    data = client.recv(1024)
    try:
        with open(rec_path, mode='wb') as f:
            f.write(data)
        print('下载完成')
    except Exception:
        print('下载失败')
    while True:
        if flag := input('是否继续下载？（y/n）') in('y','n'):
            client.send(flag.encode('utf8'))
            break
        else:
            print("请输入'y' or 'n'")
    client.close()


if __name__ == '__main__':
    main()
