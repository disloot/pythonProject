#!/usr/bin/python
#author: Lyle
#time：2023/06/09 16:37

import multiprocessing
import time
import os
import random
from multiprocessing.pool import Pool
import sys


def father_process():
    arry = [1, 2, 3]
    p = multiprocessing.Process(target=sub_process, args=(arry, ))
    p.start()
    for i in range(3, 0, -1):
        q.put(i)
    time.sleep(0.01)
    p.terminate()


def sub_process(arry):
    arry.pop()
    while True:
        if not q.empty():
            print(f'son: {q.get()}')


def apply_pool():
    print('applied')
    time.sleep(1)


if __name__ == '__main__':
    temp = 0
    q = multiprocessing.Queue(1)
    pool = Pool(2)
    q = multiprocessing.Queue(0)
    # 异步过程 先把任务安排到队列 后通过信号分配进程
    for _ in range(5):
        pool.apply_async(apply_pool) 

    print('ok')
    print('you can see me')
    pool.close()
    pool.join()