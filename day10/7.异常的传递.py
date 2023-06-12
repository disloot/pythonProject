# author luke
# 2022年02月24日

def demo1():
    num=int(input("输入整数："))
    return num


def demo2():
    return demo1  ()

# 利用异常的传递性，在主程序捕获异常
try:
    num=demo2()
except Exception as result:
    print("未知错误 %s" % result)
    print(result.__traceback__.tb_lineno)
finally:
    print(num)  #异常时实际num并没有得到赋值，因此不存在