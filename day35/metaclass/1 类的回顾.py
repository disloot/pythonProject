# 作者: 王道 龙哥
# 2022年03月25日10时55分38秒
class ObjectCreator(object):
    pass


my_object = ObjectCreator()
print(my_object)

print(ObjectCreator)


def echo(obj):
    print(obj)


echo(ObjectCreator)

# hasattr用来判断一个对象是否有某个属性，有就是True，没有就是false
print(hasattr(ObjectCreator, 'new_attribute'))

ObjectCreator.new_attribute = 'foo'  # 你可以为类增加属性

print(hasattr(ObjectCreator, 'new_attribute'))

# 把类名给一个变量
val = ObjectCreator
print(val)

print(type(1))
print(type(my_object))
print(type(ObjectCreator))

# 创建类出来的那个类，叫元类
