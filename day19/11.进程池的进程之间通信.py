# 作者: 王道 龙哥
# 2022年03月07日16时39分48秒

from multiprocessing import Manager,Pool
import os,time,random

def reader(q):
    print("reader启动(%s),父进程为(%s)" % (os.getpid(), os.getppid()))
    for i in range(q.qsize()):
        print("reader从Queue获取到消息：%s" % q.get())

def writer(q):
    print("writer启动(%s),父进程为(%s)" % (os.getpid(), os.getppid()))
    for i in "wangdao":
        q.put(i)

if __name__ == '__main__':
    q=Manager().Queue()
    po=Pool() #初始化进程池
    po.apply_async(writer,args=(q,))
    time.sleep(1)
    po.apply_async(reader, args=(q,))
    po.close()
    po.join()