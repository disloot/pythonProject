

def use_if():
    # 1. 定义年龄变量
    age = 17

    # 2. 判断是否满 18 岁
    # if 语句以及缩进部分的代码是一个完整的代码块
    if age >= 18:
        print("可以进网吧嗨皮……")
        print('打游戏')
    else:
        print("你还没长大，应该回家写作业！")

    # 3. 思考！- 无论条件是否满足都会执行
    print("这句代码什么时候执行?")

def use_if2():
    python_score = 50
    c_score = 50

    # 要求只要有一门成绩 > 60 分就算合格
    #not 优先级低于 关系运算符
    if not python_score > 60 or c_score > 60:
        print("考试通过")
    else:
        print("再接再厉！")


def use_elif():
    holiday_name = "情人节"

    if holiday_name == "情人节":
        print("买玫瑰")
        print("看电影")
    elif holiday_name == "平安夜":
        print("买苹果")
        print("吃大餐")
    elif holiday_name == "生日":
        print("买蛋糕")
    else:
        print("每天都是节日啊……")

# if 嵌套
def use_if_else():
    # 定义布尔型变量 has_ticket 表示是否有车票
    has_ticket = True

    # 定义整数型变量 knife_length 表示刀的长度，单位：厘米
    knife_length = 20

    # 首先检查是否有车票，如果有，才允许进行 安检
    if has_ticket:
        print("有车票，可以开始安检...")

        # 安检时，需要检查刀的长度，判断是否超过 20 厘米
        # 如果超过 20 厘米，提示刀的长度，不允许上车
        if knife_length >= 20:
            print("不允许携带 %d 厘米长的刀上车" % knife_length)
        # 如果不超过 20 厘米，安检通过
        else:
            print("安检通过，祝您旅途愉快……")

    # 如果没有车票，不允许进门
    else:
        print("大哥，您要先买票啊")



if __name__ == '__main__':
    # use_if()
    # use_if2()
    # use_elif()
    use_if_else()