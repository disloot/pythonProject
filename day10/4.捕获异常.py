# author luke
# 2022年02月24日

try:
    num=int(input('请输入一个整数：'))
    print(num)
except:  #出现异常才会走到except，有了except，程序不会崩溃
    print('请输入整数！！！')

print('you can see me ')