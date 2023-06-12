#!/usr/bin/python
# author luke
# 2022年02月21日


xiaoming = {"name": "小明",
            "age": 18,
            "gender": True,
            "height": 1.75}


# 1 新增和修改

xiaoming['408'] = 120
xiaoming['408'] = 125  #这里是修改
xiaoming.setdefault('408',130)  #只会新增，不会修改
print(xiaoming)
xiaoming.update({'math':120,'english':110})
print(xiaoming)
print('-'*50)
# 2 查询
print(xiaoming['math'])
print(xiaoming.get('math1'))  #如果key不存在，程序不会崩
for key in xiaoming:  #默认是key
    print(key)

for v in xiaoming.values():
    print(v)

for i in xiaoming.items():
    print(i)
print('-'*50)
# print(xiaoming.fromkeys({'408':5}))  #没啥用
print('-'*50)



#3 删除
del xiaoming['math']
print(xiaoming)
xiaoming.pop('english')
print(xiaoming)
xiaoming.popitem()  #随机删除
print(xiaoming)
xiaoming.clear()
print(xiaoming)

str1='hello'
str1.split()