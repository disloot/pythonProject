name = input("请输入姓名：")
company = input("输入公司名称：")
title = input("输入职位：")
phone = input("输入电话号码：")
email = input("输入电子邮箱：")

print("*" * 50)
print(company)
print()
print("%s(%s)\n" % (name, title))
print("电话：%s" % phone)
print("邮箱：%s" % email)

