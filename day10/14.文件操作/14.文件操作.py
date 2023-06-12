# author luke
# 2022年02月24日
import os
def use_open():
    # python 以下面形式打开，默认是打开文本文件
    file = open('dir/file.txt',mode='r', encoding='utf8')
    # 读取
    text = file.read()
    print(text)
    text = file.read() #读到文件结尾，再读会得到空字符串
    print(text)
    # 关闭
    file.close()

def use_write():
    # python 以下面形式打开，默认是打开文本文件
    file = open('dir/file.txt',mode='a+', encoding='utf8')
    # 写入
    file.write('ABC')
    # 关闭
    file.close()

def use_readline():
    # python 以下面形式打开，默认是打开文本文件
    file = open('dir/file.txt', mode='r+', encoding='utf8')
    # 写入
    while True:
        text=file.readline()
        if not text: #文件读结束了
            break
        print(text,end='')
    # 关闭
    file.close()

#使用seek对位置指针进行偏移
def use_seek():
    file = open('dir/file.txt', mode='r+', encoding='utf8')
    #写入
    file.write('hello123')
    file.seek(2)
    text=file.read()
    print(text)
    file.close()

# 二进制模式打开得到的是字节流，二进制模式下磁盘上存的是什么字符，直接拿出来
# 文本模式下，\r\n 拿出来是\n
def open_binary_file():
    file = open('dir/file1.txt', mode='w+',encoding='utf8')
    # text=file.read()
    file.write('hello\nworld')
    file.close()

if __name__ == '__main__':
    # use_open()
    # use_write()
    # use_readline()
    # use_seek()
    open_binary_file()