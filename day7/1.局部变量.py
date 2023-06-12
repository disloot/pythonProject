def demo1():
    num = 10
    print(num)
    num = 20
    print("修改后 %d" % num)


def demo2():
    num = 100
    print(num)
    # for或者while内定义的变量在函数内均有效
    for i in range(1):
        num1 = 200
    print(num1)


# 局部变量修改相互之间不影响,局部变量在函数结束后释放
demo1()
demo2()

print("over")
