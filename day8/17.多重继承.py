
class A:
    def demo(self):
        print('A demo')

    def test(self):
        print('A test')


class B:
    def demo(self):
        print('B demo')

    def test(self):
        print('B test')

class C(A,B):
    def demo(self):
        print('C demo')

print(C.__mro__)
c=C()
c.demo()