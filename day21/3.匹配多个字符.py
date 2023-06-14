
import re

def use_star():
    ret = re.match("[A-Z][a-z]*","M")
    print(ret.group())

    ret = re.match("[A-Z][a-z]*","MnnM")
    print(ret.group())

    ret = re.match("[A-Z][a-z]*","Aabcdef")
    print(ret.group())

def use_plus():

    names = ["name1", "_name", "2_name", "__name__"]

    for name in names:
        ret = re.match("[a-zA-Z_]+[a-zA-Z_0-9]*", name)
        if ret:
            print(f"变量名 {ret.group()} 符合要求")
        else:
            print(f"变量名 {name} 非法")


# 使用问号
def use_question():
    ret = re.match("[1-9]?[0-9]", "7")
    print(ret.group())

    ret = re.match("[1-9]?\d", "33")
    print(ret.group())

    ret = re.match("[1-9]?\d", "09")  #到开头结尾
    print(ret.group())

# 字符数量由自己控制
def use_m():
    ret = re.match("[a-zA-Z0-9_]{3}", "12a3g45678")
    print(ret.group())

    ret = re.match("[a-zA-Z0-9_]{8,20}", "1ad12f23s34455ff66")
    print(ret.group())

if __name__ == '__main__':
    # use_star()
    # use_plus()
    # use_question()
    use_m()