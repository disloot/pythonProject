# 作者: 王道 龙哥
# 2022年03月24日15时05分36秒

class Test:
    def __init__(self, func):
        self.__func = func

    def __call__(self, *args, **kwargs):
        print('权限验证')
        self.__func(*args, **kwargs)


@Test
def foo(name):
    print(f'I am foo {name}')


foo(123)
