# 查看两个变量的id情况
def var_id():
    a = 1
    print(id(a))
    b = 1
    print(id(b))
    a = 2
    print(id(a))


# 想用change改变a的值,实际没有
def change(num):
    print("num=%d时在函数内的内存地址是 %d" % (num, id(num)))
    num = 20
    print("num=%d时在函数内的内存地址是 %d" % (num, id(num)))


def big_int_id():
    a = -300
    print(id(a))
    del a
    b = -300
    print(id(b))


# 理解python中变量，数据之间的关系
if __name__ == '__main__':
    var_id()
    print("-" * 50)
    a = 10
    print(id(a))
    change(a)
    print(a)  # a不会发生改变
    print("-" * 50)
    big_int_id()
