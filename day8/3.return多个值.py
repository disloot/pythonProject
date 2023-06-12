  #!/usr/bin/python
# author luke
# 2022年02月22日

# return返回多个值时，加与不加括号都是一个元组
def measure():
    """返回当前的温度"""

    print("开始测量...")
    temp = 39
    wetness = 10
    print("测量结束...")

    return temp,wetness


if __name__ == '__main__':
    temp, wetness = measure()
    print(temp, wetness)
