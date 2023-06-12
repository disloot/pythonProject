#!/usr/bin/python
# author luke
# 2022年02月22日

def sum(n):
    # 结束条件写在return之前
    if 1 == n:
        return 1
    return n + sum(n - 1)


def step(n):
    if n <= 2:
        return n
    return step(n - 1) + step(n - 2)


if __name__ == '__main__':
    for i in range(1, 10):
        print(step(i), end=' ')
    print()
