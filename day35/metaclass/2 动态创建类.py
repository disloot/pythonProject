# 作者: 王道 龙哥
# 2022年03月25日11时03分10秒
def choose_class(name):
    if name == 'foo':
        class Foo(object):
            pass

        return Foo  # 返回的是类，不是类的实例
    else:
        class Bar(object):
            pass

    return Bar


MyClass = choose_class('foo')
print(MyClass)
m = MyClass()
print(m)
