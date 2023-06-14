

def print_diamond1():
    # abs求绝对值
    i = 1
    while i <= 9:
        j = 1
        while j <= abs(5 - i):
            print(' ', end='')
            j += 1
        j = 1
        while j <= 9 - 2 * abs(5 - i):
            if j % 2 == 0:
                print(' ', end='')
            else:
                print('*', end='')
            j += 1
        print()
        i += 1


def print_diamond2():
    # abs求绝对值
    i = 1
    while i <= 9:
        print(' ' * abs(5 - i), end='')
        j = 1
        while j <= 9 - 2 * abs(5 - i):
            if j == 1 or j == 9 - 2 * abs(5 - i):  # 如果是第一个，或者最后一个，打印
                print('*', end='')
            else:
                print(' ', end='')
            j += 1
        print()
        i += 1


# 找101个数中的出现1次的数
def find_list101_one():
    list1 = [8, 3, 2, 6, 3, 8, 2]  # 所有的数都异或起来，就得到了出现1次的那个数
    result = 0
    for i in list1:
        result ^= i
    print(result)


# 找102个数中的出现1次的两个数，如何把出现1次的两个数分到两堆
def find_list102_one():
    list1 = [8, 3, 2, 6, 3, 8, 2, 11]
    result = 0
    for i in list1:
        result ^= i
    split_flag = result & -result
    result1 = 0
    result2 = 0
    for i in list1:
        if split_flag & i:
            result1 ^= i
        else:
            result2 ^= i
    print('出现1次的两个数分别是 %d %d' % (result1,result2))

def answer_62():
    # list1=['Hello', 'David', 'OK,over', 'nice me you']
    list1 = ['Hello', '我是David', 'OK, 好', '很高兴认识你']  #这个默认是不太对齐的
    for i in list1:
        print('%s' % i.center(30))

def use_format():
    i=98.5
    j=10
    print('我很帅{} {}'.format(i,j))


if __name__ == '__main__':
    # print_diamond1()
    # print_diamond2()
    # find_list101_one()
    # find_list102_one()
    answer_62()
    # use_format()