# 作者: 王道 龙哥
# 2022年03月07日15时14分06秒
import os
from multiprocessing import Process
import time

nums=[11,22]
def work1():
    print('I am work1,{}'.format(os.getpid()))
    nums.append(33)
    time.sleep(2)
    print('work1 {}'.format(nums))

def work2():  # sourcery skip: use-fstring-for-formatting
    print('I am work2,{}'.format(os.getpid()))
    print(nums)

# 子进程创建是父进程的复制品，资源是独立使用

if __name__ == '__main__':
    p=Process(target=work1)
    p.start()
    time.sleep(1)
    nums.append(44)
    print(f'I am parent,{nums}')
    p.join()
    p = Process(target=work2)
    p.start()
    p.join()