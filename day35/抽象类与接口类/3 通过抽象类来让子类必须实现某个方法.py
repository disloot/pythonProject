# 作者: 王道 龙哥
# 2022年03月25日16时14分54秒

from abc import abstractmethod, ABCMeta


# 使用了抽象方法的类，就是抽象类，Payment就是一个抽象类
class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self, money):
        pass


class Alipay(Payment):
    def pay(self, money):  # 这里类的方法不是一致的pay,导致后面调用的时候找不到pay
        print('支付宝支付了')


# 如果子类中没有实现抽象方法，实例化对象时，就会报错
p = Alipay()
