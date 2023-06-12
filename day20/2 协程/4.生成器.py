# 作者: 王道 龙哥
# 2022年03月08日15时18分18秒
# 含有yield的函数称为生成器
def fib(n):
    current = 0
    num1, num2 = 0, 1
    while current < n:
        num = num1
        num1, num2 = num2, num1 + num2
        current += 1
        # print(num,end=' ')
        yield num
    return 'done'

# F是一个生成器，支持next
F=fib(10)
for i in fib(10):
    print(i,end=' ')
print()
for i in fib(10):
    print(i,end=' ')


# l=[ i for i in F ]
# print(l)