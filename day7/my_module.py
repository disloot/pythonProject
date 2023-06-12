name = "ly"
print("module")
print(id(name))

b = 1
def print_line():
    print('*' * 50)
    print("print_line:")
    x = b
    print(x)


# if __name__ == '__main__':  为了实现一切皆模块
if __name__ == '__main__':

    b += 1
    print(name)
    name = 'xiongda'  # 虽然是全局变量，但是对外不可见
    print(id(name))
    print(__name__)
