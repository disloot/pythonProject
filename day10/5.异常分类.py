
def exception_separate():
    try:
        num = int(input("请输入整数："))
        result = 8 / num
        print(result)
    except ValueError:
        print("请输入正确的整数")
    except ZeroDivisionError:
        print("除 0 错误")
    except Exception as result:  #所有没有提前设置的异常都会走到这里
        print("未知错误 %s" % result)
    else: #else下面的代码如果有异常，进程会直接结束
        print("正常执行")
    finally:  #为了让阅读代码者知道这里是一个整体
        print("执行完成，无论是否有异常，都会执行")


if __name__ == '__main__':
    exception_separate()
