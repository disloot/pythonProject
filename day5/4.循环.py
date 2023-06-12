def use_while():
    # 1. 定义重复次数计数器
    i = 1

    # 2. 使用 while 判断条件
    while i <= 5:
        # 要重复执行的代码
        print("Hello Python")
        # 处理计数器 i
        i = i + 1

    print("循环结束后的 i = %d" % i)


# 从1加到100
def cal_sum():
    # 计算 0 ~ 100 之间所有数字的累计求和结果
    # 0. 定义最终结果的变量
    result = 0

    # 1. 定义一个整数的变量记录循环的次数
    i = 0

    # 2. 开始循环
    while i <= 100:
        # print(i)
        if i % 2 == 0:
            i += 1
            continue  # continue之前必须有让i趋近于假的条件
        # 每一次循环，都让 result 这个变量和 i 这个计数器相加
        result += i

        # 处理计数器
        i += 1

    print("0~100之间的数字求和结果 = %d" % result)


def cal_sum2():
    # 计算 0 ~ 50 之间所有数字的累计求和结果
    # 0. 定义最终结果的变量
    result = 0

    # 1. 定义一个整数的变量记录循环的次数
    i = 0

    # 2. 开始循环
    while i <= 100:
        # print(i)
        if i >50:
            break  #循环终止了
        # 每一次循环，都让 result 这个变量和 i 这个计数器相加
        result += i

        # 处理计数器
        i += 1

    print("0~100之间的数字求和结果 = %d" % result)

if __name__ == '__main__':
    # use_while()
    # cal_sum()
    cal_sum2()
