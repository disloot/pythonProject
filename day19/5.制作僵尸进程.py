# 作者: 王道 龙哥
# 2022年03月07日14时37分04秒
import os
from multiprocessing import Process
import time
def run_proc():
    print('我是子进程 pid={},ppid={}'.format(os.getpid(),os.getppid()))
    print('子进程结束')

if __name__ == '__main__':
    child=Process(target=run_proc)  #target代表子进程启动时，运行那个函数
    child.start()
    print('我是父进程 pid={},ppid={}'.format(os.getpid(),os.getppid()))
    # while True:
    #     time.sleep(1)