
print(eval("1+1"))

print(type(eval("[1, 2, 3, 4, 5]")))
str1="{'name': 'xiaoming', 'age': 18}"
print(type(str1))
print(type(eval(str1)))

# 安全风险，不要用eval去执行前端传递过来的字符串
eval("__import__('os').system('ls')")