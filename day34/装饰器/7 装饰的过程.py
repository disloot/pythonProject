
#装饰器一定是内部有闭包的函数
def set_func(func):
    print('--开始进行装饰--')
    def call_func(a):
        print("---这是权限验证1----")
        print("---这是权限验证2----")
        func(a)
    return call_func


@set_func
def test1(num):
    print('----test1---- %d' % num)

test1(3)

