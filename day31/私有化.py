class A :
    def __init__(self) -> None:
        self._a = 'a'
        self.__a = 'aa'
    def use__a(self):
        print(self.__a)
a = A()

print(a._a)
a.use__a()
print(a._A__a) 