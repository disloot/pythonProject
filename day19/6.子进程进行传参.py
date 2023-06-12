# 作者: 王道 龙哥
# 2022年03月07日15时03分48秒
import os
from multiprocessing import Process
import time
def run_proc(name,age,**kwargs):
    for _ in range(10):
        print(f'子进程{name} {age} ,{kwargs}')
        time.sleep(0.2)

if __name__ == '__main__':
    p=Process(target=run_proc,args=('xiongda',5),kwargs={'408':120})
    p.start()
    time.sleep(1)
    p.terminate()  #给子进程发信号杀掉它
    p.join()  # 一直等子进程，子进程结束，资源会被回收
    print('我是父进程')