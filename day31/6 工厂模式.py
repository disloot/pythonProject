
class Animal():

    def eat(self):
        pass

    def voice(self):
        pass


class Dog(Animal):
    def eat(self):
        print('狗吃骨头')

    def voice(self):
        print('狗叫汪汪')


class Cat(Animal):
    def eat(self):
        print('猫吃鱼')

    def voice(self):
        print('猫叫喵喵')


class FactoryMode():
    def __init__(self):
        self.d={'dog':Dog,'cat':Cat}
    def create_ani(self, animal_name):
        return self.d[animal_name]()

f=FactoryMode()
animal=f.create_ani('dog')
animal.eat()
animal.voice()
