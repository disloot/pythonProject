# 作者: 王道 龙哥
# 2022年03月24日14时45分43秒
from time import ctime, sleep

def timefun(func):
    def wrapped_func():
        print("%s called at %s" % (func.__name__, ctime()))
        return func()  #针对被装饰的函数，带参数，那么闭包内需要这么写,为了通用，都这么写
    return wrapped_func

def test():
    print('test')

@timefun
def foo():
    print("I am foo")

@timefun
def getInfo():
    return '----hahah---'

foo()

val=getInfo()
print(val)

val=test()
print(val)