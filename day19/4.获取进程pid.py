#!/usr/bin/python
#author: Lyle
#time：2023/06/05 17:27

import os
from multiprocessing import Process
import time
def run_proc():
    print(f'我是子进程 pid={os.getpid()}')
    # while True:
    #     pass
    print('子进程结束')

if __name__ == '__main__':
    child=Process(target=run_proc)  #target代表子进程启动时，运行那个函数
    child.start()
    print('我是父进程 pid={}'.format(os.getpid(),'a'))
    while True:
        pass
