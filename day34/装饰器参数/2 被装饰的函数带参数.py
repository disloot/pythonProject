# 作者: 王道 龙哥
# 2022年03月24日14时42分08秒
from time import ctime, sleep

def timefun(func):
    def wrapped_func(a, b):  #参数数目要和被装饰的函数一样
        print("%s called at %s" % (func.__name__, ctime()))
        print(a, b)
        func(a, b)
    return wrapped_func

@timefun
def foo(a, b):
    print(a+b)

foo(3,5)
sleep(2)
foo(2,4)