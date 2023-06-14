
class Women:

    def __init__(self, name):
        self.name = name
        # 不要问女生的年龄
        self.__age = 18

        # self._height=186  #不这样用

    def eat(self):
        self.__secret()  # 私有方法只能被自己的方法调用

    def __secret(self):
        print("我的年龄是 %d" % self.__age)  # 私有属性只能被自己的方法调用


xiaomei = Women('小美')
print(xiaomei.name)
xiaomei.eat()

# print(xiaomei._height)


