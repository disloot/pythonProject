
class Line5(object):
    def __init__(self, k, b):
        self.k = k
        self.b = b

    def __call__(self, x):
        print(self.k * x + self.b)


line1=Line5(2,3)

line1(3)

line2=Line5(5,6)

line2(3)