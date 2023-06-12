# 定义一个全局变量
num = 10


def demo1():
    # num=20 # 并没有修改到全局变量，只是定义了一个局部变量,内部使用是就近原则
    global num
    num += 20
    print(num)


def demo2():
    print(num)


# 针对全局变量，读的时候可以不加，要修改时候，要加上global
demo1()
demo2()

print("over")
