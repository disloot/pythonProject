# 作者: 王道 龙哥
# 2022年03月08日14时40分08秒

from collections.abc import Iterable
class MyList:
    def __init__(self):
        self.container=[]

    def add(self,item):
        self.container.append(item)

    # 只要重写了iter方法，就会变为可迭代的
    def __iter__(self):
        pass

if __name__ == '__main__':
    mylist=MyList()
    mylist.add(1)
    mylist.add(2)
    mylist.add(3)
    print(isinstance(mylist,Iterable))
    # for i in mylist:
    #     print(i)

