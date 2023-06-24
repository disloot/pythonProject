# 作者: 王道 龙哥
# 2022年03月25日16时22分23秒
from abc import abstractmethod, ABCMeta


class WalkAnimal(metaclass=ABCMeta):
    @abstractmethod
    def walk(self):
        pass


class SwimAnimal(metaclass=ABCMeta):
    @abstractmethod
    def swim(self):
        pass


class FlyAnimal(metaclass=ABCMeta):
    @abstractmethod
    def fly(self):
        pass


# 如果正常一个老虎有跑和跑的方法的话，我们会这么做
class Tiger(WalkAnimal, SwimAnimal):
    def walk(self): pass

    def swim(self): pass


t = Tiger()
