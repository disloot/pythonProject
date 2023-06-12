# 作者: 王道 龙哥
# 2022年03月09日11时20分28秒
import re

def use_email():
    email_list = ["xiaoWang@163.com", "xiaoWang@163.comheihei", ".com.xiaowang@qq.com"]

    for email in email_list:
        ret = re.match("[\w]{4,20}@163\.com$", email)
        if ret:
            print("%s 是符合规定的邮件地址,匹配后的结果是:%s" % (email, ret.group()))
        else:
            print("%s 不符合要求" % email)
# 只要零到99
def use_099():
    ret = re.match("[1-9]?\d$", "0")
    print(ret.group())
if __name__ == '__main__':
    # use_email()
    use_099()