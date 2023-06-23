
#装饰器一定是内部有闭包的函数
def set_func(func):
    def call_func():
        print("---这是权限验证1----")
        print("---这是权限验证2----")
        func()
    return call_func



def test1():
    print('----test1----')

test1=set_func(test1)  #装饰器实际做了这个事情
test1()
pass