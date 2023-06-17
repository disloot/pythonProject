
import re

# search 匹配到就返回
ret = re.search(r"\d+", "阅读次数为 9996,点赞次数 888")
print(ret.group())

# findall会匹配到字符串末尾，列表返回，不要用group
ret = re.findall(r"\d+", "python = 9999, c = 7890, c++ = 12345")
print(ret)

s = 'hello world, now is 2020/7/20 18:48, 现在是2020年7月20日18时48分。'
ret_s = re.sub(r'年|月', r'/', s)
ret_s = re.sub(r'日|分', r' ', ret_s)
ret_s = re.sub(r'时', r':', ret_s)
print(ret_s)

# hello world, now is 2020/7/20 18:48, 现在是2020/7/20 18:48
# compile避免了每次都去写正则，findall 有问题
com = re.compile(r'\d{4}/[01]?[0-9]/[1-3]?[0-9]\s(0[0-9]|1[0-9]|2[0-4]):[0-5][0-9]')
ret = com.findall(ret_s)
print(ret)

# ?:可以避免findall只提取分组内的内容
com1 = re.compile(r'\d{4}/[01]?[0-9]/[1-3]?[0-9]\s(?:0[0-9]|1[0-9]|2[0-4]):[0-5][0-9]')
ret = com1.findall(ret_s)
print(ret)


def add(temp):
    strNum = temp.group()
    print(temp.group())
    num = int(strNum) + 1
    return str(num)


ret = re.sub(r"\d+", add, "python = 997asdf123")
print(ret)

ret = re.sub(r"\d+", lambda temp: str(int(temp.group()) + 1), "python = 99aadsfa123")
print(ret)
 