# 作者: 王道 龙哥
# 2022年03月24日15时14分59秒
def my_decorator(func):
    def wper(*args, **kwargs):
        '''decorator'''
        print('Calling decorated function...')
        return func(*args, **kwargs)
    return wper

@my_decorator
def example():
    """Docstring"""
    print('Called example function')


print(example.__name__, example.__doc__)#wper decorator

from functools import wraps


def my_new_decorator(func):
    @wraps(func)
    def wper(*args, **kwargs):
        '''decorator'''
        print('Calling decorated function...')
        return func(*args, **kwargs)

    return wper

@my_new_decorator
def example1():
    """I am example1"""
    print('Called example1 function')

print(example1.__name__, example1.__doc__)
example1()