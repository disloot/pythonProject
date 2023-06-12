# 作者: 王道 龙哥
# 2022年03月07日16时55分12秒

# 循环接收
def cycle_recv(client,file,file_size):
    total=0

    while total<file_size:
        data=client.recv(1000)
        file.write(data)
        total+=len(data)


def cycle_recv_process(client,file,file_size):
    total=0

    while total<file_size:
        data=client.recv(1000)
        file.write(data)
        total+=len(data)