# 作者: 王道 龙哥
# 2022年03月24日14时37分04秒
from time import ctime, sleep

def timefun(func):
    def wrapped_func():
        print("%s called at %s" % (func.__name__, ctime()))
        func()
    return wrapped_func

@timefun
def foo():
    """
    我是foo的注释
    :return:
    """
    print("I am foo")

print(foo.__doc__)
foo()
sleep(2)
foo()