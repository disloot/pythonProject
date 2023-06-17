
import re
# 使用|和（）
def use_two():
    ret = re.match("[1-9]?\d$|100","8")
    print(ret.group())

    #匹配3种类型邮箱
    ret=re.match('\w{4,20}@(163|qq|126)\.com','12345@126.com')
    print(ret.group())

    ret = re.match("\w{4,20}@(163|126|qq)\.com", "test@gmail.com")
    if ret:
        print(ret.group())
    else:
        print("不是163、126、qq邮箱")


    tels = ["13100001234", "18912344321", "10086", "18800007777"]
    for i in tels:
        ret=re.match('1\d{9}[0-35-68-9]$',i)
        if ret:
            print('{} is a phone num'.format(ret.group()))
        else:
            print('{} is not a good phone num'.format(i))

    # ([^-]+) 代表没有遇到小横杠-就一直进行匹配，一直匹配下去
    ret = re.match("([^-]+)-(\d+)","010-12345678")
    print(ret.group())
    print(ret.group(1))
    print(ret.group(2))

#使用引用分组
def use_group():
    # 能够完成对正确的字符串的匹配
    ret = re.match("<[a-zA-Z]*>\w*</[a-zA-Z]*>", "<html>hh</html>")
    print(ret.group())

    # 如果遇到非正常的html格式字符串，匹配出错
    ret = re.match("<[a-zA-Z]*>\w*</[a-zA-Z]*>", "<html>hh</htmlbalabala>")
    print(ret.group())

    # 通过引用分组中匹配到的数据即可，但是要注意是元字符串，即类似 r""这种格式
    ret = re.match(r"<([a-zA-Z]*)>\w*</\1>", "<div>hh</div>")
    print(ret.group())

    # 因为2对<>中的数据不一致，所以没有匹配出来
    test_label = "<html>hh</htmlbalabala>"
    ret = re.match(r"<([a-zA-Z]*)>\w*</\1>", test_label)
    if ret:
        print(ret.group())
    else:
        print("%s 这是一对不正确的标签" % test_label)

    labels = ["<html><h1>www.cskaoyan.com</h1></html>", "<html><h1>www.cskaoyan.com</h2></html>"]

    for label in labels:
        ret = re.match(r"<(\w*)><(\w*)>.*</\2></\1>", label)
        if ret:
            print("%s 是符合要求的标签" % ret.group())
        else:
            print("%s 不符合要求" % label)

    # 通过?P<>来起名,<>内是它的名字
    ret = re.match(r"<(?P<name1>\w*)><(?P<name2>\w*)>.*</(?P=name2)></(?P=name1)>",
               "<html><h1>www.cskaoyan.com</h1></html>")
    print(ret.group())
if __name__ == '__main__':
    use_group()