

# 解释器知道这里定义了一个函数
def say_hello():
    """
    我只是一个快捷的注释
    :return:
    """
    print("hello 1")
    print("hello 2")
    print("hello 3")


# 只有在调用函数时，之前定义的函数才会被执行
# 函数执行完成之后，会重新回到之前的程序中，继续执行后续的代码
say_hello()
print('xiaoming')