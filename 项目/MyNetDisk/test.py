import re
while True:
    user_name = input('输入用户名（数字或字母或下划线长度不超过8位）：')
    if not re.search(r'[\W]', user_name):
        break
print('done')