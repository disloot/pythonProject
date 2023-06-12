# 作者: 王道 龙哥
# 2022年03月07日16时25分32秒
from multiprocessing.pool import Pool

import os, time, random

def worker(msg):
    t_start=time.time()
    print("%s开始执行,进程号为%d" % (msg, os.getpid()))  #只有3个服务员
    # random.random()随机生成0~1之间的浮点数
    time.sleep(random.random() * 2)
    t_stop = time.time()
    print(msg, "执行完毕，耗时%0.2f" % (t_stop - t_start))

if __name__ == '__main__':
    po=Pool(3)
    for i in range(10):
        # 每次循环将会用空闲出来的子进程去调用目标
        po.apply_async(worker,(i,))

    print("----start----")
    po.close()  # 关闭进程池，关闭后po不再接收新的请求
    po.join()  # 等待po中所有子进程执行完成，必须放在close语句之后
    print("-----end-----")