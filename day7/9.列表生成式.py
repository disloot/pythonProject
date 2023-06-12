# 列表推导式：用来快速地生成列表。
# 好处：代码比较短
# 坏处：可读性差
#
# [元素表达式 if(条件)  else  for 变量 in 迭代对象 ]
# 简单使用
a = [x for x in range(10)]
print(a)  #0到9
b = []
for x in range(10):
    b.append(x)
print(b)
# 2个for循环
a = [j for i in range(10) for j in range(i)]
print(a)
a = [[col*row for col in range(5)] for row in range(5)]
print(a)
a = [j for x in a for j in x]  # 2维列表转1维列表
print(a)
# 只有if时
a = [x for x in range(10) if x % 2 == 0]  # 将只会筛选偶数
print(a)
# if-else的三元表达式
a = [x if x % 2 == 0 else x ** 2 for x in range(10)]
print(a)

a = [x**2 for x in range(10)]
print(a)
