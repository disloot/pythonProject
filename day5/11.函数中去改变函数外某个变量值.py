def use_list():
    demo_list = [1, 2, 3]  # demo_list是一个列表

    print(demo_list)
    print("定义列表后的内存地址 %d" % id(demo_list))

    print(demo_list[0])
    print(demo_list[1])
    print(demo_list[2])
    demo_list[0] = 10
    print("改变后列表的内存地址 %d" % id(demo_list))
    print(type(demo_list))


# 可变数据类型可以在子函数中去通过其接口修改数据空间中的值
def change(my_list):
    my_list[0] = 20


# 不可变数据类型只能通过赋值运算符对其直接赋值，地址会发生改变
def use_tuple():
    demo_tuple = (1, 2, 3)
    print(id(demo_tuple))
    print(demo_tuple[0])
    demo_tuple = (4, 5, 6)
    print(id(demo_tuple))


def use_same_tuple():
    tuple1 = (1, 2, 3)
    tuple2 = (1, 2, 3)
    print(id(tuple1))
    print(id(tuple2))


def use_hash():
    print(hash("xiaoming"))
    print(hash("xiaoming"))


if __name__ == '__main__':
    use_hash()
