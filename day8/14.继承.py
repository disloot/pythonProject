
class Animal:

    def eat(self):
        print("吃---")

    def drink(self):
        print("喝---")

    def run(self):
        print("跑---")

    def sleep(self):
        print("睡---")


class Dog(Animal):
    def bark(self):
        print("汪汪叫")


class Cat(Animal):
    def catch(self):
        print('爬树')


class XiaoTianQuan(Dog):
    def fly(self):
        print('会飞')


# 创建一个对象 - 狗对象
wangcai = Dog()

wangcai.eat()
wangcai.drink()
wangcai.run()
wangcai.sleep()
wangcai.bark()

shenquan = XiaoTianQuan()
shenquan.fly()
