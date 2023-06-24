# 作者: 王道 龙哥
# 2022年03月25日11时13分24秒
from test import ObjectCreator

print(ObjectCreator)
# 不带属性
Test2 = type('Test2', (), {})
print(Test2)  # <class '__main__.Test2'>  main代表所属的模块

t = Test2()
print(t)

print(help(Test2))
print('-' * 50)
# 使用type创建带属性的类
Foo = type('Foo', (), {'bar': True})
print(Foo.bar)

# 使用type创建继承父类的子类
FooChild = type('FooChild', (Foo,), {})
print(FooChild.bar)


def echo_bar(self):
    print('echo bar:', end=' ')
    print(self.bar)


# 让FooChild类中的echo_bar属性，指向了上面定义的函数
FooChild = type('FooChild', (Foo,), {'echo_bar': echo_bar})
my_foo = FooChild()
my_foo.echo_bar()
