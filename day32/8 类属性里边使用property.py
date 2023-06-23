
class Foo:
    """
    我是Foo类
    """
    def get_bar(self):
        return 'laowang'

    BAR = property(get_bar)

print(Foo.BAR)  #BAR不是类属性
print(Foo.__doc__)
help(Foo)
obj = Foo()
reuslt = obj.BAR  # 自动调用get_bar方法，并获取方法的返回值
print(reuslt)