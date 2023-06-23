# 作者: 王道 龙哥
# 2022年03月24日14时52分16秒
from time import ctime


def timefun_arg(pro,pre):
    print(pro)
    def timefun(func):
        print(pre)
        def wrapped_func():
            print("%s called at %s" % (func.__name__, ctime()))
            return func()  #针对被装饰的函数，带参数，那么闭包内需要这么写,为了通用，都这么写
        return wrapped_func
    return timefun

@timefun_arg('a','b')
def foo():
    print('I am foo')

@timefun_arg(1,2)
def foo1():
    print('I am foo1')
    
foo()
foo1()