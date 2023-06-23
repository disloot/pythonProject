
x = 300 # 这是 global

def test1():
    
    # x = 200 # 这是 nonlocal

    def test2():
        global x
        # nonlocal x  #如果要使用外部函数的变量，需要加nonlocal
        print("----1----x=%d" % x)
        x = 100
        print("----2----x=%d" % x)

    return test2


t1 = test1()
t1()
print(x)