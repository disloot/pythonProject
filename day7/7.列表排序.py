name_list = ["zhangsan", "lisi", "wangwu", "wangxiaoer"]
num_list = [6, 8, 4, 1, 10]

# 升序,默认
name_list.sort()
num_list.sort()
print(name_list)
print(num_list)
print('-' * 50)

# 降序
name_list.sort(reverse=True)
num_list.sort(reverse=True)
print(name_list)
print(num_list)
print('-' * 50)
# 逆序（反转），本身不做排序操作的
name_list.reverse()  # reverse不可以传参
print(name_list)
num_list.reverse()

print(name_list)
print(num_list)
