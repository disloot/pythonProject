# 作者: 王道 龙哥
# 2022年03月08日10时29分30秒
from threading import Thread
import time

def work1(nums):
    nums.append(44)
    print("----in work1---",nums)


def work2(nums):
    #延时一会，保证t1线程中的事情做完
    time.sleep(1)
    print("----in work2---",nums)

def main():
    g_nums = [11,22,33]

    t1 = Thread(target=work1, args=(g_nums,))
    t1.start()

    t2 = Thread(target=work2, args=(g_nums,))
    t2.start()

if __name__ == '__main__':
    main()