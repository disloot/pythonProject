# 作者: 王道 龙哥
# 2022年03月08日16时32分25秒
import gevent
import time
def f(n):
    for i in range(n):
        print(gevent.getcurrent(),i)
        gevent.sleep(1)
g1=gevent.spawn(f,5)
g2=gevent.spawn(f,5)
g3=gevent.spawn(f,5)
g1.join()
g2.join()
g3.join()