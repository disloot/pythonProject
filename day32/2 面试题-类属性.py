
class Parent(object):
    x = 1

class Child1(Parent):
    pass

class Child2(Parent):
    pass

print(Parent.x, Child1.x, Child2.x)
Child1.x = 2  #对child1增加了类属性
print(Parent.x, Child1.x, Child2.x)
Parent.x = 3
print(Parent.x, Child1.x, Child2.x)


c1=Child1()
c2=Child2()
p=Parent()
print(c1.x,c2.x,p.x)
c1.x=4
print(c1.x,c2.x,p.x)
print(Child1.x, Child2.x,Parent.x)
p.x=5
print(c1.x,c2.x,p.x)