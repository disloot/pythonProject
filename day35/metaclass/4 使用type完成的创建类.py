# 作者: 王道 龙哥
# 2022年03月25日11时28分44秒
class A(object):
    num = 100


def print_b(self):
    print(self.num)


@staticmethod
def print_static():
    print("----haha-----")


@classmethod
def print_class(cls):
    print(cls.num)


B = type("B", (A,), {"print_b": print_b, "print_static": print_static,
                     "print_class": print_class})
b = B()
b.print_b()
b.print_static()
b.print_class()

a = A()
print(a.__class__)
print(a.__class__.__class__)
i = 1
print(i.__class__)
print(i.__class__.__class__)
