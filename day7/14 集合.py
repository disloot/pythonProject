#!/usr/bin/python
# author luke
# 2022年02月21日

dict1= {}

print(type(dict1))

set1=set()  #空集合的定义方法

# 集合里边的元素必须唯一
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
print(fruits)

fruits.discard('apple')
print(fruits)