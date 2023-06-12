# 作者: 王道 龙哥
# 2022年03月09日10时24分59秒
import re
def example1():
    ret = re.match(".","M")
    print(ret.group())

    ret = re.match("t.o","too")
    print(ret.group())

    ret = re.match("t.o","two")
    print(ret.group())

def example2():
    # 如果hello的首字符小写，那么正则表达式需要小写的h
    ret = re.match("h", "hello Python")
    print(ret.group())

    # 如果hello的首字符大写，那么正则表达式需要大写的H
    ret = re.match("H", "Hello Python")
    print(ret.group())

    # 大小写h都可以的情况
    ret = re.match("[hH]", "hello Python")
    print(ret.group())
    ret = re.match("[hH]", "Hello Python")
    print(ret.group())
    ret = re.match("[hH]ello Python", "Hello Python")
    print(ret.group())

    # 匹配0到9第一种写法
    ret = re.match("[0123456789]Hello Python", "7Hello Python")
    print(ret.group())

    # 匹配0到9第二种写法
    ret = re.match("[0-9]Hello Python", "7Hello Python")
    print(ret.group())

    ret = re.match("[0-35-9]Hello Python", "7Hello Python")
    print(ret.group())

    # 下面这个正则不能够匹配到数字4，因此ret为None
    ret = re.match("[0-35-9]Hello Python", "4Hello Python")
    if ret:
        print(ret.group())

def match_decimal():
    # 使用\d进行匹配
    ret = re.match("嫦娥\d号", "嫦娥9号发射成功")
    print(ret.group())

    ret = re.match("嫦娥\d号", "嫦娥2号发射成功")
    print(ret.group())

    ret = re.match("嫦娥\d号", "嫦娥3号发射成功")
    print(ret.group())

def match_space():
    ret = re.match("嫦娥\s号", "嫦娥 号发射成功")
    print(ret.group())

def match_word():
    ret = re.match("嫦娥\w号", "嫦娥五号发射成功")
    print(ret.group())

if __name__ == '__main__':
    # example1()
    # example2()
    # match_decimal()
    # match_space()
    match_word()