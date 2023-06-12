import my_module


def no_1():  # 1到100奇数求和
    i = 1
    result = 0
    while i <= 100:
        result += i
        i += 2
    print(result)


def no_2():  # 九九乘法表
    num1 = 1
    num2 = 1
    for i in range(1, 10):
        for j in range(1, i + 1):
            print("%d*%d = %d" % (j, i, j * i), end="  ")
        print()


def no_3():
    choose = int(input("选择形状："))
    a = [4, 3, 2, 1, 0, 1, 2, 3, 4]
    if choose == 1:
        for i in a:
            print(" " * i, end="")
            print("* " * (5 - i))
    if choose == 2:
        for i in a:
            print(" " * i, end="")
            if i != 4:
                print("*", end=" " * ((2 * (4 - i)) - 1))
                print("*")
            else:
                print("*")


def no_4():
    x = int(input("输入一个数："))

    if x == 0:
        print(0)
    elif x > 0:
        a = tuple(bin(x))
        print(a.count('1'))
    else:
        x = 2 ** 64 + x
        a = tuple(bin(x))
        result = a.count('1')
        print(result)


def no_5():
    a = []
    print("依次输入4个数，其中3个数输入两次，1个数输入1次，顺序可以打乱，共输入7次")
    for i in range(1, 8):
        a.append(int(input("第%d次输入：" % i)))
    for i in range(7):
        if a.count(a[i]) == 1:
            print(a[i])
            break


def no_6():
    for i in range(1, 21):
        print(i, end=" ")


def say_hello():
    '''打印多次say hello'''
    count = int(input("输入打印次数："))
    for i in range(count):
        print("say hello")


def no_10():
    for i in range(3, 0, -1):
        print(" " * i, end="")
        print("* " * (5 - i), end="")
        print(" " * (2 * i), end="")
        print("* " * (5 - i), end="")
        print()
    for i in range(10, 0, -1):
        print(" " * (10 - i), end="")
        print("* " * i, end="")
        print()


def no_11():
    a = []
    print("依次输入4个数，其中3个数输入两次，2个数输入1次，顺序可以打乱，共输入8次")
    for i in range(1, 9):
        a.append(int(input("第%d次输入：" % i)))
    for i in range(8):
        if a.count(a[i]) == 1:
            print(a[i], end=" ")


if __name__ == '__main__':
    my_module.print_line("-")
    no_11()
