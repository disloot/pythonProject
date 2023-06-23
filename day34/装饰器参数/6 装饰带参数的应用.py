# 作者: 王道 龙哥
# 2022年03月24日14时56分46秒
def set_level(level_num):
    def set_func(func):
        def call_func(*args, **kwargs):
            nonlocal level_num
            if level_num == 1:
                print("----权限级别1，验证----")
            elif level_num == 2:
                print("----权限级别2，验证----")
            level_num=3
            return func()

        return call_func
    return set_func


@set_level(1)
def test1():
    print("-----test1---")
    return "ok"


@set_level(2)
def test2():
    print("-----test2---")
    return "ok"


test1()
test2()