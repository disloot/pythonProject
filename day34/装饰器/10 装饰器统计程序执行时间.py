
import time

def set_func(func):
   def call_func():
      start_time = time.time()  #开始
      func()
      stop_time = time.time()  #结束
      print("alltimeis %f" % (stop_time - start_time))
   return call_func

@set_func
def test1():
   """
   我是test1
   :return:
   """
   print("-----test1----")
   for i in range(1000000):
      pass

test1()
print(test1.__doc__)