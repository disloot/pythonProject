
def add_first(func):
   print("---开始进行装饰权限1的功能---")
   def call_func(*args, **kwargs):
      print("---这是权限验证1----")
      return func(*args, **kwargs)
   return call_func


def add_second(func):
   print("---开始进行装饰权限2的功能---")
   def call_func(*args, **kwargs):
      print("---这是权限验证2----")
      return func(*args, **kwargs)
   return call_func

# 离函数越近的先装饰
@add_first
@add_second
def test1():
    print('--test1--')

# s=add_second(test1)
# f=add_first(s)

# 后装饰的先执行
test1()

