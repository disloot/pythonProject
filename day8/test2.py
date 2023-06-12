#!usr/bin/python3
# author lyle

class Person(object):
    def __init__(self, name, age, height):
        self.__name = name
        self.__age = age
        self.__height = height

    def run(self):
        print('跑了步')

    def eat(self):
        print('吃东西了')

    def __str__(self):
        return '%s%d岁身高%.2f米' % (self.__name, self.__age, self.__height)


class Dog(object):
    value = 0

    def __init__(self, name, color):
        self.color = color
        self.name = name
        Dog.value += 1

    def bark(self):
        print("汪汪叫")

    def shake(self):
        print('摇尾巴')

    def __str__(self):
        return '%s %s色' % (self.name, self.color)

    @classmethod
    def create(cls):
        cls.value += 1


class GodDog(Dog):

    def __init__(self, name, color):
        self.color = color
        self.name = name
        Dog.value += 2

    def bark(self):
        super().bark()
        print('狂吠')


if __name__ == '__main__':
    xiaoming = Person('小明', 18, 1.75)
    xiaomei = Person('小美', 17, 1.65)
    xiaoming.run()
    xiaomei.eat()
    print(xiaomei)
    print(xiaoming)
    dog = Dog('大黄', '黄')
    print(dog)
    dog.name = '小黄'
    print(dog)
    god_dog = GodDog('哮天犬', '黑')
    god_dog.bark()
    Dog.value += 1
    god_dog.value = 1
    Dog.create()
    print(god_dog)
    print(Dog.value)
    print(dog.value)
    print(god_dog.value)
    print(id(Dog.value))
    print(id(dog.value))
    print(id(god_dog.value))
