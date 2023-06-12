# 定义一个函数，通过def，下面是算术运算
def calc():
    print(5 / 2)  # 不是整除
    print(5 // 2)  # 整除
    print(5 % 2)  # 取余  取模
    print(2 ** 3)  # 2的3次方
    print(3 + 5 - 2)  # 相同优先级从左到右


# 关系运算
def relation():
    num = int(input('请输入一个数:'))
    print(3 < num < 10)  # python支持某个数关系运算符连写


# 逻辑运算
def logic():
    # year=int(input('请输入年份:'))
    # print(year%400==0 or year%4==0 and year%100!=0 )
    print(5 and 3)
    print(5 or 3)


# 赋值运算符
def assign():
    a = 3
    a += 4
    print(a)
    # if a=5: 不可以在if后写一个赋值表达式
    b=100
    a,b=b,a  #两个数进行交换
    print(a,b)

# 位运算
# 1 byte(字节）=8 bit(位)
# 1 KB=1024 byte
# 1MB=1024 KB
# 只能对整数做位运算
def bit():
    i = 5
    j = 7
    print(i & j)  # 5
    print(i | j)  # 7
    print(i ^ j)  # 异或  2
    print(~i)  # 按位取反
    print(i << 1)  # 左移是乘2
    print(i >> 1)  # 右移是正数整除2，负数的右移是减一整除2


if __name__ == '__main__':
    # calc()
    # relation()
    # logic()
    assign()
    # bit()
