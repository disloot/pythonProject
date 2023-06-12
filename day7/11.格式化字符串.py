info_tuple = ("小明", 21, 1.85)

# 格式化字符串后面的 `()` 本质上就是元组
print("%s 年龄是 %d 身高是 %.2f" % info_tuple)

info_str = "%s 年龄是 %d 身高是 %.2f" % info_tuple

print(type(info_str))

info = ("zhangsan", 18)
demo_list = list(info)
print(demo_list)
demo_tuple = tuple(demo_list)
print(demo_tuple)

# 元组生成式,要在外面加tuple

demo_tuple1 = tuple(x for x in range(10))
print(demo_tuple1)
