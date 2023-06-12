# 作者: 王道 龙哥
# 2022年03月08日14时59分54秒
# 作者: 王道 龙哥
# 2022年03月08日14时40分08秒

from collections.abc import Iterable
class MyList:
    def __init__(self):
        self.container=[]

    def add(self,item):
        self.container.append(item)

    # 只要重写了iter方法，就会变为可迭代的,iter必须返回一个迭代器
    def __iter__(self):
        myiterator=MyIterator(self)
        return myiterator

class MyIterator:
    def __init__(self,mylist):
        self.mylist:MyList = mylist
        # current用来记录当前访问到的位置
        self.current = 0


    def __next__(self):
        current=self.current
        self.current+=1
        if current<len(self.mylist.container):
            return self.mylist.container[current]
        else:
            raise StopIteration

    def __iter__(self): #iter必须返回一个迭代器
        return self


if __name__ == '__main__':
    mylist=MyList()
    mylist.add(1)
    mylist.add(2)
    mylist.add(3)
    print(isinstance(mylist,Iterable))
    #for 是先对 myiter=iter(mylist) ,不断的next(myiter)
    for i in mylist:
        print(i)
    # myiter = iter(mylist)
    # print(next(myiter))
    # print(next(myiter))
    # print(next(myiter))
    # print(next(myiter))
