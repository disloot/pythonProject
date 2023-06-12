#!usr/bin/python3
# author lyle
file = open('./dir/file1.txt', encoding='utf-8')
text = file.read()
print(text)
file.close()