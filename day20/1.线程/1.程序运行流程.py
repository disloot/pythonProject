# 作者: 王道 龙哥
# 2022年03月08日09时46分42秒
from time import sleep

def sing():
    for i in range(3):
        print("正在唱歌...%d"%i)
        sleep(1)

def dance():
    for i in range(3):
        print("正在跳舞...%d"%i)
        sleep(1)

if __name__ == '__main__':
    sing() #唱歌
    dance() #跳舞