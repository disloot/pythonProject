#!/usr/bin/python
#author: Lyle
#time：2023/06/05 16:52

from multiprocessing import Process
import time

# 子进程的代码
def run_proc():
    while True:
        print('---2----')
        time.sleep(3)

if __name__ == '__main__':
    p=Process(target=run_proc)  #run_proc传递时不可以加括号
    p.start()
    while True:
        print('---1----')
        time.sleep(1)