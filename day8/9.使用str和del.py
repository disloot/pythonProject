#!/usr/bin/python
# author luke
# 2022年02月22日
class Cat:

    def __init__(self, new_name):

        self.name = new_name

        print("%s 来了" % self.name)

    def __del__(self):  #对象销毁的时候调用
        print("%s 我去了" % self.name)


    def __str__(self):  #打印对象调用这个

        # 必须返回一个字符串
        return "我是小猫[%s]" % self.name

tom=Cat('Tom')
print(tom)
del tom
pass