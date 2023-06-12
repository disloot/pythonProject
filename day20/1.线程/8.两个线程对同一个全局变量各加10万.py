# 作者: 王道 龙哥
# 2022年03月08日11时10分51秒
import threading
import time

g_num = 0

def work1(num):
    global g_num
    for i in range(num):
        g_num += 1
    print("----in work1, g_num is %d---"%g_num)

def work2(num):
    global g_num
    for i in range(num):
        g_num += 1
    print("----in work2, g_num is %d---"%g_num)

# 加1操作不是原子操作
if __name__ == '__main__':
    t1=threading.Thread(target=work1,args=(1000000,))
    t2 = threading.Thread(target=work2, args=(1000000,))
    t1.start()
    t2.start()
    t1.join()  #等t1结束
    t2.join()  #等t2结束

    print("2个线程对同一个全局变量操作之后的最终结果是:%s" % g_num)