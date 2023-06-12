# 作者: 王道 龙哥
# 2022年03月08日16时03分14秒
def gen():
    i=0
    while i<5:
        temp=yield i
        print(temp)
        i+=1

g=gen()

print(next(g))
print(g.send('hello'))